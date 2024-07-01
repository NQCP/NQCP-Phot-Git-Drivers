import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from matplotlib import pyplot as plt

# Load in text files to data frame
data_frame = pd.read_csv('Driver1CurrentSweep.txt', delimiter='\t', skiprows=15)
print(data_frame)

# Extract Data
bias_current = data_frame.BC # uA
bias_voltage_1 = data_frame.BV1 # V
bias_voltage_2 = data_frame.BV2 # V
bias_voltage_3 = data_frame.BV3 # V
bias_voltage_4 = data_frame.BV4 # V
counts_1 = data_frame.C1 # V
counts_2 = data_frame.C2 # V
counts_3 = data_frame.C3 # V
counts_4 = data_frame.C4 # V
integration_time = data_frame.IT # ms

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(bias_current, bias_voltage_1, marker='o', linestyle='-', color='b')

# Add titles and labels
plt.xlabel('Bias Voltage CH1 (V)')
plt.ylabel('Bias Current CH1 (uA)')

# Show grid
plt.grid(True)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot( bias_current, counts_1, marker='o', linestyle='-', color='b')

# Add titles and labels
plt.ylabel('Dark Counts')
plt.xlabel('Bias Current (uA)')

# Show grid
plt.grid(True)

# Find the index of the maximum counts
peak_index = np.argmax(counts_1)

# Find the maximum bias current and corresponding bias voltage
max_bias_current = bias_current[peak_index]
max_counts = counts_1[peak_index]

# Estimate peak width
half_height = counts_1[peak_index] / 2
left_boundary = peak_index
right_boundary = peak_index

# Find the left boundary of the peak
while left_boundary > 0 and counts_1[left_boundary] > half_height:
    left_boundary -= 1

# Find the right boundary of the peak
while right_boundary < len(counts_1) - 1 and counts_1[right_boundary] > half_height:
    right_boundary += 1

# Highlight the maximum point
plt.scatter(max_bias_current, max_counts, color='r', zorder=5)
plt.text(max_bias_current, max_counts, f'Max ({max_bias_current}, {max_counts})',
         fontsize=12, verticalalignment='bottom', horizontalalignment='right')

# Create the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(bias_current, bias_voltage_1, 'b-', label='Bias Current')
ax1.set_xlabel('Bias Current (uA)')
ax1.set_ylabel('Bias Voltage (V)', color='b')
ax1.tick_params('y', colors='b')

ax1.set_xlim([0, max(bias_current)])
# Create a grid for the second y-axis
# Get the limits of the second y-axis
y1_min, y1_max = ax1.get_ylim()
ax1.set_ylim(0, y1_max * 1.1)  # Adjust the limits as needed

# Create custom grid lines
for y in ax1.get_yticks():
    ax1.axhline(y=y, color='b', linestyle='-', alpha=0.3, linewidth=0.5)



# Create a second y-axis
ax2 = ax1.twinx()
ax2.scatter(left_boundary, counts_1[left_boundary], color='r', zorder=5)
ax2.plot(bias_current, counts_1, 'r-', label='Power')
ax2.set_ylabel('Counts', color='r')
ax2.tick_params('y', colors='r')

# Create a grid for the second y-axis
# Get the limits of the second y-axis
y2_min, y2_max = ax2.get_ylim()
ax2.set_ylim(0, y2_max * 1.1)  # Adjust the limits as needed
ax2.set_xlim([0, max(bias_current)])
# Create custom grid lines
for y in ax2.get_yticks():
    ax2.axhline(y=y, color='r', linestyle='-', alpha=0.3, linewidth=0.5)

for x in ax1.get_xticks():
    ax2.axvline(x=x, color='k', linestyle='-', alpha=0.3, linewidth=0.5)
# Print the maximum values and their position
print(f"Maximum Counts: {max_counts} at Bias Current: {max_bias_current}")


# Highlight the maximum point
ax2.scatter(max_bias_current, max_counts, color='r', zorder=5)
ax2.text(max_bias_current, max_counts, f'Critical Current ({max_bias_current}, {max_counts})',
         fontsize=12, verticalalignment='bottom', horizontalalignment='right')


# Display the plot
plt.show()