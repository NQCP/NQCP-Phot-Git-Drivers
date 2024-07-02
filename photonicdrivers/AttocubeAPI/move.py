    
class Move():

    def __init__(self, device):
        self.device = device
        self.interface_name = "com.attocube.amc.move"
            
    def getControlContinuousBkwd(self, axis):
        """
        This function gets the axis’ movement status in backward direction.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        enabled: enabled true if movement backward is active , false otherwise
        """
        response = self.device.request(self.interface_name + "." + "getControlContinuousBkwd", [axis])
        self.device.handleError(response)
        return response[1]

    def getControlContinuousFwd(self, axis):
        """
        This function gets the axis’ movement status in positive direction.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        enabled: enabled true if movement Fwd is active, false otherwise
        """
        response = self.device.request(self.interface_name + "." + "getControlContinuousFwd", [axis])
        self.device.handleError(response)
        return response[1]

    def getControlEotOutputDeactive(self, axis):
        """
        This function gets the output applied to the selected axis on the end of travel. /PRO feature.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        enabled: enabled If true, the output of the axis will be deactivated on positive EOT detection.
        """
        response = self.device.request(self.interface_name + "." + "getControlEotOutputDeactive", [axis])
        self.device.handleError(response)
        return response[1]

    def getControlTargetPosition(self, axis):
        """
        This function gets the target position for the movement on the selected axis.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        position: position defined in nm for goniometer an rotator type actors it is µ°.
        """
        response = self.device.request(self.interface_name + "." + "getControlTargetPosition", [axis])
        self.device.handleError(response)
        return response[1]

    def getGroundAxis(self, axis):
        """
        Checks if the axis piezo drive is actively grounded
            only in AMC300

        Parameters
        ----------
        axis:  montion controler axis [0|1|2]

        Returns
        -------
        grounded: grounded true or false
        """
        response = self.device.request(self.interface_name + "." + "getGroundAxis", [axis])
        self.device.handleError(response)
        return response[1]

    def getGroundAxisAutoOnTarget(self, axis):
        """
        Pull axis piezo drive to GND if positioner is in ground target range
            only in AMC300

        Parameters
        ----------
        axis:  montion controler axis [0|1|2]

        Returns
        -------
        value: value true or false
        """
        response = self.device.request(self.interface_name + "." + "getGroundAxisAutoOnTarget", [axis])
        self.device.handleError(response)
        return response[1]

    def getGroundTargetRange(self, axis):
        """
        Retrieves the range around the target position in which the auto grounding becomes active.
            only in AMC300

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        targetrange: targetrange in nm
        """
        response = self.device.request(self.interface_name + "." + "getGroundTargetRange", [axis])
        self.device.handleError(response)
        return response[1]

    def getNSteps(self, axis):
        """
        This function gets the number of Steps in desired direction.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        nbrstep: nbrstep
        """
        response = self.device.request(self.interface_name + "." + "getNSteps", [axis])
        self.device.handleError(response)
        return response[1]

    def getPosition(self, axis):
        """
        This function gets the current position of the positioner on the selected axis.
             The axis on the web application are indexed from 1 to 3

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        position: position defined in nm for goniometer an rotator type actors it is µ°.
        """
        response = self.device.request(self.interface_name + "." + "getPosition", [axis])
        self.device.handleError(response)
        return response[1]

    def moveReference(self, axis):
        """
        This function starts an approach to the reference position. A running motion command is aborted; closed loop moving is switched on. Requires a valid reference position.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "moveReference", [axis])
        self.device.handleError(response)
        return 

    def performNSteps(self, axis, backward):
        """
        Perform the OL command for N steps

        Parameters
        ----------
        axis:  [0|1|2]
        backward:  Selects the desired direction. False triggers a forward step, true a backward step

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "performNSteps", [axis, backward])
        self.device.handleError(response)
        return 

    def setControlContinuousBkwd(self, axis, enable):
        """
        This function sets a continuous movement on the selected axis in backward direction.

        Parameters
        ----------
        axis:  [0|1|2]
        enable:  If enabled a present movement in the opposite direction is stopped. The parameter "false" stops all movement of the axis regardless its direction

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setControlContinuousBkwd", [axis, enable])
        self.device.handleError(response)
        return 

    def setControlContinuousFwd(self, axis, enable):
        """
        This function sets a continuous movement on the selected axis in positive direction.

        Parameters
        ----------
        axis:  [0|1|2]
        enable:  If enabled a present movement in the opposite direction is stopped. The parameter "false" stops all movement of the axis regardless its direction.

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setControlContinuousFwd", [axis, enable])
        self.device.handleError(response)
        return 

    def setControlEotOutputDeactive(self, axis, enable):
        """
        This function sets the output applied to the selected axis on the end of travel.

        Parameters
        ----------
        axis:  [0|1|2]
        enable:  if enabled, the output of the axis will be deactivated on positive EOT detection.

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setControlEotOutputDeactive", [axis, enable])
        self.device.handleError(response)
        return 

    def setControlTargetPosition(self, axis, target):
        """
        This function sets the target position for the movement on the selected axis.
            careful: the maximum positon in nm is 2**47/1000

        Parameters
        ----------
        axis:  [0|1|2]
        target:  absolute position : For linear type actors the position is defined in nm for goniometer an rotator type actors it is µ°.

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setControlTargetPosition", [axis, target])
        self.device.handleError(response)
        return 

    def setGroundAxis(self, axis, enabled):
        """
        Pull axis piezo drive to GND actively
            only in AMC300
            this is used in MIC-Mode

        Parameters
        ----------
        axis:  motion controler axis [0|1|2]
        enabled:  true or false

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setGroundAxis", [axis, enabled])
        self.device.handleError(response)
        return 

    def setGroundAxisAutoOnTarget(self, axis, enabled):
        """
        Pull axis piezo drive to GND actively if positioner is in ground target range
            only in AMC300
            this is used in MIC-Mode

        Parameters
        ----------
        axis:  montion controler axis [0|1|2]
        enabled:  true or false

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setGroundAxisAutoOnTarget", [axis, enabled])
        self.device.handleError(response)
        return 

    def setGroundTargetRange(self, axis, range):
        """
        Set  the range around the target position in which the auto grounding becomes active.
            only in AMC300

        Parameters
        ----------
        axis:  [0|1|2]
        range:  in nm

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setGroundTargetRange", [axis, range])
        self.device.handleError(response)
        return 

    def setNSteps(self, axis, backward, step):
        """
        This function triggers n steps on the selected axis in desired direction. /PRO feature.

        Parameters
        ----------
        axis:  [0|1|2]
        backward:  Selects the desired direction. False triggers a forward step, true a backward step
        step:  number of step

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setNSteps", [axis, backward, step])
        self.device.handleError(response)
        return 

    def setSingleStep(self, axis, backward):
        """
        This function triggers one step on the selected axis in desired direction.

        Parameters
        ----------
        axis:  [0|1|2]
        backward:  Selects the desired direction. False triggers a forward step, true a backward step

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setSingleStep", [axis, backward])
        self.device.handleError(response)
        return 

    def writeNSteps(self, axis, step):
        """
        Sets the number of steps to perform on stepwise movement. /PRO feature.

        Parameters
        ----------
        axis:  [0|1|2]
        step:  number of step

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "writeNSteps", [axis, step])
        self.device.handleError(response)
        return 

