from QDAC import QDAC2

IPAddress = "10.209.67.125"
Port= 5025
COMPort = "COM4"

qdac = QDAC2(IPAddress,Port)
id = qdac.getProductID()
print(id)
qdac.printSystemInformation()

# print(qdac.getErrorAll())
# print(qdac.getErrorCount())

# qdac.setVoltageRange("2","HIGH")
# print(qdac.getVoltageRange("1", ""))
# qdac.setVoltageMode("2","FIX")
# print(qdac.getVoltageMode("1"))
# qdac.setVoltage("2","0")
# print(qdac.getVoltage("2"))
# qdac.setVoltage

qdac.closeEthernetConnection()