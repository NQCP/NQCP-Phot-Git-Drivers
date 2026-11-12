"""A stand-in for HighFinesse's wlmData.dll, for testing WS7_Driver without the wavemeter.

Answers the calls WS7_Driver binds, with the DLL's conventions (HighFinesse WS7 IR manual, chapter 4):
values per channel (1-indexed), negative return values are error codes (wlmConst: ErrLowSignal -3, ErrBigSignal -4,
ErrNotAvailable -6). Use: driver = WS7_Driver.__new__(WS7_Driver); driver._dll = WS7_DLL_Mock(); driver._bind_functions().
"""
import photonicdrivers.Wavemeters.wlmConst as consts


class _Function:
    """A DLL function: callable, and accepts the argtypes / restype attributes ctypes sets."""

    def __init__(self, function):
        self._function = function
        self.argtypes = None
        self.restype = None

    def __call__(self, *args):
        return self._function(*args)


class WS7_DLL_Mock:
    def __init__(self, channels: int = 4):
        self.channels = channels
        self.measuring = True
        self.frequency_THz = {ch: 226.130 for ch in range(1, channels + 1)}
        self.power_uW = {ch: 10.0 for ch in range(1, channels + 1)}
        self.errors = {}                          # channel -> error code returned by every getter
        self.exposure_mode_auto = {}
        self.exposure_ms = {}
        self.switch_mode = None
        self.calls = []

        for name in ("GetWLMCount", "GetWavelengthNum", "GetFrequencyNum", "GetPowerNum", "SetExposureModeNum",
                     "SetExposureNum", "GetExposureRange", "SetSwitcherMode", "Operation", "ControlWLMEx",
                     "GetWLMVersion", "GetOperationState"):
            setattr(self, name, _Function(getattr(self, "_" + name)))

    def _value(self, channel, value):
        self.calls.append(("value", channel))
        if channel not in self.frequency_THz:
            return float(consts.ErrNotAvailable)
        if channel in self.errors:
            return float(self.errors[channel])
        return value

    def _GetWLMCount(self, _):
        return 1

    def _GetFrequencyNum(self, channel, _):
        return self._value(channel, self.frequency_THz.get(channel))

    def _GetWavelengthNum(self, channel, _):
        f = self.frequency_THz.get(channel)
        return self._value(channel, None if f is None else 299792458.0 / (f * 1e12) * 1e9)

    def _GetPowerNum(self, channel, _):
        return self._value(channel, self.power_uW.get(channel))

    def _SetExposureModeNum(self, channel, auto):
        self.exposure_mode_auto[channel] = bool(auto)
        return 0

    def _SetExposureNum(self, channel, array, exposure_ms):
        self.exposure_ms[(channel, array)] = exposure_ms
        return 0

    def _GetExposureRange(self, which):
        return 1 if which in (consts.cExpoMin, consts.cExpo2Min) else 9999

    def _SetSwitcherMode(self, mode):
        self.switch_mode = mode
        return 0

    def _Operation(self, op):
        self.measuring = op == consts.cCtrlStartMeasurement
        return 0

    def _ControlWLMEx(self, *args):
        return 1

    def _GetWLMVersion(self, _):
        return 7

    def _GetOperationState(self, _):
        return consts.cMeasurement if self.measuring else consts.cStop
