import sys
import time
from pyAndorSpectrograph.spectrograph import ATSpectrograph
from photonicdrivers.utils.Range import Range
sys.path.append(r"C:\\Program Files\\Andor SDK\\Python\\pyAndorSpectrograph")

class Andor_Kymera():
    def __init__(self) -> None:
        self.spectrograph = ATSpectrograph()
        self.device_index = 0

    def connect(self):
        message = self.spectrograph.Initialize("")
        print("Function Initialize returned {}".format(self.spectrograph.GetFunctionReturnDescription(message, 64)[1]))

    def get_grating(self):
        (message, grating) = self.spectrograph.GetGrating(self.device_index)
        return grating
    
    def set_grating(self, grating):
        #1 broader, 2 narrower
        (message, grating) = self.spectrograph.SetGrating(self.device_index)
        return grating

    def get_wavelength_range(self):
        (message, min_wavelength, max_wavelength) = self.spectrograph.GetWavelengthLimits(self.device_index, self.get_grating())
        return Range(min_wavelength, max_wavelength)
    
    def set_center_wavelength(self, wavelength):
        self.spectrograph.SetWavelength(self.device_index, wavelength=wavelength)
    
    def get_center_wavelength(self):
        (message, wavelength) = self.spectrograph.GetWavelength(self.device_index)
        return wavelength

    def disconnect(self):
        pass


