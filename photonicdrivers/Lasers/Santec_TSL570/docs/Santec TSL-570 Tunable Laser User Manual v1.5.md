Tunable Semiconductor Laser
TSL-570
Operation Manual

TSL-570 OPERATION MANUAL
Notes to Users
1) Copyright 2023, Santec LIS Corporation. All rights reserved. No part of this
Operation Manual may be reproduced or transmitted in any form or by any
means, electronic or mechanical, for any purpose, without the prior written
permission of Santec.
2) Information in this Operation Manual is subject to change without notice.
3) Information of this Operation Manual is prepared with careful examination,
however, in the event of any mistake, please contact us.
Notes in Bringing This Product Out of Japan
1) When this product is brought out of Japan, some laws or regulations of a
destination country may prohibit this product from being used there. In such
countries, the use of this product may lead to punishment. Please note, that in
such cases Santec Corporation shall not be held responsible in anyway.
2) When this product is exported (or brought out of Japan), if this product is
applicable to a strategic material specified in “Foreign Exchange and Foreign
Trade Control Law”, then required is an export permit of the Japanese
Government under the law.
2 / 113

Tunable Semiconductor Laser TSL-570
Introduction
Thank you very much for your having purchased our product, Tunable
Semiconductor Laser TSL Series. This Operation Manual contains information
necessary for the operation of TSL-570, and it is intended for those with
sufficient knowledge enough to of laser danger and its safe control. Before
operating TSL-570, you should first read thoroughly through this Operation
Manual and become familiar to its contents. After reading this Operation Manual,
keep it at your fingertip for easy reference at any time.
NOTE
The packing materials and box of this product are needed for long-term
storage or transportation; keep them in a safe place after unpacking the
product.
3 / 113

TSL-570 OPERATION MANUAL
How to Read the Manual
Before operating TSL-570, please carefully read this Operation Manual. This
Operation Manual consists of 11 Chapters:
Chapters 1 to 4 illustrate the outline of this product, safety precautions, and
installation of the product.
SANTEC recommends that Chapter 1 to 4 should be read carefully before
proceeding to the following chapters.
Chapters 5 to 7 describe how to operate the product.
Chapter 8 to 11 describes to maintain the products’ performances.
NOTE
Before using this product, please carefully read this Operation Manual.
4 / 113

                                       Tunable Semiconductor Laser TSL-570

Explanation of Terms

The meanings of the following terms used in this Operation Manual are defined
as below:
(1) Meaning
|     |         | This indicates pressing DANGER, and if  |
| --- | ------- | --------------------------------------- |
|     | DANGER  | it is not avoided, personnel death or   |

serious injury may result; therefore, it
is the most emphasized special
information.
|     |          | This indicates potential danger, and if it  |
| --- | -------- | ------------------------------------------- |
|     | WARNING  | is not avoided, personnel death or          |
serious injury may result; therefore, it
is special information.
|     |          | This indicates potential danger, and if it  |
| --- | -------- | ------------------------------------------- |
|     | CAUTION  | is not avoided, mild or slight injury may   |
|     |          | result; therefore, it is special            |
information. It also indicates potential
danger leading to only physical
damage.
|        |       | This section only indicates             |
| ------ | ----- | --------------------------------------- |
|  NOTE  | NOTE  | supplementary explanations of the text  |
|        |       | and thus other than DANGER,             |
WARNING, and CAUTION.

(2) Importance of Information
From the above meanings, the priority of the terms here are as shown below:

DANGER > WARNING > CAUTION > NOTE

 5 / 113

TSL-570 OPERATION MANUAL
Contents
Introduction
How to Read the Manual
Instrument Markings
Explanation of Terms
1. Safety Notes ...................................9
1.1. Intended use ............................................................... 9
1.2. Safety Markings ............................................................ 9
1.3. Laser Class .................................................................10
2. Product Composition ..................... 11
3. Panel Descriptions ......................... 12
3.1. Front Panel .................................................................12
3.2. Rear Panel ..................................................................12
3.3. Side Panel ..................................................................13
4. Installation ................................... 14
4.1. Operating Environments ...............................................14
4.2. Power Supply ..............................................................14
4.3. Optical Output .............................................................15
4.4. Interlock ....................................................................15
5. Basic Operation ............................. 17
5.1. Turning on the Unit ......................................................17
5.2. LCD display and Operation ............................................17
5.2.1. Screen Configuration .................................................... 17
5.2.2. Numeric Keypad Input Screen Configuration .................... 18
5.2.3. Menu screen transition ................................................. 19
5.3. Laser Output ...............................................................20
5.4. Setting the Wavelength ................................................20
6 / 113

Tunable Semiconductor Laser TSL-570
5.5. Setting the Output Power ..............................................22
5.6. Setting the Wavelength Sweep ......................................24
5.6.1. Continuous sweep setting ............................................. 27
5.6.2. Trigger setting for continuous sweep .............................. 30
5.6.3. Step sweep setting ...................................................... 31
5.6.4. Trigger setting for step sweep........................................ 32
5.6.5. Detailed trigger settings ................................................ 33
5.7. Executing the Wavelength Sweep...................................34
5.8. Turning off the Unit .....................................................35
6. Detailed Operation ........................ 36
6.1. Fine-tuning .................................................................36
6.2. Coherence Control .......................................................37
6.3. External Modulation .....................................................38
6.4. Power Monitor Signal Output .........................................41
6.5. Trigger Setting ............................................................42
6.6. Displaying the Product Information .................................44
6.7. System Alert ...............................................................45
6.8. System Settings ..........................................................47
6.9. Save/ Load Setting parameters ......................................47
7. Operation by Communication ........ 49
7.1. GPIB ..........................................................................49
7.1.1. Connection ................................................................. 49
7.1.2. GPIB Function ............................................................. 49
7.1.3. Setting the Address, Delimiter and Command set ............. 50
7.2. USB ...........................................................................52
7.2.1. Connection ................................................................. 52
7.2.2. Communication Conditions and System Requirements ....... 52
7.2.3. Installing a USB Driver Software .................................... 52
7.3. LAN ...........................................................................54
7.3.1. Connection ................................................................. 54
7.3.2. Communication Conditions and System Requirements ....... 55
7.3.3. Settings ..................................................................... 55
7 / 113

TSL-570 OPERATION MANUAL
7.4. Command Reference ....................................................56
7.4.1. Common Command List ............................................... 56
7.4.2. TSL-570 Status system ................................................. 57
7.4.3. IEEE-488.2 common commands - Detailed description ...... 59
7.4.4. TSL-570 Specific command overview .............................. 62
7.4.5. Command error ......................................................... 100
7.4.6. System alert ............................................................. 100
8. Specifications .............................. 102
8.1. Specifications ............................................................ 102
8.2. Regulations conformity ............................................... 103
9. Maintenance ............................... 104
9.1 Daily Maintenance ..................................................... 104
9.2 Cleaning the Optical Power Sensor ............................... 104
9.3 Replacing Fuses ......................................................... 104
9.4 Inspection and Calibration ........................................... 105
9.5. Self-Inspection .......................................................... 105
9.6. Firmware update ....................................................... 106
9.7. Long-term Storage .................................................... 108
10. Re-packing and shipping ............. 110
10.1. Re-packing ............................................................... 110
10.2. Packing Instruction .................................................... 110
10.3. Shipping ................................................................... 111
11. Troubleshooting .......................... 112
8 / 113

Tunable Semiconductor Laser TSL-570
1. Safety Notes
1.1. Intended use
This product is designed to measure the optical characteristics.
Do not use this product for anything other than as an optical measuring
instrument. If this product is used in a manner not specified in this manual, the
protection provided by this product may be impaired.
1.2. Safety Markings
This product is marked with this warning symbol when it is necessary
for the user to refer to the instructions in the manual.
This warning symbol is marked on products which have a laser output.
9 / 113

TSL-570 OPERATION MANUAL
1.3. Laser Class
This product is classified class 1M laser product according to IEC 60825-1 (2014).
Laser Type: External Cavity Diode Laser
Laser Class: 1M IEC60825-1(2014)
Output Power: < 50mW
Laser Diameter: 10μm
Numerical aperture: 0.1
Wavelength: 1200-1700nm
Laser Safety Labels
This product radiates class 1M invisible laser. Do not look at the tip of optical
output connector using optical instruments like magnifiers or microscopes. The
laser radiation can seriously damage your eyesight. Please pay attention to
handling of laser.
10 / 113

Tunable Semiconductor Laser TSL-570
2. Product Composition
This product is composed of the TSL-570 body and accessories. Check to make
sure that all the following items are included.
TSL-570 body x1
Power code x1 Interlock terminator x1
Operation Manual & Software x1
Inspection report x1
Check to make sure that the product body and the accessories have no
scratches or stains. If any item is found to have scratches or stains, please
contact us.
11 / 113

TSL-570 OPERATION MANUAL
3. Panel Descriptions
3.1. Front Panel
Display and Touch screen Optical Output Activation key
USB (Host)
Power On/Off Optical Output
And ED indicator Connector (inside)
Figure 3-1. Front Panel
3.2. Rear Panel
3.3.
Power inlet and Fuse Box GPIB connector LAN connector Exhaust Fan
GND
USB (Device)
Analog Input
Power monitor
External Interlock T r ig g e r Input Trigger Output
putterlock
Interlock
Figure 3-2. Rear Panel
12 / 113

Tunable Semiconductor Laser TSL-570
NOTE
It is recommended to use the GND terminal as a signal GND. It is effective in
stabilizing the reference potential between devices when constructing a
measurement system that connects multiple devices, such as the Swept Test
System (STS) linked to our MPM series/PCU/OSU/MBU.
3.3. Side Panel
Air intakes
Legs
Rear feet
Figure 3-3. Side Panel
13 / 113

TSL-570 OPERATION MANUAL
4. Installation
4.1. Operating Environments
Pay attention to the following guidelines for safe, trouble-free operation.
This product is a high-precision device and be designed to be used indoors
(Pollution Degree 2).
· Do not place over a height of 2,000 meter.
· Do not place in direct sunlight.
· Do not place under high temperature and high humidity.
· Do not place in an environment with dust, dirt, salt, or corrosive gas.
· Do not place in an area subject to large vibrations.
· Do not place in an area subject to noise by electric field, magnetic field, etc.
· Do not place in an area where the unit is subject to falling objects landing on
it.
· Do not place with possible exposure to water.
Be sure to install the TSL-570 in a level place (less than 5 degree). It is
recommended to install this product on a vibration-proof base. The unit may
not operate correctly if the device is set in an inclined position.
The mainframe of the TSL-570 weighs about 7kg. Please ensure that the table
or shelf upon which it is installed has sufficient strength. Clearance of 5 cm at
the rear and the side of the unit should be allowed for proper ventilation. And
the air intakes are located at the bottom and the side of the device. Please do
not remove the rubber legs, in order to secure airflow.
4.2. Power Supply
This product uses a 3-line power cord and plug with a protective ground line.
Power cord may be attached and detached. Connect it to the power source
socket at the rear panel. Use the power cord supplied with the product. Do not
use the inappropriate power code. This product complies with overvoltage
category Ⅱ and can operate between 100 to 120Volts or 200 to 240 Volts, and
50 to 60Hz AC Line. Temporary over voltage (TOV) is 1,500 Volts. Use two
surge resistant type fuses. T3.15AL/250V (100–120V/ 200-240V) (Refer to "9-
3. Replacing Fuses").
14 / 113

Tunable Semiconductor Laser TSL-570
This product is grounded by the ground line in the supplied power cable. This
product must be properly grounded to avoid electrical shock and other dangers.
Please make sure that this product is properly grounded to avoid electrical shock.
In addition, please place this product in a location that allows the user to easily
unplug the power cable from the power socket on the rear panel, in case of any
device malfunction.
4.3. Optical Output
The TSL-570 has polarization maintaining fiber (PMF) outputs. The PMF is the
panda type, with polarization axis in alignment with connector key (slow axis).
4.4. Interlock
This product is equipped with a terminal for connecting an external interlock
circuit.
A terminator is connected to the interlock terminal at the time of factory
shipment (or included as an accessory). If an external interlock is used, remove
the terminator and connect a circuit to the interlock terminal. The Laser is
output only when there is a short circuit. The Laser turns off when the circuit
is open. If you want the Laser to light up again, short the circuit, and then
perform Laser output operation (Refer to “5-2. Laser output”).
If you don’t use your own interlock circuit, please connect the terminator to the
terminal (BNC) indicated as “ ”. If you use your own interlock circuit, please
connect the interlock circuit to the terminal indicated “INTERLOCK”. Keep the
removed terminator so it does not become lost.
15 / 113

TSL-570 OPERATION MANUAL
NOTE
Make sure to use this product only with the terminator connected when an
external interlock is not used. The Laser is not output unless the terminator is
connected. When " " is indicated in the display of the front panel, the
interlock circuit is in open state.
16 / 113

Tunable Semiconductor Laser TSL-570
5. Basic Operation
5.1. Turning on the Unit
1. Press the Power ON/OFF key at the lower left of the front panel.
2. The LED of the power ON/OFF key will turn green, and initialization will last
for about 60 seconds.
3. Wavelength and power values are displayed on the main display.
NOTE
Immediately after startup, "Warming up" is displayed on the LCD screen, and
depending on the usage environment, it may be displayed for about 30 to 60
minutes.
5.2. LCD display and Operation
5.2.1. Screen Configuration
The Main screen is the original screen of this device. When the power is
turned on, it is possible to first transition and read the status of the device.
You can also transition to all function pages from the page transition button.
For details, refer to "5.3.3 Menu Transition".
17 / 113

TSL-570 OPERATION MANUAL
Page transition button
Wavelength display area
Power display area
Unit display area
Status display area
5.2.2. Numeric Keypad Input Screen Configuration
1. Select the blinking cursor in the digit you want to enter.
The blinking cursor can be moved with the unit shift key.
Alternatively, you can select by directly touching the number.
2. Enter the value with the numeric keypad. All digits must be entered for
the integer part. When changing the value one by one, the operation of
the unit shift key is also available.
After inputting the value, press the ENTER key to set the value. When
inputting out of the specification range, the value in the enterable range
will turn yellow.
3. After setting, return to the Main screen.
Setting parameter Inputable range
parameter
Cancel key
Blinking cursor
Unit shift
NOTE
This product can be operated the screen by connecting a mouse to the USB
(Host) port. Then, the scroll wheel can allow the user to change the input
value.
18 / 113

Tunable Semiconductor Laser TSL-570
5.2.3. Menu screen transition
The screen transition diagram of this device is shown. The "Main", "Sweep",
and "Trigger" settings that are mainly used can be easily switched back and
forth, and detailed settings can be changed from the "Other" screen.
Please refer to the configuration diagram below.
Main
Trigger Other Communication
Sweep
Information
Maintenance
Save/Load
System
Alerts
Firmware
Upgrade
19 / 113

TSL-570 OPERATION MANUAL
5.3. Laser Output
Make sure that the optical fiber is connected correctly to the optical output
connector before performing LD output.
1. Press the Optical Output Activation key. The key top turns green and the
optical output becomes active. Laser is output from the optical output
connector during the LED illuminate. While preparing to turn on laser, the
“ACTIVE” key blinks.
2. Press the Optical Output Activation key again to turn off optical output. Laser
output is interrupted and the LED turns off.
NOTE
When “ ” is displayed on the main screen of the front panel, the interlock
circuit is open and the Laser is not output.
5.4. Setting the Wavelength
1. Touch the number displayed to the right of Wavelength on the main
screen.
20 / 113

Tunable Semiconductor Laser TSL-570
2. The Numeric Keypad Input Screen appears, and it transitions to the state
where the wavelength can be set.
3. Input a value according to “5.2.2”. When inputting out of the specification
range, the value in the enterable range will turn yellow.
■ Changing the Unit of the Wavelength
1. Touch the unit on the wavelength setting screen.
2. The input unit is changed.
21 / 113

TSL-570 OPERATION MANUAL
3. To return to the previous unit, touch Unit again.
When setting the unit to Frequency, other settings are displayed for the
frequency. However, the following parameters do not change. Sweep
Speed setting is fixed at the Wavelength unit [nm/s]. Step width is fixed at
the Wavelength [nm].
5.5. Setting the Output Power
1. Touch the unit on the Power setting screen.
2. The Numeric Keypad Input Screen appears, and it transitions to the state
where the power can be set.
22 / 113

Tunable Semiconductor Laser TSL-570
3. Input a value according to “2-2”.
Range: -15dBm to +13dBm
NOTE
When a value is set that is greater than the maximum power, “ ” is
displayed on the screen. The wavelength and power accuracy are not
guaranteed while “ ” is displayed. Please decrease the setting power so
that “ ” turns off.
■ Changing the Unit of the Power
(1) Touch the unit on the power setting screen.
(2) The display/input unit is changed. All units will be changed on all screens,
including this screen.
(3) Do the same operation when switching back to the original setting.
When setting the unit to mW (linear scale), other settings are displayed for the
mW (linear scale). However, the following parameters do not change.
In case of Manual mode, the Attenuator value setting is fixed at the Attenuator
[dB].
■ Switching the Optical Power Control Mode
The power control of the optical output can be switched between Auto and
Manual. In auto control mode (Auto), the power of the output light is kept
constant by feedback from the output power value measured at the self-
contained power meter. The attenuator is controlled automatically. In manual
control mode (Manual), the injection current to the LD is controlled to be kept
constant.
(1) Touch Function on the Main screen.
23 / 113

TSL-570 OPERATION MANUAL
(2) It can be selected in Power Mode on the Setting screen.
“Auto” Auto Power control mode
“Manual” Manual control mode by internal attenuator
(3) Power mode is a manual control mode when “Attenuator” is displayed on
the main screen.
5.6. Setting the Wavelength Sweep
This section describes the wavelength sweep settings. This product has two
sweep modes: continuous sweep and step sweep. Make the following settings
to operate correctly in each mode.
Continuous sweep: A mode that continuously changes the wavelength within
the specified wavelength range.
24 / 113

Tunable Semiconductor Laser TSL-570
Step sweep: A mode that changes the wavelength within the specified
wavelength range with the specified feed width.
(A) Perform one-way sweep with step operation. Change the
Step and One way wavelength from the start wavelength to the stop wavelength
with the wavelength interval set by STEP and the wait time set
by Dwell. When the wavelength returns to the start wavelength,
the speed and time are not controlled.
(B) Perform two-way sweep with step operation. Change the
Step and Two way wavelength from the start wavelength to the stop wavelength
with the wavelength interval set by STEP and the wait time set
by Dwell. Afterwards, change the wavelength from the end
wavelength to the start wavelength in the same manner.
(C) Perform one-way sweep by changing the wavelength
Cont. and One way continuously. Change the wavelength from the start wavelength
to the stop wavelength with the speed set by Speed and return
to the start wavelength. The wait time between each sweep is
set by Delay. It does not include the time to return to the start
wavelength.
(D) Perform two-way sweep by changing the wavelength
Cont. and Two way continuously. Change the wavelength from the start wavelength
to the stop wavelength with the speed set by Speed. Afterwards,
change the wavelength from the stop wavelength to the start
25 / 113

TSL-570 OPERATION MANUAL
wavelength in the same manner. The wait time between each
sweep is set by Delay.
Continuous sweep setting
Setting Unit Description
parameter
Start nm Start wavelength
Stop (THz) Stop wavelength
Speed nm/s Sweep speed
Cycle times Number of wavelength sweeps
Delay sec The wait time between each sweep in continuous sweep operation
Step Width nm The interval of the trigger signal output
Start Trigger - Sweep start procedure setting
Constant Mode - Calculation setting of the trigger output
Wavelength The trigger is periodic output in wavelength using
the internal wavelength monitor.
Time: The trigger is periodic output in time.
Timing Mode - Timing setting of the trigger output
NONE Trigger signal is not output.
STOP Trigger signal is output at sweep completion.
START Trigger signal is output when sweep starts.
STEP Trigger signal is output at a constant interval
(wavelength or time) during sweep
Step sweep setting
Setting Unit Description
parameter
Start Nm Start wavelength
Stop (THz) Stop wavelength
Step The interval (wavelength) of step sweep
Cycle times Number of wavelength sweeps
Dwell sec Amount of time spent during each step
Timing Mode - Timing setting of the trigger output
NONE Trigger signal is not output.
26 / 113

Tunable Semiconductor Laser TSL-570
STOP Trigger signal is output at sweep completion.
START Trigger signal is output when sweep starts.
STEP Trigger signal is output at a constant interval
(wavelength) during sweep
The flow of the sweep operation is as follows.
1. Set to the start wavelength
2. Sweep operation
3. Stop at the stop wavelength
In the case of continuous sweep, when each sweep is completed, the
wavelength returns to the start wavelength and the operation is executed for
the number of cycles.
NOTE
When stopping sweep operation in the middle, follow "5-6-6 Stop Sweep".
The number of sweeps displayed returns to 0 when the number exceeds
1000. If the mode is set to Two way, one round trip counts as two.
5.6.1. Continuous sweep setting
1. Touch the “Sweep” tab.
2. After the screen switches to the Sweep setting screen, set Sweep Mode. The
Continuous sweep has one-way operation "Cont and One way" and two-way
operation "Cont and Two way".
27 / 113

TSL-570 OPERATION MANUAL
3. Input the sweep start wavelength and sweep stop wavelength according to
“5-4. Setting the wavelength”.
4. Touch the number on the right side of Speed to more to the sweep speed
setting screen.
5. Select a sweep speed from the Sweep Speed setting screen.
28 / 113

Tunable Semiconductor Laser TSL-570
6. Touch the “Setting” on the Sweep setting screen to perform detailed settings.
7. Set the following parameters on the detailed setting screen.
Parameter Unit Description
Cycles times Set the Number of wavelength sweeps. After each sweep
completes, the wavelength is set at the stop wavelength. If the
mode is set to Two way, one round trip counts as two. When
setting the Cycles to “0” (Zero), the sweep times is infinite.
Delay sec Set the wait time between each sweep in continuous sweep
operation.
Step width nm Set the interval of the trigger signal output.
29 / 113

TSL-570 OPERATION MANUAL
5.6.2. Trigger setting for continuous sweep
Set the trigger setting for continuous sweep.
1. Touch the “Trigger” tab.
2. Set each parameter at the Trigger setting screen.
Setting parameter Description
Auto The sweep is started by command / screen operation
Start Trigger The sweep is started by the external signal input.
Manual
Sweep is also executed by command / screen operation.
Trigger signal is periodic output in wavelength using the
Constant Wavelength
calculation of the internal wavelength monitor.
Mode
Time Trigger signal is periodic output in time.
30 / 113

Tunable Semiconductor Laser TSL-570
Setting parameter Description
NONE Trigger signal is not output.
STOP Trigger signal is output at sweep completion.
Timing mode
START Trigger signal is output when sweep starts.
Trigger signal is output at a constant interval (wavelength or
STEP
time) during sweep.
5.6.3. Step sweep setting
1. Touch the “Sweep” tab.
2. After the screen switches to the Sweep setting screen, set Sweep Mode.
The Step sweep has one-way operation "Step and One way" and two-way
operation "Step and Two way".
3. Input the sweep start wavelength and sweep stop wavelength according to
"5-4. Setting the Wavelength".
31 / 113

TSL-570 OPERATION MANUAL
4. Set the Step interval.
Minimum step: 0.0001 nm
5.6.4. Trigger setting for step sweep
Set the trigger setting for step sweep.
1. Touch the “Setting” button.
2. Set each parameter at the Sweep setting screen.
32 / 113

Tunable Semiconductor Laser TSL-570
Parameter Unit Description
Cycles times Sweep repetition times
Dwell sec Wait time between consequent steps in step sweep mode.
When setting the Cycles to “0” (Zero), the sweep times is infinite.
5.6.5. Detailed trigger settings
Describe the detailed trigger output setting.
Setting Parameter Description
Input Polarity/ Set the Input/ Output trigger polarity.
Output Polarity Factory settings is “Rising”.
Select the polarity to change to “Falling” (Low).
Pass Through Set this parameter when using the trigger signal in synchronization
with other products.
When using a trigger from the device, such as in Sweep mode, set
it to “Off”.
Rear BNC This product operates using the input voltage to the Trigger Input
terminal on the rear panel as a trigger signal.
When setting to “Disable”, LCD operation or soft trigger of
communication command is recognized as a trigger.
33 / 113

TSL-570 OPERATION MANUAL
5.7. Executing the Wavelength Sweep
1. Touch RUN on the Sweep setting screen.
2. The sweep operation screen is displayed.
The operation status is shown on the first line during the sweep operation.
・ RUNNING Sweeping
・ PREPARE Stand-by
An indicator at the lower shows the progress of the sweep operation.
When setting the Cycles to “0” (Zero), the sweep times is infinite.
3. Stop Sweep
Touch STOP to stop a sweep in progress. Sweep is stopped immediately
NOTE
When stopping sweep operation in the middle, follow "5-6-6 Stop Sweep".
The number of sweeps displayed returns to 0 when the number exceeds
1000. If the mode is set to Two way, one round trip counts as two.
34 / 113

Tunable Semiconductor Laser TSL-570
5.8. Turning off the Unit
1. Press the power ON/OFF key.
2. “Shutting Down ...” is displayed on the main screen and LED of ON/OFF key
blinks during power shut down operation.
The unit is shut down after several seconds, and LED is turn off.
Do not unplug power cord from rear panel before power shut down is
complete (LED of power ON/OFF key is turn off). Damage of the device may
be caused by vibration under transportation if power supply is not shut down
properly. Make sure power supply is shut down properly before
transportation. If power supply is shut down under abnormal conditions or
due to events such as power failures while Laser is illuminated, turn power
back on (once) after power distribution is restored, and then turn off power
using the normal procedure.
NOTE
Unplug power cord from rear panel to completely shut down power supply.
35 / 113

TSL-570 OPERATION MANUAL
6. Detailed Operation
6.1. Fine-tuning
Fine-tuning adjusts output wavelength with a resolution under 1MHz. The
adjustable wavelength range is about 10 GHz (about 80 pm around 1550 nm).
Fine-tuning can be also performed with an external analog signal. Refer to “6-3.
External Modulation” for details.
■ How to set on the front panel
1. Set the wavelength according to the wavelength setting procedure.
2. Touch Main -> Function to move the setting screen.
3. Touch On at the Enable Fine-Tuning.
4. The input area of the FT value is displayed on the main screen. Input a
value with the numeric keypad. (Refer to “5-4 Setting the Wavelength”.)
Wavelength is shifted to shorter wavelength as FT value is increased.
Range: -100.00 to +100.00
Step: 0.01
36 / 113

Tunable Semiconductor Laser TSL-570
5. Tune the wavelength to the desired wavelength while monitoring the
output wavelength with an instrument such as a wavelength meter.
■ How to cancel on the front panel
When touching Off on the right side of Enable Fine-Tuning, the fine tuning
mode is canceled.
NOTE
Closed-loop wavelength control is stopped when Fine-tuning function is
active. To restart Closed-loop wavelength control, cancel Fine-tuning mode or
set the wavelength.
6.2. Coherence Control
Coherence Control increases spectral linewidth of output light. Coherency of
output light is reduced by this function, and fluctuation of optical power by
interference can be suppressed. If fluctuation of optical power becomes a
problem due to influence from reflecting point in a system using the device, use
the function.
■ How to set
1. Touch Function to move to the modulation setting screen.
2. Select “Coherence Control” in Modulation Source pull-down menu.
37 / 113

TSL-570 OPERATION MANUAL

3.  The operation starts when Modulation State is turned ON. During operation,
the “Coh.Ctrl” status is displayed on the status screen.

■  How to stop
1.  Select the Off at the Modulation State.
2.  Coherence control function turns OFF, and the “Coh.Ctrl” status turns off on
the screen.

6.3. External Modulation
6-3.1. Intensity Modulation
Modulating the intensity of optical power is performed at relatively low frequency.

Specifications
| Parameter          | Unit   | Description              |
| ------------------ | ------ | ------------------------ |
| Input voltage      |   V    | -2 ~ 0                   |
| Modulation depth   | %      | 100 (Maximum)            |
| Bandwidth          |   kHz  | 0 ~ 400 (typical value)  |
| Input impedance    |   Ω    | 100                      |
| Input terminal     |   -    | ANALOG INPUT             |
 38 / 113

Tunable Semiconductor Laser TSL-570
■ How to set
1. Touch Function to move to the modulation setting screen.
2. Select “Intensity Mod.” in Modulation Source pull-down menu.
3. Select On at the Modulation State. During operation, the “Intensity Mod.”
status is displayed at the status area.
NOTE
While the "Intensity Mod." Status is displayed, the wavelength and power
closed-loop control is stopped. Therefore, the wavelength and power may
fluctuate due to changes in the environment.
4. Input the voltage signal into the BNC connector labeled “ANALOG INPUT” at
the rear panel.
Analog Input
Never apply voltage out of the input level range. Doing so may damage the
device.
39 / 113

TSL-570 OPERATION MANUAL

■  How to cancel
1.  Select the Off at the Modulation State.
2.  Intensity Modulation control function turns OFF, and the “Intensity Mod.”
Status turns of on the screen.
6-3.2. Frequency Modulation
The function fine tunes wavelength with external signal.

Specifications
| Parameter          | Unit   | Description          |
| ------------------ | ------ | -------------------- |
| Input voltage      |   V    | -1.2 ~ 1.2           |
| Modulation depth   | GHz/V  | 5 (typical value)    |
| Bandwidth          |   Hz   | 100 (typical value)  |
| Input impedance    |   kΩ   | 4.7                  |
| Input terminal     |   -    | ANALOG INPUT         |

■  How to use
1.  Touch Main -> Setting to move to the modulation setting screen.
2.  Select “Frequency Mod.” in Modulation Source pull-down menu.

3.  Select On at the Modulation State. During operation, the “Frequency Mod.”
status is displayed at the status area.

4.  Input the voltage signal into the BNC connector labeled “ANALOG INPUT” at
the rear panel.
 40 / 113

Tunable Semiconductor Laser TSL-570
Analog Input
Never apply voltage out of the input level range. Doing so may damage the
device.
■ How to cancel
1. Select the Off at the Modulation State.
2. Frequency Modulation control function turns OFF, and the “Frequency Mod.”
Status turns of on the screen.
NOTE
While the “Frequency Mod." Status is displayed, the wavelength closed-loop
control is stopped. Therefore, the wavelength may fluctuate due to changes in
the environment.
6.4. Power Monitor Signal Output
The function outputs voltage signal according to integrated power monitor. It
can be used to compensate optical output power fluctuation in real time. (For
example, this feature is best recommended to be used with Santec’s Swept Test
System as WDL/PDL measurement solution.)
Power monitor output
41 / 113

TSL-570 OPERATION MANUAL
Signal is output from BNC connector leveled “POWER MONITOR” on rear panel.
The relation between output voltage and optical power depends on
measurement range of power monitor, as shown below. Measurement range is
adjusted automatically. Output voltage value against optical output power is not
calibrated.
Typical voltage over output power correlation for each measurement range is
shown below.
Range0: 0.03 V/mW (> 20 mW)
Range1: 0.15 V/mW (4 to 20 mW)
Range2: 0.75 V/mW (0.8 to 4 mW)
Range3: 3.75 V/mW (0.16 to 0.8 mW)
Range4: 18.75 V/mW (< 0.16 mW)
6.5. Trigger Setting
Trigger signals can be used for synchronizing with external instruments.
Specifications of output trigger signal
Signal Voltage: 3.3V (High), 0V (Low)
Signal width: 25 μs
Repetition rate: 20 kHz (Maximum)
Minimum trigger step: Dependence on sweep speed. See table below
as reference.
Sweep speed Minimum trigger step [pm]
[nm/s] Time constant mode Wavelength constant mode
42 / 113

                                       Tunable Semiconductor Laser TSL-570
| 1    | >0.1  | >0.2  |
| ---- | ----- | ----- |
| 2    | >0.1  | >0.2  |
| 5    | >0.3  | >0.5  |
| 10   | >0.5  | >1    |
| 20   | >1    | >1    |
| 50   | >2.5  | >2.5  |
| 100  | >5    | >5    |
| 200  | >10   | >10   |

NOTE
If settings other than those in the above table are set, the sweep speed will be
prioritized.
e.g.
When the sweep speed is set to 200 nm/s, the minimum trigger interval is set to
1pm, the minimum trigger interval is automatically set to 10pm.
If necessary high resolution trigger output at a slow sweep speed, the time
constant mode is effective. In this case, please read the wavelength logging data
using the “:READout:DATa?” command.

1.  Touch the Setting on the Trigger tab to move to trigger setting screen.

 43 / 113

TSL-570 OPERATION MANUAL
Input Polarity Sets input trigger polarity.
Rising Triggers on a rising edge.
Falling Triggers on a falling edge.
Output Polarity Sets output trigger polarity.
Rising Select when use an instrument that identifies rising edge.
Falling Select when use an instrument that identifies falling edge.
Pass Through Replicates the input trigger on the output trigger with identical timing.
ON A trigger is output with the same timing as the input trigger, but
reshaped according to the Output Polarity setting.
OFF No trigger is output even if there is an input trigger.
6.6. Displaying the Product Information
Display the various product information.
1. Touch Information on the Other tab to move to the screen for various
settings.
The following information is displayed.
・ Product name
・ Serial Number
・ Product Code
・ Firmware Version
44 / 113

Tunable Semiconductor Laser TSL-570
6.7. System Alert
If an error occurs in the product, marks are displayed in the lower left corner of
the screen. Follow the following steps to check the details of the error.
1. Touch Alerts on the Other tab to move to the Alerts screen.
2. The error code is displayed in the alarm list field. The detailed information is
as below.
45 / 113

TSL-570 OPERATION MANUAL
3. Refer to the following for the error contents and the copying method for the
error number.
Error Detail How to deal with errors
number
No 00 There is something issue with Please stop using the product and contact santec.
to 03 power supply.
No 04 Power setting Error Reset the power in the configurable power range
No 05 Wavelength Error. Press the Power ON/OFF key to turn off the product
and restart the product. If the error still occurs,
please stop using the product and contact santec.
No 06 There is something issue with Press the Power ON/OFF key to turn off the product
the attenuator. and restart the product. If the error still occurs,
please stop using the product and contact santec.
No 07 There is something issue with Check the Interlock connection. Refer to “4-3
the interlock. Interlock”.
No 20 There is something issue with Press the Power ON/OFF key to turn off the product
to 22 the Temperature control. and restart the product. If the error still occurs,
please stop using the product and contact santec.
No 23 Ongoing Warm up. Please wait until the warm up display disappears.
No 24 There is something issue with Press the Power ON/OFF key to turn off the product
the sensor. and restart the product. If the error still occurs,
please stop using the product and contact santec.
No 25 There is something issue with Please stop using the product and contact santec.
the shutter function.
No 26 There is something issue with Press the Power ON/OFF key to turn off the product
the sensor. and restart the product. If the error still occurs,
please stop using the product and contact santec.
No 27 There is something issue with Please stop using the product and contact santec.
the connection.
No 30 There is something issue with Press the Power ON/OFF key to turn off the product
the exhaust fan. and restart the product. If the error still occurs,
46 / 113

Tunable Semiconductor Laser TSL-570
please stop using the product and contact santec.
*Contact information can be found on the last page of this document.
6.8. System Settings
This function allows various settings related to System.
1. Touch System on the Other tab. The “System” screen will be displayed.
Sound Set the presence or absence of a beep sound during touch operation.
Brightness Sets the screen brightness in the range 10 to 100%.
The screen brightness is reduced to 10% when the touch screen, numeric
keypad have not been used for the specified period of time.
Off Time
Set the time in minutes (up to 99 minutes). When setting to “0“ minutes,
the timer is disabled and the brightness will not decrease.
Date Set the date of the built-in clock.
Time Set the time of the built-in clock.
6.9. Save/ Load Setting parameters
This product can save up to 4 set parameters.
1. Touch the Save/Load on the Other tab to move to the Save/Load screen.
47 / 113

TSL-570 OPERATION MANUAL
2. Select the Save/Load destination file. When touching the Load on the
Present, the setting returns to the factory setting.
48 / 113

Tunable Semiconductor Laser TSL-570
7. Operation by Communication
This device supports GP-IB, LAN and USB as means of communication. The
setting method, characteristics, and differences of each method are described
below.
7.1. GPIB
A communication function based on standards specified in IEEE-488.
7.1.1. Connection
Connect the 24-pin GPIB cable to the GPIB connector on the rear panel.
The total extension of the connected cable shall be 20 m or less. The cable
length between each device must be 2 m or less. At most, 15 devices can be
connected.
GPIB connector
Do not disconnect or connect a cable from and to devices connected with
GPIB cable, do not short-circuit connector, and do not turn ON/OFF the
devices. Otherwise, action may be stopped, error may occur, causing a
failure. In the event of trouble owing to these causes, reset all the connected
devices, and then activate the system once again. When configuring a
system, remove the unused device or unnecessary cable and return to the
original setup.
7.1.2. GPIB Function
GP-IB has 10 kinds of interface functions, each of which has its grade that is called
its subset. A "0" after the symbol of each function shows that support is not made,
49 / 113

TSL-570 OPERATION MANUAL
and each numeric value represents grade.
Symbol Function TSL-570 Subset
SH Source handshake SH1: All functions
AH Acceptor handshake AH1: All functions
T Talker T8: Basic talker, talker release by MLA
L Listener L4: Basic listener, listener release by MTA
SR Service request SR1: All functions
RL Remote/Local RL2: Remote/local function, no local lockout
function
PP Parallel poll PP0: none
DT Device trigger DT0: none
DC Device clear DC1: All functions
C Controller C0: none
1. GPIB address
GP-IB address of this product can be changed to refer to “7-1-3 Setting the
address, delimiter, and command set”. The changed address will be available
after setting. The changed address is saved in internal memory.
2. LOCAL
LOCAL is a state that this product is controlled by a key operation. This state is
valid for all key operations.
3. REMOTE
REMOTE is a state that this product is controlled from other controllers through
GPIB bus. In this state, all the key operations are disable except for LOCAL key
and LD key.
4. Device Clear (DCL)
When this product receives the universal command “DCL” in REMOTE state, the
transmit and receive buffers are cleared.
7.1.3. Setting the Address, Delimiter and Command set
1. Touch Communication on the Other tab. The GPIB setting screen will be
displayed.
Set GPIB address and delimiter.
50 / 113

Tunable Semiconductor Laser TSL-570
2. Touch GPIB on the Communication.
3. Set GPIB Address and Delimiter.
Address Set an address from 1 to 30. The default value is 1.
Delimiter Select a delimiter from ”CR”, ”LF”, ”CR+LF”, and ”EOI “. Set the end
character of the command string. When “CR”, ”LF” or ”CR+LF” is
selected, the command is accepted and analysis begins when the
specified delimiter is received. When a command is sent, the delimiter
is added to the end of the command and an EOI signal is asserted.
When “EOI” is selected, the command is accepted and analysis begins
when the EOI is received. When a command is sent, an EOI is asserted
when the last character is sent.
51 / 113

TSL-570 OPERATION MANUAL
7.2. USB
7.2.1. Connection
Connect USB B type cable to the connector leveled “USB DEVICE” on rear panel.
“USB HOST” connector is not used for communication.
USB connector
7.2.2. Communication Conditions and System Requirements
Transfer speed 1 MBps (with D2XX driver)
Setting the Delimiter: The delimiter of the command is “CR”. At receiving time,
the reception of commands is completed and analysis begins after the delimiter
is recognized. At sending time, the delimiter is added to the end of the response
string and then sent.
7.2.3. Installing a USB Driver Software
To enable USB communication, USB driver software must be installed.
Even though some pop-up messages will be displayed when USB cable is
connected the device and PC, please click cancel or close message.
1. Open “Device Manager” (Figure 7-2-3-1) and open “TSL-570” under “Other
devices.” Right-click on “TSL-570” and click on “Update Driver Software...”.
52 / 113

Tunable Semiconductor Laser TSL-570
Figure 7-2-3-1. Device message
2. Click on “Browse my computer for driver software” when message window
(Figure 7-2-3-2) appears.
Figure 7-2-3-2. Update driver software
3. On message window (Figure 7-2-3-3), click on “Browse” button to select
the driver software location under Removable disk included in package.
(e.g., D:\Common\USB Driver on Figure 7-2-3-3)
Figure 7-2-3-3. Search for driver software location
4. Installation will automatically start. Message window Figure 7-2-3-4 will
53 / 113

TSL-570 OPERATION MANUAL
appear.
Figure 7-2-3-4. Installation in progress
5. If a Windows Security message in Figure 7-2-3-5 appears, please click on
“Install this driver software anyway” to proceed.
Figure 7-2-3-5. Windows security message
6. Installation is completed successfully when Figure 7-2-3-6 appears. Click on
“Close” to exit the installation.
Figure 7-2-3-6. Installation complete
7.3. LAN
7.3.1. Connection
Connect the LAN cable to the RJ-45 connector on the rear panel.
54 / 113

Tunable Semiconductor Laser TSL-570
LAN connector
7.3.2. Communication Conditions and System Requirements
Electrical Specifications IEEE802.3 Standard
Transfer Method Ethernet（100BASE-TX）
Transfer speed 30Mbps
Communication Protocol TCP/IP
Connector Type RJ-45
IP Address *.*.*.* (* = integer from 0 ~ 255)
Subnet mask *.*.*.* (* = integer from 0 ~ 255)
Default Gateway *.*.*.* (* = integer from 0 ~ 255)
Port No. Integer from 0 ~ 65535
The delimiter of the command is “CR”.
The command is accepted and analysis begins when the delimiter is received.
At sending time, the delimiter is added to the end of the response string and
sent.
7.3.3. Settings
1. Touch the Communication on the Other tab to move to the Communication
setting screen. Then, touch the LAN to move to the Ethernet setting
screen.
55 / 113

TSL-570 OPERATION MANUAL
2. Set the following items.
Physical Address The number is unique and cannot be changed.
Port Number Set integer number from 0 to 65535 using numeric
keypad.
IP Address Input numbers using numeric keypad.
Subnet Mask Input numbers using numeric keypad.
Default Gateway Input numbers using numeric keypad.
3. Touch the Apply to complete settings.
7.4. Command Reference
7.4.1. Common Command List
Available for IEEE-488.2 common commands in the following list.
Command Description
Identification Query
*IDN?
Returns strings that identify the device.
*RST Reset (Aborts the standby command.)
*TST? Initiates an instrument self-test and returns the results.
56 / 113

Tunable Semiconductor Laser TSL-570
;*OPC? Queries the completion of operation.
*CLS Status Clear (Clears STBR and SESR.)
Sets Standard Event Enable Register.
*ESE
(The result of SESR and SEER is set to ESB.)
*ESE? Reads out the value of the Standard Event Enable Register.
*ESR? Reads out the value of the Standard Event Status Register.
*SRE Sets Service Request Enable. (Selects enable or disable SRQ.)
*SRE? Reads out the value of the Service Request Enable Register.
*STB? Reads out the value of the Status Byte Register.
7.4.2. TSL-570 Status system
When Command set 1 is selected, the following status systems with four registers
are provided.
(1) Status Byte Register (STBR)
(2) Service Request Enable Register (SRER)
(3) Standard Event Status Register (SESR)
(4) Standard Event Enable Register (SEER)
1. Status System Structure Overview
* Output queue is cleared when a new command is input into the input queue.
2. Status Byte Register (STBR）
57 / 113

TSL-570 OPERATION MANUAL
The status is read out by serial poll, or *STB? command.
7 6 5 4 3 2 1 0
Not used RQS ESB MAV Not used Not used Not used Not used
RQS (Request Service Bit):
RQS is set when a Service Request is issued.
ESB (Event Status Bit):
ESB is set when any of the bits of the Standard Event Status Register
(SESR) is set.
MAV (Message Available Bit):
MAV is set when output data is prepared.
3. Service Request Enable Register (SRER）
An 8-bit register to set Enable/Disable of each bit of the Status Byte
Register. If a bit of the SRER is set to 1, the corresponding bit of the STBR
is set to Enable.
4. Standard Event Status Register (SESR）
An 8-bit register to indicate the standard status of the device.
7 6 5 4 3 2 1 0
PON Not used CME EXE DDE QYE Not used OPC
PON (Power ON):
Bit is set when power is turned on.
CME (Command Error):
CME is set when a command has a syntax error or is misspelled.
EXE (Execution Error):
EXE is set when a command is not available for the device, or a command
cannot be executed in the current device condition.
DDE (Device Definition Error):
Not used
QYE (Query Error):
QYE is set when an attempt is made to read data from the output queue
while the output queue is empty.
OPC (Operation Completion):
OPC is set when all pending operations are completed.
5. Standard Event Enable Register (SEER)
SEER is an 8-bit register to set Enable/Disable of each bit of the SESR. If a
58 / 113

Tunable Semiconductor Laser TSL-570
bit of the SEER is set to 1, the corresponding bit of the SESR is set to Enable.
7.4.3. IEEE-488.2 common commands - Detailed description
Command *IDN?
Description Identification Query
A query to identify the device; places strings of device
information such as the manufacturer name, model number,
serial number, firmware version in the output queue.
Syntax *IDN?
Parameter None
Response The information of this device information is as follows.
SANTEC,TSL-570,########,****.****.****
# field = serial number of the device in 8 digits.
* field = firmware version as 4 digits + .(period) + 4 digits
+ .(period) + 4 digits.
Example The information of this device information is as follows.
Manufacturer: SANTEC, Model: TSL-570,
Serial: 21020001, Firmware: 0001.0000.00001
Transmission *IDN?
Response →SANTEC,TSL-570,21020001,0001.0000.0001
Command *RST
Description Device Reset
Aborts standby operation.
Clears the following items.
・Command input queue
・Error queue
Syntax *RST
Parameter None
Response None
Example The device is in the idle state waiting a command.
Transmission *RST
Response None
Command *TST?
Description Self-test Query
Initiates an instrument self-test and places the results in the
output queue.
Syntax *TST?
59 / 113

TSL-570 OPERATION MANUAL
Parameter None
Response This should return “0” for success, non-zero return values for
error conditions
0: No error
Non zero: Error
Example This should return “0” for success, non-zero return values for
error conditions.
Transmission *TST?
Response →0
Command *OPC?
Description Operation Complete Query
Places 1 in the output queue when all operation processing has
completed.
Syntax *OPC?
Parameter None
Response 0: (In operation)
1: (Operation completed)
Example All operation processing has completed.
Transmission *OPC?
Response →1
Command *CLS
Description Clear Status
Clears all event registers and queues and reflects the summary
in the Status Byte Register.
Clears the following items.
・Status Byte Register
・Standard Event Status Register
・Error Queue
Syntax *CLS
Parameter None
Response None
Example Clears all event registers and queues.
Transmission *CLS
Response None
Command *ESE
Description Standard Event Enable Register Setting
Sets the Standard Event Enable Register (SEER).
Syntax *ESE<wsp><value>
60 / 113

                                       Tunable Semiconductor Laser TSL-570
| Parameter         | Setting value from 0 to 255  |     |
| ----------------- | ---------------------------- | --- |
| Response          | None                         |     |
| Example           | Set SEER to 255.             |     |
|     Transmission  | *ESE 255                     |     |
| Response          | None                         |     |

| Command      | *ESE?                                 |     |
| ------------ | ------------------------------------- | --- |
| Description  | Standard Event Enable Register Query  |     |
Places the value of the Standard Event Enable Register (SEER)
in the output queue.
| Syntax            | *ESE?                  |     |
| ----------------- | ---------------------- | --- |
| Parameter         | None                   |     |
| Response          | Integer from 0 to 255  |     |
| Example           | SEER setting is 255.   |     |
|     Transmission  | *ESE?                  |     |
| Response          | →255                   |     |

| Command      | *ESR?                                  |     |
| ------------ | -------------------------------------- | --- |
| Description  | Standard Event Status Register Query   |     |
Places the value of the Standard Event Status Register (SESR)
in the output queue. Register is cleared after being read.
| Syntax            | *ESR?                  |     |
| ----------------- | ---------------------- | --- |
| Parameter         | None                   |     |
| Response          | Integer from 0 to 255  |     |
| Example           | ESR setting is 255.    |     |
|     Transmission  | *ESR?                  |     |
| Response          | →255                   |     |

| Command      | *SRE                                     |     |
| ------------ | ---------------------------------------- | --- |
| Description  | Service Request Enable Register Setting  |     |
Sets the Service Request Enable Register (SRER).
| Syntax            | *SRE<wsp><value>             |     |
| ----------------- | ---------------------------- | --- |
| Parameter         | Setting value from 0 to 255  |     |
| Response          | None                         |     |
| Example           | Set SRE to 255.              |     |
|     Transmission  | *SRE 255                     |     |
| Response          | None                         |     |

| Command  | *SRE?  |     |
| -------- | ------ | --- |
 61 / 113

TSL-570 OPERATION MANUAL
Description Service Request Enable Register Query
Places the value of the Service Request Enable Register (SRER)
in the output queue.
Syntax *SRE?
Parameter None
Response Integer from 0 to 63, or 128 to 191.
(Values are missing since Bit 6 is always 0.)
Example SRER setting is 63.
Transmission *SRE?
Response →63
Command *STB?
Description Status Byte Register Query
Places the value of the Status Byte Register (STBR) in the
output queue.
Syntax *SRE?
Parameter None
Response Integer from 0 to 255
When read out by a serial poll, the value returned is the sum of
64 and the value of the Status Byte Register (since Bit 6 is set
in the serial poll).
Example STB setting is 0.
Transmission *STB?
Response →0
7.4.4. TSL-570 Specific command overview
Two kinds of command sets are provided for the TSL-570. Select one of
them in advance and use the commands in that category. Commands in
one command set cannot be used with commands in the other command
set simultaneously. “TSL-570 SCPI” is using commands complying with the
standards specified by the SCPI consortium. This command set has high
compatibility with other companies’ instruments.
“Legacy” is using commands based on santec’s conventional SCPI
commands. This command set has compatibility with santec conventional
model TSL-550, TSL-710, and TSL-510.
■ How to switch the command set
1. Touch Communication on the Other tab to move to command set ting
screen.
62 / 113

                                       Tunable Semiconductor Laser TSL-570
2. Select ”Legacy” or ” SCPI”.

Command set  Description
Legacy  This command is compatible with our previous products.
SCPI  This command complies with the standards specified by the
SCPI consortium.

Command  set  can  also  be  selected  by  “:SYSTem:COMMunicate:CODe”
command.

|     | Command  |     | Description  | Page  |
| --- | -------- | --- | ------------ | ----- |
67
1.  Optical output related commands
| :WAVelength   |     | Sets the output wavelength.      |     | 67  |
| ------------- | --- | -------------------------------- | --- | --- |
| :WAVelength?  |     | Reads out the wavelength value.  |     | 68  |
68
| :WAVelength:UNIT  |     | Sets units of displayed wavelength.  |     |     |
| ----------------- | --- | ------------------------------------ | --- | --- |
:WAVelength:UNIT?  Reads out units of displayed wavelength.  68
| :WAVelength:FINe  |     |     |     | 69  |
| ----------------- | --- | --- | --- | --- |
Sets Fine-Tuning value.
| :WAVelength:FINe?               |     | Reads out Fine-Tuning value.  |     | 69  |
| ------------------------------- | --- | ----------------------------- | --- | --- |
| :WAVelength:FINetuning:DISable  |     |                               |     | 69  |
Terminates Fine-Tuning operation.
[:WAVelength]:FREQuency  Sets the output wavelength in optical  69
frequency.
[:WAVelength]:FREQuency?  Reads out output wavelength in optical  70
frequency.
| :COHCtrl  |     | Sets Coherence control status.  |     | 70  |
| --------- | --- | ------------------------------- | --- | --- |
71
| :COHCtrl?     |     | Reads out Coherence control status.  |     |     |
| ------------- | --- | ------------------------------------ | --- | --- |
| :POWer:STATe  |     | Sets optical output status.          |     | 71  |
 63 / 113

TSL-570 OPERATION MANUAL
| :POWer:STATe?  |     | 71  |
| -------------- | --- | --- |
Reads out optical output status.
| :POWer:ATTenuation  |     | 71  |
| ------------------- | --- | --- |
Sets the attenuator value.
72
| :POWer:ATTenuation?  | Reads out the attenuator value.  |     |
| -------------------- | -------------------------------- | --- |
72
| :POWer:ATTenuation:AUTo  | Sets the power control mode.  |     |
| ------------------------ | ----------------------------- | --- |
:POWer:ATTenuation:AUTo?  Reads out the setting of the power control.  72
| :POWer[:LEVel]  |     | 72  |
| --------------- | --- | --- |
Sets optical output power level.
| :POWer[:LEVel]?  |     | 73  |
| ---------------- | --- | --- |
Reads out optical output power level setting.
:POWer:ACTual[:LEVel]?
|                 | Reads out monitored optical power.   | 73  |
| --------------- | ------------------------------------ | --- |
| :POWer:SHUTter  |                                      | 74  |
Sets Open/Close status of the internal shutter.
| :POWer:SHUTter?  |     | 74  |
| ---------------- | --- | --- |
Reads out the status of the internal shutter.
:POWer:UNIT
|     | Changes the unit of the power setting and  | 74  |
| --- | ------------------------------------------ | --- |
display.
| :POWer:UNIT?  |     | 74  |
| ------------- | --- | --- |
Reads out the unit of the power setting and
display.
:WAVelength:SWEep:STARt
|     | Sets the sweep start wavelength.  | 75  |
| --- | --------------------------------- | --- |
:WAVelength:SWEep:STARt?  Reads out the sweep start wavelength.  75
| [:WAVelength]:FREQuency:SWEep:S |     | 76  |
| ------------------------------- | --- | --- |
Sets the sweep start wavelength in optical
TARt
frequency.
[:WAVelength]:FREQuency:SWEep:S
|     | Reads out the sweep start wavelength in  | 76  |
| --- | ---------------------------------------- | --- |
TARt?
optical frequency.
| :WAVelength:SWEep:STOP  |     | 77  |
| ----------------------- | --- | --- |
Sets the sweep stop wavelength.
:WAVelength:SWEep:STOP?  Reads out the sweep stop wavelength.  77
77
:WAVelength:SWEep:RANGe:MINimu Reads out the minimum wavelength in the
| m?                            | configurable sweep range  |     |
| ----------------------------- | ------------------------- | --- |
| :WAVelength:SWEep:RANGe:MAXim |                           | 78  |
Reads out the maximum wavelength in the
um?
configurable sweep range
[:WAVelength]:FREQuency:SWEep:S Sets the sweep stop wavelength in optical  78
| TOP  | frequency.  |     |
| ---- | ----------- | --- |
[:WAVelength]:FREQuency:SWEep:S Reads out the sweep stop wavelength in  79
| TOP?  | optical frequency.  |     |
| ----- | ------------------- | --- |
79
[:WAVelength]:FREQuency:SWEep:R Reads out the minimum frequency in the
| ANGe:MINimum?  | configurable sweep range  |     |
| -------------- | ------------------------- | --- |
[:WAVelength]:FREQuency:SWEep:R Reads out the maximum frequency in the  80
| ANGe:MAXimum?           | configurable sweep range  |     |
| ----------------------- | ------------------------- | --- |
| :WAVelength:SWEep:MODe  | Sets the sweep mode.      | 80  |
 64 / 113

                                       Tunable Semiconductor Laser TSL-570
| :WAVelength:SWEep:MODe?  | Reads out the sweep mode.  | 81  |
| ------------------------ | -------------------------- | --- |
81
| :WAVelength:SWEep:SPEed   | Sets the sweep speed.   |     |
| ------------------------- | ----------------------- | --- |
| :WAVelength:SWEep:SPEed?  | Reads out sweep speed.  | 81  |
82
| :WAVelength:SWEep:STEP[:WIDTh]  | Sets the step for Step sweep mode.  |     |
| ------------------------------- | ----------------------------------- | --- |
:WAVelength:SWEep:STEP[:WIDTh]? Reads out the step for Step sweep mode.  82
[:WAVelength]:FREQuency:SWEep:S Sets the step for Step sweep mode in optical  83
| TEP[:WIDTh]  | frequency.  |     |
| ------------ | ----------- | --- |
83
[:WAVelength]:FREQuency:SWEep:S Reads out the step for Step Sweep mode in
| TEP[:WIDTh]?  | optical frequency.  |     |
| ------------- | ------------------- | --- |
:WAVelength:SWEep:DWELl  Sets wait time between consequent steps in  84
step sweep mode.
:WAVelength:SWEep:DWELl?  Reads out wait time between consequent  84
steps in step sweep mode.
84
| :WAVelength:SWEep:CYCLes  | Sets the sweep repetition times.  |     |
| ------------------------- | --------------------------------- | --- |
:WAVelength:SWEep:CYCLes?  Reads out the setting sweep repetition times.  85
85
:WAVelength:SWEep:COUNt?  Reads out the current number of completed
sweeps.
:WAVelength:SWEep:DELay  Sets the wait time between consequent scans.  85
:WAVelength:SWEep:DELay?  Reads out the setting wait time between  85
consequent scans.
86
| :WAVelength:SWEep[:STATe]  | Sets sweep status.  |     |
| -------------------------- | ------------------- | --- |
:WAVelength:SWEep[:STATe]?  Reads out the current sweep status.  86
86
| :WAVelength:SWEep[:STATe]:REPea | Starts repeat scan.  |     |
| ------------------------------- | -------------------- | --- |
t
86
| :READout:POINts?  | Reads out the number of logging data.  |     |
| ----------------- | -------------------------------------- | --- |
| :READout:DATa?    | Reads out wavelength logging data.     | 87  |
87
| :READout:DATa:POWer?  | Reads out power logging data.                |     |
| --------------------- | -------------------------------------------- | --- |
| :AM:STATe             | Enables and disables modulation function of  | 88  |
the laser output.
:AM:STATe?  Reads out status of modulation function of the  88
laser output.
88
| :AM:SOURce   | Sets modulation source.       |     |
| ------------ | ----------------------------- | --- |
| :AM:SOURce?  | Reads out modulation source.  | 88  |
89
[:SOURce]:WAVelength:OFFSet  Add the constant offset to the output
wavelength.
[:SOURce]:WAVelength:OFFSet?  Reads out the constant offset to the output  89
wavelength.
| 2.  Input/ Output related command  |     | 90  |
| ---------------------------------- | --- | --- |
 65 / 113

TSL-570 OPERATION MANUAL
:TRIGger:INPut:EXTernal  Enables / Disables external trigger input.  90
90
:TRIGger:INPut:EXTernal?  Reads out the setting of external trigger input.
:TRIGger:INPut[:EXTernal]:ACTive  Sets input trigger polarity.  90
90
| :TRIGger:INPut[:EXTernal]:ACTive?  | Reads out input trigger polarity.  |     |
| ---------------------------------- | ---------------------------------- | --- |
:TRIGger:INPut:STANdby  Sets the device in trigger signal input standby  91
mode.
:TRIGger:INPut:STANdby?  Reads out the trigger signal input standby  91
mode.
91
:TRIGger:INPut:SOFTtrigger  Executes sweep from trigger standby mode.
:TRIGger:OUTPut  Sets the timing of the trigger signal output.  91
92
:TRIGger:OUTPut?  Reads out the timing setting of the trigger
signal output.
92
| :TRIGger:OUTPut:ACTive  | Sets output trigger polarity.  |     |
| ----------------------- | ------------------------------ | --- |
:TRIGger:OUTPut:ACTive?  Reads out output trigger polarity.  92
92
:TRIGger:OUTPut:STEP[:WIDTh]  Sets the interval of the trigger signal output.
:TRIGger:OUTPut:STEP[:WIDTh]?  Reads out the interval of the trigger signal  93
output.
:TRIGger:OUTPut:SETTing  Sets the output trigger period mode.  93
93
:TRIGger:OUTPut:SETTing?  Reads out the output trigger period mode.
| :TRIGger:THRough  | Sets the trigger through mode.   | 94  |
| ----------------- | -------------------------------- | --- |
94
| :TRIGger:THRough?            | Reads out the trigger through mode.  |     |
| ---------------------------- | ------------------------------------ | --- |
| 3.  System related commands  |                                      | 94  |
94
| :SYSTem:ERRor?                 | Reads out the error issued.  |     |
| ------------------------------ | ---------------------------- | --- |
| :SYSTem:COMMunicate:GPIB:ADDRe | Sets the GPIB address.       | 95  |
ss
:SYSTem:COMMunicate:GPIB:ADDRe Reads out the GPIB address.  95
ss?
95
:SYSTem:COMMunicate:GPIB:DELimi Sets the command delimiter for GPIB
| ter  | communication.   |     |
| ---- | ---------------- | --- |
:SYSTem:COMMunicate:GPIB:DELimi Reads out the command delimiter for GPIB  95
| ter?  | communication.  |     |
| ----- | --------------- | --- |
:SYSTem:COMMunicate:ETHernet:M Reads out the MAC address.  96
ACaddress?
96
| :SYSTem:COMMunicate:ETHernet:IP | Sets the IP address.  |     |
| ------------------------------- | --------------------- | --- |
ADdress
:SYSTem:COMMunicate:ETHernet:IP Reads out the IP address.  96
ADdress?
| :SYSTem:COMMunicate:ETHernet:SM | Sets the subnet mask.  | 96  |
| ------------------------------- | ---------------------- | --- |
 66 / 113

                                       Tunable Semiconductor Laser TSL-570
ASk
:SYSTem:COMMunicate:ETHernet:SM Reads out the subnet mask.  96
ASk?
97
| :SYSTem:COMMunicate:ETHernet:DG | Sets the default gateway.  |     |
| ------------------------------- | -------------------------- | --- |
ATeway
:SYSTem:COMMunicate:ETHernet:DG Reads out the default gateway.  97
ATeway?
| :SYSTem:COMMunicate:ETHernet:PO | Sets the port number.  | 97  |
| ------------------------------- | ---------------------- | --- |
RT
97
| :SYSTem:COMMunicate:ETHernet:PO | Reads out the port number.  |     |
| ------------------------------- | --------------------------- | --- |
RT?
98
| :SYSTem:COMMunicate:CODe  | Sets the command set.  |     |
| ------------------------- | ---------------------- | --- |
:SYSTem:COMMunicate:CODe?  Reads out the current set command set.  98
98
| :SYSTem:LOCK?        | Reads out the status of external interlock.  |     |
| -------------------- | -------------------------------------------- | --- |
| :DISPlay:BRIGhtness  | Sets brightness of the display.              | 98  |
99
| :DISPlay:BRIGhtness?  | Reads out brightness of the display.  |     |
| --------------------- | ------------------------------------- | --- |
| :SPECial:SHUTdown     | Shuts down the device.                | 99  |
| :SPECial:REBoot       | Restarts the device.                  | 99  |
99
| :SYSTem:ALERt?    | Reads out the current alert information.  |     |
| ----------------- | ----------------------------------------- | --- |
| :SYSTem:VERSion?  | Reads out the frimware version            | 99  |
100
| :SYSTem:CODe?  | Reads out the product code  |     |
| -------------- | --------------------------- | --- |

1.  Optical output related commands

Command  :WAVelength
Description  Sets the output wavelength.
Syntax  Legacy  [:SOURce[n]][:CHANnel[m]]:WAVelength<wsp><value>
SCPI  [:SOURce[n]][:CHANnel[m]]:WAVelength<wsp><value>
[PM|NM|UM|MM|M]
Parameter  Range: Specified wavelength range
Step: 0.1 pm
  Legacy  <value> should be decimal notation in “nm”. Character strings
representing a unit cannot be accepted.
SCPI  <value> is accepted in decimal notation and exponential
notation. These numbers are followed by character strings
representing a unit. When a unit character string is not
specified, m（meter）is used as the default.
Response  None
Example  Set the wavelength to 1550nm.
 67 / 113

TSL-570 OPERATION MANUAL
Legacy :WAV 1550
SCPI1 :WAV 1550nm
SCPI2 :WAV 1550E-9
Command :WAVelength?
Description Reads out the wavelength value.
Syntax Legacy [:SOURce[n]][:CHANnel[m]]:WAVelength
[:MINimum|:MAXimum]?
SCPI [:SOURce[n]][:CHANnel[m]]:WAVelength?<wsp>
[PM|NM|UM|MM|M][MINimum|MAXimum]
Parameter None: Reads out the current set wavelength.
MINimum: Reads out the minimum acceptable wavelength.
MAXimum: Reads out the maximum acceptable wavelength.
Response Range: Specified wavelength range
Step: 0.1pm
Legacy Response is decimal notation in “nm”.
9 SCPI These numbers are followed by character strings representing
a unit. When a unit character string is not specified, m
(meter）is used as the default.
Example The setting wavelength is 1550nm.
Transmission :WAV?
Response Legacy →1550.0000
SCPI →+1.55000000E-006
Command :WAVelength:UNIT
Description Sets units of displayed wavelength.
Syntax [:SOURce]: WAVelength:UNIT<wsp><value>
Parameter 0: nm
1: THz
Response None
Example Sets units of wavelength to THz.
Transmission :WAV:UNIT 1
Command :WAVelength:UNIT?
Description Reads out units of displayed wavelength.
Syntax [:SOURce[n]][:CHANnel[m]]:WAVelength:UNIT?
Parameter None
Response 0: nm
1: THz
Example The setting unit of wavelength is THz.
Transmission :WAV:UNIT?
68 / 113

                                       Tunable Semiconductor Laser TSL-570
| Response  | Legacy  | →1   |
| --------- | ------- | ---- |
|           | SCPI    | →+1  |

| Command      |     | :WAVelength:FINe         |
| ------------ | --- | ------------------------ |
| Description  |     | Sets Fine-Tuning value.  |
Syntax  [:SOURce[n]][:CHANnel[m]]:WAVelength:FINe<wsp><value>
| Parameter  |     | Range: -100.00 to +100.00  |
| ---------- | --- | -------------------------- |
Step: 0.01
| Response  |               | None                           |
| --------- | ------------- | ------------------------------ |
| Example   |               | Sets Fine-Tuning value to 50.  |
|           | Transmission  | :WAV:FIN 50.00                 |

| Command      |         | :WAVelength:FINe?                           |
| ------------ | ------- | ------------------------------------------- |
| Description  |         | Reads out Fine-Tuning value.                |
|              | Syntax  | [:SOURce[n]][:CHANnel[m]]:WAVelength:FINe?  |
| Parameter    |         | None                                        |
| Response     |         | Range: -100.00 to +100.00                   |
Step: 0.01
| Example       |         | The setting Fine-Tuning value is 100.  |
| ------------- | ------- | -------------------------------------- |
| Transmission  |         | :WAV:FIN?                              |
| Response      | Legacy  | →100.00                                |
|               | SCPI    | →+1.00000000E+002                      |

| Command      |               | :WAVelength:FINetuning:DISable              |
| ------------ | ------------- | ------------------------------------------- |
| Description  |               | Terminates Fine-Tuning operation.           |
|              | Syntax        | [:SOURce[n]]:WAVelength:FINetuning:DISable  |
| Parameter    |               | Note                                        |
| Response     |               | None                                        |
| Example      |               | Terminates Fine-Tuning operation.           |
|              | Transmission  | :WAV:FIN:DIS                                |

| Command      |         | [:WAVelength]:FREQuency                           |
| ------------ | ------- | ------------------------------------------------- |
| Description  |         | Sets the output wavelength in optical frequency.  |
| Syntax       | Legacy  | [:SOURce[n]][:CHANnel[m]]:[:WAVelength]:          |
FREQuency<wsp><value>
|     | SCPI  | [:SOURce[n]][:CHANnel[m]][:WAVelength]:  |
| --- | ----- | ---------------------------------------- |
FREQuency<wsp><value>[Hz|kHz|MHz|GHz|THz]
| Parameter  |     | Range: Specified wavelength range  |
| ---------- | --- | ---------------------------------- |
Step: 10MHz
 69 / 113

TSL-570 OPERATION MANUAL
Legacy <value> should be decimal notation in “THz (terahertz)”.
Character strings representing a unit cannot be accepted.
SCPI <value> is accepted in decimal notation and exponential
notation. These numbers are followed by character strings
representing a unit. When a unit character string is not
specified, Hz is used as the default.
Response None
Example Sets the frequency to 200THz.
Legacy :FREQ 200
SCPI1 :FREQ 200THZ
SCPI2 :FREQ 200E+12
Command [:WAVelength]:FREQuency?
Description Reads out output wavelength in optical frequency.
Syntax Legacy [:SOURce[n]][:CHANnel[m]][:WAVelength]:FREQuency?
[:MINimum|:MAXimum]
SCPI [:SOURce[n]][:CHANnel[m]]:WAVelength?<wsp>
[Hz|kHz|MHz|GHz|THz][MINimum|MAXimum]
Parameter None: Reads out the currently setting frequency.
MINimum: Reads out the minimum acceptable frequency.
MAXimum: Reads out the maximum acceptable frequency.
Response Range: Specified frequency range
Step: 10MHz
Legacy Response is decimal notation in “THz”.
SCPI These numbers are followed by character strings representing
a unit. When a unit character string is not specified, Hz is used
as the default.
Example The setting frequency is 200THz.
Transmission : FREQ?
Response Legacy →200
SCPI →+2.00000000E+014
Command :COHCtrl
Description Sets Coherence control status.
Syntax [:SOURce[n]][:CHANnel[m]]:COHCtrl<wsp><value>
Parameter 0: Coherence control OFF
1: Coherence control ON
Response None
Example Sets Coherence control status to ON.
Transmission :COHC 1
70 / 113

Tunable Semiconductor Laser TSL-570
Command :COHCtrl?
Description Reads out Coherence control status.
Syntax [:SOURce[n]][:CHANnel[m]]:COHCtrl?
Parameter None
Response 0: Coherence control OFF
1: Coherence control ON
Example Coherence control status is ON.
Transmission :COHC?
Response Legacy →1
SCPI →+1
Command :POWer:STATe
Description Sets optical output status.
Syntax [:SOURce[n]][:CHANnel[m]]:POWer:STATe<wsp><value>
Parameter 0: optical output OFF
1: optical output ON
Response None
Example Sets optical output status to ON.
Transmission :POW:STAT 1
Command :POWer:STATe?
Description Reads out optical output status.
Syntax [:SOURce[n]][:CHANnel[m]]:POWer:STATe?
Parameter None
Response 0: optical output OFF
1: optical output ON
Example Optical output is active.
Transmission :POW:STAT?
Response Legacy →1
SCPI →+1
Command :POWer:ATTenuation
Description Sets the attenuator value.
Syntax [:SOURce[n]][:CHANnel[m]]:POWer:ATTenuation
<wsp><value>
Parameter Range: 0 〜30 (dB)
Step: 0.01 (dB)
Response None
Example Sets the attenuator value to 10 dB.
Legacy :POW:ATT 10
71 / 113

TSL-570 OPERATION MANUAL
SCPI :POW:ATT +1.00000000E+001
Command :POWer:ATTenuation?
Description Reads out the attenuator value.
Syntax [:SOURce[n]][:CHANnel[m]]:POWer:ATTenuation?
Parameter None
Response Range: 0 〜30 (dB)
Step: 0.01 (dB)
Example The attenuator value is 10 dB.
Transmission :POW:ATT?
Response Legacy →10.00
SCPI →+1.00000000E+001
Command :POWer:ATTenuation:AUTo
Description Sets the power control mode.
Syntax [:SOURce[n]][:CHANnel[m]]:POWer:ATTenuation:AUTo
<wsp><value>
Parameter 0: Manual mode
1: Auto mode
Response None
Example :POW:ATT:AUT 1
Transmission :POW:STAT 1
Command :POWer:ATTenuation:AUTo?
Description Reads out the setting of the power control.
Syntax [:SOURce[n]][:CHANnel[m]]:POWer:ATTenuation:AUTo?
Parameter None
Response 0: Manual mode
1: Auto mode
Example The power control mode is Auto mode.
Transmission :POW:ATT:AUT?
Response Legacy →1
SCPI →+1
Command :POWer[:LEVel]
Description Sets optical output power level.
Syntax Legacy [:SOURce[n]][:CHANnel[m]]:POWer[:LEVel ]<wsp><value>
SCPI [:SOURce[n]][:CHANnel[m]]:POWer[:LEVel ]<wsp>
<value>[PW|NW|UW|MW|Watt|DBM]
Parameter Range: -15dBm to +13dBm
72 / 113

Tunable Semiconductor Laser TSL-570
Step: 0.01dB (0.01mW)
@ Legacy <value> should be decimal notation in “dBm” or “mW”. Units
are defined by the command “:POWer:UNIT”.
Character strings representing a unit cannot be accepted.
SCPI <value> is accepted in decimal notation and exponential
notation. These numbers are followed by character strings
representing a unit. When a unit character string is not
specified, the default units are used. The default units are
defined by
Response None
Example Set the power level to 10dBm.
Legacy :POW 10
SCPI1 :POW 10dBm
SCPI2 :POW +1.00000000E+001
Command :POWer[:LEVel]?
Description Reads out optical output power level setting.
Syntax Legacy [:SOURce[n]][:CHANnel[m]]:POWer[:LEVel]
[:MINimum|MAXimum]?
SCPI [:SOURce[n]][:CHANnel[m]]:POWer[:LEVel]?
<wsp>[dBm|mW][MINimum|MAXimum]
Parameter None: Reads out the current set output power.
MINimum: Reads out the minimum configurable ouput power.
MAXimum: Reads out the maximum configurable output
power.
Response Range: -15dBm to +13dBm
Step: 0.01dB (0.01mW)
Units are defined by the command “:POWer:UNIT”.
Example Setting power level is 10dBm or 10mW. Units are defined by
the command “:POWer:UNIT”.
Transmission :POW?
Response Legacy →10.00
SCPI →+1.00000000E+001
Command :POWer:ACTual[:LEVel]?
Description Reads out monitored optical power. The value is measured by
the built in power monitor.
Syntax [:SOURce[n]][:CHANnel[m]]:POWer:ACTual[:LEVel]?
Parameter None
Response Range: -15dBm to peak power
Step: 0.01dB (0.01mW)
73 / 113

TSL-570 OPERATION MANUAL
Units are defined by the command “:POWer:UNIT”.
Example Monitored power level is 9.6dBm or 9.6mW. Units are defined
by the command “:POWer:UNIT”.
Transmission :POW:ACT?
Response Legacy →9.60
SCPI →+9.60000000E+000
Command :POWer:SHUTter
Description Sets Open/Close status of the internal shutter. The function is
same as the Laser ON/OFF command “:POWer:STATe” (Note,
the relationship between parameter and state is reversed).
Syntax [:SOURce[n]][:CHANnel[m]]:POWer:SHUTter<wsp><value>
Parameter 0: Shutter Open
1: Shutter Close
Response None
Example Closes the internal shutter.
Transmission :POW:SHUT 1
Command :POWer:SHUTter?
Description Reads out the status of the internal shutter.
Syntax [:SOURce]:POWer:SHUTter?
Parameter None
Response 0: Shutter Open
1: Shutter Close
Example The internal shutter is closed.
Transmission :POW:SHUT?
Response Legacy →1
SCPI →+1
Command :POWer:UNIT
Description Changes the unit of the power setting and display.
Syntax [:SOURce[n]][:CHANnel[m]]:POWer:UNIT<wsp><value>
Parameter 0: dBm
1: mW
Response None
Example Sets the power setting and display unit to “mW”.
Transmission :POW:UNIT 1
Command :POWer:UNIT?
Description Reads out the unit of the power setting and display.
74 / 113

Tunable Semiconductor Laser TSL-570
Syntax [:SOURce[n]][:CHANnel[m]]:POWer:UNIT?
Parameter None
Response 0: dBm
1: mW
Example The setting unit of power is mW.
Transmission :POW:UNIT?
Response Legacy →1
SCPI →+1
Command :WAVelength:SWEep:STARt
Description Sets the sweep start wavelength.
Syntax Legacy [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:STARt
<wsp><value>
SCPI [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:
STARt<wsp><value>[PM|NM|UM|MM|M]
Parameter Range: Specified wavelength range
Step: 0.1 pm
Legacy <value> should be decimal notation in “nm”. Character strings
representing a unit cannot be accepted.
SCPI <value> is accepted in decimal notation and exponential
notation. These numbers are followed by character strings
representing a unit. When a unit character string is not
specified, m（meter）is used as the default.
Response None
Example Sets sweep start wavelength to 1480 nm.
Legacy :WAV:SWE:STARt 1480
SCPI1 :WAV:SWE:STARt 1480nm
SCPI2 :WAV:SWE:STARt 1480E-9
Command :WAVelength:SWEep:STARt?
Description Reads out the sweep start wavelength.
Syntax Legacy [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:STARt?
SCPI [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:STARt?
<wsp>[PM|NM|UM|MM|M]
Parameter None
Response Range: Specified wavelength range
Step: 0.1pm
Legacy Response is decimal notation in “nm”.
SCPI These numbers are followed by character strings representing
a unit. When a unit character string is not specified, m
（meter）is used as the default.
75 / 113

TSL-570 OPERATION MANUAL
Example Setting sweep start wavelength is 1480 nm.
Transmission :WAV:SWE:STARt?
Response Legacy →1480.0000
SCPI →+1.48000000E-006
Command [:WAVelength]:FREQuency:SWEep:STARt
Description Sets the sweep start wavelength in optical frequency.
Syntax Legacy [:SOURce[n]][:CHANnel[m]][:WAVelength]:FREQuency:
SWEep:STARt<wsp><value>
SCPI [:SOURce[n]][:CHANnel[m]][:WAVelength]:FREQuency:
SWEep:STARt<wsp><value>[Hz|kHz|MHz|GHz|THz]
Parameter Range: Specified wavelength range
Step: 10MHz
Legacy <value> should be decimal notation in “THz”. Character strings
representing a unit cannot be accepted.
SCPI <value> is accepted in decimal notation and exponential
notation. These numbers are followed by character strings
representing a unit. When a unit character string is not
specified, Hz（Hertz）is used as the default.
Response None
Example Sets the sweep start wavelength to 185.057 THz.
Legacy :FREQ:SWE:STAR 185.0570
SCPI1 :FREQ:SWE:STAR 185.057THZ
SCPI2 :FREQ:SWE:STAR 185.057E+12
Command [:WAVelength]:FREQuency:SWEep:STARt?
Description Reads out the sweep start wavelength in optical frequency.
Syntax Legacy [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:STARt?
SCPI [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:STARt?
<wsp>[Hz|kHz|MHz|GHz|THz]
Parameter None
Response Range: Specified wavelength range
Step: 10MHz
Legacy Response is decimal notation in “THz”.
SCPI These numbers are followed by character strings representing
a unit. When a unit character string is not specified, Hz is used
as the default.
Example Setting sweep start frequency is 185.0570THz.
Transmission :FREQ:SWE:STAR?
Response Legacy →185.057
SCPI →+1.8505700E+014
76 / 113

Tunable Semiconductor Laser TSL-570
Command :WAVelength:SWEep:STOP
Description Sets the sweep stop wavelength.
Syntax Legacy :SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:STOP
<wsp><value>
SCPI [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:STOP
<wsp><value>[PM|NM|UM|MM|M]
Parameter Range: Specified wavelength range
Step: 0.1 pm
Legacy <value> should be decimal notation in “nm”. Character strings
representing a unit cannot be accepted.
SCPI <value> is accepted in decimal notation and exponential
notation. These numbers are followed by character strings
representing a unit. When a unit character string is not
specified, m（meter）is used as the default.
Response None
Example Sets sweep stop wavelength to 1640 nm.
Legacy :WAV:SWE:STOP 1640
SCPI1 :WAV:SWE:STOP 1640nm
SCPI2 :WAV:SWE:STOP 1640E-9
Command :WAVelength:SWEep:STOP?
Description Reads out the sweep stop wavelength.
Syntax Legacy [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:STOP?
SCPI [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:STOP?
STOP?<wsp>[PM|NM|UM|MM|M]
Parameter None
Response Range: Specified wavelength range
Step: 0.1pm
Legacy Response is decimal notation in “nm”.
SCPI These numbers are followed by character strings representing
a unit. When a unit character string is not specified, m
（meter）is used as the default.
Example Setting sweep stop wavelength is 1640 nm.
Transmission :WAV:SWE:STOP?
Response Legacy →1640.0000
SCPI →+1.64000000E-006
Command :WAVelength:SWEep:RANGe:MINimum?
Description Reads out the minimum wavelength in the configurable sweep
range
77 / 113

TSL-570 OPERATION MANUAL
Syntax Legacy [:SOURce]:WAVelength:SWEep:RANGe:MINimum?
SCPI [:SOURce]:WAVelength:SWEep:RANGe:MINimum?
[PM|NM|UM|MM|M]
Parameter None
Response Range: The minimum wavelength in the configurable sweep
range at the current sweep speed
Step: 0.1pm
Legacy Response is decimal notation in “nm”.
SCPI These numbers are followed by character strings representing
a unit. When a unit character string is not specified, m
（meter）is used as the default.
Example The minimum wavelength in the configurable sweep range is
1482 nm.
Transmission :WAV:SWE:RANG:MIN?
Response Legacy →1482.0000
SCPI →+1.48200000E-006
Command :WAVelength:SWEep:RANGe:MAXimum?
Description Reads out the maximum wavelength in the configurable sweep
range
Syntax Legacy [:SOURce]:WAVelength:SWEep:RANGe:MAXimum?
SCPI [:SOURce]:WAVelength:SWEep:RANGe:MAXimum?
[PM|NM|UM|MM|M]
Parameter None
Response Range: The maximum wavelength in the configurable sweep
range at the current sweep speed
Step: 0.1pm
Legacy Response is decimal notation in “nm”.
SCPI These numbers are followed by character strings representing
a unit. When a unit character string is not specified, m
（meter）is used as the default.
Example The maximum wavelength in the configurable sweep range is
1638 nm.
Transmission :WAV:SWE:RANG:MAX?
Response Legacy →1638.0000
SCPI →+1.63800000E-006
Command [:WAVelength]:FREQuency:SWEep:STOP
Description Sets the sweep stop wavelength in optical frequency.
Syntax Legacy [:SOURce[n]][:CHANnel[m]][:WAVelength]:FREQuency:
SWEep:STOP<wsp><value>
78 / 113

Tunable Semiconductor Laser TSL-570
SCPI [:SOURce[n]][:CHANnel[m]][:WAVelength]:FREQuency:
SWEep:STOP<wsp><value>[Hz|kHz|MHz|GHz|THz]
Parameter Range: Specified wavelength range
Step: 10MHz
Legacy <value> should be decimal notation in “THz”. Character strings
representing a unit cannot be accepted.
SCPI <value> is accepted in decimal notation and exponential
notation. These numbers are followed by character strings
representing a unit. When a unit character string is not
specified, Hz（Hertz）is used as the default.
Response None
Example Sets the sweep stop wavelength to 185.057 THz.
Legacy :FREQ:SWE:STOP 185.05700
SCPI1 :FREQ:SWE:STOP 185.05700THZ
SCPI2 :FREQ:SWE:STOP 185.05700E+12
Command [:WAVelength]:FREQuency:SWEep:STOP?
Description Reads out the sweep stop wavelength in optical frequency.
Syntax Legacy [:SOURce[n]][:CHANnel[m]][:WAVelength]:FREQuency:
SWEep:STOP?
SCPI [:SOURce[n]][:CHANnel[m]][:WAVelength]:FREQuency:
SWEep:STOP?<wsp>[Hz|kHz|MHz|GHz|THz]
Parameter None
Response Range: Specified wavelength range
Step: 10MHz
Legacy Response is decimal notation in “THz”.
SCPI These numbers are followed by character strings representing
a unit. When a unit character string is not specified, Hz
（Hertz）is used as the default.
Example Setting sweep stop frequency is 185.0570THz.
Transmission :FREQ:SWE:STOP?
Response Legacy →185.05700
SCPI →+1.8505700E+014
Command :FREQuency:SWEep:RANGe:MINimum?
Description Reads out the minimum frequency in the configurable sweep
range
Syntax Legacy [:SOURce][:WAVelength]:FREQuency:SWEep:RANGe
:MINimum?
SCPI [:SOURce][:WAVelength]:FREQuency:SWEep:RANGe
:MINimum? [HZ|KHZ|MHZ|GHZ|THZ]
79 / 113

TSL-570 OPERATION MANUAL
Parameter None
Response Range: The minimum frequency in the configurable sweep
range at the current sweep speed
Step: 10MHz
Legacy <value> should be decimal notation in “THz”. Character strings
representing a unit cannot be accepted.
SCPI <value> is accepted in decimal notation and exponential
notation. These numbers are followed by character strings
representing a unit. When a unit character string is not
specified, Hz（Hertz）is used as the default.
Example The minimum frequency in the configurable sweep range is
182.80028THz.
Transmission :FREQ:SWE:RANG:MIN?
Response Legacy →182.80028
SCPI →1.82800280E+014
Command 80:FREQuency:SWEep:RANGe:MAXimum?
Description Reads out the maximum frequency in the configurable sweep
range
Syntax Legacy [:SOURce][:WAVelength]:FREQuency:SWEep:RANGe
:MAXimum?
SCPI [:SOURce][:WAVelength]:FREQuency:SWEep:RANGe
:MAXimum? [HZ|KHZ|MHZ|GHZ|THZ]
Parameter None
Response Range: The maximum frequency in the configurable sweep
range at the current sweep speed
Step: 10MHz
Legacy <value> should be decimal notation in “THz”. Character strings
representing a unit cannot be accepted.
SCPI <value> is accepted in decimal notation and exponential
notation. These numbers are followed by character strings
representing a unit. When a unit character string is not
specified, Hz（Hertz）is used as the default.
Example The maximum frequecy in the configurable sweep range is
202.56247THz.
Transmission :FREQ:SWE:RANG:MAX?
Response Legacy →202.56247
SCPI →+2.02562470E+014
Command :WAVelength:SWEep:MODe
Description Sets the sweep mode.
80 / 113

                                       Tunable Semiconductor Laser TSL-570
|     | Syntax  | [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:  |
| --- | ------- | -------------------------------------------- |
MODe<wsp><value>
| Parameter  |     | 0: Step sweep mode and One way  |
| ---------- | --- | ------------------------------- |
1: Continuous sweep mode and One way
2: Step sweep mode and Two way
3: Continuous sweep mode and Two way
| Response  |               | None                                            |
| --------- | ------------- | ----------------------------------------------- |
| Example   |               | Sets the sweep mode to continuous and One way.  |
|           | Transmission  | :WAV:SWE:MOD 1                                  |

| Command      |         | :WAVelength:SWEep:MODe?                           |
| ------------ | ------- | ------------------------------------------------- |
| Description  |         | Reads out the sweep mode.                         |
|              | Syntax  | [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:MODe?  |
| Parameter    |         | None                                              |
| Response     |         | 0: Step sweep mode and One way                    |
1: Continuous sweep mode and One way
2: Step sweep mode and Two way
3: Continuous sweep mode and Two way
| Example       |         | Setting sweep mode is continuous and One way.  |
| ------------- | ------- | ---------------------------------------------- |
| Transmission  |         | :WAV:SWE:MOD?                                  |
| Response      | Legacy  | →1                                             |
|               | SCPI    | →+1                                            |

| Command      |         | :WAVelength:SWEep:SPEed                      |
| ------------ | ------- | -------------------------------------------- |
| Description  |         | Sets the sweep speed.                        |
| Syntax       | Legacy  | [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:  |
SPEed<wsp><value>
|     | SCPI  | [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:  |
| --- | ----- | -------------------------------------------- |
SPEed<wsp><value>
| Parameter  |     | Range: 1 to 200 nm/s  |
| ---------- | --- | --------------------- |
Selection: 1,2,5,10,20,50,100,200 (nm/s)
  Legacy  <value> should be decimal notation in “nm/s”. Character
strings representing a unit cannot be accepted.
|     | SCPI  | <value> should be decimal notation in “nm/s”. Character  |
| --- | ----- | -------------------------------------------------------- |
strings representing a unit cannot be accepted.
| Response  |         | None                               |
| --------- | ------- | ---------------------------------- |
| Example   |         | Sets the sweep speed to 200 nm/s.  |
|           | Legacy  | :WAV:SWE:SPE 200                   |
|           | SCPI    | :WAV:SWE:SPE 200                   |

| Command  |     | :WAVelength:SWEep:SPEed?  |
| -------- | --- | ------------------------- |
 81 / 113

TSL-570 OPERATION MANUAL
| Description  |     | Reads out sweep speed.  |
| ------------ | --- | ----------------------- |
Syntax  Legacy  [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:SPEed?
|            | SCPI  | [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:SPEed?  |
| ---------- | ----- | -------------------------------------------------- |
| Parameter  |       | None                                               |
| Response   |       | Range: 1 to 200 nm/s                               |
Selection: 1,2,5,10,20,50,100,200 (nm/s)
  Legacy  Character strings representing a unit cannot be accepted.
  SCPI  Character strings representing a unit cannot be accepted.
| Example         |         | Setting sweep speed is 200nm/s.  |
| --------------- | ------- | -------------------------------- |
|   Transmission  |         | :WAV:SWE:SPE?                    |
| Response        | Legacy  | →200.0                           |
|                 | SCPI    | →+200.0                          |

| Command      |         | :WAVelength:SWEep:STEP[:WIDTh]               |
| ------------ | ------- | -------------------------------------------- |
| Description  |         | Sets the step for Step sweep mode.           |
| Syntax       | Legacy  | [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:  |
STEP[:WIDTh]<wsp><value>
|     | SCPI  | [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:  |
| --- | ----- | -------------------------------------------- |
STEP[:WIDTh]<wsp><value>[PM|NM|UM|MM|M]
| Parameter  |     | Range: 0.1pm to specified wavelength span.  |
| ---------- | --- | ------------------------------------------- |
Step: 0.1 pm
  Legacy  <value> should be decimal notation in “nm”. Character strings
representing a unit cannot be accepted.
|     | SCPI  | <value> is accepted in decimal notation and exponential  |
| --- | ----- | -------------------------------------------------------- |
notation. These numbers are followed by character strings
representing a unit. When a unit character string is not
specified, meters are used as the default units.
| Response  |         | None                       |
| --------- | ------- | -------------------------- |
| Example   |         | Sets the step to 0.01 nm.  |
|           | Legacy  | :WAV:SWE:STEP 0.01         |
|           | SCPI1   | :WAV:SWE:STEP 10pm         |
|           | SCPI2   | :WAV:SWE:STEP 1.0E-11      |

| Command      |         | :WAVelength:SWEep:STEP[:WIDTh]?              |
| ------------ | ------- | -------------------------------------------- |
| Description  |         | Reads out the step for Step sweep mode.      |
| Syntax       | Legacy  | [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:  |
STEP[:WIDTh]?
|     | SCPI  | [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:  |
| --- | ----- | -------------------------------------------- |
STEP[:WIDTh]?<wsp>[PM|NM|UM|MM|M]
| Parameter  |     | None                                        |
| ---------- | --- | ------------------------------------------- |
| Response   |     | Range: 0.1pm to specified wavelength span.  |
 82 / 113

                                       Tunable Semiconductor Laser TSL-570
Step: 0.1 pm
|     | Legacy  | Response is decimal notation in “nm”.  |
| --- | ------- | -------------------------------------- |
  SCPI  These numbers are followed by character strings representing
a unit. When a unit character string is not specified, meters are
used as the default units.
| Example         |         | Setting step is 0.1 nm.  |
| --------------- | ------- | ------------------------ |
|   Transmission  |         | :WAV:SWE:STEP?           |
| Response        | Legacy  | →0.100                   |
|                 | SCPI    | →+1.00000000E-010        |

| Command      |         | [:WAVelength]:FREQuency:SWEep:STEP[:WIDTh]               |
| ------------ | ------- | -------------------------------------------------------- |
| Description  |         | Sets the step for Step sweep mode in optical frequency.  |
| Syntax       | Legacy  | [:SOURce[n]][:CHANnel[m]][:WAVelength]:                  |
FREQuency:SWEep:STEP[:WIDTh]<wsp><value>
|     | SCPI  | [:SOURce[n]][:CHANnel[m]][:WAVelength]  |
| --- | ----- | --------------------------------------- |
:FREQuency:SWEep:STEP[:WIDTh]<wsp><value>
[Hz|kHz|MHz|GHz|THz]
| Parameter  |     | Range: 20MHz to specified wavelength span.  |
| ---------- | --- | ------------------------------------------- |
Step: 10 MHz
  Legacy  <value> should be decimal notation in “THz”. Character strings
representing a unit cannot be accepted.
|     | SCPI  | <value> is accepted in decimal notation and exponential  |
| --- | ----- | -------------------------------------------------------- |
notation. These numbers are followed by character strings
representing a unit. When a unit character string is not
specified, “Hz” are used as the default units.
| Response  |         | None                      |
| --------- | ------- | ------------------------- |
| Example   |         | Sets the step to 10 GHz.  |
|           | Legacy  | :FREQ:SWE:STEP 0.010      |
|           | SCPI1   | :FREQ:SWE:STEP 10GHZ      |
|           | SCPI2   | :FREQ:SWE:STEP 1.0E+10    |

| Command  |     | [:WAVelength]:FREQuency:SWEep:STEP[:WIDTh]?  |
| -------- | --- | -------------------------------------------- |
Description  Reads out the step for Step Sweep mode in optical frequency.
| Syntax  | Legacy  | [:SOURce[n]][:CHANnel[m]][:WAVelength]:  |
| ------- | ------- | ---------------------------------------- |
FREQuency:SWEep:STEP[:WIDTh]?
|     | SCPI  | [:SOURce[n]][:CHANnel[m]][:WAVelength]:  |
| --- | ----- | ---------------------------------------- |
FREQuency:SWEep:STEP[:WIDTh]?<wsp>
[Hz|kHz|MHz|GHz|THz]
| Parameter  |     | None                                        |
| ---------- | --- | ------------------------------------------- |
| Response   |     | Range: 20MHz to specified wavelength span.  |
Step: 10 MHz
 83 / 113

TSL-570 OPERATION MANUAL
Legacy Response is decimal notation in “THz”.
SCPI These numbers are followed by character strings representing
a unit. When a unit character string is not specified, “Hz” are
used as the default units.
Example Setting step is 0.01 THz.
Transmission :WAV:SWE:STEP?
Response Legacy →0.01
SCPI →+1.0000000E+010
Command :WAVelength:SWEep:DWELl
Description Sets wait time between consequent steps in step sweep mode.
This wait time does not include time for wavelength tuning.
Syntax [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:
DWELl<wsp><value>
Parameter Range: 0 to 999.9 sec
Step: 0.1 sec
Response None
Example Sets the dwell time to 1 second.
Transmission :WAV:SWE:DWEL 1
Command :WAVelength:SWEep:DWELl?
Description Reads out wait time between consequent steps in step sweep
mode.
Syntax [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:DWELl?
Parameter None
Response Range: 0 to 999.9 sec
Step: 0.1 sec
Example Setting dwell time to 3 seconds.
Transmission :WAV:SWE:DWEL?
Response Legacy →3.0
SCPI →+3.00000000E+000
Command :WAVelength:SWEep:CYCLes
Description Sets the sweep repetition times.
Syntax [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:
CYCLes<wsp><value>
Parameter Range: 0 to 999
Step: 1
Response None
Example Sets the sweep repetition times to 100.
Transmission :WAV:SWE:CYCL 100
84 / 113

Tunable Semiconductor Laser TSL-570
Command :WAVelength:SWEep:CYCLes?
Description Reads out the setting sweep repetition times.
Syntax [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:CYCLes?
Parameter None
Response Range: 0 to 999
Example The setting repetition times is 100.
Transmission :WAV:SWE:CYCL?
Response Legacy →100
SCPI →+100
Command :WAVelength:SWEep:COUNt?
Description Reads out the current number of completed sweeps.
Syntax [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:COUNt?
Parameter None
Response Range: 0 to 999
Example 100 sweeps have completed.
Transmission :WAV:SWE:COUN?
Response Legacy →100
SCPI →+100
Command :WAVelength:SWEep:DELay
Description Sets the wait time between consequent scans.
Syntax [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep:
DELay<wsp><value>
Parameter Range: 0 to 999.9 sec
Step: 0.1 sec
Response None
Example Sets the wait time to 1 second.
Transmission :WAV:SWE:DEL 1
Command :WAVelength:SWEep:DELay?
Description Reads out the setting wait time between consequent scans.
Syntax [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep: DELay?
Parameter None
Response Range: 0 to 999.9 sec
Step: 0.1 sec
Example Setting wait time is 1 second.
Transmission :WAV:SWE:DEL?
Response Legacy →1.0
85 / 113

TSL-570 OPERATION MANUAL
SCPI →+1.00000000E+000
Command :WAVelength:SWEep[:STATe]
Description Sets sweep status.
Syntax [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep
[:STATe]<wsp><value>
Parameter 0: Stop.
1: Start.
This command executes single scan. Use
“:WAVelength:SWEep[:STATe]:REPeat” for repeat scan.
Response None
Example Starts a sweep.
Transmission :WAV:SWE 1
Command :WAVelength:SWEep[:STATe]?
Description Reads out the current sweep status.
Syntax [:SOURce[n]][:CHANnel[m]]:WAVelength:SWEep[:STATe]?
Parameter None
Response 0: Stopped
1: Running
3: Standing by trigger
4: Preparation for sweep start
Example Sweep is running.
Transmission :WAV:SWE?
Response Legacy →1
SCPI →+1
Command :WAVelength:SWEep[:STATe]:REPeat
Description Starts repeat scan.
Syntax [:SOURce[n]][:CHANnel[m]]:WAVelength:
SWEep[:STATe]:REPeat
Parameter None
Response None
Example Starts repeat scan.
Transmission :WAV:SWE:REP
Command :READout:POINts?
Description Reads out the number of logging data.
Syntax [:SOURce[n]][:CHANnel[m]]:READout:POINts?
Parameter None
86 / 113

Tunable Semiconductor Laser TSL-570
Response 0 to 500,000
Example Recorded data number is 10,000.
Transmission :READ:POIN?
Response Legacy →10000
SCPI →+10000
Command :READout:DATa?
Description Reads out walength logging data.
Syntax [:SOURce[n]][:CHANnel[m]]:READout:DATa?
Parameter None
Response Please refer to the following.
Legacy The data is comprised of a header (ASCII characters) and
wavelength data array (4-byte binary).
Example: #42000 □□□□□□□□ .......
The “4” after the “#” indicates the number of digits following
“4”. The following four digits, “2000”, indicate the amount of
recorded data in byte units. In this example, there are 2000
bytes of data (500 points).
The data is saved in integer format in 0.1 pm units. Binary data
is transmitted in Intel byte order.
SCPI The data is comprised of a header (ASCII characters) and
wavelength data array (8-byte binary).
Example: #44000 □□□□□□□□ The “4” after the
“#” indicates the number of digits following “4”. The following
four digits, “4000” indicate the amount of recorded data in byte
units. n this example, there are 4000 bytes of data (500 points).
The data is saved in the 64 bit IEEE Standard format and data
is transmitted in Intel byte order.
Command :READout:DATa:POWer?
Description Reads out power logging data.
Syntax [:SOURce[n]][:CHANnel[m]]:READout:DATa:POWer?
Parameter None
Response The data is comprised of a header
(ASCII characters) and wavelength data array (4- byte binary).
Example: #42000 □□□□□□□□ .......
The “4” after the “#” indicates the number of digits following is
4. The following four digits, “2000”, indicate the amount of
recorded data in byte units. In this example, there are 2000
bytes of data (500 points).
87 / 113

TSL-570 OPERATION MANUAL
The data is saved in the 32 bit IEEE Standard format and data
is transmitted in Intel byte order. The data is saved in dBm.
Command :AM:STATe
Description Enables and disables modulation function of the laser output.
Syntax [:SOURce[n]][:CHANnel[m]]:AM:STATe<wsp><value>
Parameter 0: Disable
1: Enable
Response None
Example Enables the modulation function of the laser output.
Transmission :AM:STAT 1
Command :AM:STATe?
Description Reads out status of modulation function of the laser output.
Syntax [:SOURce[n]][:CHANnel[m]]:AM:STATe?
Parameter None
Response 0: Disable
1: Enable
Example The modulation function is enabled.
Transmission :AM:STAT?
Response Legacy →1
SCPI →+1
Command :AM:SOURce
Description Sets modulation source.
Syntax [:SOURce[n]][:CHANnel[m]]:AM:SOURce<wsp><value>
Parameter 0: Coherence control (same operation as “:COHCtrl”)
1: Intensity modulation
3: Frequency modulation
Response None
Example Selects Coherence control.
Transmission :AM:SOUR 0
Command :AM:SOURce?
Description Reads out modulation source.
Syntax [:SOURce[n]][:CHANnel[m]]:AM:SOURce?
Parameter None
Response 0: Coherence control (same operation as “:COHCtrl”)
1: Intensity modulation
3: Frequency modulation
88 / 113

Tunable Semiconductor Laser TSL-570
Example The intensity modulation is set.
Transmission :AM:SOUR?
Response Legacy →1
SCPI →+1
Command [:SOURce]:WAVelength:OFFSet
Description Add the constant offset to the output wavelength.
Syntax Legacy :WAVelength:OFFSet<wsp><value>
SCPI :WAVelength:OFFSet<wsp><value>
Parameter Range: -0.1000 ~ 0.1000 (nm)
Step: 0.0001（nm）
Legacy <value> should be decimal notation in “nm”. Character strings
representing a unit cannot be accepted.
SCPI <value> is accepted in decimal notation and exponential
notation. These numbers are followed by character strings
representing a unit. When a unit character string is not
specified, m（meter）is used as the default.
Response None
Example Adds the constant offset by 0.01nm to the output wavelength.
Legacy :WAV:OFFS 0.010
SCPI1 :WAV:OFFS 10pm
SCPI2 :WAV:OFFS 1.0E-13
Command [:SOURce]:WAVelength:OFFSet?
Description Reads out the constant offset to the output wavelength.
Syntax Legacy [:SOURce]:WAVelength:OFFSet?
SCPI [:SOURce]:WAVelength:OFFSet?<wsp>[PM|NM|UM|MM|M]
Parameter None
Response Range: -0.1000 ~ 0.1000 (nm)
Step: 0.0001（nm）
Legacy Response is decimal notation in “nm”.
SCPI These numbers are followed by character strings representing
a unit. When a unit character string is not specified, m
(meter）is used as the default.
Example The constant offset to the output wavelength is 0.01nm.
Transmission :WAV:OFFS?
Response Legacy →0.01
SCPI →+1.00000000E-013
89 / 113

TSL-570 OPERATION MANUAL
2. Input/ Output related command
Command :TRIGger:INPut:EXTernal
Description Enables / Disables external trigger input.
Syntax :TRIGger:INPut:EXTernal<wsp><value>
Parameter 0: Disable
1: Enable
Response None
Example Enables external trigger input.
Transmission :TRIG:INP:EXT 1
Command :TRIGger:INPut:EXTernal?
Description Reads out the setting of external trigger input.
Syntax :TRIGger:INPut:EXTernal?
Parameter None
Response 0: Disable
1: Enable
Example External trigger input is enabled.
Transmission :TRIG:INP:EXT?
Response Legacy →1
SCPI →+1
Command :TRIGger:INPut[:EXTernal]:ACTive
Description Sets input trigger polarity.
Syntax :TRIGger:INPut[:EXTernal]:ACTive<wsp><value>
Parameter 0: High Active / Triggers at rising edge
1: Low Active / Triggers at falling edge
Response None
Example Sets the input trigger polarity to Low Active.
Transmission :TRIG:INP:ACT 1
Command :TRIGger:INPut[:EXTernal]:ACTive?
Description Reads out input trigger polarity.
Syntax :TRIGger:INPut[:EXTernal]:ACTive?
Parameter None
Response 0: High Active / Triggers at rising edge
1: Low Active / Triggers at falling edge
Example The input trigger polarity is set to Low Active.
Transmission :TRIG:INP:ACT?
Response Legacy →1
90 / 113

Tunable Semiconductor Laser TSL-570
SCPI →+1
Command :TRIGger:INPut:STANdby
Description Sets the device in trigger signal input standby mode.
Syntax :TRIGger:INPut:STANdby<wsp><value>
Parameter 0: Normal operation mode
1: Trigger standby mode
Response None
Example Sets the device in trigger standby mode.
Transmission :TRIG:INP:STAN 1
Command :TRIGger:INPut:STANdby?
Description Reads out the trigger signal input standby mode.
Syntax :TRIGger:INPut:STANdby?
Parameter None
Response 0: Normal operation mode
1: Trigger standby mode
Example The device is in trigger standby mode.
Transmission :TRIG:INP:STAN?
Response Legacy →1
SCPI →+1
Command :TRIGger:INPut:SOFTtrigger
Description Issues a soft trigger. Executes sweep from trigger standby
mode.
Syntax :TRIGger:INPut:SOFTtrigger
Parameter None
Response None
Example Issues a soft trigger.
Transmission :TRIG:INP:SOFT
Command :TRIGger:OUTPut
Description Sets the timing of the trigger signal output.
Syntax :TRIGger:OUTPut<wsp><value>
Parameter 0: None
1: Stop
2: Start
3: Step
Response None
91 / 113

TSL-570 OPERATION MANUAL
Example Sets the timing of the trigger signal output to be at sweep
completion.
Transmission :TRIG:OUTP 1
Command :TRIGger:OUTPut?
Description Reads out the timing setting of the trigger signal output.
Syntax :TRIGger:OUTPut?
Parameter None
Response 0: None
1: Stop
2: Start
3: Step
Example The timing of the trigger signal output is at sweep start.
Transmission :TRIG:OUTP?
Response Legacy →2
SCPI →+2
Command :TRIGger:OUTPut:ACTive
Description Sets output trigger polarity.
Syntax :TRIGger:OUTPut:ACTive<wsp><value>
Parameter 0: High Active / Triggers at rising edge
1: Low Active / Triggers at falling edge
Response None
Example Sets the output trigger polarity to High Active.
Transmission :TRIG:OUTP:ACT 0
Command :TRIGger:OUTPut:ACTive?
Description Reads out output trigger polarity.
Syntax :TRIGger:OUTPut?
Parameter None
Response 0: High Active / Triggers at rising edge
1: Low Active / Triggers at falling edge
Example The output trigger polarity is set to High Active.
Transmission :TRIG:OUTP:ACT?
Response Legacy →0
SCPI →+0
Command :TRIGger:OUTPut:STEP[:WIDTh]
Description Sets the interval of the trigger signal output.
Syntax Legacy :TRIGger:OUTPut:STEP[:WIDTh]<wsp><value>
92 / 113

Tunable Semiconductor Laser TSL-570
SCPI :TRIGger:OUTPut:STEP[:WIDTh]<wsp><value>[PM|
NM|UM|MM|M]
Parameter Range：0.0001 〜 Maximum specified wavelength range (nm)
Step：0.0001（nm）
The minimum set trigger step depends on the setting sweep
speed. Refer to “6-5. Trigger Setting” for details.
Legacy <value> should be decimal notation in “nm”. Character strings
representing a unit cannot be accepted.
SCPI <value> is accepted in decimal notation and exponential
notation. These numbers are followed by character strings
representing a unit. When a unit character string is not
specified, m（meter）is used as the default.
Response None
Example Sets the interval of the trigger signal output to 1nm.
Legacy :TRIG:OUTP:STEP 1
SCPI1 :TRIG:OUTP:STEP 1nm
SCPI2 :TRIG:OUTP:STEP 1E-9
Command :TRIGger:OUTPut:STEP[:WIDTh]?
Description Reads out the interval of the trigger signal output.
Syntax :TRIGger:OUTPut:STEP[:WIDTh]?
Parameter None
Response Range: 0.0001 〜 Maximum specified wavelength range (nm)
Step: 0.0001（nm）
Leagacy Response is decimal notation in “nm”.
SCPI Response is exponential notation in meters.
Example the trigger signal output interval is 0.1 nm.
Transmission :TRIG:OUTP: STEP?
Response Legacy →0.100
SCPI →+1.00000000E-010
Command :TRIGger:OUTPut:SETTing
Description Sets the output trigger period mode.
Syntax :TRIGger:OUTPut:SETTing<wsp><value>
Parameter 0: Sets the output trigger to be periodic in wavelength.
1: Sets the output trigger to be periodic in time.
Response None
Example Sets the output trigger to be periodic in wavelength.
Transmission :TRIG:OUTP:SETT 0
Command :TRIGger:OUTPut:SETTing?
93 / 113

TSL-570 OPERATION MANUAL
Description Reads out the output trigger period mode.
Syntax :TRIGger:OUTPut:SETTing?
Parameter None
Response 0: Output trigger is periodic in wavelength.
1: Output trigger is periodic in time.
Example The output trigger is periodic in wavelength.
Transmission :TRIG:OUTP:SETT?
Response Legacy →0
SCPI →+0
Command :TRIGger:THRough
Description Sets the trigger through mode. When On is selected, input
trigger signal is put through to the output trigger port. Trigger
signal is re-shaped according to polarity setting.
Syntax :TRIGger:THRough<wsp><value>
Parameter 0: OFF
1: ON
Response None
Example Sets the trigger through mode to ON.
Transmission :TRIG:THR 1
Command :TRIGger:THRough?
Description Reads out the trigger through mode.
Syntax :TRIGger:THRough?
Parameter None
Response 0: OFF
1: ON
Example The trigger through mode is set to ON.
Transmission :TRIG:THR?
Response Legacy →1
SCPI →+1
3. System related commands
Command :SYSTem:ERRor?
Description Reads out the error issued.
Syntax :SYSTem:ERRor?
Parameter None
Response Error Number (Refer to “7-4 5. Command Error”)
Example Error numbers and error messages are returned.
94 / 113

Tunable Semiconductor Laser TSL-570
Transmission :SYST:ERR?
Command :SYSTem:COMMunicate:GPIB:ADDRess
Description Sets the GPIB address.
Syntax :SYSTem:COMMunicate:GPIB:ADDRess<wsp><value>
Parameter Integer from 1 to 30
Response None
Example Sets the GPIB address to “10”.
Transmission :SYST:COMM:GPIB:ADDR 10
Command :SYSTem:COMMunicate:GPIB:ADDRess?
Description Reads out the GPIB address.
Syntax :SYSTem:COMMunicate:GPIB:ADDRess?
Parameter None
Response Integer from 1 to 30
Example The GPIB address is “10”.
Transmission :SYST:COMM:GPIB:ADDR?
Response Legacy →10
SCPI →+10
Command :SYSTem:COMMunicate:GPIB:DELimiter
Description Sets the command delimiter for GPIB communication. EOI is
always sent.
Syntax :SYSTem:COMMunicate:GPIB:DELimiter<wsp><value>
Parameter 0: CR
1: LF
2: CR+LF
3: None
Response None
Example Sets the GPIB command delimiter to “LF”.
Transmission :SYST:COMM:GPIB:DEL 1
Command :SYSTem:COMMunicate:GPIB:DELimiter?
Description Reads out the command delimiter for GPIB communication.
Syntax :SYSTem:COMMunicate:GPIB:ADDRess?
Parameter None
Response 0: CR
1: LF
2: CR+LF
3: None
95 / 113

TSL-570 OPERATION MANUAL
Example The GPIB delimiter is ”LF”.
Transmission :SYST:COMM:GPIB:DEL?
Response Legacy →1
SCPI →+1
Command :SYSTem:COMMunicate:ETHernet:MACaddress?
Description Reads out the MAC address.
Syntax :SYSTem:COMMunicate:GPIB:ADDRess?
Parameter None
Response 12 digits hexadecimal
Example The read MAC address is 00-13-A0-00-00-00.
Transmission :SYST:COMM:ETH:MAC?
Response →0013A0000000
Command :SYSTem:COMMunicate:ETHernet:IPADdress
Description Sets the IP address.
Syntax :SYSTem:COMMunicate:ETHernet:IPADdress<wsp><value>
Parameter ***.***.***.*** (*** is integer from 0 to 255)
Response None
Example Sets the IP address to “192.168.0.1”.
Transmission :SYST:COMM:ETH:IPAD 192.168.0.1
Command :SYSTem:COMMunicate:ETHernet:IPADdress?
Description Reads out the IP address.
Syntax :SYSTem:COMMunicate:ETHernet:IPADdress?
Parameter None
Response ***.***.***.*** (*** is integer from 0 to 255)
Example The IP address is ”192.168.0.1”.
Transmission :SYST:COMM:ETH:IPAD?
Response →192.168.0.1
Command :SYSTem:COMMunicate:ETHernet:SMASk
Description Sets the subnet mask.
Syntax :SYSTem:COMMunicate:ETHernet:SMASk<wsp><value>
Parameter ***.***.***.*** (*** is integer from 0 to 255)
Response None
Example Sets the subnet mask to “255.255.255.0”.
Transmission :SYST:COMM:ETH:SMAS 255.255.255.0
Command :SYSTem:COMMunicate:ETHernet:SMASk?
96 / 113

Tunable Semiconductor Laser TSL-570
Description Reads out the subnet mask.
Syntax :SYSTem:COMMunicate:ETHernet:SMASk?
Parameter None
Response ***.***.***.*** (*** is integer from 0 to 255)
Example The subnet mask is “255.255.255.0”.
Transmission :SYST:COMM:ETH:SMAS?
Response →255.255.255.0
Command :SYSTem:COMMunicate:ETHernet:DGATeway
Description Sets the default gateway.
Syntax :SYSTem:COMMunicate:ETHernet:DGATeway
<wsp><value>
Parameter ***.***.***.*** (*** is integer from 0 to 255)
Response None
Example Sets the default gateway to “192.168.0.254”.
Transmission :SYST:COMM:ETH:DGAT 192.168.0.254
Command :SYSTem:COMMunicate:ETHernet:DGATeway?
Description Reads out the default gateway.
Syntax :SYSTem:COMMunicate:ETHernet:DGATeway?
Parameter None
Response ***.***.***.*** (*** is integer from 0 to 255)
Example The default gateway is “192.168.0.254”.
Transmission :SYST:COMM:ETH:DGAT?
Response →192.168.0.254
Command :SYSTem:COMMunicate:ETHernet:PORT
Description Sets the port number.
Syntax :SYSTem:COMMunicate:ETHernet:PORT<wsp><value>
Parameter Integer from 0 to 65535
Response None
Example Sets the port number to “64000”.
Transmission :SYST:COMM:ETH:PORT 64000
Command :SYSTem:COMMunicate:ETHernet:PORT?
Description Reads out the port number.
Syntax :SYSTem:COMMunicate:ETHernet:PORT?
Parameter None
Response Integer from 0 to 65535
Example The port number is “64000”.
97 / 113

TSL-570 OPERATION MANUAL
Transmission :SYST:COMM:ETH:PORT?
Response Legacy →64000
SCPI →+64000
Command :SYSTem:COMMunicate:CODe
Description Sets the command set.
Syntax :SYSTem:COMMunicate:CODe<wsp><value>
Parameter 0: Legacy
1: SCPI
Response None
Example Sets the command set to “SCPI”.
Transmission :SYST:COMM:COD 1
Command :SYSTem:COMMunicate:CODe?
Description Reads out the current set.
Syntax :SYSTem:COMMunicate:CODe?
Parameter None
Response 0: Legacy
1: SCPI
Example The command set is “SCPI”.
Transmission :SYST:COMM:COD?
Response Legacy →1
SCPI →+1
Command :SYSTem:LOCK?
Description Reads out the status of external interlock.
Syntax :SYSTem:LOCK?
Parameter None
Response 0: Unlocked
1: External inter locked
Example The external interlock is locked.
Transmission :SYST:LOCK?
Response Legacy →1
SCPI →+1
Command :DISPlay:BRIGhtness
Description Sets brightness of the display.
Syntax :DISPlay:BRIGhtness<wsp><value>
Parameter 0 to 100
Unit: %
98 / 113

Tunable Semiconductor Laser TSL-570
Response None
Example Sets brightness of the display to 50%.
Transmission :DISP:BRIG 50
Command :DISPlay:BRIGhtness?
Description Reads out brightness of the display.
Syntax :DISPlay:BRIGhtness?
Parameter None
Response 0 to 100
Unit: %
Example Brightness of the display is 50%.
Transmission :DISP:BRIG?
Response Legacy →50
SCPI →+50
Command :SPECial:SHUTdown
Description Shuts down the device.
Syntax :SPECial:SHUTdown
Parameter None
Response None
Example Shuts down the device.
Transmission :SPEC:SHUT
Command :SPECial:REBoot
Description Restarts the device.
Syntax :SPECial:REBoot
Parameter None
Response None
Example Restarts the device.
Transmission :SPECial:REBoot
Command :SYSTem:ALERt?
Description Reads out the current alert information.
Syntax :SYSTem:ALERt?
Parameter None
Response Error Number (Refer to “7-4 6. System Alert”)
Example Error numbers and error messages are returned.
Transmission :SYST:ALER?
Command :SYSTem:VERSion?
99 / 113

TSL-570 OPERATION MANUAL
Description Reads out the frimware version
Syntax :SYSTem:VERSion?
Parameter None
Response ****.****.****
4 digits + .(period) + 4 digits + .(period) + 4 digits.
Example The firmware version is 0012.0010.0005.
Transmission :SYSTem:VERSion?
Response '→0012.0010.0005
Command :SYSTem:CODe?
Description Reads out the product code
Syntax :SYSTem:CODe?
Parameter None
Response *-******-*-*-**-**-*
1 digit + “-“ + 6 digits (integer) + “-“ + 1 digit + “-“ + 1 digit
+ “-“ + 2 digits (integer) + “-“ + 1 digit (integer)
Example The product code is C-480640-P-F-AP-00-1.
Transmission :SYSTem:CODe?
Response →C-480640-P-F-AP-00-1
7.4.5. Command error
Errors issued are stored as error messages in the error queue and can be read
out with the ”:SYSTem:ERRor?” command. The list is as shown below.
Command error list
Code Error message
0 No error
-102 Syntax error
-103 Invalid separator
-108 Parameter not allowed
-109 Missing parameter
-113 Undefined header
-148 Character data not allowed
-200 Execution error
-222 Data out of range
-410 Query INTERRUPTED
7.4.6. System alert
Alert issued are stored as alert messages in the alert queue and can be read out
100 / 113

Tunable Semiconductor Laser TSL-570
with the ” :SYSTem:ALERt?” command. The list is as shown below.
System alert list
Code Alert condition
No00. Power supply Error1
No02. Power supply Error2
No03. Power supply Error3
No04 Power setting error (Unconfigurable power)
No05. Wavelength Error
No06. Attenuator Error
No07. Inter lock detection
No20. Temperature control Error1
No21. Temperature control Error2
No22. Temperature control Error3
No23. Temperature control Error4
No24. Sensor Error1
No25. Shutter Error
No26. Sensor Error2
No27. Connection Error
No30. Exhaust Fan Error
101 / 113

TSL-570 OPERATION MANUAL
8. Specifications
8.1. Specifications
Table 1: Model number 260360, 355485, 500630 and 560680 specifications
Table 2: Model number 240380, 355505 and 480640 specifications
102 / 113

Tunable Semiconductor Laser TSL-570
Table 3: General specifications
8.2. Regulations conformity
This product conforms the following standards.
● EMC:
EN 61326-1:2013
EN55011:2009 + A1:2010 (Class A, Group 1)
EN61000-4-2:2009
EN61000-4-3:2006 + A1:2008 + A2:2010
EN61000-4-4:2012
EN61000-4-5:2014 + A1:2017
EN61000-4-6:2014
EN61000-4-8:2010
EN61000-4-11:2004 + A1:2017
FCC 47 CFR Part15 Subpart B Class A (ANSI C63.4:2014)
ICES-003 Issue 7(October 2020) Class A
ICES-003 Issue 6 Class A (ANZI C63.4:2014)
● Safety:
IEC 61010-1: 2010 +
AMD1:2016 IEC 60825-1: 2014(3rd Edition)
● RoHS:
EN IEC 63000:2018
103 / 113

TSL-570 OPERATION MANUAL
9. Maintenance
9.1 Daily Maintenance
Turn off the power and pull out the power cord before cleaning, and use a soft
dry cloth to gently dust the instrument. Do not use chemicals (acetone, alcohol,
cleaning fluid, etc.), as they may cause damage to the coating. Do not
vigorously rub the display, as damage may result.
9.2 Cleaning the Optical Power Sensor
Connection of the optical fiber with dust and dirt on the end of the optical
connector of the TSL-570 cause loss of optical output, therefore, clean the
connector periodically.
■ Procedure
1. Loosen the 2 screws of the optical adapter and pull out the optical adapter
straight toward you.
2. Clean the end of the optical connector with alcohol immersed in cotton pad.
3. After cleaning, reinsert the optical adapter and tighten the screws again.
NOTE
If the optical adapter is not attached correctly, optical output power loss will
result.
9.3 Replacing Fuses
Fuses are in the fuse box above the power inlet on the rear panel. Use two
surge resistant type fuses. T3.15AL/250V (100 – 120V/ 200- 240V). Pull out
the fuse box, and replace with new fuses. Replace both of them with new ones.
104 / 113

Tunable Semiconductor Laser TSL-570
9.4 Inspection and Calibration
The TSL-570 is warranted for a period of two year. Inspection and calibration
on a regular basis (once every 24 months) are recommended. Please contact
our Sales Department concerning requests for instrument inspection/calibration
or consultation on other matters.
9.5. Self-Inspection
This is a simple inspection function that is executed by the device itself. The self-
inspection function checks each functional characteristic of the device.
It has a function to add an offset amount to the device. If there is a difference
between the set and measured wavelengths by another instruments (a
wavelength meter, optical spectrum analyzer, etc.), the output wavelength can
be calibrated.
■ Procedure
1. Touch Other to move to the Maintenance screen.
2. Select Execute at the Self-Test.
3. Press START in the confirmation screen.
4. The Self-Inspection will be completed in about 1 minute and the result will
be displayed.
105 / 113

TSL-570 OPERATION MANUAL
If there is any abnormality, please contact Santec. Contact information is
provided on the last page of this document.
Message Details and how to deal with faults
No faults have been detected. Instrument is operating normally.
A wavelength lock error has been There may be a problem with the wavelength monitor
detected. and the accuracy of the wavelength may have
deteriorated. Restart the product. If the error still
occurs, please stop using the product and contact
santec.
A decrease in output power was There may be a problem with the laser source and the
detected. output power may be low. Restart the product. If the
error still occurs, please stop using the product and
contact santec.
A fault has been detected with the There may be a problem with the internal attenuator.
attenuation control. Restart the product. If the error still occurs, please
stop using the product and contact santec.
A fault has been detected with the There may be a problem with the fine-tuning function
fine tuning control. and the wavelength accuracy may have deteriorated.
Restart the product. If the error still occurs, please stop
using the product and contact santec.
A fault has been detected with the There may be a problem with the optical system.
light source. Please stop using the product and contact santec.
A fault has been detected with the There may be a problem with the wavelength monitor.
wavelength monitor. Please stop using the product and contact santec.
A fault has been detected with the There may be a problem with the power monitor.
power monitor. Please stop using the product and contact santec.
TSL-570 encountered an error There may be a problem with tunable mechanism for
while setting wavelength. wavelength. Restart the product. If the error still
Please restart TSL-570. occurs, please stop using the product and contact
santec.
The self-test procedure has failed. There may be a problem with internal memory data.
Restart the product. If the error still occurs, please stop
using the product and contact santec.
9.6. Firmware update
The firmware can be updated using the USB (Host) port on the front of the
instrument. Please contact Santec to obtain the latest firmware update.
106 / 113

Tunable Semiconductor Laser TSL-570
The power must not be interrupted during firmware update. Please ensure a
stable power supply. If the power is interrupted during the firmware update
procedure it may not be possible to restart the instrument.
■ Procedure
1. Copy the firmware data files to a USB flash drive. (Firmup.txt,
COMupdate.tar.g2, SBC.tar.g2)
2. Insert the USB flash drive into the USB (HOST) port on the front panel.
3. Touch Other -> Firmware upgrade, the firmware update screen will be
displayed. Read the caution notice and press START.
107 / 113

TSL-570 OPERATION MANUAL
4. Since the confirmation screen appears, press START in order to update the
firmware.
5. The update will be completed in about 1 minute, and it will restart
automatically. Or, if the following message appears, follow the instructions
on the screen to manually turn off the power, unplug the power cord, and
then restart it.
Do not turn off the power while updating the firmware. Please ensure the
power cable is firmly inserted into its socket before starting the update
procedure and be careful not to disconnect the cable during the update. If
the power is interrupted during the update the instrument may not restart.
9.7. Long-term Storage
■ Procedure
1. Make sure the power is shut down completely. (Refer to 5-7 Turning off the
unit)
2. Wipe off dust, fingerprints, dirt, stains, etc., from the instrument.
3. Avoid storing the instrument in the following types of places.
108 / 113

Tunable Semiconductor Laser TSL-570
• Locations that receive direct sunlight
• Locations subject to high temperature or high humidity
• Locations where there’s a large amount of dirt, dust, salt content, or corrosive
gas
• Locations subject to vibration
• Locations where the instrument can be affected by noise from an electric or
magnetic field,
Damage of the device may be caused by the vibration under transportation
if the power supply is not shut down properly. Make sure the power is shut
down completely. (Refer to 5-8)
Since this instrument is precision measuring equipment, please avoid
vibration as much as possible, and maintain the storage conditions
previously specified.
109 / 113

TSL-570 OPERATION MANUAL
10. Re-packing and shipping
Special attention for re-packing and shipping is required when you ship the
instrument for repair or to a remote location.
10.1. Re-packing
Please make sure that the original shipping box is used during the shipment,
according to the following instructions. If the original shipping box is misplaced
or damaged, please contact our customer service department. We can arrange
for the shipping box to be sent to you.
Alternately, when the original shipping box is not available, send the instrument
with a sturdy, robust shipping box and at least 10cm packing material between
the instrument and the shipping box. The entire 10cm space on every side of
the instrument should be filled with a cushioning material.
The packing materials we used are designed to protect the instrument from
the shock or vibration during the shipment. If the instrument is shipped
without packing materials or improperly packed, the instrument might be
damaged. Any instrument damage that occurred when the instrument
shipped without the original shipping box or without proper packing will not
be applicable for warranty repair, even during the guaranteed term.
Damage of the device may be caused by the vibration under transportation
if the power supply is not shut down properly. Make sure the power is shut
down completely. (Refer to 5-7)
10.2. Packing Instruction
1. Set the cushions to the product as Figure 1. There are two types of
cushions. One is printed as “FRONT” and the other is printed as “REAR”.
110 / 113

Tunable Semiconductor Laser TSL-570
Figure 1
2. Put the product with two cushions in the shipping box.
3. Secure the box by shipping tape or band after closing the box.
10.3. Shipping
Treat the box carefully, and avoid shock or vibration as much as possible.
Maintain the box in an upright position and label “THIS SIDE UP” as much as
possible.
111 / 113

TSL-570 OPERATION MANUAL
11.  Troubleshooting

| Fault condition  | Cause  | Action  |
| ---------------- | ------ | ------- |
No power  Cord is unconnected.  Connect power cord properly.
|     | No fuse or fuse is blown out  | Open the fuse box lid and replace  |
| --- | ----------------------------- | ---------------------------------- |
fuse.(Refer to “9-3 Replacing Fuses”)
|     | Power cord is broken or not  | Use proper power cord. (Refer to “4- |
| --- | ---------------------------- | ------------------------------------ |
|     | correct.                     | 2 Power Supply”)                     |
The unit is not turn off.  Some electrical faults occur.  Press power ON/OFF key for at least
10 seconds. If it did not turn off,
unplug the power cord.
No light output  Optical output is not active.  Press ACTIVE key and make sure
LED is lit.
|     | External interlock circuit is open.  | Close the circuit or put short circuit  |
| --- | ------------------------------------ | --------------------------------------- |
cap on the interlock connecter.
|     | The end of the optical output  | Clean the end face of the optical    |
| --- | ------------------------------ | ------------------------------------ |
|     | connector is dirty.            | connector. (Refer to "9-2. Cleaning  |
the Optical Power Sensor")
|     | Optical connector is lost.  | Put the connector properly.  |
| --- | --------------------------- | ---------------------------- |
Connected optical cable is broken. Replace to an adequate cable.
”SysAlert” and “TempErr” The ambient temperature may  To ensure exhaust heat inside the
is displayed.  have exceeded the operating  product, leave space near the vent
|     | temperature range.  | so as not to block the flow of air.  |
| --- | ------------------- | ------------------------------------ |
Also note the environmental
temperature during operation.
If after checking the above list, and the device is still not operating correctly,
please contact us.

In the event of any trouble with this product, turn the unit off in accordance
with the procedures to shut off the power described in this operation manual,
disconnect the power source cord, record the product name and serial number
described on the name plate of the product, and then contact our dealer at
your place or directly contact us at Santec Photonics Laboratories. Our
telephone number and facsimile number are shown below. However, we are
not responsible for any trouble arising from your own repair or modification on
this product. In addition, if the Void sticker on the main body is peeled off and
there is evidence that the product has been opened, not only is the product
warranty not applicable, it may not be covered by maintenance support.
 112 / 113

Tunable Semiconductor Laser TSL-570
5823 Ohkusa-Nenjozaka, Komaki, Aichi 485-0802, Japan.
Santec Japan Corporation
Tel: +81-568-79-3536
Fax: +81-568-79-1718
400 Kelby Street Suite 1501, Fort Lee, NJ 07024, USA
Santec USA Corporation
Toll Free: +1-800-726-8321 (santec-1)
Tel: +1-201-488-5505
Fax: +1-201-488-7702
99 Park Drive, Milton Park, Abingdon Oxfordshire, OX14 4RY, UK
Santec Europe Ltd.
Tel: +44-20-3176-1550
21F Room H, Hua Du Bldg., No.838 Zhangyang Road, Pudong, Shanghai 200122 China
Santec (Shanghai) Corporation, Ltd.
Tel: +86-21-58361261,
+86-21-58361262
Fax: +86-21-58361263
www.santec.com
TSL-570-M-E-Ver.1.5 CODE-202307-HK-KT-CPY/ Santec Corporation/Tech.&Design sec.
113 / 113