from ..Abstract.Connectable import Connectable
from atto_device.CRYO800.attoDry800 import Device


class AttoDry800_Driver(Connectable, Device):
    """Driver for interfacing with the AttoDry800. Inherits from Connectable and Device.

    Args:
        Connectable (Abstract): abstract class for devices that can be connected to and disconnected from.
        Device (Device): device class from the atto_device library that provides methods for communicating with the AttoDry800.
    """
    def __init__(self, address: str):
        super().__init__(address)

    # Connectable interface methods

    def connect(self) -> None:
        """Connects to the AttoDry800 using the connect method from the Device class."""
        super().connect()

    def disconnect(self) -> None:
        """Disconnects from the AttoDry800 using the close method from the Device class."""
        self.close()

    def is_connected(self) -> bool:
        """Checks if the AttoDry800 is connected using the is_open attribute from the Device class.

        Returns:
            bool: True if the AttoDry800 is connected, False otherwise.
        """
        return self.is_open
    
    # Device interface methods

    def _request(self, method: str, params: dict | None = None) -> dict:
        """Sends a request to the AttoDry800 using the sendRequest method from the Device class.

        Args:
            method (str): The method to be called on the AttoDry800.
            params (dict, optional): The parameters to be sent with the request. Defaults to None.

        Returns:
            dict: The response from the AttoDry800.
        """
        return self.request(method, params)

    
    # Pressure methods

    def get_sample_space_pressure(self) -> float:
        """Gets the sample space pressure from the AttoDry800.

        Returns:
            float: The sample space pressure in mbar.
        """
        return self.pressures.getSampleSpacePressure()

    # System information methods

    def get_device_type(self) -> str:
        """Gets the device type from the AttoDry800.

        Returns:
            str: The device type of the AttoDry800.
        """
        return self.system.getDeviceType()

    def get_last_error(self) -> tuple[int, str, str, str, int]:
        """Gets the last error from the AttoDry800.

        Returns:
            list: A list containing the error code, error message, error source, and error timestamp.
        """
        return self.system.getLastError()
    
    def get_features(self) -> list[str]:
        """Gets the features of the AttoDry800.

        Returns:
            list: A list of features supported by the AttoDry800.
        """
        return self.system.getFeatures()

    def get_device_name(self) -> str:
        """Gets the device name from the AttoDry800.

        Returns:
            str: The device name of the AttoDry800.
        """
        return self.system_service.getDeviceName()

    def error_number_to_string(self, language: int, err_nbr: int) -> str:
        """Converts an error number to a string using the errorNumberToString method from the System class.

        Args:
            language (int): The language code for the error message.
            err_nbr (int): The error number to be converted.

        Returns:
            str: The error message corresponding to the error number.
        """
        return self.system_service.errorNumberToString(language, err_nbr)

    def get_hostname(self) -> str:
        """Gets the hostname of the AttoDry800 using the getHostname method from the System class.

        Returns:
            str: The hostname of the AttoDry800.
        """
        return self.system_service.getHostname()

    def get_mac_address(self) -> str:
        """Gets the MAC address of the AttoDry800 using the getMacAddress method from the System class.

        Returns:
            str: The MAC address of the AttoDry800.
        """
        return self.system_service.getMacAddress()

    # Action methods

    def get_current_command(self) -> str:
        """Gets the current command from the AttoDry800 using the getCurrentCommand method from the Action class.

        Returns:
            str: The current command being executed by the AttoDry800.
        """
        return self.action.getCurrentCommand()

    def get_current_command_status(self) -> str:
        """Gets the current command status from the AttoDry800 using the getCurrentCommandStatus method from the Action class.

        Returns:
            str: The status of the current command being executed by the AttoDry800.
        """
        return self.action.getCurrentCommandStatus()

    def get_go_to_base_ramp_rate_setting(self) -> float:
        """Gets the go to base ramp rate setting from the AttoDry800 using the getGoToBaseRampRateSetting method from the Action class.

        Returns:
            float: The go to base ramp rate setting of the AttoDry800 in mW/s.
        """
        return self.action.getGoToBaseRampRateSetting()

    def get_sample_exchange_pump_on_setting(self) -> bool:
        """Gets the sample exchange pump on setting from the AttoDry800 using the getSampleExchangePumpOnSetting method from the Action class.

        Returns:
            bool: True if the sample exchange pump is on, False otherwise.
        """
        return self.action.getSampleExchangePumpOnSetting()

    def get_sample_exchange_ramp_rate_setting(self) -> float:
        """Gets the sample exchange ramp rate setting from the AttoDry800 using the getSampleExchangeRampRateSetting method from the Action class.

        Returns:
            float: The sample exchange ramp rate setting of the AttoDry800 in mW/s.
        """
        return self.action.getSampleExchangeRampRateSetting()

    def get_wait_for_event(self) -> str:
        """Gets the wait for event from the AttoDry800 using the getWaitForEvent method from the Action class.

        Returns:
            str: The event that the AttoDry800 is waiting for.
        """
        return self.action.getWaitForEvent()

    # Sample information methods

    def get_heater_heating_mode(self) -> int:
        """Gets the heater heating mode from the AttoDry800.

        Returns:
            int: The heater heating mode of the AttoDry800.
        """
        return self.sample.getHeaterHeatingMode()

    def get_heater_power(self) -> float:
        """Gets the heater power from the AttoDry800.

        Returns:
            float: The heater power of the AttoDry800 in mW.
        """
        return self.sample.getHeaterPower()

    def get_heater_ramp_data(self) -> tuple[bool, float]:
        """Gets the heater ramp data from the AttoDry800.

        Returns:
            tuple: A tuple containing the time and power data for the heater ramp.
        """
        return self.sample.getHeaterRampData()

    def get_heater_status(self) -> int:
        """Gets the heater status from the AttoDry800.

        Returns:
            int: The heater status of the AttoDry800.
        """
        return self.sample.getHeaterStatus()

    def get_heater_max_power(self) -> float:
        """Gets the heater maximum power from the AttoDry800.

        Returns:
            float: The heater maximum power of the AttoDry800 in mW.
        """
        return self.sample.getMaxPower()

    def get_heater_pid(self) -> tuple[float, float, float]:
        """Gets the heater PID parameters from the AttoDry800.

        Returns:
            tuple: A tuple containing the P, I, and D parameters for the heater PID controller.
        """
        return self.sample.getPID()

    def get_heater_ramp_control_status(self) -> bool:
        """Gets the heater ramp control status from the AttoDry800.

        Returns:
            bool: True if the heater ramp control is active, False otherwise.
        """
        return self.sample.getRampControlStatus()

    def get_sample_ramp_rate(self) -> float:
        """Gets the sample ramp rate from the AttoDry800.

        Returns:
            float: The sample ramp rate of the AttoDry800 in mW/s.
        """
        return self.sample.getRampRate()

    def get_sample_setpoint(self) -> float:
        """Gets the sample setpoint from the AttoDry800.

        Returns:
            float: The sample setpoint of the AttoDry800 in mW.
        """
        return self.sample.getSetPoint()

    def get_temp_control_status(self) -> bool:
        """Gets the temperature control status from the AttoDry800.

        Returns:
            bool: True if the temperature control is active, False otherwise.
        """
        return self.sample.getTempControlStatus()

    def get_sample_temperature(self) -> float:
        """Gets the sample temperature from the AttoDry800.

        Returns:
            float: The sample temperature of the AttoDry800 in K.
        """
        return self.sample.getTemperature()

    # Temperature board information methods

    def get_tboard_temperature(self, channel_number: int) -> float:
        """Gets the temperature from the specified channel of the temperature board.

        Args:
            channel_number (int): The channel number of the temperature board.

        Returns:
            float: The temperature of the specified channel in K.
        """
        return self.tboard.getTemperature(channel_number)
