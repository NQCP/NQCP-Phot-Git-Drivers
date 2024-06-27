    
class Functions():

    def __init__(self, device):
        self.device = device
        self.interface_name = "com.attocube.system.functions"
            
    def checkAMCinRack(self):
        """
        If AMC is on Rack position 0, use it as DHCP server, else use it as DHCP client
        -------
        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "checkAMCinRack")
        return 

