import pyvisa

rm = pyvisa.ResourceManager()
ip = "10.209.64.205"

device_address = f'TCPIP0::{ip}::INSTR'

oscilloscope = rm.open_resource(device_address)

print(oscilloscope.query("*IDN?"))