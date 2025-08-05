"""Virtual channels are used to generate new data streams from given input streams. These data streams
can be used just like physical channels. It is also possible to cascade virtual channels
to create mighty filters that operate on the fly.
We use virtual channels in this example to answer the question: if the rising edges of the
built-in test signal on two channels are quite close to each other, are the subsequent falling
edges close as well? We use a cascade of virtual channels:
1. "Coincidence" determines whether two rising edges are close or not.
2. The result acts as a start signal for the "GatedChannel" for the falling edges of channel 1.
3. A "DelayedChannel" generated from the "Coincidence" closes this gate after one edge.
4. A second "GatedChannel" with swapped opener/closer includes complimentary data (falling edges
of input 1 following rising edges which are far apart)
Finally, we compare the Correlations of channel 2 and the two GatedChannel, respectively."""

from matplotlib import pyplot as plt
import numpy as np
import TimeTagger

# Create a TimeTagger instance to control your hardware
tagger = TimeTagger.createTimeTagger()

# Enable the test signal on channel 1 and channel 2
tagger.setTestSignal([1, 2], True)

# We use a Correlation measurement to determine the current delay between channel 1 and 2,
# then we set it to a defined value, DELAY, that requires compensation of the current delay.
DELAY = 200
calibration = TimeTagger.Correlation(tagger=tagger,
                                     channel_1=1,
                                     channel_2=2,
                                     binwidth=1,
                                     n_bins=10_000)
calibration.startFor(1E11)
calibration.waitUntilFinished()
current_delay = np.round(np.average(
    calibration.getIndex(), weights=calibration.getData()))
tagger.setInputDelay(1, DELAY - current_delay)
tagger.setInputDelay(-1, DELAY - current_delay)

# Now, we want to distinguish two cases: rising edges that are quite close with each other 
# and those that are further apart.
# As a tool, we use the virtual channel Coincidence with our measured average delay as coincidenceWindow.
# This means: if two edges are within the coincidenceWindow, there will be one timestamp
# in the virtual channel, right at the average of both input timestamps (determined by the "timestamp" argument).
open_gate = TimeTagger.Coincidence(tagger=tagger,
                                   channels=[1, 2],
                                   coincidenceWindow=DELAY,
                                   timestamp=TimeTagger.CoincidenceTimestamp.Average)
# To close the gate after one falling edge, we create a DelayedChannel from "open_gate". It is a copy of the open gate
# channel delayed by 900000 ps. Note how the channel number of "open_gate" is passed to the new virtual
# channel: We call the getChannel() method to retrieve the number assigned by the Time Tagger backend.
close_gate = TimeTagger.DelayedChannel(tagger=tagger,
                                       input_channel=open_gate.getChannel(),
                                       delay=900000)

# Now, we can create a reduced copy of the falling edges of input 1 that contains only those following a
# narrow pair of rising edges (those present in "open_gate"). We use the getInvertedChannel() method
# here to keep the example compatible with first generation Time Taggers that used another numbering
# scheme (starting with channel 0). If your Time Tagger starts at channel 1, you can use channel number
# -1 directly.
falling_narrow = TimeTagger.GatedChannel(tagger=tagger,
                                         input_channel=tagger.getInvertedChannel(
                                             1),
                                         gate_start_channel=open_gate.getChannel(),
                                         gate_stop_channel=close_gate.getChannel())
# The complementary data can be obtained by swapping "gate_start_channel" and "gate_stop_channel"
falling_wide = TimeTagger.GatedChannel(tagger=tagger,
                                       input_channel=tagger.getInvertedChannel(
                                           1),
                                       gate_start_channel=close_gate.getChannel(),
                                       gate_stop_channel=open_gate.getChannel())
# In the same way, we create GatedChannels from the later one of channel 1 and 2.
# Because the Coincidence timestamp is set to the average of both, we can use it
# to gate the second one.
# We use this second set of GatedChannels to demonstrate a special feature: if an opened gate is
# supposed to transmit exactly one input tag, you can use gate_stop_channel=input_channel, that
# means an input tag passes and closes the gate right after it. Similarly, if a closed gate is
# supposed to exclude exactly one input tag, you can use gate_start_channel=input_channel.
# With this scheme, you could realize this example without defining the DelayedChannel close_gate.
rising_narrow = TimeTagger.GatedChannel(tagger=tagger,
                                        input_channel=1,
                                        gate_start_channel=open_gate.getChannel(),
                                        gate_stop_channel=1)
rising_wide = TimeTagger.GatedChannel(tagger=tagger,
                                      input_channel=1,
                                      gate_start_channel=1,
                                      gate_stop_channel=open_gate.getChannel())

# Create a SynchronizedMeasurement to ensure that the same data set is used in both cases
synchronized = TimeTagger.SynchronizedMeasurements(tagger=tagger)
binwidth = 1
n_bins = abs(5 * DELAY) // binwidth
corr_falling_narrow = TimeTagger.Correlation(tagger=synchronized.getTagger(),
                                             channel_1=falling_narrow.getChannel(),
                                             channel_2=tagger.getInvertedChannel(
                                                 2),
                                             binwidth=binwidth,
                                             n_bins=n_bins)
corr_falling_wide = TimeTagger.Correlation(tagger=synchronized.getTagger(),
                                           channel_1=falling_wide.getChannel(),
                                           channel_2=tagger.getInvertedChannel(
                                               2),
                                           binwidth=binwidth,
                                           n_bins=n_bins)

corr_rising_narrow = TimeTagger.Correlation(tagger=tagger,
                                            channel_1=rising_narrow.getChannel(),
                                            channel_2=2,
                                            binwidth=binwidth,
                                            n_bins=n_bins)
corr_rising_wide = TimeTagger.Correlation(tagger=tagger,
                                          channel_1=rising_wide.getChannel(),
                                          channel_2=2,
                                          binwidth=binwidth,
                                          n_bins=n_bins)

# Run the measurement for 1 s
synchronized.startFor(capture_duration=int(1E12))
synchronized.waitUntilFinished()

# Plot the result
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(9, 6), sharex=True)
axes[0].plot(corr_rising_narrow.getIndex(), corr_rising_narrow.getData())
axes[0].plot(corr_rising_wide.getIndex(), corr_rising_wide.getData())
axes[0].set_title("Rising edges")
axes[0].set_ylabel("Counts/bin")
axes[0].legend(["corr_rising_narrow", "corr_rising_wide"])
# We use getDataNormalized() instead of getData() to account for a non-perfect
# 50:50 ratio of the counts of the two GatedChannels.
axes[1].plot(corr_falling_narrow.getIndex(),
             corr_falling_narrow.getDataNormalized())
axes[1].plot(corr_falling_wide.getIndex(),
             corr_falling_wide.getDataNormalized())
axes[1].set_title("Falling edges")
axes[1].set_xlabel("Time (ps)")
axes[1].set_ylabel("Counts/bin")
axes[1].legend(["corr_falling_narrow", "corr_falling_wide"])
axes[1].text(0, max(corr_falling_wide.getDataNormalized()/2), """Typically, the two curves are
more or less identical. This shows
that the position of a falling edge
is not correlated to the position of
the previous rising edge.""", ha="right")
plt.show()

TimeTagger.freeTimeTagger(tagger)
