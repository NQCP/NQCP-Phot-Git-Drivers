# import API classes into the current namespace
from pulsestreamer import PulseStreamer, Sequence, OutputState, Sequence, ClockSource, TriggerRearm, TriggerStart, findPulseStreamers

# Example
# query the network for all connected Pulse Streamers
devices = findPulseStreamers("00:26:32:F0:B2:20")
print(devices)

# Connect to Pulse Streamer
ip= "10.209.69.141"
#ip = 'pulsestreamer'
ps = PulseStreamer(ip)

print(ps.getSerial())
print(ps.forceFinal())
print(ps.getSerial())
print(ps.hasFinished())
print(ps.getSerial())
ps = PulseStreamer(ip)
ps = PulseStreamer(ip)