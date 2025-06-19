% This example shows how to use the virtual channel Combinations.
% It detects clicks on all possible channel combinations and facilitates 
% counting coincidences with clicks on a specific group of channels while 
% no clicks on others. Up to 6 input channels will be used, 
% with the test signal with co-prime dividers.
% It yields a high input rate, decreasing toward higher-order coincidences.
clear all;
clc;

% Create a TimeTagger instance to control your hardware
tagger = TimeTagger.createTimeTagger();

% Get up to 6 available channels.
all_channels = tagger.getChannelList(TTChannelEdge.Rising);
all_channels = all_channels(1:min(6, length(all_channels)));
reference_channel = all_channels(1);
channels = all_channels(2:end);

% Enable test signal
tagger.setTestSignal(all_channels, true);

% Create Correlation measurements and use SynchronizedMeasurements to start them easily
sync_meas = TTSynchronizedMeasurements(tagger);
sync_tagger = sync_meas.getTagger();

corr_list = {};
for i = 1:length(channels)
    corr_list{i} = TTCorrelation(sync_tagger, reference_channel, channels(i), 1, 5000);
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

% Increase the test signal rate to have enhance the probability
% to have high-order coincidences
default_divider = tagger.getTestSignalDivider();
tagger.setTestSignalDivider(ceil(default_divider / 4));

% Measure the period of the test signal
crate = TTCountrate(tagger, channels);
crate.startFor(1e11);
crate.waitUntilFinished();
crate_values = crate.getData();
period = int64(1e12 / crate_values(1));
disp(['Rate per input without divider: ' num2str(1e6 / period) ' Mcps']);
windows_size = period / 2;

% Set the prime dividers on all channels except for the first one.
% The first channel will be included in the combination, and we will see that all combinations
% without this channel will be zero, as it always clicks.
dividers = sort([3, 5, 7, 11, 13, 17]);
dividers = dividers(1:length(all_channels));
for i = 2:length(all_channels)
    tagger.setEventDivider(channels(i-1), dividers(i));
end

% Create the Combinations virtual channel
combination = TTCombinations(tagger, all_channels, windows_size);

% Make all possible combinations to access the virtual channel numbers
groups = {};
max_order = length(all_channels) + 1;

for order = max_order:-1:2
    combinations = nchoosek(all_channels, order);
    groups = [groups; num2cell(combinations, 2)];
end

% Create a list with the virtual channels monitoring the combinations
virtual_channels = [];
for i = 1:length(groups)
    group = groups(i,:);
    group = group{:};
    virtual_channels = [virtual_channels; combination.getChannel(group)];
end
% Add to the list of virtual channels, the one monitoring 2-fold combinations
n_channel = 2;
virtual_channels = [virtual_channels; combination.getSumChannel(n_channel)];

% Run a countrate measurement on each virtual channel to see the individual rates.
disp('***********************************************************************************');
disp(['Channel ' num2str(reference_channel) ' has full click rate. It will always be present in the combination window.']);
disp('We expect all combinations without channel 1 to have 0 rate');
disp('***********************************************************************************');
measure_countrates(tagger, virtual_channels, groups, reference_channel);

% Set the divider to the first channel as well as see how the combinations rates change
tagger.setEventDivider(reference_channel, dividers(1));

% Run a countrate measurement on each virtual channel to see the individual rates.
disp('***********************************************************************************');
disp(['Channel ' num2str(reference_channel) ' has a lower rate now']);
disp('We expect all combinations to have a rate greater than 0.');
disp('***********************************************************************************');
rates = measure_countrates(tagger, virtual_channels, groups, reference_channel);

% Use the getCombination() method to find the index range corresponding to the 2-fold combinations.
lower_2fold_index = length(virtual_channels);
upper_2fold_index = 0;
for i = 1:length(virtual_channels)
    virtual_channel = virtual_channels(i);
    if length(combination.getCombination(virtual_channel)) == 2
        lower_2fold_index = min(i, lower_2fold_index);
        upper_2fold_index = max(i, upper_2fold_index);
    end
end

% This will be compared to the last entry in rates correspond to the sumChannel(2).
disp(['Sum of 2-fold combination from the sumChannel(2): ' num2str(rates(end)) ' cps and from the sum of the individual channels with combination of 2 elements: ' num2str(sum(rates(lower_2fold_index:upper_2fold_index))) ' cps']);

% Close the connection to the Time Tagger
freeTimeTagger(tagger);



% Function defined to measure and print the count rates
function rates = measure_countrates(tagger, virtual_channels, groups, reference_channel)
    % Measure and print the count rates
    crate = TTCountrate(tagger, virtual_channels);
    crate.startFor(5e12);
    crate.waitUntilFinished();
    rates = crate.getData();
    for includes_first = [true, false]
        disp(['Combinations ' 'including' ' not including ' num2str(reference_channel) ':']);
        for i = 1:length(groups)
            group = groups{i};
            if any(group == reference_channel) == includes_first
                disp(['Combination: ' num2str(group) ', rate: ' num2str(rates(i)) ' cps']);
            end
        end
    end
end

