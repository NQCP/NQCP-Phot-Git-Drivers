    
class Rtin():

    def __init__(self, device):
        self.device = device
        self.interface_name = "com.attocube.amc.rtin"
            
    def apply(self):
        """
        Apply all realtime input function

        Parameters
        ----------

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "apply")
        self.device.handleError(response)
        return 

    def discard(self):
        """
        Discard all values beting set and not yet applieds

        Parameters
        ----------

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "discard")
        self.device.handleError(response)
        return 

    def getControlAQuadBInResolution(self, axis):
        """
        This function gets the AQuadB input resolution for setpoint parameter.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        resolution: resolution ion nm
        """
        response = self.device.request(self.interface_name + "." + "getControlAQuadBInResolution", [axis])
        self.device.handleError(response)
        return response[1]

    def getControlMoveGPIO(self, axis):
        """
        This function gets the status for real time input on the selected axis in closed-loop mode.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        enable: enable boolean true: approach enabled , false: approach disabled
        """
        response = self.device.request(self.interface_name + "." + "getControlMoveGPIO", [axis])
        self.device.handleError(response)
        return response[1]

    def getGpioMode(self):
        """
        get the GPIO mode for Mic Mode feature

        Parameters
        ----------

        Returns
        -------
        gpio_mode: gpio_mode: 0: Standard GPIO 1: NSL-/Mic-Mode
        """
        response = self.device.request(self.interface_name + "." + "getGpioMode")
        self.device.handleError(response)
        return response[1]

    def getNslMux(self):
        """
        get the axis the NSL multiplexer is set to

        Parameters
        ----------

        Returns
        -------
        mux_mode: mux_mode  0: Off 1: Axis 1 2: Axis 2 3: Axis 3
        """
        response = self.device.request(self.interface_name + "." + "getNslMux")
        self.device.handleError(response)
        return response[1]

    def getRealTimeInChangePerPulse(self, axis):
        """
        This function gets the change per pulse for the selected axis under real time input in the closed-loop mode.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        resolution: resolution to be added in current pos in nm
        """
        response = self.device.request(self.interface_name + "." + "getRealTimeInChangePerPulse", [axis])
        self.device.handleError(response)
        return response[1]

    def getRealTimeInFeedbackLoopMode(self, axis):
        """
        Get if the realtime function must operate in close loop operation or open loop operation

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        mode: mode 0: open loop, 1 : close-loop
        """
        response = self.device.request(self.interface_name + "." + "getRealTimeInFeedbackLoopMode", [axis])
        self.device.handleError(response)
        return response[1]

    def getRealTimeInMode(self, axis):
        """
        This function sets or gets the real time input mode for the selected axis.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        mode: mode see `RT_IN_MODES`
        """
        response = self.device.request(self.interface_name + "." + "getRealTimeInMode", [axis])
        self.device.handleError(response)
        return response[1]

    def getRealTimeInStepsPerPulse(self, axis):
        """
        Get the change in step per pulse  of the realtime input when trigger and stepper mode is used

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        steps: steps number of steps to applied
        """
        response = self.device.request(self.interface_name + "." + "getRealTimeInStepsPerPulse", [axis])
        self.device.handleError(response)
        return response[1]

    def setControlAQuadBInResolution(self, axis, resolution):
        """
        This function sets the AQuadB input resolution for setpoint parameter.

        Parameters
        ----------
        axis:  [0|1|2]
        resolution:  ion nm

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setControlAQuadBInResolution", [axis, resolution])
        self.device.handleError(response)
        return 

    def setControlMoveGPIO(self, axis, enable):
        """
        This function sets the status for real time input on the selected axis in closed-loop mode.

        Parameters
        ----------
        axis:  [0|1|2]
        enable:  boolean true: eanble the approach , false: disable the approach

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setControlMoveGPIO", [axis, enable])
        self.device.handleError(response)
        return 

    def setGpioMode(self, gpio_mode):
        """
        set the GPIO mode for Mic Mode feature

        Parameters
        ----------
        gpio_mode:  [0|1]
              0: Standard GPIO
              1: NSL-/Mic-Mode

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setGpioMode", [gpio_mode])
        self.device.handleError(response)
        return 

    def setNslMux(self, mux_mode):
        """
        set the axis the NSL multiplexer is set to

        Parameters
        ----------
        mux_mode:  [0|1|2|3]
              0: Off
              1: Axis 1
              2: Axis 2
              3: Axis 3

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setNslMux", [mux_mode])
        self.device.handleError(response)
        return 

    def setRealTimeInChangePerPulse(self, axis, delta):
        """
        This function sets the change per pulse for the selected axis under real time input in the closed-loop mode.
            only used in closed loop operation

        Parameters
        ----------
        axis:  [0|1|2]
        delta:  to be added to current position in nm

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setRealTimeInChangePerPulse", [axis, delta])
        self.device.handleError(response)
        return 

    def setRealTimeInFeedbackLoopMode(self, axis, mode):
        """
        Set if the realtime function must operate in close loop operation or open loop operation

        Parameters
        ----------
        axis:  [0|1|2]
        mode:  0: open loop, 1 : close-loop

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setRealTimeInFeedbackLoopMode", [axis, mode])
        self.device.handleError(response)
        return 

    def setRealTimeInMode(self, axis, mode):
        """
        This function sets the real time input mode for the selected axis.

        Parameters
        ----------
        axis:  [0|1|2]
        mode:  see `RT_IN_MODES` @see realtime

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setRealTimeInMode", [axis, mode])
        self.device.handleError(response)
        return 

    def setRealTimeInStepsPerPulse(self, axis, steps):
        """
        Set the change in step per pulse  of the realtime input when trigger and stepper mode is used
            only used in open loop operation

        Parameters
        ----------
        axis:  [0|1|2]
        steps:  number of steps to applied

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setRealTimeInStepsPerPulse", [axis, steps])
        self.device.handleError(response)
        return 

