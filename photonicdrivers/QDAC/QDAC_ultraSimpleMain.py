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
print(response)