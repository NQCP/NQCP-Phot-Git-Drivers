# ## Python sample script to communicate with RLS Picus laser

## Python sample script to communicate with RLS Picus laser
import pyvisa #Communication via VISA
rm = pyvisa.ResourceManager()
# Connect to the laser
laser = rm.open_resource('COM3') # use the correct COM port
laser.read_termination = '\n'
laser.write_termination = '\n'
## Enable Laser

print(type(laser))
print(laser.query('Laser:Enable?'))
a = laser.write("Laser:Enable?")
print(a)
b = laser.read()
print(b)


## Set and query wavelength
# print(laser.query('Laser:Wavelength 850'))
# print(laser.query('Laser:Wavelength?'))
# ## Shutdown Laser
# print(laser.query('Laser:Enable 0'))
laser.close()

print("different method!")

## Alternatively, use of Pyserial if VISA is not available
from serial import Serial # Communication via Serial Port
laser = Serial(port='COM3', timeout = 3)
cmd = 'Laser:Enable?\n' #Append Termchar!
laser.write(cmd.encode()) #Pyserial needs to encode string to bytes
print(laser.readline().decode()) #Decoding necessary for read data
#In serial communication, the laser.write() command needs to be
#followed by a laser.readline() command
laser.close()