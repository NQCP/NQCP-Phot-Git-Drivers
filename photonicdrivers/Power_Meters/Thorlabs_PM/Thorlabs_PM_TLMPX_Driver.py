from ctypes import cdll,c_long, c_ulong, c_uint32,byref,create_string_buffer,c_bool,c_char_p,c_int,c_int16,c_double, sizeof, c_voidp, c_uint16

from photonicdrivers.Power_Meters.Thorlabs_PM.TLPMX import TLPMX, TLPM_DEFAULT_CHANNEL

from photonicdrivers.Power_Meters.Thorlabs_PM.Thorlabs_Power_Meter_Driver import Thorlabs_Power_Meter_Driver

# See Thorlabs' github for example https://github.com/Thorlabs/Light_Analysis_Examples/tree/main 
# Get the dll files by downloading the Thorlabs "Optical Power Monitor" software, which will put the files here:
# C:\Program Files\IVI Foundation\VISA\Win64\Bin

"""
Driver class for interfacing with Thorlabs powermeters via the TLPMX dll.

"""

class Thorlabs_PM_TLMPX_Driver(Thorlabs_Power_Meter_Driver):

    def __init__(self, resource_name:str) -> None:
        """
        Initializes the Thorlabs_PM100D_driver instance.

        Args:
            resource_manager (pyvisa.ResourceManager): The VISA resource manager for handling VISA resources.
            port (str): The VISA resource string for connecting to the Thorlabs PM100D power meter.
        """
        self.driver = TLPMX()
        self.resource_name = resource_name
        
    def connect(self) -> None:
        """
        Establishes a connection to the Thorlabs power meter.
        """

        self.driver.open(resourceName=c_char_p(self.resource_name.encode('utf-8')), IDQuery=c_bool(True), resetDevice=c_bool(True))

    def disconnect(self) -> None:
        """
        Closes the connection to the Thorlabs power meter.
        """
        self.driver.close()

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
        self.driver.identificationQuery(manufacturer_name, device_name, serial_number, firmware_revision)
        return manufacturer_name.value, device_name.value, serial_number.value, firmware_revision.value

    def get_averaging(self) -> int:
        """
        Retrieves the current number of averaging cycles configured on the power meter.

        Returns:
            int: The number of averaging cycles.
        """

        average = c_int()
        self.driver.getAvgCnt(averageCount=byref(average), channel=TLPM_DEFAULT_CHANNEL)
        return average.value

    def set_averaging(self, average: int) -> None:
        """
        Sets the number of averaging cycles on the power meter.

        Args:
            average (int): The number of averaging cycles to set.
        """

        average = c_uint16(average)
        self.driver.setAvgCnt(averageCount=average, channel=TLPM_DEFAULT_CHANNEL)

    def set_config_power(self) -> None:
        """
        Configures the power meter for power measurements.
        """
        pass

    def set_auto_range(self, auto_range_bool: bool) -> None:
        """
        Sets the auto range mode of the power meter.

        Args:
            auto_range (str): 'ON' to enable auto range, 'OFF' to disable.
        """
        if auto_range_bool:
            auto_range = c_uint16(1)
        else:
            auto_range = c_uint16(0)
        
        result_code = self.driver.setPowerAutoRange(auto_range, channel=TLPM_DEFAULT_CHANNEL)
        return result_code

    def set_beam(self, beam: str = 'MIN') -> None:
        """
        Sets the beam correction type.

        Args:
            beam (str): The beam correction type ('MIN', 'MAX', etc.).
        """
        pass

    def set_wavelength(self, wavelength):
        """
        Sets the wavelength value in nanometers.

        Args:
            wavelength (float): The wavelength value to set in nanometers.
            channel (int, optional): The sensor channel number. Default is 1.

        Returns:
            int: The return value, 0 is for success.
        """

        wavelength = c_double(wavelength)
        result_code = self.driver.setWavelength(wavelength, channel=TLPM_DEFAULT_CHANNEL)
        return result_code
    
    def get_wavelength(self) -> float:
        """
        Retrieves the current wavelength setting of the power meter.

        Returns:
            float: The wavelength in nanometers.
        """

        wavelength = c_double()
        attribute = c_int()
        attribute.value = 0
        self.driver.getWavelength(attribute=attribute, wavelength=byref(wavelength), channel=TLPM_DEFAULT_CHANNEL)

        return wavelength.value

    def set_power_unit(self, power_unit: str) -> None:
        """
        Sets the units for power measurements.

        Args:
            unit (str): The unit to set ('W', or 'dBm').
        """
        if power_unit == "W":
            unit_num = c_uint16(0)    
        elif power_unit == "dBm":
            unit_num = c_uint16(1)
        
        self.driver.setPowerUnit(powerUnit=unit_num, channel=TLPM_DEFAULT_CHANNEL)

    def get_power_unit(self) -> str:
        """
        Retrieves the current units for power measurements.

        Returns:
            str: The current units ('W', 'mW', or 'dBm').
        """
        
        power_unit = c_uint16()
        self.driver.getPowerUnit(powerUnit=byref(power_unit), channel=TLPM_DEFAULT_CHANNEL)
        if power_unit.value:
            return "dBm"
        else:
            return "W"

    def get_power(self) -> float:
        """
        Retrieves the current power measurement from the detector.

        Returns:
            float: The measured power.
        """

        power =  c_double()
        self.driver.measPower(byref(power),TLPM_DEFAULT_CHANNEL)
        return power.value
    
    def get_power_mW(self) -> float:
        return self.get_power() * 1000
    
    def get_min_wavelength(self) -> float:
        """
        Retrieves the current wavelength setting of the power meter.

        Returns:
            float: The wavelength in nanometers.
        """

        wavelength = c_double()
        attribute = c_int()
        attribute.value = 1
        self.driver.getWavelength(attribute=attribute, wavelength=byref(wavelength), channel=TLPM_DEFAULT_CHANNEL)

        return wavelength.value
    
    def get_max_wavelength(self) -> float:
        """
        Retrieves the current wavelength setting of the power meter.

        Returns:
            float: The wavelength in nanometers.
        """

        wavelength = c_double()
        attribute = c_int()
        attribute.value = 2
        self.driver.getWavelength(attribute=attribute, wavelength=byref(wavelength), channel=TLPM_DEFAULT_CHANNEL)

        return wavelength.value

    def set_power_ref(self, power_reference_value):
        """
        Sets the power reference value.

        Args:
            power_reference_value (float): Specifies the power reference value.

        Returns:
            int: The return value, 0 is for success.
        """
        
        self.driver.setPowerRef(power_reference_value, channel=TLPM_DEFAULT_CHANNEL)
    
    def reset(self) -> None:
        """
        Resets the power meter to its default state.
        """
        pass

    def zero(self) -> None:
        """
        Initiates a zero correction procedure on the detector.
        """
        self.driver.startDarkAdjust(channel=TLPM_DEFAULT_CHANNEL)

