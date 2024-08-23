
from Thorlabs_Power_Meter_Driver import Thorlabs_Power_Meter_Driver
import socket 

class Thorlabs_Power_Meter_Proxy(Thorlabs_Power_Meter_Driver):

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
        Establishes a connection to the power meter.

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        self.server_connect()
        request = 'CONNECT'
        response = self.send_request(request)
        print(f"Connect response: {response}")

    def disconnect(self):
        """
        Disconnects from the power meter.

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        
        request = 'DISCONNECT'
        response = self.send_request(request)
        print(f"Disconnect response: {response}")
        self.server_disconnect()

    def get_detector_power(self):
        """
        Get detector power

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        
        request = 'GET_DETECTOR_POWER'
        response = self.send_request(request)
        print(f"Get dector power: {response}")
        return response


    def set_wavelength(self, wavelength: float):
        """
        Sends a request to the server to set the wavelength of the power meter
        Args:
            wavelength (float): wavelength specified
        """
        request = f'SET_WAVELENGTH {str(wavelength)}'
        response = self.send_request(request)
        print(f"Set wavelength response: {response}")


    def get_averaging(self):
        """
        Sends a request to the server to get the wavelength set of the power meter.
        """
        request = 'GET_AVERAGING'
        response = self.send_request(request)
        print(f"Get averaging response: {response}")
        return response
    
    def set_averaging(self, averaging: int):
        """
        Sends a request to the server to set the wavelength of the power meter
        Args:
            averaging (int): averaging specified
        """
        request = f'SET_AVERAGING {str(averaging)}'
        response = self.send_request(request)
        print(f"Set averaging response: {response}")

    def get_wavelength(self):
        """
        Sends a request to the server to get the wavelength set of the power meter.
        """
        request = 'GET_WAVELENGTH'
        response = self.send_request(request)
        print(f"Get wavelength response: {response}")
        return response

if __name__ == "__main__": 
    proxy_1 = Thorlabs_Power_Meter_Proxy(host_ip_address = '10.209.67.42', host_port=12500)
    proxy_2 = Thorlabs_Power_Meter_Proxy(host_ip_address = '10.209.67.42', host_port=12501)

    proxy_1.connect()
    print(proxy_1.get_detector_power())
    proxy_1.disconnect()

    proxy_2.connect()
    print(proxy_2.get_detector_power())
    proxy_2.disconnect()