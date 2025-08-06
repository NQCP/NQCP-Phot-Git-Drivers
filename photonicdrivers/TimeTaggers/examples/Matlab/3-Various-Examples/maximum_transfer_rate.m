%
% The MaximumTransferRate.m tests the maximum transfer rate you can achieve
%

clear all;

% create a TimeTagger instance
tagger = TimeTagger.createTimeTagger();

disp('*******************************');
disp('*** Turn on the test signal ***');
disp('*******************************');

disp('The data transfer rate will be measured by turning on the internal test signal')
disp('on several channels, with which in total the USB transfer rate is exceeded.')
disp('By measuring the rate of incoming time tags, the maximum data rate is measured.')

disp('')
disp('Please close all other programs to get the maximum data rate possible.')
disp('')

allRisingChannels = tagger.getChannelList(TTChannelEdge.Rising); %get all channel numbers of the rising edges
if strcmp(tagger.getModel(), 'Time Tagger 20')
    % Time Tagger 20
    % set test signal rate close to 2.5 MHz
    default_divider = tagger.getTestSignalDivider();
    tagger.setTestSignalDivider(ceil(default_divider/3))
    disp('Total rate: 4x ~2.5 MHz');
else
    % Time Tagger Ultra or Time Tagger X
    % set test signal rate close to 25 MHz
    default_divider = tagger.getTestSignalDivider();
    tagger.setTestSignalDivider(ceil(default_divider/30))
    disp('Total rate: 4x ~25 MHz');
end

testChannels = allRisingChannels(1:4); % select the first 4 channels
tagger.setTestSignal(testChannels, true)

disp(' ');
disp('******************************************************');
disp('*** Capture the stream via the TimeTagStream class ***');
disp('******************************************************');
disp(' ');
disp('The TimeTagStream class stores the incoming tags in memory');
disp('and is therefore the fastest way to access the time tag stream.');
disp(' ');
bufferSize = 75e6; % tags
capture_time = 0.5; %s
averages = 20;
disp(['Capture buffer size: ' num2str(bufferSize/1e6)   ' MTags']);
disp(['Capture duration:    ' num2str(capture_time) ' s']);
disp(['Test runs:           ' num2str(averages)]);
disp(' ');

totalCounts = 0;
totalTime = 0;

transfer_rate = zeros(1, averages);
stream = TTTimeTagStream(tagger, bufferSize, testChannels);
tagger.sync();
tic;
startTime = toc;
endTime = startTime;
for i = 1:averages
    pause(capture_time - (toc - endTime));
    endTime = toc;
    data = stream.getData();
    dt = endTime - startTime;
    startTime = endTime;
    totalCounts = totalCounts + data.size;
    totalTime = totalTime + dt;
    transfer_rate(i) = double(data.size) / 1e6 / dt;
    fprintf('#%3d: %5.1f MTags/s | dt: %7.3f ms | buffer fill: %3.0f %%\n', i, transfer_rate(i), dt * 1e3, data.size * 100 / bufferSize);
end

transfer_rate = sort(transfer_rate);

fprintf('\n>>>  Average transfer rate: %4.1f MTags/s  <<<\n', double(totalCounts) / 1e6 / totalTime);

if strcmp(tagger.getModel(), 'Time Tagger 20')
    disp('The transfer rate should be between 8.5-9 MTags/s and is limited by the USB 2.0 bandwidth.');
    disp('Usually, the CPU performance is not playing a role at these data rates.');
else
    disp('The maximum transfer rate is not limited by USB 3.x but by the single thread CPU performance.');
    disp('A very good processor (i9-9900K, max. 5 GHz) can process in total 75-80 MTags/s.');
    disp('If the transfer rate drops during the measurement compared the first measurement points,');
    disp('your CPU is probably throttling. This happens especially with mobile processors.');
    disp('In case your data rate is only between 10-12 MTags/s, you have likely connected the Time Tagger')
    disp('to a USB 2.0 port, instead of a USB 3.x port.');
end

clear stream;
freeTimeTagger(tagger);
clear tagger
