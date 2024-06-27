    
class Control():

    def __init__(self, device):
        self.device = device
        self.interface_name = "com.attocube.amc.control"
            
    def MultiAxisPositioning(self, set1, set2, set3, target1, target2, target3):
        """
        Simultaneously set 3 axes positions
            and get positions to minimize network latency

        Parameters
        ----------
        set1:  axis1 otherwise pos1 target is ignored
        set2:  axis2 otherwise pos2 target is ignored
        set3:  axis3 otherwise pos3 target is ignored
        target1:  target position of axis 1
        target2:  target position of axis 2
        target3:  target position of axis 3

        Returns
        -------
        ref1: ref1 Status of axis 1
        ref2: ref2 Status of axis 2
        ref3: ref3 Status of axis 3
        refpos1: refpos1 reference Position of axis 1
        refpos2: refpos2 reference Position of axis 2
        refpos3: refpos3 reference Position of axis 3
        pos1: pos1 position of axis 1
        pos2: pos2 position of axis 2
        pos3: pos3 position of axis 3
        """
        response = self.device.request(self.interface_name + "." + "MultiAxisPositioning", [set1, set2, set3, target1, target2, target3])
        self.device.handleError(response)
        return response[1], response[2], response[3], response[4], response[5], response[6], response[7], response[8], response[9]

    def getActorName(self, axis):
        """
        This function gets the name of the positioner of the selected axis.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        actor_name: actor_name
        """
        response = self.device.request(self.interface_name + "." + "getActorName", [axis])
        self.device.handleError(response)
        return response[1]

    def getActorParametersActorName(self, axis):
        """
        Control the actors parameter: actor name

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        actorname: actorname
        """
        response = self.device.request(self.interface_name + "." + "getActorParametersActorName", [axis])
        self.device.handleError(response)
        return response[1]

    def getActorSensitivity(self, axis):
        """
        Get the setting for the actor parameter sensitivity

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        sensitivity: sensitivity
        """
        response = self.device.request(self.interface_name + "." + "getActorSensitivity", [axis])
        self.device.handleError(response)
        return response[1]

    def getActorType(self, axis):
        """
        This function gets the type of the positioner of the selected axis.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        actor_type: actor_type  0: linear, 1: rotator, 2: goniometer
        """
        response = self.device.request(self.interface_name + "." + "getActorType", [axis])
        self.device.handleError(response)
        return response[1]

    def getAutoMeasure(self, axis):
        """
        This function returns if the automeasurement on axis enable is enabled

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        enable: enable true: enable automeasurement, false: disable automeasurement
        """
        response = self.device.request(self.interface_name + "." + "getAutoMeasure", [axis])
        self.device.handleError(response)
        return response[1]

    def getControlAmplitude(self, axis):
        """
        This function gets the amplitude of the actuator signal of the selected axis.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        amplitude: amplitude in mV
        """
        response = self.device.request(self.interface_name + "." + "getControlAmplitude", [axis])
        self.device.handleError(response)
        return response[1]

    def getControlAutoReset(self, axis):
        """
        This function resets the position every time the reference position is detected.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        enabled: enabled boolean
        """
        response = self.device.request(self.interface_name + "." + "getControlAutoReset", [axis])
        self.device.handleError(response)
        return response[1]

    def getControlFixOutputVoltage(self, axis):
        """
        This function gets the DC level output of the selected axis.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        amplitude_mv: amplitude_mv in mV
        """
        response = self.device.request(self.interface_name + "." + "getControlFixOutputVoltage", [axis])
        self.device.handleError(response)
        return response[1]

    def getControlFrequency(self, axis):
        """
        This function gets the frequency of the actuator signal of the selected axis.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        frequency: frequency in mHz
        """
        response = self.device.request(self.interface_name + "." + "getControlFrequency", [axis])
        self.device.handleError(response)
        return response[1]

    def getControlMove(self, axis):
        """
        This function gets the approach of the selected axis’ positioner to the target position.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        enable: enable boolean true: closed loop control enabled, false: closed loop control disabled
        """
        response = self.device.request(self.interface_name + "." + "getControlMove", [axis])
        self.device.handleError(response)
        return response[1]

    def getControlOutput(self, axis):
        """
        This function gets the status of the output relays of the selected axis.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        enabled: enabled power status (true = enabled,false = disabled)
        """
        response = self.device.request(self.interface_name + "." + "getControlOutput", [axis])
        self.device.handleError(response)
        return response[1]

    def getControlReferenceAutoUpdate(self, axis):
        """
        This function gets the status of whether the reference position is updated when the reference mark is hit.
            When this function is disabled, the reference marking will be considered only the first time and after then ignored.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        enabled: enabled boolen
        """
        response = self.device.request(self.interface_name + "." + "getControlReferenceAutoUpdate", [axis])
        self.device.handleError(response)
        return response[1]

    def getControlTargetRange(self, axis):
        """
        This function gets the range around the target position in which the flag "In Target Range" becomes active.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        targetrange: targetrange in nm
        """
        response = self.device.request(self.interface_name + "." + "getControlTargetRange", [axis])
        self.device.handleError(response)
        return response[1]

    def getCrosstalkThreshold(self, axis):
        """
        This function gets the threshold range and slip phase time which is used while moving another axis

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        range: range in pm
        time: time after slip phase which is waited until the controller is acting again in microseconds
        """
        response = self.device.request(self.interface_name + "." + "getCrosstalkThreshold", [axis])
        self.device.handleError(response)
        return response[1], response[2]

    def getCurrentOutputVoltage(self, axis):
        """
        This function gets the current Voltage which is applied to the Piezo

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        amplitude: amplitude in mV
        """
        response = self.device.request(self.interface_name + "." + "getCurrentOutputVoltage", [axis])
        self.device.handleError(response)
        return response[1]

    def getExternalSensor(self, axis):
        """
        This function gets whether the sensor source of closed loop is IDS
            It is only available when the feature AMC/IDS closed loop has been activated

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        enabled: enabled
        """
        response = self.device.request(self.interface_name + "." + "getExternalSensor", [axis])
        self.device.handleError(response)
        return response[1]

    def getFinePositioningRange(self, axis):
        """
        This function gets the fine positioning DC-range

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        range: range in nm
        """
        response = self.device.request(self.interface_name + "." + "getFinePositioningRange", [axis])
        self.device.handleError(response)
        return response[1]

    def getFinePositioningSlewRate(self, axis):
        """
        This function gets the fine positioning slew rate

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        slewrate: slewrate [0|1|2|3]
        """
        response = self.device.request(self.interface_name + "." + "getFinePositioningSlewRate", [axis])
        self.device.handleError(response)
        return response[1]

    def getMotionControlThreshold(self, axis):
        """
        This function gets the threshold range within the closed-loop controlled movement stops to regulate.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        threshold: threshold in pm
        """
        response = self.device.request(self.interface_name + "." + "getMotionControlThreshold", [axis])
        self.device.handleError(response)
        return response[1]

    def getPositionsAndVoltages(self):
        """
        Simultaneously get 3 axes positions as well as the DC offset
            to maximize sampling rate over network

        Parameters
        ----------

        Returns
        -------
        pos1: pos1 position of axis 1
        pos2: pos2 position of axis 2
        pos3: pos3 position of axis 3
        val1: val1 dc voltage of of axis 1 in mV
        val2: val2 dc voltage of of axis 2 in mV
        val3: val3 dc voltage of of axis 3 in mV
        """
        response = self.device.request(self.interface_name + "." + "getPositionsAndVoltages")
        self.device.handleError(response)
        return response[1], response[2], response[3], response[4], response[5], response[6]

    def getReferencePosition(self, axis):
        """
        This function gets the reference position of the selected axis.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        position: position: For linear type actors the position is defined in nm for goniometer an rotator type actors it is µ°.
        """
        response = self.device.request(self.interface_name + "." + "getReferencePosition", [axis])
        self.device.handleError(response)
        return response[1]

    def getSensorDirection(self, axis):
        """
        This function gets whether the IDS sensor source of closed loop is inverted
            It is only available when the feature AMC/IDS closed loop has been activated

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        inverted: inverted boolen
        """
        response = self.device.request(self.interface_name + "." + "getSensorDirection", [axis])
        self.device.handleError(response)
        return response[1]

    def getSensorEnabled(self, axis):
        """
        Get sensot power supply status

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        value: value true if enabled, false otherwise
        """
        response = self.device.request(self.interface_name + "." + "getSensorEnabled", [axis])
        self.device.handleError(response)
        return response[1]

    def getStatusMovingAllAxes(self):
        """
        Get Status of all axes, see getStatusMoving for coding of the values

        Parameters
        ----------

        Returns
        -------
        moving1: moving1 status of axis 1
        moving2: moving2 status of axis 2
        moving3: moving3 status of axis 3
        """
        response = self.device.request(self.interface_name + "." + "getStatusMovingAllAxes")
        self.device.handleError(response)
        return response[1], response[2], response[3]

    def searchReferencePosition(self, axis):
        """
        This function searches for the reference position of the selected axis.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "searchReferencePosition", [axis])
        self.device.handleError(response)
        return 

    def setActorParametersByName(self, axis, actorname):
        """
        This function sets the name for the positioner on the selected axis. The possible names can be retrieved by executing getPositionersList

        Parameters
        ----------
        axis:  [0|1|2]
        actorname:  name of the actor

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setActorParametersByName", [axis, actorname])
        self.device.handleError(response)
        return 

    def setActorParametersJson(self, axis, json_dict):
        """
        Select and override a positioner out of the Current default list only override given parameters set others default

        Parameters
        ----------
        axis:  [0|1|2]
        json_dict:  dict with override params

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setActorParametersJson", [axis, json_dict])
        self.device.handleError(response)
        return 

    def setActorSensitivity(self, axis, sensitivity):
        """
        Control the actor parameter closed loop sensitivity

        Parameters
        ----------
        axis:  [0|1|2]
        sensitivity: 

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setActorSensitivity", [axis, sensitivity])
        self.device.handleError(response)
        return 

    def setAutoMeasure(self, axis, enable):
        """
        This function enables/disables the automatic C/R measurement on axis enable

        Parameters
        ----------
        axis:  [0|1|2]
        enable:  true: enable automeasurement, false: disable automeasurement

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setAutoMeasure", [axis, enable])
        self.device.handleError(response)
        return 

    def setControlAmplitude(self, axis, amplitude):
        """
        This function sets the amplitude of the actuator signal of the selected axis.

        Parameters
        ----------
        axis:  [0|1|2]
        amplitude:  in mV

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setControlAmplitude", [axis, amplitude])
        self.device.handleError(response)
        return 

    def setControlAutoReset(self, axis, enable):
        """
        This function resets the position every time the reference position is detected.

        Parameters
        ----------
        axis:  [0|1|2]
        enable:  boolean

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setControlAutoReset", [axis, enable])
        self.device.handleError(response)
        return 

    def setControlFixOutputVoltage(self, axis, amplitude_mv):
        """
        This function sets the DC level output of the selected axis.

        Parameters
        ----------
        axis:  [0|1|2]
        amplitude_mv:  in mV

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setControlFixOutputVoltage", [axis, amplitude_mv])
        self.device.handleError(response)
        return 

    def setControlFrequency(self, axis, frequency):
        """
        This function sets the frequency of the actuator signal of the selected axis.
             Note: Approximate the slewrate of the motion controller  according to Input Frequency

        Parameters
        ----------
        axis:  [0|1|2]
        frequency:  in  mHz

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setControlFrequency", [axis, frequency])
        self.device.handleError(response)
        return 

    def setControlMove(self, axis, enable):
        """
        This function sets the approach of the selected axis’ positioner to the target position.

        Parameters
        ----------
        axis:  [0|1|2]
        enable:  boolean true: eanble the approach , false: disable the approach

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setControlMove", [axis, enable])
        self.device.handleError(response)
        return 

    def setControlOutput(self, axis, enable):
        """
        This function sets the status of the output relays of the selected axis.
            Enable only if cable is connected and FlyBack is enabled
            use a PWM startup of 1sec

        Parameters
        ----------
        axis:  [0|1|2]
        enable:  true: enable drives, false: disable drives

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setControlOutput", [axis, enable])
        self.device.handleError(response)
        return 

    def setControlReferenceAutoUpdate(self, axis, enable):
        """
        This function sets the status of whether the reference position is updated when the reference mark is hit.
            When this function is disabled, the reference marking will be considered only the first time and after then ignored.

        Parameters
        ----------
        axis:  [0|1|2]
        enable:  boolean

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setControlReferenceAutoUpdate", [axis, enable])
        self.device.handleError(response)
        return 

    def setControlTargetRange(self, axis, range):
        """
        This function sets the range around the target position in which the flag "In Target Range" (see VIII.7.a) becomes active.

        Parameters
        ----------
        axis:  [0|1|2]
        range:  in nm

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setControlTargetRange", [axis, range])
        self.device.handleError(response)
        return 

    def setCrosstalkThreshold(self, axis, threshold, slipphasetime):
        """
        This function sets the threshold range and slip phase time which is used while moving another axis

        Parameters
        ----------
        axis:  [0|1|2]
        threshold:  in pm
        slipphasetime:  time after slip phase which is waited until the controller is acting again in microseconds

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setCrosstalkThreshold", [axis, threshold, slipphasetime])
        self.device.handleError(response)
        return 

    def setExternalSensor(self, axis, enabled, ignoreFunctionError=True):
        """
        This function sets the sensor source of closed loop to the IDS when enabled. Otherwise the normal AMC Sensor depending on the configuration (e.g. NUM or RES) is used
            It is only available when the feature AMC/IDS closed loop has been activated

        Parameters
        ----------
        axis:  [0|1|2]
        enabled: 
        ignoreFunctionError : boolean (default: True)
            True = Do not raise an AttoException if a warning code is returned.

        Returns
        -------
        warningNo: warningNo Warning code, can be converted into a string using the errorNumberToString function
        """
        response = self.device.request(self.interface_name + "." + "setExternalSensor", [axis, enabled])
        self.device.handleError(response, ignoreFunctionError)
        return response[0]

    def setFinePositioningRange(self, axis, range):
        """
        This function sets the fine positioning DC-range

        Parameters
        ----------
        axis:  [0|1|2]
        range:  in nm

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setFinePositioningRange", [axis, range])
        self.device.handleError(response)
        return 

    def setFinePositioningSlewRate(self, axis, slewrate):
        """
        This function sets the fine positioning slew rate

        Parameters
        ----------
        axis:  [0|1|2]
        slewrate:  [0|1|2|3]

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setFinePositioningSlewRate", [axis, slewrate])
        self.device.handleError(response)
        return 

    def setMotionControlThreshold(self, axis, threshold):
        """
        This function sets the threshold range within the closed-loop controlled movement stops to regulate. Default depends on connected sensor type

        Parameters
        ----------
        axis:  [0|1|2]
        threshold:  in pm

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setMotionControlThreshold", [axis, threshold])
        self.device.handleError(response)
        return 

    def setReset(self, axis):
        """
        This function resets the actual position of the selected axis given by the NUM sensor to zero and marks the reference position as invalid.
            It does not work for RES positioners and positions read by IDS.
            For IDS, use com.attocube.ids.displacement.resetAxis() or com.attocube.amc.amcids.resetIdsAxis() instead.

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setReset", [axis])
        self.device.handleError(response)
        return 

    def setSensorDirection(self, axis, inverted):
        """
        This function sets the IDS sensor source of closed loop to inverted when true.
            It is only available when the feature AMC/IDS closed loop has been activated

        Parameters
        ----------
        axis:  [0|1|2]
        inverted: 

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setSensorDirection", [axis, inverted])
        self.device.handleError(response)
        return 

    def setSensorEnabled(self, axis, value):
        """
        Set sensor power supply status, can be switched off to save heat generated by sensor [NUM or RES]
            Positions retrieved will be invalid when activating this, so closed-loop control should be switched off beforehand

        Parameters
        ----------
        axis:  [0|1|2]
        value:  true if enabled, false otherwise

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setSensorEnabled", [axis, value])
        self.device.handleError(response)
        return 

