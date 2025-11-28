import pyvisa

# Initialize PyVISA resource manager
rm = pyvisa.ResourceManager()
list_of_resources = rm.list_resources()
print(list_of_resources)

# # Open a connection to the MPM instrument via RS232
# instrument = rm.open_resource("USB0::0x1313::0x807A::M01044633::INSTR")
instrument = rm.open_resource('GPIB0::16::INSTR')  # Example for COM5 on Windows
# # instrument = rm.open_resource("TCPIP0::192.168.1.161::SOCKET")

# Print the instrument identification
print(instrument.query("*IDN?"))
print(instrument.query("WAV?"))
print(instrument.query('READ? 0').split(','))


rm.close() 
