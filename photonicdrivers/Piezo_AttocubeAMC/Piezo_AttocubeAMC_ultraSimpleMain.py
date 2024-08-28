from photonicdrivers.AttocubeAPI import AMC

# has to run on the attocube PC
ip = "192.168.1.1"

amc = AMC.Device(ip)
amc.connect()
print(amc.control.getPositionsAndVoltages())

x = 2659504.854 # in nm
y = 3400544.614
z = 3145000.0

amc.control.MultiAxisPositioning(1, 1, 1, x, y, z)
print(amc.control.getStatusMovingAllAxes())
amc.close()