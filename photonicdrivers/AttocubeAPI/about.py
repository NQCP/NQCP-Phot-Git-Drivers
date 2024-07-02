    
class About():

    def __init__(self, device):
        self.device = device
        self.interface_name = "com.attocube.system.about"
            
    def getInstalledPackages(self):
        """
        Get list of packages installed on the device

        Parameters
        ----------

        Returns
        -------
        value_string1: string: Comma separated list of packages
        """
        response = self.device.request(self.interface_name + "." + "getInstalledPackages")
        self.device.handleError(response)
        return response[1]

    def getPackageLicense(self, pckg):
        """
        Get the license for a specific package

        Parameters
        ----------
        pckg:  string: Package name

        Returns
        -------
        value_string1: string: License for this package
        """
        response = self.device.request(self.interface_name + "." + "getPackageLicense", [pckg])
        self.device.handleError(response)
        return response[1]

