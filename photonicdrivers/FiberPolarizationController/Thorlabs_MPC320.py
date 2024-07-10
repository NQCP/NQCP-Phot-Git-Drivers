import clr
from photonicdrivers.utils.execution_time import execution_time

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
        """
        
        """
        self.polarization_controller.Connect(self.serial_number)
        if not self.polarization_controller.IsSettingsInitialized():
            self.polarization_controller.WaitForSettingsInitialized(10000)  # 10 second timeout.
            assert self.polarization_controller.IsSettingsInitialized() is True
        self.polarization_controller.StartPolling(self.polling_rate)  
        self.polarization_controller.EnableDevice()
    
    def get_decription(self):
        """
        Returns a describe string of the device
        """
        return self.polarization_controller.GetDeviceInfo()
    
    def move_to(self,position_0, position_1, position_2):
        """
        Moves the three padlets to their specified positions
        """
        self.polarization_controller.MoveTo(Decimal(position_0), self.paddle_1, self.time_out)
        self.polarization_controller.MoveTo(Decimal(position_1), self.paddle_2, self.time_out)
        self.polarization_controller.MoveTo(Decimal(position_2), self.paddle_3, self.time_out)

    def move_0_to(self,position):
        """
        Moves the first padlets to its specified positions
        """
        self.polarization_controller.MoveTo(Decimal(position), self.paddle_1, self.time_out)

    def move_1_to(self,position):
        """
        Moves the first padlets to its specified positions
        """
        self.polarization_controller.MoveTo(Decimal(position), self.paddle_2, self.time_out)

    def move_2_to(self,position):
        """
        Moves the first padlets to its specified positions
        """
        self.polarization_controller.MoveTo(Decimal(position), self.paddle_3, self.time_out)

    def move_padlet_to(self,position, padlet_index):
        """
        Moves the first padlets to its specified positions
        """
        if padlet_index == 0:
            self.move_0_to(position)
        if padlet_index == 1:
            self.move_1_to(position)
        if padlet_index == 2:
            self.move_2_to(position)

    def home(self):
        """
        Homes all three padlets to the starting position
        """
        self.polarization_controller.Home(self.paddle_1, self.time_out)
        self.polarization_controller.Home(self.paddle_2, self.time_out)
        self.polarization_controller.Home(self.paddle_3, self.time_out)
        

    def disconnect(self):
        self.polarization_controller.StopPolling()
        self.polarization_controller.Disconnect()


    
    