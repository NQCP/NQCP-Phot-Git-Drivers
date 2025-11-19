

import serial
from photonicdrivers.Abstract.Connectable import Connectable
from photonicdrivers.Lasers.SuperK.NKTP_DLL import NKTP_DLL
#"C:\Users\Public\Documents\NKT Photonics\SDK\Examples\DLL_Example_Python\NKTPDLL.dll"

import ctypes

# # Load the DLL
# dll_path = r"C:\Users\Public\Documents\NKT Photonics\SDK\Examples\DLL_Example_Python\NKTPDLL.dll"

# nktp_dll = ctypes.CDLL(dll_path)

# import NKTPDLL as NKT 

class SuperK_Driver(Connectable):
    """
    A driver class for controlling an NKT Photonics SuperK COMPACT laser
    via a USB (COM port) serial connection.

    Attributes:
        port (str): The COM port used to connect to the laser (e.g., 'COM5').
        baudrate (int): The baud rate for the serial connection.
        ser (serial.Serial): The active serial connection object.
    """

    def __init__(self, port: str ='COM5', module_address: int =1):
        """
        Initializes the SuperK driver with serial communication parameters.

        Args:
            port (str):
            module_address (int):
        
        """
        self.port=port
        self.module_address=module_address

    def connect(self) -> bool:
        print("Always connected")
        return True
    
    def disconnect(self) -> bool:
        print("Can't disconnect")
        return False
    
    def enable_emission(self) -> None:
        result = NKTP_DLL.registerWriteU8(self.port, self.module_address, 0x30, 0x01, -1)
        #print('Setting emission ON - Extreme:', RegisterResultTypes(result))

    def disable_emission(self) -> None:
        result = NKTP_DLL.registerWriteU8(self.port, self.module_address, 0x30, 0x00, -1)
        # print('Setting emission OFF - Extreme:', RegisterResultTypes(result))

    def set_power_level(self,power_level : float):
        #power_level_hex = hex(power_level)
        result = NKTP_DLL.registerWriteU8(self.port, self.module_address, 0x3E, power_level, -1)

    

