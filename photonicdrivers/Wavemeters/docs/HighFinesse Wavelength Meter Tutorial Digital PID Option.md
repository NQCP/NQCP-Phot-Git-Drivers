HighFinesse Tutorial
HighFinesse Digital PID Option:
Laser Control
HighFinesse Tutorial · Digital PID option · 8-2023
This document provides general information only and may be subject to change at any time without prior notice.

Overview Further information
How to …
… set up the HighFinesse Digital PID Option:
Laser Control
This option can be used with TOPTICA lasers controlled by a DLC pro only.
This quickstart guide is intended to give you a brief overview of how to configure
the HighFinesse laser control settings. The guide does not replace reading the
manual. Make sure you have read and understood it (especially section 3.5) Quick Start Guide
before you start the regulation. Setting voltage bounds incorrectly might cause HighFinesse Wavelength Meter
damage to your laser.
https://www.highfinesse.com
Here we assume that the laser is already successfully connected with a fiber to /en
the wavelength meter. If you have any questions about that refer to the quickstart /support
guide “HighFinesse Wavelength Meter” /quick-start-guide.html

1 2
1a
Start the software and set the voltage bounds in the Laser Control Menu Click on the black triangle 1a to obtain
such that you can exclude a damage to your laser and make sure the output more settings. Move to the frame bounds
range is suitable (e.g. as defined by a mode-hope-free scanning range). to enter the correct bounds.

3
Connect the DLC pro Controller and the computer running the wavemeter software
to the same network (UDP has to be allowed for automatic recognition).
In restrictive network it might be necessary to specify the IP address and the port of the DLC pro
Controller (Standard port: 1998) in the “Adjust ports” menu → “Additional IPs”.

Using multiple channels
4 4a 4b
Click to Click again to
simultaneously
assign … unassign …
Choose the port where the digital Then click on one of the colored You can unassign it by clicking on the
signal will be put out by clicking numbers to assign the switch signal same number again. In the example the
on the black numbers. to the port. Switch signal 5 is assigned to port 1.

4c
In this example, the light
output of the laser is
connected to channel 5
on the switch.
Both channel 5 and the
You can use the “Adjust ports” menu correct laser are assigned
for assigning the lasers to the ports. to digital Port 1.

5 6
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

7 7a
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
| 8   | 8a  | 8b  |
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

9
Click on the blue triangles to
enter the bounds 9a (range should
be smaller or equal to the bounds
9b Click to determine
in 1.) and number of collection
the sensitivity …
points used for calculation.
Then click on the red dot 9b
9a Click to enter
to automatically determine the
the bounds …
sensitivity. Once this is determined
transfer the result to the frame
“Regulation” and enter it as the
“Sensitivity” of the laser.
Caution: this will vary the output
voltage, so a safe choice for the
bounds is important.

10
10b
10c Get the current
wavelength
Click to enter the
10a
current voltage ...
Click on the blue triangle 10a .
Enter the current voltage .
10b
Get the corresponding wavelenth
by clicking on the red dot 10c .

11 11a 11b
Click to determine
the PID parameters.
Press “Auto TPID” to determine the
PID parameters. Finally, you can close
In this example the laser should the PIDSim2. Now the system should
Enter a target wavelength or a function. be stabilized at 632.9910722 nm. be ready for a test.

12
For this start the Regulation.
You can optimize the regulation further
by using the LongTerm application and
minimizing possible unwanted effects
by altering the PID parameters.

HighFinesse GmbH T + 49 (0) 7071 - 53 918 0 Additional information
Wöhrdstraße 4 F + 49 (0) 7071 - 53 918 99 and distributors:
72072 Tübingen, Germany M info@highfinesse.com www.highfinesse.com
© HighFinesse GmbH 2023