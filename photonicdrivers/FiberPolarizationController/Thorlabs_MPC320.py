import clr
import time

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.PolarizerCLI.dll")

from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.PolarizerCLI import *
from System import Decimal

class Thorlabs_MPC320():

    def __init__(self, serial_number): # serial number S/N can be found underneath the device 
        """Connect to and reset Thorlabs PM101USB"""
        DeviceManagerCLI.BuildDeviceList()
        self.polarization_controller = Polarizer.CreatePolarizer(serial_number)
        self.paddle_1 = PolarizerPaddles.Paddle1
        self.paddle_2 = PolarizerPaddles.Paddle2
        self.paddle_3 = PolarizerPaddles.Paddle3
        self.serial_number = serial_number
        self.polling_rate = 250
        self.time_out = 60000 # 60 seconds to complete move.

    def connect(self):
        self.polarization_controller.Connect(self.serial_number)
        if not self.polarization_controller.IsSettingsInitialized():
            self.polarization_controller.WaitForSettingsInitialized(10000)  # 10 second timeout.
            assert self.polarization_controller.IsSettingsInitialized() is True
        self.polarization_controller.StartPolling(self.polling_rate)  #250ms polling rate.
        time.sleep(1)
        self.polarization_controller.EnableDevice()
        time.sleep(1)  # Wait for device to enable.

    def get_device_info(self):
        device_info = self.polarization_controller.GetDeviceInfo()
        print(device_info.Description)
    
    def get_decription(self):
        return self.polarization_controller.GetDeviceInfo()
    
    def move_to(self,position_1, position_2, position_3):
        self.polarization_controller.MoveTo(position_1, self.paddle_1, self.time_out)
        self.polarization_controller.MoveTo(position_2, self.paddle_2, self.time_out)
        self.polarization_controller.MoveTo(position_3, self.paddle_3, self.time_out)

    def disconnect(self):
        self.polarization_controller.StopPolling()
        self.polarization_controller.Disconnect()

if __name__ == "__main__":
    serial_number = "38449564"
    polarization_controller = Thorlabs_MPC320(serial_number)
    polarization_controller.connect(polling_rate=polling_rate_ms)
    new_pos = Decimal(10.0)  # Must be a .NET decimal.
    polarization_controller.move_to(new_pos,new_pos, new_pos)
    polarization_controller.disconnect()

    
    