"""This example demonstrates how to use the HighRes option.
It tells you which HighRes configurations are available and presents a test measurement.

A TimeDifferences measurement takes a series of histograms of the time difference of two channels.
Under some conditions, heating effects of the hardware may be observed."""

from matplotlib import pyplot as plt
import numpy as np
import TimeTagger


def get_delay_and_jitter(x, y):
    # Helper method to calculate the mean time difference of a histogram and the standard deviation.
    mean = np.ones([y.shape[0]]) * np.nan
    std = np.ones([y.shape[0]]) * np.nan
    for i, line in enumerate(y):
        if not any(line):
            break
        mean[i] = np.average(x, weights=line)
        std[i] = np.sqrt(np.average((x-mean[i])**2, weights=line))
    return mean, std


def select_channel(channel_name, options):
    # Asks the user for a channel number and removes it from the list of options
    while True:
        if len(options) == 1:
            option = options[0]
            options.remove(option)
            print("Will use channel {} as {}".format(option, channel_name))
            return option
        try:
            option = int(
                input("Select {} from {}: ".format(channel_name, options)))
            options.remove(option)
            return option
        except BaseException:
            pass


NUMBER_OF_HISTOGRAMS = 500


# Firstly, the user needs to select one of the HighRes modes.
# In the dictionary HIGHRES_MODES the modes are assigned to one of the letters.
HIGHRES_MODES = {
    "S": TimeTagger.Resolution.Standard,
    "A": TimeTagger.Resolution.HighResA,
    "B": TimeTagger.Resolution.HighResB,
    "C": TimeTagger.Resolution.HighResC
}

print("""There are four different resolution modes:
- Standard [S]
- HighResA [A]
- HighResB [B]
- HighResC [C]""")
while True:
    mode = str.capitalize(input("Pick one of the modes [S/A/B/C]: "))
    if mode in HIGHRES_MODES:
        try:
            tagger = TimeTagger.createTimeTagger(
                "", resolution=HIGHRES_MODES[mode])
            break
        except RuntimeError:
            print("HighRes mode 'HighRes{}' is not supported.".format(mode))

# You can retrieve a certain subset of channels by tagger.getChannelList by passing one of the attributes of TimeTagger.ChannelEdge.
# Here, we look at the "StandardRising" (rising edges of channels with Standard resolution) and "HighResRising" (rising edges of
# channels with the chosen HighRes mode)
standard_channels = list(tagger.getChannelList(
    TimeTagger.ChannelEdge.StandardRising))
highres_channels = list(tagger.getChannelList(
    TimeTagger.ChannelEdge.HighResRising))

# The user can select two HighRes channels if one of the HighRes modes is chosen, otherwise the Standard channels are used.
# The click_channel is delayed by 2.5 ns to ensure that it arrives after the start_channel.
click_channel = select_channel("click_channel",
                               highres_channels if highres_channels else standard_channels)
start_channel = select_channel("start_channel",
                               highres_channels if highres_channels else standard_channels)
tagger.setInputDelay(click_channel, 2500)

# For the TimeDifferences measurement, we pick a next_channel. This shifts the measurement to the next histogram.
# We use one of the unused channels and let pass only one out of 40,000 clicks through the EventDivider.
next_channel = standard_channels[-1] if standard_channels else highres_channels[-1]
tagger.setEventDivider(next_channel, 40000)

# The TimeDifferences measurement is set up with a set of NUMBER_OF_HISTOGRAMS histograms, each of them providing 5000 temporal bins
# with a width of 1 ps. 5000 bins are actually more than enough, but the high number of bins ensures that the measurement span
# covers the specific delay of the internal test signal.
# The measurement collects the time differences of click_channel and start_channel into a histogram.
# The next_channel shifts the measurement to the next histogram. We limit this to a single run through all
# histograms by .setMaxCounts(1), so the measurement does not acquire additional data after the first rollover.
diff = TimeTagger.TimeDifferences(tagger=tagger,
                                  click_channel=click_channel,
                                  start_channel=start_channel,
                                  next_channel=next_channel,
                                  binwidth=1,
                                  n_bins=5000,
                                  n_histograms=NUMBER_OF_HISTOGRAMS)
diff.setMaxCounts(1)

# The internal test signal is enabled for the chosen channels.
tagger.setTestSignal([click_channel, start_channel, next_channel], True)

# The plot is steadily updated until diff.ready() returns True. After that, it plots a final image.
fig = plt.figure("Time Differences")
final = False
section = 100 if tagger.getModel() == "Time Tagger 20" else 20
while True:
    # By diff.getData(), we retrieve the set of histograms, and by diff.getIndex() the temporal position of the bins.
    # The mean value and the standard deviation are calculated and the bins around the maximum of the first histogram
    # are displayed.
    data = diff.getData()
    index = diff.getIndex()
    mean, std = get_delay_and_jitter(index, data)
    if np.isnan(mean[0]):
        plt.pause(.1)
        continue
    new_index = index - mean[0]
    mean_index = int(mean[0])
    fig.clear()
    plt.title("TimeDifferences with click_channel={}, start_channel={}".format(
        click_channel, start_channel))
    plt.imshow(data[:, (mean_index-section):(mean_index+section)],
               aspect="auto",
               extent=(new_index[mean_index-section], new_index[mean_index+section], 499, 0))
    new_mean = mean-mean_index

    # The blue line indicates the mean value of the histogram relative to the mean value of the first histogram.
    # The white lines indicate the 2-channel RMS jitter.
    plt.plot(new_mean, np.arange(NUMBER_OF_HISTOGRAMS), "b", label="Mean")
    plt.plot(new_mean + std, np.arange(NUMBER_OF_HISTOGRAMS),
             "w", label="RMS jitter")
    plt.plot(new_mean - std, np.arange(NUMBER_OF_HISTOGRAMS), "w")
    plt.legend()
    plt.xlabel("Time difference (ps)")
    plt.ylabel("Histogram index")
    plt.gca().invert_yaxis()
    if final:
        break
    if diff.ready():
        final = True
        continue
    plt.pause(.05)
plt.show()

TimeTagger.freeTimeTagger(tagger)
