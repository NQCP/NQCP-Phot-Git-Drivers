    
class Diagnostic():

    def __init__(self, device):
        self.device = device
        self.interface_name = "com.attocube.amc.diagnostic"
            
    def getDiagnosticPower(self, axis):
        """
        Returns the current power consumption

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        power: power
        """
        response = self.device.request(self.interface_name + "." + "getDiagnosticPower", [axis])
        self.device.handleError(response)
        return response[1]

    def getDiagnosticResults(self, axis):
        """
        Returns the results of the last diagnostic run and an error, if there was no run, it is currently running or the run failed

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        capacity: capacity in nF
        resistance: resistance in Ohm
        """
        response = self.device.request(self.interface_name + "." + "getDiagnosticResults", [axis])
        self.device.handleError(response)
        return response[1], response[2]

    def getDiagnosticStepSize(self, axis):
        """
        Performs 10 steps in forward and backward and calculates the average step size in both directions on a specific axis

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        stepsize_fwd: stepsize_fwd
        stepsize_bwd: stepsize_bwd
        """
        response = self.device.request(self.interface_name + "." + "getDiagnosticStepSize", [axis])
        self.device.handleError(response)
        return response[1], response[2]

    def getDiagnosticTemperature(self, axis):
        """
        Returns the current axis temperature

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        temperature: temperature
        """
        response = self.device.request(self.interface_name + "." + "getDiagnosticTemperature", [axis])
        self.device.handleError(response)
        return response[1]

    def startDiagnostic(self, axis):
        """
        Start the diagnosis procedure for the given axis

        Parameters
        ----------
        axis:  [0|1|2]

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "startDiagnostic", [axis])
        self.device.handleError(response)
        return 

