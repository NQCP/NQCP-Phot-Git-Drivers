    
class System_service():

    def __init__(self, device):
        self.device = device
        self.interface_name = "com.attocube.system"
            
    def apply(self):
        """
        Apply temporary system configuration

        Parameters
        ----------

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "apply")
        self.device.handleError(response)
        return 

    def errorNumberToRecommendation(self, language, errNbr):
        """
        Get a recommendation for the error code

        Parameters
        ----------
        language:  integer: Language code
        errNbr:   interger: Error code to translate

        Returns
        -------
        value_string1: string: Error recommendation (currently returning an int = 0 until we have recommendations)
        """
        response = self.device.request(self.interface_name + "." + "errorNumberToRecommendation", [language, errNbr])
        self.device.handleError(response)
        return response[1]

    def errorNumberToString(self, language, errNbr):
        """
        Get a description of an error code

        Parameters
        ----------
        language:  integer: Language code 0 for the error name, 1 for a more user friendly error message
        errNbr:   interger: Error code to translate

        Returns
        -------
        value_string1: string: Error description
        """
        response = self.device.request(self.interface_name + "." + "errorNumberToString", [language, errNbr])
        return response[1]

    def factoryReset(self):
        """
        Turns on the factory reset flag. To perform the factory reset, a reboot is necessary afterwards. All settings will be set to default and the IDS will be configured as DHCP server.

        Parameters
        ----------

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "factoryReset")
        self.device.handleError(response)
        return 

    def getDeviceName(self):
        """
        Get the actual device name

        Parameters
        ----------

        Returns
        -------
        value_string1: string: actual device name
        """
        response = self.device.request(self.interface_name + "." + "getDeviceName")
        self.device.handleError(response)
        return response[1]

    def getFirmwareVersion(self):
        """
        Get the firmware version of the system

        Parameters
        ----------

        Returns
        -------
        value_string1: string: The firmware version
        """
        response = self.device.request(self.interface_name + "." + "getFirmwareVersion")
        self.device.handleError(response)
        return response[1]

    def getFluxCode(self):
        """
        Get the flux code of the system

        Parameters
        ----------

        Returns
        -------
        value_string1: string: flux code
        """
        response = self.device.request(self.interface_name + "." + "getFluxCode")
        self.device.handleError(response)
        return response[1]

    def getHostname(self):
        """
        Return device hostname

        Parameters
        ----------

        Returns
        -------
        available: available
        """
        response = self.device.request(self.interface_name + "." + "getHostname")
        self.device.handleError(response)
        return response[1]

    def getMacAddress(self):
        """
        Get the mac address of the system

        Parameters
        ----------

        Returns
        -------
        value_string1: string: Mac address of the system
        """
        response = self.device.request(self.interface_name + "." + "getMacAddress")
        self.device.handleError(response)
        return response[1]

    def getSerialNumber(self):
        """
        Get the serial number of the system

        Parameters
        ----------

        Returns
        -------
        value_string1: string: Serial number
        """
        response = self.device.request(self.interface_name + "." + "getSerialNumber")
        self.device.handleError(response)
        return response[1]

    def rebootSystem(self):
        """
        Reboot the system

        Parameters
        ----------

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "rebootSystem")
        self.device.handleError(response)
        return 

    def setDeviceName(self, name):
        """
        Set custom name for the device

        Parameters
        ----------
        name:  string: device name

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setDeviceName", [name])
        self.device.handleError(response)
        return 

    def setTime(self, day, month, year, hour, minute, second):
        """
        Set system time manually

        Parameters
        ----------
        day:  integer: Day (1-31)
        month:  integer: Day (1-12)
        year:  integer: Day (eg. 2021)
        hour:  integer: Day (0-23)
        minute:  integer: Day (0-59)
        second:  integer: Day (0-59)

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setTime", [day, month, year, hour, minute, second])
        self.device.handleError(response)
        return 

    def softReset(self):
        """
        Performs a soft reset (Reset without deleting the network settings). Please reboot the device directly afterwards.

        Parameters
        ----------

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "softReset")
        self.device.handleError(response)
        return 

    def updateTimeFromInternet(self):
        """
        Update system time by querying attocube.com

        Parameters
        ----------

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "updateTimeFromInternet")
        self.device.handleError(response)
        return 

