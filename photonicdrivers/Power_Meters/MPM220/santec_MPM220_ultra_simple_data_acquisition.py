import pyvisa
import struct
import numpy as np

rm = pyvisa.ResourceManager()
mpm = rm.open_resource("GPIB0::16::INSTR", read_termination=None)
mpm.timeout = 5000 

# Stop logging first if necessary
mpm.write("LOGS 0")

# Request log data
mpm.write("LOGG? 0,0")

# Step 1: Read header
header_start = mpm.read_bytes(1)      # should be b'#'
num_digits_byte = mpm.read_bytes(1)   # ASCII digit
num_digits = int(num_digits_byte.decode('ascii'))
byte_count_ascii = mpm.read_bytes(num_digits)  # total binary byte count
byte_count = int(byte_count_ascii.decode('ascii'))

print(f"Expecting {byte_count} bytes of binary data...")

# Step 2: Read binary data
binary_data = mpm.read_bytes(byte_count)

# Step 3: Convert to floats (little endian)
num_floats = byte_count // 4
log_values = list(struct.unpack('<' + 'f'*num_floats, binary_data))

print(f"Received {len(log_values)} points")
print(log_values)  

mpm.close()
