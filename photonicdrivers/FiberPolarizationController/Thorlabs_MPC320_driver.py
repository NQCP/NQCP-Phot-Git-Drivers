import clr
from photonicdrivers.utils.execution_time import execution_time
from abc import ABC, abstractmethod
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

    def __init__(self, host_ip_address: str, host_port: int = 12346):
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

class Thorlabs_MPC320_Server:

    def __init__(self, serial_number="38449564", host_ip='localhost', port=12346):

        self.host_ip_address = host_ip
        self.host_port = port
        self.host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_socket.bind((self.host_ip_address, self.host_port))
        self.host_socket.listen(5)  # Increase backlog to allow multiple connections
        self.running = True
        print(f"Server listening on {self.host_ip_address}:{self.host_port}")

        Thorlabs_MPC320_Serial(serial_number=serial_number)

    def handle_client(self, client_socket):
        """
        Handles a client connection, processing incoming requests and sending responses.

        Args:
            client_socket (socket.socket): The client socket connected to the server.

        Raises:
            Exception: If an error occurs while handling the client.
        """
        try:
            while self.running:
                request = client_socket.recv(1024).decode('utf-8')
                if not request:
                    break
                
                print(f"Received from {client_socket.getpeername()}: {request}")

                response = self.handle_request(request)

                print(f"Sending response to {client_socket.getpeername()}: {response}")
                client_socket.send(response.encode('utf-8'))
        
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            print(f"Closing connection with {client_socket.getpeername()}")
            client_socket.close()

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
            'SET_POSITION_0 <position>': Moves the first padlet to a specified position.
            'SET_POSITION_1 <position>': Moves the second padlet to a specified position.
            'SET_POSITION_2 <position>': Moves the third padlet to a specified position.
            Unknown commands will result in a 'Unknown command' response.
        """
        if request == 'CONNECT':
            self.polarization_controller.connect()
            response = 'Connected to polarization controller'

        elif request == 'DISCONNECT':
            self.polarization_controller.disconnect()
            response = 'Disconnected from polarization controller'

        elif request.startswith('SET_POSITION_0'):
            _, position = request.split()
            self.polarization_controller.move_0_to(float(position))
            response = f'Moved padlet 0 to position: {position}'

        elif request.startswith('SET_POSITION_1'):
            _, position = request.split()
            self.polarization_controller.move_1_to(float(position))
            response = f'Moved padlet 1 to position: {position}'

        elif request.startswith('SET_POSITION_2'):
            _, position = request.split()
            self.polarization_controller.move_2_to(float(position))
            response = f'Moved padlet 2 to position: {position}'

        else:
            response = 'Unknown command'

        return response

    def start(self):
        """
        Starts the server to accept and handle client connections.

        The server runs in a loop, accepting connections and spawning a new thread
        to handle each client.
        
        Raises:
            Exception: If an error occurs while accepting connections.
        """
        try:
            while self.running:
                client_socket, addr = self.host_socket.accept()
                print(f"Accepted connection from {addr}")
                self.handle_client(client_socket)
        
        except Exception as e:
            print(f"Error accepting connection: {e}")
        
        finally:
            self.host_socket.close()
            print("Server stopped")

    def stop(self):
        """
        Stops the server and closes the socket.

        Sets the running state to False and closes the server socket.
        """
        self.running = False
        self.host_socket.close()
        print("Server stopped")