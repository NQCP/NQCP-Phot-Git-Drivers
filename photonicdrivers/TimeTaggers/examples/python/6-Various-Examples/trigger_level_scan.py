import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from TimeTagger import scanTimeTagger, createTimeTagger, Countrate, getVersion, StartStop
from scipy.optimize import curve_fit
from time import sleep
from datetime import datetime
from typing import Tuple

# SETTINGS
# Please change the settings according to your setup

channels = [1, 2]  # Use negative numbers to trigger on falling edge
min_trigger_voltage = 0.1  # V
max_trigger_voltage = 1.0  # V
data_points = 11  # per scan
analysis_range = 100000  # +/- .. ps around the maximum of the StartStop measurement
warmup_time = 0  # s
integration_time = 1  # s
jitter_analysis = False  # requires periodic signals, set to False otherwise

print("Time Tagger - Trigger Level Scan Script\n")
print("Settings (can be changed within the script)")
print(f"^ Channels: {channels} (positive numbers: rising edge, negative numbers: falling edge)")
print(f"^ Trigger level scan range from {min_trigger_voltage} mV to {max_trigger_voltage} in {data_points} steps.")
if jitter_analysis:
    print("^ Jitter analysis for periodic signals is enabled.")
else:
    print("^ Jitter analysis for periodic signals is disabled.")
print()


def gaussian(x: np.ndarray, a: float, mu: float, sigma: float) -> np.ndarray:
    return a * np.exp(-0.5 * ((x - mu) / sigma)**2)


def calc_mean_and_jitter(x: np.ndarray, y: np.ndarray) -> Tuple[float, float, float, float, float]:
    N = np.sum(y)
    if N == 0:
        return np.nan, np.nan, np.nan, np.nan, np.nan
    sum_z = np.sum(y * x)
    z_mean = sum_z / N
    variance = np.sum(y * (x - z_mean) ** 2) / N
    rms = np.sqrt(variance)
    x0 = x[y.argmax()]
    y0 = y.max()
    try:
        pop, _ = curve_fit(gaussian, x, y, p0=(y0, x0, rms))
    except RuntimeError:
        return z_mean, rms, np.nan, np.nan, np.nan
    a, mu, sigma = pop
    return z_mean, rms, a, mu, sigma


# Create Trigger level array as specified in the settings
trigger_levels = np.linspace(min_trigger_voltage, max_trigger_voltage, num=data_points)

# Create output folder
output_folder = 'trigger_level_scan/'
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Initialize TimeTagger
print("Time Tagger Version: {}".format(getVersion()))
taggers = scanTimeTagger()
assert len(taggers) == 1, "Exactly one Time Tagger must be attached which is not in use."
tagger = createTimeTagger()
print("Time Tagger: {}  SN: {}  t = {}".format(tagger.getModel(), tagger.getSerial(), datetime.now()))

# Countrate measurement is used to analyze the count rates of all channels
countrate = Countrate(tagger, channels)
# StartStop measurements are used to analyze the autocorrelation jitter for periodic signals
start_stop_measurement = []
for channel in channels:
    start_stop_measurement.append(StartStop(tagger, channel, channel, binwidth=1))

if warmup_time == 0:
    print('For jitter analysis: please consider a warmup time of 60s for the final measurement.')
else:
    print('Wait {}s to warmup...'.format(warmup_time))
    sleep(warmup_time)
print()

# preallocate the result arrays
result = np.zeros([len(trigger_levels), len(channels)])
result_autocorr_rms = np.full_like(result, np.nan)
result_autocorr_fit = np.full_like(result, np.nan)

# Setup plots
plt.ion()
fig = plt.figure(figsize=(16, 10))
colors = plt.get_cmap('tab20').colors
gs = GridSpec(2, 2, figure=fig)
ax1 = fig.add_subplot(gs[:, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1:, 1])

# Start measurement and analysis
for i, triggerlevel in enumerate(trigger_levels):
    # Measure input signals
    for channel in channels:
        tagger.setTriggerLevel(channel, triggerlevel)

    countrate.startFor(integration_time * 1e12)
    for start_stop in start_stop_measurement:
        start_stop.startFor(integration_time * 1e12)

    countrate.waitUntilFinished()
    for start_stop in start_stop_measurement:
        start_stop.waitUntilFinished()
    result[i, :] = countrate.getData()

    # Plot and analyze autocorrelation
    ax1.clear()
    for i_ss, (channel, start_stop) in enumerate(zip(channels, start_stop_measurement)):
        autocorr = start_stop.getData()
        if autocorr.size == 0:
            continue
        max_t = autocorr[autocorr[:, 1].argmax(), 0]
        analysis_dt = (int(max_t - analysis_range), int(max_t + analysis_range))
        analysis_index = np.where(
            np.logical_and(analysis_dt[0] <= autocorr[:, 0], autocorr[:, 0] < analysis_dt[1]))[0]
        if len(analysis_index) > 1:
            x = autocorr[analysis_index, 0]
            counts = autocorr[analysis_index, 1]
            ax1.plot(x, counts, color=colors[2 * i_ss + 1], label=f'data ch {channel}')
            if jitter_analysis:
                rms_x0, rms_jitter, fit_a, fit_mu, fit_jitter = calc_mean_and_jitter(x, counts)
                ax1.plot(x, gaussian(x, fit_a, fit_mu, fit_jitter), ':',
                         color=colors[2 * i_ss], label=f'fit rms {fit_jitter:.1f} ps, ch {channel}')
                result_autocorr_rms[i, i_ss] = rms_jitter
                result_autocorr_fit[i, i_ss] = fit_jitter
        else:
            x = autocorr[:, 0]
            counts = autocorr[:, 1]
            ax1.plot(x, counts, color=colors[i], label=f'data ch {channel}')
    ax1.set_title(f"Histogram channel {channel}, triggerlevel {triggerlevel*1e3:.0f} mV")
    ax1.set_xlabel("Time Difference (ps)")
    ax1.set_ylabel("Counts")
    ax1.legend()

    # Plot countrate
    ax2.clear()
    if np.all(result <= 0):
        ax2.plot(trigger_levels * 1e3, result, label=str(channels))
    else:
        ax2.semilogy(trigger_levels * 1e3, result, label=str(channels))
    ax2.set_title("Countrate vs Trigger Level")
    ax2.legend([f"ch {c}" for c in channels])
    ax2.set_xlim(min_trigger_voltage * 1e3, max_trigger_voltage * 1e3)
    ax2.set_xlabel("Trigger Level (mV)")
    ax2.set_ylabel("Count rate (Hz)")

    # Plot jitter for periodic signals
    if jitter_analysis:
        ax3.clear()
        ax3.set_prop_cycle(color=colors[0::2])
        ax3.semilogy(trigger_levels * 1e3, result_autocorr_rms, label=str(channels))
        ax3.set_prop_cycle(color=colors[1::2])
        ax3.semilogy(trigger_levels * 1e3, result_autocorr_fit, ':', label=str(channels))
        ax3.set_ylabel("Single Channel jitter * sqrt(2) (ps)")
        ax3.legend([f"ch {c} rms" for c in channels] + [f"ch {c} fitted" for c in channels])
        ax3.set_xlim(min_trigger_voltage * 1e3, max_trigger_voltage * 1e3)
        ax3.set_title("Jitter vs Trigger Level")
        ax3.set_xlabel("Trigger Level (mV)")

    plt.pause(0.1)
    fig.tight_layout()
    fig.savefig(output_folder + f'trigger_level_scan_countrate_jitter_{int(triggerlevel)}_mV.png')

    for i_channel, channel in enumerate(channels):
        msg = (
            f"Trigger level ch {channel}: {triggerlevel*1e3:4.0f} mV, countrate {result[i, i_channel]/1e3:8.3f} kHz, "
            f"rms jit {result_autocorr_rms[i, i_channel]:5.1f} ps, "
            f"fitted jit {result_autocorr_fit[i, i_channel]:5.1f} ps  ({i+1}/{len(trigger_levels)})"
        )
        print(msg)

del tagger
plt.ioff()
plt.show()
