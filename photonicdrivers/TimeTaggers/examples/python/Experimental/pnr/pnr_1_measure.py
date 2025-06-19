"""
Use this script to measure calibration time tags.
You will need to adjust the settings in pnr_constants.py file to your specific
configuration.
"""

import TimeTagger
from pnr_constants import FRONT_EDGE, REAR_EDGE, LASER_CHANNEL, FOLDER, FILENAME


DURATION = 5E12

# Adjust these settings according to your setup
DETECTOR_TRIGGER_LEVEL = 0.5
LASER_TRIGGER_LEVEL = 0.5

# Setup the tagger, the ConditionalFilter ensures the sequence falling edge -> laser
tagger = TimeTagger.createTimeTagger()
tagger.setTriggerLevel(FRONT_EDGE, DETECTOR_TRIGGER_LEVEL)
tagger.setTriggerLevel(LASER_CHANNEL, LASER_TRIGGER_LEVEL)

# Run file dump for defined duration
sync = TimeTagger.SynchronizedMeasurements(tagger)
fw = TimeTagger.FileWriter(tagger=sync.getTagger(),
                           filename=FOLDER + FILENAME,
                           channels=[FRONT_EDGE, REAR_EDGE, LASER_CHANNEL])
sync.startFor(DURATION)
sync.waitUntilFinished()
