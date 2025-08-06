import sys
import time

from instruments.utils.Range import Range
from photonicdrivers.Abstract.Connectable import Connectable
import numpy as np
from typing import Optional

try:
    sys.path.append(r"C:\\Program Files\\Andor SDK\\Python\\pyAndorSDK2")
    sys.path.append(r"C:\\Program Files\\Andor SDK\\Python\\pyAndorSpectrograph")
    from pyAndorSpectrograph.spectrograph import ATSpectrograph # type: ignore
except:
    print("Andor Solis is not installed ")


class Andor_Spectrograph_Driver(Connectable):
    def __init__(self) -> None:
        self.device_index = 0

    def connect(self):
        self.spectrograph = ATSpectrograph(userPath="C:\\Program Files\\Andor SDK\\Python\\pyAndorSpectrograph\\pyAndorSpectrograph\\libs\\Windows\\64")
        message = self.spectrograph.Initialize("")
        print("Function Initialize returned {}".format(self.spectrograph.GetFunctionReturnDescription(message, 64)[1]))

    def get_serial_number(self):
        sn, status = self.get_serial_number_with_success()
        return sn
    
    def get_serial_number_with_success(self):
        (message, serial_number) = self.spectrograph.GetSerialNumber(self.device_index, maxSerialStrLen=20)
        return serial_number, message == self.spectrograph.ATSPECTROGRAPH_SUCCESS
    
    def get_id(self):
        return self.get_serial_number()
    
    def get_grating(self):
        (message, grating) = self.spectrograph.GetGrating(self.device_index)
        return grating
    
    def set_grating(self, grating):
        self.spectrograph.SetGrating(self.device_index, grating)
    
    def set_center_wavelength(self, wavelength):
        self.spectrograph.SetWavelength(self.device_index, wavelength=wavelength)
    
    def get_center_wavelength(self):
        (message, wavelength) = self.spectrograph.GetWavelength(self.device_index)
        return wavelength
    
    def get_focus_mirror_max_steps(self):
        (message, max_steps) = self.spectrograph.GetFocusMirrorMaxSteps(self.device_index)
        return message, max_steps

    def get_focus_mirror_position(self):
        (message, position) = self.spectrograph.GetFocusMirror(self.device_index)
        return position

    def set_focus_mirror_position(self,position):
        return self.spectrograph.SetFocusMirror(self.device_index,position)

    def get_calibration_coefficients(self,xpixels,xsize):
        # Returns a tuple of the 4 coefficients for the third order polynomial in the function:
        # lambda = c0+c1*pixel+c2*pixel**2+c3pixel**3
        # Where lambda is the wavelength in nm for a corresponding pixel
        self.spectrograph.SetNumberPixels(0, xpixels)
        self.spectrograph.SetPixelWidth(0, xsize)
        (shm, c0, c1, c2, c3) = self.spectrograph.GetPixelCalibrationCoefficients(0)
        return (c0,c1,c2,c3)

    def get_calibration_array(self,xpixels,xsize):
        #Returns an np.array of length xpixels with the wavelength corresponding to each pixel
        coeffs = self.get_calibration_coefficients(xpixels,xsize)
        pixels=np.arange(0,xpixels,1)
        wavelengths=coeffs[0]+coeffs[1]*pixels+coeffs[2]*pixels**2+coeffs[3]*pixels**3
        return wavelengths

    def disconnect(self):
        self.spectrograph.Close()
        
    def is_connected(self):
        try:
            _, success = self.get_serial_number_with_success()
            return success
        except:
            return False

    def get_settings(self) -> dict:
        return {
            "id": self.get_id(),
            "grating": self.get_grating(),
            "center_wavelength": self.get_center_wavelength()
        }
