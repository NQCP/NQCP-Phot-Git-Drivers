"""In this example, we observe the overflow behavior of the Time Tagger. Overflows occur when the data
rate is too high and the buffer onboard the Time Tagger is completely filled. In this situation, data
loss occurs."""

import sys
from time import sleep
import numpy as np
from matplotlib import pyplot as plt
import TimeTagger

# Create a TimeTagger instance to control your hardware
tagger = TimeTagger.createTimeTagger()

rising_edges = tagger.getChannelList(TimeTagger.ChannelEdge.Rising)
if tagger.getModel() == 'Time Tagger 20':
    CHANNELS = rising_edges[:1]
else:
    falling_edges = tagger.getChannelList(TimeTagger.ChannelEdge.Falling)
    CHANNELS = rising_edges[:4] + falling_edges[:4]

# Activate test signal on the selected channels
tagger.setTestSignal(CHANNELS, True)

counter = TimeTagger.Counter(tagger=tagger,
                             channels=CHANNELS,
                             binwidth=1000000000,
                             n_values=60000)

default_divider = tagger.getTestSignalDivider()
print("The test signal divider is reduced until overflows occur.")
print("The default test signal divider is: {}".format(default_divider))

sleep(2)

# We increase the data rate successively by reducing the TestSignalDivider
divider = default_divider
while divider > 1 and not tagger.getOverflows():
    divider //= 2
    sys.stdout.write("divider = {:<3}\r".format(divider))
    tagger.setTestSignalDivider(divider)
    sleep(5)
print("\nOverflows occurred at test signal divider of {}".format(divider))

# We let the Time Tagger run for two more seconds in the overflow
sleep(5)

# Reset TestSignalDivider to the default value to recover from overflow mode
tagger.setTestSignalDivider(default_divider)
sleep(3)
counter.stop()

# Use the .getDataObject() method to obtain an object that includes additional information
# on the data, e.g. the overflows or the count rate in counts/s.
data_object = counter.getDataObject()

# Plot the result
fig = plt.figure()
plt.title("Counter measurement with increasing test signal frequency")
plt.plot(data_object.getIndex()/1E12, data_object.getFrequency()[0, :])
plt.xlabel("Time (s)")
plt.ylabel("Counts/s")
data_for_annotation = data_object.getFrequency()[0, :]
annotation_y = np.nanmax(data_for_annotation)
annotation_x = data_object.getIndex()[np.where(
    data_for_annotation == annotation_y)[0][0]]/1e12
plt.annotate("""In the overflow mode,
there are gaps in the curve.
After the overflown buffer is
emptied by the USB transfer, it
can accumulate normal time-tags
for a short period, before
it overflows again. These
time-tags are displayed
between the gaps.""",
             (annotation_x, annotation_y),
             xytext=(0, annotation_y*0.6),
             va='center',
             ha='left',
             arrowprops={'arrowstyle': '->'})
plt.show()

TimeTagger.freeTimeTagger(tagger)
