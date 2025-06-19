% Virtual channels are used to generate new data streams from given input streams. These data streams
% can be used just like physical channels. It is also possible to cascade virtual channels
% to create mighty filters that operate on the fly.
% We will use virtual channels in this example to answer the question: If the rising edges of the
% built-in test signal on two channels are quite close to each other, will the subsequent falling
% edges be close as well? We will use a cascade of virtual channels:
% 1. "Coincidence" will tell us whether two rising edges are close or not.
% 2. The result will act as a start signal for the "GatedChannel" for the falling edges of channel 1.
% 3. A "DelayedChannel" generated from the "Coincidence" will close this gate after one edge.
% 4. A second "GatedChannel" with swapped opener/closer will include complimentary data (falling edges
% of input 1 following rising edges which are far apart)
% Finally, we will compare the Correlations of channel 2 and the two GatedChannel, respectively.

% Create a TimeTagger instance to control your hardware
tagger = TimeTagger.createTimeTagger();

% Enable the test signal on channel 1 and channel 2
tagger.setTestSignal([1, 2], true);

% We use a Correlation measurement to determine the current delay between channel 1 and 2,
% then we set it to a defined value, DELAY, which requires compensation of the current delay.
DELAY = 200;
calibration = TTCorrelation(tagger, 1, 2, 1, 10000);
calibration.startFor(1E11);
calibration.waitUntilFinished();
index = double(calibration.getIndex());
weights = double(calibration.getData()); 
current_delay = round(sum(index.*weights)/sum(weights));
tagger.setInputDelay(1, DELAY - current_delay);
tagger.setInputDelay(-1, DELAY - current_delay);

% Now, we want to distinguish two cases: Rising edges that are quite close and those that are further apart.
% As a tool, we use the virtual channel Coincidence with our measured average delay as coincidenceWindow.
% This means: If two edges are relatively close (= inside coincidenceWindow), there will be one timestamp
% in the virtual channel, right at the average of both input timestamps (determined by the "timestamp" argument).
open_gate = TTCoincidence(tagger, [1, 2], DELAY, TTCoincidenceTimestamp.Average);

% To close the gate after one falling edge, we create a DelayedChannel from "open_gate". It is an exact
% copy, but delayed by 900000 ps. Note how the channel number of "open_gate" is passed to then new virtual
% channel: We call the getChannel() method to retrieve the number assigned by the Time Tagger backend.
close_gate = TTDelayedChannel(tagger, open_gate.getChannel(), 900000);

% Now we can create a reduced copy of the falling edges of input 1 that contains only those following a
% narrow pair of rising edges (those present in "open_gate"). We use the getInvertedChannel() method
% here to keep the example compatible with first generation Time Taggers that used another numbering
% scheme (starting with channel 0). If your Time Tagger starts at channel 1, you can use channel number
% -1 directly.
falling_narrow = TTGatedChannel(tagger, tagger.getInvertedChannel(1), open_gate.getChannel(), close_gate.getChannel());

% The complementary data can be obtained by swapping "gate_start_channel" and "gate_stop_channel"
falling_wide = TTGatedChannel(tagger, tagger.getInvertedChannel(1), close_gate.getChannel(), open_gate.getChannel());

% In the same way, we create GatedChannels from the later one of channel 1 and 2.
% Because the Coincidence timestamp is set to the average of both, we can use it
% to gate the second one.
% We use this second set of GatedChannels to demonstrate a special feature: If an opened gate is
% supposed to transmit exactly one input tag, you can use gate_stop_channel=input_channel, which
% means an input tag passes and closes the gate right after it. Similarly, if a closed gate is
% supposed to exclude exactly one input tag, you can use gate_start_channel=input_channel.
% With this scheme, you could realize this example without defining the DelayedChannel close_gate.
rising_narrow = TTGatedChannel(tagger, 1, open_gate.getChannel(), 1);
rising_wide = TTGatedChannel(tagger, 1, 1, open_gate.getChannel());

% Create a SynchronizedMeasurement to ensure that the same data set is used in both cases
synchronized_meas = TTSynchronizedMeasurements(tagger);
sync_tagger = synchronized_meas.getTagger();
binwidth = 1;
n_bins = abs(5 * DELAY) / binwidth;
corr_falling_narrow = TTCorrelation(sync_tagger, falling_narrow.getChannel(), tagger.getInvertedChannel(2), binwidth, n_bins);
corr_falling_wide = TTCorrelation(sync_tagger, falling_wide.getChannel(), tagger.getInvertedChannel(2), binwidth, n_bins);

corr_rising_narrow = TTCorrelation(tagger, rising_narrow.getChannel(), 2, binwidth, n_bins);
corr_rising_wide = TTCorrelation(tagger, rising_wide.getChannel(), 2, binwidth, n_bins);

% Run the measurement for 1 s
synchronized_meas.startFor(1E12);
synchronized_meas.waitUntilFinished();

freeTimeTagger(tagger);

% Plot the result
figure('Position', [100, 100, 840, 840]); % Adjust the position and size as needed
subplot(2, 1, 1);
plot(corr_rising_narrow.getIndex(), corr_rising_narrow.getData());
hold on;
plot(corr_rising_wide.getIndex(), corr_rising_wide.getData());
ylabel('Counts/bin');
title('Rising edges');
legend({'corr\_rising\_narrow', 'corr\_rising\_wide'},'Location','northwest');

subplot(2, 1, 2);
plot(corr_falling_narrow.getIndex(), corr_falling_narrow.getDataNormalized());
hold on;
plot(corr_falling_wide.getIndex(), corr_falling_wide.getDataNormalized());
xlabel('Time (ps)');
ylabel('Counts/bin');
title('Falling edges');
legend({'corr\_falling\_narrow', 'corr\_falling\_wide'},'Location','northwest');
text(0, max(corr_falling_wide.getDataNormalized() / 2), {'Typically, the two curves'; 'are more or less identical.'; 'This shows that the position'; 'of a falling edge is not correlated'; 'to the position of the previous rising edge.'}, 'HorizontalAlignment', 'right');
