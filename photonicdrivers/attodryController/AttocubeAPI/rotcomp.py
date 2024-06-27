    
class Rotcomp():

    def __init__(self, device):
        self.device = device
        self.interface_name = "com.attocube.amc.rotcomp"
            
    def getControlTargetRanges(self):
        """
        Checks if all three axis are in target range.

        Parameters
        ----------

        Returns
        -------
        in_target_range: boolean
            true all three axes are in target range, false at least one axis is not in target range
        """
        response = self.device.request(self.interface_name + "." + "getControlTargetRanges")
        self.device.handleError(response)
        return response[1]

    def getEnabled(self):
        """
        Gets the enabled status of the rotation compensation

        Parameters
        ----------

        Returns
        -------
        enabled: boolean
            true Rotation compensation is enabled, false Rotation compensation is disabled
        """
        response = self.device.request(self.interface_name + "." + "getEnabled")
        self.device.handleError(response)
        return response[1]

    def getLUT(self):
        """
        Gets the LUT file as JSON string

        Parameters
        ----------

        Returns
        -------
        lut: string
            JSON string of the LUT file for the rotation compensation
        """
        response = self.device.request(self.interface_name + "." + "getLUT")
        self.device.handleError(response)
        return response[1]

    def setEnabled(self, enabled):
        """
        Enables and disables the rotation compensation

        Parameters
        ----------
        enabled: 
            true Rotation compensation is enabled, false Rotation compensation is disabled

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setEnabled", [enabled])
        self.device.handleError(response)
        return 

    def setLUT(self, lut_string):
        """
        Sets the LUT file from a JSON string

        Parameters
        ----------
        lut_string: 
            JSON string of the LUT file for the rotation compensation

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setLUT", [lut_string])
        self.device.handleError(response)
        return 

    def updateOffsets(self, offset_axis0, offset_axis1, offset_axis2):
        """
        Updates the start offsets of the axes

        Parameters
        ----------
        offset_axis0: 
            Offset of axis 1 in [nm]
        offset_axis1: 
            Offset of axis 2 in [nm]
        offset_axis2: 
            Offset of axis 3 in [nm]

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "updateOffsets", [offset_axis0, offset_axis1, offset_axis2])
        self.device.handleError(response)
        return 

