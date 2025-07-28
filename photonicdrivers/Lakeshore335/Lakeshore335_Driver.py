# https://pypi.org/project/lakeshore/
# https://lake-shore-python-driver.readthedocs.io/en/latest/model_335.html 

from lakeshore import Model335
from photonicdrivers.Abstract.Connectable import Connectable

class Lakeshore335_Driver(Connectable):
    def __init__(self, com_port:str, baud_rate:int=57600) -> None:
        self.port = com_port
        self.baud = baud_rate

    def connect(self) -> None:
        self.connection = Model335(baud_rate=self.baud, com_port=self.port)
        # self.connection.connect_usb

    def disconnect(self) -> None:
        self.connection = None

    def is_connected(self) -> bool:
        try:
            self.get_id()
            return True
        except Exception:
            return False

    def get_id(self) -> str:
        return self.connection.query('*IDN?')
    
    def get_all_kelvin(self) -> list[float]:
        '''
        Returns temperature reading in kelvin for all sensors in an array of floats
        '''
        return self.connection.get_all_kelvin_reading()
