"""
Merge Time Tag Stream files recorded separately from two Time Taggers.

This example records two time tag stream files, one for channels 1 and 2 and another for channels 3 and 4.
Later these separate stream files are combined into one to calculate the correlation between channels 1 and 3.
The file merger is combining the streams. The user can specify a constant time offset for each stream
as well as the channel number offset.

"""

from TimeTagger import (createTimeTagger, createTimeTaggerVirtual, mergeStreamFiles,
                        FileWriter, SynchronizedMeasurements, Correlation)
import matplotlib.pyplot as plt

MAKE_TESTDATA = True
MERGE_DUMPS = True
REPLAY_MERGE = True

# Create test data
if MAKE_TESTDATA:
    with createTimeTagger() as t:
        t.setTestSignal([1, 2, 3, 4], True)
        with SynchronizedMeasurements(t) as sm:
            fw12 = FileWriter(sm.getTagger(), 'dump12.ttbin', [1, 2])
            fw34 = FileWriter(sm.getTagger(), 'dump34.ttbin', [3, 4])
            sm.startFor(5e12)
            sm.waitUntilFinished()


if MERGE_DUMPS:
    # Merges multiple *.ttbin files into one.
    # You can specify channel number offsets to separate channels if dumps were recorded using the same channel numbers
    # You can specify a constant time offset for each ttbin file.
    mergeStreamFiles(
        output_filename='dump1234_merged.ttbin',            # Filename of the output ttbin file
        input_filenames=['dump12.ttbin', 'dump34.ttbin'],   # List of dump files that will be merged
        channel_offsets=[0, 0],     # Channel number offset for each ttbin file. Useful when dumps have the same channel numbers.
        time_offsets=[0, 1000],     # Time offset for each ttbin file in picoseconds.
        overlap_only=True,          # If True, then merge only the regions where the time is overlapping.
    )


if REPLAY_MERGE:
    # Uses merged file and calculates correlation for the channels 1&3
    # that were originally in different dump files, and also for channels 1&2.
    with createTimeTaggerVirtual() as ttv:
        cor12 = Correlation(ttv, 1, 2, binwidth=10, n_bins=3000)
        cor13 = Correlation(ttv, 1, 3, binwidth=10, n_bins=3000)

        ttv.replay('dump1234_merged.ttbin')
        ttv.waitForCompletion()

    plt.plot(cor12.getIndex(), cor12.getData(), label='1 vs 2')
    plt.plot(cor13.getIndex(), cor13.getData(), label='1 vs 3')
    plt.xlabel('Time (ps)')
    plt.ylabel('Counts/bin')
    plt.legend()

    plt.show()
