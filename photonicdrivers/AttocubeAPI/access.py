    
class Access():

    def __init__(self, device):
        self.device = device
        self.interface_name = ""
            
    def getLockStatus(self):
        """
        This function returns if the device is locked and if the current client is authorized to use the device.

        Parameters
        ----------

        Returns
        -------
        locked: locked Is the device locked?
        authorized: authorized Is the client authorized?
        """
        response = self.device.request(self.interface_name + "" + "getLockStatus")
        self.device.handleError(response)
        return response[1], response[2]

    def grantAccess(self, password):
        """
        Grants access to a locked device for the requesting IP by checking against the password

        Parameters
        ----------
        password: string the current password

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "" + "grantAccess", [password])
        self.device.handleError(response)
        return 

    def lock(self, password):
        """
        This function locks the device with a password, so the calling of functions is only possible with this password. The locking IP is automatically added to the devices which can access functions

        Parameters
        ----------
        password: string the password to be set

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "" + "lock", [password])
        self.device.handleError(response)
        return 

    def unlock(self, password):
        """
        This function unlocks the device, so it will not be necessary to execute the grantAccess function to run any function

        Parameters
        ----------
        password: string the current password

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "" + "unlock", [password])
        self.device.handleError(response)
        return 

