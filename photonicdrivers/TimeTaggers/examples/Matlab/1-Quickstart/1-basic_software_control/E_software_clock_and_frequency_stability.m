disp('**********************************************')
disp('*** Software Clock and Frequency Stability ***')
disp('**********************************************')
% The SoftwareClock is the recommended way of applying an external clock to the Time Tagger.
% For the demonstration of the software clock, we use the internal
% test signal as clock input and will measure its frequency stability
% against itself (trivial) and against the internal clock. This will actually decrease
% the quality of the measurements and is done solely for demonstration purposes.

tagger=TimeTagger.createTimeTagger();

if contains(tagger.getModel(), 'Time Tagger 20')
    tagger.freeTimeTagger();
    warning(['Time Tagger Ultra or Time Tagger X are highly recommended for FrequencyStability measurements.\n', ...
        'Script end.\n'], [])
    return
end

tagger.setTestSignal([1, 2], true);

disp('Measuring the countrate of the test signal')
cnr = TTCountrate(tagger, (1));
cnr.startFor(1e12);
cnr.waitUntilFinished();
countrate = cnr.getData();
fprintf('Test signal frequency is %d kHz\n', round(countrate / 1e3))

disp(' ')
disp('Setting up the software clock with different averaging periods,')
disp('then measuring the phase errors of the clock signal and comparing this value')
disp('to the RMS jitter the test signal and ideal clock channel.')
disp(' ')
disp('averaging_periods | SoftwareClockState.phase_error_estimation | RMS from Correlation | Clock errors')
disp('----------------- + ----------------------------------------- + -------------------- + ------------')

% The following correlation measurement compares the time-tags on channel 1 with the 'ideal_clock_channel'.
% With activated software clock, the tags we receive on channel 1 are rescaled according to the
% software clock, but they deviate from a perfect periodicity according to their measurement jitter
% and clock imperfections that are reduced by the averaging. The 'ideal_clock_channel' is a virtual
% channel with a perfect period of SoftwareClockState.clock_period. It can be interpreted as a grid
% calculated by the software clock.
ideal_clock_channel = tagger.getSoftwareClockState.ideal_clock_channel;
correlation = TTCorrelation(tagger, 1, ideal_clock_channel, 1, 5000);

% We will check the locking behavior for different values of average_periods. Large values result
% in a slowly varying detected frequency, but faster deviations of the clock may cause the locking
% process to fail. The inability to compensate for the deviations quickly will result in a broad
% distribution of time differences in the Correlation measurement. For very small values, phase noise
% will dominate the result, and the detected frequency will be unstable.
for average_periods = [3000, 1000, 300, 100, 30, 10]
    % The software clock is defined for the entire hardware device using the setSoftwareClock() method.
    try
        tagger.setSoftwareClock(1, countrate(1), average_periods);
    catch
         fprintf('%17d | ################################# not locked ##################################\n', ...
             average_periods)
         continue
    end
    correlation.startFor(1e12);
    correlation.waitUntilFinished();
    data = double(correlation.getData());
    index = double(correlation.getIndex());
    clock_state = tagger.getSoftwareClockState();
    phase_error = clock_state.phase_error_estimation;
    clock_errors = clock_state.error_counter;
    if any(data)
        stdev = std(index, data);
        fprintf('%17d | %38.2f ps | %17.2f ps | %11d\n', average_periods, phase_error, stdev, clock_errors);
    else
        fprintf('%17d | ######### very bad locking (no valid Correlation data) ######### | %12d', average_periods, clock_errors)
    end
end

disp(' ')
disp('Starting frequency stability measurements with software clock enabled.')
% Here, steps from 1E0 to 1E6 at a test signal frequency of ~900 kHz will cover a time
% range ('tau') from 1E0/800 kHz = 1.1 µs to 1E6/800 kHz = 1.125 s.
steps = round(logspace(0, 6, 200));
freq_stab = TTFrequencyStability(tagger, 2, steps, 1, 1000);

% FrequencyStability Measurement #1:
% Comparing the stability of the SoftwareClock to the test signal
% and hence to itself is almost trivial. The FrequencyStability graphs
% will be dominated by the discretization noise of the Time Tagger.

disp('Measuring for 5 seconds.')
% The maximum 'tau' is at 1.125. Because the TDEV compares 4 samples, the
% time needed is 3*max(tau) is needed at least to cover the full range and
% avoid NaNs in the TDEV result.
freq_stab.startFor(5e12);
freq_stab.waitUntilFinished();
data_sw_clk = freq_stab.getDataObject();
taus = data_sw_clk.getTau();
time_trace = data_sw_clk.getTraceIndex();

disp(' ')
disp('Starting frequency stability measurements with software clock disabled.')
disp('Measuring for 5 seconds.')
% FrequencyStability measurement # 2:
% SoftwareClock is disabled and the test signal is compared to the
% internal clock of the TimeTagger.
tagger.disableSoftwareClock();
freq_stab.startFor(5e12);
freq_stab.waitUntilFinished();
data_no_sw_clk = freq_stab.getDataObject();

disp('Plotting the results of the frequency stability analysis.')
f = figure();
f.Position = [100, 100, 800, 500];
subplot(2, 2, 1)

loglog(taus, double(data_sw_clk.getADEV()), taus, data_sw_clk.getMDEV(), ...
    taus, data_sw_clk.getHDEV()),
legend('ADEV', 'MDEV', 'HDEV')
xlabel('Tau (s)')
ylabel('Allan deviations')
title('Test signal as clock vs itself')
grid on

subplot(2, 2, 3)
loglog(taus, data_sw_clk.getADEVScaled(), taus, data_sw_clk.getTDEV(), ...
    taus, data_sw_clk.getHDEVScaled(), taus, data_sw_clk.getSTDD()),
legend({'scaled ADEV', 'TDEV', 'scaled HDEV', 'STDDEV'}, 'Location', 'east')
ylabel('Time error (ps)')
xlabel('Time (s)')
grid on

subplot(2, 2, 2)
loglog(taus, data_no_sw_clk.getADEV(), taus, data_no_sw_clk.getMDEV(), ...
    taus, data_no_sw_clk.getHDEV()),
legend('ADEV', 'MDEV', 'HDEV')
xlabel('Tau (s)')
title('Test signal vs internal clock')
grid on

subplot(2, 2, 4)
loglog(taus, data_no_sw_clk.getADEVScaled(), taus, data_no_sw_clk.getTDEV(), ...
    taus, data_no_sw_clk.getHDEVScaled(), taus, data_no_sw_clk.getSTDD()),
legend({'scaled ADEV', 'TDEV', 'scaled HDEV', 'STDDEV'}, 'Location', 'northwest')
xlabel('Time (s)')
grid on

clear tagger
