"""
wlmData API function bindings generated from wlmData.h on 2024-11-12
"""
# pylint: disable=line-too-long

import ctypes
import platform

_FUNCTYPE = ctypes.WINFUNCTYPE if platform.system() == 'Windows' else ctypes.CFUNCTYPE

CALLBACK_TYPE = _FUNCTYPE(None, ctypes.c_int32, ctypes.c_int32, ctypes.c_double)
CALLBACK_EX_TYPE = _FUNCTYPE(None, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_double,
    ctypes.c_int32)

_PROTOTYPES = {
# ***********  Functions for general usage  ****************************
    # intptr_t Instantiate(int32_t RFC, int32_t Mode, intptr_t P1, int32_t P2)
    'Instantiate': (ctypes.c_void_p, (ctypes.c_int32, ctypes.c_int32, ctypes.c_void_p, ctypes.c_int32)),


    # void CallbackProc(int32_t Mode, int32_t IntVal, double DblVal)

    # void CallbackProcEx(int32_t Ver, int32_t Mode, int32_t IntVal, double DblVal, int32_t Res1)

    # int32_t WaitForWLMEvent(int32_t* Mode, int32_t* IntVal, double* DblVal)
    'WaitForWLMEvent': (ctypes.c_int32, (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_double))),

    # int32_t WaitForWLMEventEx(int32_t* Ver, int32_t* Mode, int32_t* IntVal, double* DblVal, int32_t* Res1)
    'WaitForWLMEventEx': (ctypes.c_int32, (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int32))),

    # int32_t WaitForNextWLMEvent(int32_t* Mode, int32_t* IntVal, double* DblVal)
    'WaitForNextWLMEvent': (ctypes.c_int32, (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_double))),

    # int32_t WaitForNextWLMEventEx(int32_t* Ver, int32_t* Mode, int32_t* IntVal, double* DblVal, int32_t* Res1)
    'WaitForNextWLMEventEx': (ctypes.c_int32, (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int32))),

    # void ClearWLMEvents(void)
    'ClearWLMEvents': (None, ()),


    # int32_t ControlWLM(int32_t Action, intptr_t App, int32_t Ver)
    'ControlWLM': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_void_p, ctypes.c_int32)),

    # int32_t ControlWLMEx(int32_t Action, intptr_t App, int32_t Ver, int32_t Delay, int32_t Res)
    'ControlWLMEx': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)),

    # int64_t SynchroniseWLM(int32_t Mode, int64_t TS)
    'SynchroniseWLM': (ctypes.c_int64, (ctypes.c_int32, ctypes.c_int64)),

    # int32_t SetMeasurementDelayMethod(int32_t Mode, int32_t Delay)
    'SetMeasurementDelayMethod': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32)),

    # int32_t SetWLMPriority(int32_t PPC, int32_t Res1, int32_t Res2)
    'SetWLMPriority': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)),

    # int32_t PresetWLMIndex(int32_t Ver)
    'PresetWLMIndex': (ctypes.c_int32, (ctypes.c_int32,)),


    # int32_t GetWLMVersion(int32_t Ver)
    'GetWLMVersion': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetWLMIndex(int32_t Ver)
    'GetWLMIndex': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetWLMCount(int32_t V)
    'GetWLMCount': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetOptionInfo(int32_t Index, int32_t Detail, int64_t* I64Val, double* DblVal, char* sVal)
    'GetOptionInfo': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int64), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_char))),


# ***********  General Get... & Set...-functions  **********************
    # double GetWavelength(double WL)
    'GetWavelength': (ctypes.c_double, (ctypes.c_double,)),

    # double GetWavelength2(double WL2)
    'GetWavelength2': (ctypes.c_double, (ctypes.c_double,)),

    # double GetWavelengthNum(int32_t num, double WL)
    'GetWavelengthNum': (ctypes.c_double, (ctypes.c_int32, ctypes.c_double)),

    # double GetCalWavelength(int32_t ba, double WL)
    'GetCalWavelength': (ctypes.c_double, (ctypes.c_int32, ctypes.c_double)),

    # double GetCalibrationEffect(double CE)
    'GetCalibrationEffect': (ctypes.c_double, (ctypes.c_double,)),

    # double GetFrequency(double F)
    'GetFrequency': (ctypes.c_double, (ctypes.c_double,)),

    # double GetFrequency2(double F2)
    'GetFrequency2': (ctypes.c_double, (ctypes.c_double,)),

    # double GetFrequencyNum(int32_t num, double F)
    'GetFrequencyNum': (ctypes.c_double, (ctypes.c_int32, ctypes.c_double)),

    # double GetLinewidth(int32_t Index, double LW)
    'GetLinewidth': (ctypes.c_double, (ctypes.c_int32, ctypes.c_double)),

    # double GetLinewidthNum(int32_t num, double LW)
    'GetLinewidthNum': (ctypes.c_double, (ctypes.c_int32, ctypes.c_double)),

    # double GetDistance(double D)
    'GetDistance': (ctypes.c_double, (ctypes.c_double,)),

    # double GetAnalogIn(double AI)
    'GetAnalogIn': (ctypes.c_double, (ctypes.c_double,)),

    # double GetMultimodeInfo(int32_t num, int32_t type, int32_t mode, double* Val)
    'GetMultimodeInfo': (ctypes.c_double, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_double))),

    # int32_t GetResultInfo(int32_t num, int32_t info)
    'GetResultInfo': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32)),

    # double GetMeasurementUncertainty(int32_t Index,   int32_t num,   double MU)
    'GetMeasurementUncertainty': (ctypes.c_double, (ctypes.c_int32, ctypes.c_int32, ctypes.c_double)),

    # double GetTemperature(double T)
    'GetTemperature': (ctypes.c_double, (ctypes.c_double,)),

    # int32_t SetTemperature(double T)
    'SetTemperature': (ctypes.c_int32, (ctypes.c_double,)),

    # double GetPressure(double P)
    'GetPressure': (ctypes.c_double, (ctypes.c_double,)),

    # int32_t SetPressure(int32_t Mode, double P)
    'SetPressure': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_double)),

    # int32_t GetAirParameters(int32_t Mode, int32_t* State, double* Val)
    'GetAirParameters': (ctypes.c_int32, (ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_double))),

    # int32_t SetAirParameters(int32_t Mode, int32_t State, double Val)
    'SetAirParameters': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_double)),

    # double GetExternalInput(int32_t Index, double I)
    'GetExternalInput': (ctypes.c_double, (ctypes.c_int32, ctypes.c_double)),

    # int32_t SetExternalInput(int32_t Index, double I)
    'SetExternalInput': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_double)),

    # int32_t GetExtraSetting(int32_t Index, int32_t* lGet, double* dGet, char* sGet)
    'GetExtraSetting': (ctypes.c_int32, (ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_char))),

    # int32_t SetExtraSetting(int32_t Index, int32_t lSet, double dSet, char* sSet)
    'SetExtraSetting': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_double, ctypes.POINTER(ctypes.c_char))),


    # uint16_t GetExposure(uint16_t E)
    'GetExposure': (ctypes.c_uint16, (ctypes.c_uint16,)),

    # int32_t SetExposure(uint16_t E)
    'SetExposure': (ctypes.c_int32, (ctypes.c_uint16,)),

    # uint16_t GetExposure2(uint16_t E2)
    'GetExposure2': (ctypes.c_uint16, (ctypes.c_uint16,)),

    # int32_t SetExposure2(uint16_t E2)
    'SetExposure2': (ctypes.c_int32, (ctypes.c_uint16,)),

    # int32_t GetExposureNum(int32_t num, int32_t arr, int32_t E)
    'GetExposureNum': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)),

    # int32_t SetExposureNum(int32_t num, int32_t arr, int32_t E)
    'SetExposureNum': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)),

    # double GetExposureNumEx(int32_t num, int32_t arr, double E)
    'GetExposureNumEx': (ctypes.c_double, (ctypes.c_int32, ctypes.c_int32, ctypes.c_double)),

    # int32_t SetExposureNumEx(int32_t num, int32_t arr, double E)
    'SetExposureNumEx': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_double)),

    # bool GetExposureMode(bool EM)
    'GetExposureMode': (ctypes.c_bool, (ctypes.c_bool,)),

    # int32_t SetExposureMode(bool EM)
    'SetExposureMode': (ctypes.c_int32, (ctypes.c_bool,)),

    # int32_t GetExposureModeNum(int32_t num, bool EM)
    'GetExposureModeNum': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_bool)),

    # int32_t SetExposureModeNum(int32_t num, bool EM)
    'SetExposureModeNum': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_bool)),

    # int32_t GetExposureRange(int32_t ER)
    'GetExposureRange': (ctypes.c_int32, (ctypes.c_int32,)),

    # double GetExposureRangeEx(int32_t ER)
    'GetExposureRangeEx': (ctypes.c_double, (ctypes.c_int32,)),

    # int32_t GetAutoExposureSetting(int32_t num, int32_t AES, int32_t* iVal, double* dVal)
    'GetAutoExposureSetting': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_double))),

    # int32_t SetAutoExposureSetting(int32_t num, int32_t AES, int32_t iVal, double dVal)
    'SetAutoExposureSetting': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_double)),


    # uint16_t GetResultMode(uint16_t RM)
    'GetResultMode': (ctypes.c_uint16, (ctypes.c_uint16,)),

    # int32_t SetResultMode(uint16_t RM)
    'SetResultMode': (ctypes.c_int32, (ctypes.c_uint16,)),

    # uint16_t GetRange(uint16_t R)
    'GetRange': (ctypes.c_uint16, (ctypes.c_uint16,)),

    # int32_t SetRange(uint16_t R)
    'SetRange': (ctypes.c_int32, (ctypes.c_uint16,)),

    # uint16_t GetPulseMode(uint16_t PM)
    'GetPulseMode': (ctypes.c_uint16, (ctypes.c_uint16,)),

    # int32_t SetPulseMode(uint16_t PM)
    'SetPulseMode': (ctypes.c_int32, (ctypes.c_uint16,)),

    # int32_t GetPulseDelay(int32_t PD)
    'GetPulseDelay': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t SetPulseDelay(int32_t PD)
    'SetPulseDelay': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetPulseIntegration(int32_t PI)
    'GetPulseIntegration': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t SetPulseIntegration(int32_t PI)
    'SetPulseIntegration': (ctypes.c_int32, (ctypes.c_int32,)),

    # uint16_t GetWideMode(uint16_t WM)
    'GetWideMode': (ctypes.c_uint16, (ctypes.c_uint16,)),

    # int32_t SetWideMode(uint16_t WM)
    'SetWideMode': (ctypes.c_int32, (ctypes.c_uint16,)),


    # int32_t GetDisplayMode(int32_t DM)
    'GetDisplayMode': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t SetDisplayMode(int32_t DM)
    'SetDisplayMode': (ctypes.c_int32, (ctypes.c_int32,)),

    # bool GetFastMode(bool FM)
    'GetFastMode': (ctypes.c_bool, (ctypes.c_bool,)),

    # int32_t SetFastMode(bool FM)
    'SetFastMode': (ctypes.c_int32, (ctypes.c_bool,)),


    # bool GetLinewidthMode(bool LM)
    'GetLinewidthMode': (ctypes.c_bool, (ctypes.c_bool,)),

    # int32_t SetLinewidthMode(bool LM)
    'SetLinewidthMode': (ctypes.c_int32, (ctypes.c_bool,)),


    # bool GetDistanceMode(bool DM)
    'GetDistanceMode': (ctypes.c_bool, (ctypes.c_bool,)),

    # int32_t SetDistanceMode(bool DM)
    'SetDistanceMode': (ctypes.c_int32, (ctypes.c_bool,)),


    # int32_t GetSwitcherMode(int32_t SM)
    'GetSwitcherMode': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t SetSwitcherMode(int32_t SM)
    'SetSwitcherMode': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetSwitcherChannel(int32_t CH)
    'GetSwitcherChannel': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t SetSwitcherChannel(int32_t CH)
    'SetSwitcherChannel': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetSwitcherSignalStates(int32_t Signal, int32_t* Use, int32_t* Show)
    'GetSwitcherSignalStates': (ctypes.c_int32, (ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32))),

    # int32_t SetSwitcherSignalStates(int32_t Signal, int32_t Use, int32_t Show)
    'SetSwitcherSignalStates': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)),

    # int32_t SetSwitcherSignal(int32_t Signal, int32_t Use, int32_t Show)
    'SetSwitcherSignal': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)),


    # int32_t GetAutoCalMode(int32_t ACM)
    'GetAutoCalMode': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t SetAutoCalMode(int32_t ACM)
    'SetAutoCalMode': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetAutoCalSetting(int32_t ACS, int32_t* val, int32_t Res1, int32_t* Res2)
    'GetAutoCalSetting': (ctypes.c_int32, (ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32))),

    # int32_t SetAutoCalSetting(int32_t ACS, int32_t val, int32_t Res1, int32_t Res2)
    'SetAutoCalSetting': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)),


    # int32_t GetActiveChannel(int32_t Mode, int32_t* Port, int32_t Res1)
    'GetActiveChannel': (ctypes.c_int32, (ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32)),

    # int32_t SetActiveChannel(int32_t Mode, int32_t Port, int32_t CH, int32_t Res1)
    'SetActiveChannel': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)),

    # int32_t GetChannelsCount(int32_t C)
    'GetChannelsCount': (ctypes.c_int32, (ctypes.c_int32,)),


    # uint16_t GetOperationState(uint16_t OS)
    'GetOperationState': (ctypes.c_uint16, (ctypes.c_uint16,)),

    # int32_t Operation(uint16_t Op)
    'Operation': (ctypes.c_int32, (ctypes.c_uint16,)),

    # int32_t SetOperationFile(char* lpFile)
    'SetOperationFile': (ctypes.c_int32, (ctypes.POINTER(ctypes.c_char),)),

    # int32_t Calibration(int32_t Type, int32_t Unit, double Value, int32_t Channel)
    'Calibration': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_double, ctypes.c_int32)),

    # int32_t PowerCalibration(int32_t Unit, double Value, int32_t Channel, int32_t Options, int32_t Res)
    'PowerCalibration': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_double, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)),

    # int32_t RaiseMeasurementEvent(int32_t Mode)
    'RaiseMeasurementEvent': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t TriggerMeasurement(int32_t Action)
    'TriggerMeasurement': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetTriggerState(int32_t TS)
    'GetTriggerState': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetInterval(int32_t I)
    'GetInterval': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t SetInterval(int32_t I)
    'SetInterval': (ctypes.c_int32, (ctypes.c_int32,)),

    # bool GetIntervalMode(bool IM)
    'GetIntervalMode': (ctypes.c_bool, (ctypes.c_bool,)),

    # int32_t SetIntervalMode(bool IM)
    'SetIntervalMode': (ctypes.c_int32, (ctypes.c_bool,)),

    # double GetInternalTriggerRate(double TR)
    'GetInternalTriggerRate': (ctypes.c_double, (ctypes.c_double,)),

    # int32_t SetInternalTriggerRate(double TR)
    'SetInternalTriggerRate': (ctypes.c_int32, (ctypes.c_double,)),

    # int32_t GetBackground(int32_t BG)
    'GetBackground': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t SetBackground(int32_t BG)
    'SetBackground': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetAveragingSettingNum(int32_t num, int32_t AS, int32_t Value)
    'GetAveragingSettingNum': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)),

    # int32_t SetAveragingSettingNum(int32_t num, int32_t AS, int32_t Value)
    'SetAveragingSettingNum': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)),


    # bool GetLinkState(bool LS)
    'GetLinkState': (ctypes.c_bool, (ctypes.c_bool,)),

    # int32_t SetLinkState(bool LS)
    'SetLinkState': (ctypes.c_int32, (ctypes.c_bool,)),

    # void LinkSettingsDlg(void)
    'LinkSettingsDlg': (None, ()),


    # int32_t GetPatternItemSize(int32_t Index)
    'GetPatternItemSize': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetPatternItemCount(int32_t Index)
    'GetPatternItemCount': (ctypes.c_int32, (ctypes.c_int32,)),

    # uintptr_t GetPattern(int32_t Index)
    'GetPattern': (ctypes.c_void_p, (ctypes.c_int32,)),

    # uintptr_t GetPatternNum(int32_t Chn, int32_t Index)
    'GetPatternNum': (ctypes.c_void_p, (ctypes.c_int32, ctypes.c_int32)),

    # int32_t GetPatternData(int32_t Index, uintptr_t PArray)
    'GetPatternData': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_void_p)),

    # int32_t GetPatternDataNum(int32_t Chn, int32_t Index, uintptr_t PArray)
    'GetPatternDataNum': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_void_p)),

    # int32_t SetPattern(int32_t Index, int32_t iEnable)
    'SetPattern': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32)),

    # int32_t SetPatternData(int32_t Index, uintptr_t PArray)
    'SetPatternData': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_void_p)),


    # bool GetAnalysisMode(bool AM)
    'GetAnalysisMode': (ctypes.c_bool, (ctypes.c_bool,)),

    # int32_t SetAnalysisMode(bool AM)
    'SetAnalysisMode': (ctypes.c_int32, (ctypes.c_bool,)),

    # int32_t GetAnalysisItemSize(int32_t Index)
    'GetAnalysisItemSize': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetAnalysisItemCount(int32_t Index)
    'GetAnalysisItemCount': (ctypes.c_int32, (ctypes.c_int32,)),

    # uintptr_t GetAnalysis(int32_t Index)
    'GetAnalysis': (ctypes.c_void_p, (ctypes.c_int32,)),

    # int32_t GetAnalysisData(int32_t Index, uintptr_t PArray)
    'GetAnalysisData': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_void_p)),

    # int32_t SetAnalysis(int32_t Index, int32_t iEnable)
    'SetAnalysis': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32)),


    # int32_t GetMinPeak(int32_t M1)
    'GetMinPeak': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetMinPeak2(int32_t M2)
    'GetMinPeak2': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetMaxPeak(int32_t X1)
    'GetMaxPeak': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetMaxPeak2(int32_t X2)
    'GetMaxPeak2': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetAvgPeak(int32_t A1)
    'GetAvgPeak': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t GetAvgPeak2(int32_t A2)
    'GetAvgPeak2': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t SetAvgPeak(int32_t PA)
    'SetAvgPeak': (ctypes.c_int32, (ctypes.c_int32,)),


    # int32_t GetAmplitudeNum(int32_t num, int32_t Index, int32_t A)
    'GetAmplitudeNum': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)),

    # double GetIntensityNum(int32_t num, double I)
    'GetIntensityNum': (ctypes.c_double, (ctypes.c_int32, ctypes.c_double)),

    # double GetPowerNum(int32_t num, double P)
    'GetPowerNum': (ctypes.c_double, (ctypes.c_int32, ctypes.c_double)),


    # uint16_t GetDelay(uint16_t D)
    'GetDelay': (ctypes.c_uint16, (ctypes.c_uint16,)),

    # int32_t SetDelay(uint16_t D)
    'SetDelay': (ctypes.c_int32, (ctypes.c_uint16,)),

    # uint16_t GetShift(uint16_t S)
    'GetShift': (ctypes.c_uint16, (ctypes.c_uint16,)),

    # int32_t SetShift(uint16_t S)
    'SetShift': (ctypes.c_int32, (ctypes.c_uint16,)),

    # uint16_t GetShift2(uint16_t S2)
    'GetShift2': (ctypes.c_uint16, (ctypes.c_uint16,)),

    # int32_t SetShift2(uint16_t S2)
    'SetShift2': (ctypes.c_int32, (ctypes.c_uint16,)),

    # double GetGain(int32_t num, int32_t index, int32_t mode, double* Gain)
    'GetGain': (ctypes.c_double, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_double))),

    # int32_t SetGain(int32_t num, int32_t index, int32_t mode, double Gain)
    'SetGain': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_double)),


# ***********  Deviation (Laser Control) and PID-functions  ************
    # bool GetDeviationMode(bool DM)
    'GetDeviationMode': (ctypes.c_bool, (ctypes.c_bool,)),

    # int32_t SetDeviationMode(bool DM)
    'SetDeviationMode': (ctypes.c_int32, (ctypes.c_bool,)),

    # double GetDeviationReference(double DR)
    'GetDeviationReference': (ctypes.c_double, (ctypes.c_double,)),

    # int32_t SetDeviationReference(double DR)
    'SetDeviationReference': (ctypes.c_int32, (ctypes.c_double,)),

    # int32_t GetDeviationSensitivity(int32_t DS)
    'GetDeviationSensitivity': (ctypes.c_int32, (ctypes.c_int32,)),

    # int32_t SetDeviationSensitivity(int32_t DS)
    'SetDeviationSensitivity': (ctypes.c_int32, (ctypes.c_int32,)),

    # double GetDeviationSignal(double DS)
    'GetDeviationSignal': (ctypes.c_double, (ctypes.c_double,)),

    # double GetDeviationSignalNum(int32_t Port, double DS)
    'GetDeviationSignalNum': (ctypes.c_double, (ctypes.c_int32, ctypes.c_double)),

    # int32_t SetDeviationSignal(double DS)
    'SetDeviationSignal': (ctypes.c_int32, (ctypes.c_double,)),

    # int32_t SetDeviationSignalNum(int32_t Port, double DS)
    'SetDeviationSignalNum': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_double)),

    # double RaiseDeviationSignal(int32_t iType, double dSignal)
    'RaiseDeviationSignal': (ctypes.c_double, (ctypes.c_int32, ctypes.c_double)),


    # int32_t GetPIDCourse(char* PIDC)
    'GetPIDCourse': (ctypes.c_int32, (ctypes.POINTER(ctypes.c_char),)),

    # int32_t SetPIDCourse(char* PIDC)
    'SetPIDCourse': (ctypes.c_int32, (ctypes.POINTER(ctypes.c_char),)),

    # int32_t GetPIDCourseNum(int32_t Port, char* PIDC)
    'GetPIDCourseNum': (ctypes.c_int32, (ctypes.c_int32, ctypes.POINTER(ctypes.c_char))),

    # int32_t SetPIDCourseNum(int32_t Port, char* PIDC)
    'SetPIDCourseNum': (ctypes.c_int32, (ctypes.c_int32, ctypes.POINTER(ctypes.c_char))),

    # int32_t GetPIDSetting(int32_t PS, int32_t Port, int32_t* iSet, double* dSet)
    'GetPIDSetting': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_double))),

    # int32_t SetPIDSetting(int32_t PS, int32_t Port, int32_t iSet, double dSet)
    'SetPIDSetting': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_double)),

    # int32_t GetLaserControlSetting(int32_t PS, int32_t Port, int32_t* iSet, double* dSet, char* sSet)
    'GetLaserControlSetting': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_char))),

    # int32_t SetLaserControlSetting(int32_t PS, int32_t Port, int32_t iSet, double dSet, char* sSet)
    'SetLaserControlSetting': (ctypes.c_int32, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_double, ctypes.POINTER(ctypes.c_char))),

    # int32_t ClearPIDHistory(int32_t Port)
    'ClearPIDHistory': (ctypes.c_int32, (ctypes.c_int32,)),


# ***********  Other...-functions  *************************************
    # double ConvertUnit(double Val, int32_t uFrom, int32_t uTo)
    'ConvertUnit': (ctypes.c_double, (ctypes.c_double, ctypes.c_int32, ctypes.c_int32)),

    # double ConvertDeltaUnit(double Base, double Delta, int32_t uBase, int32_t uFrom, int32_t uTo)
    'ConvertDeltaUnit': (ctypes.c_double, (ctypes.c_double, ctypes.c_double, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)),


# ***********  Obsolete...-functions  **********************************
    # bool GetReduced(bool R)
    'GetReduced': (ctypes.c_bool, (ctypes.c_bool,)),

    # int32_t SetReduced(bool R)
    'SetReduced': (ctypes.c_int32, (ctypes.c_bool,)),

    # uint16_t GetScale(uint16_t S)
    'GetScale': (ctypes.c_uint16, (ctypes.c_uint16,)),

    # int32_t SetScale(uint16_t S)
    'SetScale': (ctypes.c_int32, (ctypes.c_uint16,)),


}

dll = None # pylint: disable=invalid-name

def LoadDLL(path = None): # pylint: disable=invalid-name
    """Load wlmData library"""
    global dll # pylint: disable=global-statement

    if path is None:
        if platform.system() == 'Windows':
            path = 'wlmData.dll'
        elif platform.system() == 'Darwin':
            path = 'libwlmData.dylib'
        else:
            path = 'libwlmData.so'

    dll = ctypes.WinDLL(path) if platform.system() == 'Windows' else ctypes.CDLL(path)

    for name, (restype, argtypes) in _PROTOTYPES.items():
        try:
            fnptr = getattr(dll, name)
        except AttributeError:
            continue
        fnptr.argtypes = argtypes
        fnptr.restype = restype

    return dll
