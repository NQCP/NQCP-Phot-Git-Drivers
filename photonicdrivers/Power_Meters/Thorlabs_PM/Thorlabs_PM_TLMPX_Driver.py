from ctypes import cdll,c_long, c_ulong, c_uint32,byref,create_string_buffer,c_bool,c_char_p,c_int,c_int16,c_double, sizeof, c_voidp

from TLPMX import TLPMX
from TLPMX import TLPM_DEFAULT_CHANNEL

from photonicdrivers.Power_Meters.Thorlabs_PM.Thorlabs_Power_Meter_Driver import Thorlabs_Power_Meter_Driver

# See Thorlabs' githib for example https://github.com/Thorlabs/Light_Analysis_Examples/tree/main 
# Get the dll files by downloading the Thorlabs "Optical Power Monitor" software, which will put the files here:
# C:\Program Files\IVI Foundation\VISA\Win64\Bin

"""
Driver class for interfacing with Thorlabs powermeters via the TLPMX dll.

"""

class Thorlabs_PM_TLMPX_Driver(Thorlabs_Power_Meter_Driver):

    def __init__(self, _resource_name:str) -> None:
        """
        Initializes the Thorlabs_PM100D_driver instance.

        Args:
            resource_manager (pyvisa.ResourceManager): The VISA resource manager for handling VISA resources.
            port (str): The VISA resource string for connecting to the Thorlabs PM100D power meter.
        """
        self.powerMeter = TLPMX()
        self.resource_name = c_char_p(_resource_name.encode('utf-8'))
        
    def connect(self) -> None:
        """
        Establishes a connection to the Thorlabs power meter.
        """
        self.powerMeter.open(self.resource_name, c_bool(True), c_bool(True))

    def disconnect(self) -> None:
        """
        Closes the connection to the Thorlabs power meter.
        """
        self.powerMeter.close()

    def is_connected(self) -> bool:
        """
        Checks if a connection to the Thorlabs power meter is established.

        Returns:
            bool: True if the device is connected, False otherwise.
        """
        try:
            return self.get_idn() is not None
        except ConnectionError:
            return False
        except Exception:
            return False

    def get_idn(self) -> str:
        """
        Retrieves the identification string of the Thorlabs PM100D power meter.

        Returns:
            str: The response from the *IDN? command.
        """
        manufacturer_name = create_string_buffer(256)
        device_name = create_string_buffer(256)
        serial_number = create_string_buffer(256)
        firmware_revision = create_string_buffer(256)
        self.powerMeter.identificationQuery(manufacturer_name, device_name, serial_number, firmware_revision)
        return manufacturer_name.value, device_name.value, serial_number.value, firmware_revision.value

    def get_averaging(self) -> int:
        """
        Retrieves the current number of averaging cycles configured on the power meter.

        Returns:
            int: The number of averaging cycles.
        """
        pass

    def set_averaging(self, average: int) -> None:
        """
        Sets the number of averaging cycles on the power meter.

        Args:
            average (int): The number of averaging cycles to set.
        """
        pass

    def set_config_power(self) -> None:
        """
        Configures the power meter for power measurements.
        """
        pass

    def set_auto_range(self, auto_range: str = 'ON') -> None:
        """
        Sets the auto range mode of the power meter.

        Args:
            auto_range (str): 'ON' to enable auto range, 'OFF' to disable.
        """
        pass

    def set_beam(self, beam: str = 'MIN') -> None:
        """
        Sets the beam correction type.

        Args:
            beam (str): The beam correction type ('MIN', 'MAX', etc.).
        """
        pass

    def set_wavelength(self, wavelength_nm: float) -> None:
        """
        Sets the detector wavelength for calibration.

        Args:
            wavelength_nm (float): The wavelength in nanometers.
        """
        pass

    def set_units(self, unit: str) -> None:
        """
        Sets the units for power measurements.

        Args:
            unit (str): The unit to set ('W', 'mW', or 'dBm').
        """
        pass

    def get_units(self) -> str:
        """
        Retrieves the current units for power measurements.

        Returns:
            str: The current units ('W', 'mW', or 'dBm').
        """
        pass

    def get_power(self) -> float:
        """
        Retrieves the current power measurement from the detector.

        Returns:
            float: The measured power.
        """
        power =  c_double()
        self.powerMeter.measPower(byref(power),TLPM_DEFAULT_CHANNEL)
        return power.value

    def get_wavelength(self) -> float:
        """
        Retrieves the current wavelength setting of the power meter.

        Returns:
            float: The wavelength in nanometers.
        """
        pass

    def reset(self) -> None:
        """
        Resets the power meter to its default state.
        """
        pass

    def zero(self) -> None:
        """
        Initiates a zero correction procedure on the detector.
        """
        pass

