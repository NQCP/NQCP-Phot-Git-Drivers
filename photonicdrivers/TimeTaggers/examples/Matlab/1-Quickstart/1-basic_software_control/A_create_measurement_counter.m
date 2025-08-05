% In this example, we learn how to start a simple measurement. 
% We use the Counter class to measure a count rate trace
% on channels 1 and 2 while switching on the built-in test signals.

% create a TimeTagger instance
tagger=TimeTagger.createTimeTagger();

% simple counter on channels 1 and 2 with 1 ms binwidth (1e9 ps) and 1000 points for each channel
disp('****************************************');
disp('*** Demonstrate a counter time trace ***');
disp('****************************************');
disp(' ');
disp('Create counters on channels 1 and 2 with 1 ms binwidth and 1000 points.');
disp(' ');

count = TTCounter(tagger, [1 2], 1e9, 1000);

% apply the built-in test signal (~0.8 to 0.9 MHz) to channels
disp('Enabling test signal on channel 1.'); disp(' ');
tagger.setTestSignal(1, true);
pause(.5);

%Apply test signal to channel 2
disp('Enabling test signal on channel 2.'); disp(' ');
tagger.setTestSignal(2, true);
pause(.5);

%After waiting for 0.5 s, the 1000 values should be filled


%retrieve the data
data = count.getData();

figure()
% here is a pitfall: you have to cast count.getIndex() to a double first -
% otherwise it is a integer division which screws up your plot
plot(double(count.getIndex())/1e12, data);
xlabel('Time (s)');
ylabel('Countrate (kHz)');
legend('channel 1', 'channel 2', 'Location', 'Southeast');
title('Time trace of the click rate on channel 1 and 2')
text(0.55,450, {'The built-in test signal', '(frequency ~ 800 to 900 kHz)',...
    'is applied first to channel 1', 'and 0.5 s later to channel 2.'});

freeTimeTagger(tagger);
