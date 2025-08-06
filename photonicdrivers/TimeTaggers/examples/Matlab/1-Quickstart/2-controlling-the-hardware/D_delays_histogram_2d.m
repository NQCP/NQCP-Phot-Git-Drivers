% Example of using Histogram2D measurement
%
tagger=TimeTagger.createTimeTagger();

% Channel definitions
START_CH = 1;
INPUT_T1 = 2;
INPUT_T2 = 3;

% Histogram parameters
binwidth_1 = 1;
binwidth_2 = binwidth_1;
n_bins_1 = 400;
n_bins_2 = 300;

% Enable test signal
tagger.setTestSignal([START_CH, INPUT_T1, INPUT_T2], true);
tagger.sync();

% Measure signal delays at each input relative to the start input.
corr1 = TTCorrelation(tagger, INPUT_T1, START_CH, 10, 10000);
corr2 = TTCorrelation(tagger, INPUT_T2, START_CH, 10, 10000);

corr1.startFor(1e12);
corr2.startFor(1e12);
corr2.waitUntilFinished();

x = corr1.getIndex();
sd1 = corr1.getData();
[~, idx] = max(sd1);
delay1 = x(idx);

fprintf('Measured delay at INPUT_T1: %0.0f ps\n', delay1)

x = corr2.getIndex();
sd2 = corr2.getData();
[~, idx] = max(sd2);
delay2 = x(idx);

fprintf('Measured delay at INPUT_T2: %0.0f ps\n', delay2)

% Delays signals T1 and T2 signals by a half of the histogram span.
T1_delay = -delay1 + round(binwidth_1*n_bins_1/2);
T2_delay = -delay2 + round(binwidth_2*n_bins_2/2);

tagger.setInputDelay(INPUT_T1, T1_delay);
tagger.setInputDelay(INPUT_T2, T2_delay);
tagger.sync();

% Create 2D Histogram measurement
h2d = TTHistogram2D(tagger, START_CH, INPUT_T1, INPUT_T2, binwidth_1, binwidth_2, n_bins_1, n_bins_2);

% Wait for data to accumulate
h2d.startFor(2e12);
h2d.waitUntilFinished();

% Get and plot Histogram2D data
data2d = h2d.getData();
time1 = h2d.getIndex_1();
time2 = h2d.getIndex_2();

figure();
imagesc(time1, time2, data2d.');
title('Histogram 2D');
xlabel('dt 1 (ps)');
ylabel('dt 2 (ps)');
axis xy

clear tagger
