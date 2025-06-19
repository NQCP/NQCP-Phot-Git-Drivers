"""A custom measurement that is supposed to provide the same result as Countrate.getTotalCounts().
This example is using numpy and does not require numba.
For an example using numba, have a look at '4-Custom-Measurements' -> CustomStartStop.py"""

import TimeTagger
import numpy as np


class CustomCount(TimeTagger.CustomMeasurement):
    """
    A simple CustomMeasurement that counts the events on each given channel.
    """

    def __init__(self, tagger, channels):
        TimeTagger.CustomMeasurement.__init__(self, tagger)
        self.channels = list(channels)
        self.counts = np.zeros((len(channels),), dtype=np.int32)

        # Each used channel must be registered
        for channel in channels:
            self.register_channel(channel)

        self.clear_impl()

        # At the end of a Measurement construction we must indicate that we
        # have finished
        self.finalize_init()

    def __del__(self):
        # The measurement must be stopped before deconstruction to avoid
        # concurrent measure() calls
        self.stop()

    def getData(self):
        # lock this instance to avoid conflicting results while measure is
        # running apart.
        with self.mutex:
            counts = np.array(self.counts)
        return counts

    def getIndex(self):
        # this method does not depend on the internal state, so there is no
        # need for a lock
        return list(self.channels)

    def clear_impl(self):
        # the lock is already acquired in the backend
        self.counts *= 0

    def on_start(self):
        # the lock is already acquired in the backend
        pass

    def on_stop(self):
        # the lock is already acquired in the backend
        pass

    def process(self, incoming_tags, begin_time, end_time):
        # the lock is already acquired in the backend
        # self.data is provided as reference, so it must not be accessed
        # anywhere else without locking the mutex.
        # incoming_tags is provided as a read-only reference. The storage is
        # deallocated after this call, so you must not store a reference to
        # this object. Make a copy instead.
        channel_numbers, counts = np.unique(incoming_tags["channel"], return_counts=True)
        for channel_number, count in zip(channel_numbers, counts):
            self.counts[self.channels.index(channel_number)] += count


if __name__ == '__main__':
    tagger = TimeTagger.createTimeTagger()

    tagger.setTestSignal(tagger.getChannelList(TimeTagger.ChannelEdge.Rising), True)
    sync = TimeTagger.SynchronizedMeasurements(tagger)

    custom_count = CustomCount(sync.getTagger(),
                               channels=[1, 2, 3, 4])
    countrate = TimeTagger.Countrate(sync.getTagger(),
                                     channels=[1, 2, 3, 4])

    sync.startFor(int(1E12))
    sync.waitUntilFinished()
    custom_data = custom_count.getData()
    standard_data = countrate.getCountsTotal()
    print("Custom measurement:", custom_data)
    print("Countrate:", countrate.getCountsTotal())
    if (custom_data == standard_data).all():
        print("Results are identical!")
    else:
        print("Results are not identical! Debugging is left as an exercise to the user :)")

    TimeTagger.freeTimeTagger(tagger)
