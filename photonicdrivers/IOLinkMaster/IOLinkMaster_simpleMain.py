# from IOLinkMaster import IOLinkMaster
from photonicdrivers.IOLinkMaster.IOLinkMaster_Driver import IOLinkMaster_Driver

ipadr='10.209.67.95'
inputPort=1

iolink = IOLinkMaster_Driver(ipadr)
flow, temp = iolink.getFlowAndTemp(inputPort)
print("Water low rate [L/min]: " + str(flow))
print("Water temperature [C]: " + str(temp))