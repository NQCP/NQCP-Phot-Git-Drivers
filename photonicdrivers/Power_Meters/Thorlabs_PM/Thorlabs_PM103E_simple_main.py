
print(AnyVisa.FindResources())
detector = Thorlabs_PM103E("TCPIP0::10.209.67.184::PM5020_07::INSTR")
detector.connect()
print(detector.get_idn())
print(detector.get_detector_power())
print(detector.get_detector_power())
print(detector.get_detector_power())
detector.disconnect()