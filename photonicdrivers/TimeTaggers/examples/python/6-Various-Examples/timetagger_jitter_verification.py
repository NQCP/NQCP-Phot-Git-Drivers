"""In this example, we measure the jitter/resolution of the Time Tagger channels with the built-in test signals
and compare the results to the specifications of the Time Tagger, which is connected.
"""
import TimeTagger
import numpy as np
import matplotlib.pyplot as plt
import time
from typing import Dict


def gaussian(x, mu, sigma, A):
    """Scaled Gaussian function for visual comparison of the measured data"""
    return A/(np.sqrt(2*np.pi)*sigma)*np.exp(-0.5*(x-mu)**2/sigma**2)


def synchronized_correlation_measurement(tagger, channels, binwidth=1, bins=int(5e5), duration=int(15e12)):
    """
    For the jitter measurement, we use correlation measurements of the periodic built-in test signal.
    The function initializes multiple correlation measurements between channels.
    To have a simultaneous start, we make use of the Synchronized Measurement class.
    Returns correlation histogram data for each channel combination.
    """
    correlation_measurements = {}
    # Here we use a single channel, which is correlated to all other channels.
    start_channel = channels[0]
    # Use helper class to synchronize measurements
    with TimeTagger.SynchronizedMeasurements(tagger) as sync_meas:
        for stop_channel in channels:
            # When using Synchronizer, correlate only channels within the same device
            if stop_channel - start_channel >= 100:
                start_channel = stop_channel

            # Do not correlate the channel against itself
            if start_channel == stop_channel:
                continue

            corr_channels = (start_channel, stop_channel)
            # Initiate the measurements and register them for the synchronized measurements
            corr = TimeTagger.Correlation(sync_meas.getTagger(), start_channel, stop_channel, binwidth, bins)
            correlation_measurements[corr_channels] = corr

        # Start all measurements simultaneously
        sync_meas.startFor(duration)
        sync_meas.waitUntilFinished()

        # Collect correlation results
        corr_histograms = {}
        for corr_channels, corr in correlation_measurements.items():
            corr_histograms[corr_channels] = (corr.getIndex(), corr.getData())
    return corr_histograms


def warmup(tagger, duration=int(30e12)):
    """
    Function to warm up the Time Tagger until temperatures are stable.
    """
    all_channels = tagger.getChannelList(TimeTagger.ChannelEdge.Rising)
    tagger.setTestSignal(all_channels, True)
    # Create load on all channels to warm up the Time Tagger
    countrate = TimeTagger.Countrate(tagger, all_channels)
    if tagger.getModel() == "Time Tagger 20" or tagger.getSensorData()[0]['FPGA board']['FPGA Temp'] == 0.0:
        warmup_time = duration/1e12
        print("Warming up ... ", end=' ')
        while warmup_time > 0:
            print(f'{warmup_time:0.0f}', end=' ')
            time.sleep(2)
            warmup_time -= 2
        print("Done.")
    else:
        print("For the Time Tagger Ultra and Time Tagger X, we can check for stable temperatures on the board.")
        warmed_up = False
        cnt = 0
        while not warmed_up:
            pcb_temperatures = []
            fpga_temperatures = []
            # Measure 5 times, then check whether the temperatures on the board have been stable. If not, repeat.
            for i in range(5):
                time.sleep(1)
                cnt = cnt + 1
                sensor_data = tagger.getSensorData()
                pcb = sensor_data[0]['FPGA board']['Board Temp #1']
                fpga = sensor_data[0]['FPGA board']['FPGA Temp']
                pcb_temperatures.append(pcb)
                fpga_temperatures.append(fpga)
                print(f"t: {cnt:3d} s, Board temperature: {pcb:2.1f} °C, FPGA temperature: {fpga:2.1f} °C")
            if (np.ptp(pcb_temperatures) < 1) and (np.ptp(fpga_temperatures) < 1.5):
                warmed_up = True
                print("The Time Tagger is warmed up.")
                print("")
            else:
                print("The Time Tagger is not yet warmed up.")
    del countrate


def get_jitter_and_delay(hist_t, hist_c):
    """
    Calculate RMS jitter and mean (giving the internal delay of the test signal to later shift the plots)
    """
    mean_t = np.average(hist_t, weights=hist_c)
    jitter_rms = np.sqrt(np.average((hist_t-mean_t)**2, weights=hist_c))
    return jitter_rms, mean_t


# Searching for available Time Taggers
serials = TimeTagger.scanTimeTagger()
print(f'Found {len(serials)} connected Time Tagger(s)')

# Connect to the Time Tagger and collect device information.
# Please specify the serial number explicitly in case more than one device is connected
# and not already taken care of by a synchronizer.
tagger = TimeTagger.createTimeTagger(serial='')
serial = tagger.getSerial()
model = tagger.getModel()
lic_info = tagger.getDeviceLicense()
edition = lic_info['edition']

resolution_modes = ['Standard']
if edition == 'HighRes':
    if model == 'Time Tagger Ultra':
        resolution_modes.extend(['HighResA', 'HighResB', 'HighResC'])
    elif model == 'Time Tagger X':
        resolution_modes.append('HighResB')
    else:
        raise ValueError('Unknown combination of model and edition!')

print('Time Tagger info: ')
print(' Serial:          ', serial)
print(' Model:           ', model)
print(' Edition:         ', edition)
print(' Resolution modes:', ', '.join(resolution_modes))

if model not in ['Time Tagger 20', 'Time Tagger Ultra', 'Time Tagger X']:
    raise ValueError(f'Currently {model} is not supported by this example script')

time.sleep(0.5)
print('Warming up the Time Tagger to get an accurate jitter measurement.')
warmup(tagger)

# Storing our data in dictionaries to account for the different modes of the HighRes option.
measured_jitters: Dict[str, list] = {}
within_specs: Dict[str, list] = {}
measured_channels: Dict[str, list] = {}
spec_jitter_label = 'Spec. typical jitter'
specified_jitter_rms = {}

# We loop over the different HighRes modes, if available. Or only use the single available mode.
for i, mode in enumerate(resolution_modes):
    measured_jitters[mode] = []
    within_specs[mode] = []
    measured_channels[mode] = []

    print(f'Operating the Time Tagger in {mode} resolution mode')
    # To change the resolution mode, first, we need to disconnect the Time Tagger
    TimeTagger.freeTimeTagger(tagger)
    resolution = getattr(TimeTagger.Resolution, mode)  # get enum value
    tagger = TimeTagger.createTimeTagger(serial=serial, resolution=resolution)

    assert isinstance(tagger, TimeTagger.TimeTagger)

    # Retrieve rms resolution value from the first channel (a constant value from device specifications)
    # Determine channel resolutions specification from the device
    tagger_configuration = tagger.getConfiguration()
    input_cfg = tagger_configuration['inputs'][0]
    specified_jitter_rms[mode] = input_cfg['resolution rms']

    if mode == 'Standard':
        available_inputs = tagger.getChannelList(TimeTagger.ChannelEdge.Rising)
    else:
        # Measure only on HighRes channels
        available_inputs = tagger.getChannelList(TimeTagger.ChannelEdge.HighResRising)

    print(' Available inputs:', available_inputs)

    # Enable test signals on the available inputs
    tagger.setTestSignal(available_inputs, True)

    print('Measuring for 30 seconds...')
    # Retrieving the measured data
    correlation_data = synchronized_correlation_measurement(tagger, available_inputs, duration=int(30e12))

    print('Measurement complete.\nNow evaluating the data')
    time.sleep(1)

    fig, ax = plt.subplots()  # Create a plot to visualize the TWO channel jitter
    ax.set_title('Visual comparison of the measured two-channel jitters to specifications')
    ax.set_xlabel('Time (ps)')
    ax.set_ylabel('kCounts')
    # Looping over the measurement data, evaluating the single channel RMS jitter from it and displaying the results
    # For the visual comparison a Gaussian with standard deviation = sqrt(2)*specified_RMS_jitter is used
    # since we look at the two-channel jitter
    for corr_channels, (hist_t, hist_c) in correlation_data.items():
        start_channel, stop_channel = corr_channels
        rms_t, mean_t = get_jitter_and_delay(hist_t, hist_c)
        jitter_measured = rms_t / np.sqrt(2)  # per channel jitter

        # Plot measure correlation curve
        label = f'{start_channel:>2d} vs {stop_channel:>2d}'
        line, = ax.plot(hist_t-mean_t, hist_c/1e3)

        # Check if measured jitter is within specifications
        jitter_spec = specified_jitter_rms[mode]
        print((f'Correlation {label} Measured channel jitter: {jitter_measured:0.1f} ps ',
               spec_jitter_label,
               f'{jitter_spec: 0.1f} ps'))
        measured_channels[mode].append(label)
        measured_jitters[mode].append(jitter_measured)

    mean_jitter = np.mean(measured_jitters[mode])
    print('\n')
    print(f'mean jitter: {mean_jitter:0.1f} ps, within specs: {mean_jitter < jitter_spec}')
    print('\n')

    line.set_label(label)  # Add only one label to prevent a crowded plot

    # Plot Gaussian function corresponding to specified jitter
    hist_c_model = gaussian(x=hist_t, mu=0, sigma=jitter_spec*np.sqrt(2), A=np.sum(hist_c))
    ax.plot(hist_t, hist_c_model/1e3, color='k', ls='--', label=spec_jitter_label)

    ax.set_xlim(-5*jitter_spec, 5*jitter_spec)
    ax.legend(loc=1)
    plt.show()

print('Plotting a summary of the results')
# Summary of the measured RMS jitters for a single channel in a table

color_map = {True: 'green', False: 'red'}  # Cell colors
colLabels = ['Channels', 'single channel\nRMS jitter (ps)', spec_jitter_label+' (ps)']

for i, mode in enumerate(resolution_modes):
    fig, ax = plt.subplots()
    rowLabels = measured_channels[mode]
    jitters = measured_jitters[mode]
    jitter_spec = specified_jitter_rms[mode]

    cellContent = [(ch, f'{jitt:0.1f}', jitter_spec) for ch, jitt in zip(rowLabels, jitters)]
    the_table = ax.table(cellText=cellContent, colLabels=colLabels, loc='center', cellLoc='center')
    the_table.scale(1, 1.5)
    ax.axis('tight')
    ax.axis('off')
    fig.suptitle(f'{model} {edition} {mode}')
    fig.tight_layout()

# Freeing the Time Tagger again so that it can be used in another application
TimeTagger.freeTimeTagger(tagger)
plt.show()
