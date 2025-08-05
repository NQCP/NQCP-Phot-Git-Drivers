import TimeTagger
from custom_pnr_constants import FRONT_EDGE, REAR_EDGE, LASER_CHANNEL, FOLDER, FILENAME, CALIBRATION_FILES
from json import load
import numba
import numpy as np
import os


class CustomPNRMultichannel(TimeTagger.CustomMeasurement):
    """
    Custom measurement to perform photon number resolution on multiple detectors simultaneously using one common trigger signal.
    Input parameters, i.e., trigger and detector channels, are imported from an external file named custom_pnr_constants.py. 
    The data can be accessed using the getData() module. The output is a numpy array with one row for each time tag and a column for each detector, storing the number of detected photons.
    """

    def __init__(self, tagger, trigger_ch, pnr_channels, n_detectors, n_channels, buffer_size):
        TimeTagger.CustomMeasurement.__init__(self, tagger)
        self.trigger_ch = trigger_ch
        self.pnr_channels = pnr_channels
        self.n_detectors = n_detectors
        self.n_channels = n_channels
        self.buffer_size = int(buffer_size)

        # Channels that will be transferred from the TT to the PC
        self.register_channel(channel=trigger_ch)
        for pnr_channel in np.nditer(pnr_channels):
            self.register_channel(channel=pnr_channel)

        self.clear_impl()

        self.finalize_init()

    def __del__(self):
        # The measurement must be stopped before deconstruction to avoid
        # concurrent process() calls.
        self.stop()

    def getData(self):
        # Acquire a lock this instance to guarantee that process() is not running in parallel
        # This ensures to return a consistent data.
        with self.mutex:
            # Check if there are new data. if not return an array of -1
            if self.index == self.read_index:
                return np.zeros((0, self.n_detectors), dtype=np.int8)
            else:
                if not self.state['is_ring_full']:
                    data = self.data[self.read_index:self.index].copy()
                    self.read_index = self.index
                else:
                    data = np.concatenate(
                        (self.data[self.index:], self.data[self.read_index:self.index]))
                    self.read_index = self.index
            return data

    def clear_impl(self):
        # The lock is already acquired within the backend.
        self.data = np.full(
            (self.buffer_size, self.n_detectors), fill_value=-1, dtype=np.int8)
        self.index = 0
        self.read_index = 0
        self.timestamp = 0
        self.state = np.array([(False, False)], dtype=[
                              ('has_laser', bool), ('is_ring_full', bool)])

    def on_start(self):
        # The lock is already acquired within the backend.
        pass

    def on_stop(self):
        # The lock is already acquired within the backend.
        pass

    @staticmethod
    @numba.jit(nopython=True, nogil=True)
    def fast_process(
            tags,
            timestamp,
            data,
            trigger_ch,
            pnr_channels,
            n_detectors,
            n_channels,
            index,
            read_index,
            buffer,
            state):
        data[0][:] = -1
        for tag in tags:
            # print(tag['type'], tag['time'], tag['channel'])
            # tag.type can be: 0 - TimeTag, 1- Error, 2 - OverflowBegin, 3 -
            # OverflowEnd, 4 - MissedEvents (you can use the TimeTagger.TagType IntEnum)
            if tag['type'] != TimeTagger.TagType.TimeTag:
                # tag is not a TimeTag, so we are in an error state, e.g. overflow
                continue
            elif tag['channel'] == trigger_ch:
                if timestamp == 0:
                    # This is a new timestamp. It starts a new event
                    timestamp = tag['time']
                    state[0]['has_laser'] = True
                elif timestamp == tag['time']:
                    # It is still the same event
                    if state[0]['has_laser']:
                        # This is a sanity check. There shouldn't be two laser events with the same timestamp
                        raise RuntimeError(
                            'Two Laser events with the same timestamp')
                    else:
                        state[0]['has_laser'] = True
                else:
                    # This is a new timestamp. Check if the laser was missing and in case keep the same index
                    if not state[0]['has_laser']:
                        pass
                    # Otherwise increase the index by one
                    else:
                        # First check if the buffer will be exceeded by doing it and data will be lost
                        if (index + 1 == read_index) or (index + 1 == buffer and read_index == 0):
                            raise RuntimeError(
                                'Buffer exceeded! Please increase the buffer, or call getData() more ofter')
                        # If there is still space, increase the index
                        index += 1
                        # Check if ring is full, and in case start from the beginning. Data in the first rows were saved already
                        if index == buffer:
                            index = 0
                            state[0]['is_ring_full'] = True
                    # assign the new time stamp
                    timestamp = tag['time']
                    state[0]['has_laser'] = True
            else:
                idx = 0
                for detector_index in range(n_detectors):
                    for channel_index in range(n_channels[detector_index]):
                        if tag['channel'] == pnr_channels[idx]:
                            if timestamp == 0:
                                # This is a new timestamp. It starts a new event
                                timestamp = tag['time']
                                #  And write the number of photons in the right column
                                data[index][detector_index] = channel_index
                            elif timestamp == tag['time']:
                                # It is still the same event. Write the number of photons in the right column
                                data[index][detector_index] = channel_index
                            else:
                                # This is a new event. Check if the laser was missing and in case keep the same index
                                if not state[0]['has_laser']:
                                    pass
                                # Otherwise increase the index by one checking if it fills the buffer
                                else:
                                    # First check if the buffer will be exceeded by doing it and data will be lost
                                    if (index + 1 == read_index) or (index + 1 == buffer and read_index == 0):
                                        raise RuntimeError(
                                            'Buffer exceeded! Please increase the buffer, or call getData() more ofter')
                                    # If there is still space, increase the index
                                    index += 1
                                    # Check if ring is full, and in case start from the beginning. Data in the first rows were saved already
                                    if index == buffer:
                                        index = 0
                                        state[0]['is_ring_full'] = True
                                # Assign the new time stamp
                                timestamp = tag['time']
                                # Set the laser state to false
                                state[0]['has_laser'] = False
                                # And write the number of photons in the right column
                                data[index][detector_index] = channel_index
                        idx += 1
        return index, read_index

    def process(self, incoming_tags, begin_time, end_time):
        self.index, self.read_index = CustomPNRMultichannel.fast_process(
            incoming_tags,
            self.timestamp,
            self.data,
            self.trigger_ch,
            self.pnr_channels,
            self.n_detectors,
            self.n_channels,
            self.index,
            self.read_index,
            self.buffer_size,
            self.state)


# Buffer size
BUFFER_SIZE = 1e6

if __name__ == '__main__':

    print("""Custom multichannel PNR measurement

""")

    if FRONT_EDGE and REAR_EDGE:
        if len(FRONT_EDGE) != len(REAR_EDGE):
            raise ValueError('The number of FRONT_EDGE and REAR_EDGE should be the same. There were given in input {} FRONT and {} REAR edges'.format(
                len(FRONT_EDGE), len(REAR_EDGE)))
        else:
            n_detectors = len(FRONT_EDGE)
    else:
        raise RuntimeError('FRONT and/or REAR edges not found')

    if len(CALIBRATION_FILES) != n_detectors:
        raise RuntimeError('{} calibration files given with {} detectors. Exactly one calibration file for each detector is needed.'.format(
            len(CALIBRATION_FILES), n_detectors))

    parameters: list[dict] = []
    n_channels = np.zeros((n_detectors), dtype=np.int8)
    # Looping over all calibration files
    for i, calib_file in enumerate(CALIBRATION_FILES):
        # if no absolute path is given, it assumed the calibration files to be in the same folder as the time tags data
        if os.path.basename(calib_file) == '':
            with open(FOLDER + calib_file, "rb") as param_file:
                parameters[i] = load(param_file)
        else:
            with open(FOLDER + calib_file, "rb") as param_file:
                parameters[i] = load(param_file)
        n_channels[i] = len(parameters[i]["x_intercepts"])

    ttv = TimeTagger.createTimeTaggerVirtual()
    ttv.setReplaySpeed(-1)

    pnr_measurements = []
    pnr_channels = np.empty(0, np.sum(n_channels))

    for i in range(n_detectors):

        print(i, parameters[i]["x_intercepts"])

        pnr_measurements.append(TimeTagger.Experimental.PhotonNumber(tagger=ttv,
                                                                     trigger_ch=LASER_CHANNEL,
                                                                     signal_start_ch=FRONT_EDGE[i],
                                                                     signal_stop_ch=REAR_EDGE[i],
                                                                     slope=parameters[i]["slope"],
                                                                     x_intercepts=parameters[i]["x_intercepts"],
                                                                     dead_time=100_000))
        pnr_channels = np.append(
            pnr_channels, pnr_measurements[i].getChannels())

    print(pnr_channels)

    multipnr = CustomPNRMultichannel(
        ttv, LASER_CHANNEL, pnr_channels, n_detectors, n_channels, BUFFER_SIZE)

    ttv.replay(FOLDER + FILENAME)

    with open('pnr_counts.txt', 'w') as f:
        while not ttv.waitForCompletion(timeout=1):
            np.savetxt(f, multipnr.getData(), fmt="%s")
