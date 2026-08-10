'''
Driver for Vaunix Lab Brick LDA variable digital attenuators over Ethernet.

Developed against an LDA-908V (200-8000 MHz, 90 dB range, 0.1 dB step, single
channel), but every limit is queried from the device at connect() time, so the
multi-channel LDA-908V-2/-4/-8/-N variants and other LDA models work too.

The Ethernet port speaks a raw TCP protocol on port 40001, carrying the same
8-byte HID-style command reports the USB interface uses. There is no HTTP, telnet,
SCPI or VISA involved -- the device's web interface exists but the SDK does not
use it. This driver therefore wraps VNX_Eth_Attn64.dll.

This is a SEPARATE driver from Vaunix_LDA_USB_Driver rather than a transport
option on one class, because the two DLLs are not signature-compatible:

                        USB (VNX_atten64)        Ethernet (VNX_Eth_Attn64)
    device key          unsigned int DEVID       char* deviceip
    getters             return the value         return status, value via int*
    error codes         0x8001_0000 style        STATUS_OK 0 / STATUS_ERROR 1
    attenuation unit    0.25 dB, or 0.05 "HR"    always 0.05 dB, no HR names
    library init        none exported            fnLDA_Init() mandatory
    discovery           GetNumDevices/DevInfo    none -- caller supplies the IP

Two consequences worth knowing before using this driver:

  * There is NO discovery on Ethernet. You must know the unit's IP address, which
    you can find with the Vaunix GUI over USB, or from its web interface. The
    macOS Ethernet library has fnLDA_AddLDADevice for this; Windows does not.
  * Errors carry no detail. STATUS_ERROR is a single undifferentiated code, so
    every message raised from here names the function and its arguments -- that is
    the only diagnostic available.

Typical use:

    from photonicdrivers.Variable_Digital_Attenautor.Vaunix_LDA_Ethernet_Driver import Vaunix_LDA_Ethernet_Driver

    with Vaunix_LDA_Ethernet_Driver(ip_address="192.168.100.5") as attenuator:
        attenuator.set_frequency_MHz(6000)
        attenuator.set_attenuation_dB(31.5)
        print(attenuator.get_attenuation_dB())
'''

from __future__ import annotations

import ctypes
import functools
import os
import threading
from ctypes import POINTER, byref, c_bool, c_char_p, c_int, create_string_buffer
from dataclasses import dataclass
from typing import Optional, Sequence

from photonicdrivers.Abstract.Connectable import Connectable
from photonicdrivers.Variable_Digital_Attenautor.Vaunix_LDA_Constants import (
    ETH_STATUS_NAMES,
    ETH_STATUS_OK,
    HAS_BIDIR_RAMPS,
    HAS_PROFILES,
    IP_MODE_NAMES,
    PROFILE_OFF,
    PROFILE_ONCE,
    PROFILE_REPEAT,
    STRING_BUFFER_SIZE,
    Vaunix_LDA_Error,
    Vaunix_LDA_Feature_Error,
    Vaunix_LDA_Transport_Error,
    counts_to_db,
    counts_to_mhz,
    db_to_counts,
    describe_features,
    mhz_to_counts,
    round_half_up,
)

PINT = POINTER(c_int)

IS_64BIT = ctypes.sizeof(ctypes.c_void_p) == 8

# Location of the DLL inside the SDK drop that ships alongside this driver.
_SDK_RELATIVE_DIR = os.path.join(
    "LDA_SDK_06-08-2026", "LDA_SDK_06-08-2026", "Windows SDK", "Ethernet", "Ethernet",
)
# Note the inconsistent vendor casing: the 32-bit build is not "VNX_Eth_Atten.dll".
_DLL_NAME = "VNX_Eth_Attn64.dll" if IS_64BIT else "VNX_Eth_atten.dll"
_DLL_SUBDIR = "x64" if IS_64BIT else "Win32"

# fnLDA_Init initialises a process-global device array, so it must run exactly once
# per process -- a second call can clobber an already-open device's entry. Caching
# the bound API by DLL path is what enforces that.
_API_CACHE: dict[str, "_LDA_Ethernet_Api"] = {}
_API_CACHE_LOCK = threading.Lock()


@dataclass
class Vaunix_LDA_Device_Info:
    '''
    Everything the driver learns about a unit at connect() time. Fields that do
    not apply to Ethernet are left as None.
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
    Absolute path to the bundled VNX_Eth_Attn DLL matching this interpreter's bitness.
    '''
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        _SDK_RELATIVE_DIR,
        _DLL_SUBDIR,
        "Release",
        _DLL_NAME,
    )


def eth_checked(status: int, context: str) -> None:
    '''
    Validate an LDASTATUS return from the Ethernet DLL.

    Unlike the USB API, every function here returns only a status; the requested
    value arrives in the caller's byref out-parameter. There is a single error
    code with no further detail, which is why `context` must always spell out the
    function name and its arguments.
    '''
    if status != ETH_STATUS_OK:
        description = ETH_STATUS_NAMES.get(status, f"unknown status {status}")
        raise Vaunix_LDA_Error(f"{context}: {description}")


def _locked(method):
    '''
    Serialise a public method on the driver's reentrant lock.

    Selecting a channel and then reading it is a read-modify-write pair, so two
    Python threads interleaving would silently address the wrong channel.
    '''

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        with self._lock:
            return method(self, *args, **kwargs)

    return wrapper


class _LDA_Ethernet_Api:
    '''
    ctypes binding for VNX_Eth_Attn64.dll. One instance per DLL path per process.
    '''

    def __init__(self, dll_path: str) -> None:
        self.dll_path = os.path.abspath(dll_path)
        if not os.path.isfile(self.dll_path):
            raise Vaunix_LDA_Error(
                f"Vaunix Ethernet DLL not found at {self.dll_path}. Extract the LDA SDK zip next to "
                f"this driver, or pass dll_path= pointing at {_DLL_NAME}."
            )
        try:
            os.add_dll_directory(os.path.dirname(self.dll_path))
        except (OSError, AttributeError):
            pass
        try:
            # These exports are __cdecl, so CDLL rather than WinDLL.
            self._dll = ctypes.CDLL(self.dll_path, winmode=0)
        except OSError as error:
            raise Vaunix_LDA_Error(
                f"Could not load {self.dll_path}. This is {'64' if IS_64BIT else '32'}-bit Python, "
                f"which needs {_DLL_NAME}; a bitness mismatch is the usual cause. Original error: {error}"
            ) from error

        self._bind_functions()

        # Mandatory first call, and exactly once per process.
        self.Init()
        # Without this the DLL may answer from its simulated devices.
        self._test_mode = False
        self.set_test_mode(False)

    def set_test_mode(self, enabled: bool) -> None:
        '''
        Turn the DLL's simulated-hardware mode on or off.
        '''
        self._test_mode = bool(enabled)
        self.SetTestMode(self._test_mode)

    def _bind_functions(self) -> None:
        dll = self._dll

        # --- void returns. restype MUST be None, or ctypes reads a garbage int. ---
        self.Init = dll.fnLDA_Init
        self.Init.argtypes = []
        self.Init.restype = None

        self.SetTestMode = dll.fnLDA_SetTestMode
        self.SetTestMode.argtypes = [c_bool]
        self.SetTestMode.restype = None

        # --- Returns char*. With the default c_int restype the pointer would be
        #     truncated to 32 bits on x64 and the value would be meaningless. ---
        self.LibVersion = dll.fnLDA_LibVersion
        self.LibVersion.argtypes = []
        self.LibVersion.restype = c_char_p

        self.GetLibVersion = dll.fnLDA_GetLibVersion
        self.GetLibVersion.argtypes = []
        self.GetLibVersion.restype = c_int

        # --- [char* ip] -> LDASTATUS ---
        for name in ("InitDevice", "CloseDevice", "CheckDeviceReady", "SaveSettings"):
            function = getattr(dll, "fnLDA_" + name)
            function.argtypes = [c_char_p]
            function.restype = c_int
            setattr(self, name, function)

        # --- [char* ip, int* out] -> LDASTATUS ---
        for name in (
            "GetMaxChannels", "GetSerialNumber", "GetIPMode", "GetFeatures", "GetChannel",
            "GetWorkingFrequency", "GetMinWorkingFrequency", "GetMaxWorkingFrequency",
            "GetAttenuation", "GetMinAttenuation", "GetMaxAttenuation",
            "GetRampStart", "GetRampEnd", "GetAttenuationStep", "GetAttenuationStepTwo",
            "GetDwellTime", "GetDwellTimeTwo", "GetIdleTime", "GetHoldTime", "GetRF_On",
            "GetProfileMaxLength", "GetProfileCount", "GetProfileDwellTime",
            "GetProfileIdleTime", "GetProfileIndex",
        ):
            function = getattr(dll, "fnLDA_" + name)
            function.argtypes = [c_char_p, PINT]
            function.restype = c_int
            setattr(self, name, function)

        # --- [char* ip, char* out] -> LDASTATUS ---
        for name in ("GetModelName", "GetSoftwareVersion", "GetIPAddress", "GetNetmask", "GetGateway"):
            function = getattr(dll, "fnLDA_" + name)
            function.argtypes = [c_char_p, c_char_p]
            function.restype = c_int
            setattr(self, name, function)

        # --- [char* ip, int] -> LDASTATUS ---
        for name in (
            "SetWorkingFrequency", "SetChannel", "SetAttenuation",
            "SetAttenuationStep", "SetAttenuationStepTwo", "SetRampStart", "SetRampEnd",
            "SetDwellTime", "SetDwellTimeTwo", "SetIdleTime", "SetHoldTime",
            "SetProfileCount", "SetProfileIdleTime", "SetProfileDwellTime", "StartProfile",
        ):
            function = getattr(dll, "fnLDA_" + name)
            function.argtypes = [c_char_p, c_int]
            function.restype = c_int
            setattr(self, name, function)

        # --- three-argument forms ---
        self.SetAttenuationQ = dll.fnLDA_SetAttenuationQ
        self.SetAttenuationQ.argtypes = [c_char_p, c_int, c_int]
        self.SetAttenuationQ.restype = c_int

        self.SetProfileElement = dll.fnLDA_SetProfileElement
        self.SetProfileElement.argtypes = [c_char_p, c_int, c_int]
        self.SetProfileElement.restype = c_int

        self.GetProfileElement = dll.fnLDA_GetProfileElement
        self.GetProfileElement.argtypes = [c_char_p, c_int, PINT]
        self.GetProfileElement.restype = c_int

        # --- [char* ip, bool] -> LDASTATUS. MSVC bool is one byte. ---
        for name in ("SetRFOn", "SetRampDirection", "SetRampMode", "SetRampBidirectional", "StartRamp"):
            function = getattr(dll, "fnLDA_" + name)
            function.argtypes = [c_char_p, c_bool]
            function.restype = c_int
            setattr(self, name, function)

        # Deliberately not bound: fnLDA_StartRampMC and fnLDA_StartProfileMC, which
        # sit under a "To Be Done" banner in ldadrvr.h, and fnLDA_StartRampMC2,
        # which is exported but undocumented.

    def get_dll_version_string(self) -> str:
        '''
        Version of the loaded Ethernet DLL, from fnLDA_LibVersion, falling back to
        the numeric fnLDA_GetLibVersion if the string pointer comes back NULL.
        '''
        raw = self.LibVersion()
        if raw:
            return raw.decode("ascii", errors="replace").strip()
        numeric = self.GetLibVersion()
        return f"{(numeric >> 8) & 0xFF}.{numeric & 0xFF:02d}"


def _get_api(dll_path: Optional[str]) -> _LDA_Ethernet_Api:
    '''
    Return the process-wide bound API for this DLL, loading and initialising it on
    first use so that fnLDA_Init runs exactly once.
    '''
    path = os.path.normcase(os.path.abspath(dll_path or default_dll_path()))
    with _API_CACHE_LOCK:
        api = _API_CACHE.get(path)
        if api is None:
            api = _LDA_Ethernet_Api(path)
            _API_CACHE[path] = api
        return api


def set_test_mode(enabled: bool, dll_path: Optional[str] = None) -> None:
    '''
    Switch the DLL between real hardware and simulated devices.

    Test mode is global to the DLL, not per device, so this affects every driver
    instance in the process. It is useful for exercising the ctypes binding end to
    end without a reachable attenuator -- wrong argtypes show up here as an access
    violation, which is much easier to diagnose before real hardware is involved.

    Call it before constructing a driver.
    '''
    _get_api(dll_path).set_test_mode(enabled)


class Vaunix_LDA_Ethernet_Driver(Connectable):
    '''
    Vaunix Lab Brick LDA variable digital attenuator over Ethernet.

    Channels are 1-indexed, matching the vendor API. Attenuation is in dB,
    frequency in MHz, and ramp/profile times in milliseconds.
    '''

    def __init__(
        self,
        ip_address: str,
        serial_number: Optional[int] = None,
        dll_path: Optional[str] = None,
        attenuation_step_dB: float = 0.1,
    ) -> None:
        '''
        Args:
            ip_address: IPv4 address of the attenuator, e.g. "192.168.100.5". There
                is no discovery API on Windows, so this is required. Find it with
                the Vaunix GUI over USB or from the device's web interface.
            serial_number: Optional expected serial number. When given, connect()
                verifies it against the device and raises on a mismatch, which
                catches the case where the unit at this IP has been swapped.
            dll_path: Override for the bundled VNX_Eth_Attn DLL.
            attenuation_step_dB: Hardware attenuation step used for quantisation.
                The Ethernet DLL exports no fnLDA_GetMinAttenStep, so unlike the USB
                driver this cannot be read from the device. The LDA-908V steps in
                0.1 dB; change this only for a model with a coarser step.
        '''
        if not ip_address:
            raise ValueError("Vaunix_LDA_Ethernet_Driver requires an ip_address")

        self.connectionType = "Ethernet"
        self.ip_address = str(ip_address).strip()
        self._ip_bytes = self.ip_address.encode("utf-8")
        self.serial_number = None if serial_number is None else int(serial_number)
        self.dll_path = dll_path
        self.attenuation_step_dB = float(attenuation_step_dB)

        self._lock = threading.RLock()
        self._api: Optional[_LDA_Ethernet_Api] = None
        self._opened = False

        # Populated by connect(); all limits come from the device, not the datasheet.
        self._model_name = ""
        self._features = 0
        self._num_channels = 1
        self._active_channel = 1
        self._min_atten_counts = 0
        self._max_atten_counts = 0
        self._step_counts = max(1, db_to_counts(self.attenuation_step_dB))
        self._min_freq_counts = 0
        self._max_freq_counts = 0
        self._profile_max_length = 0

    # ==================== Connectable ====================

    @_locked
    def connect(self) -> None:
        '''
        Open a socket to the attenuator and cache its limits. Idempotent.
        '''
        if self.is_connected():
            return

        self._api = _get_api(self.dll_path)

        # This generates a lot of traffic to the device, so it belongs at the start
        # of a session; repeatedly opening and closing carries a real penalty.
        eth_checked(self._api.InitDevice(self._ip_bytes), f"fnLDA_InitDevice(ip={self.ip_address})")
        self._opened = True

        if not self._is_device_ready():
            self._opened = False
            raise Vaunix_LDA_Error(
                f"fnLDA_InitDevice(ip={self.ip_address}) succeeded but the device does not report "
                f"ready. Check that the IP is correct and reachable, and that TCP port 40001 is "
                f"not blocked by a firewall."
            )

        self._cache_device_limits()

        reported_serial = self.get_serial_number()
        if self.serial_number is not None and reported_serial != self.serial_number:
            self._opened = False
            raise Vaunix_LDA_Error(
                f"The attenuator at {self.ip_address} reports serial {reported_serial}, but "
                f"serial_number={self.serial_number} was requested. The unit at this address may "
                f"have been swapped or re-addressed."
            )
        self.serial_number = reported_serial

    @_locked
    def disconnect(self) -> None:
        '''
        Close the socket. Idempotent, and never raises -- a failed close must not
        leave the object claiming to still be connected.
        '''
        if self._api is None or not self._opened:
            self._opened = False
            return
        try:
            eth_checked(self._api.CloseDevice(self._ip_bytes), f"fnLDA_CloseDevice(ip={self.ip_address})")
        except Exception as error:
            print(f"WARNING in Vaunix_LDA_Ethernet_Driver.disconnect: {error}")
        finally:
            self._opened = False

    def is_connected(self) -> bool:
        '''
        True if the device answers as ready.

        Unlike the USB driver this costs a network round trip, subject to the DLL's
        own socket timeout, so it can block for a few hundred milliseconds. Avoid
        calling it inside a tight measurement loop.
        '''
        if self._api is None or not self._opened:
            return False
        try:
            return self._is_device_ready()
        except Exception:
            return False

    def __enter__(self) -> "Vaunix_LDA_Ethernet_Driver":
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
            connection_type="Ethernet",
            device_id=None,
            ip_address=self.ip_address,
            software_version=self.get_software_version(),
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
        return self._get_int(self._api.GetSerialNumber, "fnLDA_GetSerialNumber")

    def get_connection_type(self) -> str:
        '''
        Always "Ethernet" for this driver.
        '''
        return self.connectionType

    @_locked
    def get_dll_version(self) -> str:
        '''
        Version of the loaded VNX_Eth_Attn DLL.
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

    @_locked
    def get_channel(self) -> int:
        '''
        The currently selected channel, read from the device.
        '''
        return self._get_int(self._api.GetChannel, "fnLDA_GetChannel")

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
        return counts_to_db(self._get_int(self._api.GetAttenuation, "fnLDA_GetAttenuation"))

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
            eth_checked(
                self._api.SetAttenuation(self._ip_bytes, counts),
                f"fnLDA_SetAttenuation(ip={self.ip_address}, counts={counts})",
            )
            return

        # The channel-qualified call is atomic, so it cannot be interleaved with
        # another thread's channel change the way SetChannel + SetAttenuation can.
        validated = self._validated_channel(channel)
        eth_checked(
            self._api.SetAttenuationQ(self._ip_bytes, counts, validated),
            f"fnLDA_SetAttenuationQ(ip={self.ip_address}, counts={counts}, channel={validated})",
        )
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

        The Ethernet DLL exports no fnLDA_GetMinAttenStep, so this returns the value
        passed to the constructor rather than a device reading. It never raises,
        because quantisation depends on it.
        '''
        return counts_to_db(self._step_counts)

    def set_attenuation_multichannel_dB(self, attenuation_dB: float, channels: Sequence[int]) -> None:
        '''
        Not available over Ethernet. Use Vaunix_LDA_USB_Driver, or call
        set_attenuation_dB once per channel.
        '''
        raise Vaunix_LDA_Transport_Error(
            "set_attenuation_multichannel_dB is not available over Ethernet: VNX_Eth_Attn64.dll "
            "exports no fnLDA_SetAttenuationMCHR. Set each channel individually, or use "
            "Vaunix_LDA_USB_Driver."
        )

    # ==================== working frequency ====================

    @_locked
    def get_frequency_MHz(self) -> float:
        '''
        The working frequency the attenuation calibration is applied at, in MHz.
        '''
        return counts_to_mhz(self._get_int(self._api.GetWorkingFrequency, "fnLDA_GetWorkingFrequency"))

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
        eth_checked(
            self._api.SetWorkingFrequency(self._ip_bytes, counts),
            f"fnLDA_SetWorkingFrequency(ip={self.ip_address}, counts={counts})",
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
        return bool(self._get_int(self._api.GetRF_On, "fnLDA_GetRF_On"))

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
        return counts_to_db(self._get_int(self._api.GetRampStart, "fnLDA_GetRampStart"))

    @_locked
    def set_ramp_start_dB(self, attenuation_dB: float) -> None:
        '''
        Set the attenuation the ramp starts from.
        '''
        self._set_attenuation_like(self._api.SetRampStart, "fnLDA_SetRampStart", attenuation_dB)

    @_locked
    def get_ramp_end_dB(self) -> float:
        '''
        Attenuation the ramp ends at, in dB.
        '''
        return counts_to_db(self._get_int(self._api.GetRampEnd, "fnLDA_GetRampEnd"))

    @_locked
    def set_ramp_end_dB(self, attenuation_dB: float) -> None:
        '''
        Set the attenuation the ramp ends at.

        An upward ramp requires the end to be above the start.
        '''
        self._set_attenuation_like(self._api.SetRampEnd, "fnLDA_SetRampEnd", attenuation_dB)

    @_locked
    def get_ramp_step_dB(self) -> float:
        '''
        Attenuation increment per ramp step, in dB.
        '''
        return counts_to_db(self._get_int(self._api.GetAttenuationStep, "fnLDA_GetAttenuationStep"))

    @_locked
    def set_ramp_step_dB(self, step_dB: float) -> None:
        '''
        Set the attenuation increment per ramp step.
        '''
        self._set_step_like(self._api.SetAttenuationStep, "fnLDA_SetAttenuationStep", step_dB)

    @_locked
    def get_ramp_step_two_dB(self) -> float:
        '''
        Attenuation increment for the second phase of a bidirectional ramp, in dB.
        '''
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "get_ramp_step_two_dB")
        return counts_to_db(self._get_int(self._api.GetAttenuationStepTwo, "fnLDA_GetAttenuationStepTwo"))

    @_locked
    def set_ramp_step_two_dB(self, step_dB: float) -> None:
        '''
        Set the attenuation increment for the second phase of a bidirectional ramp.
        '''
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "set_ramp_step_two_dB")
        self._set_step_like(self._api.SetAttenuationStepTwo, "fnLDA_SetAttenuationStepTwo", step_dB)

    @_locked
    def get_ramp_dwell_time_ms(self) -> int:
        '''
        Time spent at each ramp step, in milliseconds.
        '''
        return self._get_int(self._api.GetDwellTime, "fnLDA_GetDwellTime")

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
        return self._get_int(self._api.GetDwellTimeTwo, "fnLDA_GetDwellTimeTwo")

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
        return self._get_int(self._api.GetIdleTime, "fnLDA_GetIdleTime")

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
        return self._get_int(self._api.GetHoldTime, "fnLDA_GetHoldTime")

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

    def start_ramp_multichannel(self, channels: Sequence[int], repeat: bool = False,
                                deferred: bool = False) -> None:
        '''
        Not available over Ethernet. Use Vaunix_LDA_USB_Driver.
        '''
        raise Vaunix_LDA_Transport_Error(
            "start_ramp_multichannel is not available over Ethernet: fnLDA_StartRampMC is declared "
            "under a \"To Be Done\" banner in ldadrvr.h and is not implemented. Use "
            "Vaunix_LDA_USB_Driver."
        )

    def is_ramping(self) -> bool:
        '''
        Not available over Ethernet -- the DLL exports no fnLDA_GetDeviceStatus, so
        there is no way to poll ramp activity. Use Vaunix_LDA_USB_Driver.
        '''
        raise Vaunix_LDA_Transport_Error(
            "is_ramping is not available over Ethernet: VNX_Eth_Attn64.dll exports no "
            "fnLDA_GetDeviceStatus, so ramp activity cannot be polled. Use Vaunix_LDA_USB_Driver."
        )

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
        return self._get_int(self._api.GetProfileCount, "fnLDA_GetProfileCount")

    @_locked
    def set_profile_count(self, count: int) -> None:
        '''
        Set how many profile points are played.

        Args:
            count: Number of points, from 1 to get_profile_max_length().
        '''
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "set_profile_count")
        count = int(count)
        if not 1 <= count <= self._profile_max_length:
            raise ValueError(
                f"profile count={count} is outside [1, {self._profile_max_length}] "
                f"for {self._model_name} at {self.ip_address}"
            )
        eth_checked(
            self._api.SetProfileCount(self._ip_bytes, count),
            f"fnLDA_SetProfileCount(ip={self.ip_address}, count={count})",
        )

    @_locked
    def get_profile_element_dB(self, index: int) -> float:
        '''
        Read one profile point.

        Args:
            index: 0-based index into the profile.
        '''
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "get_profile_element_dB")
        validated = self._validated_profile_index(index)
        counts = self._get_int(
            self._api.GetProfileElement, f"fnLDA_GetProfileElement(index={validated})", validated
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
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "set_profile_element_dB")
        validated = self._validated_profile_index(index)
        counts = self._quantize_attenuation_counts(attenuation_dB)
        eth_checked(
            self._api.SetProfileElement(self._ip_bytes, validated, counts),
            f"fnLDA_SetProfileElement(ip={self.ip_address}, index={validated}, counts={counts})",
        )

    @_locked
    def set_profile_dB(self, attenuations_dB: Sequence[float]) -> None:
        '''
        Write a whole profile and set its length in one call.

        Args:
            attenuations_dB: Attenuation for each point, in dB, in play order.
        '''
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "set_profile_dB")
        if not attenuations_dB:
            raise ValueError("attenuations_dB must contain at least one point")
        if len(attenuations_dB) > self._profile_max_length:
            raise ValueError(
                f"profile has {len(attenuations_dB)} points but {self._model_name} at "
                f"{self.ip_address} holds at most {self._profile_max_length}"
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
        return self._get_int(self._api.GetProfileDwellTime, "fnLDA_GetProfileDwellTime")

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
        return self._get_int(self._api.GetProfileIdleTime, "fnLDA_GetProfileIdleTime")

    @_locked
    def set_profile_idle_time_ms(self, idle_time_ms: int) -> None:
        '''
        Set the idle time between repeats of a profile.
        '''
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "set_profile_idle_time_ms")
        self._set_time(self._api.SetProfileIdleTime, "fnLDA_SetProfileIdleTime", idle_time_ms, minimum_ms=0)

    def get_profile_index(self) -> int:
        '''
        Not available over Ethernet.

        ldadrvr.h documents fnLDA_GetProfileIndex as "not currently supported over
        Ethernet". The symbol IS exported and returns STATUS_OK with a meaningless
        out-value, so this is blocked here rather than left to the DLL.
        '''
        raise Vaunix_LDA_Transport_Error(
            "get_profile_index is not available over Ethernet: ldadrvr.h documents "
            "fnLDA_GetProfileIndex as unsupported, and the exported symbol returns STATUS_OK with "
            "a meaningless value. Use Vaunix_LDA_USB_Driver."
        )

    @_locked
    def start_profile(self, repeat: bool = False) -> None:
        '''
        Play the stored profile.

        Args:
            repeat: True to loop the profile until stop_profile(), False to play once.
        '''
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "start_profile")
        mode = PROFILE_REPEAT if repeat else PROFILE_ONCE
        eth_checked(
            self._api.StartProfile(self._ip_bytes, mode),
            f"fnLDA_StartProfile(ip={self.ip_address}, mode={mode})",
        )

    @_locked
    def stop_profile(self) -> None:
        '''
        Stop a playing profile.
        '''
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "stop_profile")
        eth_checked(
            self._api.StartProfile(self._ip_bytes, PROFILE_OFF),
            f"fnLDA_StartProfile(ip={self.ip_address}, mode={PROFILE_OFF})",
        )

    def start_profile_multichannel(self, channels: Sequence[int], repeat: bool = False,
                                   delayed: bool = False) -> None:
        '''
        Not available over Ethernet. Use Vaunix_LDA_USB_Driver.
        '''
        raise Vaunix_LDA_Transport_Error(
            "start_profile_multichannel is not available over Ethernet: fnLDA_StartProfileMC is "
            "declared under a \"To Be Done\" banner in ldadrvr.h and is not implemented. Use "
            "Vaunix_LDA_USB_Driver."
        )

    def is_profile_playing(self) -> bool:
        '''
        Not available over Ethernet -- the DLL exports no fnLDA_GetDeviceStatus, so
        there is no way to poll profile activity. Use Vaunix_LDA_USB_Driver.
        '''
        raise Vaunix_LDA_Transport_Error(
            "is_profile_playing is not available over Ethernet: VNX_Eth_Attn64.dll exports no "
            "fnLDA_GetDeviceStatus, so profile activity cannot be polled. Use Vaunix_LDA_USB_Driver."
        )

    # ==================== network ====================

    @_locked
    def get_ip_address(self) -> str:
        '''
        IP address the device reports for itself.
        '''
        return self._get_str(self._api.GetIPAddress, "fnLDA_GetIPAddress")

    @_locked
    def get_netmask(self) -> str:
        '''
        Subnet mask the device is configured with.
        '''
        return self._get_str(self._api.GetNetmask, "fnLDA_GetNetmask")

    @_locked
    def get_gateway(self) -> str:
        '''
        Default gateway the device is configured with.
        '''
        return self._get_str(self._api.GetGateway, "fnLDA_GetGateway")

    @_locked
    def get_ip_mode(self) -> str:
        '''
        How the device obtains its address: "static" or "DHCP".
        '''
        mode = self._get_int(self._api.GetIPMode, "fnLDA_GetIPMode")
        return IP_MODE_NAMES.get(mode, f"unknown IP mode {mode}")

    @_locked
    def get_software_version(self) -> str:
        '''
        Firmware version reported by the device.
        '''
        return self._get_str(self._api.GetSoftwareVersion, "fnLDA_GetSoftwareVersion")

    # ==================== persistence and diagnostics ====================

    @_locked
    def save_settings(self) -> None:
        '''
        Persist the current settings to the device's non-volatile memory so they
        are restored at power-on.
        '''
        self._require_connected("save_settings")
        eth_checked(self._api.SaveSettings(self._ip_bytes), f"fnLDA_SaveSettings(ip={self.ip_address})")

    def get_device_status(self) -> int:
        '''
        Not available over Ethernet. Use Vaunix_LDA_USB_Driver.
        '''
        raise Vaunix_LDA_Transport_Error(
            "get_device_status is not available over Ethernet: VNX_Eth_Attn64.dll exports no "
            "fnLDA_GetDeviceStatus. Use Vaunix_LDA_USB_Driver."
        )

    def set_trace_level(self, trace_level: int, io_trace_level: int, verbose: bool) -> None:
        '''
        Not available over Ethernet. Use Vaunix_LDA_USB_Driver.
        '''
        raise Vaunix_LDA_Transport_Error(
            "set_trace_level is not available over Ethernet: VNX_Eth_Attn64.dll exports no "
            "fnLDA_SetTraceLevel. Use Vaunix_LDA_USB_Driver."
        )

    # ==================================================================
    #                          PRIVATE METHODS
    # ==================================================================

    def _is_device_ready(self) -> bool:
        '''
        Ask the device whether it is ready.

        fnLDA_CheckDeviceReady returns STATUS_OK (0) when the device IS ready and 1
        when it is NOT -- the opposite of Python truthiness, and the opposite of
        every other function in this DLL. This is the only place it is called, and
        "not ready" is a normal answer here, so it deliberately does not go through
        eth_checked.
        '''
        return self._api.CheckDeviceReady(self._ip_bytes) == ETH_STATUS_OK

    def _cache_device_limits(self) -> None:
        '''
        Read the limits that range checks and quantisation depend on.
        '''
        self._model_name = self._get_str(self._api.GetModelName, "fnLDA_GetModelName")
        self._features = self._get_int(self._api.GetFeatures, "fnLDA_GetFeatures")
        self._num_channels = max(1, self._get_int(self._api.GetMaxChannels, "fnLDA_GetMaxChannels"))
        self._min_atten_counts = self._get_int(self._api.GetMinAttenuation, "fnLDA_GetMinAttenuation")
        self._max_atten_counts = self._get_int(self._api.GetMaxAttenuation, "fnLDA_GetMaxAttenuation")
        self._min_freq_counts = self._get_int(
            self._api.GetMinWorkingFrequency, "fnLDA_GetMinWorkingFrequency"
        )
        self._max_freq_counts = self._get_int(
            self._api.GetMaxWorkingFrequency, "fnLDA_GetMaxWorkingFrequency"
        )
        self._profile_max_length = self._get_int(
            self._api.GetProfileMaxLength, "fnLDA_GetProfileMaxLength"
        )
        self._active_channel = self._get_int(self._api.GetChannel, "fnLDA_GetChannel")

        # There is no fnLDA_GetMinAttenStep over Ethernet, so the constructor value
        # is the only grid available.
        self._step_counts = max(1, db_to_counts(self.attenuation_step_dB))

        if self._max_atten_counts <= self._min_atten_counts:
            raise Vaunix_LDA_Error(
                f"The attenuator at {self.ip_address} reported an empty attenuation range "
                f"[{self._min_atten_counts}, {self._max_atten_counts}] counts."
            )

    def _require_connected(self, method: str) -> None:
        if self._api is None or not self._opened:
            raise Vaunix_LDA_Error(f"{method} requires an open connection -- call connect() first.")

    def _require_feature(self, bit: int, bit_name: str, method: str) -> None:
        self._require_connected(method)
        if not self._features & bit:
            raise Vaunix_LDA_Feature_Error(
                f"{method} requires {bit_name}, but {self._model_name} at {self.ip_address} "
                f"reports features={describe_features(self._features)}."
            )

    def _get_int(self, function, context: str, *extra_args) -> int:
        '''
        Invoke a getter whose value comes back through an int* out-parameter.
        '''
        self._require_connected(context)
        out = c_int(0)
        eth_checked(function(self._ip_bytes, *extra_args, byref(out)), f"{context}(ip={self.ip_address})")
        return int(out.value)

    def _get_str(self, function, context: str) -> str:
        '''
        Invoke a getter whose value comes back through a char* out-parameter.
        '''
        self._require_connected(context)
        buffer = create_string_buffer(STRING_BUFFER_SIZE)
        eth_checked(function(self._ip_bytes, buffer), f"{context}(ip={self.ip_address})")
        return buffer.value.decode("ascii", errors="replace").strip()

    def _set_bool(self, function, context: str, value: bool) -> None:
        self._require_connected(context)
        eth_checked(
            function(self._ip_bytes, bool(value)),
            f"{context}(ip={self.ip_address}, value={bool(value)})",
        )

    def _set_attenuation_like(self, function, context: str, attenuation_dB: float) -> None:
        '''
        Set a parameter that shares the attenuation range, e.g. a ramp endpoint.
        '''
        self._require_connected(context)
        counts = self._quantize_attenuation_counts(attenuation_dB)
        eth_checked(
            function(self._ip_bytes, counts), f"{context}(ip={self.ip_address}, counts={counts})"
        )

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
                f"{self._model_name} at {self.ip_address}"
            )
        eth_checked(
            function(self._ip_bytes, counts), f"{context}(ip={self.ip_address}, counts={counts})"
        )

    def _set_time(self, function, context: str, time_ms: int, minimum_ms: int) -> None:
        self._require_connected(context)
        time_ms = int(time_ms)
        if time_ms < minimum_ms:
            raise ValueError(f"{context} requires at least {minimum_ms} ms, got {time_ms}")
        eth_checked(
            function(self._ip_bytes, time_ms), f"{context}(ip={self.ip_address}, ms={time_ms})"
        )

    def _select_channel(self, channel: int) -> None:
        '''
        Select a channel, skipping the call when it is already active.
        '''
        if channel == self._active_channel:
            return
        eth_checked(
            self._api.SetChannel(self._ip_bytes, channel),
            f"fnLDA_SetChannel(ip={self.ip_address}, channel={channel})",
        )
        self._active_channel = channel

    def _validated_channel(self, channel: int) -> int:
        self._require_connected("channel selection")
        channel = int(channel)
        if not 1 <= channel <= self._num_channels:
            raise ValueError(
                f"channel={channel} is outside [1, {self._num_channels}] for {self._model_name} "
                f"at {self.ip_address}. Channels are 1-indexed."
            )
        return channel

    def _validated_profile_index(self, index: int) -> int:
        index = int(index)
        if not 0 <= index < self._profile_max_length:
            raise ValueError(
                f"profile index={index} is outside [0, {self._profile_max_length - 1}] for "
                f"{self._model_name} at {self.ip_address}. Indices are 0-based."
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
                f"{self._model_name} at {self.ip_address}"
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
                f"{self._model_name} at {self.ip_address} reports no working frequency range, so its "
                f"attenuation is not frequency-compensated and the working frequency cannot be set. "
                f"features={describe_features(self._features)}"
            )

        minimum_MHz = counts_to_mhz(self._min_freq_counts)
        maximum_MHz = counts_to_mhz(self._max_freq_counts)

        counts = mhz_to_counts(frequency_MHz)
        if not self._min_freq_counts <= counts <= self._max_freq_counts:
            raise ValueError(
                f"frequency_MHz={frequency_MHz} is outside [{minimum_MHz}, {maximum_MHz}] MHz for "
                f"{self._model_name} at {self.ip_address}"
            )
        return counts
