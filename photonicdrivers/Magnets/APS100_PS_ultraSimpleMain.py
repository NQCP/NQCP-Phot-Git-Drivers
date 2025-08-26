import serial
import time
import socket

################### USB BASED CONNECTION ###################

# COM_PORT = 'COM6'
# BAUD_RATE = 9600


# device = serial.Serial(COM_PORT, BAUD_RATE, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE, timeout=1)
# # device = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
# # device.write(b'*IDN?\n')
# device.write(b'*IDN?;*ESE 12;*ESE?\r')

# time.sleep(0.5)
# # response = device.readline().decode('utf-8').strip()
# # response = device.readline().decode('utf-8')
# response = device.readline(1024)
# print(response)
# response = device.readline(1024)
# print(response)
# response = device.readline(1024)
# print(response)

# device.close()




# import pyvisa
# print("hello")
# # Open a VISA resource manager
# rm = pyvisa.ResourceManager()
# # List available VISA resources (instruments)
# # available_resources = rm.list_resources()
# # if not available_resources:
# #     print("No available VISA resources found.")
# # # Print the list of available resources
# # print("Available VISA resources:")
# # for idx, resource in enumerate(available_resources, start=1):
# #     print(f"{idx}. {resource}")



# # ASRL6::INSTR

# instrument = rm.open_resource("ASRL6::INSTR")

# # Send an IDN query using SCPI
# idn_query = "*IDN?"
# response = instrument.query(idn_query)
# print("Device Identification:", response)






# import serial.tools.list_ports
# # Get a list of all connected COM ports
# ports = serial.tools.list_ports.comports()
# # Print each available COM port
# if ports:
#     print("Connected COM ports:")
#     for port in ports:
#         print(f"{port.device}: {port.description}")
# else:
#     print("No COM ports found.")


################### ETHERNET BASED CONNECTION ###################

IPAddress='10.209.67.152'
Port=4444

print('Connecting via ethernet')
connectionType = 'Ethernet'

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5) # sets the timeout of the receive command. 
server_address = (IPAddress, Port) #IP address, port
sock.connect(server_address)

commandString = "*IDN?;*ESE 12;*ESE?\r\n"
sock.sendall(commandString.encode())
response = sock.recv(100)
print(response)

# commandString = "ULIM 1\n"
# sock.sendall(commandString.encode())

commandString = "*ESR?\n"
sock.sendall(commandString.encode())
response = sock.recv(100)
print(response)

commandString = "ULIM?\n"
sock.sendall(commandString.encode())
response = sock.recv(100)
print(response)

# commandString = "UNITS?\n"
# sock.sendall(commandString.encode())
# response = sock.recv(100)
# print(response)

# commandString = "UNITS A\n"
# sock.sendall(commandString.encode())

# commandString = "UNITS?\n"
# sock.sendall(commandString.encode())
# response = sock.recv(100)
# print(response)

sock.close()