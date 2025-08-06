% The trigger level is the voltage value that is compared to your input signal in the very first
% stage in the Time Tagger. The built-in test signal cannot be used to demonstrate the effect of the
% trigger level setting as it is injected in a subsequent stage. However, we can check the accuracy
% of the trigger level of your device in this example: At a setting of 0 V, the input noise of the
% unconnected input will trigger the comparator randomly. We will scan the voltage range around 0 V
% to determine the noise level.

clear all;
clc;

% Create a TimeTagger instance to control your hardware
tagger = TimeTagger.createTimeTagger();
inputs = tagger.getChannelList(TTChannelEdge.Rising);

% Set hysteresis value to 1 mV in TTX - by default it is 20 mV
hyst = 1;
if strcmp(tagger.getModel(), 'Time Tagger X')
    for i = 1:length(inputs)
        tagger.setInputHysteresis(inputs(i), hyst);
    end
end

DACRange = tagger.getDACRange;
%With getDACRange(), we can check the minimum and maximum values of the trigger level. A Time
%Tagger 20 only accepts positive values, while a Time Tagger Ultra and Time Tagger X take negative values as well.
if DACRange(1) < 0
    levels = linspace(-0.01, 0.01, 201);
    fprintf('Scan trigger levels from -10 mV to 10 mV:\n');
else
    levels = linspace(0, 0.01, 101);
    fprintf('Scan trigger levels from 0 mV to 10 mV:\n');
end

countrate = TTCountrate(tagger, inputs);
results = [];

for level = levels
    for inp = inputs
        tagger.setTriggerLevel(inp, level);
    end
    countrate.startFor(1E8);
    countrate.waitUntilFinished();
    results = [results; countrate.getData()];
    fprintf('Trigger level: %.3f mV, Overflows: %d\n', level * 1000, tagger.getOverflowsAndClear());
end
fprintf('Done\n');

try
    sensorData = tagger.getSensorData();
    if sensorData{1}.calibration.high_jitter_warning_rising
        fprintf(['Caused by extremely high noise frequencies in the input stages, your Time Tagger\n' ...
            'experienced a calibration error. These frequencies are beyond the specifications\n' ...
            'of the Time Tagger and cannot be handled correctly.\n']);
        if strcmp(tagger.getModel(), 'Time Tagger X')
            fprintf('Look at the channel LEDs of your Time Tagger X: Red lights indicate calibration errors.\n');
        end
        input(['With incoming input signals that are within the specifications, the Time Tagger would\n' ...
            'quickly re-calibrate itself. However, there is no input signal at the moment. You can\n' ...
            'use the autoCalibration() function instead that will use the test signal for re-calibration.\n' ...
            'Press Enter to re-calibrate the Time Tagger.\n']);
        tagger.autoCalibration();
    end
catch
end

% Plot results
if sum(any(results))>0
    figure('Position', [100 100 560 460])
    plots = plot(levels', results);
    title('Trigger level scan');
    xlabel('Trigger level (V)');
    ylabel('Countrate (counts/s)');
    legend(plots, cellfun(@(x) ['Input ' num2str(x)], num2cell(inputs), 'UniformOutput', false));
    set(gca,'FontSize',12)
else
    fprintf(['For your device, no noise clicks occurred for the given trigger level range.\n' ...
             'All acquired counts are 0.\n' ...
             'You can still see from the code of this example how the trigger levels can be set.\n']);
end

freeTimeTagger(tagger);
