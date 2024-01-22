# code for communicating with the PicoMotor from NewFocus model 8742 via USB

import usb.core 
# 'usb' is part of the pyusb package (which has dependencies in the libusb package).
# Neither package is included in the .toml file, because installing the packages with pip does not work.
# Instead the packages should be installed with conda using:
# conda install conda-forge::pyusb
# installing pyusb like this will also install its dependencies (libusb) and add the .dll files from libusb to the PATH environment
# Documentation:
# https://docs.circuitpython.org/en/latest/shared-bindings/usb/core/index.html#usb.core.Device
# https://itecnote.com/tecnote/python-pyusb-reading-from-a-usb-device/

import socket


class PicoMotor:
    def __init__(self, vendorIDHex = None, productIDHex = None, IPAddress = None, Port = None):
        print("Initialising instance of PicoMotor class")

        self.connectionType = None
        if vendorIDHex != None and productIDHex != None:
            # open a usb connection
            print('Connecting via USB')
            self.endpointIn = 0x2
            self.endpointOut = 0x81
            self.timeOut = 1000 # ms
            self.termChar = '\r' # the termination character THIS IS NEVER USED, BECAUSE IT SHOULD BE SAVED IN A WAY THAT PRESERVES THE TERMINATION CHARACTER TYPE
            self.dev = usb.core.find(idVendor=vendorIDHex, idProduct=productIDHex)
            self.connectionType = 'USB'

        elif IPAddress != None and Port != None:
            # open an ethernet connection
            print('Connecting via ethernet')
            
            print('implement cuntionality here')

            self.connectionType = 'Ethernet'

        else:
            print("Insufficient arguments for initialising the PicoMotor class")

        # print(self.dev)
    
    def printEPO(self):
        print(self.endpointOut)
        
    def getProductID(self):
        self.__writeCommand('*IDN?')
        # print('wrote command') 
        response = self.__readCommand()
        # print(response)
        return response
    
    def MoveTargetPosition(self, axisNumberStr):
        self.__writeCommand(axisNumberStr + 'PA')

    def moveRelativePosition(self, axisNumberStr, distanceStr):
        self.__writeCommand(axisNumberStr + 'PR' + distanceStr)

    def getTargetPosition(self, axisNumberStr):
        self.__writeCommand(axisNumberStr + 'PR?')
        response = self.__readCommand()
        return response
    
    
    def closeConnection(self):
        usb.util.dispose_resources(self.dev)
        print("connection closed")

##################### PRIVATE METHODS ###########################

    def __writeCommand(self, command):
        if self.connectionType == 'USB':
            # print('sending usb command')
            commandString = command + self.termChar
            self.dev.write(self.endpointIn,commandString,self.timeOut)

        elif self.connectionType == 'Ethernet':
            print('implement cuntionality here')

        else:
            print('ERROR in PicoMotorClass - connection has not been initialised properly')

    
    def __readCommand(self, bitsToRead=100000):
        if self.connectionType == 'USB':
            response_ASCII = self.dev.read(self.endpointOut,bitsToRead,self.timeOut)
            # Convert response from ASCII to string 
            # using method 2 from https://www.geeksforgeeks.org/python-ways-to-convert-list-of-ascii-value-to-string/
            response = ''.join(map(chr, response_ASCII))
            return response
        
        elif self.connectionType == 'Ethernet':
            print('implement cuntionality here')
            
        else:
            print('ERROR in PicoMotorClass - connection has not been initialised properly')
















