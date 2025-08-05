from ctypes import *
import ctypes.util
import time
import platform
import os, sys
from typing import Union, List

MAX_PATH = 256


class ATSpectrograph:
    __version__ = '0.1'
  
    def __init__(self, userPath = None):   
        self.dll = self._load_library(userPath)

    def _load_library(self, userPath)-> Union[WinDLL, CDLL]:
        if sys.platform == "linux":
          return cdll.LoadLibrary("/usr/local/lib/libatspectrograph.so")
        elif sys.platform == "win32":
            if userPath is not None:
                _path = userPath + ';' + os.environ['PATH']
                os.environ['PATH'] = _path
            dllname = "atspectrograph.dll"
            path = ctypes.util.find_library(dllname)    
        
            return windll.LoadLibrary(path)
        else:
            print("Cannot detect operating system, will now stop")
            raise

    # Error Code Returns and Definitions
    ATSPECTROGRAPH_COMMUNICATION_ERROR = 20201
    ATSPECTROGRAPH_SUCCESS = 20202
    ATSPECTROGRAPH_ERROR = 20249
    ATSPECTROGRAPH_P1INVALID = 20266
    ATSPECTROGRAPH_P2INVALID = 20267
    ATSPECTROGRAPH_P3INVALID = 20268
    ATSPECTROGRAPH_P4INVALID = 20269
    ATSPECTROGRAPH_P5INVALID = 20270
    ATSPECTROGRAPH_NOT_INITIALIZED = 20275
    ATSPECTROGRAPH_NOT_AVAILABLE = 20292
    INPUT_FLIPPER = 1
    OUTPUT_FLIPPER = 2
    DIRECT = 0
    SIDE = 1
    INPUT_SIDE = 1
    INPUT_DIRECT = 2
    OUTPUT_SIDE = 3
    OUTPUT_DIRECT = 4
    SHUTTER_CLOSED = 0
    SHUTTER_OPEN = 1
    SHUTTER_BNC = 2
    ATSPECTROGRAPH_ERRORLENGTH = 64

    def IsAccessoryPresent(self, device):
        """ 
            Description:
              Finds if Accessory is present.

            Synopsis:
              (ret, present) = IsAccessoryPresent(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Accessory presence flag returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              present - pointer to flag::
                0 - Accessory is NOT present
                1 - Accessory IS present

            C++ Equiv:
              unsigned int IsAccessoryPresent(int device, int * present);

            See Also:
              GetAccessoryState SetAccessory 

        """
        cdevice = c_int(device)
        cpresent = c_int()
        ret = self.dll.ATSpectrographAccessoryIsPresent(cdevice, byref(cpresent))
        return (ret, cpresent.value)

    def AtZeroOrder(self, device):
        """ 
            Description:
              Finds if wavelength is at zero order.

            Synopsis:
              (ret, atZeroOrder) = AtZeroOrder(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - At zero order flag returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              atZeroOrder - pointer to flag::
                0 - wavelength is NOT at zero order
                1 - wavelength IS at zero order

            C++ Equiv:
              unsigned int AtZeroOrder(int device, int * atZeroOrder);

            See Also:
              IsWavelengthPresent GetWavelength GetWavelengthLimits SetWavelength GotoZeroOrder 

        """
        cdevice = c_int(device)
        catZeroOrder = c_int()
        ret = self.dll.ATSpectrographAtZeroOrder(cdevice, byref(catZeroOrder))
        return (ret, catZeroOrder.value)

    def Close(self):
        """ 
            Description:
              Closes the spectrograph system down.

            Synopsis:
              ret = Close()

            Inputs:
              None

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - spectrograph shut down

            C++ Equiv:
              unsigned int Close(void);

            See Also:
              Initialize GetNumberDevices GetFunctionReturnDescription 

        """
        ret = self.dll.ATSpectrographClose()
        return (ret)

    def EepromGetOpticalParams(self, device):
        """ 
            Description:
              Returns the Focal Length, Angular Deviation and Focal Tilt from the spectrograph device.

            Synopsis:
              (ret, FocalLength, AngularDeviation, FocalTilt) = EepromGetOpticalParams(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Focal Length, Angular Deviation and Focal Tilt returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              FocalLength - pointer to Focal Length
              AngularDeviation - pointer to Angular Deviation
              FocalTilt - pointer to Focal Tilt

            C++ Equiv:
              unsigned int EepromGetOpticalParams(int device, float * FocalLength, float * AngularDeviation, float * FocalTilt);

            See Also:
              GetSerialNumber 

        """
        cdevice = c_int(device)
        cFocalLength = c_float()
        cAngularDeviation = c_float()
        cFocalTilt = c_float()
        ret = self.dll.ATSpectrographEepromGetOpticalParams(cdevice, byref(cFocalLength), byref(cAngularDeviation), byref(cFocalTilt))
        return (ret, cFocalLength.value, cAngularDeviation.value, cFocalTilt.value)

    def EepromSetOpticalParams(self, device, focalLength, angularDeviation, focalTilt):
        """ 
            Description:
              Sets the Focal Length, Angular Deviation and Focal Tilt on the spectrograph device.

            Synopsis:
              ret = EepromSetOpticalParams(device, focalLength, angularDeviation, focalTilt)

            Inputs:
              device - spectrograph to interrogate 
              FocalLength - pointer to Focal Length
              AngularDeviation - pointer to Angular Deviation
              FocalTilt - pointer to Focal Tilt

            Outputs:
              ret - Function Return Code

            C++ Equiv:
              int EepromSetOpticalParams(int device, float focalLength, float angularDeviation, float focalTilt);

        """
        cdevice = c_int(device)
        cfocalLength = c_float(focalLength)
        cangularDeviation = c_float(angularDeviation)
        cfocalTilt = c_float(focalTilt)
        ret = self.dll.ATSpectrographEepromSetOpticalParams(cdevice, cfocalLength, cangularDeviation, cfocalTilt)
        return (ret)

    def IsFilterPresent(self, device):
        """ 
            Description:
              Finds if Filter is present.

            Synopsis:
              (ret, present) = IsFilterPresent(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Filter presence flag returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              present - pointer to flag::
                0 - Filter is NOT present
                1 - Filter IS present

            C++ Equiv:
              unsigned int IsFilterPresent(int device, int * present);

            See Also:
              GetFilter SetFilter GetFilterInfo SetFilterInfo 

        """
        cdevice = c_int(device)
        cpresent = c_int()
        ret = self.dll.ATSpectrographFilterIsPresent(cdevice, byref(cpresent))
        return (ret, cpresent.value)

    def FilterReset(self, device):
        """ 
            Description:
              Resets the filter to its default position. 
              

            Synopsis:
              ret = FilterReset(device)

            Inputs:
              device - spectrograph to reset the filter

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Filter reset
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int FilterReset(int device);

            See Also:
              SetFilter GetFilter SetFilterInfo GetFilterInfo IsFilterPresent 

        """
        cdevice = c_int(device)
        ret = self.dll.ATSpectrographFilterReset(cdevice)
        return (ret)

    def IsFlipperMirrorPresent(self, device, flipper):
        """ 
            Description:
              Finds if Flipper is present.
              

            Synopsis:
              (ret, present) = IsFlipperMirrorPresent(device, flipper)

            Inputs:
              device - spectrograph to interrogate
              flipper - The flipper can have two values which are as follows::
                 INPUT_FLIPPER (1) - 
                OUTPUT_FLIPPER  (2) - 

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Flipper presence flag returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid flipper
                ATSPECTROGRAPH_P3INVALID - Invalid present
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              present -  pointer to flag:
                0 - Flipper is NOT present
                1 - Flipper is present

            C++ Equiv:
              unsigned int FlipperMirrorIsPresent(int device, int flipper, int * present);

            See Also:
              SetFlipperMirror GetFlipperMirror FlipperMirrorReset GetCCDLimits 

        """
        cdevice = c_int(device)
        cflipper = c_int(flipper)
        cpresent = c_int()
        ret = self.dll.ATSpectrographFlipperMirrorIsPresent(cdevice, cflipper, byref(cpresent))
        return (ret, cpresent.value)

    def FlipperMirrorReset(self, device, flipper):
        """ 
            Description:
              Resets the specified flipper to its default.
              

            Synopsis:
              ret = FlipperMirrorReset(device, flipper)

            Inputs:
              device -  spectrograph to interrogate
              flipper - The flipper can have two values which are as follows::
              INPUT_FLIPPER (1) - 
              OUTPUT_FLIPPER ( 2) - 

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Flipper reset
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid flipper
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int FlipperMirrorReset(int device, int flipper);

            See Also:
              SetFlipperMirror GetFlipperMirror GetCCDLimits IsFlipperMirrorPresent 

        """
        cdevice = c_int(device)
        cflipper = c_int(flipper)
        ret = self.dll.ATSpectrographFlipperMirrorReset(cdevice, cflipper)
        return (ret)

    def IsFocusMirrorPresent(self, device):
        """ 
            Description:
              Resets the filter to its default position.

            Synopsis:
              (ret, present) = IsFocusMirrorPresent(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Focus Mirror presence flag returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              present - pointer to flag: 
                0 Focus Mirror is NOT present
                1 Focus Mirror IS present

            C++ Equiv:
              unsigned int FocusMirrorIsPresent(int device, int * present);

            See Also:
              SetFocusMirror GetFocusMirror GetFocusMirrorMaxSteps IsFocusMirrorPresent 

        """
        cdevice = c_int(device)
        cpresent = c_int()
        ret = self.dll.ATSpectrographFocusMirrorIsPresent(cdevice, byref(cpresent))
        return (ret, cpresent.value)

    def FocusMirrorReset(self, device):
        """ 
            Description:
              Resets the filter to its default position.

            Synopsis:
              ret = FocusMirrorReset(device)

            Inputs:
              device - spectrograph to reset the filter

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Focus Mirror reset
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int FocusMirrorReset(int device);

            See Also:
              SetFocusMirror GetFocusMirror GetFocusMirrorMaxSteps IsFocusMirrorPresent 

        """
        cdevice = c_int(device)
        ret = self.dll.ATSpectrographFocusMirrorReset(cdevice)
        return (ret)

    def GetAccessoryState(self, device, Accessory):
        """ 
            Description:
              Gets the Accessory state.

            Synopsis:
              (ret, state) = GetAccessoryState(device, Accessory)

            Inputs:
              device - spectrograph to interrogate
              Accessory - line to interrogate::
                1 - line 1
                2 - line 2

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Line state returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid line
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              state - pointer to line state::
                0 - OFF
                1 - ON

            C++ Equiv:
              unsigned int GetAccessoryState(int device, int Accessory, int * state);

            See Also:
              SetAccessory IsAccessoryPresent 

        """
        cdevice = c_int(device)
        cAccessory = c_int(Accessory)
        cstate = c_int()
        ret = self.dll.ATSpectrographGetAccessoryState(cdevice, cAccessory, byref(cstate))
        return (ret, cstate.value)

    def GetCalibration(self, device, NumberPixels):
        """ 
            Description:
              Obtains the wavelength calibration of each pixel of attached sensor.

            Synopsis:
              (ret, CalibrationValues) = GetCalibration(device, NumberPixels)

            Inputs:
              device - Select spectrograph to control
              NumberPixels - number of pixels of attached sensor

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - port set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P3INVALID - Invalid number
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              CalibrationValues - wavelength calibration of each pixel of attached sensor

            C++ Equiv:
              unsigned int GetCalibration(int device, float * CalibrationValues, int NumberPixels);

            See Also:
              GetPixelWidth SetPixelWidth GetNumberPixels SetNumberPixels 

        """
        cdevice = c_int(device)
        cCalibrationValues = (c_float * NumberPixels)()
        cNumberPixels = c_int(NumberPixels)
        ret = self.dll.ATSpectrographGetCalibration(cdevice, cCalibrationValues, cNumberPixels)
        arr = []
        for data in cCalibrationValues:
          arr.append(round(data, 6))
        return (ret, arr)

    def GetCCDLimits(self, device, port):
        """ 
            Description:
              Gets the upper and lower accessible wavelength through the port.

            Synopsis:
              (ret, Low, High) = GetCCDLimits(device, port)

            Inputs:
              device - spectrograph to interrogate
              port - port to interrogate:
                1 - port 1
                2 - port 2

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Accessible wavelength limits returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid port
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              Low - pointer to lower accessible wavelength (nm)
              High - pointer to upper accessible wavelength (nm)

            C++ Equiv:
              unsigned int GetCCDLimits(int device, int port, float * Low, float * High);

            See Also:
              GetPort SetPort 

        """
        cdevice = c_int(device)
        cport = c_int(port)
        cLow = c_float()
        cHigh = c_float()
        ret = self.dll.ATSpectrographGetCCDLimits(cdevice, cport, byref(cLow), byref(cHigh))
        return (ret, cLow.value, cHigh.value)

    def GetDetectorOffset(self, device, entrancePort, exitPort):
        """ 
            Description:
              Sets the detector offset. Use this function if the system has 4 ports and a detector offset value of a specific entrance and exit port combination is required.
              DIRECT, DIRECT = 0, 0
              DIRECT, SIDE = 0, 1
              SIDE, DIRECT = 1, 0
              SIDE, SIDE = 1, 1

            Synopsis:
              (ret, offset) = GetDetectorOffset(device, entrancePort, exitPort)

            Inputs:
              device - spectrograph to interrogate
              entrancePort - Select entrance port to use
              exitPort - Select exit port to use

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Detector offset set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              offset - pointer to detector offset (steps)

            C++ Equiv:
              unsigned int GetDetectorOffset(int device, int entrancePort, int exitPort, int * offset);

            See Also:
              IsGratingPresent GetTurret GetNumberGratings GetGrating GetGratingInfo GetGratingOffset GetDetectorOffset SetDetectorOffsetEx SetDetectorOffset SetTurret SetGrating WavelengthReset SetGratingOffset 

        """
        cdevice = c_int(device)
        centrancePort = c_int(entrancePort)
        cexitPort = c_int(exitPort)
        coffset = c_int()
        ret = self.dll.ATSpectrographGetDetectorOffset(cdevice, centrancePort, cexitPort, byref(coffset))
        return (ret, coffset.value)

    def GetFilter(self, device):
        """ 
            Description:
              Gets current Filter.

            Synopsis:
              (ret, filter) = GetFilter(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Filter returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              filter - pointer to Filter

            C++ Equiv:
              unsigned int GetFilter(int device, int * filter);

            See Also:
              IsFilterPresent GetFilterInfo SetFilter SetFilterInfo 

        """
        cdevice = c_int(device)
        cfilter = c_int()
        ret = self.dll.ATSpectrographGetFilter(cdevice, byref(cfilter))
        return (ret, cfilter.value)

    def GetFilterInfo(self, device, Filter, maxInfoLen):
        """ 
            Description:
              Gets the filter information.

            Synopsis:
              (ret, info) = GetFilterInfo(device, Filter, maxInfoLen)

            Inputs:
              device - spectrograph to interrogate
              Filter - Filter to interrogate
              maxInfoLen - maximum string length

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Filter information returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid filter
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              Info - pointer to the filter information

            C++ Equiv:
              unsigned int GetFilterInfo(int device, int Filter, char * info, int maxInfoLen);

            See Also:
              IsFilterPresent GetFilter SetFilter SetFilterInfo 

        """
        cdevice = c_int(device)
        cFilter = c_int(Filter)
        cInfo = create_string_buffer(maxInfoLen)
        cmaxInfoLen = c_int(maxInfoLen)
        ret = self.dll.ATSpectrographGetFilterInfo(cdevice, cFilter, cInfo, cmaxInfoLen)
        return (ret, cInfo.value.decode("utf-8"))

    def GetFlipperMirror(self, device, flipper):
        """ 
            Description:
              Returns the current port for the specified flipper mirror.
              

            Synopsis:
              (ret, port) = GetFlipperMirror(device, flipper)

            Inputs:
              device - spectrograph to interrogate
              flipper - The flipper can have two values which are as follows:
                :
                INPUT_FLIPPER - 1
                OUTPUT_FLIPPER - 2

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - port returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              port - pointer to the current port:
                DIRECT - 0
                SIDE - 1

            C++ Equiv:
              unsigned int GetFlipperMirror(int device, int flipper, int * port);

            See Also:
              IsFlipperMirrorPresent GetCCDLimits SetFlipperMirror FlipperMirrorReset 

        """
        cdevice = c_int(device)
        cflipper = c_int(flipper)
        cport = c_int()
        ret = self.dll.ATSpectrographGetFlipperMirror(cdevice, cflipper, byref(cport))
        return (ret, cport.value)

    def GetFlipperMirrorMaxPosition(self, device, flipper):
        """ 
            Description:
              Returns the maximum position for the specified flipper mirror.

            Synopsis:
              (ret, position) = GetFlipperMirrorMaxPosition(device, flipper)

            Inputs:
              device - spectrograph to interrogate
              flipper - The flipper can have two values which are as follows:
                INPUT_FLIPPER 1
                OUTPUT_FLIPPER 2

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - position returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              position - pointer to the maximum flipper mirror position

            C++ Equiv:
              unsigned int GetFlipperMirrorMaxPosition(int device, int flipper, int * position);

            See Also:
              IsFlipperMirrorPresent GetFlipperMirrorPosition SetFlipperMirrorPosition FlipperMirrorReset 

        """
        cdevice = c_int(device)
        cflipper = c_int(flipper)
        cposition = c_int()
        ret = self.dll.ATSpectrographGetFlipperMirrorMaxPosition(cdevice, cflipper, byref(cposition))
        return (ret, cposition.value)

    def GetFlipperMirrorPosition(self, device , flipper):
        """ 
            Description:
              Returns the current position for the specified flipper mirror.

            Synopsis:
              (ret, position) = GetFlipperMirrorPosition(device , flipper)

            Inputs:
              device  - spectrograph to interrogate
              flipper - The flipper can have two values which are as follows:
                INPUT_FLIPPER 1
                OUTPUT_FLIPPER 2

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - position returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              position - pointer to the current flipper mirror position

            C++ Equiv:
              unsigned int GetFlipperMirrorPosition(int device , int flipper, int * position);

            See Also:
              IsFlipperMirrorPresent GetFlipperMirrorMaxPosition SetFlipperMirrorPosition FlipperMirrorReset 

        """
        cdevice  = c_int(device )
        cflipper = c_int(flipper)
        cposition = c_int()
        ret = self.dll.ATSpectrographGetFlipperMirrorPosition(cdevice , cflipper, byref(cposition))
        return (ret, cposition.value)

    def GetFocusMirror(self, device):
        """ 
            Description:
              Gets current focus position in steps.

            Synopsis:
              (ret, focus) = GetFocusMirror(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Current focus position returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              focus - pointer to focus 

            C++ Equiv:
              unsigned int GetFocusMirror(int device, int * focus);

            See Also:
              SetFocusMirror GetFocusMirrorMaxSteps FocusMirrorReset IsFocusMirrorPresent 

        """
        cdevice = c_int(device)
        cfocus = c_int()
        ret = self.dll.ATSpectrographGetFocusMirror(cdevice, byref(cfocus))
        return (ret, cfocus.value)

    def GetFocusMirrorMaxSteps(self, device):
        """ 
            Description:
              Gets maximum possible focus position in steps.

            Synopsis:
              (ret, steps) = GetFocusMirrorMaxSteps(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Max focus position returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              steps - pointer to steps

            C++ Equiv:
              unsigned int GetFocusMirrorMaxSteps(int device, int * steps);

            See Also:
              SetFocusMirror GetFocusMirror FocusMirrorReset IsFocusMirrorPresent 

        """
        cdevice = c_int(device)
        csteps = c_int()
        ret = self.dll.ATSpectrographGetFocusMirrorMaxSteps(cdevice, byref(csteps))
        return (ret, csteps.value)

    def GetFunctionReturnDescription(self, error, MaxDescStrLen):
        """ 
            Description:
              Returns a short description of an Error Code.

            Synopsis:
              (ret, description) = GetFunctionReturnDescription(error, MaxDescStrLen)

            Inputs:
              error - Error Code to identify
              MaxDescStrLen - number of char allocated for the description string

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Error Code description returned
                ATSPECTROGRAPH_P3INVALID - Invalid MaxDescStrLen
              description - pointer to the Error Code description

            C++ Equiv:
              unsigned int GetFunctionReturnDescription(int error, char * description, int MaxDescStrLen);

            See Also:
              Initialize GetNumberDevices Close 

            Note: Returns a short description of an Error Code.

        """
        cerror = c_int(error)
        cdescription = create_string_buffer(MaxDescStrLen)
        cMaxDescStrLen = c_int(MaxDescStrLen)
        ret = self.dll.ATSpectrographGetFunctionReturnDescription(cerror, cdescription, cMaxDescStrLen)
        return (ret, cdescription.value.decode("utf-8"))

    def GetGrating(self, device):
        """ 
            Description:
              Returns the current grating.

            Synopsis:
              (ret, grating) = GetGrating(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - grating returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              grating - pointer to grating

            C++ Equiv:
              unsigned int GetGrating(int device, int * grating);

            See Also:
              IsGratingPresent GetTurret GetNumberGratings GetGratingInfo GetGratingOffset GetDetectorOffset SetTurret SetGrating WavelengthReset SetGratingOffset SetDetectorOffset 

        """
        cdevice = c_int(device)
        cgrating = c_int()
        ret = self.dll.ATSpectrographGetGrating(cdevice, byref(cgrating))
        return (ret, cgrating.value)

    def GetGratingInfo(self, device, Grating, maxBlazeStrLen):
        """ 
            Description:
              Returns the grating information

            Synopsis:
              (ret, lines, blaze, home, offset) = GetGratingInfo(device, Grating, maxBlazeStrLen)

            Inputs:
              device - spectrograph to interrogate
              Grating - grating to interrogate
              maxBlazeStrLen - maximum string length

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - grating information returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid grating
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              Lines - pointer to the grating lines/mm
              Blaze - pointer to the grating blaze wavelength (nm)
              Home - pointer to the grating home (steps)
              Offset - pointer to the grating offset (steps)

            C++ Equiv:
              unsigned int GetGratingInfo(int device, int Grating, float * Lines, char * Blaze, int * Home, int * Offset);

            See Also:
              IsGratingPresent GetTurret GetNumberGratings GetGrating GetGratingOffset GetDetectorOffset SetTurret SetGrating WavelengthReset SetGratingOffset SetDetectorOffset 

        """
        cdevice = c_int(device)
        cGrating = c_int(Grating)
        cLines = c_float()
        cBlaze = create_string_buffer(maxBlazeStrLen)
        cmaxBlazeStrLen = c_int(maxBlazeStrLen)
        cHome = c_int()
        cOffset = c_int()
        ret = self.dll.ATSpectrographGetGratingInfo(cdevice, cGrating, byref(cLines), cBlaze, cmaxBlazeStrLen, byref(cHome), byref(cOffset))
        return (ret, round(cLines.value, 6), cBlaze.value.decode("utf-8"), cHome.value, cOffset.value)

    def GetGratingOffset(self, device, Grating):
        """ 
            Description:
              Returns the grating offset

            Synopsis:
              (ret, offset) = GetGratingOffset(device, Grating)

            Inputs:
              device - spectrograph to interrogate
              Grating - grating to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - grating offset returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid grating
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              offset - pointer to the grating offset (steps)

            C++ Equiv:
              unsigned int GetGratingOffset(int device, int Grating, int * offset);

            See Also:
             IsGratingPresent GetTurret GetNumberGratings GetGrating GetGratingInfo GetDetectorOffset SetTurret SetGrating WavelengthReset SetGratingOffset SetDetectorOffset 

        """
        cdevice = c_int(device)
        cGrating = c_int(Grating)
        coffset = c_int()
        ret = self.dll.ATSpectrographGetGratingOffset(cdevice, cGrating, byref(coffset))
        return (ret, coffset.value)

    def GetIris(self, device, iris):
        """ 
            Description:
              Gets iris position for the specified iris port. Value will be in the range 0 to 100.

            Synopsis:
              (ret, value) = GetIris(device, iris)

            Inputs:
              device - spectrograph to interrogate
              iris - Iris to query: Direct=0; Side=1

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Current focus position returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid iris specified.
                ATSPECTROGRAPH_P3INVALID - Value pointer is null
                ATSPECTROGRAPH_NOT_AVAILABLE - No iris at specified index
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              value - pointer to an int to store the position of the iris, in the range 0-100

            C++ Equiv:
              unsigned int GetIris(int device, int iris, int * value);

            See Also:
              SetIris IsIrisPresent 

        """
        cdevice = c_int(device)
        ciris = c_int(iris)
        cvalue = c_int()
        ret = self.dll.ATSpectrographGetIris(cdevice, ciris, byref(cvalue))
        return (ret, cvalue.value)

    def GetNumberDevices(self):
        """ 
            Description:
              Returns the number of available s.

            Synopsis:
              (ret, nodevices) = GetNumberDevices()

            Inputs:
              None

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Number of available s returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
              nodevices - pointer to the number of available s

            C++ Equiv:
              unsigned int GetNumberDevices(int * nodevices);

            See Also:
              Initialize GetFunctionReturnDescription Close 

        """
        cnodevices = c_int()
        ret = self.dll.ATSpectrographGetNumberDevices(byref(cnodevices))
        return (ret, cnodevices.value)

    def GetNumberGratings(self, device):
        """ 
            Description:
              Returns the number of available gratings.

            Synopsis:
              (ret, noGratings) = GetNumberGratings(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - number of available gratings returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              noGratings - pointer to the number of available gratings

            C++ Equiv:
              unsigned int GetNumberGratings(int device, int * noGratings);

            See Also:
              IsGratingPresent GetTurret GetGrating GetGratingInfo GetGratingOffset GetDetectorOffset SetTurret SetGrating WavelengthReset SetGratingOffset SetDetectorOffset 

        """
        cdevice = c_int(device)
        cnoGratings = c_int()
        ret = self.dll.ATSpectrographGetNumberGratings(cdevice, byref(cnoGratings))
        return (ret, cnoGratings.value)

    def GetNumberPixels(self, device):
        """ 
            Description:
              Gets the number of pixels of the attached sensor.

            Synopsis:
              (ret, NumberPixels) = GetNumberPixels(device)

            Inputs:
              device - Select spectrograph to control

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - port set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              NumberPixels - number of pixels of attached sensor

            C++ Equiv:
              unsigned int GetNumberPixels(int device, int * NumberPixels);

            See Also:
              GetPixelWidth SetPixelWidth SetNumberPixels GetCalibration 

        """
        cdevice = c_int(device)
        cNumberPixels = c_int()
        ret = self.dll.ATSpectrographGetNumberPixels(cdevice, byref(cNumberPixels))
        return (ret, cNumberPixels.value)

    def GetPixelCalibrationCoefficients(self, device):
        """ 
            Description:
              Gets pixel calibration coefficients.

            Synopsis:
              (ret, A, B, C, D) = GetPixelCalibrationCoefficients(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Constants returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Pointer is NULL
                ATSPECTROGRAPH_P3INVALID - Pointer is NULL
                ATSPECTROGRAPH_P4INVALID - Pointer is NULL
                ATSPECTROGRAPH_P5INVALID - Pointer is NULL
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              A - pointer to constant 1
              B - pointer to constant 2
              C - pointer to constant 3
              D - pointer to constant 4

            C++ Equiv:
              unsigned int GetPixelCalibrationCoefficients(int device, float * A, float * B, float * C, float * D);

            See Also:
              GetPixelWidth SetGratingOffset GetNumberPixels GetCalibration 

        """
        cdevice = c_int(device)
        cA = c_float()
        cB = c_float()
        cC = c_float()
        cD = c_float()
        ret = self.dll.ATSpectrographGetPixelCalibrationCoefficients(cdevice, byref(cA), byref(cB), byref(cC), byref(cD))
        return (ret, cA.value, cB.value, cC.value, cD.value)

    def GetPixelWidth(self, device):
        """ 
            Description:
              Gets the current value of the pixel width in microns of the attached sensor.

            Synopsis:
              (ret, Width) = GetPixelWidth(device)

            Inputs:
              device - Select spectrograph to control

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Pixel width returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              Width - current pixel width of attached sensor

            C++ Equiv:
              unsigned int GetPixelWidth(int device, float * Width);

            See Also:
              SetPixelWidth GetNumberPixels SetNumberPixels GetCalibration 

        """
        cdevice = c_int(device)
        cWidth = c_float()
        ret = self.dll.ATSpectrographGetPixelWidth(cdevice, byref(cWidth))
        return (ret, cWidth.value)

    def GetSerialNumber(self, device, maxSerialStrLen):
        """ 
            Description:
              Returns the device serial number.

            Synopsis:
              (ret, serial) = GetSerialNumber(device, maxSerialStrLen)

            Inputs:
              device - spectrograph to interrogate
              maxSerialStrLen - maximum string length

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - serial number returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              serial - pointer to the device serial number

            C++ Equiv:
              unsigned int GetSerialNumber(int device, char * serial);

            See Also:
              EepromGetOpticalParams 

        """
        cdevice = c_int(device)
        cserial = create_string_buffer(maxSerialStrLen)
        cmaxSerialStrLen = c_int(maxSerialStrLen)
        ret = self.dll.ATSpectrographGetSerialNumber(cdevice, cserial, cmaxSerialStrLen)
        return (ret, cserial.value.decode("utf-8"))

    def GetShutter(self, device):
        """ 
            Description:
              Returns the current device shutter mode.

            Synopsis:
              (ret, mode) = GetShutter(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - device shutter mode returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              mode - pointer to the device shutter mode:
                -1 - Shutter not set yet
                0 - Closed
                1 - Open

            C++ Equiv:
              unsigned int GetShutter(int device, int * mode);

            See Also:
              IsShutterPresent SetShutter IsModePossible 

        """
        cdevice = c_int(device)
        cmode = c_int()
        ret = self.dll.ATSpectrographGetShutter(cdevice, byref(cmode))
        return (ret, cmode.value)

    def GetSlitWidth(self, device, slit):
        """ 
            Description:
              Returns the Input Slit width.

            Synopsis:
              (ret, width) = GetSlitWidth(device, slit)

            Inputs:
              device - spectrograph to interrogate
              slit - index of the slit, must be one of the following,
                INPUT_SIDE 
                INPUT_DIRECT 
                OUTPUT_SIDE 
                OUTPUT_DIRECT 

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Input Slit width returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              width - pointer to the Slit width (m)

            C++ Equiv:
              unsigned int GetSlitWidth(int device, eSlitIndex slit, float *width);

            See Also:
              IsSlitPresent SetSlit SlitReset 

        """
        cdevice = c_int(device)
        cslit = (slit)
        cwidth = c_float()
        ret = self.dll.ATSpectrographGetSlitWidth(cdevice, cslit, byref(cwidth))
        return (ret, cwidth.value)

    def GetSlitCoefficients(self, device):
        """ 
            Description:
              

            Synopsis:
              (ret, x1, y1, x2, y2) = GetSlitCoefficients(device)

            Inputs:
              device - 

            Outputs:
              ret - Function Return Code
              x1 - 
              y1 - 
              x2 - 
              y2 - 

            C++ Equiv:
              unsigned int GetSlitCoefficients(int device, int & x1, int & y1, int & x2, int & y2);

        """
        cdevice = c_int(device)
        cx1 = c_int()
        cy1 = c_int()
        cx2 = c_int()
        cy2 = c_int()
        ret = self.dll.ATSpectrographGetSlitCoefficients(cdevice, byref(cx1), byref(cy1), byref(cx2), byref(cy2))
        return (ret, cx1.value, cy1.value, cx2.value, cy2.value)

    def GetSlitZeroPosition(self, device, index):
        """ 
            Description:
              Gets the zero position for the slit at the given index.

            Synopsis:
              (ret, offset) = GetSlitZeroPosition(device, index)

            Inputs:
              device - Select spectrograph to control
              index - index of the slit, must be one of the following,
                INPUT_SIDE 
                INPUT_DIRECT 
                OUTPUT_SIDE 
                OUTPUT_DIRECT 

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Slit zero position set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid index
                ATSPECTROGRAPH_P3INVALID - Invalid offset
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              offset - the offset returned by the shamrock. valid only if the return is ATSPECTROGRAPH_SUCCESS

            C++ Equiv:
              unsigned int GetSlitZeroPosition(int device, int index, int * offset);

            See Also:
              SetSlitZeroPosition 

        """
        cdevice = c_int(device)
        cindex = c_int(index)
        coffset = c_int()
        ret = self.dll.ATSpectrographGetSlitZeroPosition(cdevice, cindex, byref(coffset))
        return (ret, coffset.value)

    def GetTurret(self, device):
        """ 
            Description:
              Returns the current Turret.

            Synopsis:
              (ret, Turret) = GetTurret(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Turret returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              Turret - pointer to the Turret

            C++ Equiv:
              unsigned int GetTurret(int device, int * Turret);

            See Also:
              IsGratingPresent GetNumberGratings GetGrating GetGratingInfo GetGratingOffset GetDetectorOffset SetTurret SetGrating WavelengthReset SetGratingOffset SetDetectorOffset 

        """
        cdevice = c_int(device)
        cTurret = c_int()
        ret = self.dll.ATSpectrographGetTurret(cdevice, byref(cTurret))
        return (ret, cTurret.value)

    def GetWavelength(self, device):
        """ 
            Description:
              Returns the current wavelength.

            Synopsis:
              (ret, wavelength) = GetWavelength(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - wavelength returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              wavelength - pointer to the wavelength

            C++ Equiv:
              unsigned int GetWavelength(int device, float * wavelength);

            See Also:
              IsWavelengthPresent AtZeroOrder GetWavelengthLimits SetWavelength GotoZeroOrder 

        """
        cdevice = c_int(device)
        cwavelength = c_float()
        ret = self.dll.ATSpectrographGetWavelength(cdevice, byref(cwavelength))
        return (ret, cwavelength.value)

    def GetWavelengthLimits(self, device, Grating):
        """ 
            Description:
              Returns the Grating wavelength limits.

            Synopsis:
              (ret, Min, Max) = GetWavelengthLimits(device, Grating)

            Inputs:
              device - spectrograph to interrogate
              Grating - grating to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - wavelength returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid grating
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              Min - pointer to the lower wavelength limit (nm)
              Max - pointer to the upper wavelength limit (nm)

            C++ Equiv:
              unsigned int GetWavelengthLimits(int device, int Grating, float * Min, float * Max);

            See Also:
              IsWavelengthPresent GetWavelength AtZeroOrder SetWavelength GotoZeroOrder 

        """
        cdevice = c_int(device)
        cGrating = c_int(Grating)
        cMin = c_float()
        cMax = c_float()
        ret = self.dll.ATSpectrographGetWavelengthLimits(cdevice, cGrating, byref(cMin), byref(cMax))
        return (ret, cMin.value, round(cMax.value, 6))

    def GotoZeroOrder(self, device):
        """ 
            Description:
              Sets wavelength to zero order.

            Synopsis:
              ret = GotoZeroOrder(device)

            Inputs:
              device - spectrograph to send command to.

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Wavelength set to zero order
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int GotoZeroOrder(int device);

            See Also:
              WavelengthIsPresent GetWavelength AtZeroOrder GetWavelengthLimits SetWavelength 

            Note: Sets wavelength to zero order.

        """
        cdevice = c_int(device)
        ret = self.dll.ATSpectrographGotoZeroOrder(cdevice)
        return (ret)

    def IsGratingPresent(self, device):
        """ 
            Description:
              Finds if grating is present.

            Synopsis:
              (ret, present) = IsGratingPresent(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Grating presence flag returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              present - pointer to flag::
                0 - grating is NOT present
                1 - grating IS present

            C++ Equiv:
              unsigned int IsGratingPresent(int device, int * present);

            See Also:
              GetTurret GetNumberGratings GetGrating GetGratingInfo GetGratingOffset GetDetectorOffset SetTurret SetGrating WavelengthReset SetGratingOffset SetDetectorOffset 

        """
        cdevice = c_int(device)
        cpresent = c_int()
        ret = self.dll.ATSpectrographGratingIsPresent(cdevice, byref(cpresent))
        return (ret, cpresent.value)

    def Initialize(self, IniPath):
        """ 
            Description:
              Initializes the spectrograph driver.

            Synopsis:
              ret = Initialize(IniPath)

            Inputs:
              IniPath - pointer to the Andor camera DETECTOR.ini file

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - spectrograph driver initialized
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initalized
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Can't read spectrograph EEPROM

            C++ Equiv:
              unsigned int Initialize(char * IniPath);

            See Also:
              GetNumberDevices GetFunctionReturnDescription Close 

            Note: Initializes the spectrograph driver.

        """
        cIniPath = IniPath
        ret = self.dll.ATSpectrographInitialize(cIniPath)
        return (ret)

    def IsIrisPresent(self, device, iris):
        """ 
            Description:
              Indicates whether or not an input port has an iris.

            Synopsis:
              (ret, present) = IsIrisPresent(device, iris)

            Inputs:
              device - spectrograph to interrogate
              iris - Iris to query: Direct=0; Side=1

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Current focus position returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid iris specified.
                ATSPECTROGRAPH_P3INVALID - present pointer is null
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              present - pointer to an int to store the result. not present = 0, present = 1

            C++ Equiv:
              unsigned int IsIrisPresent(int device, int iris, int * present);

            See Also:
              GetIris SetIris 

        """
        cdevice = c_int(device)
        ciris = c_int(iris)
        cpresent = c_int()
        ret = self.dll.ATSpectrographIrisIsPresent(cdevice, ciris, byref(cpresent))
        return (ret, cpresent.value)

    def IsShutterModePossible(self, device, mode):
        """ 
            Description:
              Checks if a particular shutter mode is available.

            Synopsis:
              (ret, possible) = IsShutterModePossible(device, mode)

            Inputs:
              device - spectrograph to interrogate
              mode - shutter mode to check

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Shutter mode availability returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid mode
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              possible - pointer to flag::
                0 - shutter mode is NOT available
                1 - shutter mode IS available

            C++ Equiv:
              unsigned int IsModePossible(int device, int mode, int * possible);

            See Also:
              ShutterIsPresent GetShutter SetShutter 

        """
        cdevice = c_int(device)
        cmode = c_int(mode)
        cpossible = c_int()
        ret = self.dll.ATSpectrographIsShutterModePossible(cdevice, cmode, byref(cpossible))
        return (ret, cpossible.value)

    def SetAccessoryState(self, device, Accessory, State):
        """ 
            Description:
              Sets the Accessory state.

            Synopsis:
              ret = SetAccessoryState(device, Accessory, State)

            Inputs:
              device - Select spectrograph to control
              Accessory - line to set::
                1 - line 1
                2 - line 2
              State - Accessory state::
                0 - OFF
                1 - ON

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Line state set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid line
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int SetAccessoryState(int device, int Accessory, int State);

            See Also:
              IsAccessoryPresent GetAccessoryState 

            Note: Sets the Accessory state.

        """
        cdevice = c_int(device)
        cAccessory = c_int(Accessory)
        cState = c_int(State)
        ret = self.dll.ATSpectrographSetAccessoryState(cdevice, cAccessory, cState)
        return (ret)

    def SetDetectorOffset(self, device, entrancePort, exitPort, offset):
        """ 
            Description:
              

            Synopsis:
              ret = SetDetectorOffset(device, entrancePort, exitPort, offset)

            Inputs:
              device - 
              entrancePort - Select entrance port to use
              exitPort - Select exit port to use
              offset - 

            Outputs:
              ret - Function Return Code

            C++ Equiv:
              int SetDetectorOffset(int device,  entrancePort,  exitPort, int offset);

            See Also:
              GetDetectorOffsetPort 

        """
        cdevice = c_int(device)
        centrancePort = c_int(entrancePort)
        cexitPort = c_int(exitPort)
        coffset = c_int(offset)
        ret = self.dll.ATSpectrographSetDetectorOffset(cdevice, centrancePort, cexitPort, coffset)
        return (ret)

    def SetFilter(self, device, filter):
        """ 
            Description:
              Sets the required filter.

            Synopsis:
              ret = SetFilter(device, filter)

            Inputs:
              device - Select spectrograph to control
              filter - required filter

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - filter set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid filter
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int SetFilter(int device, int filter);

            See Also:
              IsFilterPresent GetFilter GetFilterInfo SetFilterInfo 

        """
        cdevice = c_int(device)
        cfilter = c_int(filter)
        ret = self.dll.ATSpectrographSetFilter(cdevice, cfilter)
        return (ret)

    def SetFilterInfo(self, device, Filter, Info):
        """ 
            Description:
              Sets the filter information.

            Synopsis:
              ret = SetFilterInfo(device, Filter, Info)

            Inputs:
              device - Select spectrograph to control
              Filter - filter to which set the information
              Info - pointer to filter information

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Filter information set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid filter
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int SetFilterInfo(int device, int Filter, char * Info);

            See Also:
              IsFilterPresent GetFilter GetFilterInfo SetFilter 

        """
        cdevice = c_int(device)
        cFilter = c_int(Filter)
        cInfo = Info
        ret = self.dll.ATSpectrographSetFilterInfo(cdevice, cFilter, cInfo)
        return (ret)

    def SetFlipperMirror(self, device, flipper, port):
        """ 
            Description:
              Sets the position of the specified flipper mirror.
              

            Synopsis:
              ret = SetFlipperMirror(device, flipper, port)

            Inputs:
              device - spectrograph to interrogate
              flipper - The flipper can have two values which are as follows::
                ATSPECTROGRAPH_INPUT_FLIPPER - 1
                ATSPECTROGRAPH_OUTPUT_FLIPPER - 2
              port - The port to set the flipper mirror to.:
                DIRECT - 0
                SIDE - 1

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - port set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid flipper
                ATSPECTROGRAPH_P3INVALID - Invalid port
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int SetFlipperMirror(int device, int flipper, int port);

            See Also:
              IsFlipperMirrorPresent GetFlipperMirror GetCCDLimits FlipperMirrorReset 

        """
        cdevice = c_int(device)
        cflipper = c_int(flipper)
        cport = c_int(port)
        ret = self.dll.ATSpectrographSetFlipperMirror(cdevice, cflipper, cport)
        return (ret)

    def SetFlipperMirrorPosition(self, device, flipper, position):
        """ 
            Description:
              Sets the current position for the specified flipper mirror.

            Synopsis:
              ret = SetFlipperMirrorPosition(device, flipper, position)

            Inputs:
              device - spectrograph to interrogate
              flipper - The flipper can have two values which are as follows:
                INPUT_FLIPPER 1
                OUTPUT_FLIPPER 2
              position - new position for the current flipper mirror

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - position set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int SetFlipperMirrorPosition(int device, int flipper, int position);

            See Also:
              IsFlipperMirrorPresent GetFlipperMirrorPosition SetFlipperMirror FlipperMirrorReset 

        """
        cdevice = c_int(device)
        cflipper = c_int(flipper)
        cposition = c_int(position)
        ret = self.dll.ATSpectrographSetFlipperMirrorPosition(cdevice, cflipper, cposition)
        return (ret)

    def SetFocusMirror(self, device, focus):
        """
            Description:
              Sets the required Focus movement. Focus movement is possible from 0 to max steps, so possible values will be from (0 - current steps) to (max - current steps)

            Synopsis:
              ret = SetFocusMirror(device, focus)

            Inputs:
              device - Select spectrograph to control
              focus - required focus movement:
                +steps move focus mirror forward
                -steps move focus mirror backwards

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Focus movement set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid Focus value
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int SetFocusMirror(int device, int focus);

            See Also:
              GetFocusMirror GetFocusMirrorMaxSteps FocusMirrorReset IsFocusMirrorPresent 

        """
        cdevice = c_int(device)
        cfocus = c_int(focus)
        ret = self.dll.ATSpectrographSetFocusMirror(cdevice, cfocus)
        return (ret)

    def SetGrating(self, device, grating):
        """ 
            Description:
              Sets the required grating.

            Synopsis:
              ret = SetGrating(device, grating)

            Inputs:
              device - Select spectrograph to control
              grating - required grating

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - grating set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid grating
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int SetGrating(int device, int grating);

            See Also:
              IsGratingPresent GetTurret GetNumberGratings GetGrating GetGratingInfo GetGratingOffset GetDetectorOffset SetTurret WavelengthReset SetGratingOffset SetDetectorOffset 

        """
        cdevice = c_int(device)
        cgrating = c_int(grating)
        ret = self.dll.ATSpectrographSetGrating(cdevice, cgrating)
        return (ret)

    def SetGratingOffset(self, device, Grating, offset):
        """ 
            Description:
              Sets the grating offset

            Synopsis:
              ret = SetGratingOffset(device, Grating, offset)

            Inputs:
              device - Select spectrograph to control
              Grating - grating to to which set the offset
              offset - grating offset (steps)

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - grating offset set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid grating
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int SetGratingOffset(int device, int Grating, int offset);

            See Also:
              IsGratingPresent GetTurret GetNumberGratings GetGrating GetGratingInfo GetGratingOffset GetDetectorOffset SetTurret SetGrating WavelengthReset SetDetectorOffset 

        """
        cdevice = c_int(device)
        cGrating = c_int(Grating)
        coffset = c_int(offset)
        ret = self.dll.ATSpectrographSetGratingOffset(cdevice, cGrating, coffset)
        return (ret)

    def SetIris(self, device, iris, value):
        """ 
            Description:
              Sets iris position for the specified iris port. Value must be in the range 0 to 100.

            Synopsis:
              ret = SetIris(device, iris, value)

            Inputs:
              device - spectrograph to interrogate
              iris - Iris to set: Direct=0; Side=1
              value - Position to set the iris, in the range 0-100

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Current iris position returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid iris specified.
                ATSPECTROGRAPH_P3INVALID - Value is out of range
                ATSPECTROGRAPH_NOT_AVAILABLE - No iris at specified index
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int SetIris(int device, int iris, int value);

            See Also:
              GetIris IsIrisPresent 

        """
        cdevice = c_int(device)
        ciris = c_int(iris)
        cvalue = c_int(value)
        ret = self.dll.ATSpectrographSetIris(cdevice, ciris, cvalue)
        return (ret)

    def SetNumberPixels(self, device, NumberPixels):
        """ 
            Description:
              Sets the number of pixels of the attached sensor.

            Synopsis:
              ret = SetNumberPixels(device, NumberPixels)

            Inputs:
              device - Select spectrograph to control
              NumberPixels - number of pixels of attached sensor

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - port set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid number
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int SetNumberPixels(int device, int NumberPixels);

            See Also:
              GetPixelWidth SetPixelWidth GetNumberPixels GetCalibration 

        """
        cdevice = c_int(device)
        cNumberPixels = c_int(NumberPixels)
        ret = self.dll.ATSpectrographSetNumberPixels(cdevice, cNumberPixels)
        return (ret)

    def SetPixelWidth(self, device, Width):
        """ 
            Description:
              Sets the pixel width in microns of the attached sensor.

            Synopsis:
              ret = SetPixelWidth(device, Width)

            Inputs:
              device - Select spectrograph to control
              Width - pixel width of attached sensor

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - port set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid width
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int SetPixelWidth(int device, float Width);

            See Also:
              GetPixelWidth GetNumberPixels SetNumberPixels GetCalibration 

        """
        cdevice = c_int(device)
        cWidth = c_float(Width)
        ret = self.dll.ATSpectrographSetPixelWidth(cdevice, cWidth)
        return (ret)

    def SetShutter(self, device, mode):
        """ 
            Description:
              Sets the shutter mode.

            Synopsis:
              ret = SetShutter(device, mode)

            Inputs:
              device - Select spectrograph to control
              mode - shutter mode:
                0 - Closed
                1 - Open

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Shutter mode set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid shutter
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int SetShutter(int device, int mode);

            See Also:
              IsShutterPresent GetShutter IsModePossible 

        """
        cdevice = c_int(device)
        cmode = c_int(mode)
        ret = self.dll.ATSpectrographSetShutter(cdevice, cmode)
        return (ret)

    def SetSlitCoefficients(self, device, x1, y1, x2, y2):
        """ 
            Description:
              

            Synopsis:
              ret = SetSlitCoefficients(device, x1, y1, x2, y2)

            Inputs:
              device - 
              x1 - 
              y1 - 
              x2 - 
              y2 - 

            Outputs:
              ret - Function Return Code

            C++ Equiv:
              unsigned int SetSlitCoefficients(int device, int x1, int y1, int x2, int y2);

        """
        cdevice = c_int(device)
        cx1 = c_int(x1)
        cy1 = c_int(y1)
        cx2 = c_int(x2)
        cy2 = c_int(y2)
        ret = self.dll.ATSpectrographSetSlitCoefficients(cdevice, cx1, cy1, cx2, cy2)
        return (ret)

    def SetSlitWidth(self, device, slit, width):
        """ 
            Description:
              Sets the Slit width.

            Synopsis:
              ret = SetSlitWidth(device, slit, width)

            Inputs:
              device - Select spectrograph to control
              slit - index of the slit, must be one of the following,
                INPUT_SIDE 
                INPUT_DIRECT 
                OUTPUT_SIDE 
                OUTPUT_DIRECT 
              width - Slit width

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Input Slit width set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid width
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              int SetSlitWidth(int device,  slit, float width);

            See Also:
              IsSlitPresent GetSlit SlitReset 

        """
        cdevice = c_int(device)
        cslit = c_int(slit)
        cwidth = c_float(width)
        ret = self.dll.ATSpectrographSetSlitWidth(cdevice, cslit, cwidth)
        return (ret)

    def SetSlitZeroPosition(self, device, index, offset):
        """ 
            Description:
              Sets the zero position for the slit at the given index.

            Synopsis:
              ret = SetSlitZeroPosition(device, index, offset)

            Inputs:
              device - Select spectrograph to control
              index - index of the slit, must be one of the following,
                ATSPECTROGRAPH_INPUT_SLIT_SIDE 
                ATSPECTROGRAPH_INPUT_SLIT_DIRECT 
                ATSPECTROGRAPH_OUTPUT_SLIT_SIDE 
                ATSPECTROGRAPH_OUTPUT_SLIT_DIRECT 
              offset - must be in the range (-200 - 0)

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Slit zero position set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid index
                ATSPECTROGRAPH_P3INVALID - Invalid offset
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int SetSlitZeroPosition(int device, int index, int offset);

            See Also:
              GetSlitZeroPosition 

        """
        cdevice = c_int(device)
        cindex = c_int(index)
        coffset = c_int(offset)
        ret = self.dll.ATSpectrographSetSlitZeroPosition(cdevice, cindex, coffset)
        return (ret)

    def SetTurret(self, device, Turret):
        """ 
            Description:
              Sets the required Turret.

            Synopsis:
              ret = SetTurret(device, Turret)

            Inputs:
              device - Select spectrograph to control
              Turret - required Turret

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Turret set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid Turret
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int SetTurret(int device, int Turret);

            See Also:
              IsGratingPresent GetTurret GetNumberGratings GetGrating GetGratingInfo GetGratingOffset GetDetectorOffset SetGrating WavelengthReset SetGratingOffset SetDetectorOffset 

        """
        cdevice = c_int(device)
        cTurret = c_int(Turret)
        ret = self.dll.ATSpectrographSetTurret(cdevice, cTurret)
        return (ret)

    def SetWavelength(self, device, wavelength):
        """ 
            Description:
              Sets the required wavelength.

            Synopsis:
              ret = SetWavelength(device, wavelength)

            Inputs:
              device - Select spectrograph to control
              wavelength - required wavelength

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Required wavelength set
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_P2INVALID - Invalid wavelength
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int SetWavelength(int device, float wavelength);

            See Also:
              IsWavelengthPresent 

        """
        cdevice = c_int(device)
        cwavelength = c_float(wavelength)
        ret = self.dll.ATSpectrographSetWavelength(cdevice, cwavelength)
        return (ret)

    def IsShutterPresent(self, device):
        """ 
            Description:
              Finds if Shutter is present.

            Synopsis:
              (ret, present) = IsShutterPresent(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Shutter presence flag returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              present - pointer to flag::
                0 - Shutter is NOT present
                1 - Shutter IS present

            C++ Equiv:
              unsigned int ShutterIsPresent(int device, int * present);

            See Also:
              GetShutter SetShutter IsModePossible 

        """
        cdevice = c_int(device)
        cpresent = c_int()
        ret = self.dll.ATSpectrographShutterIsPresent(cdevice, byref(cpresent))
        return (ret, cpresent.value)

    def IsSlitPresent(self, device, slit):
        """ 
            Description:
              

            Synopsis:
              (ret, present) = IsSlitPresent(device, slit)

            Inputs:
              device - spectrograph to interrogate
              slit - index of the slit, must be one of the following,
                INPUT_SIDE 
                INPUT_DIRECT 
                OUTPUT_SIDE 
                OUTPUT_DIRECT 
            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Input Slit presence flag returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              present - pointer to flag::
                0 - Slit is NOT present
                1 - Slit IS present

            C++ Equiv:
              unsigned int SlitIsPresent(int device, int * present);

            See Also:
              GetSlit SetSlit SlitReset 

        """
        cdevice = c_int(device)
        cslit = c_int(slit)
        cpresent = c_int()
        ret = self.dll.ATSpectrographSlitIsPresent(cdevice, cslit, byref(cpresent))
        return (ret, cpresent.value)

    def SlitReset(self, device, slit):
        """ 
            Description:
              Resets the Slit to its default (10m).

            Synopsis:
              ret = SlitReset(device, slit)

            Inputs:
              device - Select spectrograph to control.
              slit - index of the slit, must be one of the following,
                INPUT_SIDE 
                INPUT_DIRECT 
                OUTPUT_SIDE 
                OUTPUT_DIRECT 
            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - Input Slit reset
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              int SlitReset(int device,  slit);

            See Also:
              IsSlitPresent GetSlit SetSlit 

        """
        cdevice = c_int(device)
        cslit = c_int(slit)
        ret = self.dll.ATSpectrographSlitReset(cdevice, cslit)
        return (ret)

    def IsWavelengthPresent(self, device):
        """ 
            Description:
              Finds if the turret motors are installed.

            Synopsis:
              (ret, present) = IsWavelengthPresent(device)

            Inputs:
              device - spectrograph to interrogate

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - turret motors presence flag returned
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph
              present - pointer to flag::
                0 - turret motors is NOT present
                1 - turret motors IS present

            C++ Equiv:
              unsigned int WavelengthIsPresent(int device, int * present);

            See Also:
              GetWavelength AtZeroOrder GetWavelengthLimits SetWavelength GotoZeroOrder 

        """
        cdevice = c_int(device)
        cpresent = c_int()
        ret = self.dll.ATSpectrographWavelengthIsPresent(cdevice, byref(cpresent))
        return (ret, cpresent.value)

    def WavelengthReset(self, device):
        """ 
            Description:
              Resets the wavelength to 0 nm.

            Synopsis:
              ret = WavelengthReset(device)

            Inputs:
              device - Select spectrograph to control.

            Outputs:
              ret - Function Return Code:
                ATSPECTROGRAPH_SUCCESS - wavelength reset
                ATSPECTROGRAPH_NOT_INITIALIZED - spectrograph not initialized
                ATSPECTROGRAPH_P1INVALID - Invalid device
                ATSPECTROGRAPH_COMMUNICATION_ERROR - Unable to communicate with spectrograph

            C++ Equiv:
              unsigned int WavelengthReset(int device);

            See Also:
              IsGratingPresent GetTurret GetNumberGratings GetGrating GetGratingInfo GetGratingOffset GetDetectorOffset SetTurret SetGrating SetGratingOffset SetDetectorOffset 

            Note: Resets the wavelength to 0 nm.

        """
        cdevice = c_int(device)
        ret = self.dll.ATSpectrographWavelengthReset(cdevice)
        return (ret)

