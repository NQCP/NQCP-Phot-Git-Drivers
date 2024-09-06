from photonicdrivers.Cameras.Thorlabs.thorlabs_tsi_sdk.tl_camera import TLCameraSDK

class Thorlabs_Camera_Driver():  # Developer: Magnus Linnet Madsen

    def __init__(self, driver: TLCameraSDK, serial_number: str):
        """
        :param resource_manager:
        :param serial_number:
        """
        self.sdk = sdk
        self.driver = driver
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
            camera_serial_list = self.driver.discover_available_cameras()

            if not camera_serial_list:
                message = "Thorlabs Cameras.connect: No Thorlabs camera found"
                raise ConnectionError(message)

            if self.serial_number not in camera_serial_list:
                message = "Thorlabs Cameras.connect: Cameras with serial number " + self.serial_number + " not found"
                raise ConnectionError(message)

            if self.get_is_connected():
                message = "Thorlabs Cameras.connect: Cameras already connected"
                raise ConnectionError(message)

            self.camera_driver = self.driver.open_camera(self.serial_number)
            self.camera_driver.frames_per_trigger_zero_for_unlimited = 0
            self.camera_driver.arm(2)
            self.camera_driver.issue_software_trigger()

            self.is_connected = True
            print("Connection successfully established to Thorlabs Cameras with serial number " + self.serial_number)

        except Exception as error:
            print(error)

    def disconnect(self):
        """
        Disconnects the camera
        :return: None
        """
        try:
            camera_serial_list = self.driver.discover_available_cameras()

            if not camera_serial_list:
                message = "Thorlabs Cameras.disconnect: No Thorlabs camera found"
                raise ConnectionError(message)

            if self.serial_number not in camera_serial_list:
                message = "Thorlabs Cameras.disconnect: Cameras with serial number " + self.serial_number + " not found"
                raise ConnectionError(message)

            if not self.get_is_connected():
                raise ConnectionError("Thorlabs Cameras.disconnect: Cameras already disconnected ")

            self.camera_driver.dispose()
            self.is_connected = False
            print(
                "Disconnected successfully the Thorlabs Cameras with serial number " + self.serial_number)

        except Exception as error:
            print(error)

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
            print("Gain out of range from {} to {}".format(*self.get_gain_range()))

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
        Apply settings to the Thorlabs Cameras
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
        print("Current camera settings: " + str(self.load_settings()))

if __name__ == "__main__":
    from thorlabs_tsi_sdk.tl_camera import TLCameraSDK
    from examples.tkinter_camera_live_view import ImageAcquisitionThread, LiveViewCanvas
    import tkinter as tk

    with TLCameraSDK() as sdk:
        camera_list = sdk.discover_available_cameras()
        print(camera_list)
        with sdk.open_camera(camera_list[0]) as camera:
            # create generic Tk App with just a LiveViewCanvas widget
            print("Generating app...")
            root = tk.Tk()
            root.title(camera.name)
            image_acquisition_thread = ImageAcquisitionThread(camera)
            camera_widget = LiveViewCanvas(parent=root, image_queue=image_acquisition_thread.get_output_queue())

            print("Setting camera parameters...")
            camera.frames_per_trigger_zero_for_unlimited = 0
            camera.arm(2)
            camera.issue_software_trigger()

            print("Starting image acquisition thread...")
            image_acquisition_thread.start()

            print("App starting")
            root.mainloop()

            print("Waiting for image acquisition thread to finish...")
            image_acquisition_thread.stop()
            image_acquisition_thread.join()

            print("Closing resources...")

    print("App terminated. Goodbye!")

