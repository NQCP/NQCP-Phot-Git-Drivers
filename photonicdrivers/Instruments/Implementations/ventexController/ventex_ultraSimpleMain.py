## ultra simple program for the Ventex controller

# import socket

# IPAddress='10.209.67.120'
# Port=502

# print('Connecting via ethernet')
# connectionType = 'Ethernet'

# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.settimeout(5) # sets the timeout of the receive command. 
# server_address = (IPAddress, Port) #IP address, port
# sock.connect(server_address)

# commandString = "*IDN?\n"
# sock.sendall(commandString.encode())
# response = sock.recv(100)
# # response = response.decode('utf-8')
# print(response)

from pymodbus.client import ModbusTcpClient #  conda install conda-forge::pymodbus 
from pymodbus import pymodbus_apply_logging_config # to enable debug mode
import struct

# Define the Modbus server IP address and port
SERVER_HOST = '10.209.67.120'  # Change this to your Modbus server IP address
SERVER_PORT = 502           # Change this to your Modbus server port

# Define the Modbus slave ID
SLAVE_ID = 10  # Change this to your Modbus slave ID

# Define the Modbus register address to read
REGISTER_ADDRESS = 0

def uint16_to_decimal(uint16_value):
    return int(uint16_value)

def uint16_to_float(uint16_msw, uint16_lsw):
    # Convert uint16 (MSW-LSW) to float32
    uint32_value = (uint16_msw << 16) | uint16_lsw
    float_value = struct.unpack('f', struct.pack('I', uint32_value))[0]
    return float_value

def uint16_to_float32(uint16_array):
    float_array = []
    for i in range(0, len(uint16_array), 2):
        uint16_lsw = uint16_array[i]
        uint16_msw = uint16_array[i+1]
        uint32_value = (uint16_msw << 16) | uint16_lsw
        float_value = struct.unpack('f', struct.pack('I', uint32_value))[0]
        float_array.append(float_value)
    return float_array

def read_modbus_register(host, port, slave_id, register_address):
    pymodbus_apply_logging_config("DEBUG")
    try:
        print(host)
        print(port)
        print(slave_id)
        print(register_address)
        # Connect to the Modbus TCP server
        client = ModbusTcpClient(host, port)

        # Open the connection
        client.connect()

        # Read the register
        # result = client.read_holding_registers(register_address, 1, unit=)
        #result = client.read_holding_registers(5, 4, 10)
        result = client.read_input_registers(register_address, 20, slave_id)
        #print('')
        print(result)

        if result.isError():
             print("Error:", result)
        else:
            # values = result.registers
            # decimal_values = [uint16_to_decimal(value) for value in values]
            # print("Decimal values:", decimal_values)

                        # Convert uint16 values to float
            float_values = array_uint16_to_float32(result.registers)
            print("Float values:", float_values)
            print("Register value:", result.registers)

    # except Exception as e:
    #     print("Error:", e)

    finally:
        # Close the connection
        client.close()

# Call the function to read the Modbus register

def uint16_to_float32(msb, lsb):
    # Pack the two uint16 values into a byte string
    byte_string = struct.pack('>HH', msb, lsb)
    
    # Unpack the byte string as a single float32 value
    # >f specifies a float with big-endian (most to least significant bit) byte order
    float_value = struct.unpack('>f', byte_string)[0]
    
    return float_value

def array_uint16_to_float32(uint16_array):
    # Check if the length of the input array is even
    if len(uint16_array) % 2 != 0:
        raise ValueError("Input array length must be even")

    float_array = []
    for i in range(0, len(uint16_array), 2):
        msb = uint16_array[i]
        lsb = uint16_array[i + 1]

        # Pack the two uint16 values into a byte string
        byte_string = struct.pack('>HH', msb, lsb)

        # Unpack the byte string as a single float32 value
        float_value = struct.unpack('>f', byte_string)[0]

        float_array.append(float_value)

    return float_array

# Example usage: Convert 16827 and 13107 to a float32 value
result = uint16_to_float32(16827, 13107)
print(result)
read_modbus_register(SERVER_HOST, SERVER_PORT, SLAVE_ID, REGISTER_ADDRESS)
