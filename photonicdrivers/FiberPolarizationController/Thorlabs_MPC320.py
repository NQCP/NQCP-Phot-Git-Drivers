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
    def set_position_0(self,position):
        """
        Moves the first padlets to its specified positions
        """
        pass

    @abstractmethod
    def set_position_1(self,position):
        """
        Moves the first padlets to its specified positions
        """
        pass

    @abstractmethod
    def set_position_2(self,position):
        """
        Moves the first padlets to its specified positions
        """
        pass

class Thorlabs_MPC320_Request_handler(Request_Handler):

    def __init__(self, driver: Thorlabs_MPC320_Driver) -> None:
        self.driver: Thorlabs_MPC320_Driver = driver
    
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
            return 'Connected'

        if request == 'DISCONNECT':
            self.driver.disconnect()
            return 'Disconnected'
        
        if request.startswith("SET_POSITION_0"):
            _, position = request.split()
            self.driver.set_position_0(position=float(position))
            return f'Set position_0 to {position}'
        
        if request.startswith("SET_POSITION_1"):
            _, position = request.split()
            self.driver.set_position_1(position=float(position))
            return f'Set position_1 to {position}'
        
        if request.startswith("SET_POSITION_2"):
            _, position = request.split()
            self.driver.set_position_2(position=float(position))
            return f'Set position_2 to {position}'        
        return 'Unknown command'

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
        self.polarization_controller.Connect(self.serial_number)
        if not self.polarization_controller.IsSettingsInitialized():
            self.polarization_controller.WaitForSettingsInitialized(10000)  # 10 second timeout.
            assert self.polarization_controller.IsSettingsInitialized() is True
        self.polarization_controller.StartPolling(self.polling_rate)  
        self.polarization_controller.EnableDevice()
    
    def set_position_0(self,position:float):
        """
        Moves the first padlets to its specified positions
        """
        self.polarization_controller.MoveTo(Decimal(position), self.paddle_1, self.time_out)

    def set_position_1(self,position:float):
        """
        Moves the first padlets to its specified positions
        """
        self.polarization_controller.MoveTo(Decimal(position), self.paddle_2, self.time_out)

    def set_position_2(self,position:float):
        """
        Moves the first padlets to its specified positions
        """
        self.polarization_controller.MoveTo(Decimal(position), self.paddle_3, self.time_out)
        
    def disconnect(self):
        self.polarization_controller.StopPolling()
        self.polarization_controller.Disconnect()
    
class Thorlabs_MPC320_Proxy(Thorlabs_MPC320_Driver):

    def __init__(self, host_ip_address: str, host_port: int):
        self.host_ip_address: str = host_ip_address
        self.host_port: int = host_port
        self.socket = None

    def server_connect(self):
            """
            Establishes a connection to the server.
            """
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host_ip_address, self.host_port))
            print(f"Connected to {self.host_ip_address}:{self.host_port}")

    def server_disconnect(self):
        """
        Closes the connection to the server.
        """
        if self.socket:
            self.socket.close()
            self.socket = None

    def send_request(self, request: str) -> str:
        """
        Sends a request to the server and waits for a response.

        Args:
            request (str): The request string to send.

        Returns:
            str: The response from the server.

        Raises:
            ConnectionError: If not connected to the server.
        """
        print(request)
        if not self.socket:
            print("Not connected to the server")
            raise ConnectionError("Not connected to the server")
        try:
            self.socket.sendall(request.encode('utf-8'))
            response = self.socket.recv(1024).decode('utf-8')
            return response
        except socket.timeout:
            print("Socket timeout: No response received")
            return None
        except Exception as error:
            print(error)
            return None


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

    def set_position_0(self, position):
        """
        Moves the first padlets to its specified positions
        """
        request = f'SET_POSITION_0 {position}'
        response = self.send_request(request)
        print(f"Get move padlet 2 to: {response}")

    def set_position_1(self, position):
        """
        Moves the first padlets to its specified positions
        """
        request = f'SET_POSITION_1 {position}'
        response = self.send_request(request)
        print(f"Get move padlet 2 to: {response}")

    def set_position_2(self, position):
        """
        Moves the first padlets to its specified positions
        """
        request = f'SET_POSITION_2 {position}'
        response = self.send_request(request)
        print(f"Get move padlet 2 to: {response}")
