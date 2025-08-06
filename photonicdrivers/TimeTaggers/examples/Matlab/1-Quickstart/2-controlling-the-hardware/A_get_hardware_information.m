% In this example we look at methods that provide information on the Time Tagger(s) in your lab.

% Scan for available TimeTaggers
available_taggers = TimeTagger.scanTimeTagger();
if ~isempty(available_taggers)
    disp('Time Taggers available via TimeTagger.scanTimeTagger():');
    disp(available_taggers);
else
    disp('There are no Time Taggers available. Connect one and retry.');
    return;
end

% Create a TimeTagger instance
tagger = TimeTagger.createTimeTagger();

disp(' ');
disp('Your Time Tagger model via tagger.getModel():');
disp(tagger.getModel());

disp(' ');
disp('Your Time Tagger serial number via tagger.getSerial():');
disp(tagger.getSerial());

% Acquiring internal sensor data of your Time Tagger
disp(' ');
disp('Acquiring internal sensor data of your Time Tagger via tagger.getSensorData().');
try
    disp(' ');
    disp('Sensor data:');
    disp(tagger.getSensorData());
catch
    disp(['The ', tagger.getModel(), 's do not support sensor readout.']);
end

disp(' ');
disp('Full Time Tagger Configuration via tagger.getConfiguration():');
disp(tagger.getConfiguration());

% Free the Time Tagger instance
freeTimeTagger(tagger);
