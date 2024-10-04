from photonicdrivers.AttocubeAPI import AMC

# has to run on the attocube PC
ip = "192.168.1.1"

amc = AMC.Device(ip)
amc.connect()
x, y, z, v1, v2, v3 = amc.control.getPositionsAndVoltages()
print((x,y,z))

x = x + 50*1000
# y = y + 120*1000
z = 3_174_000 # nm


# amc.control.MultiAxisPositioning(1, 1, 0, x, y, z)
amc.control.MultiAxisPositioning(0, 0, 1, x, y, z)
print(amc.control.getStatusMovingAllAxes())
amc.close()