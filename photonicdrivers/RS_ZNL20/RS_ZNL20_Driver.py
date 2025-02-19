import socket
from photonicdrivers.Abstract.Connectable import Connectable

class RS_ZNL20_Driver(Connectable):
    def __init__(self, ip_address: str, port=5025):
        self.ip_address = ip_address
        self.port = port
        self.socket: socket.socket | None = None

    def connect(self):
        self.socket = socket.socket()
        self.socket.settimeout(5)
        self.socket.connect((self.ip_address, self.port))


    def disconnect(self):
        if self.socket is not None:
            self.socket.close()
            self.socket = None

    def is_connected(self):
        success = False
        try:
            response = self.query("*IDN?")
            if response is not None and response != "":
                success = True
        finally:
            return success
        
    def write(self, command: str):
        self.socket.sendall(command.encode("ascii") + b'\n') # type: ignore

    def read(self, buf_size=4096) -> str:
        print(self.socket.recv(buf_size)) # type: ignore
        return self.socket.recv(buf_size).decode("ascii").strip() # type: ignore

    def query(self, command) -> str:
        self.write(command)
        return self.read()

driver = RS_ZNL20_Driver("ip")
driver.connect()
print(driver.is_connected())