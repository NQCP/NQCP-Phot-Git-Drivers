from photonicdrivers.ArduinoPressureReader.ArduinoPressureReader_Driver import ArduinoPressureReader_Driver
import numpy as np 

ip = "10.209.67.165"
port = "8082"
pressureRanges = np.array([16, 16, -1, -1]) # _pressureRanges_npArray has to be length 4 to match the number of sensors

reader = ArduinoPressureReader_Driver(ip,port,pressureRanges)
data = reader.getPressures()
print("Pressures [bar]: " + str(data))
