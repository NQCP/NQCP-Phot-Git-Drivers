import serial
import time

# COM_PORT = 'COM4'
# BAUD_RATE = 9600

# device = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
# device.write(b'*IDN?\n')
# time.sleep(0.5)
# response = device.readline().decode('utf-8').strip()




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






# List all available COM ports using pyserial's list_ports
print("Available COM ports:")
for port in serial.tools.list_ports.comports():
    print(port.device)