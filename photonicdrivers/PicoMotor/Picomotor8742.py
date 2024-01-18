# code for communicating with the PicoMotor from NewFocus model 8742 via USB

# https://itecnote.com/tecnote/python-pyusb-reading-from-a-usb-device/


import usb.core 
# documentation:
# https://docs.circuitpython.org/en/latest/shared-bindings/usb/core/index.html#usb.core.Device




class PicoMotor:
    def __init__(self, vendorIDHex, productIDHex):
        print("Initialising instance of PicoMotor class")
        self.endpointIn = 0x2
        self.endpointOut = 0x81
        self.timeOut = 1000 # ms
        self.termChar = '/r' # the termination character
        self.dev = usb.core.find(idVendor=vendorIDHex, idProduct=productIDHex)
        
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
    
    def __del__(self):
        usb.util.dispose_resources(self.dev)
        print("connection closed")



####### MAIN FUNCTION HERE #######

# pico = PicoMotor(0x104d, 0x4000)
# print(pico.getProductID())
# pico.closeConnection()
















