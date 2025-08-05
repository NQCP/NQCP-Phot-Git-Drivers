from anyvisa import AnyVisa
from Thorlabs_PM103E_Driver import Thorlabs_PM103E_Driver
print(AnyVisa.FindResources())
detector = Thorlabs_PM103E_Driver("TCPIP0::10.209.67.196::2000::SOCKET")
detector.connect()
print(detector.set_power_unit("W"))
print(detector.get_power())
detector.disconnect()