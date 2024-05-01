# code for communicating with the PicoMotor from NewFocus model 8742 via USB

from Picomotor8742 import PicoMotor

# pico = PicoMotor(vendorIDHex=0x104d, productIDHex=0x4000)
pico = PicoMotor(IP_adress='10.209.67.98', port=23)
print(pico.get_product_ID())
print(pico.get_MAC_address())
print(pico.get_IP_address())
print(pico.get_host_name())
# pico.moveRelativePosition('1','-100')
pico.disconnect()