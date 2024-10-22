import serial
import time

COM_PORT = 'COM4'
BAUD_RATE = 115200


# device = serial.Serial(COM_PORT, BAUD_RATE, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE, timeout=1)
device = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
# device.write(b'*IDN?\n')
device.write(b'*IDN?;*ESE 12;*ESE?\n')

time.sleep(0.5)
# response = device.readline().decode('utf-8').strip()
# response = device.readline().decode('utf-8')
response = device.readline()
print(response)




# import pyvisa
# print("hello")
# # Open a VISA resource manager
# rm = pyvisa.ResourceManager()
# # List available VISA resources (instruments)
# available_resources = rm.list_resources()
# if not available_resources:
#     print("No available VISA resources found.")
# # Print the list of available resources
# print("Available VISA resources:")
# for idx, resource in enumerate(available_resources, start=1):
#     print(f"{idx}. {resource}")




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

