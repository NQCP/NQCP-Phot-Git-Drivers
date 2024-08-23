from photonicdrivers.AttocubeAPI import AMC

# ip = "192.168.1.1"
ip = "10.209.67.151"

amc = AMC.Device(ip)
amc.connect()
print(amc.control.getPositionsAndVoltages())
amc.close()