

class Thorlabs_Camera_Stub: # Developer: Magnus Linnet Madsen

    def __init__(self, camera_driver, serial_number):
        self.serial_number = serial_number
        self.camera_driver = camera_driver

    def connect(self):
        pass

    def disconnect(self):
        pass

    def get_exposure_time_us(self):
        return 1000000

    def set_exposure_time_us(self, exposure_time_us):
        pass

    def get_exposure_time_us_range(self):
        return 10000

    def get_gain(self):
        return 100

    def set_gain(self, gain):
        pass

    def get_gain_range(self):
        return (0, 100)

    def get_frame_time_us(self):
        return 100

    def get_driver(self):
        return self.camera_driver

    def get_serial_number(self):
        return self.serial_number
