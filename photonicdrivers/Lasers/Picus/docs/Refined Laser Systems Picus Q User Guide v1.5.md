User Guide
Picus Series
VERSION 1.5
FEBRUARY 2024

Picus Series User guide
If you encounter issues not addressed by this user guide, please contact
us for additional support.
ii

Picus Series  User guide

Document Revisions
Version
Date  Document Changes
Number
| 05.01.2022  | 1.0  | First Release    |
| ----------- | ---- | ---------------- |
| 02.04.2022  | 1.1  | Revisions        |
| 08.07.2022  | 1.2  | Revisions        |
| 10.08.2023  | 1.3  | Minor revisions  |
05.10.2023  1.4  Revise chapter Operation and Remote Control to support version 4.0
| 13.02.2024  | 1.5  | Include Picus Q Filter and Idler options  |
| ----------- | ---- | ----------------------------------------- |
|             |      |                                           |
|             |      |                                           |
|             |      |                                           |

iii

Picus Series User guide
Contents
Contents ------------------------------------------------------------------------------------------------------------- iv
1. Introduction---------------------------------------------------------------------------------------------------- 1
Scope and Purpose 1
2. All-fiber Picosecond OPO PicusQ --------------------------------------------------------------------------- 2
Typical Specifications 2
Output Characteristics 3
Outline Drawings 4
3. Laser Safety & Compliance ---------------------------------------------------------------------------------- 5
Safety Labels 6
Warnings including Hazards and Injury Prevention 7
Specific Safety Aspects 9
4. Controls & Indicators --------------------------------------------------------------------------------------- 12
Electronics Supply Unit (SU) 12
5. Installation --------------------------------------------------------------------------------------------------- 14
6. Operation ----------------------------------------------------------------------------------------------------- 15
Start Up Procedure 15
Shutdown Procedure 16
7. Maintenance & Diagnostic --------------------------------------------------------------------------------- 17
8. Remote Control --------------------------------------------------------------------------------------------- 18
USB Connection 18
RS232 Connection 18
GUI Operation 19
Laser Commands 24
Measurement Commands 25
Monitoring Commands 25
Error Codes 26
9. Sample Control Scripts ------------------------------------------------------------------------------------ 27
MATLAB 27
Python 28
iv

Picus Series User guide
1. Introduction
Scope and Purpose
This Manual is to be used with Refined Laser Systems’ PICUS series All-fiber Picosecond OPO. The laser
is a class 4 laser system and must only be operated by laser experts using proper laser safety measures.
It is the user’s obligation to verify the compliance of the laser with the local requirements.
Never operate the laser until you have thoroughly read the manual, especially the chapters about laser
safety, handling, and regulatory information. A class 4 laser is dangerous and has the potential to cause
damage and injury. Considering this, ensure that you take all precautions possible.
1

2.
Picus DUO OEM User guide
2. All-fiber Picosecond OPO PicusQ
Refined Laser Systems’ All-fiber Picosecond OPO represents a class 4 laser source that can generate
ultra-short pulses over a bandwidth of 770 to 980 nm. The system comprises two main elements: a
power supply and a laser head. The laser head includes an integrated pump laser and a fiber-based
optical parametric oscillator.
Refined Laser Systems’ All-fiber Picosecond OPO offers one main laser output, providing signal pulses
from the parametric oscillator, tunable between 770 and 980 nm.
Typical Specifications
The following table provides the typical specifications of the All-fiber Picosecond OPO.
Optical Main Output
Tuning Range 770 – 980 nm
Average Power >100 mW
Tuning Speed <1 s (full range)
Pulse Duration <15 ps
Spectral Bandwidth <1.2 nm
Repetition Frequency 80 MHz
RMS Noise <1 %
Polarization PER >17 dB, aligned to slow axis
Electrical
Communication through USB of RS232
Interfaces
Sync. Out for external synchronization
Software Interfaces GUI and custom serial API (e.g., Python or Matlab)
Power Supply 110 VAC or 230 VAC
Mechanical
Laser Head Dimension 44x49x13 cm³
Supply Unit Dimension 44x45x15 cm³
Cooling Air-cooled
Weight <40 kg
Umbilical Length 2 m
2

Picus Series User guide
Output Characteristics
The output is formed by the end facet of an optical patch cable (NKT PM-LMA15, others on request).
The fiber is terminated by an FC/APC fiber connector, without any output coupling optics. The values
given below, are an estimate considering the mode field diameter of the fiber. The full angle beam
divergence Θ is calculated by
4∗𝜆
𝜃 =
2∗𝜋∗𝑤
0
with λ being the wavelength and w the beam diameter at the Gaussian beam waist, i.e., at the fiber
0
end-facet.
Main Output
Output beam diameter (fiber mode field diameter w ) 12.8 ± 1.5 µm
0
Divergence (full angle) 42.3 mrad (@850 nm)
Caution:
Do not turn on the laser without blocking the path of the laser beam emitted from the output. Refer to
section Laser Safety & Compliance for further details.
Warning:
Do not attach or detach the optical patch cable when the laser is running. This can damage the end
facets and lead to significant power and beam quality degradation!
3

Picus Series User guide
Outline Drawings
Figure 1: Outline drawing of the laser head (top and front view), Idler Output and Filter
Output optional.
4

Picus Series User guide
3. Laser Safety & Compliance
MUST READ: Never operate the laser until you have thoroughly read this document. A class 4 laser is
dangerous and has the potential to cause damage and injury. Considering this, ensure that you take all
precautions possible, including being fully familiar with and following all the safety recommendations
listed here.
Laser Classification
These lasers are classified as a Class 4 laser products as per the IEC/EN 60825-1:2014 laser safety
standard and complies with IEC 61010-1 Safety requirements for electrical equipment for
measurement, control, and laboratory use.
Intended Use
The lasers have been designed for general laboratory or industrial use and as such are not approved
nor tested for use in treatment or diagnostics of human or animals and does not comply with European,
US or rest of the World requirements for medical device lasers. Neither is the system appropriate for
outdoor use or use in extreme conditions such as elevated/lowered temperatures, particle/chemical
contaminated environment, or vacuum conditions.
Laser Safety Officer
The laser must be used by staff familiar with laser safety procedures and in facilities appropriate for
laser operation. Refined recommends appointing a Laser Safety Officer (LSO) in accordance with valid
local and national safety regulations. The LSO should ensure that every user of the system is familiar
with the safety aspects of the laser unit and that the laser’s operation documents should be clear and
present to operators of the laser. Furthermore, any other staff in proximity of the laser should be aware
of any risk in connection with usage of the unit.
5

Picus Series User guide
Safety Labels
N ote:
If any labels are missing, immediately notify Refined Laser Systems GmbH.
The All-fiber Picosecond OPO chassis includes multiple labels that indicate hazards and regulatory or
manufacturing information. The labels are located on the right side of the laser head as described in
the Table 1.
Table 1: Safety labels on chassis
Label Panel Description Picture
Classification Right Safety information stating
the laser emission hazards
and the laser’s class rating.
Manufacturing Right Manufacturing
information including
address, part and serial
number, date
manufactured and
regulatory compliance.
Laser Aperture / Front Safety information alert
Laser Warning indicating this area of the
laser is near a source of
dangerous laser emissions.
Product Right Safety information alert
Information indicating key emission
specifications.
Certification Right Safety compliance
information.
6

Picus Series User guide
Warnings including Hazards and Injury Prevention
General Warnings
This laser is a Class 4 laser product, and the operation room and operation conditions must comply
with CFR21 1040.10, Laser Notice LN56. If these regulations are not followed, you must operate the
laser in accordance with local regulations for a Class 4 laser source.
Using controls, adjusting, or altering the procedures other than those specified by the guides
associated with this laser may result in exposure to hazardous radiation and/or voltages.
This device emits two Class 4 collimated laser beams. Radiation warning labels are affixed at the
emitting apertures. To prevent injury, the beam path must be strictly controlled.
Using this equipment in a manner not specified by the manufacturer may impair the protection
capabilities of the equipment.
At all times the laser is on, it is advised that you have clear access to the shut-off controls of the laser.
Shut-off controls consist of the power supply front panel key switch, the remote interlock, or the
software control.
At all times during system operation, ensure that the beam path is known and controlled. Wear
wavelength specific eye and skin protection and ensure everyone in the laser area is aware that the
system is in operation. Ensure that remote interlock is in place.
The laser should only be operated by authorized users who are properly trained in the appropriate
safety aspects and of statutory minimum age. To prevent unauthorized and likely unsafe operation by
untrained personnel, remove the front panel key from the key switch when the laser is not in use. Store
the key in a secure location.
It is not recommended to operate the laser without an appropriate interlock connection to, e.g., a door
or other entry mechanism to the system enclosure. If you bypass this safety feature, Refined Laser
Systems bears no responsibility for any damage, loss or harm caused by accidental laser exposure.
Never make any modifications, additions, or conversions, which might affect safety. This also applies
to the installation and adjustment of safety devices. Should safety relevant modifications or
operational behavior changes occur with the laser, stop the laser device immediately and report the
malfunction to Refined Laser Systems GmbH.
7

Picus Series User guide
Damage Prevention
If the laser’s full or partial beam is obstructed or guided towards flammable materials, it can ignite a
fire. Flammable materials include paper, solvents, or other similar combustible material. Keep the
beam path free from any combustible material. In case of an internal failure a fire could also be ignited
within the laser housing. Keep a fire extinguisher nearby the laser operation area.
Avoid spilling fluid onto the laser chassis and accessories. If spillage occurs, remove it immediately
using absorbent material. Do not allow spilled fluid to enter the chassis. Avoid spilling fluid onto the
electrical system. Place the laser so that in the event of a spillage, the electrical sockets’ exposure is
minimized. To clean the chassis, disconnect the power source and use a soft and damp cloth. Do not
use solvents or similar cleaning agents on the chassis or any other parts of the laser.
If required, the laser should be stored in a dry and cool place (15-20°C). The optical output should be
protected using the mechanical shutter at the front panel of the chassis. Avoid exposing the unit to
vibrations or mechanical shock.
In the event of an emergency or accident, make sure to have a contingency plan prepared and readily
available including response actions and contact persons.
When disposing the laser, follow local waste regulations.
Precautions
Take the necessary precautions to ensure that the laser is used only when in a safe and reliable state.
In the event of malfunctions, disable the laser device immediately and unplug its electrical power. Have
any defects rectified immediately.
Before starting the laser, prepare a site-specific Risk Assessment to ensure no persons are at risk.
Inform operating personnel before beginning special operations and appoint a person to supervise the
activities. Ensure that the user operation area is adequately secured.
Protective Equipment:
• Laser Safety Officers are also responsible for the issuing and/or wearing of personal
protective equipment. Direct exposure of the eye to the invisible laser beams must be avoided.
At all times, proper eyewear must be worn and maintained according to Personal Protection
Equipment at Work regulations.
• Compulsory regulations also require the issuing and/or wearing of personal protective
equipment. The necessity of reading the laser’s documentation applies especially to persons
working only occasionally with the laser.
• Use protective equipment, wherever required by the circumstances or by law.
8

Picus Series User guide
Specific Safety Aspects
Within this classification, the laser is a class 4 (high power) laser and is a potential hazard to the human
operator. The class 4 laser beam is also classified as a potential fire hazard. Class 4 is the most powerful
(and potentially hazardous) category of lasers. Direct and scattered radiation from Class 4 products is
an acute hazard to eyes and skin. Precautions include eye and skin protection, remote interlocks, and
warning labels.
Physical Hazards
The laser beam is dangerous to the eyes and skin. The dangers include:
• Direct radiation as it leaves the laser.
• Radiation reflected from a surface.
• Diffused radiation originated from a scattered reflection.
Light
In case of exposure, the laser may provide laser radiation with power levels up to 500 milliwatts. The
laser’s emissions consist of a wide band of wavelengths from 750 to 1060 nm. Despite the non-ionizing
nature of the operating wavelengths, damage can still occur to living tissue as a result of heat produced
during radiation absorption or via multi-photon absorption. Suitable beam dumps must always be
used when the laser is operating.
In general, the maximum permissible radiation exposure for the skin is several times greater than for
the eye. Safety measures regarding the radiation hazard are therefore mainly focused on dangers for
the eye. Not only is the direct laser beam hazardous, but unchecked reflections of laser light also
constitute a potential hazard.
Risk of severe injury: Always wear wavelength specific laser safety glasses when there is a chance of
exposure to radiation from the laser. The filter in protective eyewear provides protection for only a
narrow band of wavelengths. Ensure you are wearing the appropriate protective eyewear for the laser
device in question. Check with your Laser Safety Officer or other safety personnel for guidance in
selecting the appropriate eyewear.
For protective eyewear, the American National Standards Institute (ANSI) standard for the safe use of
lasers requires that a set of protective eyewear blocking the appropriate laser wavelength should be
worn while operating or servicing class 4 lasers.
Clearly label safety eyewear with their optical density and their specified wavelength protection. To
avoid confusion, laser safety eyewear should be kept separate from any other safety eyewear and
personal protective equipment.
Using the wrong type of safety eyewear is dangerous. It can be more dangerous to have improper
eyewear and a false sense of security than to have no eyewear and take precautions based on the
absence of protection. Even if you are wearing protective eyewear, never look directly into the beam;
intense laser radiation can destroy the protective filter.
9

Picus Series User guide
Eye Protection
Potential eye burns: Only use the laser in accordance with its designated use. The following guidelines
describe some of the actions necessary to avoid injury caused by the laser beam. Always follow these
guidelines and take additional precautions if necessary.
• When eyewear is necessary, make sure it has the proper optical density for the laser
wavelength.
• All other personnel in the vicinity of the laser must wear protective eyewear.
• Permit only qualified personnel to operate the laser.
• Never look directly into any laser beam.
• Avoid indirect viewing of direct or reflected laser radiation. Specular and diffuse reflections
(from reflective surfaces) can be as dangerous as the direct laser beam. Never view the beam
directly through optical instruments.
• Take precautions to ensure that there are no reflecting objects in the path of the laser beam.
• Do not deviate from standard operating procedures when working with class 4 laser
equipment.
• Use lasers only in approved applications and locations. Take adequate precautions to prevent
unauthorized personnel from entering the area where a class 4 laser is operating. Do not use
lasers around untrained personnel. Ensure that all personnel in the area observe proper safety
precautions.
• Report all incidents of exposure to your supervisor.
• Clearly display warning signs indicating the laser enclosed area with an additional warning
light outside the door.
• Adhere to local and national regulations governing the safe use of lasers.
• Be aware that maintenance of eyewear includes, but not limited to, inspection, cleaning,
testing and training in use. Maintenance should only be performed by competent personnel.
Skin Protection
Potential skin burns: Direct and reflected laser radiation can burn exposed skin. Only use the laser in
accordance with its designated use. Safety interlocks are only to be overruled by authorized personnel.
• Although the skin can withstand considerably higher radiation intensity than the eyes, tissue
may be burned to a greater or lesser degree, depending on the radiation time and the
irradiation intensity.
• Avoid contact between the skin and the beam, or specular reflections of the beam. Reflections
of the beam may be as dangerous as the beam itself. Wear appropriate protective clothing to
protect the skin whenever necessary.
10

Picus Series User guide
Fire Protection
Fire hazards: Class 4 lasers are potential fire hazards. The laser beam can cause flammable materials
to ignite or explode. Always keep a fire extinguisher in the laser area in case a fire occurs.
Because of the high output power from the class 4 laser, a wide range of materials can be set on fire.
Therefore, take appropriate fire prevention measures when the beam path is open:
• Combustible materials may be ignited by the laser beam or by electrical components inside
the laser system. Flammable items must be isolated from the laser beam and from the laser
system.
• Paper (circuit diagrams, leaflets, or even posters on the wall), curtains that are not coated with
fire retardant, wooden panels or similar materials can be easily set on fire by direct or
reflected laser radiation.
• Use only beam stops made of non-flammable materials (not asbestos!).
• Many fluids and solvents (e.g., cleaning agents used for maintenance) are combustible. The
intense beam of the laser can ignite vapors from these materials. Prevent the laser beam from
contacting flammable materials used in the laser area.
• Move containers of flammable materials as far from the laser system as possible and shield
them from the beam with opaque materials. Never place these solutions and vapors in the
beam path or near the system.
Constructive Safety Features
The laser device is equipped with the following constructional safety features:
• Appropriate Class 4 label affixed to laser device enclosure (see section Labeling).
• All parts of the laser where laser radiation may possibly escape are marked with the
appropriate adhesive danger signs (according to IEC 60825).
• The laser has an emission indicator LED fitted that indicates laser energy is present or can be
accessed.
• The laser is equipped with a safety interlock system. In case of an emergency, the laser can be
fully switched off (no laser emission) by pulling the interlock line.
• The laser is equipped with a key switch that limits laser operation.
• The laser device can only be switched on with the key-switch in the ‘ON’ position. This
prevents inadvertent or unauthorized starting of the laser. The key needs to be cycled to the
OFF position after a power loss / shutdown. It cannot be operated with the key in the OFF
position and the key cannot be removed in the ON position.
11

Picus Series User guide
4. Controls & Indicators
Electronics Supply Unit (SU)
1. 2.
3. 4. 5. 6. 7.
Figure 2: Electronics supply unit (front).
1. Main Laser Keyswitch with LED indicator (labeled “0/1”) – Key stops all laser emission as a
master switch for emergency shutdown. Needs to be in off position or must be moved to off
position for a restart of the electronics supply unit. When the LED indicator is on, laser light
of Class 4 may be emitted- take necessary safety precautions.
2. Laser Enable Button with LED indicator (labeled “Laser enable”) – Button can be used to
start the laser emission instead of software commands (see chapter Operation for details).
LED indicates current status of the laser and acts as a redundant emission warning. If either
the Button or the Keyswitch LED are on or blinking, laser light of Class 4 can be emitted.
3. USB port for software control of the laser (labeled “USB” / see chapter )
4. RS232 port as an alternative method for software control (labeled “RS232”)
5. Trigger input BNC connector (labeled “Trigger In”) – for rapid wavelength switching from
pre-programmed table.
6. Interlock BNC connector for connecting a remote interlock. To enable laser operation the
connection must be shorted to close the interlock. If the interlock is opened/kept floating or
actively pulled high (>3V) all laser operation is disabled. After closing the interlock connection
again, the main laser Keyswitch must be cycled to off and on position before the laser can be
turned on again.
7. Sync Out – SMA port providing a signal synchronized to the fundamental repetition frequency
of the system (80 MHz).
8. (Optional) Mod Out – SMA port providing the synchronized modulation frequency (20, 10 or
6 MHz).
12

Picus Series User guide
4. 1.
2.
3.
Figure 3: Electronics supply unit (back).
1. Mains Power Switch.
2. Mains Fuse.
3. Mains power plug.
4. USB port for debugging and firmware updates.
13

Picus Series User guide
5. Installation
Before installing the laser, take necessary safety precautions listed in chapter 3, “Laser Safety &
Compliance”. The laser head ships assembled to the supply unit. No user accessible parts or alignments
are inside either unit. The power supply is air cooled and rack mountable and requires at least 6 in.
(15 cm) of clearance at the rear and on top for proper cooling. Keep the shipping containers. If you file
a damage claim, you may need the containers to demonstrate that the damage occurred as a result of
shipping. If you need to return the system for service at a later date, the specially designed containers
assure adequate protection.
Caution:
If the laser system is shipped during extreme weather conditions, i.e., heat or freezing temperatures,
leave the laser system in its shipping container, put it in environmental conditions similar to where it
should be operated, and let it acclimate to room temperature.
The following steps are required to set up the laser system:
• Fix the laser head to your optical table using the provided clamps. Make sure that the
shutter is closed or that suitable beam dumps are installed.
• Connect the Laser Control USB Port or Laser Control RS232 Port with your computer. For
details about computer control see chapter 1.
• Optional: connect the Laser Sync Out (for external use) on the laser head with external
hardware of choice.
• Optional: connect the modulation out signal (Trigger out of the pulse picker/AOM) on the
laser head with external hardware of choice.
• Connect the power supply cable to the electronics supply unit.
Caution:
Beware of high-power laser output – provide proper laser safety gear according to the specified output
powers and pulse durations!
14

Picus Series User guide
6. Operation
Read chapter 3, “Laser Safety & Compliance,” before turning on the system. There are no controls to
adjust or optics to change inside the laser head. The laser head should never be opened.
Start Up Procedure
1. Check that the Laser Keyswitch is in the off position.
2. Turn on the supply unit via Mains Switch on the back.
3. Wait at least 30 s while the system initializes (key-switch and button LED blinking) and allow
the temperature controllers (TEC) in the supply unit to reach a stable state (otherwise an
enable command will be answered with a “TEC error”).
Turn Laser Keyswitch to on position. If it has been in on position during power-on, a cycling to off-
and back to on position is necessary.
To ensure that the beam is safely captured, install a beam block or power meter in front of any laser
output ports. Beware of high-power laser output – wear proper laser safety gear and
remove flammable objects from beam path!
Use the GUI (see chapter 1) or send Laser:Enable 1 to enable the laser system remotely.
Optional: Alternatively, press the Enable Button once to enable and start oscillator & pre-
amplifier (Ready mode). The Keyswitch LED should light up and the button LED is blinking.
Turn on main amplifiers (Running mode) by pressing the Enable Button a second time. LED
Keyswitch will stay on, and LED Button will blink rapidly and emit continuously after the
transition. The outputs will start emitting at full power.
If no Laser:Wavenumber or Laser:Wavelength command has been sent since power-on of
the supply unit, the laser starts with the settings used before last regular shutdown.
Recommendation: To reduce power and wavelength drifts to a minimum, use the Picus Wavelength
Lock with the internal calibration during the warm-up period.
15

Picus Series User guide
Shutdown Procedure
In case of emergency, laser operation can be immediately stopped by turning the Main Laser Enable
Keyswitch or by opening the remote interlock connection/actively pulling the input of remote
interlock to HIGH (>3V).
For normal shutdown, follow the following procedure:
1. Shutdown, either:
a. Remote shutdown by sending Laser:Enable 0.
b. GUI shutdown (please refer to section 1).
c. Shutdown using Button:
i. Make sure the Laser is in regular running mode (Button LED is lit
continuously)
ii. Press Button once
2. Verify that both Keyswitch & Button LEDs are off.
3. Turn main laser Keyswitch to off position.
4. Optional: Shutdown power supply unit by Mains Switch on the back panel.
Caution - Use of controls, adjustments, or performance of procedures other than those
specified herein may result in hazardous radiation exposure.
16

Picus Series User guide
7. Maintenance & Diagnostic
The provided laser system is a robust all-fiber light source. No regular user maintenance or alignment
is required or necessary. Currently, no scheduled service maintenance is required as well. If laser
operates outside of specified parameters, contact Refined Laser Systems GmbH.
17

8.
Picus Series User guide
8. Remote Control
USB Connection
Connect the Laser Control USB Port with your computer.
The laser will be installed as a USB communications device class (or USB CDC class) in Windows 10
or Linux based OS (ttyACM*) automatically and acts as a virtual COM port.
Check the COM port number that was assigned, e.g., using the device manager in Windows.
Figure 4: Screenshot of the USB connections in Windows.
Connect to the COM port using your preferred method (Python, MATLAB, Termite…).
Baud rate, parity etc. can be used as is (communication is USB based and independent of the
chosen values).
Set read/write termination character to newline \n.
Each set command is answered by the laser with an ACK\n.
RS232 Connection
Connect the Laser Control RS232 Port with a serial port on your computer.
Open the COM port with the following settings:
• Baud rate: 115.200 Bits / s
• Data bits: 8
• Parity: none
• Stop bits: 1
Set read/write termination character to newline \n.
Each set command is answered by the laser with an ACK\n. This reply needs to be read after every
write command, to empty the buffer and avoid a buildup of data.
18

Picus Series User guide
GUI Operation
The Refined Laser Systems’ Graphical User Interface (RLS-GUI) is provided with the Laser system in
form of a simple executable (“RLS_Control_vX.Y.exe”). Set up the laser according to chapter 5
“Installation” and start the executable. shows a screenshot of the connection dialog appearing when
starting the RLS-GUI. Choose the correct COM port (see section ) and click connect. If the laser is
connected via RS232, set the baudrate to 115200 before connecting. Check the checkbox to
automatically connect to the laser on the next RLS-GUI start. Note: the laser starting routine, indicated
by the blinking button LED, must be completed to successfully connect.
Figure 5: Screenshot of the RLS-GUI connection dialog.
If the connection is successful, the main window of the RLS-GUI will appear (see screenshot in ).
The status bar at the bottom of the window displays the replies of the laser system as well as the
indicators for the interlock, keyswitch, and modelock status. The response of the laser is displayed
after every command which has been sent by the GUI. If everything is working properly, the response
is ACK, which is short for acknowledged. In case of an error, an error code will be displayed (the error
codes are listed in Section ). The indicators behave as follows:
• Interlock: The indicator is red, if the interlock is closed, otherwise it is gray. Refer to chapter
4 “Controls & Indicators” for more information.
• Keyswitch: The indicator is red, if the key (see chapter 4 “Controls & Indicators”) is turned
on, otherwise it is gray. Note, that if it has been in on position during power-on, a cycling to
off- and on position is necessary.
• Modelock: This indicator is red when the oscillator is turned on and operating expectedly.
Internal safety measures are in place, if a sudden loss of mode-locking occurs (e.g., external
mechanical or electrical shock) to prevent further damage. In such an event, both, the
oscillator, and amplifiers are turned off and the error needs to be reset, by re-enabling the
laser system.
19

Picus Series User guide
The laser system can be enabled via the toggle button in the Enable groupbox on the top right. This
process takes a few seconds. Below, a groupbox depicts the measured wavelength and estimated
power of the Output. If the “Idler” option is available, a second groupbox will display the center
wavelength of the additional Idler output beam. If the “Filter” option is available, another groupbox
will be available.
Figure 6: Screenshot of the main window of the RLS-GUI.
The groupbox in the left column allows the control of the Laser Output. The details will be discussed
in the following:
• Wavelength: Select the wavelength of the output with the spinbox. This value is set in
nanometers (see test protocol for input bounds).
• Fine tune: This slider (ranging from -100% to 100 %) allows to fine-tune the output
wavelength within a certain range. This setting has a limited tuning range in the order of
50 cm-1, depending on the selected wavelength.
• Wavelength lock: The toggle button activates the “PICUS Wavelength Lock”, which engages
a PID locking of the wavelength of the output. This does not affect the selected wavelength but
uses the fine-tuning capability. The Picus Wavelength Lock can be used to eliminate slow drifts
of the central wavelengths from external temperature changes, or within the warm-up period.
• Power lock: Clicking the toggle button enables the “PICUS Power Lock”, which engages a PID
locking of the current output power. This can be used to eliminate slow power drifts induced
by external temperature changes. Especially during the warm-up period, the power lock may
run into its limit, causing the output power to drift again. To fix this, deactivate the power lock,
reset the wavelength of interest, and activate the power lock again. The power lock should
now stabilize the new power value. (Note: the power lock is an experimental feature and
might cause unexpected behavior. If you encounter any issues, please consult RLS for further
support.)
The groupbox in the left column allows the control of the Filtered Output (if option is available). The
details will be discussed in the following:
20

Picus Series User guide
• Auto-tune filter: This toggle button activates the auto-tune feature, where the filter
wavelength follows the set wavelength of the Laser Output (see above). As the output
wavelength of the signal slightly depends on the environment, it is recommended to engage
the “Wavelength lock” for the Signal.
• Wavelength: Select the wavelength of the filtered output with the spinbox if the Auto-tune
filter is disengaged. This value is set in nanometers (see test protocol for input bounds).
Menu Edit
The menu Edit allows to Disconnect (Ctrl+D) the laser, to open the Settings dialog (Ctrl+S), switch
between light and dark theme (Ctrl+T), as well as Exit (Ctrl+Q) the RLS-GUI.
The Settings window incorporates the following items:
• Picus Wavelength Lock: If the toggle button Internal Calibration is disabled a manual set
point can be chosen, otherwise an internal calibration is utilized.
• Miscellaneous: The spinbox Polling interval changes the rate with which the RLS-GUI
communicates with the laser system. Increase the polling interval to achieve less
communication traffic.
Figure 7: Screenshot of the Settings window.
Menu Show
The Monitoring View and the Command Window (see screenshots in and Figure 9) can be selected via
the Show menu at the top. Additionally, they can be invoked by the keyboard shortcuts Ctrl+M and
Ctrl+K, respectively. These views incorporate the following components:
• Monitoring View
• Section “Temperatures” shows internal temperature readings of the different
subsystems.
• Section “Currents” shows internal readings of various subsystems, such as seed
monitoring from photodiode measurements.
• Command Window
• Shows the command history of the recent commands send to the laser via the command
window.
21

Picus Series User guide
• Commands can be sent via the command line and the Send button at the bottom.
Figure 8: Screenshot of the Monitoring view (right groupbox).
Figure 9: Screenshot of the Command Window.
22

Picus Series User guide
Menu About
This menu shows details of the licenses and versions of the RLS-GUI as well as the driver and firmware
version.
23

Picus Series User guide
Laser Commands
The laser commands can be used to control and manipulate the state of the laser system. To query the
current value of a command, a question mark ? needs to be added. All laser commands (set and query)
must be terminated by a newline character \n.
The laser commands are based on SCPI commands and can be categorized into three categories:
Laser, Measure, and Monitor. The command names and a corresponding description is denoted in
the following.
Command Description
Laser:Enable {0|1} Sets or queries the Enable Status of the laser
Laser:Enable? system.
Laser:Wavelength {wavelength} Sets or queries the output wavelength.
Laser:Wavelength? {wavelength} is given in nanometers. See test
protocol for valid values.
Laser:PumpPID:Power:Enable {0|1} Sets or queries the Power Lock of the Pump
Laser:PumpPID:Power:Enable? output.
Laser:PumpPID:Power:Setpoint {pow} Sets or queries the setpoint of the Power Lock
Laser:PumpPID:Power:Setpoint? of the Pump output.
Laser:PumpPID:Wavelength:Enable Sets or queries the Wavelength Lock of the
{0|1} output.
Laser:PumpPID:Wavelength:Enable?
Laser:PumpPID:Wavelength:Setpoint Sets or queries the setpoint of the Wavelength
{wav} Lock of the output. {wav} is a wavelength or
Laser:PumpPID:Wavelength:Setpoint? wavenumber, depending on the setpoint type.
Laser:PumpPID:Wavelength:Type {0|1} Sets or queries the setpoint type of the
Laser:PumpPID:Wavelength:Type? Wavelength Lock, where type “0” uses
wavelength and type “1” uses wavenumber.
Laser:PumpPID:Wavelength:Internal Sets or queries the values used for Wavelength
{0|1} Lock. The internal setpoint uses a calibrated
Laser:PumpPID:Wavelength:Internal? look-up table. Without using the internal
setpoint, the Wavelength Lock can be used for
custom fine-tune values.
Laser:Finetune {finetune} Sets or queries the fine tune value of the
Laser:Finetune? current wavenumber. {finetune} is given in
percent and can be set within the boundaries
[–100, 100]. The fine-tune parameter can only
be set if the Wavelength Lock is disabled.
24

Picus Series User guide
Measurement Commands
The following commands can be used for a measure certain physical quantities of the laser system. All
parameters are read-only parameters.
Command Description
Measure:Runtime:Oscillator? Queries the runtime of the oscillator in hours.
Measure:Runtime:Amplifier? Queries the runtime of the main amplifiers in
hours.
Measure:Wavelength:Pump? Measures the current weighted mean center
wavelength of the output.
Measure:Power:Pump? Measures the current output power in mW.
Monitoring Commands
The following commands are intended for monitoring. All commands are read-only parameters.
Monitor:Temperature:Laserhead? Measures the internal laser head temperature.
Monitor:Temperature:Diode:{object}? Measures the temperature of one of the
following objects
{Oscillator|Preamp|Mainamp|Heatsink}.
Monitor:Current:{object}? Measures the current flowing into the respective
pump diode {Oscillator|Preamp|Pump}
({Oscillator|Preamp} in DAC bits and {Pump} in
A).
Monitor:Modelock:State? Returns the mode-locking state of the oscillator,
where “1” is mode-locking and “0” is non mode-
locking.
Monitor:Seed:Pump? Measures the optical seed power via a monitor
photodiode (in DAC bits).
Monitor:DiodePower:{object}? Measures the optical pump power of the
{Oscillator|Preamp} pump diode via its monitor
photodiode (in DAC bits).
25

Picus Series User guide
Error Codes
When changing a parameter, the laser typically responds with an acknowledge ACK. If an error occurs
when changing a parameter, the laser responds with a specific error code. Fehler! Verweisquelle
konnte nicht gefunden werden. shows a list of error codes with a description and possible causes.
Table 2: List of error codes, their description, and possible causes. The list is ordered
alphabetically.
Error code Description
AOM_ERR Activating or deactivating the AOM failed. Additionally, missing
seed radiation will raise this error.
BOUNDS_ERR The set value is out of the allowed bounds of the command.
ENABLE_ERR The laser cannot be enabled, because the key switch is not in the
enable position or the interlock is open.
GETSET_ERR An error occurred while trying to set or get a value. This error might
occur
LED_ERR Failure of the laser warning LED.
ML_ERR The oscillator is not in a proper mode-locked state. A mode-lock
error should disable all amplifiers immediately.
NOT_IMPLEMENTED_ERR The hardware addressed with the command is not implemented in
the laser system at hand.
SEED_ERR The seed radiation for the main amplifier is not detected. Missing
seed radiation can damage the main amplifiers. This error might
occur when trying to enable the main amplifiers while the oscillator
is not running.
SERVICE_ERR The laser system needs service. Please contact Refined Laser
Systems for assistance.
SWITCH_ERR Internal communication error. Please contact Refined Laser
Systems for assistance.
TEC_MAIN_ERR The TEC status of the main amplifiers’ laser diodes is not ok. This
error might occur when the TEC has not reached a stable state after
a cold start. Observe the temperature monitors in the monitor tab
of the GUI and retry to start the laser after a few minutes.
TEC_OSC_ERR The TEC status of the oscillator’s laser diode is not ok.
TEC_PRE_ERR The TEC status of the pre-amplifier’s laser diode is not ok.
26

Picus Series User guide
9. Sample Control Scripts
MATLAB
%% Matlab sample program to communicate with RLS Picus laser
% Open a serial connection to the laser
laser = visa('ni','COM7') % use the correct COM port of the laser
laser.Terminator = '\n'
fopen(laser)
%% Enable Laser
disp(query(laser,'Laser:Enable 1'))
%% Set the wavelength
disp(query(laser,'Laser:Wavelength 850'))
%% Get the wavelength
disp(query(laser,'Laser:Wavelength?'))
%% Shutdown Laser
disp(query(laser,'Laser:Enable 0'))
%% Close the serial connection
fclose(laser)
27

Picus Series User guide
Python
## Python sample script to communicate with RLS Picus laser
import visa #Communication via VISA
rm = visa.ResourceManager()
# Connect to the laser
laser = rm.open_resource('COM7') # use the correct COM port
laser.read_termination = '\n'
laser.write_termination = '\n'
## Enable Laser
print(laser.query('Laser:Enable 1'))
## Set and query wavelength
print(laser.query('Laser:Wavelength 850'))
print(laser.query('Laser:Wavelength?'))
## Shutdown Laser
print(laser.query('Laser:Enable 0'))
##
laser.close()
## Alternatively, use of Pyserial if VISA is not available
from serial import Serial # Communication via Serial Port
laser = Serial(port='COM8', timeout = 3)
cmd = 'Laser:Enable 1\n' #Append Termchar!
laser.write(cmd.encode()) #Pyserial needs to encode string to bytes
print(laser.readline().decode()) #Decoding necessary for read data
#In serial communication, the laser.write() command needs to be
followed by a laser.readline() command!
28