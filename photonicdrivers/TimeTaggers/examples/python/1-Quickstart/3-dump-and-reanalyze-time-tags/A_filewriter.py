"""To dump time tags efficiently to your hard drive, you can use the FileWriter measurement class.
These files can be read by the Virtual Time Tagger (example 3-B) to re-analyze the data just like you
do it on-the-fly, or by the FileReader (example 4-A) that provides access to the raw time tags.
In this example, we compare the effect of different start methods (autostart, startFor,
and start by SynchronizedMeasurements) and learn how to configure the FileWriter."""

import os
import TimeTagger
from time import sleep
import tempfile


def print_folder_content(folder):
    """Print filename and size of the files in the folder."""
    print("Filename            |       Size")
    print("--------------------+-----------")
    filenames = os.listdir(folder)
    for filename in [filenames[-1]] + filenames[:-1]:
        print("{:<20}|{:>8.1f} kB".format(filename, os.path.getsize(folder + os.sep + filename)/1024))


# Create a TimeTagger instance to control your hardware
tagger = TimeTagger.createTimeTagger()

# Enable the test signal on channels 1 and 2
tagger.setTestSignal(1, True)
tagger.setTestSignal(2, True)

# In the following, we repeat the data acquisition several times in slightly
# different ways. Follow the output in your console to learn about the differences.
print()
print("In the first round, we just create a FileWriter measurement that will be stopped and resumed three times.")
input("-> Press Enter to run")

# We use a temporary directory here. If you want to store data permanently, use a permanent
# directory on your hard drive.
tempdir = tempfile.TemporaryDirectory()

# The FileWriter is instantiated just like any other measurement class
filewriter = TimeTagger.FileWriter(tagger=tagger,
                                   filename=tempdir.name + os.sep + "filewriter",
                                   channels=[1, 2])

# Start and stop the measurement several times to observe the result in the folder
for i in range(3):
    sleep(.1)
    filewriter.stop()
    print("\nAfter run {}:".format(i))
    print_folder_content(tempdir.name)
    filewriter.start()

del filewriter
tempdir.cleanup()

print("""
The FileWriter created four files: The header file filewriter.ttbin and one data file for every new start.
The data files get enumerated names <main_filename>.<index>.ttbin.

In the second round, we use startFor instead of start/stop.""")
input("-> Press Enter to run")

tempdir = tempfile.TemporaryDirectory()
filewriter = TimeTagger.FileWriter(tagger, tempdir.name + os.sep + "filewriter", [1, 2])

for i in range(3):
    filewriter.startFor(int(1E11))  # instead of start/stop, we use startFor now
    filewriter.waitUntilFinished()
    print("\nAfter run {}:".format(i))
    print_folder_content(tempdir.name)

del filewriter
tempdir.cleanup()

print("""
The result is similar, but the data files have similar sizes, because the timing is
more precise. However, there are four data files with a very small one, named filewriter.1.ttbin. This file
is created when the FileWriter object has been initialized (autostart). The files with indices
2 to 4 have been created by our startFor calls.

The autostart behavior is suppressed when you use the FileWriter with SynchronizedMeasurements. This is the
recommended way to use the FileWriter and it is very useful when you want to analyze data on the fly
and store the same data for later re-analysis.""")
input("-> Press Enter to run")

tempdir = tempfile.TemporaryDirectory()
synchronized = TimeTagger.SynchronizedMeasurements(tagger)

# This FileWriter will not start automatically, it waits for 'synchronized'
filewriter = TimeTagger.FileWriter(synchronized.getTagger(), tempdir.name + os.sep + "filewriter", [1, 2])

for i in range(3):
    synchronized.startFor(int(1E11))  # now the measurement is controlled by SynchronizeMeasurements
    synchronized.waitUntilFinished()
    print("\nAfter run {}:".format(i))
    print_folder_content(tempdir.name)

del filewriter
del synchronized
tempdir.cleanup()

print("""
New data files may not only be started by a new start/startFor command. You can also set a maximum file
size for the data files. The FileWriter starts a new file after the maximum size is exceeded. As the
data is stored blockwise, the actual file size may exceed the specified size (here it's 500 kB) by up to
one block size.""")
input("-> Press Enter to run")
print("")
tempdir = tempfile.TemporaryDirectory()
synchronized = TimeTagger.SynchronizedMeasurements(tagger)
filewriter = TimeTagger.FileWriter(synchronized.getTagger(), tempdir.name + os.sep + "filewriter", [1, 2])
filewriter.setMaxFileSize(500 * 1024)

synchronized.startFor(int(5E11))
synchronized.waitUntilFinished()
print_folder_content(tempdir.name)

number_of_events = filewriter.getTotalEvents()
file_size = filewriter.getTotalSize()
print("\nStoring these data requires {:.2f} bytes/tag".format(file_size/number_of_events))
del filewriter
del synchronized
tempdir.cleanup()

TimeTagger.freeTimeTagger(tagger)
