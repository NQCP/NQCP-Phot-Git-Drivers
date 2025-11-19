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
    
    def get_heater_output_mode(self, output: int) -> dict:
        return self.connection.get_heater_output_mode(output)
    
    def all_heaters_off(self):
        self.connection.all_heaters_off()

    def set_temperature_limit(self, output: int, temperature_limit: float) -> None:
        self.connection.set_temperature_limit(output, temperature_limit)

    def set_temperature_setpoint(self, output: int, setpoint_in_K: float) -> None:
        self.connection.set_control_setpoint(output, setpoint_in_K)
    
    def get_temperature_setpoint(self, output: int) -> float:
        return self.connection.set_control_setpoint(output)
    
    def set_heater_range(self, output: int, range: int) -> None:
        """
        Args:
            range (int): range value. 0 = OFF, 1 = LOW, 2 = MED, 3 = HIGH
        """
        self.connection.set_heater_range(output, range)

    def get_heater_range(self, output: int) -> int:
        """
        Args:
            range (int): range value. 0 = OFF, 1 = LOW, 2 = MED, 3 = HIGH
        """
        return self.connection.get_heater_range(output)

