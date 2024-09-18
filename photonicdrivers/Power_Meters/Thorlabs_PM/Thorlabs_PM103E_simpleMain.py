from anyvisa import AnyVisa
from Thorlabs_PM103E_Driver import Thorlabs_PM103E_Driver
print(AnyVisa.FindResources())
detector = Thorlabs_PM103E_Driver("TCPIP0::10.209.67.196::PM103E-A0_M01080977::INSTR")
detector.connect()
print(detector.set_power_unit("W"))
print(detector.get_power())
detector.disconnect()