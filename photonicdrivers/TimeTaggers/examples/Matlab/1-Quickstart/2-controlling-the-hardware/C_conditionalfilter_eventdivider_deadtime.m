% In this example, we learn how to remove events on the device containing
% no information to save USB bandwidth.

% Create a TimeTagger instance to control your hardware
tagger = TimeTagger.createTimeTagger();

% Set a threshold for the random counts according to the Time Tagger model
if strcmp(tagger.getModel(), "Time Tagger 20")
    min_random_rate = 3E7;
else
    min_random_rate = 1E8;
end

% Try to find a channel that exceeds the count rate threshold and set the
% trigger level accordingly
[random_channel, random_level, random_found] = find_random_signal(tagger, min_random_rate);
if random_found
    fprintf("Found a random signal on channel %d at %.3f mV.\n", random_channel, 1000 * random_level);
    tagger.setTriggerLevel(random_channel, random_level);

    % The default dead-time is defined by the internal clock of the Time Tagger
    % TT X: 750 MHz, TT Ultra: 500 MHz, TT 20: 166.6 MHz
    default_deadtime = tagger.getDeadtime(random_channel);

    % To measure the count rate that exceeds the USB transfer limit without overflows,
    % we use the EventDivider. With divider=100, we discard 99 out of 100 events and
    % let only one pass every 100th event, which is within the USB bandwidth
    tagger.setEventDivider(random_channel, 100);
    countrate = TTCountrate(tagger, random_channel);
    countrate.startFor(int64(1E12));
    countrate.waitUntilFinished();

    % To obtain the real count rate, we have to multiply by 100
    countrate = countrate.getData() * 100;
    specified_usb_rate = 7.5E6; % For Time Tagger 20
    if strcmp(tagger.getModel(), "Time Tagger X")
        specified_usb_rate = 82E6; % For Time Tagger X
    end
    fprintf("The countrate of the random channel is %.1f Mtags/s\n", countrate / 1E6);
    fprintf("This is %.1f%% of the specified USB data rate and %.1f%% of the maximal time-to-digital conversion rate.\n", 100 * countrate / specified_usb_rate, 100 * countrate / (1E12 / default_deadtime));

    % Switch off the EventDivider = set it to 1
    tagger.setEventDivider(random_channel, 1);

    % Take a second input channel which is NOT the random channel and let it
    % measure the built-in test signal, i.e. a periodic signal
    periodic_channel = 2;
    if random_channel == 2
        periodic_channel = 1;
    end
    tagger.setTestSignal(periodic_channel, true);

    % We want to measure only the very first random click after a periodic click.
    % This is achieved by the ConditionalFilter. It opens a gate for any event
    % on the 'trigger' channels and lets only one event of each 'filtered' channel
    % pass. After that, the gate is closed until the next trigger event.
    % The trigger channel is the periodic channel.
    % The filter channel is the random channel.
    tagger.setConditionalFilter(periodic_channel, random_channel);

    % We measure the correlation between the periodic and the FILTERED random channels
    corr = TTCorrelation(tagger, random_channel, periodic_channel, default_deadtime/100, 3000);
                                  
    figure('Position', [100, 100, 900, 600]); 
    fprintf("\nMeasuring with different dead-times:\n");
    for i = 1:5
        % We repeat this measurement for five different dead-times
        tagger.setDeadtime(random_channel, i * default_deadtime);
        deadtime = tagger.getDeadtime(random_channel);
        fprintf("Default dead-time x %d = %d\n", i, deadtime);
        corr.startFor(int64(1E12));
        corr.waitUntilFinished();
        index = double(corr.getIndex());
        data = double(corr.getData());
        plot(index/double(default_deadtime), data, 'DisplayName', sprintf("%d ps", deadtime));
        hold on
        legend();
        title('Correlation for different dead-times');
        xlabel('Delay/Deadtime');
        ylabel("Counts/bin");
    end
    

    annotation('textbox', [0.6, 0.4, 0.3, 0.3], 'String', {...
        'Within the dead-time,',...
        'the Correlation is pretty constant,', ...
        ' i.e, randomly distributed.', ...
        'For larger delays, the', ...
        'Correlation drops with', ...
        'the probability of finding', ...
        'no preceding time-tag.'}, ...
        'HorizontalAlignment', 'right', 'FitBoxToText', 'on');
    

end

freeTimeTagger(tagger);


function [random_channel, random_level, random_found] = find_random_signal(tagger, threshold_rate)
    % This function scans the trigger level in the same way as
    % it is shown in example 2-B.
    DACRange = tagger.getDACRange();
    level = max(-0.01, DACRange(1));
    channels = tagger.getChannelList(TTChannelEdge.Rising);
    
    % If using the Time Tagger X, the input hysteresis value should be set to the lowest possible value for all input channels.
    if strcmp(tagger.getModel(), 'Time Tagger X')
        for i = 1:length(channels)
            tagger.setInputHysteresis(channels(i), 1);
        end
    end
    
    countrate = TTCountrate(tagger, channels);
    disp("")
    while level < 0.01
        fprintf("Searching level: %.1f mV\r", level * 1000);
        for channel = channels
            tagger.setTriggerLevel(channel, level);
        end
        countrate.startFor(int64(1E8));
        countrate.waitUntilFinished();
        data = countrate.getData();
        if max(data) > threshold_rate
            [max_value, max_index] = max(data);
            random_channel = channels(max_index);
            random_level = level;
            random_found = true;
            return;
        end
        level = level + 0.0001;
        
    end
    random_channel = 0;
    random_level = 0;
    random_found = false;
end

