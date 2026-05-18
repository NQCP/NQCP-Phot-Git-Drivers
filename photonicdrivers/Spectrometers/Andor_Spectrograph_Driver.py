import os
import numpy as np
from enum import IntEnum

from photonicdrivers.Abstract.Connectable import Connectable

from .Kymera328i.pyAndorSpectrograph.pyAndorSpectrograph import ATSpectrograph


class Error_Codes (IntEnum):
    """Error codes for the Andor Spectrograph SDK
    """
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

errors = Error_Codes

class AndorException(Exception):
    def __init__(self, error_text = None, error_number = 0):
        self.error_text = error_text
        self.error_number = error_number


class Andor_Spectrograph_Driver(Connectable):
    """
    Module for controlling Andor spectrographs using the Andor Spectrograph SDK.

    Args:
        Connectable (class): abstract class that defines the connect, disconnect and is_connected methods that all drivers should have.
    """

    def __init__(self, verbose = False) -> None:
        self.device_index = 0
        self.verbose = verbose

    # Basic configuration methods

    def get_function_return_description(self, error_num):
        return self.spectrograph.GetFunctionReturnDescription(error=error_num, MaxDescStrLen=64)[1]

    def error_num_to_str(self, error_num: int) -> str:
        try:
            return self.get_function_return_description(error_num)
        except ValueError:
            return f"UNKNOWN_ERROR_{error_num}"

    def handle_return(self, ret_value: int):
        if ret_value != errors.ATSPECTROGRAPH_SUCCESS:
            raise AndorException(("Error " + str(self.error_num_to_str(ret_value))), ret_value)
        return ret_value

    def connect(self):
        self.spectrograph = ATSpectrograph(userPath=os.path.join(os.path.dirname(__file__), r"Kymera328i/pyAndorSpectrograph/pyAndorSpectrograph/libs/Windows/64"))
        ret = self.spectrograph.Initialize(IniPath="")
        self.handle_return(ret_value=ret)
        if self.verbose:
            print("Function Initialize returned {}".format(self.get_function_return_description(ret)))

    def get_serial_number(self):
        (ret, serial_number) = self.spectrograph.GetSerialNumber(self.device_index, maxSerialStrLen=20)
        self.handle_return(ret_value=ret)
        return serial_number

    def get_id(self):
        return self.get_serial_number()

    def disconnect(self):
        ret = self.spectrograph.Close()
        self.handle_return(ret_value=ret)

    def is_connected(self):
        try:
            self.get_serial_number()
            return True
        except Exception:
            return False

    def get_settings(self) -> dict:
        return {
            "id": self.get_id(),
            "grating": self.get_grating(),
            "center_wavelength": self.get_center_wavelength()
        }

    def get_grating(self):
        (ret, grating) = self.spectrograph.GetGrating(self.device_index)
        self.handle_return(ret_value=ret)
        return grating

    def set_grating(self, grating):
        ret = self.spectrograph.SetGrating(self.device_index, grating)
        self.handle_return(ret_value=ret)

    def set_center_wavelength(self, wavelength):
        ret = self.spectrograph.SetWavelength(self.device_index, wavelength=wavelength)
        self.handle_return(ret_value=ret)

    def get_center_wavelength(self):
        (ret, wavelength) = self.spectrograph.GetWavelength(self.device_index)
        self.handle_return(ret_value=ret)
        return wavelength

    def get_focus_mirror_max_steps(self):
        (ret, max_steps) = self.spectrograph.GetFocusMirrorMaxSteps(self.device_index)
        self.handle_return(ret_value=ret)
        return max_steps

    def get_focus_mirror_position(self):
        (ret, position) = self.spectrograph.GetFocusMirror(self.device_index)
        self.handle_return(ret_value=ret)
        return position

    def set_focus_mirror_position(self,position):
        ret = self.spectrograph.SetFocusMirror(self.device_index,position)
        self.handle_return(ret_value=ret)

    def get_calibration_coefficients(self,xpixels,xsize):
        # Returns a tuple of the 4 coefficients for the third order polynomial in the function:
        # lambda = c0+c1*pixel+c2*pixel**2+c3pixel**3
        # Where lambda is the wavelength in nm for a corresponding pixel
        ret = self.spectrograph.SetNumberPixels(0, xpixels)
        self.handle_return(ret_value=ret)
        ret = self.spectrograph.SetPixelWidth(0, xsize)
        self.handle_return(ret_value=ret)
        (shm, c0, c1, c2, c3) = self.spectrograph.GetPixelCalibrationCoefficients(0)
        return (c0,c1,c2,c3)

    def get_calibration_array(self,xpixels,xsize):
        #Returns an np.array of length xpixels with the wavelength corresponding to each pixel
        coeffs = self.get_calibration_coefficients(xpixels,xsize)
        pixels=np.arange(0,xpixels,1)
        wavelengths=coeffs[0]+coeffs[1]*pixels+coeffs[2]*pixels**2+coeffs[3]*pixels**3
        return wavelengths
