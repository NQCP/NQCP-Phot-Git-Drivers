%
% The TTDumpAndLoad.m shows how to save and load the raw time tag stream
%
%
% create a TimeTagger instance
disp('*****************************************************');
disp('*** Show save and load of the raw time tag stream ***');
disp('*****************************************************');
tagger=TimeTagger.createTimeTagger();
channels = [1 2];
% apply a test signal to the selected channels
disp(' ');
disp('Enable the internal test signal.');
tagger.setTestSignal(channels, true);

%
% create the file dump
disp(' ');
disp('Create a TTFileWriter object which saves the raw time tags of the given channels.');
disp('Parameters:')
disp(' (1) Time Tagger object the dump belongs to')
disp(' (2) file name for the raw time tag stream.')
disp('     FileWriter supports file splitting and more than one file will be created.')
disp('     Every created file will have the same filename plus a counter as a suffix.')
disp(' (3) channels which are dumped')
disp(' ');

dirpath = tempname; % directory for files created by the FileWriter
mkdir(dirpath);
filepath = fullfile(dirpath, 'example.ttbin');
disp(['Dump file name: ' filepath]);

file_writer = TTFileWriter(tagger, filepath, channels);
pause(1)
disp(' ');
disp('file_writer.stop() stops recording and closes the file.');
file_writer.stop()
clear file_writer
clear tagger


disp('Read back the dumped stream from the filesystem using TTFileReader.');
file_reader = TTFileReader(filepath);

%now the data can be accessed via methods of the file_reader object

disp('Read all tags data from the file(s).');
while file_reader.hasData()
    n_events = 100000; % Number of events to read at once
    % Read at most n_events.
    data = file_reader.getData(n_events);  % data is an instance of TimeTagStreamBuffer
    fprintf('Size of the returned data chunk: %d events\n', data.size)
    
    disp('Showing a few selected timetags')
    channel = data.getChannels();
    timestamps = data.getTimestamps();
    overflow_types = data.getEventTypes(); % TimeTag = 0, Error = 1, OverflowBegin = 2, OverflowEnd = 3, MissedEvents = 4
    missed_events = data.getMissedEvents();
    
    
    for i = 1:3
        fprintf('    TAG# %8d \t t = %d ps \t Channel: %d \t MissedEvents: %d \t EventType: %s \n', ...
            i, timestamps(i), channel(i), missed_events(i), TTTagType(overflow_types(i)));
    end
    disp('      ...');
    fprintf('    TAG# %8d \t t = %d ps \t Channel: %d \t MissedEvents: %d \t EventType: %s \n\n', ...
            numel(timestamps), timestamps(end), channel(end), missed_events(end), TTTagType(overflow_types(end)));
end

disp('--- The end of the data is reached. ---')

disp(' ');
disp('The raw time tag stream can be also accessed in real-time using the TimeTagStream class.');
disp('The TimeTagStream class returns the tags received directly from the hardware for on-the-fly processing.');

disp('===============================')
disp('Deleting the temporary files.')
clear file_reader;
rmdir(dirpath, 's');