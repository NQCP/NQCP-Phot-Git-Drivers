from anyvisa import AnyVisa
from Thorlabs_PM103E_Driver import Thorlabs_PM103E_Driver
print(AnyVisa.FindResources())
detector = Thorlabs_PM103E_Driver("TCPIP0::10.209.67.196::PM103E-A0_M01080977::INSTR")
detector.connect()
print(detector.get_idn())
print(detector.get_detector_power())
detector.disconnect()