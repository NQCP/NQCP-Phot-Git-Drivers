# -*- coding: utf-8 -*-
"""
Network Time Tagger: Client example
See also: "server.py"
"""
import TimeTagger

print("""
*****************************
*    Time Tagger Network
*      Client example
*****************************
""")

print("Search for Time Taggers on the network...")
# Use the scanTimeTaggerServers() function to search for Time Tagger servers in the local network
servers = TimeTagger.scanTimeTaggerServers()
print("{} servers found.".format(len(servers)))
print(servers)

print('Information about Time Tagger server on localhost:')
try:
    server_info = TimeTagger.getTimeTaggerServerInfo('localhost')
    print(server_info)
except RuntimeError:
    raise Exception('No Time Tagger server available on "localhost" and the default port 41101.')

print('Connecting to the server on localhost.')

# Create a TimeTaggerNetwork instance and connect to the server
ttn = TimeTagger.createTimeTaggerNetwork('localhost')

# With the TimeTaggerNetwork object, we can set up a measurement as usual
channels = [1, 2, 3, 4]
crt = TimeTagger.Countrate(ttn, channels)

crt.startFor(int(1e12))
crt.waitUntilFinished()
countrates = crt.getData()

print('Measured count rates of channel 1-4 in counts/s:')
print(countrates)

# Check for overflows
overflows = ttn.getOverflows()
if overflows == 0:
    print("All incoming data has been processed.")
else:
    print("""{} data blocks are lost.\nBlock loss can happen during the USB transfer from the Time Tagger
to the Time Tagger Server and/or during the data transfer over the network from the Time Tagger Server to the client.
Overflows are caused by exceeding the processing power (CPU) on the client and/or the server,
the USB bandwidth, or the network bandwidth.""".format(overflows))

# Disconnect the client from the server
TimeTagger.freeTimeTagger(ttn)
del ttn
