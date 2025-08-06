%
% The synchronized_measurements.m demonstrates the SynchronizedMeasurements
% class. By using the very same time tag set (ensured by synchronized
% measurement), the difference between StartStop, Histogram, and
% Correlation measurement is illustrated.
%
% Create a TimeTagger instance and apply test signals.
tagger=TimeTagger.createTimeTagger();
tagger.setTestSignal([1, 2], true);

% Create an instance of the SynchronizedMeasurements class for tagger
sync_meas = TTSynchronizedMeasurements(tagger);

% Retrieve the proxy object for the synchronized tagger. The sync_tagger
% object can be used in any place the tagger object would be used for
% initialization of a measurement.
% The new measurement will be added on initialization to the synchronization
% group and the measurement itself does not start automatically.
sync_tagger = sync_meas.getTagger();

% Define different measurements using the sync_tagger proxy object.
% The measurement is not started immediately in this case. It waits for
% the sync_meas object to start it.
start_stop = TTStartStop(sync_tagger, 1, 2, 25);
hist = TTHistogram(sync_tagger, 1, 2, 5, 550000);
corr = TTCorrelation(sync_tagger, 1, 2, 5, 1100000);
% We add also two Countrate instances to verify that
% SynchronizedMeasurements ensures the same number of counts.
count1 = TTCountrate(sync_tagger, [1]);
pause(0.1)
count2 = TTCountrate(sync_tagger, [1]);

% Start the measurement for 1 s and wait as long as it is running.
sync_meas.startFor(1e12);
while sync_meas.isRunning()
    pause(0.1)
end

% Check the countrates.
fprintf('Total counts:\n');
fprintf('- Channel 1 - measurement 1: %d counts\n', count1.getCountsTotal());
fprintf('- Channel 1 - measurement 2: %d counts\n', count2.getCountsTotal());

% Plot the results.
figure(1)
clf()
plot1 = subplot(3, 1, 1);
start_stop_data = start_stop.getData();
semilogy(start_stop_data(:, 1), start_stop_data(:, 2));
ylabel('Counts/bin');
title('StartStop: Single-start/single-stop => only positive time differences')
fprintf('Number of data points (StartStop) and bins (Histogram, Correlation):\n');
fprintf('- StartStop:   %7d\n', length(start_stop_data));
plot2 = subplot(3, 1, 2);
semilogy(hist.getIndex(), hist.getData());
ylabel('Counts/bin');
title('Histogram: Multiple-start/multiple-stop, restricted to positive time differences')
fprintf('- Histogram:   %7d (by definition)\n', length(hist.getIndex()))
plot3 = subplot(3, 1, 3);
semilogy(corr.getIndex(), corr.getData());
ylabel('Counts/bin');
title('Correlation: Multiple-start/multiple-stop, positive and negative time differences')
fprintf('- Correlation: %7d (by definition)\n', length(corr.getIndex()))

linkaxes([plot1, plot2, plot3], 'xy')

xlabel('Time (ps)');
% Free time tagger.
clear tagger