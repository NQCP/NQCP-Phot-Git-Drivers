from anyvisa import AnyVisa
from Thorlabs_PM103E_Driver import Thorlabs_PM103E_Driver
print(AnyVisa.FindResources())
detector = Thorlabs_PM103E_Driver("TCPIP0::10.209.67.184::PM103E-4E_M01027537::INSTR")
detector.connect()
print(detector.get_idn())
print(detector.get_detector_power())
print(detector.get_detector_power())
print(detector.get_detector_power())
detector.disconnect()