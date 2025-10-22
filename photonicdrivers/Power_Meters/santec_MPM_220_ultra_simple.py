# from mpm_instrument import MPM
# import pyvisa

# # Initialize PyVISA resource manager
# rm = pyvisa.ResourceManager()
# list_of_resources = rm.list_resources()
# print(list_of_resources)

# # Open a connection to the MPM instrument via GPIB
# instrument = rm.open_resource("ASRL4::INSTR")
# # instrument.read_termination = '\r\n'
# # instrument.write_termination = '\n'
# instrument.timeout = 100  # Set timeout to 1000 milliseconds


# # mpm = MPM(instrument)

# # # Print the instrument identification
# # print(mpm.get_idn())


# rm.close() 

from ftd2xxhelper import Ftd2xxhelper

list_of_devices = Ftd2xxhelper.list_devices()      # Gets the list of detected USB connections
print(list_of_devices)