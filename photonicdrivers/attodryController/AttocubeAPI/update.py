    
class Update():

    def __init__(self, device):
        self.device = device
        self.interface_name = "com.attocube.system.update"
            
    def getLicenseUpdateProgress(self):
        """
        Get the progress of running license update

        Parameters
        ----------

        Returns
        -------
        value_int1: int: progress in percent
        """
        response = self.device.request(self.interface_name + "." + "getLicenseUpdateProgress")
        self.device.handleError(response)
        return response[1]

    def getSwUpdateProgress(self):
        """
        Get the progress of running update

        Parameters
        ----------

        Returns
        -------
        value_int1: int: progress in percent
        """
        response = self.device.request(self.interface_name + "." + "getSwUpdateProgress")
        self.device.handleError(response)
        return response[1]

    def licenseUpdateBase64(self):
        """
        Execute the license update with base64 file uploaded. After execution, a manual reboot is nevessary.

        Parameters
        ----------

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "licenseUpdateBase64")
        self.device.handleError(response)
        return 

    def softwareUpdateBase64(self):
        """
        Execute the update with base64 file uploaded. After completion, a manual reboot is necessary.

        Parameters
        ----------

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "softwareUpdateBase64")
        self.device.handleError(response)
        return 

    def uploadLicenseBase64(self, offset, b64Data):
        """
        Upload new license file in format base 64

        Parameters
        ----------
        offset:  int: offset of the data
        b64Data:  string: base64 data

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "uploadLicenseBase64", [offset, b64Data])
        self.device.handleError(response)
        return 

    def uploadSoftwareImageBase64(self, offset, b64Data):
        """
        Upload new firmware image in format base 64

        Parameters
        ----------
        offset:  int: offset of the data
        b64Data:  string: base64 data

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "uploadSoftwareImageBase64", [offset, b64Data])
        self.device.handleError(response)
        return 

