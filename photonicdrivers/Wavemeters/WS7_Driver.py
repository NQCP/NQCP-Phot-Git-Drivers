from __future__ import annotations
import ctypes
from ctypes import c_int32, c_double, c_bool, c_uint16, POINTER, byref
from dataclasses import dataclass
from typing import Optional
from photonicdrivers.Abstract.Connectable import Connectable 
import photonicdrivers.Wavemeters.wlmConst as consts 

@dataclass
class ExposureLimits:
    arr1_min: int
    arr1_max: int
    arr2_min: Optional[int] = None
    arr2_max: Optional[int] = None

def error_checked(result: int):
    if result < 0:
        raise RuntimeError(f"DLL returned error code: {result}")
    return result

class WS7_Driver(Connectable):
    """
    WS7 Wavelength Meter Driver. Channels are 1-indexed
    """
    def __init__(self, dll_path: str=r"C:\Windows\System32\wlmData.dll"):
        self._dll = ctypes.WinDLL(dll_path)
        self._bind_functions()
        self.exposure_limits = None

    def connect(self):
        self._ControlWLMEx(consts.cCtrlWLMShow | consts.cCtrlWLMWait, 0, 0, 30*1000, 0)

    def disconnect(self):
        pass

    def shutdown(self):
        self._ControlWLMEx(consts.cCtrlWLMExit | consts.cCtrlWLMWait, 0, 0, 10*1000, 0)

    def is_connected(self) -> bool:
        try:
            return self.get_version() > 0
        except Exception:
            return False

    def is_measuring(self) -> bool:
        state = self.get_operation_state()
        return state == consts.cMeasurement

    def get_operation_state(self) -> int:
        return self._GetOperationState(0)

    def get_version(self) -> int:
        return self._GetWLMVersion(0)

    def get_wavelength_nm(self, channel: int) -> float:
        return error_checked(self._GetWavelengthNum(channel, 0.0)) if self.is_measuring() else None

    def get_frequency_THz(self, channel: int) -> float:
        """
        Optical frequency [THz] of the given channel, as computed by the wavemeter itself.

        Preferred over converting get_wavelength_nm() by hand: the DLL applies the same
        air/vacuum refractive index correction it uses for the wavelength reading.

        @return: frequency [THz], or None if the wavemeter is not measuring
        """
        return error_checked(self._GetFrequencyNum(channel, 0.0)) if self.is_measuring() else None

    def get_frequency_GHz(self, channel: int) -> float:
        """
        Optical frequency [GHz] of the given channel.

        @return: frequency [GHz], or None if the wavemeter is not measuring
        """
        frequency_THz = self.get_frequency_THz(channel)
        return frequency_THz * 1e3 if frequency_THz is not None else None

    def get_frequency_MHz(self, channel: int) -> float:
        """
        Optical frequency [MHz] of the given channel.

        @return: frequency [MHz], or None if the wavemeter is not measuring
        """
        frequency_THz = self.get_frequency_THz(channel)
        return frequency_THz * 1e6 if frequency_THz is not None else None

    def get_frequency_Hz(self, channel: int) -> float:
        """
        Optical frequency [Hz] of the given channel.

        @return: frequency [Hz], or None if the wavemeter is not measuring
        """
        frequency_THz = self.get_frequency_THz(channel)
        return frequency_THz * 1e12 if frequency_THz is not None else None

    def get_power_uW(self, channel: int) -> float:
        """
        Power [uW] of the last measured cw signal on the given channel (the DLL's GetPowerNum).

        Relative unless the wavemeter has been power calibrated: the WS7 "basically cannot measure
        the absolute power" (manual, GetPowerNum remarks); calibrate in the WLM program, menu
        Operation | Calibration | Power calibration.

        @return: power [uW], or None if the wavemeter is not measuring. Raises on a DLL error code
                 (e.g. -3 under-exposed, -4 over-exposed, -6 channel not available).
        """
        return error_checked(self._GetPowerNum(channel, 0.0)) if self.is_measuring() else None

    def set_exposure(self, channel: int, exposure_ms: int, arrays: tuple[int, ...] = (1, 2)):
        """
        Set exposure for the given channel.
        By default applies the same exposure to arrays 1 and 2 (WS7 typically has 2 arrays).
        """

        # Set exposure mode to manual first
        error_checked(self._SetExposureModeNum(channel, c_bool(False)))

        for arr in arrays:
            error_checked(self._SetExposureNum(channel, arr, exposure_ms))

    def get_exposure_limits(self) -> ExposureLimits:
        """
        Fetch exposure min/max for arrays 1 and 2, if available.
        """
        if self.exposure_limits is not None:
            return self.exposure_limits

        arr1_min = self._GetExposureRange(consts.cExpoMin)
        arr1_max = self._GetExposureRange(consts.cExpoMax)
        # Some devices may not have array 2; in that case, values can be 0/negative.
        arr2_min = self._GetExposureRange(consts.cExpo2Min)
        arr2_max = self._GetExposureRange(consts.cExpo2Max)
        if arr2_min <= 0 or arr2_max <= 0:
            arr2_min = None
            arr2_max = None

        if arr1_min <= 0 or arr1_max <= 0:
            self.exposure_limits = None
        
        else:
            self.exposure_limits = ExposureLimits(arr1_min, arr1_max, arr2_min, arr2_max)

        return self.exposure_limits
    
    def set_switch_mode(self, enabled: bool):
        """
        Enable or disable multichannel fiber switch mode.
        """
        val = int(enabled)
        return error_checked(self._SetSwitcherMode(val))
    
    def get_switch_mode(self) -> bool:
        """
        True if the multichannel switch mode is on (GetSwitcherMode). Devices without a switch
        always return False.
        """
        return bool(error_checked(self._GetSwitcherMode(0)))

    def get_switch_channel(self) -> int:
        """
        The switch channel the wavemeter last switched to (GetSwitcherChannel). In switch mode this
        runs 1-2 measurement cycles ahead of the channel being measured (manual, remarks).
        """
        return error_checked(self._GetSwitcherChannel(0))

    def set_switch_channel(self, channel: int):
        """
        Selects the active switch channel (SetSwitcherChannel). Has an effect in non-switch mode only.
        """
        return error_checked(self._SetSwitcherChannel(channel))

    def get_switch_channel_states(self, channel: int) -> tuple[bool, bool]:
        """
        (use, show) of a switch channel (GetSwitcherSignalStates): use = the channel is measured in
        switch mode; show = its interferometer pattern is displayed. Defined in switch mode only.
        """
        use, show = c_int32(0), c_int32(0)
        error_checked(self._GetSwitcherSignalStates(channel, byref(use), byref(show)))
        return bool(use.value), bool(show.value)

    def set_switch_channel_states(self, channel: int, use: bool, show: bool):
        """
        Sets whether a switch channel is measured (use) and displayed (show) in switch mode
        (SetSwitcherSignalStates).
        """
        return error_checked(self._SetSwitcherSignalStates(channel, int(use), int(show)))

    def get_channels_count(self) -> int:
        """
        The number of channels that can measure a wavelength (GetChannelsCount), e.g. the switch
        channels.
        """
        return error_checked(self._GetChannelsCount(0))

    def get_exposure_ms(self, channel: int, array: int = 1) -> int:
        """
        The exposure [ms] currently in use on a channel's CCD array (GetExposureNum; array 1 = the
        Fizeau interferometers, 2 = the wide interferometer(s)). Also valid in automatic exposure.
        """
        return error_checked(self._GetExposureNum(channel, array, 0))

    def get_exposure_mode_auto(self, channel: int) -> bool:
        """
        True if the channel uses automatic exposure control (GetExposureModeNum).
        """
        return bool(error_checked(self._GetExposureModeNum(channel, False)))

    def set_exposure_mode_auto(self, channel: int, auto: bool):
        """
        Automatic (True) or manual (False) exposure control for a channel (SetExposureModeNum).
        """
        return error_checked(self._SetExposureModeNum(channel, c_bool(auto)))

    def start_measurement(self):
        return error_checked(self._Operation(consts.cCtrlStartMeasurement))
    
    def stop_measurement(self):
        return error_checked(self._Operation(consts.cCtrlStopAll))

    def _bind_functions(self):
        self._GetWLMCount = self._dll.GetWLMCount
        self._GetWLMCount.argtypes = [c_int32]
        self._GetWLMCount.restype  = c_int32

        self._GetWavelengthNum = self._dll.GetWavelengthNum
        self._GetWavelengthNum.argtypes = [c_int32, c_double]
        self._GetWavelengthNum.restype  = c_double

        self._GetFrequencyNum = self._dll.GetFrequencyNum
        self._GetFrequencyNum.argtypes = [c_int32, c_double]
        self._GetFrequencyNum.restype  = c_double

        self._GetPowerNum = self._dll.GetPowerNum
        self._GetPowerNum.argtypes = [c_int32, c_double]
        self._GetPowerNum.restype  = c_double

        self._GetSwitcherMode = self._dll.GetSwitcherMode
        self._GetSwitcherMode.argtypes = [c_int32]
        self._GetSwitcherMode.restype  = c_int32

        self._GetSwitcherChannel = self._dll.GetSwitcherChannel
        self._GetSwitcherChannel.argtypes = [c_int32]
        self._GetSwitcherChannel.restype  = c_int32

        self._SetSwitcherChannel = self._dll.SetSwitcherChannel
        self._SetSwitcherChannel.argtypes = [c_int32]
        self._SetSwitcherChannel.restype  = c_int32

        self._GetSwitcherSignalStates = self._dll.GetSwitcherSignalStates
        self._GetSwitcherSignalStates.argtypes = [c_int32, POINTER(c_int32), POINTER(c_int32)]
        self._GetSwitcherSignalStates.restype  = c_int32

        self._SetSwitcherSignalStates = self._dll.SetSwitcherSignalStates
        self._SetSwitcherSignalStates.argtypes = [c_int32, c_int32, c_int32]
        self._SetSwitcherSignalStates.restype  = c_int32

        self._GetChannelsCount = self._dll.GetChannelsCount
        self._GetChannelsCount.argtypes = [c_int32]
        self._GetChannelsCount.restype  = c_int32

        self._GetExposureNum = self._dll.GetExposureNum
        self._GetExposureNum.argtypes = [c_int32, c_int32, c_int32]
        self._GetExposureNum.restype  = c_int32

        self._GetExposureModeNum = self._dll.GetExposureModeNum
        self._GetExposureModeNum.argtypes = [c_int32, c_bool]
        self._GetExposureModeNum.restype  = c_int32

        self._SetExposureModeNum = self._dll.SetExposureModeNum
        self._SetExposureModeNum.argtypes = [c_int32, c_bool]
        self._SetExposureModeNum.restype  = c_int32

        self._SetExposureNum = self._dll.SetExposureNum
        self._SetExposureNum.argtypes = [c_int32, c_int32, c_int32]
        self._SetExposureNum.restype  = c_int32

        self._GetExposureRange = self._dll.GetExposureRange
        self._GetExposureRange.argtypes = [c_int32]
        self._GetExposureRange.restype  = c_int32

        self._SetSwitcherMode = self._dll.SetSwitcherMode
        self._SetSwitcherMode.argtypes = [c_int32]
        self._SetSwitcherMode.restype  = c_int32

        self._Operation = self._dll.Operation
        self._Operation.argtypes = [c_int32]
        self._Operation.restype  = c_int32

        self._ControlWLMEx = self._dll.ControlWLMEx
        self._ControlWLMEx.argtypes = [c_int32, c_int32, c_int32, c_int32, c_int32]
        self._ControlWLMEx.restype  = c_int32

        self._GetWLMVersion = self._dll.GetWLMVersion
        self._GetWLMVersion.argtypes = [c_int32]
        self._GetWLMVersion.restype  = c_int32

        self._GetOperationState = self._dll.GetOperationState
        self._GetOperationState.argtypes = [c_uint16]
        self._GetOperationState.restype  = c_uint16
