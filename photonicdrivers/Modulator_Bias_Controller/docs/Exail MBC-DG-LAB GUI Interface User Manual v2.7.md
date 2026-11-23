MBC DG GUI
MBC INTERFACE
User Manual
Version 2.7
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57
25000 Besançon, France www.photonics.ixblue.com

Table des matières
Interface - Introduction..................................................................................................................... 3
Interface - Setup ................................................................................................................................ 3
Minimum Computer Requirements..................................................................................................... 3
Software installation ....................................................................................................................... 3
Hardware Setup .............................................................................................................................. 3
Interface - Operation ......................................................................................................................... 4
General considerations ........................................................................................................................ 4
Setting bias control parameters .......................................................................................................... 6
Saving and loading bias control parameters ........................................................................................ 8
Bias monitoring ................................................................................................................................... 9
Bias data recording ............................................................................................................................ 10
Manual mode .................................................................................................................................... 12
Diagnostic .......................................................................................................................................... 13
ANNEXE: ............................................................................................................................................ 15
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57
25000 Besançon, France www.photonics.ixblue.com

Interface - Introduction
exail proposes a graphical user interface to simplify bias control management for the ModBox
and MBC products family. Based on a RS232 serial communication and a Visual Basic®
interface, bias parameters are strictly similar also whole bias control are tunable and could be
saved and loaded.
Interface - Setup
Minimum Computer Requirements
• Processor 1 GHz with 512MB RAM
• Disk space (minimum) 32-bit : 600 MB 64-bit: 1.5 GB
• Windows XP Professional SP3
• One USB port for each MBC to drive.
Software installation
1/ Log on with an administrator account.
2/ Plug the USB key.
3/ Install setup.exe (system restart maybe required)
4/ Install USB MBC Drivers (if needed)
5/ Run MBC DG Control.exe file
Hardware Setup
1. Connect USB cable to the controller rear panel and the PC
2. Plug the power cable and switch on the device.
3. USB MBC connexion will be seen as COM peripheral by your PC
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57
25000 Besançon, France www.photonics.ixblue.com

Interface - Operation
General considerations
One needs to choose the COM port. To proceed, click on the down arrow of the list box and
select the COM port connected to the controller.
After selecting your port, click on “Connect” to obtain your S/N number and activate the rest
of the interface.
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57
25000 Besançon, France www.photonics.ixblue.com

Once done, the MBC serial number will be displayed.

     exail
| Photonic Solutions Business Unit  | T. : +33 3 81 85 31 80  |     |
| --------------------------------- | ----------------------- | --- |
| 3, rue Sophie Germain, TEMIS      | F. : +33 3 81 85 15 57  |     |

| 25000 Besançon, France  | www.photonics.ixblue.com  |     |
| ----------------------- | ------------------------- | --- |

Setting bias control parameters
• Standard Mode:
Figure 1: Bias control standard parameters
Auto-Calibration button: A scan of the system is performed in order to find the right MBC
parameters for the 3 most used setting points: QUAD, MIN, MAX. (see Annexe for details)
Scan Restart button: The bias control routine is reinitialised. This is recommended to restart
the feedback control when some parameters have been changed (Dither amplitude, Dither
frequency, Photodiode gain).
Refresh Screen button: Application reloads all parameters from the board.
Save Config button: Current configuration is saved in one of the 3 configuration area. (Config
1-3).
Load Config button: Selected configuration is loaded into MBC (Config 1-3).
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57
25000 Besançon, France www.photonics.ixblue.com

• Advanced Mode:
Figure 2: Bias control advanced parameters
Running Mode : Auto / Manual
DC Bias Voltage : From –10 to +10V (variable step)
Transfer Level : From –100% to +100% (0.1% step)
Dither Frequency : From 400 to 1400Hz (40Hz step)
Dither Amplitude : From 10 to 1000mV (typically 10mV step)
Photodiode Polarity : Inverted or Non Inverted (Non Inv.)
Photodiode Gain : From 1 (Low) to 127 (High)
After setting a value, it has to be validated with “Send” button.
The validation is effective only when “Send” button restore its initial colour.
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57
25000 Besançon, France www.photonics.ixblue.com

Saving and loading bias control parameters
Figure 3 : bias control parameters save and load buttons
Save : All bias control parameters are saved in a file for further loading. The user specifies the
file name and its path through a dialog box.
Load button : All bias control parameters are loaded from a file specified by the user in a
dialog box.
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57
25000 Besançon, France www.photonics.ixblue.com

Bias monitoring

Figure 4: bias monitoring control

DC bias is always monitored, you can clear or save the graph.

|     |     |     |
| --- | --- | --- |
     exail
| Photonic Solutions Business Unit  | T. : +33 3 81 85 31 80  |     |
| --------------------------------- | ----------------------- | --- |
| 3, rue Sophie Germain, TEMIS      | F. : +33 3 81 85 15 57  |     |

| 25000 Besançon, France  | www.photonics.ixblue.com  |     |
| ----------------------- | ------------------------- | --- |

Bias data recording
The Records function allows saving a measure with a specific step time. It saves in a text file,
time and DC bias value.
Figure 5 : start recording bias values
The “Record” button starts the bias recording procedure.
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57
25000 Besançon, France www.photonics.ixblue.com

First step:
Set the time interval between each record with “Step Time” and the record duration with
“Total Time” in hour. “Total time” at 0 means recording until “Stop” button is pressed.
Second step:
Press “Records” button and a dialog box appear to set the file name and destination folder.
Third step:
Press “Save” button in the dialog box to launch record procedure.
Figure 6 : stop recording bias values
At any time it is possible to stop the record procedure by clicking on the “Stop” button (See
Figure 6).
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57
25000 Besançon, France www.photonics.ixblue.com

Manual mode
figure 7 :bias control in manual mode
In Manual Mode, the Bias control works as a DC voltage source. The applied bias is adjusted
by decreasing / increasing the “DC Bias Voltage” (See Figure 7). It is also possible to change
the step.
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57
25000 Besançon, France www.photonics.ixblue.com

Diagnostic:
Diagnostic is a function which is used by our support team. It will help us understand and see
what can be your feedback loop problem. Click on Diagnostic and enter the Password:
“trepxe”.
figure 8 :bias control in manual mode
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57
25000 Besançon, France www.photonics.ixblue.com

You obtain a new tab:
figure 9 :bias control in manual mode
Click on tab diagnostic and send an email to us with the diagnostic file.
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57
25000 Besançon, France www.photonics.ixblue.com

ANNEXE:

Auto calibration step:

| Step  | Quad                         |     | Min / Max                    |
| ----- | ---------------------------- | --- | ---------------------------- |
| 1     | Apply a dither of 120mV      |     | Apply a dither of 120mV      |
| 2     | Do a scan to detect DC Vπ    |     | Do a scan to detect DC Vπ    |
| 3     | Dither is set to 3% of Vπ    |     | Dither is set to 3% of Vπ    |
| 4     | Set modulator to Quad point  |     | Set modulator to Quad point  |
5  Increase  Photodiode  Gain  until  Increase  Photodiode  Gain  until
obtaining a value of 2Vpp on our ADC.  obtaining a value of 2Vpp on our ADC
Photodiode Gain is limited to 120  Photodiode Gain is limited to 120
| 6   | Do a Scan                      |     | Set the dither to 0.25% of Vπ        |
| --- | ------------------------------ | --- | ------------------------------------ |
| 7   | Board is locked to Quad Point  |     | Do a Scan                            |
| 8   |                                |     | Board is locked to Min or Max Point  |

If the feedback loops oscillate, you can reduce the Photodiode Gain in order to stabilize the
loop (reducing from 5 to 20 is generally enough).

     exail
| Photonic Solutions Business Unit  |     | T. : +33 3 81 85 31 80  |     |
| --------------------------------- | --- | ----------------------- | --- |
| 3, rue Sophie Germain, TEMIS      |     | F. : +33 3 81 85 15 57  |     |

| 25000 Besançon, France  |     | www.photonics.ixblue.com  |     |
| ----------------------- | --- | ------------------------- | --- |