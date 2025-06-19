from math import nan
import numpy as np
from time import sleep, perf_counter
from TimeTagger import ChannelEdge, CustomMeasurement, createTimeTagger, getVersion, freeTimeTagger


class TransferRate(CustomMeasurement):
    def __init__(self, tagger, channels):
        CustomMeasurement.__init__(self, tagger)

        for channel in channels:
            self.register_channel(channel)

        self.clear_impl()
        self.finalize_init()

    def __del__(self):
        self.stop()

    def getData(self):
        with self.mutex:
            return self.counter

    def getRate(self):
        with self.mutex:
            return nan if self.time_spend == 0 else self.counter / self.time_spend

    def clear_impl(self):
        # the lock is already acquired
        self.counter = 0
        self.time_spend = 0
        self.time_started = 0
        self.has_started = False

    def process(self, incoming_tags, begin_time, end_time):
        # the lock is already acquired
        now = perf_counter()

        if self.has_started:
            self.counter += incoming_tags.size
            self.time_spend += now - self.time_started

        self.has_started = True
        self.time_started = now


def probe_transfer_rate(tagger):
    [tagger.setTestSignal(i, False) for i in tagger.getChannelList()]
    [tagger.setInputDelay(i, 0) for i in tagger.getChannelList()]
    channels = tagger.getChannelList(ChannelEdge.Rising)[:3]

    tagger.setTestSignal(channels, True)

    min_rate = 10e6 if tagger.getModel() == 'Time Tagger 20' else 100e6
    default_divider = tagger.getTestSignalDivider()
    divider = int(default_divider * 800e3 / min_rate * len(channels))
    assert divider >= 1, "Test signal cannot reach the required data rate for the given number of channels."

    tagger.setTestSignalDivider(divider)

    time_integrate = 2  # s
    avgs = 10

    transfer_rate = TransferRate(tagger, channels)
    tagger.sync()
    tagger.clearOverflows()

    transfer_rates = np.zeros(avgs)

    for i in range(avgs):
        transfer_rate.clear()
        tagger.sync()
        sleep(time_integrate)
        transfer_rates[i] = transfer_rate.getRate()

    transfer_rates_sorted = np.sort(transfer_rates)

    overflows = tagger.getOverflows()

    if overflows == 0:
        print("WARNING - test signal input test signal rate too low.")

    # take the median as the data rate
    data = {'transfer_rate': transfer_rates_sorted[avgs//2],
            'transfer_rates': transfer_rates,
            'overflows': overflows,
            'channels': channels,
            }

    tagger.setTestSignalDivider(default_divider)
    return data


if __name__ == '__main__':
    print("Time Tagger Software Version {}".format(getVersion()))
    tagger = createTimeTagger()
    print("Model:    {}".format(tagger.getModel()))
    print("Serial:   {}".format(tagger.getSerial()))
    print("Hardware: {}".format(tagger.getPcbVersion()))
    try:
        import cpuinfo
        print("CPU:      {}".format(cpuinfo.get_cpu_info()['brand_raw']))
    except BaseException:
        print("\nINFO: Module cpuinfo not found - please install it via pip install py-cpuinfo to display the CPU information here.")

    print("\nTest Maximum transfer data rate with three active channels\n\nPlease wait...")
    result = probe_transfer_rate(tagger)
    print("\nMeasured transfer rates:")
    for i, rate in enumerate(result['transfer_rates']):
        print(
            "test run {:2d}: transfer rate {:.1f} MTags/s".format(i+1, rate/1e6))
    freeTimeTagger(tagger)
