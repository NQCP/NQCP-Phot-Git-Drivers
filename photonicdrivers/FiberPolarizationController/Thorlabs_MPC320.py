import clr
from photonicdrivers.utils.execution_time import execution_time
from abc import ABC, abstractmethod
from serial import Serial
import socket
from photonicdrivers.Server.Server import *

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.PolarizerCLI.dll")

from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.PolarizerCLI import *
from System import Decimal


class Thorlabs_MPC320_Driver(ABC):

    @abstractmethod
    def connect(self):
        """
        Establishes a connection to the polarization controller.

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        pass

    @abstractmethod
    def disconnect(self):
        """
        Disconnects from the polarization controller.

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        pass

    @abstractmethod
    def get_id(self):
        """
        Disconnects from the polarization controller.

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        pass

    @abstractmethod
    def get_decription(self):
        """
        Returns a describe string of the device
        """
        pass
    
    @abstractmethod
    def move_to(self,position_0, position_1, position_2):
        """
        Moves the three padlets to their specified positions
        """
        pass

    @abstractmethod
    def move_0_to(self,position):
        """
        Moves the first padlets to its specified positions
        """
        pass

    @abstractmethod
    def move_1_to(self,position):
        """
        Moves the first padlets to its specified positions
        """
        pass

    @abstractmethod
    def move_2_to(self,position):
        """
        Moves the first padlets to its specified positions
        """
        pass


class Thorlabs_MPC320_Request_handler(Request_Handler):

    def __init__(self, driver) -> None:
        self.driver = driver
    
    def handle_request(self, request):
        """
        Processes a single client request and returns the appropriate response.

        Args:
            request (str): The client request string.

        Returns:
            str: The response string to be sent back to the client.

        Possible Requests:
            'CONNECT': Connects the polarization controller.
            'DISCONNECT': Disconnects the polarization controller.
            'SET_POLARIZATION <qwp_angle> <hwp_angle>': Sets the polarization angles.
            'RESET_POLARIZATION': Resets the polarization to default values.
            'GET_ID': Retrives the id of the connected polarization controller
            Unknown commands will result in a 'Unknown command' response.
        """
        if request == 'CONNECT':
            self.driver.connect()
            response = 'Connected'

        elif request == 'DISCONNECT':
            self.driver.disconnect()
            response = 'Disconnected'

        elif request.startswith('SET_POLARIZATION'):
            _, qwp_angle, hwp_angle = request.split()
            self.driver.set_polarization(float(qwp_angle), float(hwp_angle))
            response = f"Polarization set: QWP to {qwp_angle}°, HWP to {hwp_angle}°"

        elif request == 'RESET_POLARIZATION':
            self.driver.reset_polarization()
            response = 'Polarization reset'

        elif request == 'GET_ID':
            response = self.driver.get_id()

        else:
            response = 'Unknown command'
            
        return response

class Thorlabs_MPC320_Serial(Thorlabs_MPC320_Driver):

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

    def get_position_0(self):
        return self.polarization_controller.GetPosition(0, self.time_out)
        
    def get_position_1(self):
        return self.polarization_controller.GetPosition(1, self.time_out)
    
    def get_position_2(self):
        return self.polarization_controller.GetPosition(2, self.time_out)
        
    def disconnect(self):
        self.polarization_controller.StopPolling()
        self.polarization_controller.Disconnect()

    def get_id(self):
        return "id" 
    

class Thorlabs_MPC320_Proxy(Thorlabs_MPC320_Driver, Proxy):

    def __init__(self, host_ip_address: str, host_port: int):
        self.host_ip_address: str = host_ip_address
        self.host_port: int = host_port
        self.socket = None

    def connect(self):
        """
        Establishes a connection to the polarization controller.

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        self.server_connect()
        request = 'CONNECT'
        response = self.send_request(request)
        print(f"Connect response: {response}")


    def disconnect(self):
        """
        Disconnects from the polarization controller.

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        
        request = 'DISCONNECT'
        response = self.send_request(request)
        print(f"Disconnect response: {response}")
        self.server_disconnect()

    def get_id(self):
        """
        Disconnects from the polarization controller.

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        request = 'GET_ID'
        response = self.send_request(request)
        print(f"Get ID response: {response}")

    def get_decription(self):
        """
        Returns a describe string of the device
        """
        request = 'GET_DESCRIPTION'
        response = self.send_request(request)
        print(f"Get description response: {response}")

    def move_padlet_0_to(self, position):
        """
        Moves the first padlets to its specified positions
        """
        request = f'MOVE_2_TO {position}'
        response = self.send_request(request)
        print(f"Get move padlet 2 to: {response}")

    def move_padlet_1_to(self, position):
        """
        Moves the first padlets to its specified positions
        """
        request = f'MOVE_2_TO {position}'
        response = self.send_request(request)
        print(f"Get move padlet 2 to: {response}")

    def move_padlet_2_to(self, position):
        """
        Moves the first padlets to its specified positions
        """
        request = f'MOVE_2_TO {position}'
        response = self.send_request(request)
        print(f"Get move padlet 2 to: {response}")

    def get_position_0(self):
        request = 'GET_POSITION_0'
        response = self.send_request(request)
        print(f"Get position 0: {response}")

    def get_position_1(self):
        request = 'GET_POSITION_1'
        response = self.send_request(request)
        print(f"Get position 1: {response}")

    def get_position_2(self):
        request = 'GET_POSITION_2'
        response = self.send_request(request)
        print(f"Get position 2: {response}")

