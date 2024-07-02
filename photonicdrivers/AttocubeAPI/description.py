    
class Description():

    def __init__(self, device):
        self.device = device
        self.interface_name = "com.attocube.amc.description"
            
    def checkChassisNbr(self):
        """
        Get Chassis and Slot Number, only works when AMC is within a Rack

        Parameters
        ----------

        Returns
        -------
        slotNbr: slotNbr
        chassisNbr: chassisNbr
        """
        response = self.device.request(self.interface_name + "." + "checkChassisNbr")
        self.device.handleError(response)
        return response[1], response[2]

    def getDeviceType(self):
        """
        This function gets the device type based on its EEPROM configuration.

        Parameters
        ----------

        Returns
        -------
        devicetype: devicetype Device name (AMC100, AMC150, AMC300) with attached feature ( AMC100\\NUM, AMC100\\NUM\\PRO)
        """
        response = self.device.request(self.interface_name + "." + "getDeviceType")
        self.device.handleError(response)
        return response[1]

    def getFeaturesActivated(self):
        """
        Get the activated features and return as a string

        Parameters
        ----------

        Returns
        -------
        features: features activated on device concatenated by comma e.g. Closed loop Operation, Pro, Wireless Controller, IO
        """
        response = self.device.request(self.interface_name + "." + "getFeaturesActivated")
        self.device.handleError(response)
        return response[1]

    def getPositionersList(self):
        """
        This function reads the actor names that can be connected to the device.

        Parameters
        ----------

        Returns
        -------
        PositionersList: PositionersList
        """
        response = self.device.request(self.interface_name + "." + "getPositionersList")
        self.device.handleError(response)
        return response[1]

