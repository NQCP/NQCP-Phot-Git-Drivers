# from photonicdrivers.SNSPDs.FilesFromManufacturer.WebSQControl import WebSQControl
import TimeTagger
from matplotlib import pyplot as plt
from time import sleep

# https://www.swabianinstruments.com/static/documentation/TimeTagger/tutorials/TimeTaggerRPC.html
# If the "Time Tagger Lab" software is installed, code example can be found here C:\Program Files\Swabian Instruments\Time Tagger\examples

# The TimeTagger module uses an older version of numpy. I got it to work with 1.26 (the highest 1.x version)

print("hello")
print("Serial numbers of all available TimeTaggers:")
print(TimeTagger.scanTimeTagger())

serialNumber = "23010013V4"
ttx = TimeTagger.createTimeTagger(serialNumber)
print(ttx.getSerial())
binwidth_ps = int(1e9)

counter = TimeTagger.Counter(tagger=ttx, channels=[1, 2], binwidth=binwidth_ps, n_values=1000)

# Apply the built-in test signal (~0.8 to 0.9 MHz) to channel 1
ttx.setTestSignal(1, True)
print("Test signal on channel 1 enabled")
sleep(.5)
ttx.setTestSignal(1, False)

# After waiting two times for 0.5 s, the 1000 values should be filled
sleep(.5)

# Data is retrieved by calling the method "getData" on the measurement class.
data = counter.getData()
time_s = counter.getIndex()/1e12
ch1 = data[0]*1e-3
ch2 = data[1]*1e-3

# Plot the result
plt.figure()
plt.plot(time_s, ch1, label='channel 1')
plt.plot(time_s, ch2, label='channel 2')
plt.xlabel('Time (s)')
plt.ylabel('Countrate (MHz)')
plt.legend()
plt.tight_layout()
plt.show()

TimeTagger.freeTimeTagger(ttx)