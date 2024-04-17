from thorlabs_tsi_sdk.tl_camera import TLCameraSDK

from Instruments.Settings.Console_Controller import Console_Controller
from Instruments.Abstract import Instrument


class Thorlabs_Camera(Instrument):  # Developer: Magnus Linnet Madsen

    def __init__(self, resource_manager: TLCameraSDK, serial_number: str):
        """
        :param resource_manager:
        :param serial_number:
        """
        self.resource_manager = resource_manager
        self.camera_driver = None
        self.serial_number = serial_number
        self.is_connected = False

    def __del__(self):
        self.disconnect()

    def get_id(self, settings: dict) -> None:
        return self.serial_number

    def connect(self):
        """
        Connect to the Thorlabs camera.
        :return: None
        """

        try:
            camera_serial_list = self.resource_manager.discover_available_cameras()

            if not camera_serial_list:
                message = "Thorlabs Camera.connect: No Thorlabs camera found"
                raise ConnectionError(message)

            if self.serial_number not in camera_serial_list:
                message = "Thorlabs Camera.connect: Camera with serial number " + self.serial_number + " not found"
                raise ConnectionError(message)

            if self.get_is_connected():
                message = "Thorlabs Camera.connect: Camera already connected"
                raise ConnectionError(message)

            self.camera_driver = self.resource_manager.open_camera(self.serial_number)
            self.camera_driver.frames_per_trigger_zero_for_unlimited = 0
            self.camera_driver.arm(2)
            self.camera_driver.issue_software_trigger()

            self.is_connected = True
            Console_Controller.print_message(
                "Connection successfully established to Thorlabs Camera with serial number " + self.serial_number)

        except Exception as error:
            Console_Controller.print_message(error)

    def disconnect(self):
        """
        Disconnects the camera
        :return: None
        """
        try:
            camera_serial_list = self.resource_manager.discover_available_cameras()

            if not camera_serial_list:
                message = "Thorlabs Camera.disconnect: No Thorlabs camera found"
                raise ConnectionError(message)

            if self.serial_number not in camera_serial_list:
                message = "Thorlabs Camera.disconnect: Camera with serial number " + self.serial_number + " not found"
                raise ConnectionError(message)

            if not self.get_is_connected():
                raise ConnectionError("Thorlabs Camera.disconnect: Camera already disconnected ")

            self.camera_driver.dispose()
            self.is_connected = False
            Console_Controller.print_message(
                "Disconnected successfully the Thorlabs Camera with serial number " + self.serial_number)

        except Exception as error:
            Console_Controller.print_message(error)

    def get_is_connected(self):
        return self.is_connected

    def get_exposure_time_us(self):
        """
        Get the exposure time of the camera.
        :return: The exposure time of the camera of type (int) in units of mikro seconds
        """
        return self.camera_driver.exposure_time_us

    def set_exposure_time_us(self, exposure_time_us):
        """
        Set the exposure time of the camera.
        :param exposure_time_us: The exposure time of the camera of type (int) in units of mikro seconds
        :return: None
        """
        exposure_time_us_range = self.get_exposure_time_us_range()
        if min(exposure_time_us_range) <= exposure_time_us <= max(exposure_time_us_range):
            self.camera_driver.exposure_time_us = exposure_time_us
        else:
            print("Exposure time out of range from {} to {}".format(*exposure_time_us_range, self))

    def get_exposure_time_us_range(self):
        """
        Get exposure time range of the camera.
        :return: The exposure time range of the camera of type (int, int) in units of mikro seconds
        """
        exposure_time_us_range = self.camera_driver.exposure_time_range_us
        return exposure_time_us_range.min, exposure_time_us_range.max

    def get_gain(self):
        """
        Get the gain of the camera.
        :return: The camera gain of type in
        """
        return self.camera_driver.gain

    def set_gain(self, gain):
        """
        Set the gain of the camera.
        :param gain: The camera gain of type int
        :return: None
        """
        gain_range = self.get_gain_range()
        if min(gain_range) <= gain <= max(gain_range):
            self.camera_driver.gain = gain
        else:
            Console_Controller.print_message("Gain out of range from {} to {}".format(*self.get_gain_range()))

    def get_gain_range(self):
        """
        Returns the gain range of the Thorlabs camera.
        :return: Gain range of the Thorlabs camera of type (int,int)
        """
        gain_range = self.camera_driver.gain_range
        return gain_range.min, gain_range.max

    def get_frame_time_us(self):
        """
        Returns the frame time in mikro seconds.
        :return: Frame time of type (int) in unit of mikro seconds
        """
        pass

    def get_driver(self):
        """
        Returns the camera driver.
        :return: Driver instance of the type (TLCamera)
        """
        return self.camera_driver

    def get_serial_number(self):
        """
        Returns the serial number of the camera connected.
        :return: Serial number of the camera of type (string)
        """
        return self.serial_number

    def save_settings(self, settings):
        """
        Apply settings to the Thorlabs Camera
        :param settings:
        :return: None
        """
        self.set_exposure_time_us(settings["exposure_time_us"])
        self.set_gain(settings["gain"])

    def load_settings(self):
        """
        Retrieve the current camera settings
        :return: the current camera settings
        """
        return {
            "exposure_time_us": self.get_exposure_time_us(),
            "gain": self.get_gain(),
        }

    def print_settings(self):
        """
        Print the current camera settings
        :return:
        """
        Console_Controller.print_message("Current camera settings: " + str(self.load_settings()))
