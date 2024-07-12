
from abc import ABC, abstractmethod
from serial import Serial
import socket


class Abstract_Free_Space_Polarization_Controller(ABC):
    @abstractmethod
    def set_polarization(self):
        pass

    @abstractmethod
    def set_polarization(self):
        pass

    @abstractmethod
    def reset_polarization(self):
        pass
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass

class Free_Space_Polarization_Controller(Abstract_Free_Space_Polarization_Controller):

    def __init__(self, port: str, quarter_waveplate_address: int, half_waveplate_address: int):
        self.connection: Serial = None
        self.port: str = port
        self.quarter_waveplate_address: int = quarter_waveplate_address
        self.half_waveplate_address: int = half_waveplate_address
        self.quarter_waveplate: Thorlabs_ELL14K = None
        self.half_waveplate: Thorlabs_ELL14K = None

    def connect(self):
        self.connection = Serial(port=self.port, baudrate=9600, stopbits=1, parity='N', timeout=0.05)
        self.quarter_waveplate = Thorlabs_ELL14K(serial_connection=self.connection, offset=-8529, address=self.quarter_waveplate_address)
        self.half_waveplate = Thorlabs_ELL14K(serial_connection=self.connection, offset=-8529, address=self.half_waveplate_address)

    def disconnect(self):
        self.connection.close()
    
    def set_polarization(self, quarter_waveplate_angle, half_waveplate_angle):
        self.quarter_waveplate.set_angle(quarter_waveplate_angle)
        self.half_waveplate.set_angle(half_waveplate_angle)

    def reset_polarization(self):
        self.quarter_waveplate.home()
        self.half_waveplate.home()

class Free_Space_Polarization_Controller_Proxy(Abstract_Free_Space_Polarization_Controller):
    def __init__(self, host_ip_adress, host_port, instrument_port: str, quarter_waveplate_address: int, half_waveplate_address: int):
        self.host_ip_address: str = host_ip_adress
        self.host_port: str = host_port
        self.instrument_port: str = instrument_port
        self.quarter_waveplate_address: int = quarter_waveplate_address
        self.half_waveplate_address: int = half_waveplate_address

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host_ip_address, self.host_port))
        print(f"Connected to {self.host_ip_address}:{self.host_port}")

    def disconnect(self):
        if self.sock:
            self.sock.close()
            self.sock = None
            print("Disconnected")

    def send_request(self, request):
        if not self.sock:
            raise ConnectionError("Not connected to the server")
        self.sock.sendall(request.encode('utf-8'))
        response = self.sock.recv(1024).decode('utf-8')
        return response

    def set_polarization(self, quarter_waveplate_angle: float, half_waveplate_angle: float):
        request = f'SET_POLARIZATION {self.quarter_waveplate_address} {quarter_waveplate_angle} {self.half_waveplate_address} {half_waveplate_angle}'
        response = self.send_request(request)
        print(f"Set polarization response: {response}")

    def reset_polarization(self):
        request = 'RESET_POLARIZATION'
        response = self.send_request(request)
        print(f"Reset polarization response: {response}")
        
class Free_Space_Polarization_Controller_Server:
    def __init__(self, host_ip='10.209.67.42', port=12345):
        self.host_ip_address = host_ip
        self.host_port = port
        self.host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_socket.bind((self.host_ip_address, self.host_port))
        self.host_socket.listen(5)
        print(f"Server listening on {self.host_ip_address}:{self.host_port}")

    def handle_client(self, client_socket):
        try:
            request = client_socket.recv(1024).decode('utf-8')
            print(f"Received: {request}")
            if request == 'CONNECT':
                self.controller.connect()
                response = 'Connected'
            elif request == 'DISCONNECT':
                self.controller.disconnect()
                response = 'Disconnected'
            elif request.startswith('SET_POLARIZATION'):
                _, qwp_angle, hwp_angle = request.split()
                self.controller.set_polarization(float(qwp_angle), float(hwp_angle))
                response = f"Polarization set: QWP to {qwp_angle}°, HWP to {hwp_angle}°"
            elif request == 'RESET_POLARIZATION':
                self.controller.reset_polarization()
                response = 'Polarization reset'
            else:
                response = 'Unknown command'
            client_socket.send(response.encode('utf-8'))
        except Exception as error:
            print(f"Error handling client: {error}")
        finally:
            client_socket.close()

    def start(self):
        self.running = True
        while self.running:
            try:
                client_socket, addr = self.host_socket.accept()
                print(f"Accepted connection from {addr}")
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
            except Exception as e:
                print(f"Error accepting connections: {e}")
                break

    def stop(self):
        self.running = False
        self.host_socket.close()
        self.controller.disconnect()
        print("Server stopped")


if __name__ == "__main__":
    proxy = Free_Space_Polarization_Controller_Proxy('192.168.1.100', 12345, 'COM3', 1, 2)
    
    proxy.connect()
    proxy.set_polarization(45.0, 90.0)
    proxy.reset_polarization()
    proxy.disconnect()