import socket
import time
from photonicdrivers.Abstract.Connectable import Connectable

class RS_ZNL20_Driver(Connectable):
    def __init__(self, ip_address: str, port=5025):
        self.ip_address = ip_address
        self.port = port
        self.socket: socket.socket | None = None

    def connect(self) -> None:
        self.socket = socket.socket()
        self.socket.settimeout(5)
        self.socket.connect((self.ip_address, self.port))


    def disconnect(self) -> None:
        if self.socket is not None:
            self.socket.close()
            self.socket = None

    def is_connected(self) -> bool:
        success = False
        try:
            response = self.query("*IDN?")
            if response is not None and response != "":
                success = True
        finally:
            return success
        
    def write(self, command: str) -> None:
        self.socket.sendall(command.encode("ascii") + b'\n') # type: ignore

    def read(self, bufsize=4096) -> str:
        return self.socket.recv(bufsize).decode("ascii").strip() # type: ignore

    def query(self, command) -> str:
        self.write(command)
        return self.read()
    
    def reset(self) -> None:
        self.write("*RST")
    
    def identify(self):
        return self.query("*IDN?")
    
    def status(self) -> int:
        return int(self.query("*STB?"))
    
    def wait(self) -> None:
        self.write("*WAI")
    
    def wait_operation_complete(self) -> int:
        return int(self.query("*OPC?"))
    
    def set_frequency_start(self, start: float, channel=1) -> None:
        self.write(f"SENS{channel}:FREQ:START {start}")

    def set_frequency_end(self, end: float, channel=1) -> None:
        self.write(f"SENS{channel}:FREQ:END {end}")
    
    def set_sweep_points(self, points: int, channel=1) -> None:
        self.write(f"SENS{channel}:SWE:POIN {points}")

    def start_sweep(self, channel=1) -> None:
        self.write(f"INIT{channel}:IMM")
    
    def set_data_format(self, format: str, channel=1) -> None:
        self.write(f"CALC{channel}:FORM {format}")
    
    def read_data(self, channel=1) -> str:
        self.query(f"CALC{channel}:DATA?", )

driver = RS_ZNL20_Driver("ip")
driver.connect()
print(driver.is_connected())
print(driver.status())
print(driver.wait_operation_complete())
time.sleep(1)
print(driver.read())