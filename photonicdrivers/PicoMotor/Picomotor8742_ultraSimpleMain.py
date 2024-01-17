# code for communicating with the PicoMotor from NewFocus model 8742 via USB

# https://itecnote.com/tecnote/python-pyusb-reading-from-a-usb-device/


import usb.core 
# documentation:
# https://docs.circuitpython.org/en/latest/shared-bindings/usb/core/index.html#usb.core.Device


####### find all USB devices connected to the PC #######
devices = usb.core.find(find_all=True)
print('All USB devices connected to the PC - VendorID and ProductID: \n')
for cfg in devices:
    # print('Manufacturer = ' + str(cfg.manufacturer) + ', Product = ' + str(cfg.product))
    print('Decimal VendorID = ' + str(cfg.idVendor) + ' & ProductID = ' + str(cfg.idProduct))
    print('Hexadecimal VendorID = ' + hex(cfg.idVendor) + ' & ProductID = ' + hex(cfg.idProduct) + '\n')
print('\n\n')


####### Print info of the PicoMotor #######
# Find vendor and product ID (in hex) in: Device Manager -> Properties -> Events -> Information
# Or perhaps the IDs are given in the manual of the device
# Hopefully IDs are present in the list printed with the code above
pico = usb.core.find(idVendor=0x104d, idProduct=0x4000)
if pico is None:
    raise ValueError("device not found")
else:
    print(pico)


####### Execute commands #######
# Get the IN and OUT Endpoint from the info printed about
EPI = 0x2  # EndPoint In
EPO = 0x81 # EndPoint Out
TO = 1000  # TimeOut in ms

cmd = '*IDN?\r'
print(cmd)
print(pico.write(EPI,cmd,TO)) # take care to use the right termination character (see manual)
response_raw = pico.read(EPO,100000,TO) # in decimal ASCII characters
response = ''.join(map(chr, response_raw)) # using method 2 from https://www.geeksforgeeks.org/python-ways-to-convert-list-of-ascii-value-to-string/
print(response) 

# print(pico.write(0x2,'ST\r',1000))
# print(pico.write(0x2,'1PR-200000\r'))


####### Close connection #######
# pico.reset() # this closes the connection but also "resets" the device, whatever that does
usb.util.dispose_resources(pico)