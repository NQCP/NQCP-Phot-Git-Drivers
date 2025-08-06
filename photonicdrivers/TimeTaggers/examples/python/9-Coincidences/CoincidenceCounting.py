"""
This example shows how to use perform a coincidence-counting experiment.
All up to 16 input channels will be used, with the test signal at maximum
rate with co-prime dividers. This yield a high input rate, but only a low
rate of coincidences of higher orders.
"""

from TimeTagger import (createTimeTagger, Countrate, Coincidences,
                        ChannelEdge, SynchronizedMeasurements, Correlation,
                        freeTimeTagger)
from itertools import combinations
import sys
import time
import numpy as np

tagger = createTimeTagger()

channels = tagger.getChannelList(ChannelEdge.Rising)[:16]
min_order = 2
max_order = min(10, len(channels))
print(
    "Counting all coincidences on {} channels for the orders {} to {}".format(
        len(channels), min_order, max_order
    )
)

# Enable test signal
tagger.setTestSignal(channels, True)

# Set input delays to 0, otherwise the compensation result will be incorrect.
for ch in channels:
    tagger.setInputDelay(ch, 0)

# Create Correlation measurements and use SynchronizedMeasurements to start them easily
sm = SynchronizedMeasurements(tagger)
corr_list = list()
for ch in channels[1:]:
    corr_list.append(
        Correlation(sm.getTagger(), channels[0], ch, binwidth=1, n_bins=5000)
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
for ch, dt in zip(channels[1:], delays):
    tagger.setInputDelay(ch, dt)

# Increase the test signal rate
default_divider = tagger.getTestSignalDivider()
tagger.setTestSignalDivider(np.ceil(default_divider/20))

# Measure the period of the test signal
with Countrate(tagger, channels[:1]) as rate:
    rate.startFor(int(1e11))
    rate.waitUntilFinished()
    period = int(1e12 / rate.getData()[0])
    print("Rate per input without divider: {:.1f} Mcps".format(1e6 / period))
    coincidence_window = period // 2

# Set the co-prime dividers on all channels
# 16 co-prime numbers in the range 23..77
dividers = sorted([11*7, 13*5, 17*3, 19*2, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71])
for c, d in zip(channels, dividers):
    tagger.setEventDivider(c, d)

# Measure the total rate of all channels
with Countrate(tagger, channels) as rate:
    rate.startFor(int(1e12))
    rate.waitUntilFinished()
    print("Total rate within 1s: {:.1f} Mcps".format(sum(rate.getData()) * 1e-6))


def CountCoincidences(groups, order):
    # Flush the pipeline for proper efficiency statistics
    tagger.sync()

    with Coincidences(tagger, groups, coincidence_window) as co, Countrate(tagger, co.getChannels()) as rate:
        sys.stdout.write("Order {} with {} groups: ".format(order, len(groups)))
        time.sleep(10)  # Wait 10 seconds of real time
        efficiency = rate.getCaptureDuration() * 1e-11  # % of data_time / real_time
        rate = sum(rate.getData())
        print("efficiency: {:.1f}%, total rate: {:.1f} cps".format(efficiency, rate))


# Check the performance of the Coincidences separately for all the orders of permutations
all_groups = []
for order in range(min_order, max_order + 1):
    # `order` elements out of `len(channels)` elements
    groups = list(combinations(channels, order))
    all_groups += groups

    # Perform the Coincidences + Countrate measurement
    CountCoincidences(groups, order)

# Check the performance of the Coincidences for all the permutations at once
CountCoincidences(all_groups, "{}-{}".format(min_order, max_order))

# Close the connection to the Time Tagger
freeTimeTagger(tagger)
