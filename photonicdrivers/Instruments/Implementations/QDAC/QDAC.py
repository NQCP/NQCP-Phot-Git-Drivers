# import qdac2
# import common.connection as conn
# # from serial import Serial

# device = conn.find_qdac2_on_usb()
# qdac = qdac2.QDAC2(device)
# print(qdac.status())

import socket

class QDAC2():
    def __init__(self,_ip_string,_port_number) -> None:
        self.ipAddress = _ip_string
        self.port = _port_number
        self.timeout = 2 # seconds

        self.openEthernetConnection()

        self.terminationChar = "\n"

    
    
    
    # High level methods are methods that consist of multiple low level methods
    # A low level method sends a single (or very few) command string

    ##################### HIGH LEVEL METHODS ###########################

    def printSystemInformation(self):
        print("IDN:")
        print(self.getProductID())
        print("MAC address:")
        print(self.getMACAddress())
        print("IP address:")
        print(self.getIPAddress())
        print("Subnet mask:")
        print(self.getSubnetMask())
        print("Gatewat:")
        print(self.getGetway())
        print("Hostname:")
        print(self.getHostName())
        print("DHCP [on/off]:")
        print(self.getDHCPStatus())

    ##################### LOW LEVEL SYSTEM METHODS ###########################

    def getProductID(self):
        response = self._query("*IDN?")
        return response
    
    def getIPAddress(self):
        response = self._query("syst:comm:lan:ipad?")
        return response
    
    def getMACAddress(self):
        response = self._query("syst:comm:lan:mac?")
        return response
    
    def getGetway(self):
        response = self._query("syst:comm:lan:gat?")
        return response
    
    def getSubnetMask(self):
        response = self._query("syst:comm:lan:smas?")
        return response
    
    def getHostName(self):
        response = self._query("syst:comm:lan:host?")
        return response
    
    def getDHCPStatus(self):
        response = self._query("syst:comm:lan:dhcp?")
        return response
    
    def openEthernetConnection(self):
        print('Connecting to QDAC via ethernet')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout) # sets the timeout of the receive command in seconds. 
        self.server_address = (self.ipAddress, self.port)
        self.sock.connect(self.server_address) 

    def restartSystem(self):
        self._write("syst:comm:lan:rest")

    def setDCHP(self, DHCPStatusString):
        if DHCPStatusString == "ON" or DHCPStatusString == "OFF":
            self._write("SYST:COMM:LAN:DHCP " + DHCPStatusString)
            self.updateMemory()
            self.restartSystem()
        else:
            print("The DHCPStatusString provided is not valid. It must be either ON of OFF.")

    def setIPAddress(self):
        print("Setting the IP address much be done via USB, which has not been implemented yet.")

    def updateMemory(self):
        self._write("syst:comm:lan:upd")

    ##################### LOW LEVEL SOURCE METHODS ###########################

    def getVoltageRange(self, chNumberString, chListNumberString):
        # Either chNumberString or chListNumberString must be empty - the command either changes a single channel OR a list of channels
        response = self._query("sour" + chNumberString + ":rang? " + chListNumberString) # return LOW for 2 V, HIGH for 10 V
        return response
    
    def getVoltageMode(self, chNumberString):
        response = self._query("sour" + chNumberString + ":mode?") # returns FIXED, SWEEP, or LIST
        return response
    
    def getVoltage(self, chNumberString):
        response = self._query("sour" + chNumberString + ":volt?")
        return response
    
    def getCurrent(self, chNumberString):
        response = self._query("sour" + chNumberString + ":curr?")
        return response

    def setVoltageRange(self, chNumberString, rangeString):
        if rangeString == "HIGH" or rangeString == "LOW":
            command = "sour" + chNumberString + ":rang " + rangeString
            self._write(command) # returns LOW for 2 V, HIGH for 10 V
        else:
            print("The rangeString must be either HIGH or LOW")

    def setVoltageMode(self, chNumberString, modeString):
        if modeString == "FIX" or modeString == "SWE" or modeString == "LIST":
            command = "sour" + chNumberString + ":mode " + modeString
            # print(command)
            self._write(command)
        else:
            print("The modeString must be either FIX, SWE, or LIST")

    def setVoltage(self,chNumberString,voltageString):
        self._write("sour" + chNumberString + ":volt " + voltageString) # returns the current output voltage

    ##################### PRIVATE METHODS ###########################

    def _query(self,commandString):
        self._write(commandString)
        return self._read()    

    def _write(self, commandString):
        command = commandString + self.terminationChar
        self.sock.sendall(command.encode("utf-8"))
        # command = bytes(commandString + self.terminationChar, "utf-8")
        # self.sock.sendall(command)

    def _read(self):
        bytesToReceive = 1024
        byteString = self.sock.recv(bytesToReceive)
        response = byteString.decode("utf-8")
        return response
