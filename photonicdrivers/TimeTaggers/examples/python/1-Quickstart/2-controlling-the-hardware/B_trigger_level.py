"""The trigger level is the voltage value that is compared to your input signal in the very first
stage in the Time Tagger. The built-in test signal cannot be used to demonstrate the effect of the
trigger level setting as it is injected in a subsequent stage. However, we can check the accuracy
of the trigger level of your device in this example: at a setting of 0 V, the input noise of the
unconnected input triggers the comparator randomly. We scan the voltage range around 0 V
to determine the noise level."""

from matplotlib import pyplot as plt
import numpy as np
import TimeTagger
import sys

# Create a TimeTagger instance to control your hardware
tagger = TimeTagger.createTimeTagger()
inputs = tagger.getChannelList(TimeTagger.ChannelEdge.Rising)

# If using the Time Tagger X, the input hysteresis value should be set to the lowest possible value for all input channels.
if tagger.getModel() == 'Time Tagger X':
    [tagger.setInputHysteresis(input,  1) for input in inputs]

# With getDACRange(), we can check the minimum and maximum values of the trigger level. A Time
# Tagger 20 only accepts positive values, while a Time Tagger Ultra and Time Tagger X take negative values as well.
if tagger.getDACRange()[0] < 0:
    levels = np.linspace(start=-0.01, stop=0.01, num=200)
    print("Scan trigger levels from -10 mV to 10 mV:")
else:
    levels = np.linspace(start=0, stop=0.01, num=100)
    print("Scan trigger levels from 0 mV to 10 mV:")
countrate = TimeTagger.Countrate(tagger=tagger, channels=inputs)
results = list()

for level in levels:
    for inp in inputs:
        tagger.setTriggerLevel(channel=inp, voltage=level)
    countrate.startFor(int(1E8))
    countrate.waitUntilFinished()
    results.append(countrate.getData())
    sys.stdout.write("Trigger level: {:2.3f} mV, Overflows: {:<7}\r".format(level * 1000, tagger.getOverflowsAndClear()))
print("\nDone\n")

try:
    if tagger.getSensorData()[0]["calibration"]["high jitter warning rising"]:
        print("""Caused by extremely high noise frequencies in the input stages, your Time Tagger
    experienced a calibration error. These frequencies are beyond the specifications
    of the Time Tagger and cannot be handled correctly.""")
        if tagger.getModel() == "Time Tagger X":
            print("Look at the channel LEDs of your Time Tagger X: Red lights indicate calibration errors.")
        input("""With incoming input signals that are within the specifications, the Time Tagger would
    quickly re-calibrate itself. However, there is no input signal at the moment. You can
    use the autoCalibration() function instead, that uses the test signal for re-calibration.
    Press Enter to re-calibrate the Time Tagger.""")
        tagger.autoCalibration()
except TypeError:
    pass

result_array = np.array(results)
if result_array.any():
    plt.figure()
    plots = plt.plot(levels, result_array)
    plt.title("Trigger level scan")
    plt.xlabel("Trigger level (V)")
    plt.ylabel("Countrate (counts/s)")
    plt.legend(plots, ["Input " + str(inp) for inp in inputs])
    plt.show()
else:
    print("""For your device, no noise clicks occurred for the given trigger level range.
All acquired counts are 0.
You can still see from the code of this example how the trigger levels can be set.""")

TimeTagger.freeTimeTagger(tagger)
