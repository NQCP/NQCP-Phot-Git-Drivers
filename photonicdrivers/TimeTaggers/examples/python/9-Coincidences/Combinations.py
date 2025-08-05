"""
This example shows how to use the virtual channel Combinations.
It detects clicks on all possible channel combinations and facilitates 
counting coincidences with clicks on a specific group of channels while no clicks on others. 
Up to 6 input channels will be used, with the test signal with co-prime dividers.
It yields a high input rate, decreasing toward higher-order coincidences.
"""


import itertools
import numpy as np
import TimeTagger


# Define a useful function that will be used to measure and print the count rates
def measure_countrates():
    """Measure and print the countrates"""
    with TimeTagger.Countrate(tagger, virtual_channels) as crate:
        crate.startFor(5e12)
        crate.waitUntilFinished()
        rates = crate.getData()
        for includes_first in (True, False):
            print("\nCombinations", "including" if includes_first else "not including",
                  f"{reference_channel}:")
            for i, group in enumerate(groups):
                if (1 in group) == includes_first:
                    print("Combination: {}, rate: {:.1f} cps".format(
                        group, rates[i]))
    return rates


# Create a TimeTagger instance to control your hardware
tagger = TimeTagger.createTimeTagger()

# Get up to 6 available channels.
all_channels = tagger.getChannelList(TimeTagger.ChannelEdge.Rising)
all_channels = all_channels if len(all_channels) <= 6 else all_channels[:6]
reference_channel = all_channels[0]
channels = all_channels[1:]

# Enable test signal
tagger.setTestSignal(all_channels, True)

# Create Correlation measurements and use SynchronizedMeasurements to start them easily
sm = TimeTagger.SynchronizedMeasurements(tagger)
corr_list = list()
for ch in channels:
    corr_list.append(
        TimeTagger.Correlation(
            sm.getTagger(), reference_channel, ch, binwidth=1, n_bins=5000)
    )

# Start measurements and accumulate data for 1 second
sm.startFor(int(1e12), clear=True)
sm.waitUntilFinished()

# Determine delays
delays = list()
for corr in corr_list:
    hist_t = corr.getIndex()
    hist_c = corr.getData()
    dt = np.sum(hist_t * hist_c) / np.sum(hist_c)
    delays.append(int(dt))

print("Delays:", delays)

# Set input delay correction to align all channels
for ch, dt in zip(channels, delays):
    tagger.setInputDelay(ch, dt)

# Increase the test signal rate to have enhance the probability
# to have high-order coincidences
default_divider = tagger.getTestSignalDivider()
tagger.setTestSignalDivider(np.ceil(default_divider/4))

# Measure the period of the test signal
with TimeTagger.Countrate(tagger, channels) as crate:
    crate.startFor(1e11)
    crate.waitUntilFinished()
    period = int(1e12 / crate.getData()[0])
    print("Rate per input without divider: {:.1f} Mcps".format(1e6 / period))
    windows_size = period // 2

# Set the prime dividers on all channels except for the first one.
# The first channel is included in the combination; therefore we get that all combinations
# without this channel are zero, as it always clicks.
dividers = sorted([3, 5, 7, 11, 13, 17])[:len(all_channels)]
for c, d in zip(channels, dividers[1:]):
    tagger.setEventDivider(c, d)

# Create the Combinations virtual channel
combination = TimeTagger.Combinations(tagger, all_channels, windows_size)

# Make all possible combinations to access the virtual channel numbers
groups = []
max_order = len(all_channels) + 1
for order in range(max_order, 1, -1):
    groups.extend(list(itertools.combinations(all_channels, order)))

# Create a list with the virtual channels monitoring the combinations
virtual_channels = []
for group in groups:
    virtual_channels.append(combination.getChannel(group))
# Add to the list of virtual channels the one monitoring 2-fold combinations
n_channel = 2
virtual_channels.append(combination.getSumChannel(n_channel))

# Run a countrate measurement on each virtual channel to see the individual rates.
print('\n***********************************************************************************')
print(f'Channel {reference_channel} has full click rate. It will always be present in the combination window.')
print('We expect all combinations without channel 1 to have 0 rate')
print('***********************************************************************************')
measure_countrates()

# Set the divider to the first channel as well as see how the combinations rates change
tagger.setEventDivider(reference_channel, dividers[0])

# Run a countrate measurement on each virtual channel to see the individual rates.
print('\n***********************************************************************************')
print(f'Channel {reference_channel} has a lower rate now')
print('We expect all combinations to have a rate greater than 0.')
print('***********************************************************************************')
rates = measure_countrates()

# Use the getCombination() method to find the index range corresponding to the 2-fold combinations.
lower_2fold_index = len(virtual_channels)
upper_2fold_index = 0
for index, virtual_channel in enumerate(virtual_channels):
    if len(combination.getCombination(virtual_channel)) == 2:
        lower_2fold_index = min(index, lower_2fold_index)
        upper_2fold_index = max(index, upper_2fold_index)

# This is compared to the last entry in rates correspond to the sumChannel(2).
print('\nSum of 2-fold combination from the sumChannel(2): {:.1f} cps and from the sum of the individual channels with combination of 2 elements: {:.1f} cps'.format(
    rates[-1], sum(rates[lower_2fold_index:upper_2fold_index+1])))

# Close the connection to the Time Tagger
TimeTagger.freeTimeTagger(tagger)
