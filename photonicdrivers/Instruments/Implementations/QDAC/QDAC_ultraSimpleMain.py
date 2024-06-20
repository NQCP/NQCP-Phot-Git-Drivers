# import qdac2
# import common.connection as conn
# # from serial import Serial

# device = conn.find_qdac2_on_usb()
# qdac = qdac2.QDAC2(device)
# print(qdac.status())

import socket

IPAddress='10.209.67.125'
Port=5025

print('Connecting via ethernet')
connectionType = 'Ethernet'

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5) # sets the timeout of the receive command. 
server_address = (IPAddress, Port) #IP address, port
sock.connect(server_address)

commandString = "*IDN?\n"
sock.sendall(commandString.encode())
response = sock.recv(100)