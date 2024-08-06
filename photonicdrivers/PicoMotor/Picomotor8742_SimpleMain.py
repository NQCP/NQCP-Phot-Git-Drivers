# code for communicating with the PicoMotor from NewFocus model 8742 via USB

from Picomotor8742 import NewFocus_8742_Driver

#Decimal VendorID = 1027 & ProductID = 24596
#Hexadecimal VendorID = 0x403 & ProductID = 0x6014

# pico = PicoMotorController(vendor_ID_Hex=0x104d, product_ID_Hex=0x4000)
pico = NewFocus_8742_Driver(IP_adress='10.209.67.98', port=23)
pico.connect()
print(pico.get_product_ID())
print(pico.get_MAC_address())
print(pico.get_IP_address())
print(pico.get_host_name())
print(pico.get_target_position(4))
# pico.moveRelativePosition('1','-100')
pico.disconnect()