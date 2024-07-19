from QDAC import QDAC2

IPAddress = "10.209.67.125"
Port= 5025
COMPort = "COM4"

#import socket


#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.settimeout(2) # sets the timeout of the receive command in seconds. 
#server_address = (IPAddress, Port)
#sock.connect(server_address)
#command = "*IDN?\n"
#sock.sendall(command.encode("utf-8"))
#byteString = sock.recv(1024)
#response = byteString.decode("utf-8")
#sock.close()



qdac = QDAC2(IPAddress,Port)
qdac.openEthernetConnection()
id = qdac.getProductID()
print(id)
qdac.printSystemInformation()
print(qdac.getErrorAll())
print(qdac.getErrorCount())

#qdac.setVoltageRange("2","HIGH")
#print(qdac.getVoltageRange("1", ""))
#qdac.setVoltageMode("2","FIX")
#print(qdac.getVoltageMode("1"))
#qdac.setVoltage("2","0")
#print(qdac.getVoltage("2"))
#qdac.setVoltage

qdac.closeEthernetConnection()