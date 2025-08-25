import serial
import time
import socket

from photonicdrivers.Abstract.Connectable import Connectable


class APS100_PS_Driver(Connectable):
    def __init__(self, com_port:str = None, IP_address:str=None, IP_port:float=None,) -> None:
        print("Initialising APS100 Ps Driver. Make sure to set it to REMOTE mode to control it.")
        
        self.port = com_port
        self.baud_rate = 9600
        self.timeout = 1

        self.termination_char = '\r'

        self.ip_address = IP_address
        self.port_number = IP_port

        if self.port is not None:
            print('Connection will be via USB')
            self.connectionType = 'USB'

        elif self.ip_address is not None and self.port_number is not None:
            print('Connection will be via Ethernet')
            self.connectionType = 'Ethernet'

        else:
            print("Either com_port or (IP_address and port) must be provided for APS100_PS_Driver initialization.")

    def connect(self) -> None:
        if self.connectionType == 'USB':
            self.connection = serial.Serial(port=self.port, baudrate=self.baud_rate, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE, timeout=self.timeout)

        elif self.connectionType == 'Ethernet':
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.settimeout(5)  # sets the timeout of the receive command.
            self.server_address = (self.ip_address, self.port_number)  # IP address, port
            self.connection.connect(self.server_address)

        else:
            print("Insufficient arguments for connecting the APS100_PS_Driver class")
   
    def disconnect(self) -> None:
        self.connection.close()

    def is_connected(self) -> bool:
        try:
            self.get_id()
            return True
        except Exception:
            return False

    def get_id(self) -> None:
        return self.__query("*IDN?;*ESE 12;*ESE?")

    def get_channel(self) -> str:
        '''
        Returns which output channel is currently controlled (1 or 2)
        '''
        return self.__query("CHAN?")
    
    def set_channel(self, channel_number:int) -> str:
        '''
        Sets which output channel is currently controlled (1 or 2)
        '''
        return self.__write(f"CHAN {channel_number}")
       
    def set_control_remote(self) -> str:
        if self.connectionType == 'Ethernet':
            print("It is not possible nor necessary to set the PS to REMOTE when operating via ethernet.")
            return
        return self.__write("REMOTE")
    
    def set_control_local(self) -> str:
        return self.__write("LOCAL")
    
    def get_control_mode(self) -> str:
        return "There is no way of asking the PS whether it is in LOCAL or REMOTE mode. Look at the front panel"

    def get_unit(self) -> str:
        return self.__query("UNITS?")
    
    def set_unit(self, unit:str) -> str:
        '''
        Unit options are A or kG.
        Both G and kG will set the unit to kG.
        '''
        # The PS will also accept T and G as an input, but it will set the unit to kG
        if unit == "A" or unit == "kG":
            print(f"Changing unit to {unit}")
            try:
                response = self.__write(f"UNITS {unit}")
                time.sleep(0.5)  # wait for the command to be processed
                print(f"Unit set to {self.get_unit()}")
                return response
            except:
                warning_str = "Set unit failed"
                print(warning_str)
                return warning_str
        else:
            print(f"Trying to set unit to {unit}, but it must be kG or A.")

    def get_lower_limit(self) -> str:
        return self.__query("LLIM?")

    def set_lower_limit(self, limit:float, unit:str):
        '''
        unit: should be A or kG
        '''
        ps_unit = self.get_unit()
        if  ps_unit != unit:
            warning_str = f"Trying to set the lower limit to {limit} {unit}, but the power supply unit is {ps_unit}. Ignoring command."
            print(warning_str)
            return warning_str
        return self.__write(f"LLIM {limit}")

    def get_upper_limit(self) -> tuple[float, str]:
        ps_unit = self.get_unit()
        raw_response = self.__query("ULIM?")
        if ps_unit == "A":
            limit, unit = raw_response.split("A")
        elif ps_unit == "kG":
            limit, unit = raw_response.split("kG")
        return limit, unit

    def set_upper_limit(self, limit:float, unit:str):
        '''
        unit: should be A or kG
        '''
        ps_unit = self.get_unit()
        if  ps_unit != unit:
            warning_str = f"Trying to set the upper limit to {limit} {unit}, but the power supply unit is {ps_unit}. Ignoring command."
            print(warning_str)
            return warning_str
        return self.__write(f"ULIM {limit}")
    
    def ramp_up(self, wait_while_ramping:bool=True, target_relative_tolerance:float=0) -> str:
        return self.__ramp("SWEEP UP", wait_while_ramping, target_relative_tolerance)
    
    def ramp_down(self, wait_while_ramping:bool=True, target_relative_tolerance:float=0) -> None:
        return self.__ramp("SWEEP DOWN", wait_while_ramping, target_relative_tolerance)
    
    def ramp_to_zero(self, wait_while_ramping:bool=True) -> None:
        return self.__ramp("SWEEP ZERO", wait_while_ramping)
    
    def get_sweep_mode(self) -> str:
        '''
        Returns: "Sweeping up", "Standby", "Pause", "Sweeping to zero", "Sweeping down"
        '''
        return self.__query("SWEEP?")
    
    # Attocube says the IMAG command should be avoided, as it ignores ramp rate limits.
    # def set_current(self, current_A:float, channel:int=None) -> None:
    #     # if channel != None:
    #     #     self.set_channel(str(channel))
    #     return self.__query(f"IMAG {current_A}")
    
    def __get_output(self, channel:int=None) -> str:
        '''
        Returns the output of the power supply in whatever unit it is in.
        '''
        return self.__query("IMAG?")
        
    
    def get_current(self, channel:int=None) -> float:
        '''
        Returns the current in A
        '''
        if channel != None:
            self.set_channel(str(channel))        
        
        if self.unit != "A":
            print("Changing unit to A")
            self.set_unit("A")
            print(self.get_unit())
        
        response = self.__get_output()
        current = response.rstrip('A')
        return float(current)
    
    # Attocube says the IMAG command should be avoided, as it ignores ramp rate limits.
    # def set_field(self, field_T:float, channel:int=None) -> None:
    #     if channel != None:
    #         self.set_channel(str(channel))
    #     field_kG = field_T*10
    #     return self.__query(f"IMAG {field_kG} G")

    def get_field(self, channel:int=None) -> float:
        '''
        Returns the field in kG. This number is derived from the current used a factor determined at the factory
        '''
        if channel != None:
            print("Changing unit to kG")
            self.set_channel(str(channel))

        if self.get_unit() != "kG":
            print("Changing unit to kG")
            self.set_unit("kG")
            print(self.get_unit())        
        response = self.__get_output()
        print(response)
        print(self.get_unit())
        field_kG = float(response.rstrip('kG'))
        return field_kG
    
    def query_custom_command(self, command:str) -> str:
        return(self.__query(command))

    ################################ PRIVATE METHODS ################################

    def __ramp(self, command:str, wait_while_ramping:bool, target_relative_tolerance:float=0) -> str:
        self.__write(command)
        status = "unknown"
        if wait_while_ramping: 
            print("Check if with the current ramp rates, the PS never really reaches the target field") # Can be removed later if ramp rates are made less cautious
            within_tolerance = False
            target = self.get_upper_limit()[0]

            while status != "Standby" and not within_tolerance:
                time.sleep(0.2)
                status = self.get_sweep_mode()

                raw_output = self.__get_output()
                ps_unit = self.get_unit()
                if ps_unit == "A":
                    output, unit = raw_output.split("A")
                elif ps_unit == "kG":
                    output, unit = raw_output.split("kG")

                relative_deviation = abs((float(output) - float(target)) / float(target))            
                if relative_deviation < target_relative_tolerance:
                    within_tolerance = True

                print(f"Status: {status}, Output: {output} {unit}")

    # def __query(self, command_str:str) -> str:
    #     if self.connectionType == 'USB':  
    #         command = f'{command_str}{self.termination_char}'        
    #         self.connection.write(command.encode('utf-8'))

    #         # a small wait is required for the device to send back a response. 0.1 s is too little
    #         time.sleep(0.2)

    #         # The power supply first returns the command that was sent to it:
    #         reflected_command = self.connection.readline()
    #         # The power supply then returns its response (if any)
    #         response_raw = self.connection.readline()
    #         response = response_raw.decode('utf-8').strip()

    #     elif self.connectionType == 'Ethernet':
    #         command = command_str + self.termination_char
    #         print(f"Sending command: {command}")
    #         self.connection.sendall(command.encode())

    #         time.sleep(0.2)
            
    #         response = self.connection.recv(1024)
    #         print(f"Received response: {response}")
    #          # remove the newline characters if present
    #         if b"\r\n" in response:
    #             response, dummy = response.split(b'\r\n')

    #         # convert from byte string to string
    #         response = response.decode('utf-8')

    #     else:
    #         ('ERROR in APS100_PS_Driver class - connection has not been initialised properly')            

    #     return response
    
    def __read(self) -> str:
        '''
        Reads a response from the device.
        '''
        if self.connectionType == 'USB':
            response_raw = self.connection.readline()
            response = response_raw.decode('utf-8').strip()

        elif self.connectionType == 'Ethernet':
            response = self.connection.recv(1024)
            # remove the newline characters if present
            if b"\r\n" in response:
                response, dummy = response.split(b'\r\n')

            # convert from byte string to string
            response = response.decode('utf-8')
        else:
            raise Exception("ERROR in APS100_PS_Driver class - connection has not been initialised properly")
        print(f"Received response: {response}")
        return response
        
    def __write(self, command_str:str) -> None:
        '''
        Writes a command to the device.
        '''
        command = command_str + self.termination_char  
        print(f"Sending command: {command}")

        if self.connectionType == 'USB':                
            self.connection.write(command.encode('utf-8'))            
            reflected_command = self.connection.readline() # The power supply first returns the command that was sent to it:

        elif self.connectionType == 'Ethernet':
            self.connection.sendall(command.encode())

        else:
            raise Exception("ERROR in APS100_PS_Driver class - connection has not been initialised properly")\
            
    def __query(self, command:str) -> str:
        '''
        Sends a command to the device and returns the response.
        '''
        self.__write(command)
        response = self.__read()
        
        return response
