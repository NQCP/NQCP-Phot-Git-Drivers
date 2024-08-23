from photonicdrivers.AttocubeAPI import AMC

# has to run on the attocube PC
ip = "192.168.1.1"

amc = AMC.Device(ip)
amc.connect()
print(amc.control.getPositionsAndVoltages())

x = 2862504.854 # in nm
y = 3408544.614
z = 3154000.0

amc.control.MultiAxisPositioning(1, 1, 0, x, y, z)
print(amc.control.getStatusMovingAllAxes())
amc.close()