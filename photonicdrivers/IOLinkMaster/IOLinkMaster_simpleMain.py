# from IOLinkMaster import IOLinkMaster
from IOLinkMaster import IOLinkMaster

ipadr='10.209.67.95'
inputPort=1

iolink = IOLinkMaster(ipadr)
flow, temp = iolink.getFlowAndTemp(inputPort)
print("Water low rate [L/min]: " + str(flow))
print("Water temperature [C]: " + str(temp))