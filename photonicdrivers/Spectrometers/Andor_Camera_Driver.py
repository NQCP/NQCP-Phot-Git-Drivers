import os
import time
import numpy as np

from instruments.utils.Range import Range
from photonicdrivers.Abstract.Connectable import Connectable

from labserver.Server.remote_logger import RemoteLogger, RemoteLoggerDummy

from .Kymera328i.pyAndorSDK2.pyAndorSDK2 import atmcd, atmcd_codes, atmcd_errors
codes = atmcd_codes
errors = atmcd_errors.Error_Codes


class AndorException(Exception):
    def __init__(self, error_text = None, error_number = 0):
        self.error_text = error_text
        self.error_number = error_number


class Andor_Camera_Driver(Connectable):
    """
    Module for controlling Andor cameras using the Andor SDK.

    Args:
        Connectable (class): abstract class that defines the connect, disconnect and is_connected methods that all drivers should have.
    """

    def __init__(self,
            verbose = False,
            logger: RemoteLogger | RemoteLoggerDummy = RemoteLoggerDummy(),
            acquisition_mode: int = codes.Acquisition_Mode.SINGLE_SCAN.value,
            read_mode: int = codes.Read_Mode.FULL_VERTICAL_BINNING.value,
        ) -> None:
        self.camera = atmcd(userPath=os.path.join(os.path.dirname(__file__), r"Kymera328i/pyAndorSDK2/pyAndorSDK2/libs/Windows/64"))
        self.verbose: bool = verbose
        self.logger: RemoteLogger | RemoteLoggerDummy = logger
        self.num_accumulations: int | None = None
        self.set_acquisition_mode(acquisition_mode)
        self.set_read_mode(read_mode)

    # Basic configuration methods

    def handle_return(self, ret_value: int):
        if ret_value == errors.DRV_NOT_INITIALIZED:
            self.logger.warning("Camera not initialized. Please connect to the camera first.")
        elif ret_value == errors.DRV_TEMPERATURE_OFF:
            self.logger.warning("Camera temperature is off. Please turn on the cooler to get temperature readings.")
        elif ret_value == errors.DRV_TEMPERATURE_STABILIZED:
            self.logger.info("Camera temperature stabilized.")
        elif ret_value != errors.DRV_SUCCESS:
            raise AndorException(("Error " + str(self.error_num_to_str(ret_value))), ret_value)
        return ret_value

    def error_num_to_str(self, error_num: int) -> str:
        try:
            return errors(error_num).name
        except ValueError:
            return f"UNKNOWN_ERROR_{error_num}"

    def get_serial_number(self):
        (ret, serial_number) = self.camera.GetCameraSerialNumber()
        self.handle_return(ret_value=ret)
        return serial_number

    def get_id(self):
        return self.get_serial_number()

    def init_detector_params(self):
        #get the amount of pixels in the camera
        ret,self.num_pixel_x,self.num_pixel_y=self.camera.GetDetector()
        self.handle_return(ret_value=ret)
        #get the size of the pixels
        ret,self.size_pixel_x,self.size_pixel_y =self.camera.GetPixelSize()
        self.handle_return(ret_value=ret)

    def abort_acquisition(self):
        ret = self.camera.AbortAcquisition()
        if ret != errors.DRV_SUCCESS and ret != errors.DRV_IDLE:
            self.handle_return(ret_value=ret)

    # Methods for connecting and disconnecting the camera, and checking connection status

    def connect(self):
        """
        Method to connect to the Andor camera.
        """

        ret= self.camera.Initialize("")
        # Check whether we have connection, using serial number to verify that we can get non-zero results.
        self.init_detector_params()
        if ret == errors.DRV_SUCCESS and self.get_serial_number() != 0:
            self.logger.info('Camera Initialization Successful')
        elif ret == errors.DRV_NOT_AVAILABLE and self.camera.GetCameraSerialNumber()[0]==errors.DRV_SUCCESS:
            self.logger.info('Camera Already Initialized')
        else:
            self.logger.error('ERROR WHEN INITIALIZING CAMERA')
            self.handle_return(ret_value=ret)

    def disconnect(self):
        """
        Method to disconnect from the Andor camera. We check if there is an acquisition in progress or if the cooler is on, and if so we stop the acquisition and turn off the cooler before disconnecting. We also check the temperature, and if it's too cold to safely shut down, we wait until it warms up.
        """
        if self.is_acquiring():
            self.logger.info("Acquisition in progress, aborting acquisition before disconnecting...")
            self.abort_acquisition()
        if self.is_cooler_on():
             self.logger.info("Cooler is on, turning off cooler before disconnecting...")
             self.set_cooler_off()
        temp=self.get_temperature()
        if temp < -20:
            self.logger.info("Too cold to safely shut down, waiting...")
        while temp < -20:
            self.logger.info(f"T={temp}")
            temp=self.get_temperature()
            time.sleep(10)

        ret = self.camera.ShutDown()
        self.handle_return(ret_value=ret)
        if self.verbose:
            self.logger.info(f"ShutDown returned: {errors(value=ret).name}")

    # is-methods to check the status of the camera, cooler and acquisition

    def is_connected(self):
        try:
            return bool(self.get_serial_number())
        except Exception:
            return False

    def is_cooler_on(self):
        (ret, cooler_status) = self.camera.IsCoolerOn()
        self.handle_return(ret_value=ret)
        return bool(cooler_status)

    def is_acquiring(self):
        return self.get_status() == errors.DRV_ACQUIRING

    def is_cooling(self):
        return self.is_cooler_on() and self.get_temperature_retval() in (errors.DRV_TEMP_NOT_STABILIZED, errors.DRV_TEMP_NOT_REACHED)

    def get_settings(self) -> dict:
        setting_dict: dict[str, str|float|bool|None]={
            "id": self.get_serial_number(),
            "actual_temperature": self.get_temperature(),
            "is_cooler_on": self.is_cooler_on(),
            "is_acquiring": self.is_acquiring(),
            "acquisition_mode": self.acquisition_mode,
            "read_mode": self.read_mode,
            "exposure_time": self.get_acquisition_timings()[0],
            "num_accumulations": self.num_accumulations,
            "accumulation_cycle_time": self.get_acquisition_timings()[1],
            "gain": self.get_gain(),
            "num_pixel_x": self.num_pixel_x,
            "num_pixel_y":self.num_pixel_y,
            "size_pixel_x": self.size_pixel_x,
            "size_pixel_y":self.size_pixel_y,
            "max_exposure_time": self.get_max_exposure_time(),
        }
        try:
            setting_dict.update({"acquisition_mode": self.acquisition_mode})
        except Exception:
            pass
        try:
            setting_dict.update({"read_mode":self.read_mode})
        except Exception:
            pass
        return setting_dict

    # Getter methods for camera parameters and data acquisition

    def get_status(self):
        (ret, status) = self.camera.GetStatus()
        self.handle_return(ret_value=ret)
        return status

    def get_status_string(self):
        status = self.get_status()
        try:
            return errors(status).name
        except ValueError:
            return f"UNKNOWN_STATUS_{status}"

    def get_acquisition_mode(self):
        return self.acquisition_mode

    def get_read_mode(self):
        return self.read_mode

    def get_acquisition_progress(self):
        (ret, acc, series) = self.camera.GetAcquisitionProgress()
        self.handle_return(ret_value=ret)
        return acc, series

    def get_temperature_retval(self):
        # one cannot handle the return value of this function with the usual error handling, because it returns DRV_TEMP_NOT_REACHED or DRV_TEMP_NOT_STABILIZED when the cooler is on and cooling, which is not an error but rather a status. So we just return the raw values and let the user handle them as they see fit.
        return self.camera.GetTemperature()[0]

    def get_temperature(self):
        (ret, temperature) = self.camera.GetTemperature()
        if ret == errors.DRV_TEMP_OFF or ret == errors.DRV_NOT_INITIALIZED:
            self.logger.warning("Camera temperature is off. Please turn on the cooler to get temperature readings.")
            return None
        if ret not in (errors.DRV_TEMPERATURE_NOT_REACHED, errors.DRV_TEMPERATURE_NOT_STABILIZED):
            self.handle_return(ret_value=ret)
        if self.verbose:
            self.logger.info(f"GetTemperature returned: {errors(value=ret).name}")
        return temperature

    def get_max_exposure_time(self):
        (ret, exposure_time) = self.camera.GetMaximumExposure()
        self.handle_return(ret_value=ret)
        return exposure_time

    def get_acquisition_timings(self):
        (ret, exposure, accumulate, kinetic) = self.camera.GetAcquisitionTimings()
        self.handle_return(ret_value=ret)
        return exposure, accumulate, kinetic

    def get_image(self):
        self.camera.PrepareAcquisition()
        self.camera.StartAcquisition()
        self.camera.WaitForAcquisition()
        (ret, arr, validfirst, validlast) = self.camera.GetImages(1,1, size=self.num_pixel_x*self.num_pixel_y)
        self.handle_return(ret_value=ret)
        image = np.flip(np.flip(np.reshape(arr, (self.num_pixel_y, self.num_pixel_x)), axis=1),axis=0)
        return image

    def get_ROI_counts(self,roi):
        '''return an array of counts from the image where we sum all rows within the region of interest (ROI)'''
        image = self.get_image()
        return np.sum(image[roi[0]:roi[1]], axis=0)/(roi[1] - roi[0])

    def get_trace(self):
        image = self.get_image()
        trace = np.sum(image, axis=0)
        return trace

    def get_temperature_range(self):
        (ret, min_temp, max_temp) = self.camera.GetTemperatureRange()
        self.handle_return(ret_value=ret)
        return min_temp, max_temp

    def get_temperature_status(self):
        (ret, sensor_temp, target_temp, ambient_temp, cooler_volts) = self.camera.GetTemperatureStatus()
        self.handle_return(ret_value=ret)
        return sensor_temp, float(target_temp), float(ambient_temp), float(cooler_volts)

    def get_gain_range(self):
        (ret, min_gain, max_gain) = self.camera.GetEMGainRange()
        self.handle_return(ret_value=ret)
        return Range(min_gain, max_gain)

    def get_gain(self):
        """
        Get the electron multiplier (EM) gain from (0, 256)
        """
        (ret, gain) = self.camera.GetEMCCDGain()
        self.handle_return(ret_value=ret)
        return gain

    def get_available_cameras(self):
        ret,cameras=self.camera.GetAvailableCameras()
        self.handle_return(ret_value=ret)
        if self.verbose:
            self.logger.info(f"get_available_cameras returned: {errors(value=ret).name}")
        return cameras

    def get_current_camera(self):
        ret, handle = self.camera.GetCurrentCamera()
        self.handle_return(ret_value=ret)
        return handle

    # Setter methods for camera parameters and acquisition settings

    def set_cooler_on(self):
        ret = self.camera.CoolerON()
        self.handle_return(ret_value=ret)
        if self.verbose:
            self.logger.info(f"cooler_on returned: {errors(value=ret).name}")

    def set_cooler_off(self):
        ret = self.camera.CoolerOFF()
        self.handle_return(ret_value=ret)

    def set_temperature(self, temperature_celsius):
        ret = self.camera.SetTemperature(temperature_celsius)
        self.handle_return(ret_value=ret)

    def set_gain(self, gain):
        gain_range = self.get_gain_range()
        if gain_range.contains(gain):
            ret = self.camera.SetGain(gain)
            self.handle_return(ret_value=ret)
        else:
            self.logger.warning(f"Gain out of range: {gain_range}")

    def set_exposure_time(self, exposure_time):
        ret = self.camera.SetExposureTime(exposure_time)
        self.handle_return(ret_value=ret)

    def set_active_camera(self,index):
        ret, handle = self.camera.GetCameraHandle(index)
        self.handle_return(ret_value=ret)
        ret = self.camera.SetCurrentCamera(handle)
        self.handle_return(ret_value=ret)
        if self.verbose:
            self.logger.info(f"set_active_camera returned: {errors(ret).name}")

    def set_verbose(self, boool):
        self.verbose: bool = boool

    def set_read_mode(self, read_mode):
        if read_mode not in [mode.value for mode in codes.Read_Mode]:
            self.logger.warning(f"Read mode {read_mode} not recognized. Valid modes are {[mode.value for mode in codes.Read_Mode]}")
            return
        ret=self.camera.SetReadMode(read_mode)
        self.handle_return(ret_value=ret)
        self.read_mode: int = read_mode
        if self.verbose:
            self.logger.info(f"set_read_mode returned: {errors(ret).name}")

    def set_image(self,hbin, vbin, hstart, hend, vstart, vend):
        ret=self.camera.SetImage(hbin, vbin, hstart, hend, vstart, vend)
        self.handle_return(ret_value=ret)
        if self.verbose:
            self.logger.info(f"set_image returned: {errors(ret).name}")

    def set_acquisition_mode(self, acquisition_mode: int):
        if acquisition_mode not in [mode.value for mode in codes.Acquisition_Mode]:
            self.logger.warning(f"Acquisition mode {acquisition_mode} not recognized. Valid modes are {[mode.value for mode in codes.Acquisition_Mode]}")
            return
        ret = self.camera.SetAcquisitionMode(acquisition_mode)
        self.handle_return(ret_value=ret)
        self.acquisition_mode: int = acquisition_mode
        if self.acquisition_mode not in (codes.Acquisition_Mode.ACCUMULATE.value, codes.Acquisition_Mode.KINETICS.value, codes.Acquisition_Mode.FAST_KINETICS.value):
            self.num_accumulations = None
        if self.verbose:
            self.logger.info(f"set_acquisition_mode returned: {errors(value=ret).name}")

    def set_number_accumulations(self, num_accumulations):
        if self.acquisition_mode not in (codes.Acquisition_Mode.ACCUMULATE.value, codes.Acquisition_Mode.KINETICS.value, codes.Acquisition_Mode.FAST_KINETICS.value):
            self.logger.warning(f"Number of accumulations can only be set in ACCUMULATE or KINETIC_SERIES acquisition modes, not in {self.acquisition_mode}.")
            return
        ret = self.camera.SetNumberAccumulations(num_accumulations)
        self.handle_return(ret_value=ret)
        self.num_accumulations = num_accumulations
        if self.verbose:
            self.logger.info(f"set_number_accumulations returned: {errors(value=ret).name}")
