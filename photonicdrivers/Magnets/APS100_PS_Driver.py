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
        self.unit = self.get_unit()
    
    def disconnect(self) -> None:
        self.connection.close()

    def is_connected(self) -> bool:
        try:
            self.get_id()
            return True
        except:
            return False

    def get_id(self) -> None:
        return self.__query("*IDN?;*ESE 12;*ESE?")

    def get_channel(self) -> str:
        return self.__query("CHAN?")
    
    def set_channel(self, channel_number:int) -> str:
        return self.__query(f"CHAN {channel_number}")
    
    def enable_output(self) -> None:
        print("this does nothign atm")
        return self.__query("*IDN?;*ESE 12;*ESE?")

    def disable_output(self) -> None:
        print("this does nothign atm")
        return self.__query("*IDN?;*ESE 12;*ESE?")

    def is_enabled(self) -> bool:
        print("this does nothign atm")
        return self.__query("*IDN?;*ESE 12;*ESE?")
    
    def get_mode(self) -> str:
        return self.__query("MODE?")
    
    def set_control_remote(self) -> str:
        return self.__query("REMOTE")
    
    def set_control_local(self) -> str:
        return self.__query("LOCAL")

    def get_unit(self) -> str:
        return self.__query("UNITS?")
    
    def set_unit(self, unit:str) -> str:
        if unit == "G" or unit == "A" or unit == "T" or unit == "kG":
            self.__query(f"UNITS {unit}")
        else:
            print(f"Trying to set unit to {unit}, but it must be G, kG, T, or A.")
    
    def get_lower_current_limit(self) -> str:
        return self.__query("LLIM?")

    def set_lower_current_limit(self, current:float):
        return self.__query(f"LLIM {current}")
    
    def get_upper_current_limit(self) -> str:
        return self.__query("ULIM?")

    def set_upper_current_limit(self, current:float):
        return self.__query(f"ULIM {current}")

    def set_current(self, current_A:float, channel:int=None) -> None:
        # if channel != None:
        #     self.set_channel(str(channel))
        return self.__query(f"IMAG {current_A}")
    
    def get_current(self, channel:int=None) -> float:
        '''
        Returns the current in A
        '''
        if channel != None:
            self.set_channel(str(channel))        
        
        if self.unit != "A":
            self.set_unit("A")
        
        response = self.__query("IMAG?")
        current = response.rstrip('A')
        return float(current)
    
    def set_field(self, field_T:float, channel:int=None) -> None:
        if channel != None:
            self.set_channel(str(channel))

        field_kG = field_T*10
        return self.__query(f"IMAG {field_kG} G")

    def get_field(self, channel:int=None) -> float:
        '''
        Returns the field in T. This number is derived from the current used a factor determined at the factory
        '''
        if channel != None:
            self.set_channel(str(channel))

        if self.unit != "G":
            self.set_unit("G")
        
        response = self.__query("IMAG?")
        field_kG = response.rstrip('G')
        field_T = field_kG/10
        return float(field_T)
    
    def send_custom_command(self, command:str) -> str:
        return(self.__query(command))

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

        # print("")
        print(reflected_command)
        print(response_raw)
        print(response)
        # print("")

        return response
