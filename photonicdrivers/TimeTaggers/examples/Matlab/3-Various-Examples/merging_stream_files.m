% Merge Time Tag Stream files recorded separately from two Time Taggers.

% This example records two time tag stream files, one for channels 1 and 2 and another for channels 3 and 4.
% Later these separate stream files are combined into one to calculate the correlation between channels 1 and 3.
% The file merger is combining the streams. The user can specify a constant time offset for each stream
% as well as the channel number offset.

% Create test data
MAKE_TESTDATA = true;
MERGE_DUMPS = true;
REPLAY_MERGE = true;

dirpath = tempname; % directory for files created by the FileWriter
mkdir(dirpath);
dump12 = fullfile(dirpath, 'dump12.ttbin');
dump34 = fullfile(dirpath, 'dump34.ttbin');

% Create test data
if MAKE_TESTDATA
    tagger = TimeTagger.createTimeTagger();
    tagger.setTestSignal([1, 2, 3, 4], true);
    sm = TTSynchronizedMeasurements(tagger);
    synch_tagger = sm.getTagger();
    fw12 = TTFileWriter(synch_tagger, dump12, [1, 2]);
    fw34 = TTFileWriter(synch_tagger, dump34, [3, 4]);
    sm.startFor(5e12);
    sm.waitUntilFinished();
end

dump1234_merged = fullfile(dirpath, 'dump1234_merged.ttbin');
if MERGE_DUMPS
    % Merges multiple *.ttbin files into one.
    % You can specify channel number offsets to separate channels if dumps were recorded using the same channel numbers
    % You can specify a constant time offset for each ttbin file.
    TimeTagger.mergeStreamFiles(...
        dump1234_merged, ... % Filename of the output ttbin file
        {dump12, dump34}, ... % List of dump files that will be merged
        [0, 0], ... % Channel number offset for each ttbin file. Useful when dumps have the same channel numbers.
        [0, 1000], ... % Time offset for each ttbin file in picoseconds.
        true ... % If True, then merge only the regions where the time is overlapping.
    );
end

if REPLAY_MERGE
    % Uses merged file and calculates correlation for the channels 1&3
    % that were originally in different dump files, and also for channels 1&2.
    tagger_virtual = TimeTagger.createTimeTaggerVirtual();
    cor12 = TTCorrelation(tagger_virtual, 1, 2, 10, 1000);
    cor13 = TTCorrelation(tagger_virtual, 1, 3, 10, 1000);

    tagger_virtual.replay(dump1234_merged);
    tagger_virtual.waitForCompletion();

    figure;
    plot(cor12.getIndex(), cor12.getData(), 'DisplayName', '1 vs 2');
    hold on;
    plot(cor13.getIndex(), cor13.getData(), 'DisplayName', '1 vs 3');
    xlabel('Time (ps)');
    ylabel('Counts/bin');
    legend;
    hold off;
end

freeTimeTagger(tagger);
