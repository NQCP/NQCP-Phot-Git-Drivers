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


class PicoMotor:
    def __init__(self, vendorIDHex, productIDHex):
        print("Initialising instance of PicoMotor class")
        self.endpointIn = 0x2
        self.endpointOut = 0x81
        self.timeOut = 1000 # ms
        self.termChar = '/r' # the termination character
        print("2")
        self.dev = usb.core.find(idVendor=vendorIDHex, idProduct=productIDHex)
        print("3")
        # print(self.dev)
    
    def printEPO(self):
        print(self.endpointOut)
        
    def getProductID(self):
        # cmd = '*IDN?'+self.termChar
        # print(cmd)
        self.dev.write(self.endpointIn,'*IDN?\r',self.timeOut)
        # print('wrote command')
        response_raw = self.dev.read(self.endpointOut,100000,self.timeOut)
        # print(response_raw)
        response = ''.join(map(chr, response_raw))
        # print(response)
        return response
    
    def closeConnection(self):
        usb.util.dispose_resources(self.dev)
        print("connection closed")
















