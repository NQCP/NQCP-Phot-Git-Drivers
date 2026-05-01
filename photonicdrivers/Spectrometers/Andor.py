

import sys
import time

from photonicdrivers.utils.Range import Range
from photonicdrivers.Abstract.Connectable import Connectable
import numpy as np

try:

    from photonicdrivers.utils.Range import Range
    sys.path.append(r"C:\\Program Files\\Andor SDK\\Python\\pyAndorSDK2")
    sys.path.append(r"C:\\Program Files\\Andor SDK\\Python\\pyAndorSpectrograph")
    from pyAndorSpectrograph.spectrograph import ATSpectrograph # type: ignore
    from pyAndorSDK2 import atmcd, atmcd_codes, atmcd_errors
    codes = atmcd_codes
    errors=atmcd_errors.Error_Codes
except:
    print("Andor Solis is not installed ")


class Andor(Connectable):

    def __init__(self,verbose=False) -> None:
        self.camera = None
        self.spectrograph = None
        self.verbose=verbose
        self.device_index = 0

    def connect(self):
        self.spectrograph = ATSpectrograph(userPath="C:\\Program Files\\Andor SDK\\Python\\pyAndorSpectrograph\\pyAndorSpectrograph\\libs\\Windows\\64")
        message = self.spectrograph.Initialize("")
        print(self.spectrograph)
        if message == 20202:
            print('Spectrograph Initialization Successful')
        elif self.spectrograph.GetNumberGratings(device=0)[1]!=0:
            print('Spectrograph Already Initialized')
        else:
            print('ERROR WHEN INITIALIZING SPECTROGRAPH')

        #Our connection issues stem from these lines of code. When we instantiate a new atmcd-object we lose the connection with the camera
        # this is what forces us to connect and disconnect. The spectograph seems more stable to re-instantiation, but it has been observed to hang in the same way some times.
        self.camera = atmcd(userPath="C:\\Program Files\\Andor SDK\\Python\\pyAndorSDK2\\pyAndorSDK2\\libs\\Windows\\64")

        message = self.camera.Initialize("")
        # Check whether we have connection, using serial number to verify that we can get non-zero results.
        if message == 20002:
            print('Camera Initialization Successful')
        elif message == 20992 and self.camera.GetCameraSerialNumber()[0]==20002:
            print('Camera Already Initialized')
        else:
            print('ERROR WHEN INITIALIZING CAMERA')

        #get the amount of pixels in the camera
        _,self.num_pixel_x,self.num_pixel_y=self.camera.GetDetector()        

    def get_exposure_time_s(self):
        (message, exposure_time) = self.camera.GetMaximumExposure()
        return exposure_time

    def get_image(self):
        self.camera.PrepareAcquisition()
        self.camera.StartAcquisition()
        self.camera.WaitForAcquisition()
        (ret, arr, validfirst, validlast) = self.camera.GetImages(1,1, size=self.num_pixel_x*self.num_pixel_y)
        image = np.flip(np.flip(np.reshape(arr, (self.num_pixel_y, self.num_pixel_x)), axis=1),axis=0)
        return image

    def get_ROI_counts(self,roi):
        '''return an array of counts from the image where we sum all rows within the region of interest (ROI)'''
        image = self.get_image()
        return np.sum(image[roi[0]:roi[1]], axis=0)/(roi[1] - roi[0])

    def get_trace(self):
        image = self.get_image()
        trace = np.sum(image, axis=0)
        return trace.tolist()

    def cooler_on(self):
        ret=self.camera.CoolerON()
        if self.verbose:
            print("cooler_on returned: ",errors(ret).name)

    def cooler_off(self):
        self.camera.CoolerOFF()

    def set_temperature(self, temperature_celsius):
        self.camera.SetTemperature(temperature_celsius)

    def get_temperature(self):
        (ret, temperature) = self.camera.GetTemperature()
        if self.verbose:
            print("ShutDown returned: ",errors(ret).name)
        return temperature

    def get_cameria_serial_number(self):
        serial_number, success = self.get_cameria_serial_number_with_success
        return serial_number

    def get_camera_serial_number_with_success(self):
        (message, serial_number) = self.camera.GetCameraSerialNumber()
        print(message)
        print(atmcd_errors.Error_Codes.DRV_SUCCESS)
        success = message == atmcd_errors.Error_Codes.DRV_SUCCESS
        return serial_number, success
    
    def get_id(self):
        return self.get_camera_serial_number()

    def get_gain_range(self):
        (message, min_gain, max_gain) = self.camera.GetEMGainRange()
        return Range(min_gain, max_gain)
    
    def get_gain(self):
        """
        Get the electron multiplier (EM) gain from (0, 256)
        """
        (message, gain) = self.camera.GetEMCCDGain()
        return gain

    def get_available_cameras(self):
        ret,cameras=self.camera.GetAvailableCameras()
        if self.verbose:
            print("get_available_cameras returned: ",errors(ret).name)
        return cameras

    def set_gain(self, gain):
        gain_range = self.get_gain_range()
        if gain_range.contains(gain):
            self.camera.SetGain
        else:
            print("Gain out of range: " + gain_range)
        
    def set_exposure_time_s(self, exposure_time_s):
        self.camera.SetExposureTime(exposure_time_s)

    def set_active_camera(self,index):
        ret, handle = self.camera.GetCameraHandle(index)
        ret = self.camera.SetCurrentCamera(handle)
        if self.verbose:
            print("set_active_camera returned: ",errors(ret).name)


    def set_verbose(self,boool):
        self.verbose=boool

    def set_read_mode(self, readmode):
        ret=self.camera.SetReadMode(readmode)
        if self.verbose:
            print("set_read_mode returned: ",errors(ret).name)


    def set_image(self,hbin, vbin, hstart, hend, vstart, vend):
        ret=self.camera.SetImage(hbin, vbin, hstart, hend, vstart, vend)
        if self.verbose:
            print("set_image returned: ",errors(ret).name)
    
    def set_camera_acquisition(self,mode):
        self.camera.SetAcquisitionMode(mode)

    def disconnect(self):
        self.abort_acquisition()
        self.cooler_off()
        temp=self.get_temperature()
        if temp < -20:
            print ("Too cold to safely shut down, waiting...")
        while temp < -20:
            print("T=",temp)
            temp=self.get_temperature()
            time.sleep(10)

        ret = self.camera.ShutDown()
        if self.verbose:
            print("ShutDown returned: ",errors(ret).name)

        self.spectrograph.Close()

    
    def abort_acquisition(self):
        self.camera.AbortAcquisition()

    def is_connected(self):
        try:
            _, spectrograph_success = self.get_spectrograph_serial_number_with_success()
            _, camera_success = self.get_camera_serial_number_with_success()
            print(spectrograph_success)
            print(camera_success)
            return  camera_success and spectrograph_success
        except:
            return False

    def get_settings(self):
        return {
            "id": self.get_serial_number(),
            "temperature": self.get_temperature(),
            "gain": self.get_gain(),
            "exposure_time": self.get_exposure_time_s(),
            "grating": self.get_grating(),
            "center_wavelength": self.get_center_wavelength()
        }
    
    def get_spectrograph_serial_number(self):
        serial_number, success = self.get_serial_number_with_success()
        return serial_number
    
    def get_spectrograph_serial_number_with_success(self):
        (message, serial_number) = self.spectrograph.GetGrating(self.device_index)
        print(message)
        print(self.spectrograph.ATSPECTROGRAPH_SUCCESS)
        success = message == self.spectrograph.ATSPECTROGRAPH_SUCCESS
        return serial_number, success
    
    def get_id(self):
        return self.get_serial_number()
    
    def get_grating(self):
        (message, grating) = self.spectrograph.GetGrating(self.device_index)
        return grating
    
    def set_grating(self, grating):
        #1 broader, 2 narrower
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
        self.spectrograph.SetFocusMirror(self.device_index,position)

