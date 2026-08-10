'''
Driver for Vaunix Lab Brick LDA variable digital attenuators over USB.

Developed against an LDA-908V (200-8000 MHz, 90 dB range, 0.1 dB step, single
channel), but every limit is queried from the device at connect() time, so the
multi-channel LDA-908V-2/-4/-8/-N variants and other LDA models work too.

The LDA presents a native USB HID interface -- there is no virtual COM port, so
this is a ctypes wrapper around Vaunix's VNX_atten64.dll rather than a serial
driver. The Ethernet port on the same physical unit speaks a completely different
API and is handled by Vaunix_LDA_Ethernet_Driver.py; see that file's docstring.

Attenuation is always exchanged with the DLL through the "...HR" entry points, in
0.05 dB counts. See Vaunix_LDA_Constants for why the 0.25 dB variants are never
called.

Two things in the vendor SDK are wrong or misleading, both verified against the
export table of VNX_atten64.dll:

  * fnLDA_perror is NOT exported. It is a local helper defined inside each demo
    .cpp file. Error text comes from Vaunix_LDA_Constants.USB_STATUS_NAMES.
  * fnLDA_GetChannel does NOT exist on USB, only fnLDA_SetChannel. The active
    channel is therefore tracked in software, seeded by an explicit
    fnLDA_SetChannel(devid, 1) during connect().

Typical use:

    from photonicdrivers.Variable_Digital_Attenautor.Vaunix_LDA_USB_Driver import Vaunix_LDA_USB_Driver

    for info in Vaunix_LDA_USB_Driver.list_usb_devices():
        print(info.serial_number, info.model_name)

    with Vaunix_LDA_USB_Driver(serial_number=29411) as attenuator:
        attenuator.set_frequency_MHz(6000)
        attenuator.set_attenuation_dB(31.5)
        print(attenuator.get_attenuation_dB())
'''

from __future__ import annotations

import ctypes
import functools
import os
import threading
import time
from ctypes import POINTER, c_bool, c_char_p, c_int, c_uint, c_ulonglong, create_string_buffer
from dataclasses import dataclass
from typing import Callable, Optional, Sequence

from photonicdrivers.Abstract.Connectable import Connectable
from photonicdrivers.Variable_Digital_Attenautor.Vaunix_LDA_Constants import (
    DEV_CONNECTED,
    DEV_OPENED,
    DEVICE_NOT_READY,
    HAS_BIDIR_RAMPS,
    HAS_MCHANNELS,
    HAS_PROFILES,
    MAXDEVICES,
    PROFILE_OFF,
    PROFILE_ONCE,
    PROFILE_REPEAT,
    PROFILE_ACTIVE,
    SWP_ACTIVE,
    USB_STATUS_NAMES,
    Vaunix_LDA_Error,
    Vaunix_LDA_Feature_Error,
    Vaunix_LDA_Transport_Error,
    counts_to_db,
    counts_to_mhz,
    db_to_counts,
    describe_features,
    mhz_to_counts,
    round_half_up,
    u32,
)

# DEVID is "unsigned int" in VNX_LDA_api.h. The vendor Python example allocates a
# signed array for fnLDA_GetDevInfo, which is a latent bug -- use the real type.
DEVID = c_uint
PDEVID = POINTER(c_uint)

IS_64BIT = ctypes.sizeof(ctypes.c_void_p) == 8

# Location of the DLL inside the SDK drop that ships alongside this driver.
_SDK_RELATIVE_DIR = os.path.join(
    "LDA_SDK_06-08-2026", "LDA_SDK_06-08-2026", "Windows SDK", "USB", "USB",
)
_DLL_NAME = "VNX_atten64.dll" if IS_64BIT else "VNX_atten.dll"
_DLL_SUBDIR = "x64" if IS_64BIT else "Win32"

# The DLL keeps a process-global device table and starts a read thread per opened
# device, so all driver instances in one process must share a single bound API.
_API_CACHE: dict[str, "_LDA_USB_Api"] = {}
_API_CACHE_LOCK = threading.Lock()


@dataclass
class Vaunix_LDA_Device_Info:
    '''
    Everything the driver learns about a unit at connect() time. Fields that do
    not apply to USB are left as None.
    '''

    model_name: str
    serial_number: int
    connection_type: str
    device_id: Optional[int]
    ip_address: Optional[str]
    software_version: Optional[str]
    dll_version: str
    number_of_channels: int
    features: int
    min_attenuation_dB: float
    max_attenuation_dB: float
    attenuation_step_dB: float
    min_frequency_MHz: float
    max_frequency_MHz: float
    profile_max_length: int


def default_dll_path() -> str:
    '''
    Absolute path to the bundled VNX_atten DLL matching this interpreter's bitness.
    '''
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        _SDK_RELATIVE_DIR,
        _DLL_SUBDIR,
        "Release",
        _DLL_NAME,
    )


def usb_checked(result: int, context: str) -> int:
    '''
    Validate a return value from the USB DLL, covering both of its conventions.

    Set functions return LVSTATUS: STATUS_OK (0), or an error code with bit 31 set.
    Get functions return the requested value, or an error code with bit 31 set.
    Every legal value is a small non-negative integer (the largest is 80000
    frequency counts), so "bit 31 set" discriminates errors for both conventions.

    Note that 0 is a perfectly legal getter result -- fnLDA_GetRF_On returns 0 when
    the RF path is off and fnLDA_GetMinAttenuationHR returns 0 on an LDA-908V --
    so this must never be tightened to a "result <= 0" test.
    '''
    code = u32(result)
    if code & 0x80000000:
        description = USB_STATUS_NAMES.get(code, f"unknown status 0x{code:08X}")
        raise Vaunix_LDA_Error(f"{context}: {description}")
    return result


def _retry_while_not_ready(
    call: Callable[[], int], context: str, attempts: int = 3, delay_s: float = 0.1
) -> int:
    '''
    Call a DLL getter, retrying only on DEVICE_NOT_READY.

    fnLDA_InitDevice spawns a read thread that populates the DLL's cached copy of
    the device parameters, so the first reads after opening can legitimately fail
    with DEVICE_NOT_READY. Any other error is raised immediately.
    '''
    result = 0
    for attempt in range(attempts):
        result = call()
        if u32(result) != DEVICE_NOT_READY:
            return usb_checked(result, context)
        if attempt < attempts - 1:
            time.sleep(delay_s)
    return usb_checked(result, context)


def _locked(method):
    '''
    Serialise a public method on the driver's reentrant lock.

    Selecting a channel and then reading or writing it is a read-modify-write pair,
    and the DLL runs its own read thread, so two Python threads interleaving would
    silently address the wrong channel.
    '''

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        with self._lock:
            return method(self, *args, **kwargs)

    return wrapper


class _LDA_USB_Api:
    '''
    ctypes binding for VNX_atten64.dll. One instance per DLL path per process.
    '''

    def __init__(self, dll_path: str) -> None:
        self.dll_path = os.path.abspath(dll_path)
        if not os.path.isfile(self.dll_path):
            raise Vaunix_LDA_Error(
                f"Vaunix USB DLL not found at {self.dll_path}. Extract the LDA SDK zip next to "
                f"this driver, or pass dll_path= pointing at {_DLL_NAME}."
            )
        try:
            # The DLL's own dependencies resolve from its directory.
            os.add_dll_directory(os.path.dirname(self.dll_path))
        except (OSError, AttributeError):
            pass
        try:
            # These exports are __cdecl, so CDLL. WinDLL would assume stdcall and
            # corrupt the stack on 32-bit.
            self._dll = ctypes.CDLL(self.dll_path, winmode=0)
        except OSError as error:
            raise Vaunix_LDA_Error(
                f"Could not load {self.dll_path}. This is {'64' if IS_64BIT else '32'}-bit Python, "
                f"which needs {_DLL_NAME}; a bitness mismatch is the usual cause. Original error: {error}"
            ) from error

        self._bind_functions()

        # Must precede any enumeration: if test mode is left on, the DLL invents
        # two simulated attenuators and every reading is fiction.
        self._test_mode = False
        self.set_test_mode(False)

    def _bind_functions(self) -> None:
        dll = self._dll

        # --- void returns. restype MUST be None, or ctypes reads a garbage int. ---
        self.SetTestMode = dll.fnLDA_SetTestMode
        self.SetTestMode.argtypes = [c_bool]
        self.SetTestMode.restype = None

        self.SetTraceLevel = dll.fnLDA_SetTraceLevel
        self.SetTraceLevel.argtypes = [c_int, c_int, c_bool]
        self.SetTraceLevel.restype = None

        # --- enumeration and identity ---
        self.GetNumDevices = dll.fnLDA_GetNumDevices
        self.GetNumDevices.argtypes = []
        self.GetNumDevices.restype = c_int

        self.GetDevInfo = dll.fnLDA_GetDevInfo
        self.GetDevInfo.argtypes = [PDEVID]
        self.GetDevInfo.restype = c_int

        # Second argument is an OUT buffer; a Python bytes/str here would hand the
        # DLL immutable refcounted memory. Returns a char count, not a status.
        self.GetModelNameA = dll.fnLDA_GetModelNameA
        self.GetModelNameA.argtypes = [DEVID, c_char_p]
        self.GetModelNameA.restype = c_int

        self.GetDLLVersion = dll.fnLDA_GetDLLVersion
        self.GetDLLVersion.argtypes = []
        self.GetDLLVersion.restype = c_int

        # --- [DEVID] -> int. Value, or an error code with bit 31 set. ---
        for name in (
            "GetSerialNumber", "InitDevice", "CloseDevice", "GetDeviceStatus",
            "GetNumChannels", "GetFeatures", "GetProfileMaxLength", "SaveSettings",
            "GetWorkingFrequency", "GetMinWorkingFrequency", "GetMaxWorkingFrequency",
            "GetAttenuationHR", "GetMinAttenuationHR", "GetMaxAttenuationHR", "GetMinAttenStepHR",
            "GetRampStartHR", "GetRampEndHR", "GetAttenuationStepHR", "GetAttenuationStepTwoHR",
            "GetDwellTime", "GetDwellTimeTwo", "GetIdleTime", "GetHoldTime",
            "GetRF_On",  # note the underscore
            "GetProfileCount", "GetProfileDwellTime", "GetProfileIdleTime", "GetProfileIndex",
        ):
            function = getattr(dll, "fnLDA_" + name)
            function.argtypes = [DEVID]
            function.restype = c_int
            setattr(self, name, function)

        # --- [DEVID, int] -> LVSTATUS ---
        for name in (
            "SetChannel", "SetWorkingFrequency", "SetAttenuationHR",
            "SetRampStartHR", "SetRampEndHR", "SetAttenuationStepHR", "SetAttenuationStepTwoHR",
            "SetDwellTime", "SetDwellTimeTwo", "SetIdleTime", "SetHoldTime",
            "SetProfileCount", "SetProfileIdleTime", "SetProfileDwellTime", "StartProfile",
        ):
            function = getattr(dll, "fnLDA_" + name)
            function.argtypes = [DEVID, c_int]
            function.restype = c_int
            setattr(self, name, function)

        # --- [DEVID, bool] -> LVSTATUS. MSVC bool is one byte; c_int works only by
        #     accident for 0/1 and is silently wrong for anything else. ---
        for name in ("SetRFOn", "SetRampDirection", "SetRampMode", "SetRampBidirectional", "StartRamp"):
            function = getattr(dll, "fnLDA_" + name)
            function.argtypes = [DEVID, c_bool]
            function.restype = c_int
            setattr(self, name, function)

        # --- [DEVID, int, int] ---
        self.SetAttenuationHRQ = dll.fnLDA_SetAttenuationHRQ
        self.SetAttenuationHRQ.argtypes = [DEVID, c_int, c_int]
        self.SetAttenuationHRQ.restype = c_int

        self.SetProfileElementHR = dll.fnLDA_SetProfileElementHR
        self.SetProfileElementHR.argtypes = [DEVID, c_int, c_int]
        self.SetProfileElementHR.restype = c_int

        self.GetProfileElementHR = dll.fnLDA_GetProfileElementHR
        self.GetProfileElementHR.argtypes = [DEVID, c_int]
        self.GetProfileElementHR.restype = c_int

        # --- 64-bit channel mask. c_int would push 4 bytes for an 8-byte parameter
        #     on 32-bit and misalign every later argument. ---
        self.SetAttenuationMCHR = dll.fnLDA_SetAttenuationMCHR
        self.SetAttenuationMCHR.argtypes = [DEVID, c_int, c_ulonglong]
        self.SetAttenuationMCHR.restype = c_int

        # --- The MC ramp/profile masks are plain ints, unlike SetAttenuationMCHR. ---
        for name in ("StartRampMC", "StartProfileMC"):
            function = getattr(dll, "fnLDA_" + name)
            function.argtypes = [DEVID, c_int, c_int, c_bool]
            function.restype = c_int
            setattr(self, name, function)

        # Deliberately not bound: fnLDA_perror, which does not exist in the DLL.

    def set_test_mode(self, enabled: bool) -> None:
        '''
        Turn the DLL's simulated-hardware mode on or off, remembering the choice so
        that enumerate_devices() re-asserts it rather than silently reverting.
        '''
        self._test_mode = bool(enabled)
        self.SetTestMode(self._test_mode)

    def enumerate_devices(self) -> list[tuple[int, int, str]]:
        '''
        Return [(device_id, serial_number, model_name), ...] without opening anything.
        '''
        # Re-assert the intended mode. The DLL treats this as global state that other
        # code in the process could have changed underneath us.
        self.SetTestMode(self._test_mode)
        usb_checked(self.GetNumDevices(), "fnLDA_GetNumDevices")

        # Size the buffer for MAXDEVICES rather than the count just returned:
        # fnLDA_GetDevInfo fills the DLL's whole active list, so a device plugged in
        # between the two calls would overrun a tightly-sized array. The vendor
        # Python example gets this wrong. 64 entries is 256 bytes.
        devids = (DEVID * MAXDEVICES)()
        filled = usb_checked(self.GetDevInfo(devids), "fnLDA_GetDevInfo")
        filled = max(0, min(int(filled), MAXDEVICES))

        devices = []
        for devid in devids[:filled]:
            # Both of these work on an un-opened device.
            serial = usb_checked(self.GetSerialNumber(devid), f"fnLDA_GetSerialNumber(devid={devid})")
            name_buffer = create_string_buffer(64)
            usb_checked(self.GetModelNameA(devid, name_buffer), f"fnLDA_GetModelNameA(devid={devid})")
            devices.append((int(devid), int(serial), name_buffer.value.decode("ascii", errors="replace")))
        return devices

    def get_dll_version_string(self) -> str:
        '''
        fnLDA_GetDLLVersion packs the version as BCD, e.g. 0x214 for version 2.14.
        '''
        raw = usb_checked(self.GetDLLVersion(), "fnLDA_GetDLLVersion")
        return f"{(raw >> 8) & 0xFF}.{raw & 0xFF:02d}"


def _get_api(dll_path: Optional[str]) -> _LDA_USB_Api:
    '''
    Return the process-wide bound API for this DLL, loading it on first use.
    '''
    path = os.path.normcase(os.path.abspath(dll_path or default_dll_path()))
    with _API_CACHE_LOCK:
        api = _API_CACHE.get(path)
        if api is None:
            api = _LDA_USB_Api(path)
            _API_CACHE[path] = api
        return api


def set_test_mode(enabled: bool, dll_path: Optional[str] = None) -> None:
    '''
    Switch the DLL between real hardware and its two simulated attenuators.

    Test mode is global to the DLL, not per device, so this affects every driver
    instance in the process. It is useful for exercising the ctypes binding end to
    end without hardware -- wrong argtypes show up here as an access violation,
    which is much easier to diagnose before a real device is involved.

    Call it before constructing a driver or calling list_usb_devices().
    '''
    _get_api(dll_path).set_test_mode(enabled)


class Vaunix_LDA_USB_Driver(Connectable):
    '''
    Vaunix Lab Brick LDA variable digital attenuator over USB.

    Channels are 1-indexed, matching the vendor API. Attenuation is in dB,
    frequency in MHz, and ramp/profile times in milliseconds.
    '''

    def __init__(
        self,
        serial_number: Optional[int] = None,
        device_id: Optional[int] = None,
        dll_path: Optional[str] = None,
        attenuation_step_dB: float = 0.1,
    ) -> None:
        '''
        Args:
            serial_number: Serial number of the attenuator, as printed on the unit
                and reported by list_usb_devices(). This is the stable identifier
                and the preferred way to select a device.
            device_id: The DLL's DEVID, as an escape hatch when two units somehow
                report the same serial. DEVIDs are reassigned when a device is
                replugged, so never store one between sessions.
            dll_path: Override for the bundled VNX_atten DLL.
            attenuation_step_dB: Fallback hardware step used for quantisation if
                the device does not report one. The LDA-908V steps in 0.1 dB.
        '''
        if serial_number is None and device_id is None:
            raise ValueError("Vaunix_LDA_USB_Driver requires either serial_number or device_id")

        self.connectionType = "USB"
        self.serial_number = None if serial_number is None else int(serial_number)
        self.device_id = None if device_id is None else int(device_id)
        self.dll_path = dll_path
        self.fallback_step_dB = float(attenuation_step_dB)

        self._lock = threading.RLock()
        self._api: Optional[_LDA_USB_Api] = None
        self._devid: Optional[int] = None

        # Populated by connect(); all limits come from the device, not the datasheet.
        self._model_name = ""
        self._features = 0
        self._num_channels = 1
        self._active_channel = 1
        self._min_atten_counts = 0
        self._max_atten_counts = 0
        self._step_counts = max(1, db_to_counts(self.fallback_step_dB))
        self._min_freq_counts = 0
        self._max_freq_counts = 0
        self._profile_max_length = 0

    # ==================== static discovery ====================

    @staticmethod
    def list_usb_devices(dll_path: Optional[str] = None) -> list[Vaunix_LDA_Device_Info]:
        '''
        Enumerate every LDA attached by USB, without opening any of them.

        Only the fields available before a device is opened are filled in; the
        others are left at zero. Use get_device_info() on a connected driver for
        the complete picture.
        '''
        api = _get_api(dll_path)
        dll_version = api.get_dll_version_string()
        return [
            Vaunix_LDA_Device_Info(
                model_name=model_name,
                serial_number=serial,
                connection_type="USB",
                device_id=devid,
                ip_address=None,
                software_version=None,
                dll_version=dll_version,
                number_of_channels=0,
                features=0,
                min_attenuation_dB=0.0,
                max_attenuation_dB=0.0,
                attenuation_step_dB=0.0,
                min_frequency_MHz=0.0,
                max_frequency_MHz=0.0,
                profile_max_length=0,
            )
            for devid, serial, model_name in api.enumerate_devices()
        ]

    # ==================== Connectable ====================

    @_locked
    def connect(self) -> None:
        '''
        Open the attenuator and cache its limits. Idempotent.
        '''
        if self.is_connected():
            return

        self._api = _get_api(self.dll_path)
        self._resolve_and_open()
        self._cache_device_limits()

    @_locked
    def disconnect(self) -> None:
        '''
        Close the attenuator. Idempotent, and never raises -- a failed close must
        not leave the object claiming to still be connected, or the handle leaks
        and the next process cannot open the device at all.
        '''
        if self._api is None or self._devid is None:
            self._devid = None
            return
        try:
            usb_checked(self._api.CloseDevice(self._devid), f"fnLDA_CloseDevice(devid={self._devid})")
        except Exception as error:
            print(f"WARNING in Vaunix_LDA_USB_Driver.disconnect: {error}")
        finally:
            self._devid = None

    def is_connected(self) -> bool:
        '''
        True if the device is open and still physically present.

        Costs no device I/O: fnLDA_GetDeviceStatus reads the DLL's cached state,
        which its read thread maintains.
        '''
        if self._api is None or self._devid is None:
            return False
        try:
            status = self._api.GetDeviceStatus(self._devid)
            if u32(status) & 0x80000000:
                return False
            # DEV_OPENED alone is not enough: a device that was unplugged without
            # being closed keeps DEV_OPENED set while DEV_CONNECTED clears.
            return bool(status & DEV_CONNECTED) and bool(status & DEV_OPENED)
        except Exception:
            return False

    def __enter__(self) -> "Vaunix_LDA_USB_Driver":
        self.connect()
        return self

    def __exit__(self, exception_type, exception, traceback) -> None:
        self.disconnect()

    # ==================== identity ====================

    @_locked
    def get_device_info(self) -> Vaunix_LDA_Device_Info:
        '''
        Snapshot of the connected unit's identity and limits.
        '''
        self._require_connected("get_device_info")
        return Vaunix_LDA_Device_Info(
            model_name=self._model_name,
            serial_number=self.get_serial_number(),
            connection_type="USB",
            device_id=self._devid,
            ip_address=None,
            software_version=None,
            dll_version=self._api.get_dll_version_string(),
            number_of_channels=self._num_channels,
            features=self._features,
            min_attenuation_dB=self.get_min_attenuation_dB(),
            max_attenuation_dB=self.get_max_attenuation_dB(),
            attenuation_step_dB=self.get_attenuation_step_dB(),
            min_frequency_MHz=self.get_min_frequency_MHz(),
            max_frequency_MHz=self.get_max_frequency_MHz(),
            profile_max_length=self._profile_max_length,
        )

    def get_model_name(self) -> str:
        '''
        Model string reported by the device, e.g. "LDA-908V".
        '''
        self._require_connected("get_model_name")
        return self._model_name

    @_locked
    def get_serial_number(self) -> int:
        '''
        Serial number reported by the device.
        '''
        return int(self._call_get(self._api.GetSerialNumber, "fnLDA_GetSerialNumber"))

    def get_connection_type(self) -> str:
        '''
        Always "USB" for this driver.
        '''
        return self.connectionType

    @_locked
    def get_dll_version(self) -> str:
        '''
        Version of the loaded VNX_atten DLL, e.g. "2.14".
        '''
        self._require_connected("get_dll_version")
        return self._api.get_dll_version_string()

    def get_features(self) -> int:
        '''
        Raw fnLDA_GetFeatures bitfield. Use the HAS_* constants to test it.
        '''
        self._require_connected("get_features")
        return self._features

    # ==================== channels ====================

    def get_number_of_channels(self) -> int:
        '''
        Number of attenuator channels. 1 on a base LDA-908V.
        '''
        self._require_connected("get_number_of_channels")
        return self._num_channels

    def get_channel(self) -> int:
        '''
        The currently selected channel.

        The USB DLL exports no fnLDA_GetChannel, so this is the driver's own
        tracked value. It is seeded by an explicit fnLDA_SetChannel(1) during
        connect() and updated on every channel change, so it is accurate unless
        another process moves the channel behind this driver's back.
        '''
        self._require_connected("get_channel")
        return self._active_channel

    @_locked
    def set_channel(self, channel: int) -> None:
        '''
        Select the channel that subsequent per-channel calls act on.

        Args:
            channel: 1-based channel number.
        '''
        self._require_connected("set_channel")
        self._select_channel(self._validated_channel(channel))

    # ==================== attenuation ====================

    @_locked
    def get_attenuation_dB(self, channel: Optional[int] = None) -> float:
        '''
        Read the attenuation currently applied.

        Neither DLL has a channel-qualified getter, so passing `channel` selects
        that channel first and LEAVES IT SELECTED. Restoring the previous channel
        would cost another round trip that could itself fail, leaving the channel
        indeterminate, so the selection is deliberately left where the caller put it.

        Args:
            channel: 1-based channel to read; None reads the selected channel.

        Returns:
            Attenuation in dB.
        '''
        if channel is not None:
            self._select_channel(self._validated_channel(channel))
        counts = self._call_get(self._api.GetAttenuationHR, "fnLDA_GetAttenuationHR")
        return counts_to_db(counts)

    @_locked
    def set_attenuation_dB(self, attenuation_dB: float, channel: Optional[int] = None) -> None:
        '''
        Set the attenuation.

        Values off the hardware step grid are quantised silently (the residual is
        at most half a step). Values outside the device's range raise ValueError
        rather than being clamped: silently applying 90 dB to a 120 dB request
        would produce a plausible but wrong measurement with no trace in the data.

        Args:
            attenuation_dB: Requested attenuation in dB.
            channel: 1-based channel to set; None uses the selected channel.
        '''
        self._require_connected("set_attenuation_dB")
        counts = self._quantize_attenuation_counts(attenuation_dB)

        if channel is None:
            usb_checked(
                self._api.SetAttenuationHR(self._devid, counts),
                f"fnLDA_SetAttenuationHR(devid={self._devid}, counts={counts})",
            )
            return

        # The channel-qualified call is atomic, so it cannot be interleaved with
        # another thread's channel change the way SetChannel + SetAttenuation can.
        validated = self._validated_channel(channel)
        usb_checked(
            self._api.SetAttenuationHRQ(self._devid, counts, validated),
            f"fnLDA_SetAttenuationHRQ(devid={self._devid}, counts={counts}, channel={validated})",
        )
        # This entry point leaves the channel set to whatever it was called with.
        self._active_channel = validated

    def get_min_attenuation_dB(self) -> float:
        '''
        Smallest attenuation the device accepts, in dB. 0.0 on an LDA-908V.
        '''
        self._require_connected("get_min_attenuation_dB")
        return counts_to_db(self._min_atten_counts)

    def get_max_attenuation_dB(self) -> float:
        '''
        Largest attenuation the device accepts, in dB. 90.0 on an LDA-908V.
        '''
        self._require_connected("get_max_attenuation_dB")
        return counts_to_db(self._max_atten_counts)

    def get_attenuation_step_dB(self) -> float:
        '''
        Hardware attenuation step, in dB. 0.1 on an LDA-908V.

        Note that the API unit is 0.05 dB, finer than the hardware step, so
        setpoints are quantised to a multiple of this value.
        '''
        self._require_connected("get_attenuation_step_dB")
        return counts_to_db(self._step_counts)

    @_locked
    def set_attenuation_multichannel_dB(self, attenuation_dB: float, channels: Sequence[int]) -> None:
        '''
        Set the same attenuation on several channels in one command.

        Args:
            attenuation_dB: Requested attenuation in dB.
            channels: 1-based channel numbers.
        '''
        self._require_connected("set_attenuation_multichannel_dB")
        self._require_feature(HAS_MCHANNELS, "HAS_MCHANNELS", "set_attenuation_multichannel_dB")
        if not channels:
            raise ValueError("channels must contain at least one channel number")

        counts = self._quantize_attenuation_counts(attenuation_dB)
        mask = 0
        for channel in channels:
            mask |= 1 << (self._validated_channel(channel) - 1)
        usb_checked(
            self._api.SetAttenuationMCHR(self._devid, counts, mask),
            f"fnLDA_SetAttenuationMCHR(devid={self._devid}, counts={counts}, chmask=0x{mask:X})",
        )

    # ==================== working frequency ====================

    @_locked
    def get_frequency_MHz(self) -> float:
        '''
        The working frequency the attenuation calibration is applied at, in MHz.
        '''
        counts = self._call_get(self._api.GetWorkingFrequency, "fnLDA_GetWorkingFrequency")
        return counts_to_mhz(counts)

    @_locked
    def set_frequency_MHz(self, frequency_MHz: float) -> None:
        '''
        Set the working frequency used to select the internal calibration table.

        This does not generate anything -- the LDA is a passive attenuator. Setting
        it to the frequency actually passing through the device makes the applied
        attenuation accurate across the 200-8000 MHz band.

        Args:
            frequency_MHz: Working frequency in MHz.
        '''
        self._require_connected("set_frequency_MHz")
        counts = self._quantize_frequency_counts(frequency_MHz)
        usb_checked(
            self._api.SetWorkingFrequency(self._devid, counts),
            f"fnLDA_SetWorkingFrequency(devid={self._devid}, counts={counts})",
        )

    def get_min_frequency_MHz(self) -> float:
        '''
        Lowest calibrated frequency, in MHz. 200.0 on an LDA-908V.
        '''
        self._require_connected("get_min_frequency_MHz")
        return counts_to_mhz(self._min_freq_counts)

    def get_max_frequency_MHz(self) -> float:
        '''
        Highest calibrated frequency, in MHz. 8000.0 on an LDA-908V.
        '''
        self._require_connected("get_max_frequency_MHz")
        return counts_to_mhz(self._max_freq_counts)

    # ==================== RF path ====================

    @_locked
    def get_rf_on(self) -> bool:
        '''
        True if the RF path is enabled.
        '''
        return bool(self._call_get(self._api.GetRF_On, "fnLDA_GetRF_On"))

    @_locked
    def set_rf_on(self, enabled: bool) -> None:
        '''
        Enable or disable the RF path.
        '''
        self._set_bool(self._api.SetRFOn, "fnLDA_SetRFOn", enabled)

    # ==================== ramp ====================

    @_locked
    def get_ramp_start_dB(self) -> float:
        '''
        Attenuation the ramp starts from, in dB.
        '''
        return counts_to_db(self._call_get(self._api.GetRampStartHR, "fnLDA_GetRampStartHR"))

    @_locked
    def set_ramp_start_dB(self, attenuation_dB: float) -> None:
        '''
        Set the attenuation the ramp starts from.
        '''
        self._set_attenuation_like(self._api.SetRampStartHR, "fnLDA_SetRampStartHR", attenuation_dB)

    @_locked
    def get_ramp_end_dB(self) -> float:
        '''
        Attenuation the ramp ends at, in dB.
        '''
        return counts_to_db(self._call_get(self._api.GetRampEndHR, "fnLDA_GetRampEndHR"))

    @_locked
    def set_ramp_end_dB(self, attenuation_dB: float) -> None:
        '''
        Set the attenuation the ramp ends at.

        An upward ramp requires the end to be above the start.
        '''
        self._set_attenuation_like(self._api.SetRampEndHR, "fnLDA_SetRampEndHR", attenuation_dB)

    @_locked
    def get_ramp_step_dB(self) -> float:
        '''
        Attenuation increment per ramp step, in dB.
        '''
        return counts_to_db(self._call_get(self._api.GetAttenuationStepHR, "fnLDA_GetAttenuationStepHR"))

    @_locked
    def set_ramp_step_dB(self, step_dB: float) -> None:
        '''
        Set the attenuation increment per ramp step.
        '''
        self._set_step_like(self._api.SetAttenuationStepHR, "fnLDA_SetAttenuationStepHR", step_dB)

    @_locked
    def get_ramp_step_two_dB(self) -> float:
        '''
        Attenuation increment for the second phase of a bidirectional ramp, in dB.
        '''
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "get_ramp_step_two_dB")
        return counts_to_db(self._call_get(self._api.GetAttenuationStepTwoHR, "fnLDA_GetAttenuationStepTwoHR"))

    @_locked
    def set_ramp_step_two_dB(self, step_dB: float) -> None:
        '''
        Set the attenuation increment for the second phase of a bidirectional ramp.
        '''
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "set_ramp_step_two_dB")
        self._set_step_like(self._api.SetAttenuationStepTwoHR, "fnLDA_SetAttenuationStepTwoHR", step_dB)

    @_locked
    def get_ramp_dwell_time_ms(self) -> int:
        '''
        Time spent at each ramp step, in milliseconds.
        '''
        return int(self._call_get(self._api.GetDwellTime, "fnLDA_GetDwellTime"))

    @_locked
    def set_ramp_dwell_time_ms(self, dwell_time_ms: int) -> None:
        '''
        Set the time spent at each ramp step. The hardware minimum is 1 ms.
        '''
        self._set_time(self._api.SetDwellTime, "fnLDA_SetDwellTime", dwell_time_ms, minimum_ms=1)

    @_locked
    def get_ramp_dwell_time_two_ms(self) -> int:
        '''
        Dwell time for the second phase of a bidirectional ramp, in milliseconds.
        '''
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "get_ramp_dwell_time_two_ms")
        return int(self._call_get(self._api.GetDwellTimeTwo, "fnLDA_GetDwellTimeTwo"))

    @_locked
    def set_ramp_dwell_time_two_ms(self, dwell_time_ms: int) -> None:
        '''
        Set the dwell time for the second phase of a bidirectional ramp.
        '''
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "set_ramp_dwell_time_two_ms")
        self._set_time(self._api.SetDwellTimeTwo, "fnLDA_SetDwellTimeTwo", dwell_time_ms, minimum_ms=1)

    @_locked
    def get_ramp_idle_time_ms(self) -> int:
        '''
        Idle time between repeats of a continuous ramp, in milliseconds.
        '''
        return int(self._call_get(self._api.GetIdleTime, "fnLDA_GetIdleTime"))

    @_locked
    def set_ramp_idle_time_ms(self, idle_time_ms: int) -> None:
        '''
        Set the idle time between repeats of a continuous ramp.
        '''
        self._set_time(self._api.SetIdleTime, "fnLDA_SetIdleTime", idle_time_ms, minimum_ms=0)

    @_locked
    def get_ramp_hold_time_ms(self) -> int:
        '''
        Hold time at the ramp end before the second phase, in milliseconds.
        '''
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "get_ramp_hold_time_ms")
        return int(self._call_get(self._api.GetHoldTime, "fnLDA_GetHoldTime"))

    @_locked
    def set_ramp_hold_time_ms(self, hold_time_ms: int) -> None:
        '''
        Set the hold time at the ramp end before the second phase begins.
        '''
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "set_ramp_hold_time_ms")
        self._set_time(self._api.SetHoldTime, "fnLDA_SetHoldTime", hold_time_ms, minimum_ms=0)

    @_locked
    def set_ramp_direction(self, up: bool) -> None:
        '''
        Set the ramp direction. True ramps from start up to end, which requires
        start to be below end.
        '''
        self._set_bool(self._api.SetRampDirection, "fnLDA_SetRampDirection", up)

    @_locked
    def set_ramp_repeat(self, repeat: bool) -> None:
        '''
        True makes the ramp repeat continuously, False plays it once per start_ramp().
        '''
        self._set_bool(self._api.SetRampMode, "fnLDA_SetRampMode", repeat)

    @_locked
    def set_ramp_bidirectional(self, enabled: bool) -> None:
        '''
        Enable a two-phase ramp that runs back down after reaching the end.
        '''
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "set_ramp_bidirectional")
        self._set_bool(self._api.SetRampBidirectional, "fnLDA_SetRampBidirectional", enabled)

    @_locked
    def start_ramp(self) -> None:
        '''
        Start the ramp with the currently configured parameters.
        '''
        self._set_bool(self._api.StartRamp, "fnLDA_StartRamp", True)

    @_locked
    def stop_ramp(self) -> None:
        '''
        Stop a running ramp.
        '''
        self._set_bool(self._api.StartRamp, "fnLDA_StartRamp", False)

    @_locked
    def start_ramp_multichannel(self, channels: Sequence[int], repeat: bool = False,
                                deferred: bool = False) -> None:
        '''
        Start ramps on several channels at once.

        Args:
            channels: 1-based channel numbers.
            repeat: True to ramp continuously.
            deferred: True to arm the ramps without starting them immediately.
        '''
        self._require_connected("start_ramp_multichannel")
        self._require_feature(HAS_MCHANNELS, "HAS_MCHANNELS", "start_ramp_multichannel")
        if not channels:
            raise ValueError("channels must contain at least one channel number")

        mask = 0
        for channel in channels:
            mask |= 1 << (self._validated_channel(channel) - 1)
        mode = 2 if repeat else 1
        usb_checked(
            self._api.StartRampMC(self._devid, mode, mask, bool(deferred)),
            f"fnLDA_StartRampMC(devid={self._devid}, mode={mode}, chmask=0x{mask:X}, deferred={deferred})",
        )

    @_locked
    def is_ramping(self) -> bool:
        '''
        True while a ramp is running.
        '''
        return bool(self.get_device_status() & SWP_ACTIVE)

    # ==================== profile ====================

    def get_profile_max_length(self) -> int:
        '''
        Number of attenuation points the device's profile memory holds.
        '''
        self._require_connected("get_profile_max_length")
        return self._profile_max_length

    @_locked
    def get_profile_count(self) -> int:
        '''
        Number of profile points that will actually be played.
        '''
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "get_profile_count")
        return int(self._call_get(self._api.GetProfileCount, "fnLDA_GetProfileCount"))

    @_locked
    def set_profile_count(self, count: int) -> None:
        '''
        Set how many profile points are played.

        Args:
            count: Number of points, from 1 to get_profile_max_length().
        '''
        self._require_connected("set_profile_count")
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "set_profile_count")
        count = int(count)
        if not 1 <= count <= self._profile_max_length:
            raise ValueError(
                f"profile count={count} is outside [1, {self._profile_max_length}] "
                f"for {self._model_name} serial {self.serial_number}"
            )
        usb_checked(
            self._api.SetProfileCount(self._devid, count),
            f"fnLDA_SetProfileCount(devid={self._devid}, count={count})",
        )

    @_locked
    def get_profile_element_dB(self, index: int) -> float:
        '''
        Read one profile point.

        Args:
            index: 0-based index into the profile.
        '''
        self._require_connected("get_profile_element_dB")
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "get_profile_element_dB")
        validated = self._validated_profile_index(index)
        counts = usb_checked(
            self._api.GetProfileElementHR(self._devid, validated),
            f"fnLDA_GetProfileElementHR(devid={self._devid}, index={validated})",
        )
        return counts_to_db(counts)

    @_locked
    def set_profile_element_dB(self, index: int, attenuation_dB: float) -> None:
        '''
        Write one profile point.

        Args:
            index: 0-based index into the profile.
            attenuation_dB: Attenuation for that point, in dB.
        '''
        self._require_connected("set_profile_element_dB")
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "set_profile_element_dB")
        validated = self._validated_profile_index(index)
        counts = self._quantize_attenuation_counts(attenuation_dB)
        usb_checked(
            self._api.SetProfileElementHR(self._devid, validated, counts),
            f"fnLDA_SetProfileElementHR(devid={self._devid}, index={validated}, counts={counts})",
        )

    @_locked
    def set_profile_dB(self, attenuations_dB: Sequence[float]) -> None:
        '''
        Write a whole profile and set its length in one call.

        Args:
            attenuations_dB: Attenuation for each point, in dB, in play order.
        '''
        self._require_connected("set_profile_dB")
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "set_profile_dB")
        if not attenuations_dB:
            raise ValueError("attenuations_dB must contain at least one point")
        if len(attenuations_dB) > self._profile_max_length:
            raise ValueError(
                f"profile has {len(attenuations_dB)} points but {self._model_name} serial "
                f"{self.serial_number} holds at most {self._profile_max_length}"
            )
        for index, attenuation_dB in enumerate(attenuations_dB):
            self.set_profile_element_dB(index, attenuation_dB)
        self.set_profile_count(len(attenuations_dB))

    @_locked
    def get_profile_dwell_time_ms(self) -> int:
        '''
        Time spent at each profile point, in milliseconds.
        '''
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "get_profile_dwell_time_ms")
        return int(self._call_get(self._api.GetProfileDwellTime, "fnLDA_GetProfileDwellTime"))

    @_locked
    def set_profile_dwell_time_ms(self, dwell_time_ms: int) -> None:
        '''
        Set the time spent at each profile point. The hardware minimum is 1 ms.
        '''
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "set_profile_dwell_time_ms")
        self._set_time(self._api.SetProfileDwellTime, "fnLDA_SetProfileDwellTime", dwell_time_ms, minimum_ms=1)

    @_locked
    def get_profile_idle_time_ms(self) -> int:
        '''
        Idle time between repeats of a profile, in milliseconds.
        '''
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "get_profile_idle_time_ms")
        return int(self._call_get(self._api.GetProfileIdleTime, "fnLDA_GetProfileIdleTime"))

    @_locked
    def set_profile_idle_time_ms(self, idle_time_ms: int) -> None:
        '''
        Set the idle time between repeats of a profile.
        '''
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "set_profile_idle_time_ms")
        self._set_time(self._api.SetProfileIdleTime, "fnLDA_SetProfileIdleTime", idle_time_ms, minimum_ms=0)

    @_locked
    def get_profile_index(self) -> int:
        '''
        Index of the profile point currently being played.

        USB only -- the Ethernet DLL exports this symbol but does not implement it.
        '''
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "get_profile_index")
        return int(self._call_get(self._api.GetProfileIndex, "fnLDA_GetProfileIndex"))

    @_locked
    def start_profile(self, repeat: bool = False) -> None:
        '''
        Play the stored profile.

        Args:
            repeat: True to loop the profile until stop_profile(), False to play once.
        '''
        self._require_connected("start_profile")
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "start_profile")
        mode = PROFILE_REPEAT if repeat else PROFILE_ONCE
        usb_checked(
            self._api.StartProfile(self._devid, mode),
            f"fnLDA_StartProfile(devid={self._devid}, mode={mode})",
        )

    @_locked
    def stop_profile(self) -> None:
        '''
        Stop a playing profile.
        '''
        self._require_connected("stop_profile")
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "stop_profile")
        usb_checked(
            self._api.StartProfile(self._devid, PROFILE_OFF),
            f"fnLDA_StartProfile(devid={self._devid}, mode={PROFILE_OFF})",
        )

    @_locked
    def start_profile_multichannel(self, channels: Sequence[int], repeat: bool = False,
                                   delayed: bool = False) -> None:
        '''
        Play the stored profile on several channels at once.

        Args:
            channels: 1-based channel numbers.
            repeat: True to loop the profile.
            delayed: True to arm without starting immediately.
        '''
        self._require_connected("start_profile_multichannel")
        self._require_feature(HAS_MCHANNELS, "HAS_MCHANNELS", "start_profile_multichannel")
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "start_profile_multichannel")
        if not channels:
            raise ValueError("channels must contain at least one channel number")

        mask = 0
        for channel in channels:
            mask |= 1 << (self._validated_channel(channel) - 1)
        mode = PROFILE_REPEAT if repeat else PROFILE_ONCE
        usb_checked(
            self._api.StartProfileMC(self._devid, mode, mask, bool(delayed)),
            f"fnLDA_StartProfileMC(devid={self._devid}, mode={mode}, chmask=0x{mask:X}, delayed={delayed})",
        )

    @_locked
    def is_profile_playing(self) -> bool:
        '''
        True while a profile is playing.
        '''
        return bool(self.get_device_status() & PROFILE_ACTIVE)

    # ==================== Ethernet-only methods ====================

    def get_ip_address(self) -> str:
        '''
        Not available over USB. Use Vaunix_LDA_Ethernet_Driver.
        '''
        raise Vaunix_LDA_Transport_Error(
            "get_ip_address is not available over USB: VNX_atten64.dll exports no IP functions. "
            "Use Vaunix_LDA_Ethernet_Driver."
        )

    def get_netmask(self) -> str:
        '''
        Not available over USB. Use Vaunix_LDA_Ethernet_Driver.
        '''
        raise Vaunix_LDA_Transport_Error(
            "get_netmask is not available over USB: VNX_atten64.dll exports no IP functions."
        )

    def get_gateway(self) -> str:
        '''
        Not available over USB. Use Vaunix_LDA_Ethernet_Driver.
        '''
        raise Vaunix_LDA_Transport_Error(
            "get_gateway is not available over USB: VNX_atten64.dll exports no IP functions."
        )

    def get_ip_mode(self) -> str:
        '''
        Not available over USB. Use Vaunix_LDA_Ethernet_Driver.
        '''
        raise Vaunix_LDA_Transport_Error(
            "get_ip_mode is not available over USB: VNX_atten64.dll exports no IP functions."
        )

    def get_software_version(self) -> str:
        '''
        Not available over USB -- the USB DLL reports its own version, not the
        device firmware's. Use Vaunix_LDA_Ethernet_Driver, or get_dll_version().
        '''
        raise Vaunix_LDA_Transport_Error(
            "get_software_version is not available over USB: VNX_atten64.dll exports no "
            "fnLDA_GetSoftwareVersion. get_dll_version() returns the DLL version instead."
        )

    # ==================== persistence and diagnostics ====================

    @_locked
    def save_settings(self) -> None:
        '''
        Persist the current settings to the device's non-volatile memory so they
        are restored at power-on.
        '''
        self._call_get(self._api.SaveSettings, "fnLDA_SaveSettings")

    @_locked
    def get_device_status(self) -> int:
        '''
        Raw fnLDA_GetDeviceStatus bitfield. Test it with the DEV_*, SWP_* and
        PROFILE_ACTIVE constants.
        '''
        return int(self._call_get(self._api.GetDeviceStatus, "fnLDA_GetDeviceStatus"))

    @_locked
    def set_trace_level(self, trace_level: int, io_trace_level: int, verbose: bool) -> None:
        '''
        Set the DLL's debug tracing verbosity. Both levels run 0 (off) to 3.
        '''
        self._require_connected("set_trace_level")
        self._api.SetTraceLevel(int(trace_level), int(io_trace_level), bool(verbose))

    # ==================================================================
    #                          PRIVATE METHODS
    # ==================================================================

    def _resolve_and_open(self) -> None:
        '''
        Match the requested device, open it, and establish a known channel.
        '''
        found = self._api.enumerate_devices()

        if not found:
            raise Vaunix_LDA_Error(
                "No Vaunix LDA devices found on USB. Check that the device is powered and plugged "
                "in, that no other process is holding it open (the Vaunix GUI and another Python "
                f"session both claim the HID handle exclusively), and that the DLL bitness matches: "
                f"this is {'64' if IS_64BIT else '32'}-bit Python, which needs {_DLL_NAME}."
            )

        available = ", ".join(f"serial={s} (devid={d}, model={m})" for d, s, m in found)

        if self.device_id is not None:
            # DEVIDs are reassigned on replug, so verify rather than trusting it.
            matches = [entry for entry in found if entry[0] == self.device_id]
            if not matches:
                raise Vaunix_LDA_Error(
                    f"device_id={self.device_id} is not currently enumerated. Available: {available}. "
                    f"device_id values are volatile -- prefer serial_number."
                )
        else:
            matches = [entry for entry in found if entry[1] == self.serial_number]
            if not matches:
                raise Vaunix_LDA_Error(
                    f"No Vaunix LDA with serial_number={self.serial_number} found on USB. "
                    f"Available: {available}"
                )
            if len(matches) > 1:
                raise Vaunix_LDA_Error(
                    f"serial_number={self.serial_number} matched {len(matches)} enumerated devices "
                    f"(devids {[entry[0] for entry in matches]}). Serials are unique, so either the "
                    f"DLL enumerated one unit twice or two units share a serial. Refusing to guess "
                    f"which one to attenuate -- pass device_id= to select one explicitly."
                )

        devid, serial, model_name = matches[0]
        usb_checked(self._api.InitDevice(devid), f"fnLDA_InitDevice(devid={devid})")
        self._devid = devid
        self.serial_number = serial
        self._model_name = model_name

        # The DLL starts a read thread to populate its cached parameters, which is
        # not finished the instant InitDevice returns.
        time.sleep(0.1)

        status = usb_checked(self._api.GetDeviceStatus(devid), f"fnLDA_GetDeviceStatus(devid={devid})")
        if not status & DEV_OPENED:
            self._devid = None
            raise Vaunix_LDA_Error(
                f"fnLDA_InitDevice(devid={devid}) reported success but DEV_OPENED is clear "
                f"(status=0x{u32(status):08X})."
            )

        # There is no fnLDA_GetChannel on USB, so pin the channel to make the
        # software-tracked value truthful.
        usb_checked(self._api.SetChannel(devid, 1), f"fnLDA_SetChannel(devid={devid}, channel=1)")
        self._active_channel = 1

    def _cache_device_limits(self) -> None:
        '''
        Read the limits that range checks and quantisation depend on. Retries on
        DEVICE_NOT_READY, which is expected while the DLL's read thread starts up.
        '''
        self._features = int(self._call_get(self._api.GetFeatures, "fnLDA_GetFeatures"))
        self._num_channels = max(1, int(self._call_get(self._api.GetNumChannels, "fnLDA_GetNumChannels")))
        self._min_atten_counts = int(self._call_get(self._api.GetMinAttenuationHR, "fnLDA_GetMinAttenuationHR"))
        self._max_atten_counts = int(self._call_get(self._api.GetMaxAttenuationHR, "fnLDA_GetMaxAttenuationHR"))
        self._min_freq_counts = int(
            self._call_get(self._api.GetMinWorkingFrequency, "fnLDA_GetMinWorkingFrequency")
        )
        self._max_freq_counts = int(
            self._call_get(self._api.GetMaxWorkingFrequency, "fnLDA_GetMaxWorkingFrequency")
        )
        self._profile_max_length = int(
            self._call_get(self._api.GetProfileMaxLength, "fnLDA_GetProfileMaxLength")
        )

        step_counts = int(self._call_get(self._api.GetMinAttenStepHR, "fnLDA_GetMinAttenStepHR"))
        # A device that reports no step still needs a grid to quantise onto.
        self._step_counts = step_counts if step_counts > 0 else max(1, db_to_counts(self.fallback_step_dB))

        if self._max_atten_counts <= self._min_atten_counts:
            raise Vaunix_LDA_Error(
                f"{self._model_name} serial {self.serial_number} reported an empty attenuation range "
                f"[{self._min_atten_counts}, {self._max_atten_counts}] counts."
            )

    def _require_connected(self, method: str) -> None:
        if self._api is None or self._devid is None:
            raise Vaunix_LDA_Error(f"{method} requires an open connection -- call connect() first.")

    def _require_feature(self, bit: int, bit_name: str, method: str) -> None:
        self._require_connected(method)
        if not self._features & bit:
            raise Vaunix_LDA_Feature_Error(
                f"{method} requires {bit_name}, but {self._model_name} serial {self.serial_number} "
                f"reports features={describe_features(self._features)}."
            )

    def _call_get(self, function, context: str) -> int:
        '''
        Invoke a [DEVID] -> int getter with the not-ready retry applied.
        '''
        self._require_connected(context)
        devid = self._devid
        return _retry_while_not_ready(lambda: function(devid), f"{context}(devid={devid})")

    def _set_bool(self, function, context: str, value: bool) -> None:
        self._require_connected(context)
        usb_checked(
            function(self._devid, bool(value)),
            f"{context}(devid={self._devid}, value={bool(value)})",
        )

    def _set_attenuation_like(self, function, context: str, attenuation_dB: float) -> None:
        '''
        Set a parameter that shares the attenuation range, e.g. a ramp endpoint.
        '''
        self._require_connected(context)
        counts = self._quantize_attenuation_counts(attenuation_dB)
        usb_checked(function(self._devid, counts), f"{context}(devid={self._devid}, counts={counts})")

    def _set_step_like(self, function, context: str, step_dB: float) -> None:
        '''
        Set a ramp step size. A step is a difference, so it is quantised to the
        hardware grid but range-checked against the span rather than the endpoints.
        '''
        self._require_connected(context)
        span_counts = self._max_atten_counts - self._min_atten_counts
        counts = self._step_counts * round_half_up(db_to_counts(step_dB) / self._step_counts)
        if counts <= 0 or counts > span_counts:
            raise ValueError(
                f"step={step_dB} dB is outside (0, {counts_to_db(span_counts)}] dB for "
                f"{self._model_name} serial {self.serial_number}"
            )
        usb_checked(function(self._devid, counts), f"{context}(devid={self._devid}, counts={counts})")

    def _set_time(self, function, context: str, time_ms: int, minimum_ms: int) -> None:
        self._require_connected(context)
        time_ms = int(time_ms)
        if time_ms < minimum_ms:
            raise ValueError(f"{context} requires at least {minimum_ms} ms, got {time_ms}")
        usb_checked(function(self._devid, time_ms), f"{context}(devid={self._devid}, ms={time_ms})")

    def _select_channel(self, channel: int) -> None:
        '''
        Select a channel, skipping the call when it is already active.
        '''
        if channel == self._active_channel:
            return
        usb_checked(
            self._api.SetChannel(self._devid, channel),
            f"fnLDA_SetChannel(devid={self._devid}, channel={channel})",
        )
        self._active_channel = channel

    def _validated_channel(self, channel: int) -> int:
        self._require_connected("channel selection")
        channel = int(channel)
        if not 1 <= channel <= self._num_channels:
            raise ValueError(
                f"channel={channel} is outside [1, {self._num_channels}] for {self._model_name} "
                f"serial {self.serial_number}. Channels are 1-indexed."
            )
        return channel

    def _validated_profile_index(self, index: int) -> int:
        index = int(index)
        if not 0 <= index < self._profile_max_length:
            raise ValueError(
                f"profile index={index} is outside [0, {self._profile_max_length - 1}] for "
                f"{self._model_name} serial {self.serial_number}. Indices are 0-based."
            )
        return index

    def _quantize_attenuation_counts(self, attenuation_dB: float) -> int:
        '''
        Convert dB to device counts, rejecting out-of-range values and quantising
        the rest onto the hardware step grid.
        '''
        self._require_connected("attenuation conversion")
        attenuation_dB = float(attenuation_dB)
        minimum_dB = counts_to_db(self._min_atten_counts)
        maximum_dB = counts_to_db(self._max_atten_counts)
        step_dB = counts_to_db(self._step_counts)

        # Half a step of slack so that exactly 90.0 dB is not rejected by a float
        # representation artefact.
        if not minimum_dB - 0.5 * step_dB <= attenuation_dB <= maximum_dB + 0.5 * step_dB:
            raise ValueError(
                f"attenuation_dB={attenuation_dB} is outside [{minimum_dB}, {maximum_dB}] dB for "
                f"{self._model_name} serial {self.serial_number}"
            )

        counts = self._step_counts * round_half_up(attenuation_dB / step_dB)
        # Rounding up near the top of the range can overshoot the limit.
        return max(self._min_atten_counts, min(self._max_atten_counts, counts))

    def _quantize_frequency_counts(self, frequency_MHz: float) -> int:
        '''
        Convert MHz to device counts, rejecting out-of-range values.
        '''
        self._require_connected("frequency conversion")
        frequency_MHz = float(frequency_MHz)

        # A model without frequency-compensated attenuation reports an empty range.
        # Saying so beats an unhelpful "outside [0.0, 0.0] MHz".
        if self._max_freq_counts <= self._min_freq_counts:
            raise Vaunix_LDA_Feature_Error(
                f"{self._model_name} serial {self.serial_number} reports no working frequency range, "
                f"so its attenuation is not frequency-compensated and the working frequency cannot "
                f"be set. features={describe_features(self._features)}"
            )

        minimum_MHz = counts_to_mhz(self._min_freq_counts)
        maximum_MHz = counts_to_mhz(self._max_freq_counts)

        counts = mhz_to_counts(frequency_MHz)
        if not self._min_freq_counts <= counts <= self._max_freq_counts:
            raise ValueError(
                f"frequency_MHz={frequency_MHz} is outside [{minimum_MHz}, {maximum_MHz}] MHz for "
                f"{self._model_name} serial {self.serial_number}"
            )
        return counts
