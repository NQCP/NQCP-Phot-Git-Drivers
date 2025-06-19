"""The SoftwareClock is the recommended way of applying an external clock to the Time Tagger.
In this example, we apply the test signal as an "external clock". Actually, this
decreases the quality of all the measurements and is done solely for demonstration purposes.

In the first experiment, we investigate the phase error of the software clock. We use a
Correlation measurement to compare the software clock input_signal to the calculated
"ideal_clock_channel". The RMS of the histogram is compared to the instantaneous metric
provided by SoftwareClockState.

In the second experiment, we use the FrequencyStability measurement class to characterize
the test oscillator."""

from matplotlib import pyplot as plt
import numpy as np
import TimeTagger


def measure_frequency_stability(tagger, channel, figure_name):
    """This function measures and displays a frequency stability analysis."""

    # The FrequencyStability measurement takes an argument "steps". These integer values
    # determine the frequencies at which the signal is analyzed. The steps are applied after
    # taking the "average" argument of FrequencyStability into account.
    # Here, steps from 1E0 to 1E6 at a test signal frequency of ~900 kHz cover a time
    # range ("tau") from 1E0/900 kHz = 1.1 us to 1E6/900 kHz = 1.1 s.
    steps = np.array(np.logspace(0, 6, 200), dtype=np.uint64)

    with TimeTagger.FrequencyStability(tagger,
                                       channel=channel,
                                       steps=steps,
                                       average=1) as freq_stab:
        print("\nMeasurement '{}' started.".format(figure_name))
        freq_stab.startFor(int(5E12))
        freq_stab.waitUntilFinished()
        data = freq_stab.getDataObject()

        fig, ((f3_allan, f3_time), (f3_freq, f3_phase)) = plt.subplots(
            num="FrequencyStability: " + figure_name,
            nrows=2, ncols=2, gridspec_kw={'height_ratios': [4, 2]}
        )

        tau = data.getTau()
        time_trace = data.getTraceIndex()

        f3_time.loglog(tau, data.getADEVScaled(), label='scaled ADEV')
        f3_time.loglog(tau, data.getTDEV(), label='TDEV')
        f3_time.loglog(tau, data.getHDEVScaled(), label='scaled HDEV')
        f3_time.loglog(tau, data.getSTDD(), label='STDDEV')
        f3_time.legend()
        f3_time.grid(True)
        f3_time.set_xlabel('tau (s)')
        f3_time.set_ylabel('time error (ps)')
        f3_time.set_title('error in time domain')

        f3_allan.loglog(tau, data.getADEV(), label='ADEV')
        f3_allan.loglog(tau, data.getMDEV(), label='MDEV')
        f3_allan.loglog(tau, data.getHDEV(), label='HDEV')
        f3_allan.legend()
        f3_allan.grid(True)
        f3_allan.set_xlabel('tau (s)')
        f3_allan.set_ylabel('overlapping/modified allan deviation')
        f3_allan.set_title('error in allan domain')

        f3_freq.plot(time_trace, data.getTraceFrequency()*1e9, label='frequency')
        f3_freq.set_ylabel('frequency error (ppb)')
        f3_freq.set_xlabel('time (s)')
        f3_freq.legend()
        f3_freq.grid(True)

        f3_phase.plot(time_trace, data.getTracePhase()*1e9, label='phase')
        f3_phase.set_ylabel('phase error (ns)')
        f3_phase.set_xlabel('time (s)')
        f3_phase.legend()
        f3_phase.grid(True)

        fig.tight_layout()


# The software clock writes its state changes to the logger. For this example,
# we use a custom logger to avoid writing directly to the console. 
# The log messages will be displayed at the end of the script.
log = list()
TimeTagger.setLogger(callback=lambda level, msg: log.append(msg))

# Create a TimeTagger instance and activate the test signal
tagger = TimeTagger.createTimeTagger()
tagger.setTestSignal(1, True)
tagger.setTestSignal(2, True)

# Setting up the software clock requires the frequency value of the input signal.
# A Countrate measurement is used to determine the frequency of the test signal.
with TimeTagger.Countrate(tagger, channels=[1]) as countrate:
    countrate.startFor(1E10)
    countrate.waitUntilFinished()
    test_signal_frequency = countrate.getData()[0]

print("""
***********************
Phase error measurement
***********************

With many averaging_periods, the resulting frequency is steadier,
but the locking is less stable.

averaging_periods | SoftwareClockState.phase_error_estimation | RMS from Correlation | Clock errors
------------------+-------------------------------------------+----------------------+-------------""")

plt.figure("Correlation: Rescaled input_channel vs. ideal clock")
plt.title("Correlation: rescaled input_channel vs. ideal_clock_channel")
plt.xlabel("Time difference (ps)")
plt.ylabel("Counts")

# The Correlation measurement compares the time-tags on channel 1 with the "ideal_clock_channel".
# With activated software clock, the tags we receive on channel 1 are rescaled according to the
# software clock, but they deviate from a perfect periodicity according to their measurement jitter
# and clock imperfections that are reduced by the averaging. The "ideal_clock_channel" is a virtual
# channel with a perfect period of SoftwareClockState.clock_period. It can be interpreted as a grid
# calculated by the software clock.
correlation = TimeTagger.Correlation(tagger,
                                     channel_1=1,
                                     channel_2=tagger.getSoftwareClockState().ideal_clock_channel,
                                     binwidth=50 if tagger.getModel() == "Time Tagger 20" else 1,
                                     n_bins=5000)


# We will check the locking behavior for different values of average_periods. Large values result
# in a slowly varying detected frequency, but faster deviations of the clock may cause the locking
# process to fail. The inability to compensate for the deviations quickly will result in a broad
# distribution of time differences in the Correlation measurement. For very small values, phase noise
# will dominate the result and the detected frequency will be very unstable.
for average_periods in [10000, 3000, 1000, 300, 100, 30, 10, 3]:

    # The software clock is defined for the entire hardware device using the setSoftwareClock() method.
    # By default, the method will block further execution until the software clock is locked.
    # If the locking is not successful, the method throws a RuntimeError.
    try:
        tagger.setSoftwareClock(input_channel=1,
                                input_frequency=test_signal_frequency,
                                averaging_periods=average_periods)
    except RuntimeError:
        print("{:>17} | ################################# not locked ##################################".format(average_periods))
        continue

    correlation.startFor(5E11)
    correlation.waitUntilFinished()

    clock_state = tagger.getSoftwareClockState()
    corr_index = correlation.getIndex()
    corr_data = correlation.getData()

    if corr_data.any():
        weight = corr_data/np.sum(corr_data)
        plot_rms = np.sqrt(np.sum(weight * corr_index**2))
        print("{:>17} | {:>38.2f} ps | {:>17.2f} ps | {:>12}".format(average_periods, clock_state.phase_error_estimation, plot_rms, clock_state.error_counter))

        plt.plot(corr_index, corr_data, label=str(average_periods))
        plt.legend(title='averaging\n  periods')
        plt.pause(.01)
    else:
        print("{:>17} | ######### very bad locking (no valid Correlation data) ######### | {:>12}".format(average_periods, clock_state.error_counter))

print("""
******************************
FrequencyStability measurement
******************************""")

# With the software clock locked to the test signal, the FrequencyStability measurement of
# the same test signal on another channel will be almost trivial. The FrequencyStability
# graphs will be dominated by the discretization noise of the Time Tagger.
tagger.setSoftwareClock(input_channel=1,
                        input_frequency=test_signal_frequency,
                        averaging_periods=100)
measure_frequency_stability(tagger, 2, "test signal as clock vs. itself (almost trivial)")

# We repeat the measurement without the software clock.
# This will compare the test signal oscillator to the internal clock of your Time Tagger.
# The result is a metric for the quality of the test signal compared to the Time Tagger
# internal clock.
tagger.disableSoftwareClock()
measure_frequency_stability(tagger, 2, "test signal vs. internal clock")

TimeTagger.freeTimeTagger(tagger)

print("""
*********************
Captured log messages
*********************
""")
for msg in log:
    print(msg, "\n")
print("""******************* END OF LOG *******************""")
plt.show()
