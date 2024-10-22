import serial
import time

from instruments.Abstract.Connectable import Connectable


class APS100_PS_Driver(Connectable):
    def __init__(self) -> None:
        pass

    def connect(self) -> None:
        return super().connect()
    
    def disconnect(self) -> None:
        return super().disconnect()

    def is_connected() -> bool:
        pass

    def get_id() -> None:
        pass

    def enable_output(self) -> None:
        pass

    def disable_output(self) -> None:
        pass

    def is_enabled(self) -> bool:
        pass

    def set_current(self, current_A:float) -> None:
        pass

    def get_current(self) -> float:
        pass

    ################################ PRIVATE METTHODS ################################

    def __query(self, command_str:str) -> str:
        pass
    
COM_PORT = 'COM8'
BAUD_RATE = 9600

device = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
device.write(b'*IDN?\n')
time.sleep(0.5)
response = device.readline().decode('utf-8').strip()