"""
This example demonstrates the advanced normalization feature of the HistogramLogBins class.
Simulated Dynamic Light Scattering (DLS) data are polluted by intense bursts that would destroy
the DLS measurement. The bursts are simulated as time ranges of high homogeneous count rate.
The bursts are detected based on the total count rate.
"""

import TimeTagger
from matplotlib import pyplot as plt

TOC_WINDOW = 100_000_000
TOC_COUNTRATE = 1e7
GATE_EXTRA_TIME = 1_000_000_000

MEASUREMENT_DURATION = 5_000_000_000_000

# Settings for bursts
BURST_DURATION = 1e-3   # in s
BURST_EVENT_RATE = 3e7  # in counts / s
BURST_RATE = 2.0        # in Hz

# Settings for HistogramLogBins
EXP_START = -6
EXP_STOP = 0
N_BINS = 300

# Settings for DLS simulator
DECAY_TIME = 1e-3         # in s
DLS_EVENT_RATE = 1e6      # in counts / s

# Some constants for plotting
COLOR_ORIGINAL = "C0"
COLOR_DIRTY = "r"
COLOR_FILTERED = "g"
COLOR_GATED = "k"

ttv = TimeTagger.createTimeTaggerVirtual()
ttv.setReplaySpeed(1)
sync = TimeTagger.SynchronizedMeasurements(ttv)

# Bursts are placed by a simulator and injected by the MarkovProcessGenerator
bursts = TimeTagger.Experimental.MarkovProcessGenerator(
    tagger=sync.getTagger(),
    num_states=2,
    frequencies=[
        0,                   # no events in state "no bursts"
        BURST_RATE,          # rate of switching to bursts state
        1 / BURST_DURATION,  # rate of switching to "no bursts" state
        BURST_EVENT_RATE     # rate of events within burst state
    ],
    ref_channels=[TimeTagger.CHANNEL_UNUSED, 0, 1, 2],
    base_channels=[TimeTagger.CHANNEL_UNUSED] * 3
)
bursts_start_ch, bursts_stop_ch, bursts_event_ch = bursts.getChannels()

# We use a simulator to generate the time-tags for the pure DLS curve
dls_original = TimeTagger.Experimental.DlsSignalGenerator(sync.getTagger(),
                                                          DECAY_TIME,
                                                          DLS_EVENT_RATE)
dls_dirty = TimeTagger.Combiner(tagger=sync.getTagger(),
                                channels=[bursts_event_ch, dls_original.getChannel()])

# We detect the burst by the TriggerOnCountrate class.
# The toggle events (off_trigger and on_trigger) will be put at a defined delay outside the burst area.
toc = TimeTagger.TriggerOnCountrate(tagger=sync.getTagger(),
                                    input_channel=dls_dirty.getChannel(),
                                    reference_countrate=TOC_COUNTRATE,
                                    hysteresis=1e6,
                                    time_window=1e12 * BURST_DURATION / 10)
off_trigger = TimeTagger.DelayedChannel(tagger=sync.getTagger(),
                                        input_channel=toc.getChannelAbove(),
                                        delay=-GATE_EXTRA_TIME)
on_trigger = TimeTagger.DelayedChannel(tagger=sync.getTagger(),
                                       input_channel=toc.getChannelBelow(),
                                       delay=GATE_EXTRA_TIME)

gated = TimeTagger.GatedChannel(tagger=sync.getTagger(),
                                input_channel=dls_dirty.getChannel(),
                                gate_start_channel=on_trigger.getChannel(),
                                gate_stop_channel=off_trigger.getChannel())

# With that, we can set up the histograms:
# 1. The dirty histogram that you would measure in your real-world experiment
hist_dirty = TimeTagger.HistogramLogBins(tagger=sync.getTagger(),
                                         click_channel=dls_dirty.getChannel(),
                                         start_channel=dls_dirty.getChannel(),
                                         exp_start=EXP_START,
                                         exp_stop=EXP_STOP,
                                         n_bins=N_BINS)
# 2. The pure DLS signal that you would expect in an ideal-world experiment
hist_original = TimeTagger.HistogramLogBins(tagger=sync.getTagger(),
                                            click_channel=dls_original.getChannel(),
                                            start_channel=dls_original.getChannel(),
                                            exp_start=EXP_START,
                                            exp_stop=EXP_STOP,
                                            n_bins=N_BINS)
# 3. The gated version that cuts out the burst events but does not care about proper normalization
hist_gated = TimeTagger.HistogramLogBins(tagger=sync.getTagger(),
                                         click_channel=gated.getChannel(),
                                         start_channel=gated.getChannel(),
                                         exp_start=EXP_START,
                                         exp_stop=EXP_STOP,
                                         n_bins=N_BINS)
# 4. The internally gated one that makes HistogramLogBins taking care of the proper normalization
channel_gate = TimeTagger.ChannelGate(gate_open_channel=on_trigger.getChannel(),
                                      gate_close_channel=off_trigger.getChannel(),
                                      initial=TimeTagger.GatedChannelInitial.Closed)
hist_filtered = TimeTagger.HistogramLogBins(tagger=sync.getTagger(),
                                            click_channel=dls_dirty.getChannel(),
                                            start_channel=dls_dirty.getChannel(),
                                            exp_start=EXP_START,
                                            exp_stop=EXP_STOP,
                                            n_bins=N_BINS,
                                            click_gate=channel_gate,
                                            start_gate=channel_gate)

# Additionally, we add some analysis and visualization measurements
counter = TimeTagger.Counter(tagger=sync.getTagger(),
                             channels=[dls_dirty.getChannel(),
                                       gated.getChannel(),
                                       dls_original.getChannel()],
                             binwidth=TOC_WINDOW,
                             n_values=MEASUREMENT_DURATION//TOC_WINDOW)
counter_triggers = TimeTagger.Counter(tagger=sync.getTagger(),
                                      channels=[bursts_start_ch,
                                                bursts_stop_ch,
                                                on_trigger.getChannel(),
                                                off_trigger.getChannel()],
                                      binwidth=TOC_WINDOW,
                                      n_values=MEASUREMENT_DURATION//TOC_WINDOW)

# We need to run a little bit of time before we start the real measurement.
# Without this, the negative delays applied above would cause that the actual start of the simulation is within the measurement period.
sync.startFor(GATE_EXTRA_TIME)
sync.waitUntilFinished()

# The measurements are cleared and the real measurement can start
sync.startFor(5e12)

# Wait for any data before plotting any results
ttv.sync()

f = plt.subplots(2, 2, figsize=(15, 10))
axis_histograms = plt.subplot(2, 2, 1)
axis_histograms_normalized = plt.subplot(2, 2, 3)
axis_counters = plt.subplot(2, 2, 2)
axis_triggers = plt.subplot(2, 2, 4)


def plot_histogram(histogram: TimeTagger.HistogramLogBins, color):
    """Helper function to plot the histograms"""
    data = histogram.getDataObject()
    data_norm = hist_original.getDataObject()
    axis_histograms.semilogx(1e-12 * (histogram.getBinEdges()[:-1] + histogram.getBinEdges()[1:]) / 2,
                             data.getG2(),
                             color=color)
    axis_histograms_normalized.semilogx(1e-12 * (histogram.getBinEdges()[:-1] + histogram.getBinEdges()[1:]) / 2,
                                        data.getG2() / data_norm.getG2(),
                                        color=color)


running = True
while running:
    plt.pause(0.1)
    running = sync.isRunning()
    [axis.clear() for axis in (axis_histograms,
                               axis_histograms_normalized, axis_counters, axis_triggers)]
    for line, color in zip(counter.getData()/(TOC_WINDOW/1E12), [COLOR_DIRTY, COLOR_GATED, COLOR_ORIGINAL]):
        axis_counters.plot(1e-12 * counter.getIndex(), line, color=color)
    for line in counter_triggers.getData():
        axis_triggers.plot(1e-12 * counter_triggers.getIndex(), line)
    plot_histogram(hist_original, COLOR_ORIGINAL)
    plot_histogram(hist_dirty, COLOR_DIRTY)
    plot_histogram(hist_gated, COLOR_GATED)
    plot_histogram(hist_filtered, COLOR_FILTERED)
    axis_histograms.set_xlabel("Time (s)")
    axis_histograms.set_ylabel("$g^{(2)}$")
    axis_histograms.legend(("Original", "Dirty", "Gated", "Filtered"))
    axis_histograms_normalized.set_xlabel("Time (s)")
    axis_histograms_normalized.set_ylabel("$g^{(2)}$ normalized to ideal")
    axis_histograms_normalized.set_ybound(0.99, 1.01)
    axis_histograms_normalized.legend(("Ideal", "Dirty", "Gated", "Filtered"))
    axis_counters.set_xlabel("Time (s)")
    axis_counters.set_ylabel("Counts/s")
    axis_counters.legend(("Dirty", "Gated", "Original"))
    axis_counters.hlines(y=TOC_COUNTRATE, xmin=0,
                         xmax=1e-12 * MEASUREMENT_DURATION,
                         color="r", linestyles="dotted")
    axis_triggers.set_xlabel("Time (s)")
    axis_triggers.set_ylabel("Trigger event counts")
    axis_triggers.legend(
        ("Burst start trigger", "Burst stop trigger", "Open gate", "Close gate"))
axis_histograms_normalized.sharex(axis_histograms)
axis_triggers.sharex(axis_counters)
TimeTagger.freeTimeTagger(ttv)
plt.show()
