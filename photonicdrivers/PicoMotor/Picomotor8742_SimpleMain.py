# code for communicating with the PicoMotor from NewFocus model 8742 via USB

from Picomotor8742 import PicoMotor

# pico = PicoMotor(vendorIDHex=0x104d, productIDHex=0x4000)
pico = PicoMotor(IPAddress='10.209.67.98', Port=23)
print(pico.getProductID())
print(pico.getMACAddress())
print(pico.getIPAddress())
print(pico.getHostName())
# pico.moveRelativePosition('1','-100')
pico.closeConnection()