% 
% This example shows how to use Virtual Time Tagger for reprocessing earlier stored timetag stream data.
% 
% The example consists of two steps.
% Step 1:
%     Use the real Time Tagger and record timetag data from two channels with test signal enabled.
%     In addition, accumulate a coarse histogram of the time differences.
% Step 2:
%     Use Virtual Time Tagger to reprocess earlier stored data and accumulate time difference 
%     histogram with much better time resolution. In addition, measure the countrate on both channels.

dirpath = tempname; % directory for files created by the FileWriter
mkdir(dirpath);
filepath = fullfile(dirpath, 'example.ttbin');
disp(['Dump file name: ' filepath]);

% Channel definitions
CHAN_A = 1;
CHAN_B = 2;

disp('****************************************************')
disp('STEP 1: Write events from two channels into a file. ')
disp('****************************************************')

tagger=TimeTagger.createTimeTagger();


% Enable internal test signal
tagger.setTestSignal(CHAN_A, true);
tagger.setTestSignal(CHAN_B, true);
tagger.sync();

% Create Correlation and FileWriter
corr = TTCorrelation(tagger, CHAN_A, CHAN_B, 20, 100);
fw = TTFileWriter(tagger, filepath, [CHAN_A, CHAN_B]);

% Accumulate data for some time
disp(['Writing data to a file:  ', filepath])
disp('Start data acquisition for 10 s')
disp(' ...')
pause(10)

% Stop data accumulation
corr.stop()
fw.stop()

% Print statistics on file size and data-rate
fprintf('Data recording complete.\n\n')
fprintf('*************************** STATISTICS *****************************\n')
fprintf('Recording duration:            %0.0f seconds\n', fw.getCaptureDuration()*1e-12)
fprintf('Events written to the file(s): %0.0f events\n', fw.getTotalEvents())
fprintf('Bytes written to the file(s):  %0.0f bytes\n', fw.getTotalSize())
fprintf('File writing data rate:        %0.0f bytes/s\n', fw.getTotalSize()/(uint64(fw.getCaptureDuration())*1e-12))
fprintf('Compression efficiency:        %0.2f bytes/event\n', fw.getTotalSize()/fw.getTotalEvents())
fprintf('NOTE: Compression efficiency depends on signal randomness.\n')
fprintf('********************************************************************\n\n')

% Plot the correlation histogram
figure();
bar(corr.getIndex(), corr.getData());
xlabel('time (ps)');
ylabel('counts');
title('Time Tagger: Measured live with large binwidth');

% Disconnect the Time Tagger
clear tagger;

disp('***********************************************************');
disp('STEP 2: Use Virtual Time Tagger to read the data file      ');
disp('        and repeat the measurement with different binwidth ');
disp('        In addition, measure count rate on both channels.  ');
disp('***********************************************************');

% Create Virtual Time Tagger
ttv=TimeTagger.createTimeTaggerVirtual();

% Create the measurements the same way as you do with the real Time Tagger
% Here, we perform Correlation measurement with a smaller binwidth compared
% to the previous measurement.
corr = TTCorrelation(ttv, CHAN_A, CHAN_B, 1, 2000);
crate = TTCountrate(ttv, [CHAN_A, CHAN_B]);

% Specify the file to read the time tags from file or file sequence
ttv.replay(filepath);
disp('Virtual Time Tagger is streaming time tags from the file...')

% Wait until the file reading is finished
ttv.waitForCompletion();
disp('File streaming completed.')

% Create figure and axes
figure();
ax1 = subplot(211);
ax2 = subplot(212);

% Plot correlation
bar(ax1, corr.getIndex(), corr.getData());
xlabel(ax1, 'time (ps)')
ylabel(ax1, 'counts')
title(ax1, 'Virtual Time Tagger: Reprocessed with small binwidth')

% Plot countrate
bar(ax2, [CHAN_A, CHAN_B], crate.getData())
ylabel(ax2, 'countrate (events/s)')
xlabel(ax2, 'channel')
xticks(ax2, [1,2])


% Free Virtual Time Tagger resources
clear ttv

disp('===============================')
disp('Deleting the temporary files.')
rmdir(dirpath, 's');