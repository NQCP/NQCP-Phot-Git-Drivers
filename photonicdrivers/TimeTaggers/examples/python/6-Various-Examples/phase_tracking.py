"""
Track phase of multiple signals and write it to a CSV file
"""

import TimeTagger
from pathlib import Path
from datetime import datetime
import numpy
from time import sleep

# General parameters
USE_TESTSIGNAL = True
USE_AVERAGING = False  # Activate this for better performance on the Time Tagger X
REFERENCE_CHANNEL = 1
EXT_FREQUENCY = 10E6
CHANNELS = [2]
SAMPLING_INTERVAL = 1_000_000_000
FITTING_WINDOW = 1_000_000_000
MEASUREMENT_TIME = 500_000_000_000
DATA_FOLDER = "_data"

# Control which data to write
WRITE_PHASE = True           # Amount of past fractional periods up to this window
WRITE_FREQUENCY = True       # The fitted frequency within this window
WRITE_RELATIVE_PHASE = True  # Amount of past fractional periods minus the nominal frequency

folder = Path(DATA_FOLDER)
delete_folder = False
if not folder.exists():
    folder.mkdir()
    delete_folder = True
filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.txt")

# Tagger configuration
tagger = TimeTagger.createTimeTagger()
channels = list(CHANNELS)
if REFERENCE_CHANNEL:
    channels.append(REFERENCE_CHANNEL)
frequency = EXT_FREQUENCY
if USE_TESTSIGNAL:
    tagger.setTestSignal(channels, True)

    # As the test signal varies between Time Tagger models, we measure its frequency
    countrate = TimeTagger.Countrate(tagger, channels)
    countrate.startFor(100_000_000_000)
    countrate.waitUntilFinished()
    frequency_measured = numpy.average(countrate.getData())
    frequency = round(frequency_measured/1000)*1000
    print(
        f"The test signal frequency is {frequency_measured} Hz, the nominal frequency is rounded to {frequency}")
if USE_AVERAGING:
    # Averaging requires rising and falling edges to be placed within a certain window,
    # so we need to measure the duty cycle and to shift the inverted edge
    sync = TimeTagger.SynchronizedMeasurements(tagger)
    measurements = {
        channel: TimeTagger.Histogram(
            sync.getTagger(),
            click_channel=channel,
            start_channel=-channel,
            binwidth=100,
            n_bins=round(1E12/frequency/100),
        )
        for channel in channels
    }
    sync.startFor(1E12)
    sync.waitUntilFinished()
    for channel, hist in measurements.items():
        index = numpy.argmax(hist.getData())
        tagger.setDelayHardware(-channel, hist.getIndex()[index])
        tagger.xtra_setAvgRisingFalling(channel, True)
if REFERENCE_CHANNEL:
    tagger.setSoftwareClock(REFERENCE_CHANNEL, frequency,
                            averaging_periods=10 if USE_TESTSIGNAL else 10000)

# The actual data acquisition
with open(folder / filename, "w") as datafile:
    freq_count = TimeTagger.FrequencyCounter(
        tagger, CHANNELS, SAMPLING_INTERVAL, FITTING_WINDOW)
    freq_count.startFor(MEASUREMENT_TIME)

    # Writing the column headers
    header = ["\"Index\""]
    if WRITE_PHASE:
        header += [f"\"Phase {channel}\"" for channel in CHANNELS]
    if WRITE_FREQUENCY:
        header += [f"\"Frequency {channel}\"" for channel in CHANNELS]
    if WRITE_RELATIVE_PHASE:
        header += [
            f"\"Rel. phase ({frequency * 1e-3} kHz) {channel}\"" for channel in CHANNELS]
    datafile.write(",".join(header) + "\n")

    # Writing data
    running = True
    while running:
        sleep(0.01)
        running = freq_count.isRunning()
        data = freq_count.getDataObject(remove=True, channels_last_dim=True)
        if data.size:
            lines = str()
            for index, counts, fractions, phases, frequencies, overflows in zip(data.getIndex(), data.getPeriodsCount(), data.getPeriodsFraction(), data.getPhase(frequency), data.getFrequencyInstantaneous(), data.getOverflowMask()):
                line = [str(index)]
                if WRITE_PHASE:
                    for ct, fr, overflow in zip(counts, fractions, overflows):
                        line.append(
                            "NaN" if overflow else f"{ct}.{(int(fr*1E9)):09}")
                if WRITE_FREQUENCY:
                    for freq, overflow in zip(frequencies, overflows):
                        line.append("NaN" if overflow else str(freq))
                if WRITE_RELATIVE_PHASE:
                    for phase, overflow in zip(phases, overflows):
                        line.append("NaN" if overflow else str(phase))
                lines += ",".join(line) + "\n"
            datafile.write(lines)
            datafile.flush()

# Close the connection to the Time Tagger
TimeTagger.freeTimeTagger(tagger)

# Remove created files and folders after giving the opportunity to study them
input("Press Enter to remove data")
Path(folder/filename).unlink()
if delete_folder:
    folder.rmdir()
