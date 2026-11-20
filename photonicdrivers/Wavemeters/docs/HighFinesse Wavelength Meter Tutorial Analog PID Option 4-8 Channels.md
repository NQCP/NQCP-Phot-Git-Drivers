HighFinesse Tutorial
HighFinesse Analog PID Option
(4 or 8 Channels): Laser Control
HighFinesse Tutorial · Analog PID 4 or 8 · 8-2023
This document provides general information only and may be subject to change at any time without prior notice.

Overview Further information
How to …
… set up the HighFinesse Analog PID Option
(4 or 8 channels): Laser Control
The PCIe card will provide up to ± 10 V for controlling the lasers. This tutorial is
intended to give you a brief overview of how to configure the HighFinesse laser control
settings. The tutorial does not replace reading the manual. Make sure you have Quick Start Guide
read and understood it (especially section 3.5) before you start the regulation. Setting HighFinesse Wavelength Meter
voltage bounds incorrectly might cause damage to your laser.
https://www.highfinesse.com
Here we assume that the laser is already successfully connected with a fiber to the /en
wavelength meter. If you have any questions about that refer to the quickstart guide /support
“HighFinesse Wavelength Meter”. /quick-start-guide.html

1
Insert the PCIe card to a suitable PCIe slot on your computer and install the
wavemeter software (which installs all drivers automatically).

2 3
Start the software and set the voltage bounds in the Laser Control Menu
such that you can exclude a damage to your laser and make sure the output Move to the frame bounds to
range is suitable (e.g. as defined by a mode-hope-free scanning range). enter them correctly.

4
Connect the voltage output of the PCIe card to the input at the laser using
the adapter cable (minimum impedance at the laser input 10 kOhm).

Using multiple channels
Click to Click again to
| 5   | 5a  | 5b  |
| --- | --- | --- |
simultaneously
assign … unassign …
Choose the port where the voltage  Then click on one of the colored You can unassign it by clicking on the
will be put out by clicking on the black  numbers to assign the switch signal same number again. In the example the
| numbers. | to the port. | Switch signal 5 is assigned to port 2. |
| -------- | ------------ | -------------------------------------- |

6 7
Start …
PIDSim2.exe
Type: Application
Start the PIDSim2 application
located in the path …
Use the PIDSim2 Tool to simu-
late good starting parameters. Installation Path of the
wavemeter Software
Alternatively, you can set PID
\Tools
parameters manually in the
\PIDSim2.exe
laser control settings/frame:
“Regulation & Sensitivity”. … and make sure you can measure.

8 8a
PIDSim2 Settings
Measurement count:
number of points in the simulation.
Time/Measurement [s]:
get this live from the wavemeter by clicking
on the red dot and confirm by clicking on the
checkmark.
Response Count:
2 for single channel, 1 for multichannel
measurements.
Set the minimum and maximum output
according to your system (voltage bounds
set in 1.).
Clicking on the small black triangle Now you can make your settings Set the resolution to obtain a realistic
will enable more settings. for simulation. simulation of your system.

Show more settings …
| 9   | 9a  | 9b  |
| --- | --- | --- |
Choose …
Choose to synchronize the
PIDSim2 in the section regulation.
Choose PIDSim --> WLM.
The tool can be used as a pure
| simulation tool or synchronized | You can alternatively also transfer |     |
| ------------------------------- | ----------------------------------- | --- |
to the wavelength meter software all settings you have made from the  After that set the port that
running in parallel. wavemeter to the PIDsim2 tool. you would like to adjust.

10
Click on the blue triangles to
enter the bounds 10a (range should
be smaller or equal to the bounds
10b Click to determine
in 1.) and number of collection
the sensitivity …
points used for calculation.
Then click on the red dot 10b
10a Click to enter
to automatically determine the
the bounds …
sensitivity. Once this is determined
transfer the result to the frame
“Regulation” and enter it as the
“Sensitivity” of the laser.
Caution: this will vary the output
voltage, so a safe choice for the
bounds is important.

11
11b
11c Get the current
wavelength
Click to enter the
11a
current voltage ...
Click on the blue triangle 11a .
Enter the current voltage .
11b
Get the corresponding wavelenth
by clicking on the red dot 11c .

12 12a 12b
Click to determine
the PID parameters.
Press “Auto TPID” to determine the
PID parameters. Finally, you can close
In this example the laser should the PIDSim2. Now the system should
Enter a target wavelength or a function. be stabilized at 632.9910722 nm. be ready for a test.

13
For this start the Regulation.
You can optimize the regulation further
by using the LongTerm application and
minimizing possible unwanted effects
by altering the PID parameters.

HighFinesse GmbH T + 49 (0) 7071 - 53 918 0 Additional information
Wöhrdstraße 4 F + 49 (0) 7071 - 53 918 99 and distributors:
72072 Tübingen, Germany M info@highfinesse.com www.highfinesse.com
© HighFinesse GmbH 2023