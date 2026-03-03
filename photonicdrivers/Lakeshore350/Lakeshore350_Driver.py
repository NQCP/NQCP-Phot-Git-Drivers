from lakeshore import Model350
from photonicdrivers.Abstract.Connectable import Connectable

class Lakeshore350_Driver(Connectable):
    def __init__(self, com_port:str, baud_rate:int=57600) -> None:
        self.port = com_port
        self.baud = baud_rate

    def connect(self) -> None:
        self.connection: Model350 = Model350(baud_rate=self.baud, com_port=self.port)

    def disconnect(self) -> None:
        self.connection.disconnect_usb()

    def get_id(self) -> str:
        return self.connection.query('*IDN?')
    
    def is_connected(self) -> bool:
        try:
            self.get_id()
            return True
        except Exception:
            return False

    def get_all_kelvin(self) -> list[float]:
        return [float(self.connection.query('KRDG?'))]