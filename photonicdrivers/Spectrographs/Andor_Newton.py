
### Load libraries
import sys
import time
import numpy as np


import numpy as np
import matplotlib.pyplot as plt
from photonicdrivers.utils.Range import Range
sys.path.append(r"C:\\Program Files\\Andor SDK\\Python\\pyAndorSDK2")
sys.path.append(r"C:\\Program Files\\Andor SDK\\Python\\pyAndorSpectrograph")
from pyAndorSDK2 import atmcd, atmcd_codes, atmcd_errors
codes = atmcd_codes

class Andor_Newton:

    def __init__(self) -> None:
        self.camera = atmcd("C://Program Files/Andor SDK")
        self.num_pixel_y = 200
        self.num_pixel_x = 1600

    def connect(self):
        self.camera.Initialize("")
        self.camera.SetReadMode(4)
        self.camera.SetImage(1,1,1,self.num_pixel_x,1,self.num_pixel_y)
        self.camera.SetAcquisitionMode(codes.Acquisition_Mode.SINGLE_SCAN)

    def set_exposure_time_s(self, exposure_time_s):
        self.camera.SetExposureTime(exposure_time_s)

    def get_image(self):
        self.camera.PrepareAcquisition()
        self.camera.StartAcquisition()
        self.camera.WaitForAcquisition()
        (ret, arr, validfirst, validlast) = self.camera.GetImages(1,1, size=self.num_pixel_x*self.num_pixel_y)
        image = np.flip(np.flip(np.reshape(arr, (self.num_pixel_y, self.num_pixel_x)), axis=1),axis=0)
        return image
    
    def get_trace(self):
        image = self.get_image()
        trace = np.sum(image, axis=0)
        return trace

    def cooler_on(self):
        self.camera.CoolerON()

    def coolor_off(self):
        self.camera.CoolerOFF()

    def set_temperature(self, temperature_celsius):
        self.camera.SetTemperature(temperature_celsius)
        
    def get_serial_number(self):
        return self.camera.GetCameraSerialNumber()

    def get_gain_range(self):
        (message, min_gain, max_gain) = self.camera.GetEMGainRange()
        return Range(min_gain, max_gain)
    
    def get_gain(self):
        """
        Get the electron multiplier (EM) gain from (0, 256)
        """
        (message, gain) = self.camera.GetEMCCDGain()
        return gain
    

    def set_gain(self, gain):
        gain_range = self.get_gain_range()
        if gain_range.contains(gain):
            self.camera.SetGain
        else:
            print("Gain out of range: " + gain_range)

    def disconnect(self):
        pass
        

