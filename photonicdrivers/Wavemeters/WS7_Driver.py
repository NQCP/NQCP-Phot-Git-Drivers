from __future__ import annotations
import ctypes
from ctypes import c_int32, c_double, c_bool, c_uint16
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
    def __init__(self, dll_path: str="C:\Windows\System32\wlmData.dll"):
        self._dll = ctypes.WinDLL(dll_path)
        self._bind_functions()
        self.exposure_limits = None

    def connect(self):
        self._ControlWLMEx(consts.cCtrlWLMShow | consts.cCtrlWLMWait, 0, 0, 30*1000, 0)

    def disconnect(self):
        pass

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
