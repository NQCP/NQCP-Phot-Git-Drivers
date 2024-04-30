# code for communicating with the PicoMotor from NewFocus model 8742 via USB

import socket

import usb.core
from photonicdrivers.Instruments.Abstract.Abstract import Instrument


# 'usb' is part of the pyusb package (which has dependencies in the libusb package).
# Neither package is included in the .toml file, because installing the packages with pip does not work.
# Instead the packages should be installed with conda using:
# conda install conda-forge::pyusb
# installing pyusb like this will also install its dependencies (libusb) and add the .dll files from libusb to the PATH environment
# Documentation:
# https://docs.circuitpython.org/en/latest/shared-bindings/usb/core/index.html#usb.core.Device
# https://itecnote.com/tecnote/python-pyusb-reading-from-a-usb-device/


class PicoMotor(Instrument):
    def __init__(self, vendorIDHex = None, productIDHex = None, IPAddress = None, Port = None):
        print("Initialising instance of PicoMotor class")

        self.termChar = '\r' # the termination character THIS IS NEVER USED, BECAUSE IT SHOULD BE SAVED IN A WAY THAT PRESERVES THE TERMINATION CHARACTER TYPE

        self.connectionType = None
        if vendorIDHex != None and productIDHex != None:
            # open a usb connection
            print('Connecting via USB')
            self.connectionType = 'USB'

            self.endpointIn = 0x2
            self.endpointOut = 0x81
            self.timeOut = 1000 # ms
            
            self.dev = usb.core.find(idVendor=vendorIDHex, idProduct=productIDHex)
            

        elif IPAddress != None and Port != None:
            # open an ethernet connection
            print('Connecting via ethernet')
            self.connectionType = 'Ethernet'
            
            # Create a TCP/IP socket
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(5) # sets the timeout of the receive command. 
            self.server_address = (IPAddress, Port) #IP address, port
            self.sock.connect(self.server_address)

            # For some reason, there is some output ready immediately after connection has been created. 
            # The format might be a telnet command?
            print('Immediate output from device:')
            print(self.sock.recv(1024))
            

        else:
            print("Insufficient arguments for initialising the PicoMotor class")

        # print(self.dev)
            
    def getProductID(self):
        self.__writeCommand('*IDN?')
        response = self.__readCommand()
        return response
    
    def getIPAddress(self):
        self.__writeCommand('IPADDR?')   
        response = self.__readCommand()
        return response
    
    def getHostName(self):
        self.__writeCommand('HOSTNAME?')
        response = self.__readCommand()
        return response

    def getMACAddress(self):
        self.__writeCommand('MACADDR?')
        response = self.__readCommand() # returns decimal string. For example: 5827809, 292293
        # The first number is the NewFocus specific identifier. The second is device specific
        if self.connectionType == 'USB':
            response = self.__convertToMACAddress(response)

        return response
    
    def moveTargetPosition(self, axisNumberStr):
        """
        Moves a given axis of the Picomotor to a specified target position.

        @param axisNumberStr: {0,1,2,3}
        """
        self.__writeCommand(axisNumberStr + 'PA')

    def moveRelativePosition(self, axisNumberStr, distanceStr):
        """
        Moves a given axis of the Picomotor a relative position given by the distance parameter.

        @param axisNumberStr: Parameter to identify the axis to be moved: {0,1,2,3}
        @param distanceStr: The distance to moved: float32
        @return: None
        """
        self.__writeCommand(axisNumberStr + 'PR' + distanceStr)

    def getTargetPosition(self, axisNumberStr):
        """
        Returns the position of the target axis
        @param axisNumberStr:
        @return: The distance of the target axis
        """
        self.__writeCommand(axisNumberStr + 'PR?')
        response = self.__readCommand()
        return response
    
    def writeCustomCommand(self, commandStr):
        self.__writeCommand(commandStr)
        response = self.__readCommand()
        return response
        
    def closeConnection(self):
        if self.connectionType == 'USB':
            usb.util.dispose_resources(self.dev)
            print("connection closed")

        elif self.connectionType == 'Ethernet':
            self.sock.close()

        else:
            print('ERROR in PicoMotorClass - connection has not been initialised properly')

        

##################### PRIVATE METHODS ###########################

    def __writeCommand(self, command):
        if self.connectionType == 'USB':
            commandString = command + self.termChar
            self.dev.write(self.endpointIn,commandString,self.timeOut)

        elif self.connectionType == 'Ethernet':
            commandString = command + self.termChar
            self.sock.sendall(commandString.encode())

        else:
            print('ERROR in PicoMotorClass - connection has not been initialised properly')

    
    def __readCommand(self, bitsToRead=4096):
        if self.connectionType == 'USB':
            response_ASCII = self.dev.read(self.endpointOut,bitsToRead,self.timeOut)

            # Convert response from ASCII to string 
            # using method 2 from https://www.geeksforgeeks.org/python-ways-to-convert-list-of-ascii-value-to-string/
            response = ''.join(map(chr, response_ASCII))
            return response
        
        elif self.connectionType == 'Ethernet':
            response = self.sock.recv(bitsToRead)

            # remove the newline characters if present
            if b"\r\n" in response:
                response, dummy  = response.split(b'\r\n')

            # convert from byte string to string
            response = response.decode('utf-8')
            return response

        else:
            print('ERROR in PicoMotorClass - connection has not been initialised properly')

    def __convertToMACAddress(self,MAC_string):
        # Converting the decimal numbers to HEX
        MAC1, MAC2 = MAC_string.split(', ')
        MAC1_dec = int(MAC1) # cast to int decimal
        MAC1_hex = format(MAC1_dec, '06X') # format to 6 digit hex
        MAC2_dec = int(MAC2)
        MAC2_hex = format(MAC2_dec, '06X')
        MAC_joinedStr = MAC1_hex + MAC2_hex # joining the two numbers into a 12 digit hex, which is the MAC address
        # print(MAC_joinedStr)

        return MAC_joinedStr

        