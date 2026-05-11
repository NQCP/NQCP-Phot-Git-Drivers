from ..Abstract.Connectable import Connectable
from atto_device.CRYO2100.attoDry2100 import Device


class AttoDry2100_Driver(Connectable):
    """Driver for interfacing with the AttoDry2100. Inherits from Connectable and Device.

    Args:
        Connectable (Abstract): abstract class for devices that can be connected to and disconnected from.
        Device (Device): device class from the atto_device library that provides methods for communicating with the AttoDry2100.
    """
    def __init__(self, ip_address: str):
        self.ip_address = ip_address

        self.device = Device(address=self.ip_address)

    # Connectable interface methods
    def connect(self) -> None:
        """Connects to the AttoDry2100 using the connect method from the Device class."""
        self.device.connect()

    def disconnect(self) -> None:
        """Disconnects from the AttoDry2100 using the close method from the Device class."""
        self.device.close()

    def is_connected(self) -> bool:
        """Checks if the AttoDry2100 is connected using the is_open attribute from the Device class.

        Returns:
            bool: True if the AttoDry2100 is connected, False otherwise.
        """
        return self.device.is_open
    
    # Device interface methods

    def _request(self, method: str, params: dict | None = None) -> dict:
        """Sends a request to the AttoDry2100 using the sendRequest method from the Device class.

        Args:
            method (str): The method to be called on the AttoDry2100.
            params (dict, optional): The parameters to be sent with the request. Defaults to None.

        Returns:
            dict: The response from the AttoDry2100.
        """
        return self.device.request(method, params)


    # System information methods

    def get_device_type(self) -> str:
        """Gets the device type from the AttoDry2100.

        Returns:
            str: The device type of the AttoDry2100.
        """
        return self.device.system.getDeviceType()

    def get_last_error(self) -> tuple[int, str, str, str, int]:
        """Gets the last error from the AttoDry2100.

        Returns:
            list: A list containing the error code, error message, error source, and error timestamp.
        """
        return self.device.system.getLastError()
    
    def get_features(self) -> list[str]:
        """Gets the features of the AttoDry2100.

        Returns:
            list: A list of features supported by the AttoDry2100.
        """
        return self.device.system.getFeatures()

    def get_device_name(self) -> str:
        """Gets the device name from the AttoDry2100.

        Returns:
            str: The device name of the AttoDry2100.
        """
        return self.device.system_service.getDeviceName()

    def error_number_to_string(self, language: int, err_nbr: int) -> str:
        """Converts an error number to a string using the errorNumberToString method from the System class.

        Args:
            language (int): The language code for the error message.
            err_nbr (int): The error number to be converted.

        Returns:
            str: The error message corresponding to the error number.
        """
        return self.device.system_service.errorNumberToString(language, errNbr=err_nbr)

    def get_hostname(self) -> str:
        """Gets the hostname of the AttoDry2100 using the getHostname method from the System class.

        Returns:
            str: The hostname of the AttoDry2100.
        """
        return self.device.system_service.getHostname()

    def get_mac_address(self) -> str:
        """Gets the MAC address of the AttoDry2100 using the getMacAddress method from the System class.

        Returns:
            str: The MAC address of the AttoDry2100.
        """
        return self.device.system_service.getMacAddress()

    
    # Action methods

    def get_current_command(self) -> str:
        """Gets the current command from the AttoDry2100 using the getCurrentCommand method from the Action class.

        Returns:
            str: The current command being executed by the AttoDry2100.
        """
        return self.device.action.getCurrentCommand()

    def get_current_command_status(self) -> str:
        """Gets the current command status from the AttoDry2100 using the getCurrentCommandStatus method from the Action class.

        Returns:
            str: The status of the current command being executed by the AttoDry2100.
        """
        return self.device.action.getCurrentCommandStatus()

    def get_go_to_base_ramp_rate_setting(self) -> float:
        """Gets the go to base ramp rate setting from the AttoDry2100 using the getGoToBaseRampRateSetting method from the Action class.

        Returns:
            float: The go to base ramp rate setting of the AttoDry2100 in mW/s.
        """
        return self.device.action.getGoToBaseRampRateSetting()

    def get_sample_exchange_ramp_rate_setting(self) -> float:
        """Gets the sample exchange ramp rate setting from the AttoDry2100 using the getSampleExchangeRampRateSetting method from the Action class.

        Returns:
            float: The sample exchange ramp rate setting of the AttoDry2100 in mW/s.
        """
        return self.device.action.getSampleExchangeRampRateSetting()

    def get_wait_for_event(self) -> str:
        """Gets the wait for event from the AttoDry2100 using the getWaitForEvent method from the Action class.

        Returns:
            str: The event that the AttoDry2100 is waiting for.
        """
        return self.device.action.getWaitForEvent()
    
    
    # Pressure methods

    def get_cryo_in_pressure(self) -> float:
        """Gets the cryo-in pressure from the AttoDry2100.

        Returns:
            float: The cryo-in pressure in mbar.
        """
        return self.device.pressures.getCryoInPressure()
    
    def get_cryo_out_pressure(self) -> float:
        """Gets the cryo-out pressure from the AttoDry2100.

        Returns:
            float: The cryo-out pressure in mbar.
        """
        return self.device.pressures.getCryoOutPressure()

    def get_dump_pressure(self) -> float:
        """Gets the dump pressure from the AttoDry2100.

        Returns:
            float: The dump pressure in mbar.
        """
        return self.device.pressures.getDumpPressure()

    
    # VTI methods

    def get_vti_temperature(self) -> float:
        """Gets the VTI temperature from the AttoDry2100.

        Returns:
            float: The VTI temperature in K.
        """
        return self.device.vti.getTemperature()

    def get_vti_heater_heating_mode(self) -> int:
        """Gets the VTI heater heating mode from the AttoDry2100.

        Returns:
            int: The VTI heater heating mode of the AttoDry2100.
        """
        return self.device.vti.getHeaterHeatingMode()

    def get_vti_heater_power(self) -> float:
        """Gets the VTI heater power from the AttoDry2100.

        Returns:
            float: The VTI heater power of the AttoDry2100 in mW.
        """
        return self.device.vti.getHeaterPower()

    def get_vti_heater_ramp_data(self) -> tuple[bool, float]:
        """Gets the VTI heater ramp data from the AttoDry2100.

        Returns:
            tuple: A tuple containing the time and power data for the VTI heater ramp.
        """
        return self.device.vti.getHeaterRampData()

    def get_vti_heater_status(self) -> int:
        """Gets the VTI heater status from the AttoDry2100.

        Returns:
            int: The VTI heater status of the AttoDry2100.
        """
        return self.device.vti.getHeaterStatus()

    def get_vti_set_point(self) -> float:
        """Gets the VTI set point from the AttoDry2100.

        Returns:
            float: The VTI set point of the AttoDry2100 in mW.
        """
        return self.device.vti.getSetPoint()

    def get_vti_temp_control_status(self) -> bool:
        """Gets the VTI temperature control status from the AttoDry2100.

        Returns:
            bool: True if the VTI temperature control is active, False otherwise.
        """
        return self.device.vti.getTempControlStatus()

    
    # Condenser methods

    def get_condenser_temperature(self) -> float:
        """Gets the condenser temperature from the AttoDry2100.

        Returns:
            float: The condenser temperature in K.
        """
        return self.device.condenser.getTemperature()

    def get_condenser_heater_heating_mode(self) -> int:
        """Gets the condenser heater heating mode from the AttoDry2100.

        Returns:
            int: The condenser heater heating mode of the AttoDry2100.
        """
        return self.device.condenser.getHeaterHeatingMode()

    def get_condenser_heater_power(self) -> float:
        """Gets the condenser heater power from the AttoDry2100.

        Returns:
            float: The condenser heater power of the AttoDry2100 in mW.
        """
        return self.device.condenser.getHeaterPower()

    def get_condenser_heater_ramp_data(self) -> tuple[bool, float]:
        """Gets the condenser heater ramp data from the AttoDry2100.

        Returns:
            tuple: A tuple containing the time and power data for the condenser heater ramp.
        """
        return self.device.condenser.getHeaterRampData()

    def get_condenser_heater_status(self) -> int:
        """Gets the condenser heater status from the AttoDry2100.

        Returns:
            int: The condenser heater status of the AttoDry2100.
        """
        return self.device.condenser.getHeaterStatus()


    # Dump in valve methods

    def get_dump_in_valve_status(self) -> bool:
        """Gets the dump in valve status from the AttoDry2100.

        Returns:
            bool: True if the dump in valve is open, False if it is closed.
        """
        return self.device.dumpInValve.getStatus()

    # Dump out valve methods

    def get_dump_out_valve_status(self) -> bool:
        """Gets the dump out valve status from the AttoDry2100.

        Returns:
            bool: True if the dump out valve is open, False if it is closed.
        """
        return self.device.dumpOutValve.getStatus()

    
    # Scroll pump methods

    def get_scroll_pump_status(self) -> bool:
        """Gets the scroll pump status from the AttoDry2100.

        Returns:
            bool: True if the scroll pump is running, False if it is stopped.
        """
        return self.device.scrollPump.getStatus()

    def get_scroll_pump_frequency(self) -> float:
        """Gets the scroll pump frequency from the AttoDry2100.

        Returns:
            float: The scroll pump frequency in Hz.
        """
        return self.device.scrollPump.getFrequency()

    
    # Cryo in valve methods

    def get_cryo_in_valve_status(self) -> bool:
        """Gets the cryo in valve status from the AttoDry2100.

        Returns:
            bool: True if the cryo in valve is open, False if it is closed.
        """
        return self.device.cryoInValve.getStatus()

    # Cryo out valve methods

    def get_cryo_out_valve_status(self) -> bool:
        """Gets the cryo out valve status from the AttoDry2100.

        Returns:
            bool: True if the cryo out valve is open, False if it is closed.
        """
        return self.device.cryoOutValve.getStatus()

    
    # Sample information methods

    def get_heater_heating_mode(self) -> int:
        """Gets the heater heating mode from the AttoDry2100.

        Returns:
            int: The heater heating mode of the AttoDry2100.
        """
        return self.device.sample.getHeaterHeatingMode()

    def get_sample_heater_power(self) -> float:
        """Gets the sample heater power from the AttoDry2100.

        Returns:
            float: The sample heater power of the AttoDry2100 in mW.
        """
        return self.device.sample.getHeaterPower()

    def get_sample_heater_ramp_data(self) -> tuple[bool, float]:
        """Gets the sample heater ramp data from the AttoDry2100.

        Returns:
            tuple: A tuple containing the time and power data for the sample heater ramp.
        """
        return self.device.sample.getHeaterRampData()

    def get_sample_heater_status(self) -> int:
        """Gets the sample heater status from the AttoDry2100.

        Returns:
            int: The sample heater status of the AttoDry2100.
        """
        return self.device.sample.getHeaterStatus()

    def get_sample_heater_max_power(self) -> float:
        """Gets the sample heater maximum power from the AttoDry2100.

        Returns:
            float: The sample heater maximum power of the AttoDry2100 in mW.
        """
        return self.device.sample.getMaxPower()

    def get_sample_heater_pid(self) -> tuple[float, float, float]:
        """Gets the sample heater PID parameters from the AttoDry2100.

        Returns:
            tuple: A tuple containing the P, I, and D parameters for the sample heater PID controller.
        """
        return self.device.sample.getPID()

    def get_sample_heater_ramp_control_status(self) -> bool:
        """Gets the sample heater ramp control status from the AttoDry2100.

        Returns:
            bool: True if the sample heater ramp control is active, False otherwise.
        """
        return self.device.sample.getRampControlStatus()

    def get_sample_ramp_rate(self) -> float:
        """Gets the sample ramp rate from the AttoDry2100.

        Returns:
            float: The sample ramp rate of the AttoDry2100 in mW/s.
        """
        return self.device.sample.getRampRate()

    def get_sample_setpoint(self) -> float:
        """Gets the sample setpoint from the AttoDry2100.

        Returns:
            float: The sample setpoint of the AttoDry2100 in mW.
        """
        return self.device.sample.getSetPoint()

    def get_temp_control_status(self) -> bool:
        """Gets the temperature control status from the AttoDry2100.

        Returns:
            bool: True if the temperature control is active, False otherwise.
        """
        return self.device.sample.getTempControlStatus()

    def get_sample_temperature(self) -> float:
        """Gets the sample temperature from the AttoDry2100.

        Returns:
            float: The sample temperature of the AttoDry2100 in K.
        """
        return self.device.sample.getTemperature()


    # Temperature board information methods

    def get_tboard_temperature(self, channel_number: int) -> float:
        """Gets the temperature from the specified channel of the temperature board.

        Args:
            channel_number (int): The channel number of the temperature board.

        Returns:
            float: The temperature of the specified channel in K.
        """
        return self.device.tboard.getTemperature(channelNumber=channel_number)

    
    # Stage 40K methods

    def get_stage_40k_temp_control_status(self) -> bool:
        """Gets the stage 40K temperature control status from the AttoDry2100.

        Returns:
            bool: True if the stage 40K temperature control is active, False otherwise.
        """
        return self.device.stage40k.getTempControlStatus()

    def get_stage_40k_temperature(self) -> float:
        """Gets the stage 40K temperature from the AttoDry2100.

        Returns:
            float: The stage 40K temperature of the AttoDry2100 in K.
        """
        return self.device.stage40k.getTemperature()

    def get_stage_40k_set_point(self) -> float:
        """Gets the stage 40K set point from the AttoDry2100.

        Returns:
            float: The stage 40K set point of the AttoDry2100 in K.
        """
        return self.device.stage40k.getSetPoint()

    def get_stage_40k_heater_power(self) -> float:
        """Gets the stage 40K heater power from the AttoDry2100.

        Returns:
            float: The stage 40K heater power of the AttoDry2100 in mW.
        """
        return self.device.stage40k.getHeaterPower()


    # Magnet methods

    def get_magnet_field(self, channel_number: int) -> float:
        """Gets the magnetic field from the specified channel of the magnet.

        Args:
            channel_number (int): The channel number of the magnet.

        Returns:
            float: The magnetic field of the specified channel in Tesla.
        """
        return self.device.magnet.getH(channel=channel_number)

    def get_magnet_set_point_channel(self, channel_number: int) -> float:
        """Gets the magnet set point from the specified channel of the magnet.

        Args:
            channel_number (int): The channel number of the magnet.

        Returns:
            float: The magnet set point of the specified channel in Tesla.
        """
        return self.device.magnet.getHSetPoint(channel=channel_number)

    def get_magnet_set_point(self) -> tuple[float, float, float]:
        """Gets the magnet set point 3D of the magnet.

        Args:
            channel_number (int): The channel number of the magnet.

        Returns:
            float: The magnet set point 3D of the specified channel in Tesla.
        """
        return self.device.magnet.getHSetPoint3D()

    def get_magnet_state(self, channel_number: int) -> str:
        """Gets the magnet state from the AttoDry2100.

        Args:
            channel_number (int): The channel number of the magnet.

        Returns:
            str: The magnet state of the AttoDry2100.
        """
        return self.device.magnet.getHState(channel=channel_number)

    def get_magnet_is_in_quench_state(self) -> bool:
        """Gets the magnet quench state from the AttoDry2100.

        Returns:
            bool: True if the magnet is in a quench state, False otherwise.
        """
        return self.device.magnet.getIsInQuenchState()

    def get_magnet_ramp_rate(self, channel_number: int, index: int) -> tuple[float, float]:
        """Gets the magnet ramp rate from the AttoDry2100.

        Args:
            channel_number (int): The channel number of the magnet.
            index (int): The index of the ramp rate to retrieve.

        Returns:
            float: The magnet ramp rate of the AttoDry2100 in Tesla/s.
            float: The magnet ramp rate of the AttoDry2100 in Tesla/s.
        """
        return self.device.magnet.getRampRate(channel=channel_number, index=index)

    def get_magnet_temperature(self) -> float:
        """Gets the magnet temperature from the AttoDry2100.

        Returns:
            float: The magnet temperature of the AttoDry2100 in K.
        """
        return self.device.magnet.getTemperature()

    def get_magnet_voltage(self, channel_number: int) -> float:
        """Gets the magnet voltage from the AttoDry2100.

        Args:
            channel_number (int): The channel number of the magnet.

        Returns:
            float: The magnet voltage of the AttoDry2100 in V.
        """
        return self.device.magnet.getVolt(channel=channel_number)


class AttoDry2100_Magnet_Driver(Connectable):
    """Driver for interfacing with the magnet of the AttoDry2100. Inherits from Connectable and Device.

    Args:
        Connectable (Abstract): abstract class for devices that can be connected to and disconnected from.
        Device (Device): device class from the atto_device library that provides methods for communicating with the AttoDry2100.
    """
    def __init__(self, ip_address: str):
        self.ip_address = ip_address

        self.device = Device(address=self.ip_address)

    # Connectable interface methods
    def connect(self) -> None:
        """Connects to the AttoDry2100 using the connect method from the Device class."""
        self.device.connect()

    def disconnect(self) -> None:
        """Disconnects from the AttoDry2100 using the close method from the Device class."""
        self.device.close()

    def is_connected(self) -> bool:
        """Checks if the AttoDry2100 is connected using the is_open attribute from the Device class.

        Returns:
            bool: True if the AttoDry2100 is connected, False otherwise.
        """
        return self.device.is_open

        # Magnet methods

    def get_magnet_field(self, channel_number: int) -> float:
        """Gets the magnetic field from the specified channel of the magnet.

        Args:
            channel_number (int): The channel number of the magnet.

        Returns:
            float: The magnetic field of the specified channel in Tesla.
        """
        return self.device.magnet.getH(channel=channel_number)

    def get_magnet_set_point_channel(self, channel_number: int) -> float:
        """Gets the magnet set point from the specified channel of the magnet.

        Args:
            channel_number (int): The channel number of the magnet.

        Returns:
            float: The magnet set point of the specified channel in Tesla.
        """
        return self.device.magnet.getHSetPoint(channel=channel_number)

    def get_magnet_set_point(self) -> tuple[float, float, float]:
        """Gets the magnet set point 3D of the magnet.

        Args:
            channel_number (int): The channel number of the magnet.

        Returns:
            float: The magnet set point 3D of the specified channel in Tesla.
        """
        return self.device.magnet.getHSetPoint3D()

    def get_magnet_state(self, channel_number: int) -> str:
        """Gets the magnet state from the AttoDry2100.

        Args:
            channel_number (int): The channel number of the magnet.

        Returns:
            str: The magnet state of the AttoDry2100.
        """
        return self.device.magnet.getHState(channel=channel_number)

    def get_magnet_is_in_quench_state(self) -> bool:
        """Gets the magnet quench state from the AttoDry2100.

        Returns:
            bool: True if the magnet is in a quench state, False otherwise.
        """
        return self.device.magnet.getIsInQuenchState()

    def get_magnet_ramp_rate(self, channel_number: int, index: int) -> tuple[float, float]:
        """Gets the magnet ramp rate from the AttoDry2100.

        Args:
            channel_number (int): The channel number of the magnet.
            index (int): The index of the ramp rate to retrieve.

        Returns:
            float: The magnet ramp rate of the AttoDry2100 in Tesla/s.
            float: The magnet ramp rate of the AttoDry2100 in Tesla/s.
        """
        return self.device.magnet.getRampRate(channel=channel_number, index=index)

    def get_magnet_temperature(self) -> float:
        """Gets the magnet temperature from the AttoDry2100.

        Returns:
            float: The magnet temperature of the AttoDry2100 in K.
        """
        return self.device.magnet.getTemperature()

    def get_magnet_voltage(self, channel_number: int) -> float:
        """Gets the magnet voltage from the AttoDry2100.

        Args:
            channel_number (int): The channel number of the magnet.

        Returns:
            float: The magnet voltage of the AttoDry2100 in V.
        """
        return self.device.magnet.getVolt(channel=channel_number)

