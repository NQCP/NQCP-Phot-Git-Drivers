% This example shows how to use perform a coincidence-counting experiment.
% All up to 16 input channels will be used, with the test signal at maximum
% rate with co-prime dividers. This yield a high input rate, but only a low
% rate of coincidences of higher orders.

% Create a TimeTagger instance to control your hardware
tagger = TimeTagger.createTimeTagger();

channels = tagger.getChannelList(TTChannelEdge.Rising);
channels = channels(1:min(16, length(channels))); %select up to 16 channels

min_order = 2;
max_order = min(10, length(channels));

fprintf('Counting all coincidences on %d channels for the orders %d to %d\n', ...
    length(channels), min_order, max_order);

% Enable test signal
tagger.setTestSignal(channels, true);

% Sets input delays to 0
for ch = channels
    tagger.setInputDelay(ch, 0);
end

% Create Correlation measurements and use SynchronizedMeasurements to start them easily
sync_meas = TTSynchronizedMeasurements(tagger);
sync_tagger = sync_meas.getTagger();

corr_list = {};
for i = 1:length(channels)
    corr_list{i} = TTCorrelation(sync_tagger, channels(1), channels(i), 1, 5000);
end

% Start measurements and accumulate data for 1 second
sync_meas.startFor(1e12);
sync_meas.waitUntilFinished();

% Determine delays
delays = zeros(1, length(channels));
for i = 1:length(corr_list)
    corr = corr_list{i};
    hist_t = int64(corr.getIndex());
    hist_c = int64(corr.getData());
    dt = sum(hist_t .* hist_c) / sum(hist_c);
    delays(i) = int64(dt);
end

disp(['Delays: ' num2str(delays)]);

% Set input delay correction to align all channels
for i = 1:length(channels)
    tagger.setInputDelay(channels(i), delays(i));
end

% increase the test signal rate
default_divider = tagger.getTestSignalDivider();
tagger.setTestSignalDivider(ceil(default_divider/20));

% measure the period of the test signal
rate = TTCountrate(tagger, channels(1));
rate.startFor(int64(1e11));
rate.waitUntilFinished();
period = int64(1e12 / rate.getData());
fprintf('Rate per input without divider: %.1f Mcps\n', 1e6 / period);
coincidence_window = period / 2;

% set the co-prime dividers on all channels
dividers = sort([11*7, 13*5, 17*3, 19*2, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]);
for i = 1:length(channels)
    tagger.setEventDivider(channels(i), dividers(i));
end

% measure the total rate of all channels
rate = TTCountrate(tagger, channels);
rate.startFor(int64(1e12));
rate.waitUntilFinished();
fprintf('Total rate within 1s: %.1f Mcps\n', sum(rate.getData()) * 1e-6);



% check the performance of the Coincidences separately for all order of permutations
all_groups = {};
for order = min_order:max_order
    % Generate all combinations of order elements
    groups = nchoosek(channels, order);
    groups = num2cell(groups, 2);
    all_groups = [all_groups; groups];

    % perform the Coincidences + Countrate measurement
    CountCoincidences(tagger, groups, string(order), coincidence_window);
end

% check the performance of the Coincidences for all permutations at once
CountCoincidences(tagger, all_groups, sprintf('%d-%d', min_order, max_order), coincidence_window);

% Close the connection to the Time Tagger
freeTimeTagger(tagger);


function CountCoincidences(tagger, groups, order, coincidence_window)

    co = TTCoincidences(tagger, groups, coincidence_window);
    cr = TTCountrate(tagger, co.getChannels());

    fprintf('Order %s with %d groups: ', order, length(groups));
    pause(10); % Wait 10 seconds of real time
    efficiency =  double(cr.getCaptureDuration()) * 1e-11; % % of data_time / real_time
    rate = sum(cr.getData());
    fprintf('efficiency: %.1f%%, total rate: %.1f cps\n', efficiency, rate);
end
