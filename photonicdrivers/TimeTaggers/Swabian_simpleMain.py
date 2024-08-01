# from photonicdrivers.SNSPDs.FilesFromManufacturer.WebSQControl import WebSQControl
from Swabian import SwabianTimeTagger
from matplotlib import pyplot as plt
from time import sleep

# https://www.swabianinstruments.com/static/documentation/TimeTagger/tutorials/TimeTaggerRPC.html
# If the "Time Tagger Lab" software is installed, code example can be found here C:\Program Files\Swabian Instruments\Time Tagger\examples

# The TimeTagger module uses an older version of numpy. I got it to work with 1.26 (the highest 1.x version)

serverIP = "10.209.67.193"
serverPort = "41101"

ttNetwork = SwabianTimeTagger(serverIP=serverIP, serverPort=serverPort)

ttNetwork.connect("Network")
# print(ttx.getSerial())

binWidth = int(1e11)
nBins = 20

# ttNetwork.setTriggerLevel(1, 0.2)
# ttNetwork.printAllTriggerLevels()

counter = ttNetwork.countHistogram([6], binWidth, nBins)
data = counter.getData()
print(data)
sleep(2)
data = counter.getData()
print(data)
time_s = counter.getIndex()/1e12
ch1 = data[0]
# ch2 = data[1]

# Plot the result
plt.figure()
plt.plot(time_s, ch1, label='channel 1')
# plt.plot(time_s, ch2, label='channel 2')
plt.xlabel('Time (s)')
plt.ylabel('Counts per bin')
plt.legend()
plt.tight_layout()
plt.show()

ttNetwork.disconnect()
