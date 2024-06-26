    
class Network():

    def __init__(self, device):
        self.device = device
        self.interface_name = "com.attocube.system.network"
            
    def apply(self):
        """
        Apply temporary IP configuration and load it

        Parameters
        ----------

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "apply")
        self.device.handleError(response)
        return 

    def configureWifi(self, mode, ssid, psk):
        """
        Change the wifi configuration and applies it

        Parameters
        ----------
        mode:  0: Access point, 1: Wifi client
        ssid: 
        psk:  Pre-shared key

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "configureWifi", [mode, ssid, psk])
        self.device.handleError(response)
        return 

    def discard(self):
        """
        Discard temporary IP configuration

        Parameters
        ----------

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "discard")
        self.device.handleError(response)
        return 

    def getDefaultGateway(self):
        """
        Get the default gateway of the device

        Parameters
        ----------

        Returns
        -------
        Default: Default gateway
        """
        response = self.device.request(self.interface_name + "." + "getDefaultGateway")
        self.device.handleError(response)
        return response[1]

    def getDnsResolver(self, priority):
        """
        Get the DNS resolver

        Parameters
        ----------
        priority:  of DNS resolver (Usually: 0 = Default, 1 = Backup)

        Returns
        -------
        IP: IP address of DNS resolver
        """
        response = self.device.request(self.interface_name + "." + "getDnsResolver", [priority])
        self.device.handleError(response)
        return response[1]

    def getEnableDhcpClient(self):
        """
        Get the state of DHCP client

        Parameters
        ----------

        Returns
        -------
        value_boolean1: boolean: true = DHCP client enable, false = DHCP client disable
        """
        response = self.device.request(self.interface_name + "." + "getEnableDhcpClient")
        self.device.handleError(response)
        return response[1]

    def getEnableDhcpServer(self):
        """
        Get the state of DHCP server

        Parameters
        ----------

        Returns
        -------
        value_boolean1: boolean: true = DHCP server enable, false = DHCP server disable
        """
        response = self.device.request(self.interface_name + "." + "getEnableDhcpServer")
        self.device.handleError(response)
        return response[1]

    def getIpAddress(self):
        """
        Get the IP address of the device

        Parameters
        ----------

        Returns
        -------
        IP: IP address as string
        """
        response = self.device.request(self.interface_name + "." + "getIpAddress")
        self.device.handleError(response)
        return response[1]

    def getProxyServer(self):
        """
        Get the proxy settings of the devide

        Parameters
        ----------

        Returns
        -------
        Proxy: Proxy Server String, empty for no proxy
        """
        response = self.device.request(self.interface_name + "." + "getProxyServer")
        self.device.handleError(response)
        return response[1]

    def getRealIpAddress(self):
        """
        Get the real IP address of the device set to the network interface (br0, eth1 or eth0)

        Parameters
        ----------

        Returns
        -------
        IP: IP address as string
        """
        response = self.device.request(self.interface_name + "." + "getRealIpAddress")
        self.device.handleError(response)
        return response[1]

    def getSubnetMask(self):
        """
        Get the subnet mask of the device

        Parameters
        ----------

        Returns
        -------
        Subnet: Subnet mask as string
        """
        response = self.device.request(self.interface_name + "." + "getSubnetMask")
        self.device.handleError(response)
        return response[1]

    def getWifiMode(self):
        """
        Get the operation mode of the wifi adapter

        Parameters
        ----------

        Returns
        -------
        mode: mode 0: Access point, 1: Wifi client
        """
        response = self.device.request(self.interface_name + "." + "getWifiMode")
        self.device.handleError(response)
        return response[1]

    def getWifiPassphrase(self):
        """
        Get the the passphrase of the network hosted (mode: Access point) or connected to (mode: client)

        Parameters
        ----------

        Returns
        -------
        psk: psk Pre-shared key
        """
        response = self.device.request(self.interface_name + "." + "getWifiPassphrase")
        self.device.handleError(response)
        return response[1]

    def getWifiPresent(self):
        """
        Returns is a Wifi interface is present

        Parameters
        ----------

        Returns
        -------
        True: True, if interface is present
        """
        response = self.device.request(self.interface_name + "." + "getWifiPresent")
        self.device.handleError(response)
        return response[1]

    def getWifiSSID(self):
        """
        Get the the SSID of the network hosted (mode: Access point) or connected to (mode: client)

        Parameters
        ----------

        Returns
        -------
        SSID: SSID
        """
        response = self.device.request(self.interface_name + "." + "getWifiSSID")
        self.device.handleError(response)
        return response[1]

    def setDefaultGateway(self, gateway):
        """
        Set the default gateway of the device

        Parameters
        ----------
        gateway:  Default gateway as string

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setDefaultGateway", [gateway])
        self.device.handleError(response)
        return 

    def setDnsResolver(self, priority, resolver):
        """
        Set the DNS resolver

        Parameters
        ----------
        priority:  of DNS resolver (Usually: 0 = Default, 1 = Backup)
        resolver:  The resolver's IP address as string

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setDnsResolver", [priority, resolver])
        self.device.handleError(response)
        return 

    def setEnableDhcpClient(self, enable):
        """
        Enable or disable DHCP client

        Parameters
        ----------
        enable:  boolean: true = enable DHCP client, false = disable DHCP client

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setEnableDhcpClient", [enable])
        self.device.handleError(response)
        return 

    def setEnableDhcpServer(self, enable):
        """
        Enable or disable DHCP server

        Parameters
        ----------
        enable:  boolean: true = enable DHCP server, false = disable DHCP server

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setEnableDhcpServer", [enable])
        self.device.handleError(response)
        return 

    def setIpAddress(self, address):
        """
        Set the IP address of the device

        Parameters
        ----------
        address:  IP address as string

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setIpAddress", [address])
        self.device.handleError(response)
        return 

    def setProxyServer(self, proxyServer):
        """
        Set the proxy server of the device

        Parameters
        ----------
        proxyServer:  Proxy Server Setting as string

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setProxyServer", [proxyServer])
        self.device.handleError(response)
        return 

    def setSubnetMask(self, netmask):
        """
        Set the subnet mask of the device

        Parameters
        ----------
        netmask:  Subnet mask as string

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setSubnetMask", [netmask])
        self.device.handleError(response)
        return 

    def setWifiMode(self, mode):
        """
        Change the operation mode of the wifi adapter

        Parameters
        ----------
        mode:  0: Access point, 1: Wifi client

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setWifiMode", [mode])
        self.device.handleError(response)
        return 

    def setWifiPassphrase(self, psk):
        """
        Change the passphrase of the network hosted (mode: Access point) or connected to (mode: client)

        Parameters
        ----------
        psk:  Pre-shared key

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setWifiPassphrase", [psk])
        self.device.handleError(response)
        return 

    def setWifiSSID(self, ssid):
        """
        Change the SSID of the network hosted (mode: Access point) or connected to (mode: client)

        Parameters
        ----------
        ssid: 

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "setWifiSSID", [ssid])
        self.device.handleError(response)
        return 

    def verify(self):
        """
        Verify that temporary IP configuration is correct

        Parameters
        ----------

        Returns
        -------
        """
        response = self.device.request(self.interface_name + "." + "verify")
        self.device.handleError(response)
        return 

