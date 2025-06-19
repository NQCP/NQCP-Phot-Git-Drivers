"""This script serves to calibrate the measurements for counting the number of
photons.
The results can be used with the TimeTagger.Experimental.PhotonNumber virtual channel.

Here, the Histogram2D measurement will take the information on the time
differences between the trigger signal and the front and rear edges of the
resulting signal.
The typical distribution of the points is tilted to obtain the best condition
to observe the separation between the peaks associated with the photon numbers.

The results necessary for the virtual channel are:
x_intercepts: corresponds to the series of points separating the regions associated
with the different number of photons. The series is defined as the intercept
on the axis of the front edges of the lines separating the previously defined
regions in the original 2D Histogram
slope: corresponds to the slope of the tilt of the 2D histogram.
"""

from pnr_constants import FRONT_EDGE, REAR_EDGE, LASER_CHANNEL, FOLDER, FILENAME
from json import dump
import TimeTagger
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks


def tilt(original_data, slope):
    # Rotate the image, performing a shift line by line of the 2D histogram
    tilted_data = np.zeros((n_bins_rear, n_bins_front), dtype=float)
    for i in range(1, n_bins_rear):
        shift = slope * i
        index_shift = int(np.floor(shift))
        fractional_shift = shift - index_shift
        tilted_data[i, index_shift:-1] = fractional_shift*original_data[i,
                                                                        :(n_bins_front-index_shift-1)] + (1-fractional_shift)*original_data[i, 1:(n_bins_front-index_shift)]
    return tilted_data


# Input parameters
n_bins_front = 1000
w_bins_front = 1
# Preliminary numbers. They'll be optimized below
n_bins_rear = 5000
w_bins_rear = 1


# Create Time Tagger object
tagger = TimeTagger.createTimeTaggerVirtual()
tagger.setReplaySpeed(-1)

# Find the maximum position of front edges to shift the laser trigger to the
# front
start_stop_front = TimeTagger.StartStop(tagger=tagger,
                                        click_channel=LASER_CHANNEL,
                                        start_channel=FRONT_EDGE,
                                        binwidth=w_bins_front)
# Find the maximum position of rear edges to adjust binning
start_stop_rear = TimeTagger.StartStop(tagger=tagger,
                                       click_channel=LASER_CHANNEL,
                                       start_channel=REAR_EDGE,
                                       binwidth=w_bins_rear)

tagger.replay(file=FOLDER + FILENAME)
tagger.waitForCompletion()

# Front maximum position
front_data = start_stop_front.getData()
front_center = front_data[front_data[:, 1].argmax(), 0]
delay = front_center + (n_bins_front*w_bins_front)//2
tagger.setInputDelay(LASER_CHANNEL, -delay)
# Rear maximum position
rear_data = start_stop_rear.getData()
rear_center = rear_data[rear_data[:, 1].argmax(), 0]
# new position after the laser negative delay
rear_peak = delay - rear_center

# Adjust rear edge binning
# check if rear peak is inside the binning, otherwise adjust the width to avoid having a massive matrix
n_bin_max = 5000
iter = 0
if n_bins_rear < rear_peak:
    n_bins_tmp = rear_peak
    while n_bin_max < n_bins_tmp:
        iter += 1
        n_bins_tmp = round(rear_peak + 5000, -4) // (iter*2)
    n_bins_rear = n_bins_tmp
    w_bins_rear = iter*2

# Measurement of the 2d histogram
data = TimeTagger.Histogram2D(
    tagger, LASER_CHANNEL, REAR_EDGE, FRONT_EDGE, w_bins_rear, w_bins_front, n_bins_rear, n_bins_front)

tagger.replay(file=FOLDER + FILENAME)

# Data loading
while not tagger.waitForCompletion(timeout=0):
    plt.figure(1)
    plt.pcolormesh(data.getIndex_2(), data.getIndex_1(),
                   data.getData(), shading="auto")

    plt.pause(.1)


plt.figure(1)
plt.colorbar()
plt.title('Hist 2D, before angle correction')
plt.xlabel('Trigger, CH'+str(REAR_EDGE) + ' front edge [ps]')
plt.ylabel('Trigger, CH'+str(abs(FRONT_EDGE)) + ' rear edge [ps]')
plt.set_cmap('jet')


# Rotation of the 2D histogram to find the best conditions to distinguish the
# peaks
raw_data = np.array(data.getData(), dtype=float)
sum_squared = np.sum((np.sum(raw_data, axis=0) ** 2))
best_slope = 0

for slope in np.linspace(1, 1000, 1000)/(10000/w_bins_rear):
    # Evaluation of the best conditions to emphasize the separation between
    # the peaks, and distinguish better the photon number contribution.
    sum_squared_new = np.sum((np.sum(tilt(raw_data, slope), axis=0) ** 2))
    if sum_squared_new <= sum_squared:
        break
    sum_squared = sum_squared_new
    best_slope = slope

# Find local minima
tilted_data = tilt(raw_data, best_slope)
front_opt = np.sum(tilted_data, axis=0)
maxima_front, prop = find_peaks(front_opt, height=(
    max((front_opt)) + min((front_opt)))/4, distance=10)
x_intercepts = list()
for k in range(np.size(maxima_front)-1, 0, -1):
    avg = (maxima_front[k] + maxima_front[k-1])/2
    x_intercepts.append((1 + best_slope / w_bins_rear) * delay - avg)
x_intercepts.insert(0, x_intercepts[0] - 200)
x_intercepts.append(x_intercepts[-1] + 200)

with open(FOLDER + "parameters_ch"+str(abs(FRONT_EDGE))+".json", "w") as param_file:
    dump(dict(x_intercepts=x_intercepts,
         slope=best_slope / w_bins_rear, delay=int(delay)), param_file)
    print(
        f'Parameters exported to {FOLDER}parameters_ch{abs(FRONT_EDGE)}.json')

# Plot of the comparison of histograms before and after the optimization. The
# histograms are obtained after the integration along the rear-edge's axis
plt.figure(2)
plt.plot(data.getIndex_2(), np.sum(raw_data, axis=0), label='Original')
plt.plot(data.getIndex_2(), front_opt, label='Optimized')
plt.legend()
plt.xlabel(f'Trigger, CH{REAR_EDGE} front edge [ps]')
plt.title(f'Hist,  click CH {LASER_CHANNEL},  stop CH {FRONT_EDGE}')


# Plot of the 2D Histogram after rotation
plt.figure(3)

plt.pcolormesh(data.getIndex_2(), data.getIndex_1(),
               tilted_data, shading="auto")
plt.title('Hist 2D, after angle correction')
plt.xlabel(f'Trigger, CH{REAR_EDGE} front edge [ps]')
plt.ylabel(f'Trigger, CH{abs(FRONT_EDGE)} rear edge [ps]')
plt.colorbar()

plt.show()

TimeTagger.freeTimeTagger(tagger)
