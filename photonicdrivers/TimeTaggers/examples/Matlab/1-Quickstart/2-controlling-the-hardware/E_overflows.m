% In this example we observe the overflow behavior of the Time Tagger. Overflows occur when the data
% rate is too high and the buffer onboard the Time Tagger is completely filled. In this situation, data
% loss occurs.

disp('**********************************************************');
disp('*** Demonstrate overflow handling with the data object ***');
disp('**********************************************************');

% Create a TimeTagger instance to control your hardware
tagger = TimeTagger.createTimeTagger();

rising_edges = tagger.getChannelList(TTChannelEdge.Rising);
if strcmp(tagger.getModel(), 'Time Tagger 20')
    CHANNELS = rising_edges(1);
else
    falling_edges = tagger.getChannelList(TTChannelEdge.Falling);
    CHANNELS = [rising_edges(1:4), falling_edges(1:4)];
end

% Activate test signal on the selected channels
tagger.setTestSignal(CHANNELS, true);

counter = TTCounter(tagger, CHANNELS, 1000000000, 60000);

default_divider = tagger.getTestSignalDivider();
disp('The test signal divider is reduced until overflows occur.');
disp(['The default test signal divider is: ', num2str(default_divider)]);

pause(2);

% We increase the data rate successively by reducing the TestSignalDivider
divider = default_divider;
while divider > 1 && ~tagger.getOverflows()
    divider = floor(divider / 2);
    fprintf('divider = %d\n', divider);
    tagger.setTestSignalDivider(divider);
    pause(5);
end
disp(['Overflows occurred at test signal divider of ', num2str(divider)]);

% We let the Time Tagger run for two more seconds in the overflow
pause(5);

% Reset TestSignalDivider to the default value to recover from overflow mode
tagger.setTestSignalDivider(default_divider);
pause(3);
counter.stop();

% Use the .getDataObject() method to obtain an object that includes additional information
% on the data, e.g. the overflows or the count rate in counts/s.
data_object = counter.getDataObject();

% Plot the result
figure()
% Create axes with normalized coordinates
plot(data_object.getIndex() / 1E12, data_object.getFrequency()/1e6);
title('Counter measurement with increasing test signal frequency');
xlabel('Time (s)');
ylabel('MCounts/s');
y_range = max(max(data_object.getFrequency()/1e6))*1.1;
x_range = max(data_object.getIndex() / 1E12);
xlim([0 x_range]);
ylim([0 y_range]);
data_for_annotation = double(data_object.getFrequency()/1e6);
annotation_y = max(max(data_for_annotation));
annotation_str = {'In the overflow mode,';
    'there are gaps in the curve.';
    'After the overflown buffer is';
    'emptied by the USB transfer, it';
    'can accumulate normal time-tags';
    'for a short period, before';
    'it overflows again. These';
    'time-tags are displayed';
    'between the gaps.'};
text(0.5, annotation_y, annotation_str, 'VerticalAlignment',...
    'top', 'HorizontalAlignment', 'left', 'FontSize', 10);



freeTimeTagger(tagger);

