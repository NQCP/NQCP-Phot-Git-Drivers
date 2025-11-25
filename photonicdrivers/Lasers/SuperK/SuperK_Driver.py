

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
        port (str): The COM port to which the SuperK laser is connected.
        module_address (int): The module address for communication.
    """

    def __init__(self, port: str ='COM5', module_address: int =1):
        """
        Initializes the SuperK driver with serial communication parameters.

        Args:
            port (str): The COM port to which the SuperK laser is connected. Defaults to 'COM5'.
            module_address (int): The module address for communication. Defaults to 1.
        
        """
        self.port=port
        self.module_address=module_address

    def connect(self) -> bool:
        pass
    
    def disconnect(self) -> bool:
        pass
    
    def enable_emission(self) -> None:
        """
        Enables laser emission.
        0x30 is the register for emission control. Writing 0x01 (1) enables emission. -1 is for registers with multiple entry points.
        """
        result = NKTP_DLL.registerWriteU8(self.port, self.module_address, 0x30, 0x01, -1)
        #print('Setting emission ON - Extreme:', RegisterResultTypes(result))

    def disable_emission(self) -> None:
        """
        Disables laser emission.
        0x30 is the register for emission control. Writing 0x00 (0) disables emission. -1 is for registers with multiple entry points.
        """
        result = NKTP_DLL.registerWriteU8(self.port, self.module_address, 0x30, 0x00, -1)
        # print('Setting emission OFF - Extreme:', RegisterResultTypes(result))

    def get_emission_status(self) -> bool:
        """
        Gets the current laser emission status.
        0x30 is the register for emission control. -1 is for registers with multiple entry points.

        Returns:
            bool: True if emission is enabled, False otherwise.
        """
        emission_status = NKTP_DLL.registerReadU8(self.port, self.module_address, 0x30, -1)
        return emission_status == 1

    def set_power_level(self,power_level : int):
        """
        Sets the laser power level.
        0x3E is the register for power level control. The power_level argument should be a float representing the desired power level between 0 and 100. -1 is for registers with multiple entry points.
        """
        result = NKTP_DLL.registerWriteU8(self.port, self.module_address, 0x3E, power_level, -1)

    def get_power_level(self) -> int:
        """
        Gets the current laser power level.
        0x3E is the register for power level control. -1 is for registers with multiple entry points.

        Returns:
            int: The current power level of the laser.
        """
        power_level = NKTP_DLL.registerReadU8(self.port, self.module_address, 0x3E, -1)
        return power_level
    
    def is_connected(self) -> bool:
        """
        Checks if the laser is connected.

        Returns:
            bool: True if connected, False otherwise.
        """
        return True

    

