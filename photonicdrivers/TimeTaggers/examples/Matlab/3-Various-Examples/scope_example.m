disp('*********************');
disp('*** Scope example ***');
disp('*********************');
disp(' ');

tagger = TimeTagger.createTimeTagger();
tagger.setTestSignal(1, true);
tagger.setTestSignal(2, true);

% Record signal from the channel 1 triggered by the channel 2.
% The signal is internal test signal of approx 800 kHz.
scope = TTScope(tagger, 1, 2, 10000000, 1, 1000000);

% Duration window_size and n_max_events will define the resulting trace length
% Here we simply run for 1 second.
scope.startFor(1e12, true); 
scope.waitUntilFinished();
data = scope.getData();
tagger.freeTimeTagger();

% getData() returns a nested array which in not available as a native type
% in Matlab. Therefore the Event[][] must be converted into something
% which can be plotted:
dataCh1 = data(1);
if int32(dataCh1(1).state) == TTState.UNKNOWN
    warning('No data received on channel 1 for Scope test');
else
    % to plot the data we have to convert each edge into two data points
    x = zeros(1, dataCh1.Length);
    y = zeros(1, dataCh1.Length);
    for i=1:dataCh1.Length
        x(i) = dataCh1(i).time;
        y(i) = int32(dataCh1(i).state) == TTState.HIGH;
    end
    figure();
    % The data points returned by the scope are the time stamp and new
    % state. The most suitable plotting function for such data is "stairs".
    stairs(x/1000000, y);
    ylabel('ch 1');
    xlabel('time (us)');
    ylim([-0.1, 1.1]);
end
