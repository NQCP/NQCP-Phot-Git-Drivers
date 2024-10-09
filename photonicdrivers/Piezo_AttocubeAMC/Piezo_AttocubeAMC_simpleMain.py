from photonicdrivers.Piezo_AttocubeAMC.Piezo_AttocubeAMC_Driver import Piezo_AttocubeAMC_Driver

# has to run on the attocube PC
ip = "192.168.1.1"

piezo = Piezo_AttocubeAMC_Driver(ip)
piezo.connect()
print(piezo.get_position())
piezo.disconnect()

