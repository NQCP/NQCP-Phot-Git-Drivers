import serial
import time

from instruments.Abstract.Connectable import Connectable


class APS100_PS_Driver(Connectable):
    def __init__(self, com_port:str) -> None:
        self.port = com_port
        self.baud_rate = 9600
        self.timeout = 1

        self.termination_char = '\r'

    def connect(self) -> None:
        self.connection = serial.Serial(port=self.port, baudrate=self.baud_rate, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE, timeout=self.timeout)
    
    def disconnect(self) -> None:
        self.connection.close()

    def is_connected(self) -> bool:
        pass

    def get_id(self) -> None:
        return self.__query("*IDN?;*ESE 12;*ESE?")

    def get_channel(self) -> str:
        return self.__query("CHAN?")
    
    def set_channel(self, channel_number:int) -> str:
        return self.__query(f"CHAN {channel_number}")
    
    def enable_output(self) -> None:
        return self.__query("*IDN?;*ESE 12;*ESE?")

    def disable_output(self) -> None:
        return self.__query("*IDN?;*ESE 12;*ESE?")

    def is_enabled(self) -> bool:
        return self.__query("*IDN?;*ESE 12;*ESE?")
    
    def set_current(self, current_A:float) -> None:
        return self.__query("*IDN?;*ESE 12;*ESE?")

    def get_current(self) -> float:
        return self.__query("IOUT?")

    ################################ PRIVATE METTHODS ################################

    def __query(self, command_str:str) -> str:
        command = f'{command_str}{self.termination_char}'
        # print(command)
        
        self.connection.write(command.encode('utf-8'))

        # print("READING")

        # a small wait is required for the device to send back a response. 0.1 s is too little
        time.sleep(0.2)


        reflected_command = self.connection.readline()
        response_raw = self.connection.readline()
        response = response_raw.decode('utf-8').strip()

        # print(reflected_command)
        # print(response_raw)
        # print(response)

        return response
