import socket
from Thorlabs_PM import Thorlabs_Power_Meter_Driver
from threading import Thread

class Thorlabs_Power_Meter_Server():

    def __init__(self, driver: Thorlabs_Power_Meter_Driver, host_ip='10.209.67.42', port=12347):
            """
            Initializes the power meter.

            Args:
                host_ip (str): The IP address for the server to bind to. Default is '10.209.67.42'.
                port (int): The port number for the server to bind to. Default is 12345.

            Attributes:
                host_ip_address (str): The IP address of the server.
                host_port (int): The port number the server listens on.
                host_socket (socket.socket): The server's socket object.
                running (bool): The server's running state.
                controller (Free_Space_Polarization_Controller): The polarization controller object.

            Raises:
                socket.error: If there is an issue with creating or binding the socket.
            """
            self.host_ip_address = host_ip
            self.host_port = port
            self.host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.host_socket.bind((self.host_ip_address, self.host_port))
            self.host_socket.listen(5)  # Increase backlog to allow multiple connections
            self.running = True
            self.client_socket = None
            print(f"Server listening on {self.host_ip_address}:{self.host_port}")

            self.driver = driver


    def handle_client(self):
        """
        Handles a client connection, processing incoming requests and sending responses.

        Args:
            client_socket (socket.socket): The client socket connected to the server.

        Raises:
            Exception: If an error occurs while handling the client.
        """
        try:
            while self.running:
                request = self.client_socket.recv(1024).decode('utf-8')
                if not request:
                    break
                
                print(f"Received from {self.client_socket.getpeername()}: {request}")

                response = self._handle_request(request)

                print(f"Sending response to {self.client_socket.getpeername()}: {response}")
                self.client_socket.send(response.encode('utf-8'))
        
        except Exception as error:
            print(f"Error handling client: {error}")
        finally:
            print(f"Closing connection with {self.client_socket.getpeername()}")
            self.client_socket.close()

    def _handle_request(self, request):
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
            try:
                self.driver.connect()
                response = 'SUCCESS'
            except Exception as error:
                response = 'UNSUCCESFUL'

        elif request == 'DISCONNECT':
            try:
                self.driver.disconnect()
                response = 'SUCCESS'
            except Exception as error:
                response = 'UNSUCCESFUL'

        elif request.startswith('SET_WAVELENGTH'):
            _, wavelength = request.split()
            self.driver.set_wavelength(float(wavelength))
            response = f"Wavelength set to {wavelength}"

        elif request == 'GET_WAVELENGTH':
            try:
                response = str(self.driver.get_wavelength())
            except Exception as error:
                response = 'UNSUCCESFUL'

        elif request == 'GET_DETECTOR_POWER':
            try:
                response = str(self.driver.get_detector_power())
            except Exception as error:
                response = 'UNSUCCESFUL'

        else:
            response = 'UNKNOWN COMMAND'

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
                self.client_socket, addr = self.host_socket.accept()
                print(f"Accepted connection from {addr}")
                self.handle_client()
        
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


from Thorlabs_PM103E_driver import Thorlabs_PM103E_driver

if __name__ == "__main__": 

    from anyvisa import AnyVisa
    from Thorlabs_PM103E_driver import Thorlabs_PM103E_driver
    print(AnyVisa.FindResources())

    driver = Thorlabs_PM103E_driver("TCPIP0::10.209.67.184::PM103E-4E_M01027537::INSTR")
    driver.connect()
    server = Thorlabs_Power_Meter_Server(driver=driver, host_ip='10.209.67.42', port=12500)
    thread = Thread(target=server.start)
    thread.start()


