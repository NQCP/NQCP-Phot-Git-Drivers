"""
This script allows you to check your parameters.
"""
from json import load
import TimeTagger
from matplotlib import pyplot as plt
from pnr_constants import FRONT_EDGE, REAR_EDGE, LASER_CHANNEL, FOLDER, FILENAME

with open(FOLDER + "parameters.json", "rb") as param_file:
    parameters: dict = load(param_file)

ttv = TimeTagger.createTimeTaggerVirtual()
ttv.setReplaySpeed(-1)

# Only relevant if Virtual Channels are use in the calibration file
for i in range(3):
    x = TimeTagger.SyntheticSingleTag(ttv)

# Setup photon number resolution channel
pnr = TimeTagger.Experimental.PhotonNumber(tagger=ttv,
                                           trigger_ch=LASER_CHANNEL,
                                           signal_start_ch=FRONT_EDGE,
                                           signal_stop_ch=REAR_EDGE,
                                           slope=parameters["slope"],
                                           x_intercepts=parameters["x_intercepts"],
                                           dead_time=100_000)

delayed_channels = list()
gated_channels = list()
histograms = list()
for channel in pnr.getChannels()[1:]:
    delayed = TimeTagger.DelayedChannel(tagger=ttv,
                                        input_channel=channel,
                                        delay=-parameters["delay"])
    gated = TimeTagger.GatedChannel(tagger=ttv,
                                    input_channel=FRONT_EDGE,
                                    gate_start_channel=delayed.getChannel(),
                                    gate_stop_channel=channel)
    histograms.append(TimeTagger.Histogram(tagger=ttv,
                                           click_channel=gated.getChannel(),
                                           start_channel=delayed.getChannel(),
                                           binwidth=1,
                                           n_bins=1000))
    delayed_channels.append(delayed)
    gated_channels.append(gated)

ttv.replay(FOLDER + FILENAME)
ttv.waitForCompletion()

for hist in histograms:
    plt.plot(hist.getIndex(), hist.getData())
plt.title("Split photon peaks - does it make sense? :)")
plt.legend(["1 photon"] + [f"{i} photons" for i in range(2,
           len(pnr.getChannels())-1)] + [f"≥{len(pnr.getChannels())-1} photons"])
plt.show()
