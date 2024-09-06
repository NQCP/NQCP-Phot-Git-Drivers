# import qdac2
# import common.connection as conn
# # from serial import Serial

# device = conn.find_qdac2_on_usb()
# qdac = qdac2.QDAC2(device)
# print(qdac.status())

import socket

class QDAC2_Driver():
    def __init__(self,_ip_string: str,_port_number: int) -> None:
        self.ipAddress = _ip_string
        self.port = _port_number
        self.timeout = 2 # seconds
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout) # sets the timeout of the receive command in seconds. 
        self.server_address = (self.ipAddress, self.port)
        
        self.terminationChar = "\n"

    # High level methods are methods that consist of multiple low level methods
    # A low level method sends a single (or very few) command string

    ##################### HIGH LEVEL METHODS ###########################

    def printSystemInformation(self) -> None:
        print("IDN:")
        print(self.getProductID())
        print("MAC address:")
        print(self.getMACAddress())
        print("IP address:")
        print(self.getIPAddress())
        print("Subnet mask:")
        print(self.getSubnetMask())
        print("Gateway:")
        print(self.getGetway())
        print("Hostname:")
        print(self.getHostName())
        print("DHCP [on/off]:")
        print(self.getDHCPStatus())

    ##################### LOW LEVEL SYSTEM METHODS ###########################

    def getProductID(self) -> str:
        response = self._query("*IDN?")
        return response
    
    def getIPAddress(self) -> str:
        response = self._query("syst:comm:lan:ipad?")
        return response
    
    def getMACAddress(self) -> str:
        response = self._query("syst:comm:lan:mac?")
        return response
    
    def getGetway(self) -> str:
        response = self._query("syst:comm:lan:gat?")
        return response
    
    def getSubnetMask(self) -> str:
        response = self._query("syst:comm:lan:smas?")
        return response
    
    def getHostName(self) -> str:
        response = self._query("syst:comm:lan:host?")
        return response
    
    def getDHCPStatus(self) -> str:
        response = self._query("syst:comm:lan:dhcp?")
        return response
    
    def getErrorAll(self) -> str:
        response = self._query("syst:err:all?")
        return response
    
    def getErrorCount(self) -> str:
        response = self._query("syst:err:coun?")
        return response

    def restartSystem(self) -> None:
        command = "syst:comm:lan:rest"
        self._write(command)        
        self._checkForErrors(command)

    def setDCHP(self, DHCPStatusString: str) -> None:
        if DHCPStatusString == "ON" or DHCPStatusString == "OFF":
            command = "SYST:COMM:LAN:DHCP " + DHCPStatusString
            self._write(command)            
            self._checkForErrors(command)
            self.updateMemory()
            self.restartSystem()
        else:
            print("The DHCPStatusString provided is not valid. It must be either ON of OFF.")

    def setIPAddress(self) -> None:
        print("Setting the IP address must be done via USB communication, which has not been implemented yet.")

    def updateMemory(self) -> None:
        command = "syst:comm:lan:upd"
        self._write(command)
        self._checkForErrors(command)

    ##################### LOW LEVEL SOURCE METHODS ###########################

    def getVoltageRange(self, chNumberString: str, chListNumberString: str) -> str:
        # Either chNumberString or chListNumberString must be empty - the command either changes a single channel OR a list of channels
        response = self._query("sour" + chNumberString + ":rang? " + chListNumberString) # return LOW for 2 V, HIGH for 10 V
        return response
    
    def getVoltageMode(self, chNumberString: str) -> str:
        response = self._query("sour" + chNumberString + ":mode?") # returns FIXED, SWEEP, or LIST
        return response
    
    def getVoltage(self, chNumberString: str) -> str:
        response = self._query("sour" + chNumberString + ":volt?")
        return response
    
    def getCurrent(self, chNumberString: str) -> str:
        response = self._query("sour" + chNumberString + ":curr?")
        return response

    def setVoltageRange(self, chNumberString: str, rangeString: str) -> None:
        if rangeString == "HIGH" or rangeString == "LOW":
            command = "sour" + chNumberString + ":rang " + rangeString
            self._write(command) # returns LOW for 2 V, HIGH for 10 V
            self._checkForErrors(command)
        else:
            print("The rangeString must be either HIGH or LOW")

    def setVoltageMode(self, chNumberString: str, modeString: str) -> None:
        if modeString == "FIX" or modeString == "SWE" or modeString == "LIST":
            command = "sour" + chNumberString + ":mode " + modeString
            self._write(command)
            self._checkForErrors(command)
        else:
            print("The modeString must be either FIX, SWE, or LIST")

    def setVoltage(self,chNumberString: str,voltageString: str) -> None:
        command = "sour" + chNumberString + ":volt " + voltageString
        self._write(command) # returns the current output voltage
        self._checkForErrors(command)

    ##################### OTHER METHODS ###########################
    
    def closeEthernetConnection(self) -> None:
        print('Closing QDAC ethernet connection')
        self.sock.close()

    def openEthernetConnection(self) -> None:
        print('Connecting to QDAC via ethernet')
        self.sock.connect(self.server_address) 
    
    ##################### PRIVATE METHODS ###########################

    def _query(self,commandString: str) -> str:
        self._write(commandString)
        response = self._read()    

        # check is the system responded with an error:     
        self._checkForErrors(commandString)

        return response

    def _write(self, commandString: str) -> None:
        command = commandString + self.terminationChar
        self.sock.sendall(command.encode("utf-8"))
        # command = bytes(commandString + self.terminationChar, "utf-8")
        # self.sock.sendall(command)

    def _read(self, bytesToReceive: int = 1024) -> str:
        byteString = self.sock.recv(bytesToReceive)
        response = byteString.decode("utf-8")
        return response

    def _checkForErrors(self, commandString: str) -> None: 
        # To avoid recursion, the commands are typed in directly rather than calling the class methods
        self._write("syst:err:coun?")
        errorCount = self._read()
        if float(errorCount) > 0:            
            self._write("syst:err:all?")
            errors = self._read()
            print("The QDAC returned the error(s): " + errors + "when executing the command: " + commandString)