from lakeshore import Model350
from photonicdrivers.Abstract.Connectable import Connectable

class Lakeshore350_Driver(Connectable):
    def __init__(self, ip_address:str) -> None:
        self.ip_address = ip_address

    def connect(self) -> None:
        self.connection = Model350(ip_address=self.ip_address)

    def disconnect(self) -> None:
        self.connection.disconnect_tcp()
        self.connection = None

    def is_connected(self) -> bool:
        try:
            self.get_id()
            return True
        except Exception:
            return False

    def get_all_kelvin(self) -> list[float]:
        return [float(self.connection.query('KRDG?'))]
    
    def get_id(self) -> str:
        return self.connection.query('*IDN?')