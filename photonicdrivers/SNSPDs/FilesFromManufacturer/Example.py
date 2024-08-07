"""
The MIT License (MIT)

Copyright (c) 2020 Single Quantum B. V. and Andreas Fognini

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


Example.py

The following code explains how to
    - receive counts from the detectors
    - set/get a bias current
    - set/get trigger level
    - set/get the measurement time
    - enable the detectors
    - get the number of detectors
    
    Use:
    
    python Example.py -ip 192.168.1.1 -N 3
    
"""
# from .WebSQControl import WebSQControl
from photonicdrivers.SNSPDs.FilesFromManufacturer.WebSQControl import WebSQControl
import random
import argparse


# Parses arguments, type -h for help message
parser = argparse.ArgumentParser(
    add_help=True,
    description='Example program.')
parser.add_argument('-N', dest='N', type=int, default=10,
                    help='The amount of measurements done.')
parser.add_argument(
    '--ipAddress',
    '-ip',
    dest='tcp_ip_address',
    type=str,
    default='192.168.1.1',
    help='The TCP IP address of the detector')
args = parser.parse_args()

# Number of measurements (default 10)
N = args.N

# TCP IP Address of your system (default 192.168.1.1)
tcp_ip_address = args.tcp_ip_address

# The control port (default 12000)
control_port = 12000
# The port emitting the photon Counts (default 12345)
counts_port = 12345


websq = WebSQControl(TCP_IP_ADR=tcp_ip_address, CONTROL_PORT=control_port, COUNTS_PORT=counts_port)
# Alternatively, you can use the with clause
# with WebSQControl(TCP_IP_ADR=tcp_ip_address, CONTROL_PORT=control_port, COUNTS_PORT=counts_port) as websq:


websq.connect()
print("Automatically finding bias current, avoid Light exposure")
found_bias_current = websq.auto_bias_calibration(
    DarkCounts=[100, 100, 100, 100])
print("Bias current: " + str(found_bias_current))

# Acquire number of detectors in the system
number_of_detectors = websq.get_number_of_detectors()
print("Your system has " + str(number_of_detectors) + ' detectors\n')

print("Set integration time to 20 ms\n")
websq.set_measurement_periode(20)   # Time in ms

print("Enable detectors\n")
websq.enable_detectors(True)


# Random generator
def rand():
    return random.randrange(0, 10000) / 1000.0


# Set the bias current and trigger level with random numbers
curr = []
trig = []
for n in range(number_of_detectors):
    curr.append(rand())
    trig.append(rand())

print("Set bias currents to: " + str(curr))
websq.set_bias_current(current_in_uA=curr)

print("Set trigger levels to: " + str(trig))
websq.set_trigger_level(trigger_level_mV=trig)
print("\n")


# Acquire N counts measurements
# Returns an array filled with N numpy arrays each
# containing as first element a time stamp and then the detector
# counts ascending order

print("Acquire " + str(N) + " counts measurements")
print("============================\n")
# Get the counts
counts = websq.acquire_cnts(N)

# Print the counts nicely
header = "Timestamp\t\t"
for n in range(number_of_detectors):
    header += "Channel" + str(n + 1) + "\t"

print(header)

for row in counts:
    line = ""
    for element in row:
        line += str(element) + '\t'
    print(line)

print('\n')

print("Read back set values")
print("====================\n")
print("Measurement Periode (ms): \t"
      + str(websq.get_measurement_periode()))
print("Bias Currents in uA: \t\t" + str(websq.get_bias_current()))
print("Trigger Levels in mV: \t\t" + str(websq.get_trigger_level()))


# Close connection
websq.close() # not needed since the with closes the connection
