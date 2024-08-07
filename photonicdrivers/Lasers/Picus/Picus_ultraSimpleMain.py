# ## Python sample script to communicate with RLS Picus laser

# import pyvisa

# print("Hello")
# rm = pyvisa.ResourceManager()
# print(rm.list_resources())

# connection = rm.open_resource('ASRL3::INSTR')
# print("connection opened")

# connection.baud_rate = 115200


# try:
#     print("trying something")
#     # Send an IDN query using SCPI
#     idn_query = "*IDN?\n"
#     response = connection.query(idn_query)
#     print("Device Identification:", response.strip())

# except:
#     print("An exception occurred") 

# print("closing")
# connection.close()
# rm.close()
# print("Done")






## Python sample script to communicate with RLS Picus laser
import pyvisa #Communication via VISA
rm = pyvisa.ResourceManager()
# Connect to the laser
laser = rm.open_resource('COM5') # use the correct COM port
laser.read_termination = '\n'
laser.write_termination = '\n'
## Enable Laser
print(laser.query('Laser:Enable?'))
## Set and query wavelength
# print(laser.query('Laser:Wavelength 850'))
# print(laser.query('Laser:Wavelength?'))
# ## Shutdown Laser
# print(laser.query('Laser:Enable 0'))
laser.close()



## Alternatively, use of Pyserial if VISA is not available
from serial import Serial # Communication via Serial Port
laser = Serial(port='COM5', timeout = 3)
cmd = 'Laser:Enable?\n' #Append Termchar!
laser.write(cmd.encode()) #Pyserial needs to encode string to bytes
print(laser.readline().decode()) #Decoding necessary for read data
#In serial communication, the laser.write() command needs to be
#followed by a laser.readline() command