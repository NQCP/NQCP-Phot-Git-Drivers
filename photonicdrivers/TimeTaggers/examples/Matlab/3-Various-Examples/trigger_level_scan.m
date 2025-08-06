% SETTINGS
% Please change the settings according to your setup. 
% If you want to test the code, enable test signal by uncommenting line 36

channels = [1, 2];  % Use negative numbers to trigger on falling edge
min_trigger_voltage = 0.1;  % V
max_trigger_voltage = 1.0;  % V
data_points = 10;  % per scan
analysis_range = 100000;  % +/- .. ps around the maximum of the StartStop measurement
integration_time = 1;  % s

fprintf("Time Tagger - Trigger Level Scan Script\n\n");
fprintf("Settings (can be changed within the script)\n");
fprintf("^ Channels: %s (positive numbers: rising edge, negative numbers: falling edge)\n", mat2str(channels));
fprintf("^ Trigger level scan range from %.1f mV to %.1f in %d steps.\n", min_trigger_voltage * 1e3, max_trigger_voltage * 1e3, data_points);
fprintf("\n");

gaussian = @(x, a, mu, sigma) a * exp(-0.5 * ((x - mu) / sigma).^2);

% Create Trigger level array as specified in the settings
trigger_levels = linspace(min_trigger_voltage, max_trigger_voltage, data_points);

% Create output folder
output_folder = 'trigger_level_scan/';
if ~exist(output_folder, 'dir')
    mkdir(output_folder);
end

% Initialize TimeTagger
fprintf("Time Tagger Version: %s\n", TimeTagger.getVersion());
taggers = TimeTagger.scanTimeTagger();
assert(numel(taggers) == 1, "Exactly one Time Tagger must be attached which is not in use.");
tagger = TimeTagger.createTimeTagger();
fprintf("Time Tagger: %s  SN: %s  t = %s\n", tagger.getModel(), tagger.getSerial(), datestr(now()));

%tagger.setTestSignal(channels, true) %Leave as comment for real experiment

% Countrate measurement is used to analyze the count rates of all channels
countrate = TTCountrate(tagger, channels);
% StartStop measurements are used to display the autocorrelation for periodic signals
start_stop_measurement = arrayfun(@(channel) TTStartStop(tagger, channel, channel, 1), channels);

% preallocate the result arrays
result = zeros(numel(trigger_levels), numel(channels));
result_autocorr_rms = NaN(size(result));
result_autocorr_fit = NaN(size(result));

% Setup plots
fig = figure('Position', [100, 100, 1200, 800]);
colors = lines(numel(channels));
ax1 = subplot(1, 2, 1);
ax2 = subplot(1, 2, 2);

% Start measurement and analysis
for i = 1:numel(trigger_levels)
    triggerlevel = trigger_levels(i);

    % Measure input signals
    for j = 1:numel(channels)
        channel = channels(j);
        tagger.setTriggerLevel(channel, triggerlevel);
    end

    countrate.startFor(integration_time * 1e12);
    arrayfun(@(start_stop) start_stop.startFor(integration_time * 1e12), start_stop_measurement);

    countrate.waitUntilFinished();
    arrayfun(@(start_stop) start_stop.waitUntilFinished(), start_stop_measurement);
    result(i, :) = countrate.getData();

    % Plot and analyze autocorrelation
    cla(ax1);
    for j = 1:numel(channels)
        channel = channels(j);
        autocorr = start_stop_measurement(j).getData();
        if isempty(autocorr)
            continue;
        end
        [~, idx] = max(autocorr(:, 2));
        max_t = autocorr(idx, 1);
        analysis_dt = [max_t - analysis_range, max_t + analysis_range];
        analysis_index = find(autocorr(:, 1) >= analysis_dt(1) & autocorr(:, 1) < analysis_dt(2));
        if numel(analysis_index) > 1
            x = autocorr(analysis_index, 1);
            counts = autocorr(analysis_index, 2);
            plot(ax1, x, counts, 'Color', colors(j, :), 'DisplayName', ['data ch ', num2str(channel)]);
        else
            x = autocorr(:, 1);
            counts = autocorr(:, 2);
            plot(ax1, x, counts, 'Color', colors(j, :), 'DisplayName', ['data ch ', num2str(channel)]);
        end
        hold(ax1, 'on');
    end
    title(ax1, ['Histogram channel ', num2str(channel), ', triggerlevel ', num2str(triggerlevel * 1e3, '%.0f'), ' mV']);
    xlabel(ax1, 'Time Difference (ps)');
    ylabel(ax1, 'Counts');
    legend(ax1);
    hold(ax1, 'off');

    % Plot countrate
    cla(ax2);
    if all(result <= 0, 'all')
        plot(ax2, trigger_levels * 1e3, result);
    else
        semilogy(ax2, trigger_levels * 1e3, result);
    end
    title(ax2, 'Countrate vs Trigger Level');
    legend(ax2, arrayfun(@(c) ['ch ', num2str(c)], channels, 'UniformOutput', false));
    xlim(ax2, [min_trigger_voltage * 1e3, max_trigger_voltage * 1e3]);
    xlabel(ax2, 'Trigger Level (mV)');
    ylabel(ax2, 'Count rate (Hz)');

end

freeTimeTagger(tagger);


