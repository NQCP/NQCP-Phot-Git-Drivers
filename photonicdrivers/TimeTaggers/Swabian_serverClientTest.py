import TimeTagger
from matplotlib import pyplot as plt
from time import sleep


ttNetwork = TimeTagger.createTimeTaggerNetwork('10.209.67.193:41101')
# Connect to the Time Tagger server. 'ip' is the IP address of the server and 'port' is the port defined by the server. The default port is 41101


print("hello")
binwidth_ps = int(1e9)

counter = TimeTagger.Counter(tagger=ttNetwork, channels=[1, 2], binwidth=binwidth_ps, n_values=1000)

# Apply the built-in test signal (~0.8 to 0.9 MHz) to channel 1
ttNetwork.setTestSignal(1, True)
print("Test signal on channel 1 enabled")
sleep(.5)
ttNetwork.setTestSignal(1, False)

# After waiting two times for 0.5 s, the 1000 values should be filled
sleep(.5)

# Data is retrieved by calling the method "getData" on the measurement class.
data = counter.getData()
time_s = counter.getIndex()/1e12
ch1 = data[0]*1e-3
ch2 = data[1]*1e-3

print(ch1)
print(ch2)

# Plot the result
plt.figure()
plt.plot(time_s, ch1, label='channel 1')
plt.plot(time_s, ch2, label='channel 2')
plt.xlabel('Time (s)')
plt.ylabel('Countrate (MHz)')
plt.legend()
plt.tight_layout()
plt.show()


TimeTagger.freeTimeTagger(ttNetwork)