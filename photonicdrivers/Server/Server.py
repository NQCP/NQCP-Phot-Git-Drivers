
from abc import ABC, abstractmethod

import socket

class Request_Handler(ABC):

    @abstractmethod
    def handle_request(self):
        pass


class Proxy():

    def __init__(self) -> None:
        self.socket = None

    def server_connect(self):
        """
        Establishes a connection to the server.
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host_ip_address, self.host_port))
        print(f"Connected to {self.host_ip_address}:{self.host_port}")

    def server_disconnect(self):
        """
        Closes the connection to the server.
        """
        if self.sock:
            self.sock.close()
            self.sock = None

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
        if not self.sock:
            msg = "Not connected to the server"
            print(msg)
            raise ConnectionError("Not connected to the server")
        try:
            self.sock.sendall(request.encode('utf-8'))
            response = self.sock.recv(1024).decode('utf-8')
            return response
        except socket.timeout:
            print("Socket timeout: No response received")
            return None
        except Exception as error:
            print(error)
            return None

class Server(ABC):

    @abstractmethod
    def handle_client(self):
        pass

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass


class Instrument_Server(Server):
    """
    A server class for controlling a free-space polarization controller over a network.

    Attributes:
        host_ip_address (str): The IP address of the server.
        host_port (int): The port number the server listens on.
        host_socket (socket.socket): The server's socket object.
        running (bool): The server's running state.
        controller (Free_Space_Polarization_Controller): The polarization controller object.

    Methods:
        __init__(host_ip='10.209.67.42', port=12345):
            Initializes the server with the specified IP address and port, sets up the server socket,
            and initializes the polarization controller.

        handle_client(client_socket):
            Handles incoming client connections and processes requests.

        handle_request(request):
            Processes a single client request and returns the appropriate response.

        start():
            Starts the server to accept and handle client connections.

        stop():
            Stops the server and closes the socket.
    """

    def __init__(self, request_handler: Request_Handler, host_ip='10.209.67.42', host_port=8090):
        """
        Initializes the instrument server.

        Args:
            driver: The instrument driver
            host_ip (str): The IP address for the server to bind to. Default is '10.209.67.42'.
            port (int): The port number for the server to bind to. Default is 12345.

        Attributes:
            host_ip_address (str): The IP address of the server.
            host_port (int): The port number the server listens on.
            host_socket (socket.socket): The server's socket object.
            running (bool): The server's running state.
            driver: The instrument driver.

        Raises:
            socket.error: If there is an issue with creating or binding the socket.
        """
        self.host_ip_address = host_ip
        self.host_port = host_port
        self.host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_socket.bind((self.host_ip_address, self.host_port))
        self.host_socket.listen(5)  # Increase backlog to allow multiple connections
        self.running = True
        
        print(f"Server listening on {self.host_ip_address}:{self.host_port}")

        self.request_handler= request_handler 

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

                response = self.request_handler.handle_request(request)

                print(f"Sending response to {client_socket.getpeername()}: {response}")
                client_socket.send(response.encode('utf-8'))
        
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            print(f"Closing connection with {client_socket.getpeername()}")
            client_socket.close()

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
        