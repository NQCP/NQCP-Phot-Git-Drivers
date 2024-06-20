# import qdac2
# import common.connection as conn
# # from serial import Serial

# device = conn.find_qdac2_on_usb()
# qdac = qdac2.QDAC2(device)
# print(qdac.status())

import socket

class QDAC2():
    def __init__(self,_ip_string,_port) -> None:
        self.ipAddress = _ip_string
        self.port = _port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(5) # sets the timeout of the receive command. 
        self.server_address = (self.ipAddress, self.port) #IP address, port
        self.sock.connect(self.server_address) 

    def get_product_ID(self):
        self._write_command('*IDN?')
        response = self._read_command()
        return response

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