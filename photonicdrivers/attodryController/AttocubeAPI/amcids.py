    
class Amcids():

    def __init__(self, device):
        self.device = device
        self.interface_name = "com.attocube.amc.amcids"
            
    def getLowerSoftLimit(self, axis):
        """
        Gets the lower boundary of the soft limit protection.
        This protection is needed if the IDS working range is smaller than the positioners travel range.
        It is no hard limit, so, it is possible to overshoot it!

        Parameters
        ----------
        axis: 
            Axis of the AMC to get the soft limit status from

        Returns
        -------
        limit: double
            Lower boundary in pm
        """
        response = self.device.request(self.interface_name + "." + "getLowerSoftLimit", [axis])
        self.device.handleError(response)
        return response[1]

    def getSoftLimitEnabled(self, axis):
        """
        Gets whether the soft limit protection is enabled.
        This protection is needed if the IDS working range is smaller than the positioners travel range.
        It is no hard limit, so, it is possible to overshoot it!

        Parameters
        ----------
        axis: 
            Axis of the AMC to get the soft limit status from

        Returns
        -------
        enabled: boolean
            True, if the soft limit should be enabled on this axis
        """
        response = self.device.request(self.interface_name + "." + "getSoftLimitEnabled", [axis])
        self.device.handleError(response)
        return response[1]

    def getSoftLimitReached(self, axis):
        """
        Gets whether the current position is out of the soft limit boundaries.
        This protection is needed if the IDS working range is smaller than the positioners travel range.
        It is no hard limit, so, it is possible to overshoot it!

        Parameters
        ----------
        axis: 
            Axis of the AMC to get the soft limit status from

        Returns
        -------
        enabled: boolean
            True, if the position is not within the boundaries
        """
        response = self.device.request(self.interface_name + "." + "getSoftLimitReached", [axis])
        self.device.handleError(response)
        return response[1]

    def getUpperSoftLimit(self, axis):
        """
        Gets the upper lower boundary of the soft limit protection.
        This protection is needed if the IDS working range is smaller than the positioners travel range.
        It is no hard limit, so, it is possible to overshoot it!

        Parameters
        ----------
        axis: 
            Axis of the AMC to get the soft limit status from

        Returns
        -------
        limit: double
            Upper boundary in pm
        """
        response = self.device.request(self.interface_name + "." + "getUpperSoftLimit", [axis])
        self.device.handleError(response)
        return response[1]

    def resetIdsAxis(self, axis):
        """
        Resets the position value to zero of a specific measurement axis.
        Use this for positioners with an IDS as sensor.
        This method does not work for NUM and RES sensors. Use com.attocube.amc.control.resetAxis instead.

        Parameters
        ----------
        axis: 
            Axis of the IDS to reset the position

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "resetIdsAxis", [axis])
        self.device.handleError(response)
        return 

    def setLowerSoftLimit(self, axis, limit):
        """
        Sets the lower boundary of the soft limit protection in pm.
        This protection is needed if the IDS working range is smaller than the positioners travel range.
        It is no hard limit, so, it is possible to overshoot it!

        Parameters
        ----------
        axis: 
            Axis of the AMC where the soft limit should be changed
        limit: 
            Lower boundary in pm

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setLowerSoftLimit", [axis, limit])
        self.device.handleError(response)
        return 

    def setSoftLimitEnabled(self, axis, enabled):
        """
        Enables/disables the soft limit protection.
        This protection is needed if the IDS working range is smaller than the positioners travel range.
        It is no hard limit, so, it is possible to overshoot it!

        Parameters
        ----------
        axis: 
            Axis of the AMC where the soft limit should be changed
        enabled: 
            True, if the soft limit should be enabled on this axis

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setSoftLimitEnabled", [axis, enabled])
        self.device.handleError(response)
        return 

    def setUpperSoftLimit(self, axis, limit):
        """
        Sets the upper boundary of the soft limit protection in pm.
        This protection is needed if the IDS working range is smaller than the positioners travel range.
        It is no hard limit, so, it is possible to overshoot it!

        Parameters
        ----------
        axis: 
            Axis of the AMC where the soft limit should be changed
        limit: 
            Upper boundary in pm

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setUpperSoftLimit", [axis, limit])
        self.device.handleError(response)
        return 

