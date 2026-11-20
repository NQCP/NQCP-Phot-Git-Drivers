Version: 3.4
Modified: March 2023
Products: ANC300, ANM150, ANM200, ANM300
Firmware: 23-09-2022
User Manual
Piezo Positioning Electronic
ANC300

Open source software notice
The ANC300 and its modules (ANM150, ANM200, and ANM300) include certain open
source or other software originating from third parties that is subject to the GNU
General Public License (GPL), GNU Library/Lesser General Public License (LGPL) and
different and/or additional copyright licenses, disclaimers and notices.
You may obtain a complete corresponding machine-readable copy of the source code
of such software under the GPL or LGPL from attocube systems. attocube systems
offers to provide such source code to you on CD-ROM for a charge covering the cost
of performing such distribution, such as the cost of media, shipping and handling,
upon written request to:
attocube systems AG
Eglfinger Weg 2
D-85540 München
Germany
This offer is valid for a period of three (3) years from the date of the distribution of
this product by attocube.
ATTOCUBE SYSTEMS AG MAKES NO REPRESENTATION ABOUT THE SUITABILITY OF THIS
SOURCE CODE FOR ANY PURPOSE. IT IS PROVIDED "AS IS" WITHOUT EXPRESS OR
IMPLIED WARRANTY OF ANY KIND. ATTOCUBE SYSTEMS AG DISCLAIMS ALL
WARRANTIES WITH REGARD TO THIS SOURCE CODE, INCLUDING ALL IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. IN NO
EVENT SHALL ATTOCUBE SYSTEMS AG BE LIABLE FOR ANY SPECIAL, INDIRECT,
INCIDENTAL, OR CONSEQUENTIAL DAMAGES, OR ANY DAMAGES WHATSOEVER
RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF
CONTRACT, NEGLIGENCE, OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOURCE CODE.
Part of the Software is Copyright © 1994–2011 Lua.org, PUC-Rio.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
LabViewTM is a trademark of National Instruments Corporation.
Page 2

Table of Contents
List of Abbreviations .......................................................................... 5
I. Introduction .......................................................................... 7
I.1. System Overview ................................................................. 7
I.2. Safety Information .............................................................. 8
I.2.a. Safety Symbols on the Equipment .................................... 8
I.2.b. Safety Symbols in this Manual ......................................... 9
I.2.c. Warnings .................................................................. 10
I.3. Declarations of Conformity ................................................. 11
I.4. Waste Electrical and Electronic Equipment (WEEE) Directive ....... 12
II. Setup Procedure .................................................................... 13
II.1. Mechanical Installation ...................................................... 13
II.1.a. Positioning .............................................................. 13
II.2. Electrical Installation ........................................................ 13
II.2.a. Connecting to the Voltage Supply ................................. 13
II.2.b. Fuses ...................................................................... 14
II.3. Front Panel Controls and Indicators ...................................... 16
II.4. Back Panel Connections ..................................................... 18
II.4.a. How to connect a positioner ........................................ 18
II.5. Pin Assignment ................................................................ 20
II.5.a. Trigger Port .............................................................. 20
III. Description of the Controller and General Use .............................. 21
III.1. Overview ......................................................................... 21
III.2. Main Graphical User Interface .............................................. 22
III.2.a. Start-up Screens ...................................................... 22
III.2.b. General Usage of the ANC300 GUI ................................ 23
III.2.c. Main Configuration Dialogs ......................................... 23
III.2.d. Feature Codes.......................................................... 24
III.2.e. Network Configuration Dialog ..................................... 24
III.2.f. Trigger Configuration Dialog ....................................... 25
III.2.g. Limits Configuration Dialog ........................................ 26
III.3. ANM300 Module ............................................................... 27
III.3.a. ANM300 Front Panel Usage ......................................... 28
III.3.b. ANM300 Axis Screen Elements and Usage ...................... 29
III.3.c. Stepping Functionality .............................................. 30
III.3.d. Offset Voltage Functionality ....................................... 31
III.3.e. DC-IN Functionality .................................................. 32
III.3.f. AC-IN Functionality ................................................... 33
III.3.g. Filter Settings ......................................................... 33
III.3.h. GND Functionality .................................................... 34
III.3.i. Capacitance Measurement .......................................... 35
III.3.j. Limit Functionality .................................................... 36
III.4. ANM150 Module ............................................................... 38
III.4.a. ANM150 Axis Screen Elements and Usage ...................... 39
III.5. ANM200 Module ............................................................... 40
III.5.a. ANM200 Axis Screen Elements and Usage ...................... 41
IV. Remote Control of the ANC300 ................................................. 44
IV.1. Connecting the ANC300 ..................................................... 44
IV.1.a. Ethernet Connection .................................................. 44
Page 3
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

IV.1.b. USB Slave Port ......................................................... 44
IV.1.c. USB Master Port ........................................................ 45
IV.1.d. RS232 Port .............................................................. 45
IV.2. Remote Control ................................................................ 45
IV.2.a. Standard Console Commands ....................................... 46
IV.2.b. Example Console Session ............................................ 48
IV.2.c. Programming new patterns ......................................... 49
IV.2.d. Lua Console ............................................................. 50
IV.3. LabView™ Drivers.............................................................. 54
V. Upgrades and Add-ons ........................................................... 59
V.1. Firmware Upgrade ............................................................. 59
V.2. Removal of an Axis Module.................................................. 60
V.3. Installation of an Axis Module ............................................. 61
VI. Preventive Maintenance .......................................................... 62
VI.1. Safety Testing .................................................................. 62
VI.2. Fuses ............................................................................. 62
VI.3. Cleaning ......................................................................... 62
VII. Questions & Answers .............................................................. 63
Page 4

List of Abbreviations
A Ampere. The unit of electrical current.
AC Alternating Current.
AC-IN Input connector on the frontplate for AC voltages. Also used for the corre-
sponding mode, which (de-)activates this input.
ASCII American Standard Code for Information Interchange. A character-encoding
scheme based on the ordering of the English alphabet.
BNC Bayonet Navy Connector. Standard connector for coaxial cables, here only
used for 50 Ohm impedance connectors/cables.
°C Degree Celsius. The unit of temperature. Compare to K.
COM Port Communications port. Used to identify RS232 serial ports in PC operating
systems, such as Linux or Windows. Examples: COM1, COM2, etc.
CPU Central Processing Unit. The main controller in the ANC300.
CR Carriage Return. ASCII character code 13.
DC Direct Current. Identifies constant offsets or slow changing voltage levels.
DC-IN Input connector on the frontplate for DC voltages. Also used for the corre-
sponding mode, which (de-)activates this input.
DHCP Dynamic Host Configuration Protocol. Protocol to automatically assign an IP
address on a LAN network.
DOS Disk Operating System.
EC European Community.
EMC Electro-Magnetic Compatibility. Refers to corresponding CE regulations.
ESD Electrostatic Discharge. Sudden current equilibrating the electrical poten-
tials of two different objects. ESD currents may damage electronic equip-
ment.
ETH Short for Ethernet. Used as synonym for LAN.
F Farad. The unit of electrical capacitance. F = As/V
FAT File Allocation Table. FAT16 or FAT32 are file system architectures widely
used on many computer systems, especially Windows™ PCs.
FPGA Field Programmable Gate Array. An integrated circuit that can be configured
at runtime by uploading certain boot code. The FPGA in the ANC300 controls
fast actions such as stepping as well as communication functions.
FRQ Frequency. Used in conjunction with the stepping functionality of the
ANC300.
FTP File Transport Protocol. A basic internet protocol for sending/receiving files
over a LAN network or the internet.
GND Ground. Connection of chassis mass. Also used as description of a controller
mode, in which the outputs are deactivated and connected to chassis mass.
GUI Graphical User Interface. The interface displayed on the screen for user in-
teraction
HTTP Hypertext Transfer Protocol. Standard protocol used on LANs and the inter-
net.
Hz Hertz. The unit of frequency.
IP Internet protocol. The underlying basic protocol to FTP, HTTP, and others.
I/O Input / Output
LAN Local Area Network. Standard way of connecting several PCs or devices for
exchanging data over the internet.
LED Light Emitting Diode.
LF Line Feed. ASCII character code 10.
Page 5
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

LUA A programming language for embedded devices. See www.lua.org.
LVTTL Low Voltage Transistor to Transistor Logic. Triggering standard for direct
electrical end-to-end connections between two devices. Voltage levels are 0
and 3.3V. Compare to TTL.
m Meter. The unit of length.
OEM Original Equipment Manufacturer.
OSV Offset Voltage.
PC Personal Computer.
PCB Printed Circuit Board.
RoHS Reduction of Harmful Substances. Directive of the European Community.
RS232 Industry standard that defines characteristics of a serial, binary, single-
ended port. Used as synonym for COM port.
s Seconds. The unit of time.
STP Step. Used in conjunction with the stepping functionality of the ANC300.
Sub-D Subminiature D-type connector. Industry standard for serial connectors,
which is subdivided by the number of electrical pins on the connector, e.g.
Sub-D25. Often also called D-Sub.
TTL Transistor-Transistor Logic. Used to describe the TTL-compatible logic levels
for the in- and outputs of electronic instruments. Voltage levels are 0 and
5 V. Compare to LVTTL.
USB Universal Serial Bus. A single-ended serial bus.
V Volt. The unit of voltage.
VI Virtual Instrument. A complete program or subunit within the Labview pro-
gramming environment.
WEEE Waste Electrical and Electronic Equipment. Directive of the European Com-
munity.
Page 6

I. Introduction
I.1. System Overview
The Piezo Positioning Electronic ANC300 is a modular positioner control unit
providing the suitable drive signals to actuate attocube systems positioners
or scanners manually or under computer control. The ANC300 is available as
a modular housing that can host up to seven modules. There are modules that
enable (individually or combined):
- performing single as well as continuous stepping,
- applying DC offset voltages,
- amplifying DC voltages,
- mixing in of AC voltages, and/or
- measurement of the attached capacitance.
The ANC300 can be controlled either manually from the front panel, or re-
motely using:
- a virtual COM port over an USB connection to a PC,
- a serial port via an USB/serial adapter on the USB master port, or
- a terminal connection via the LAN port (2 types).
As the ANC300 can be connected to the local area network using the LAN in-
terface (ETH), one can also access the unit by connecting via web browser or
FTP (for updates only). For example, one can download the manual or the USB
drivers using the built in web server.
The attocube systems positioners are to be connected to the outputs of the
ANC300 using either the cable delivered with the system for table-top appli-
cations, or by using user supplied cabling for applications in extreme envi-
ronments such as low temperatures or ultra-high vacuum. Please refer to the
sections below for a description of the respective cabling requirements.
Page 7
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

I.2. Safety Information
For the continuing safety of the operators of this equipment and the protec-
tion of the equipment itself, the operator should take note of the Warnings,
Cautions, and Notes throughout this user manual and, where visible, on the
ANC300 itself.
I.2.a. Safety Symbols on the Equipment
WARNING. Risk of electric shock. High voltages present.
WARNING. Risk of an immediate hazard, which will lead to severe personal
injury or death danger. Refer to the manual for details on this hazard.
Caution. Hot surface. May cause injury when touched.
Caution. Electro-statically sensitive device. Equipment may get damaged if
touched by personnel not grounded. Only touch with earthed wristband at-
tached or otherwise connected to ground.
Functional (EMC) earth/ground terminal.
Page 8

I.2.b. Safety Symbols in this Manual
It is important to recognize safety information. The safety alert symbol-
- is used to draw your attention to potentials for personal injury or
property damage. The signal words WARNING and CAUTION are used with the
safety alert symbol and identify the level of hazard seriousness.
WARNING. An instruction, which draws attention to hazards or unsafe prac-
tices which could result in severe personal injury or death, if the security ad-
vice is not obeyed.
CAUTION. An instruction, which draws attention to hazards or unsafe prac-
tices which may result in minor personal injury or damage to the product,
process, or surroundings.
Note. Clarification of an instruction or additional information.
Page 9
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

I.2.c. Warnings
WARNING. Risk of electrical shock. The piezo translators and controllers,
as described herein, are high voltage devices, capable of generating high
output currents. They may cause serious or even lethal injuries if used im-
properly. Never touch any part that might have connection to the high
voltage output. Working with high voltage devices requires adequately
educated operating personnel.
WARNING. Risk of electrical shock. If the outputs are enabled while plug-
ging cables in or out there is a risk of touching harmful voltages. Never
connect any cabling to the electronics when the electronics is not in GND
mode!
WARNING. Risk of electric shock. If covers are opened, there is a risk to
touch hazardous voltages. If malfunction is suspected, immediately con-
tact attocube systems for repair or replacement. Modified or opened elec-
tronics cannot be covered by the attocube warranty anymore. Only person-
nel trained in the servicing and maintenance of this equipment should re-
move its covers or attempt any repairs or adjustments. Follow the General
Accident Prevention Rules.
WARNING. Risk of electrical shock. If this product is used in a manner
not specified by the manufacturer, the protection provided by the product
may be impaired. Do not operate the product outside its rated supply volt-
ages or environmental range.
• For laboratory use only.
• This product is intended for operation in the temperature range
5° to 40°C, 20% to 80% RH. In particular, excessive moisture
may impair safety.
• If the unit has been stored at a low temperature or in an environ-
ment of high humidity, it must be allowed to reach ambient con-
ditions before being powered up.
• The product must be connected only to an earthed fused single-
phase supply of 100V, 115V or 230 V, 50/60 Hz.
• To ensure reliable operation the unit should not be exposed to
corrosive agents or excessive moisture, heat or dust.
Page 10

CAUTION. Risk of damage. Plugging or unplugging modules of the elec-
tronics while connected to power line will irreversibly damage them. Inter-
nal capacitors need to be discharged before plugging in or out compo-
nents. To replace modules, disconnect the ANC300 from mains power and
wait for about 5 minutes before proceeding.
CAUTION. Risk of damage. Using the electronics in conjunction or con-
nection with equipment from other manufacturers not approved by atto-
cube may result in damage to the electronics or other equipment. atto-
cube is not liable for any damage resulting from wrong usage or usage in
conjunction with other equipment
I.3. Declarations of Conformity
For Customers in Europe
The ANC300 has been tested and found to comply with the EC Directives
89/336/EEC ‘EMC Directive’ and 73/23/EEC ‘Low Voltage Directive’ as
amended by 93/68/EEC.
Compliance was demonstrated by conformance to the following specifica-
tions which have been listed in the Official Journal of the European Com-
munities:
Safety EN61010: 2001
EMC EN61326: 1997
Page 11
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

I.4. Waste Electrical and Electronic Equipment (WEEE) Di-
rective
Compliance
As required by the Waste Electrical and Electronic Equipment (WEEE) Di-
rective of the European Community and the corresponding national laws,
attocube systems offers all end users in the EC the possibility to return
"end of life" units without incurring disposal charges.
This offer is valid for attocube systems electrical and electronic equip-
ment:
• sold after August 13th 2005,
• marked correspondingly with the crossed out "wheelie bin" logo
(see logo to the left),
• sold to a company or institute within the EC,
DE16963721
• currently owned by a company or institute within the EC,
• still complete, not disassembled, and not contaminated.
As the WEEE directive applies to self contained operational electrical and
electronic products, this "end of life" take back service does not refer to
other attocube products, such as
• pure OEM products, that means assemblies to be built into a unit
by the user (e. g. OEM electronic drivers),
• components,
• mechanics and optics,
• left over parts of units disassembled by the user (PCB's, housings
etc.).
If you wish to return an attocube unit for waste recovery, please contact
attocube systems or your nearest dealer for further information.
Waste treatment on your own responsibility
If you do not return an "end of life" product to attocube systems, you
must hand it to a company specialized in waste recovery. Do not dispose of
the unit in a litter bin or at a public waste disposal site.
Ecological background
It is well known that WEEE pollutes the environment by releasing toxic
products during decomposition. The aim of the European RoHS directive is
to reduce the content of toxic substances in electronic products in the fu-
ture.
The intent of the WEEE directive is to enforce the recycling of WEEE. A con-
trolled recycling of end of live products will thereby avoid negative im-
pacts on the environment.
Page 12

II.Setup Procedure
II.1. Mechanical Installation
II.1.a. Positioning
Carefully unpack and visually inspect the controller and stages for any
damage. Place all components on a flat and clean surface.
When placing the ANC300, it should be positioned so as not to impede the
operation of the main power supply plug and switch on the rear panel. En-
sure that proper airflow is maintained to the ANC300.
WARNING. Risk of fire. If airflow from the ANC300 is blocked, the unit
may overheat. Do not obscure any ventilation holes.
Note. In applications requiring the highest level of accuracy and repeata-
bility, it is recommended that the controller unit is powered up approxi-
mately 30 minutes before use, in order to allow the internal temperature
to stabilize.
II.2. Electrical Installation
II.2.a. Connecting to the Voltage Supply
WARNING. Risk of electric shock. If this product is used in a manner not
specified by the manufacturer, the protection provided by the product may
be impaired. The product must be connected only to an earthed fused sin-
gle-phase supply of 100 V, 115 V or 230 V, 50/60 Hz. To change the system
voltage, see section 0.
The ANC300 is shipped with appropriate power cables for use in Europe,
UK, USA, and Japan. When shipped to other territories the appropriate
power plug must be fitted by the user. Use only power supply cables sup-
plied by attocube systems, other cables may not be rated to the same cur-
rent.
Page 13
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

II.2.b. Fuses
WARNING. Risk of electrical shock. To exchange fuses:
1) Switch off the power and disconnect from mains voltage before re-
moving the fuse cover.
2) After switching off, always wait 2 minutes before opening the
ANC300, and before removing or inserting any module or card.
3) Always replace broken fuses with fuses of the same type and rating.
Two main fuses are located on the back panel for the mains voltage.
Four additional fuses are located on the inside of the power supply mod-
ule.
Inspecting the main fuses
For inspecting the main fuses, switch off, remove the mains power cable,
and wait 2 minutes. Then:
- Lift the catch of the fuse holder carefully up and pull it out.
- Inspect the fuses.
- If the fuses are ok, re-insert the fuse holder into the controller.
Changing the Internal Fuses
There are four fuses located on the power supply itself. Inspect and
change them as follows:
- Switch off and separate from mains power.
- Wait 2 minutes before going on.
- Open and remove the frontcover or the module next to the power sup-
ply.
- Open the four screws of the front cover of the power supply.
- Pull out the power supply by grabbing the cooling body inside the
ANC300. Do not pull on the frontplate!
WARNING. Risk of damage. If pulling excessively
on the front plate, the front plate holder might
break. Pull the cooling body instead!
Page 14

- Check the four fuses and replace them if necessary.
Fuse name value
Fu 1 (leftmost) 2 A /250V fast blow
Fu 2 1 A /250V slow blow
Fu 3 1 A /250V slow blow
Fu 4 (rightmost) 1 A /250V slow blow
- Once all fuses are ok, re-insert the power supply.
- Close the front cover screws.
- Put back the front cover/module in the slot next to the power supply.
- Make sure to disconnect any BNC cabling for a first test.
- Connect to mains voltage and switch on to check the functionality.
Changing the System Voltage
For changing the system voltage setting you will have to remove the fuse
holder and replace the fuses:
- Lift the catch of the fuse holder carefully and pull it out.
- Remove the right of the two fuse cartridges.
- Turn the white inner fuse cartridge so that it shows desired voltage
value in the window.
- Reinsert the fuse cartridge into the fuse holder. Double-check that the
correct voltage is shown in the window.
- Replace the fuses with the correct fuse for your mains voltage (see the
correct fuse values in the following table).
Mains voltage Fuses
230 VAC, 50 / 60 Hz 1 A /250V slow blow
115 VAC, 50 / 60 Hz 2 A /250V slow blow
100 VAC, 50 / 60 Hz 2 A /250V slow blow
- Once you have the correct fuses and the correct voltage setting, re-in-
sert the fuse holder into the controller.
- Make sure to disconnect any BNC cabling for a first test.
- Connect to mains voltage and switch on to check the functionality.
Page 15
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

II.3. Front Panel Controls and Indicators
1
2 3 4 5
Figure 1: Front panel of the ANC300 with seven ANM modules in place.
The front panel is arranged as follows:
1) Main display with touch screen functionality (CPU behind it),
2) View knob to move the focus in the main screen,
3) Edit knob to change values and activate options,
4) Power supply. There are fuses directly in the power supply that
can be checked in case of malfunctioning of the device. Unplug
the ANC300 from mains before attempting to open and slide out
the power supply.
5) 7 slots for modules.
See section III on how to use the controller. See section V.2 for removing
and section V.3 for installing modules.
Here, the ANC300 is shown equipped with seven ANM modules. These mod-
ules feature stepping as well as scanning functionality. There are different
types of modules available. There are (see Figure 2):
• ANM150, stepping module
• ANM200, scanning module
• ANM300, combined stepping and scanning module.
Page 16

1 2 1 2 1 2
3 3
4 4 4
7 5 5 7
8 8
6 6
Figure 2: Front panel of the ANM150, ANM200 and ANM300 modules. The different items are explained in the text.
On these modules, there are, dependent on the model type:
1) OUT LED to indicate active outputs,
2) ACT LED to indicate activity such as stepping,
3) FRQ dial to change the frequency value for the respective axis,
4) AMP dial to change the stepping or offset amplitude,
5) AC-IN or MOD BNC connector to input AC voltages,
6) DC-IN BNC connector to input DC voltages,
7) STEP switch for triggering single steps up- or downwards (one
step per switching), and
CONT switch for triggering continuous stepping up- or downwards (step-
ping as long as pressed).
Page 17
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

II.4. Back Panel Connections
10
1
2
3
5 6 7 8 9
4
Figure 3: Back panel of the ANC 300 piezo positioning electronic.
On the back panel, there are:
1) voltage selector (100 / 115 / 230 V) with integrated fuse holder
(see fuse description above),
2) main power switch,
3) main power supply connector, (IEC connector, 100 / 115 / 230 V,
each +/- 10%, 50 / 60 Hz, max. 100 VA),
4) output BNC’s (max. 160 V DC, max 4.5 A peak),
5) RS232 connector for serial connections to a PC,
6) 25 pin SubD in-/output connector for TTL triggering,
7) USB master port for updates and USB / Serial adapters,
8) USB device port for connections to the PC,
9) Ethernet 10/100 port for LAN connections, and
10) CE label with serial number and address of manufacturer.
II.4.a. How to connect a positioner
Positioner Vacuum Vacuum
Positioner
Cable Feedthrough Extension Cable
optional
Connecting a positioner is simply done by connecting an adapter cable to
the BNC output port of the respective axis and to the connector of the po-
sitioner.
Page 18

WARNING. Risk of electric shock. Touching the inner connector of the
BNC connectors may be dangerous, as there might be high voltages pre-
sent. Do not touch them.
CAUTION. Risk of damage. Equipment may be damaged if not connected
correctly. The correct polarity is indicated by a red pin, which corresponds
always to the inner, positive contact of the BNC.
Page 19
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

II.5. Pin Assignment
II.5.a.  Trigger Port
  The pin assignment of the 25 pin Sub-D connector (trigger port) as seen
on the back panel of the electronics is given in the table below:

|     | Pin  Trigger  | Default  |   Pin  | Trigger  | Default   |
| --- | ------------- | -------- | ------ | -------- | --------- |

|     | No.  Name  | Use        | No.   | Name  | Use          |
| --- | ---------- | ---------- | ----- | ----- | ------------ |
|     | 1  1       | Axis 1 UP  |   14  | 2     | Axis 1 DOWN  |
|     | 2  3       | Axis 2 UP  |   15  | 4     | Axis 2 DOWN  |
|     | 3  5       | Axis 3 UP  |   16  | 6     | Axis 3 DOWN  |
|     | 4  7       | Axis 4 UP  |   17  | 8     | Axis 4 DOWN  |

|     | 5  9  | Axis 5 UP  |   18  | 10  | Axis 5 DOWN  |
| --- | ----- | ---------- | ----- | --- | ------------ |
    13   12  11  10   9    8    7    6     5    4    3     2    1
|     | 6  11  | Axis 6 UP  |   19  | 12  | Axis 6 DOWN  |
| --- | ------ | ---------- | ----- | --- | ------------ |

|     | 7  13  | Axis 7 UP  |   20  | 14  | Axis 7 DOWN  |
| --- | ------ | ---------- | ----- | --- | ------------ |
        25  24  23  22  21  20  19 18  17  16  15  14
|     | 8  15             |           |   21  | 16     |           |
| --- | ----------------- | --------- | ----- | ------ | --------- |
|     | 9  Out 1          |           |   22  | Out 2  |           |
|     | 10  Out 3         |           |   23  | Out 4  |           |
|     | 11                | reserved  |   24  |        | reserved  |
|     | 12  3.3 V Supply  |           |   25  |        | GND       |
|     | 13  3.3 V Supply  |           |       |        |           |

WARNING. Risk of injury and fire hazard. Do not, under any circum-
stances, attempt to connect the digital I/O to any external equipment that
is not galvanically isolated from the mains or is connected to a voltage

higher than the limits specified in section II.2.
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
Note. The output triggers have an output voltage level in high state of
about 3.3 V, with a maximum output current of about 20 mA.
The maximum output current on the 3.3 V supply is about 300 mA (10 Ohm
  output impedance). The maximum reliable frequency is around 1.5 kHz.

Page 20

III. Description of the Controller and General Use
III.1. Overview
The ANC300 consists of a casing that houses up to seven modules. The
ANC300 is an electronics that fits in 19” rack installation; it is 3 rack units
high (13.3 cm), 84 rack units wide (45 cm), and 29.5 cm in depth. The axis
modules are individual electronics boards with frontplates.
The ANC300 has a power supply that generates the voltages needed by the
modules, i.e. +5 V, +15 V, -15 V, and +150 V. Appropriate mains filtering is
employed to achieve CE-compatibility as well as low emission and low
noise.
The ANC300 hosts a main CPU (behind the touch panel), which is the main
interface for user interaction. The CPU communicates to external devices
via the different connectors on the back panel. It communicates with the
axis modules using an internal bus. The analog signals generated by the
modules are guided over the bus to the outputs on the back side.
On the front screen, an easy to use menu allows to set parameters and dis-
play the current status. Parameters can be modified using the two knobs
just under the screen by turning or pushing. Values can be changed and
functions can be triggered in the following different ways of equal priority:
- Using the touch-screen one can browse through the menu struc-
ture and set values and start actions such as measuring the capaci-
tance. See section III.2.
- Using the buttons and switches on the front panel one can also
navigate the menu structure and also issue stepping manually. See
sections III.3, III.4, and III.5.
- The full functionality of the ANC300 is also accessible using any of
the remote control possibilities. See section IV for details.
Page 21
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

III.2. Main Graphical User Interface
III.2.a. Start-up Screens
When starting the ANC300, the screen at first shows the logo screen fol-
lowed by the initialization procedure.
Then, the internal bus is scanned for present modules and their types. The
type and the serial numbers are listed at their respective position. The sys-
tem is then configured accordingly.
Note. The serial numbers can be listed at a later stage as well (see section
III.2.c).
Note. It is possible to remove or introduce modules only when the ANC300
is completely switched off and separated from mains. See sections V.2 and
V.3 for detailed instructions.
1 After the initialization procedure, the Main Screen is shown. It contains
2 3 4
the following elements:
1) the Axis button. Click on it to go to the first axis screen.
2) the status of the AC-IN, DC-IN, and Filter functionality for each axis,
3) the Frequency, Step, and Offset Voltage settings for each axis
4) the output status or the current output voltage for each axis. If a
5 6 7 8 limit is exceeded on a certain axis, the corresponding number will be
shown in red. Also active stepping is indicated by the word “stp”.
2), 3), and 4) depend on the module type. Click on a line to directly switch
to the respective axis screen.
In the lower row, there are buttons for different configuration options:
5) main
6) network
7) trigger
8) limits configuration dialog.
These dialogs are discussed below.
Page 22

III.2.b. General Usage of the ANC300 GUI
There are different ways, how to change values and activate functions. One
can use the touch-screen directly or use the two turning knobs underneath
the display.
When using the touch-screen, the following actions are possible:
• Pressing on buttons will activate functions (menu buttons), toggle
values (on/off type fields), cycle through possible settings (e.g. fil-
ter setting), or cycle the change rate (numerical value fields).
• Pressing and sliding on numerical value fields, such as frequency or
voltage fields will increase (rightwards) or decrease (leftwards) their
value according to the current rate.
There are two turning knobs below the display that can be used for these
actions respectively: The VIEW and the EDIT knob.
• Turn the VIEW knob to move the focus through the screen,
• Press either knob to activate a menu button, to toggle on/off fields,
cycle filter setting, or cycle the change rate of numerical value
fields.
• Turn the EDIT knob to change numerical value fields.
Note: Turning the EDIT knob with the focus on the Axis field or the axis
number field will cycle through the different axes available. Turn the EDIT
knob completely to the left to go back to the Main Screen. Pressing on the
Axis button in the Main Screen, as well as on the axis number in each axis
screen will cycle through the different axis screens.
Note: After a waiting time, the ANC300 will automatically switch back to
the Main Screen. This waiting time can be set in the Main Config dialog.
On each axis module, there are additional knobs and switches (dependent
on the module type). These give direct access to the most important values
and functions on the respective axis. Please refer to the module descrip-
tion below to learn about the functionality available.
III.2.c. Main Configuration Dialogs
If pressing on the Main Config button in the Main Screen, one can further
select whether to list the important serial numbers or to change GUI set-
tings. Also the menu for the Feature Codes can be accessed here.
Press on the buttons to activate the sub-menus.
Press EXIT to go back to the Main Screen.
Page 23
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

The serial numbers listing shows the important serial numbers including
the serial number of the controller itself. Please have these numbers at
hand when contacting attocube systems for any support.
The serial numbers can also be listed via remote control (see section
IV.2.a).
In the GUI configuration dialog, one can set:
• Focus out after: The time after which the focus will jump back to the
button in the upper left corner.
• Return to main after: The time after which the GUI will switch to the
main screen again.
• Dim screen after: Timeout for the screensaver. The brightness will be
reduced in this example 60 s after the last user input has been made.
III.2.d. Feature Codes
Feature Codes allow for enabling certain additional features of the
ANC300.
Feature Codes can either be entered using the Feature Code screen or us-
ing the corresponding command (“setfc”) on the console. Feature Codes
are only usable for certain electronics and cannot be transferred. On suc-
cessful recognition of a feature code, the ANC300 displays an acknowl-
edgement. Enabled features stay enabled also after rebooting of the elec-
tronics.
III.2.e. Network Configuration Dialog
For the ANC300 to be visible and accessible on the local area network, a
valid network address is required. In the Network Configuration Dialog,
the user can choose between two methods for determining the network
address (IP address): DHCP or Manual setting.
If set to DHCP, the ANC300 tries to find a DHCP master in the LAN and will
query for a valid address.
If set to Manual, you can change the IP address, the subnet mask and the
default gateway to valid values for your local area network. These settings
have immediate effect.
Click on a number field to toggle its change rate between 1 and 10.
Page 24

III.2.f. Trigger Configuration Dialog
In the trigger configuration dialog, one can link trigger inputs to certain
axes and directions. There are 16 trigger inputs on the trigger port as
shown in section II.5.a. On successful recognition of a trigger event, the
corresponding axis will perform one step each in the given direction.
Click on a number field to cycle its number or select the number by turning
the EDIT button.
It is also possible to have several axes listening to the same input trigger
by simply entering the same trigger number in these axes.
Note. It is possible to enter the same trigger input to up and downward
motion at the same time. Still, only one step is performed in either up or
down direction. It is suggested to have different triggers for up and down
motion for one axis.
Page 25
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

III.2.g. Limits Configuration Dialog
In the limit configuration dialog, the user can activate certain limit set-
tings per axis. Choose one of two limit sets, Room Temperature or Low Tem-
perature. This setting allows choosing different limit settings for e.g. two
different temperatures.
Note. The Output Voltage Limit limits the overall output voltage (Step
Voltage + Offset Voltage). If the Out limit is exceeded, stepping will be
blocked.
Enter a maximum Step Frequency, a maximum Step Voltage, and an Out
Voltage Limit. This way, one can protect a piezo from too high voltage and
additionally avoid e.g. too much heating in a sensitive setup. See section
III.3.j for a description of the limit functionality.
CAUTION. Risk of damage. The DC-IN functionality is not affected by the
limit functionality and hence equipment connected to the outputs may be
damaged due to too high voltages. Make sure to restrict the input voltage
accordingly!
CAUTION. Risk of damage. If another electronics (e.g. ASC500) is con-
nected to the DC-IN port, and is turned on or off while DC-IN is enabled,
any produced transients or voltage spikes may be amplified and given to
the outputs. This may destroy attached piezos due to over-voltages. Make
sure to switch to GND mode during such procedures and to enable the DC-
IN functionality only if there is no risk of uncontrolled voltages on the in-
put.
Page 26

III.3. ANM300 Module
The ANM300 module is an open loop positioning and scanning module.
The nominal output voltage is unipolar from 0 to 150 V. The outputs are
protected against short-circuits and have a current limiter in order to pro-
tect them. The following functions are available (see schematic graph be-
low):
• Stepping with up to 150 V or up to 10 kHz rate,
• Setting an offset voltage (value after amplification: 0 .. +150 V),
• Amplifying DC-IN voltages from -10 .. +10 V input coerced to
(nominally) 0 .. +150 V output,
• Adding an AC-IN voltage to the output (not amplified),
• Filtering of the output voltage with either 16 or 160 Hz or no fil-
tering,
• Measuring the capacitance of an attached piezo,
• OUT LED to indicate positive output voltage above ~1 V,
• ACT LED to indicate stepping,
• Single, continuous, or endless stepping.
Step
Offset
x15
DCin
+
LP
+
Out
ACin
Figure 4: Schematic diagram for the ANM300. Step, Offset, and DC-IN signals are added up, low pass filtered, and
then amplified. The AC-IN is added after the amplifier.
Page 27
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

III.3.a. ANM300 Front Panel Usage
By turning or pressing any knob on a certain module front plate, the axis
screen as shown in Figure 5 below will appear. Another way to get to the
axis screen is to select the axis from the main overview list, or to cycle to
the axis by clicking on the axis button repeatedly.
The module can be controlled by the dedicated knobs on the axis or by the
axis screen itself. The use of the knobs is as follows:
• Turning a knob will change the respective value according to the
given rate.
• Pressing on the amplitude or frequency field or knob will cycle the
change rate through the following options: x0.1, x1, and x10.
Note. Please note that for the amplitude knob, the focus will jump to the
stepping voltage or the offset voltage depending on which field is being
activated. If both are active, there is a strict binding of the knob to one of
them. Double-click on the amplitude knob to toggle this binding.
Additionally, there are two switches for the stepping functionality on the
front-plate. The upper switch triggers only one step each time the switch
is pressed. The lower switch corresponds to continuous stepping, i.e. the
axis will generate steps as long as the switch is held.
Pressing both switches at the same time will start endless stepping in the
direction chosen (both up or both down). This can be stopped by pressing
one of the switches again
Page 28

III.3.b. ANM300 Axis Screen Elements and Usage
1 6 7 8 9 10
Me
2
11
3
12
4
13
5
14 15 16 17
Figure 5: Screen shot of the Axis View. Here, only the stepping functionality is enabled.
The following elements are shown in the axis screen and allow for the de-
scribed actions:
1) Axis number. Click to cycle to the next axis screen.
2) Step frequency. Press to set the focus. Press and slide to change.
Greyed if stepping is disabled.
3) Step voltage. Press to set the focus. Press and slide to change.
Greyed if stepping is disabled.
4) Offset voltage (after amplification). Press to set the focus. Press
and slide to change. Greyed if stepping is disabled.
5) Measured output voltage.
6) AC-IN switch. Press to toggle.
7) DC-IN switch. Press to toggle.
8) Stepping switch. Press to toggle.
9) Offset switch. Press to toggle.
10) Filter setting. Press to cycle through the filter settings.
11) Change rate FRQ. Press to cycle through the change rates.
12) Change rate STP. Press to cycle through the change rates.
13) Change rate OSV. Press to cycle through the change rates.
14) Back to main menu button. Press to go back to the main screen.
15) Configuration button. Press to go to the limit configuration menu.
16) Capacitance Measurement. Press to perform one measurement.
17) Ground switch. Press to set the axis module to ground.
Page 29
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

III.3.c. Stepping Functionality
The stepping output signal is by default a sawtooth wave. See section
IV.2.c on programming new patterns.
One step corresponds either to a linear rise to the nominal voltage in time
t = 1/frequency and a steep decrease to zero (on the order of 10 – 20 µs),
or a steep increase to the step voltage and a linear decrease. These differ-
ent waveforms correspond to the two directions: The first one to stepping
“up” (as seen when driving a z-positioner with normal orientation), the
latter one to stepping down.
Note. The steep flank of the signal is done as fast as possible, which is im-
portant to initiate the sliding phase of the slip-stick drive of the position-
ers. Due to the possible high capacitances of the piezos attached, there
might be considerable currents on the outputs. The ANM300 module can
supply peak currents of 4.5 A.
Note. Due to the high currents it is important that the attached leads to
the positioners have low resistance. Please double-check your positioners’
manual for acceptable resistance values.
To enable stepping, activate the respective field in the GUI (see Figure 5).
This will also enable the step voltage and the frequency field and allows
changing them.
Note. Certain limits apply (see sections III.2.g and III.3.j) for the step-
ping voltage. When the stepping voltage is too high, the output limit can
be reached and thus stepping will be deactivated. In such case, “Limit ex-
ceeded” will be written on the display. If step frequency and voltage ex-
ceed a certain output power, the power limit (same display “Limit ex-
ceeded”) can be reached. Note that this limit depends on the actual capac-
itance value shown. Hence, it is recommended to measure the capacitance
before stepping is enabled.
The steps are initiated either by the switches on the front plate as de-
scribed in section III.3.a or can be commanded using the remote control.
On Stepping, the ACT LED will illuminate and indicate stepping activity.
The output voltage measurement will indicate “STEPPING”. In the main
screen, STP will be written on stepping activity.
Page 30

III.3.d. Offset Voltage Functionality
The ANM300 also includes an offset voltage feature. When enabling the
offset voltage feature, one can set a constant offset voltage to be given
out on the outputs. This also enables the offset voltage field OSV.
Note. Limits apply (see section III.2.g and III.3.j) for the offset voltage.
The offset voltage is limited by the output limit.
CAUTION. Risk of damage. The offset voltage is given out immediately
when the offset feature is enabled. For security, the voltage value will be
set to zero when disabling the offset voltage feature.
Page 31
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

III.3.e. DC-IN Functionality
There are two BNCs on the module frontplate, labeled DC-IN and AC-IN.
The DC-IN input accepts -10 .. +10 V, while the output is (nominally)
0 .. +150 V. The gain is 15 (see Figure 6).
Note. It is possible to input negative voltages on the DC-in of up to -10 V
in order to pull down a positive offset voltage. The minimum voltage on
the outputs is defined by the internal amplifier which coerces the output
to approximately -7 .. +150 V.
CAUTION. Risk of damage. If high frequency signals (> 1 kHz) of high am-
plitude (> 1 V) are given to the DC-IN inputs and high capacitors are con-
nected to the output (> 500 nF), it is possible to damage the amplifier.
Sudden extreme jumps on very high capacitors may cause immediate dam-
age. Restrict the input frequencies and signal levels so that the electronics
does not overheat or might be damaged.
Figure 6: Frequency response of the ANM300 DC-IN input with different output filters applied. Note that the gain is
15 up to a frequency nearly up to 100 kHz. Note though that too high frequencies and amplitudes may damage the
amplifier.
Page 32

III.3.f. AC-IN Functionality
When switching on the AC-IN feature, a voltage of up to 10 VAC can be
added to the output (gain 1, no amplification) using the AC-IN BNC on the
frontplate of the module. Additional filtering can be switched on, with a
second order low pass filter with approx. 16 Hz, 160 Hz, or no filter.
Figure 7: Frequency response of the ANM300 AC-IN input. Note that the gain is nearly 1 starting from a frequency
of about 10 Hz and independent on the output filtering.
III.3.g. Filter Settings
The ANM300 module has built in low-pass filters that can be activated in
order to filter high frequency noise. These filters are nominal 16 Hz and
160 Hz or can be disabled.
Note. It is not allowed to generate a stepping signal with the filters ena-
bled. Upon enabling the filters, the step functionality will be disabled and
vice versa.
Page 33
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

III.3.h. GND Functionality
Upon pressing of the GND button, the ANM300 will disable all AC-IN, DC-
IN, Stepping, and Offset functionality and will connect the outputs to
chassis mass.
Note. Connecting the piezoelectric actuator leads to a mass is important
in order to reduce electro-mechanical noise on the actuator that might be
produced by the electronics. This is the recommended mode for sensitive
measurements. It is recommended that the controller is always kept in
GND state during changes (setup, software, temperature, etc.) and when
not in use.
CAUTION. Risk of damage. During major temperature changes of the at-
tached piezos, static voltages may accumulate. Hence, voltage limits may
be violated and the piezos damaged. It is recommended to keep the elec-
tronics attached in GND mode.
Page 34

III.3.i. Capacitance Measurement
The ANM300 module is capable of measuring the capacitance of a con-
nected piezo. The capacitance is an indicator for an electrically functional
system. If there is short-circuit in the wiring or if there is an open connec-
tion, the capacitance measurement will not show correct values.
Moreover, the capacitance is an indicator for the temperature of the piezo,
as the capacitance of a piezo is temperature dependent.
Upon pressing on the respective button in the GUI, the ANM300 will apply
a voltage of ~100 mV to charge the capacitance first then measures the
time for the discharging. The corresponding value is shown in the respec-
tive field on the GUI or can be queried remotely.
Note. The capacitance measurement is only available when all other func-
tions are turned off (GND mode).
Note. The capacitance value changes the limits for the output power limit
(see section III.3.j).
CAUTION. Risk of damage. During a capacitance measurement, a small
voltage of ~100 mV is applied to the output. There might be small me-
chanical motions on attached piezo systems. Such motions may damage
sensitive structures or experiments. Hence, measure the capacitance only
if any such systems are in safe positions.
Note. Piezoelectric actuators are temperature dependent capacitances.
The values measured with the ANC300 can easily differ by about 10-20%
from the specified value. This applies particularly at room temperature.
Moreover, the values measured with the ANM300 can differ from values
obtained by other measurement techniques.
Page 35
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

III.3.j. Limit Functionality
The ANM300 allows setting output (Out) and stepping (Step) limits by the
user. These limits will not allow increasing the output voltage above the
given limit nor allow increasing the step voltage above the Step limit. Ad-
ditionally, the ANM300 will not start any stepping when the Out limit is ex-
ceeded. Note that the Out limit restricts the sum of offset and stepping
voltage, while the Step limit only limits the stepping voltage. The display
will show “Limit exceeded” on the respective axis.
CAUTION. Risk of damage. The DC-IN functionality is not affected by the
limit functionality and hence equipment connected to the outputs may be
damaged due to too high voltages. Make sure to restrict the input voltage
accordingly!
CAUTION. Risk of damage. If another electronic (e.g. ASC500) is con-
nected to the DC-IN port, and is turned on or off while DC-IN is enabled,
any produced transients or voltage spikes may be amplified and given to
the outputs. This may damage attached piezos due to over-voltages. Make
sure to switch to GND mode during such procedures and to enable the DC-
IN functionality only if there is no risk of uncontrolled voltages on the in-
put.
Note. In case stepping is active and the voltage is changed at the same
time, then any such stepping will be stopped once a limit is reached.
There are two limit sets, Room Temperature or Low Temperature limits.
Please note that this setting applies for all axes globally. This allows
choosing different limit settings for e.g. two different temperatures.
Please refer to positioner specification sheets for maximum voltage and
frequency limits.
Additionally, a power limit applies. The power limit restricts the stepping
output power of the ANC300 to a certain maximum output power, hence
will only allow certain combinations of frequency and voltage. The display
will show “Limit exceeded” on the respective axis.
The power limit is dependent on the actual capacitance, as the output
power is scaling linearly with the capacitance. Unless a new capacitance
value is measured, the shown value will be used for the limit calculation.
Hence, it is mandatory to measure the capacitance before applying any
voltage to the outputs, in order to protect the ANC300 and the position-
ers.
Page 36

CAUTION. Risk of damage. If a capacitance value shown on the ANC300
outdates due to large temperature change or change of positioners, there
is a risk of overheating and damaging of internal components. Make sure
always to have the right capacitance value shown, by measuring it again
after changing a setup (also changing the temperature).
CAUTION. Risk of damage. Overriding the voltage limits of a piezo at-
tached, may damage the piezo. Always obey the limitations given by the
specifications sheet of your positioner.
The maximum allowed frequency for a pair of capacitance value and volt-
age is shown in the following table. Note that if no capacitance value is
measured (“?”), the output will be restricted the most.
Max. Fre- Capacitance [µF]
quency [Hz] 1 2 2.5 3 3.5 4 4.5 5 5.5
10 10000 3815 3624 3433 3338 3242 3147 2400 1329
]
20 10000 3052 2899 2747 2670 2594 2518 1800 1208
V [ 30 5500 2441 2319 2197 2136 2075 2014 1600 1098
e
g 40 3100 1953 1855 1758 1709 1660 1611 1300 998
a
t lo 50 2000 1563 1484 1406 1367 1328 1289 1100 908
V 60 1300 1250 1188 1125 1094 1063 1031 900 825
70 1000 1000 950 900 875 850 825 800 750
Page 37
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

III.4. ANM150 Module
The ANM150 module is an open loop positioning module. The nominal out-
put voltage is unipolar from 0 .. +150 V. The outputs are protected against
short-circuits and have a current limiter in order to protect them. The fol-
lowing functions are available (see schematic graph below):
• Stepping with up to 150 V or up to 10 kHz rate (see section III.3.j on
power limit before),
• Measuring the capacitance of an attached piezo,
• OUT LED to indicate positive output voltage above ~1 V
• ACT LED to indicate stepping.
• Single, continuous or endless stepping. The stepping functionality is
identical to the ANM300 described before in section III.3.c.
As the usage and features are very similar to the ANM300, in the following
there will be only remarks to differences to the ANM300.
x15
Step Out
Figure 8: Schematic diagram for the ANM150. There is only the step generator and its signal is amplified to the fi-
nal output voltage.
Page 38

III.4.a. ANM150 Axis Screen Elements and Usage
1 6 7 8 9 10
Me
2
11
3
12
4
13
5
14 15 16 17
Figure 9: Screen shot of the ANM150 axis view. Only the stepping functionality and the capacitance measurement
can be enabled.
The following elements are shown in the axis screen and allow for the de-
scribed actions:
1) Axis number. Click to cycle to the next axis screen.
2) Step frequency. Press to set the focus. Press and slide to change.
Greyed if stepping is disabled.
3) Step voltage. Press to set the focus. Press and slide to change.
Greyed if stepping is disabled.
4) Offset voltage. Disabled.
5) Measured output voltage.
6) AC-IN switch. Disabled.
7) DC-IN switch. Disabled.
8) Stepping switch. Press to toggle.
9) Offset switch. Disabled.
10) Filter setting. Disabled.
11) Change rate FRQ. Press to cycle through the change rates.
12) Change rate STP. Press to cycle through the change rates.
13) Change rate OSV. Disabled.
14) Back to main menu button. Press to go back to the main screen.
15) Configuration button. Press to go to the limit configuration menu.
16) Capacitance Measurement. Press to perform one measurement.
17) Ground switch. Press to set the axis module to ground.
Page 39
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

III.5. ANM200 Module
The ANM200 module is an open loop, low noise scanning module. The
nominal output voltage is unipolar from 0 .. +150 V. The outputs are pro-
tected against short-circuits and have a current limiter in order to protect
them. The following functions are available (see schematic graph below):
• Setting an Offset voltage (0 .. +150 V),
• Amplifying DC-IN voltages from -10 .. +10 V to 0 to 150 V,
• Adding an AC-IN voltage to the output (not amplified),
• Filtering of the output voltage with either 1.6, 16, 160, or 1600 Hz,
• Measuring the capacitance of an attached piezo,
• OUT LED to indicate positive output voltage above ~1 V.
As the usage and features are very similar to the ANM300, in the following
there will be only remarks to differences to the ANM300.
Offset
x15
DCin
+
LP
+
Out
ACin
Figure 10: Schematic diagram for the ANM200. Offset and DC-IN signals are added up and amplified. Low pass fil-
tering and AC-IN are added after the amplifier.
Note. It is possible to input negative voltages on the DC-in of up to -10 V
in order to pull down a positive offset voltage. The minimum voltage on
the outputs is defined by the internal amplifier which coerces the output
to approximately -7 to +150 V.
Page 40

III.5.a. ANM200 Axis Screen Elements and Usage
1 6 7 8 9 10
Me
2
11
3
12
4
13
5
14 15 16 17
Figure 11: Screen shot of the Axis View. Here, only the offset functionality is enabled.
The following elements are shown in the axis screen and allow for the de-
scribed actions:
1) Axis number. Click to cycle to the next axis screen.
2) Step frequency. Disabled.
3) Step voltage. Disabled.
4) Offset voltage. Press to set the focus. Press and slide to change.
Greyed if stepping is disabled.
5) Measured output voltage.
6) AC-IN switch. Press to toggle.
7) DC-IN switch. Press to toggle.
8) Stepping switch. Disabled.
9) Offset switch. Press to toggle.
10) Filter setting. Press to cycle through the filter settings.
11) Change rate FRQ. Disabled.
12) Change rate STP. Disabled.
13) Change rate OSV. Press to cycle through the change rates.
14) Back to main menu button. Press to go back to the main screen.
15) Configuration button. Press to go to the limit configuration menu.
16) Capacitance Measurement. Press to perform one measurement.
17) Ground switch. Press to set the axis module to ground.
Page 41
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

CAUTION. Risk of damage. If high frequency signals (> 500 Hz) of high
amplitude (> 1 V) are given to the DC-IN inputs and high capacitors are
connected to the output (> 500 nF), it is possible to damage the amplifier.
Sudden extreme jumps on very high capacitors may cause immediate dam-
age. Restrict the input frequencies and signal levels so that the electronics
does not overheat or might be damaged.
limits for DC input
1000Hz
1,0µF
2,0µF
900Hz
3,0µF
800Hz 4,0µF
5,0µF
700Hz
600Hz
y safe
c
n
e u 500Hz
q
e
r
f
400Hz
300Hz
200Hz
100Hz
critical
0Hz
0V 1V 2V 3V 4V 5V 6V 7V 8V 9V 10V
voltage
Page 42

Figure 12: Frequency response of the ANM200 DC-IN input.
Figure 13: Frequency response of the ANM200 MOD modulation input. Note that the gain is 0.01 up to a frequency
of 10 kHz.
Page 43
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

IV. Remote Control of the ANC300
IV.1. Connecting the ANC300
IV.1.a. Ethernet Connection
The ANC300 has a LAN port on the backside to connect it to the local net-
work. The IP-address for the ANC300 can either be chosen manually or by
DHCP (see section III.2.e). Different protocols are supported by the LAN
adapter:
• HTTP: An integrated web-server allows downloading drivers for the
USB port, the manual, specification sheets, and additional infor-
mation. In the future, it is planned to supply a web-interface for sta-
tus information and simple tasks.
• FTP: For updates, one can connect to the ANC300 via FTP. Log in as
user “update” with password “1234”. Send the update via a “put”
command to the ANC300. It will evaluate the update and install it in
case it is suitable and valid.
• Telnet: On ports 7230 and 7231 there are two different consoles, a
standard console and a programmable LUA console. One can connect
to these using e.g. Hyperterminal or another terminal program.
IV.1.b. USB Slave Port
The ANC300 has an USB slave device port on the backside of the casing.
When connecting to a PC, one needs to have the respective drivers for Win-
dows installed. Windows will then recognize a virtual COM port accordingly.
The drivers can be downloaded via the Ethernet connection as described be-
fore or can be found on the accompanying CD.
Installation of the drivers is straight forward. Guide the assistant to the
place where you have stored the driver. Do not search on the Internet for
drivers as suggested by the assistant. Please note that the drivers have not
been subject of the Windows Logo Test, so that the assistant will complain
about it. Install the drivers anyway.
Opening a Hyperterminal connection to the new virtual COM port will open
a standard console as described in the next sections.
Page 44

IV.1.c. USB Master Port
The ANC300 has a USB master port that can be used to connect different
slave devices, e.g.:
• an USB stick to implement updates,
• an USB joystick for directing the positioners manually (in future).
If an USB stick has been recognized, the ANC300 will try to read its contents
and look for a mating update file in the root folder. See section V for details
on the firmware upgrade procedure.
Note. In order to be able to read from the USB stick, it has to be formatted
with the FAT16 or FAT32 file system.
IV.1.d. RS232 Port
The RS232 port on the backside of the ANC300 can be used to connect to a
PC in order to establish a serial connection. The correct settings for the
port are 38400 baud, 8 data bits, no parity, 1 stop bit, no flow control.
See the section below (IV.2.a) for a description of the console and its com-
mands.
IV.2. Remote Control
There are two different types of consoles; one can connect to them using
e.g. telnet or Hyperterminal over the LAN port, or by directly connecting a
PC to the USB port (using a virtual COM port).
Only, when connecting over the LAN interface, one can connect to the pro-
grammable Lua console. All other consoles are based on the standard con-
sole. Note, that the standard console over the LAN interface is on port 7230
while the Lua console is on port 7231. For the consoles that connect over
the LAN port, one has to enter a password for security. This password is
“123456” per default.
Note, that the consoles have the same priority as the front panel. This
means that changes will have immediate effect, no matter through which
channel a command or a change has been issued.
The standard console features a simple text based command prompt, where
one can issue single commands that are instantly evaluated and executed.
The Lua console is more sophisticated. Here, it is possible to program also
little functions that perform more elaborate actions, such as scanning a
voltage up or down, triggering steps on different axes at the same time, or
the like. A few examples of the possibilities are given in the section below.
Page 45
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

IV.2.a.  Standard Console Commands
  A command on the standard console is composed of normal ASCII characters
and needs to be ended by a carriage return and a line feed character (DOS
line endings: CR = ASCII code 13; LF = ASCII code 10). When a command has
been executed, the answer should be “OK “, with optional lines before con-
taining data. In case of an error, the electronics returns “ERROR” together
with an error message if applicable. The typical timeout for these commands
is about 30 ms.

|     | General commands for the usage of the ANC300:  |                                                  |
| --- | ---------------------------------------------- | ------------------------------------------------ |
|     | Command                                        | Explanation                                      |
|     | help                                           | Print out a short help text.                     |
|     | echo [on|off]                                  | Enable/disable console echo.                     |
|     | ver                                            | Print the version number and the manufacturer.   |
|     | getser <AID>                                   | List the serial number of axis <AID>.            |
|     | getcser                                        | List the serial number of the controller board.  |
|     | setfc <CODE>                                   | Send a feature code to the ANC300.               |

  Get/Set commands define or query certain properties of axis module
<AID>. These are type-dependent, hence give an error message if the re-
quested functionality is not available.

| Set Command         | Get Command  | Explanation            |
| ------------------- | ------------ | ---------------------- |
| setm <AID> <AMODE>  | getm <AID>   | Set/get mode <AMODE>.  |
setf <AID> <FRQ>  getf <AID>  Set/get the stepping frequency <FRQ>.
setv <AID> <VOL>  getv <AID>  Set/get the stepping amplitude <VOL>.
| seta <AID> <VOL>       | geta <AID>    | Set/get the offset voltage <VOL>.  |
| ---------------------- | ------------- | ---------------------------------- |
| setaci <AID> [on|off]  | getaci <AID>  | Set/get status of AC-IN input.     |
| setdci <AID> [on|off]  | getdci <AID>  | Set/get status of DC-IN input.     |
setfil <AID> <FIL>  getfil <AID>  Set/get filter setting <FIL>.note different filter
options are available on ANM200 and ANM300.

Note: Using the remote console more modes are available as compared to
the front panel. Setting to a certain mode typically switches other func-
tionalities off. Especially, there are the following modes:
  •  gnd: Setting to this mode diables all outputs and connects them to
chassis mass.
•  inp: In this mode, AC-IN and DC-IN can be enabled using the setaci
and setdci commands. Setting to inp mode disables stepping and
offset modes.
•  cap: Setting to cap mode starts a capacitance measurement. The axis
returns to gnd mode afterwards. It is not needed to switch to gnd
mode before.
•  stp: This enables stepping mode. AC-IN and DC-IN functionalities are
not modified, while an offset function would be turned off.

Page 46

•  off: This enables offset mode. AC-IN and DC-IN functionalities are
not modified, while any stepping would be turned off.
•  stp+: This enables additive offset + stepping mode. Stepping wave-
forms are added to an offset. AC-IN and DC-IN functionalities are not
modified.
•  stp-: This enables subtractive offset + stepping mode. Stepping
waveforms are subtracted from an offset. AC-IN and DC-IN function-
alities are not modified.
|     |     |     |     |
| --- | --- | --- | --- |
Note. The allowed filter values are
•  for the ANM300 module: “16”, “160” and “off”.
•  for the ANM200 module: “1.6”, “16”, “160”, and “1600”.

|     |     |     |     |
| --- | --- | --- | --- |
  Pattern commands modify the step patterns on axis module <AID> (see
section IV.2.c for details on programming patterns):
|     |                      |              |                                      |
| --- | -------------------- | ------------ | ------------------------------------ |
|     | Set Command          | Get Command  | Explanation                          |
|     | setpu <AID> [0-255]  | getpu <AID>  | Set/get step up pattern (256 bytes)  |
|     | setpd <AID> [0-255]  | getpd <AID>  | Set/get step up pattern (256 bytes)  |

Note. The pattern values for the up or down patterns must be given as 256
integer numbers, separated only by spaces.

|     |     | Axis commands start or stop actions of axis module <AID>:  |                                              |
| --- | --- | ---------------------------------------------------------- | -------------------------------------------- |
|     |     | Command                                                    | Explanation                                  |
|     |     | stepu <AID> [<C>]                                          | Move <C> steps or continuously upwards (out- |
wards). An error occurs when the axis is not in
“stp” mode.
|     |     | stepd <AID> <C>  | Move number of steps or continuously downwards  |
| --- | --- | ---------------- | ----------------------------------------------- |
(inwards).
|     |     | stop <AID>   | Stop any motion.                                 |
| --- | --- | ------------ | ------------------------------------------------ |
|     |     | geto <AID>   | Return the measured output voltage.              |
|     |     | getc <AID>   | Return the saved capacitance value.              |
|     |     | stepw <AID>  | Wait for stepping to finish.                     |
|     |     | capw <AID>   | Wait for the capacitance measurement to finish.  |

|     |     | Trigger Commands modify input or output trigger settings:  |     |
| --- | --- | ---------------------------------------------------------- | --- |

Page 47
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

|     | Set Command  | Get Command  | Explanation  |     |
| --- | ------------ | ------------ | ------------ | --- |
settu <AID> [1-7|off]  gettu <AID>  Set/get input trigger up number on axis <AID>
settd <AID> [1-7|off]  gettd <AID>  Set/get input trigger down numbers on axis <AID>
|     | setto <TNUM> [0|1]  | getto <TNUM>  | Set/get output trigger status  |     |
| --- | ------------------- | ------------- | ------------------------------ | --- |

Note. Setting the status of the output triggers is only available if the fea-
ture is enabled.

  Valid Variables for these commands are:

|     | Variable  | Name     | Type     | Valid values         |
| --- | --------- | -------- | -------- | -------------------- |
|     | <AID>     | axis id  | integer  | 1, 2, 3, 4, 5, 6, 7  |
<AMODE>  axis mode  text  gnd, inp, cap, stp, off, stp+, stp-
|     | <C>  | run mode  | text/integer  | c  (continuous run),   |
| --- | ---- | --------- | ------------- | ---------------------- |
1, 2, … [steps]
|     | <FRQ>   | frequency       | integer  | 1, 2, ... , 10000 [Hertz]     |
| --- | ------- | --------------- | -------- | ----------------------------- |
|     | <VOL>   | voltage         | float    | 0.000,  ... , 150.000 [Volt]  |
|     | <TNUM>  | trigger number  | integer  | 1, 2, 3                       |
|     | <FIL>   | filter          | integer  | 1.6, 16, 160, 1600, off       |
(dependent on axis type)

| IV.2.b.  | Example Console Session  |     |     |     |
| -------- | ------------------------ | --- | --- | --- |
  This commented log of an example session demonstrates some basic fea-
tures of the console.
|     | > setm 1 stp  |     | Switch mode to stepping on axis 1  |     |
| --- | ------------- | --- | ---------------------------------- | --- |
OK
> setf 1 1000
|     |     |     | Set frequency on axis 1 to 1000 Hz  |     |
| --- | --- | --- | ----------------------------------- | --- |
OK
> setv 1 20
|     |     |     | Set the step voltage on axis 1 to 20 V  |     |
| --- | --- | --- | --------------------------------------- | --- |
OK
> stepu 1 1000
|     |     |     | Start 1,000 steps in upward direction on axis 1  |     |
| --- | --- | --- | ------------------------------------------------ | --- |
OK
> setm 2 off
|     |     |     | Switch axis 2 to offset mode  |     |
| --- | --- | --- | ----------------------------- | --- |
OK
  > seta 2 2.345678  Set the offset voltage on axis 2 to 2.345678 V
OK
|     | > geta 2              |     | Read the offset voltage on axis 2:    |     |
| --- | --------------------- | --- | ------------------------------------- | --- |
|     | voltage = 2.345000 V  |     | result: 2.345 V                       |     |
OK
  > geto 1  Read the output voltage on axis 1 (not stepping):
|     | voltage = 0.000000 V  |     | result: 0 V  |     |
| --- | --------------------- | --- | ------------ | --- |
OK
  > stepu 1 10000  Start 10,000 steps in upward direction on axis 1

Page 48

OK
> geto 1 While stepping, read the output voltage:
voltage = 10.500000 V result: 10.500 V
OK
IV.2.c. Programming new patterns
The normal patterns of the ANM150 and ANM300 are shown in Figure 14
below. These can be changed if needed.
A signal is generated from 256 sequential values, with the values ranging
from 0 to 255. A linear pattern for example consists of 256 small steps with
increments of 1/256 multiplied by the voltage that has been set on the front
panel. The time for each individual step is t= 1/256 * 1/f, with f being the
chosen frequency.
In the ANC300, the up and down patterns stored on each respective module
can be modified individually.
Figure 14: Default Up and Down Patterns.
If you query the upwards pattern the ANC300 will list the respective values
separated by newlines:
> getpu 1
0
1
(more lines here)
254
255
OK
Programming a new pattern is very simple. Just list all 256 values after the
axis number.
> setpu 1 0 1 2 3 4 [...] 254 255
OK
Page 49
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

IV.2.d. Lua Console
Using this console, it is possible to program more sophisticated tasks. The
Lua console offers programming of functions, tab completion, as well as a
history function. For a general overview on Lua it is recommended to look
up www.lua.org or http://www.lua.org/manual/5.1/manual.html.
Some few examples will be given in the following.
Axes are referred to as „modules“ on the Lua console. Hence, axis no. 1 is
addressed as module 1, alas “m1”, axis no. 2 is “m2”, and so on.
Like other object oriented languages, Lua differentiates between properties
and methods. Properties are called with a single dot “.”, methods are ad-
dressed using the colon “:”, as demonstrated in the following example:
Example No. 1: Setting the step-voltage on axis no. 1 to 20 V:
> m1.stp = 20
Hence, switching on or off an axis functionality is simply done by setting
the respective variable.
For the module objects, the following properties are available. Pressing tab
(tab completion) lists all possibilities.
Property Explanation Valid values
.acin AC-IN functionality ON, OFF
.dcin DC-IN functionality ON, OFF
.mode Mode setting GND, INP, CAP, STP, OSV,
STPP, STPM
.filt Filter setting 0,1,2,3,4
.cap Capacitance value (Read only value)
.frq Frequency setting 1, 2, ... , 10000 [Hertz]
.stp Step voltage 0.000, ... , 150.000 [Volt]
.osv Offset voltage 0.000, ... , 150.000 [Volt]
.out Measured output voltage (Read only value)
.act Activity indicator (Read only value)
.safe Limit indicator (Read only value)
.frqlimit Frequency limit value (Read only value)
.stplimit Step voltage limit (Read only value)
.outlimit Output voltage limit (Read only value)
.serial Axis serial number (Read only value)
.trigu Trigger input up 1, 2, 3, 4, 5, 6, 7
.trigd Trigger input down 1, 2, 3, 4, 5, 6, 7
.patu Pattern up table of pattern values
.patd Pattern down table of pattern values
In the same way, the output trigger values can be modified:
> trig1.value = 1
This will set to output trigger no. 1 to high level (3.3 V). Set it to 0 again to
commence the trigger pulse. The trigger object only has the .value prop-
erty.
Page 50

  Example No. 2: Switching axis no. 1 to step mode:
> m1.mode = STP

STP is a constant and represents a numerical value (4). Note, that a single
command doesn’t have to be ended by a semicolon “;”.
The following mode constants are predefined:
| Mode name      | Short  | Value  |
| -------------- | ------ | ------ |
| Ground         | GND    | 0      |
| Input          | INP    | 1      |
| Capacitance    | CAP    | 2      |
| Offset         | OSV    | 3      |
| Step mode      | STP    | 4      |
| Offset + Step  | STPP   | 5      |
| Offset - Step  | STPM   | 6      |

Note.  AC-IN and DC-IN are activated by separate variables.

  The following constants are equal to these numerical values:
Constant  Value
| ON    | 1   |     |
| ----- | --- | --- |
| OFF   | 0   |     |
| UP    | 1   |     |
| DOWN  | 0   |     |
 Additionally, the following filter settings are available:

| Filter setting  | ANM200   | ANM300  |
| --------------- | -------- | ------- |
| 0               | 1600 Hz  | off     |
| 1               | 160 Hz   | 16 Hz   |
| 2               | 16 Hz    | 160 Hz  |
| 3               | 1.6 Hz   | off     |
| 4, 5, ...       | 1600 Hz  | off     |
   Example No. 3: Making 100 steps upwards on axis 1:
> m1:step(UP,100)

Here, the method step is called with the parameters direction and number
of steps. Again, UP or DOWN are constants representing the numerical val-
ues 0 and 1. Hence, stepping is invoked by calling the proper method. These
other methods are available:
| Method  Explanation                          |     |     |
| -------------------------------------------- | --- | --- |
| :step(DIR,N)  step N steps in direction DIR  |     |     |
| :stop()  stop any actions                    |     |     |
| :wait()  wait for stepping to complete       |     |     |

Page 51
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

Example No. 4: Reading the status of the AC-IN input port on axis 1:
> print(m1.acin)
0
Here, we make use of a built-in Lua function, print. In this example the AC-
IN feature was switched off; if the feature was switched on, 1 would be the
result.
Example No. 5: Programming a simple function test, that lists all values
from 1 to n. In a normal Lua program the function could, for example, look
like this:
function test(n)
i=0;
while i<n do
i=i+1;
print(i);
end;
end
On the console, the whole function has to be written in one line, hence
one types:
> function test(n) i=0; while i<n 
do i=i+1; print(i); end; end
You don’t have to declare n, nor the output of the function. For example,
you call the function with the parameter 5 in this way:
> test(5)
1
2
3
4
5
This example shows that in Lua it is possible to program functions and sub-
routines, which enables much more sophisticated possibilities than only
calling single commands. The great advantage versus having a program
running on a PC is that delays due to repetitive commands through the se-
rial communication are minimized.
Example No. 6: Calculating the faculty of a number n:
> function factorial(n) if n==0 then 
return 1; else return n*factorial(n-1); 
end; end
Call the function as follows:
Page 52

> print(factorial(5))
120
Note, that this is a recursive function.
Example No. 7: Ramping a voltage continuously up on axis module from
start voltage start to end voltage end in steps number of steps:
> function scan(axis,start,stop,step) 
axis.mode=3; i=start; while i<stop do 
axis.osv=i; i=i+step; end; end
Call the function for example in the following way:
> scan(m1,10,20,0.001)
This will increase the voltage from 10 V to 20 V with 1 mV step width on
axis 1. Note that 1 mV is much more precise than the electronics can gen-
erate. The value is for the output rounded to the closest value. As an idea
for your own experiments, please try constructing an xy-scan function.
Example No. 8: Reading a pattern and defining a new one.
> for k,v in pairs(m2.patu) do print(k,v)
end;
As the result, the indexed up-pattern will be given out (index, value):
1 0
2 1
3 2
...
For setting the table, we need to define a table and then fill it. Note that
indexing in Lua starts with index 1:
> t={}
> for i = 1,256 do table.insert(t,i-1) end
> m2.patu = t
The last command sets the up-pattern to the constructed pattern table t.
Page 53
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

IV.3. LabView™ Drivers
All the commands described above are also available as LabView™ VIs. You
can find them on the CD delivered with the system. The drivers are only avail-
able for a specific LabView version and are provided “as is”.
Copy all of them to a convenient location on your disk.
All VI’s communicate to the ANC300 via USB or Ethernet. If no value for the
COM port number is given, Ethernet is selected by default.
Some of the VI’s only write certain values, some only read, while others can
read and write values. In the latter case, a Boolean value is required that
decides whether to write or to read a value.
Most of the VI’s generate a command string for convenience, which is sent
to the ANC300. It can be used to trace problems and to debug your own pro-
grams. Also in read data the data read from the ANC300 is given without any
conversion, so that the correct functionality can be traced.
Most of the VI’s feature error in and error out terminals. This can be used for
instance, to order them in a series.
The following VIs are provided (ANC300_v0.5.llb):
ANC300_Open.vi
This VI opens the communication channel and supplies the connection ID for
further vis.
Milliseconds to wait: Timeout for opening the device. If the timeout is
met, an error is given out
OpeningData_x: Response from the ANC300 [only via Ethernet]
ANC300_Close.vi
This VI closes the communication channel.
Page 54

ANC300_Mode.vi
ANC300_Mode.vi can read or set the mode for a respective Axis.
The VI writes the resulting mode to Axis mode out, when the mode is que-
ried. Transfer ok is true when the command was successful. Data out is the
direct response from the ANC300.
Allowed mode values that can be set, are:
Mode name Short
Ground GND
Input INP
Capacitance CAP
Offset OSV
Step mode STP
Offset + Step STPP
Offset - Step STPM
For more details on these modes see the first note in section IV.2.a
Note. Measure the capacitance The result has to be read with the
ANC300_preferences.vi.
ANC300_Input.vi
This VI controls the AC-IN and DC-IN inputs.
set /get determines whether the value is written or read. Use ON/OFF re-
spectively. Transfer ok is true when the command was successful. Data out is
the direct response from the ANC300.
Page 55
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

ANC300_Preferences.vi
ANC300_preferences.vi reads and writes stepping or offset voltage, or fre-
quency. It can also read the capacitance or measured output value. set /get
determines whether the value is written or read. Use value in and value out
respectively. Transfer ok is true when the command was successful. Data out
is the direct response from the ANC300.
parameter can be one of the following:
Cap [only get], Freq, Volt, Output [only get], Offset
Please note that for the capacitance measurement, the ANC300 has to be
switched to cap mode first before the capacitance value can be read with
the ANC300_preferences.vi.
ANC300_Step.vi
ANC300_Step.vi starts stepping a given number of steps. Send “0” to start
continuous stepping. Transfer ok is true when the command was successful.
Data out is the direct response from the ANC300.
ANC300_Stop.vi
Stops stepping on axis Axis.
Transfer ok is true when the command was successful. Data out is the direct
response from the ANC300.
Page 56

ANC300_WaitForStep.vi
This sub-VI waits for the end of a stepping command on a given axis.
Transfer ok is true when the command was successful. Data out is the direct
response from the ANC300.
ANC300_GetSerial.vi
This VI reads the serial number of a given axis. Specify “0” as the Axis ID in
order to read the serial number of the controller.
Transfer ok is true when the command was successful.
The serial number is given in Serial. The program determines whether a
valid serial number was returned and writes this result to Serial OK. Data out
is the direct response from the ANC300.
ANC300_trigger_setget.vi
ANC300_trigger_SetGet.vi reads and writes trigger status.
set /get determines whether the value is written or read.
Trigger Up / Down relates the trigger to an axis and direction, and respec-
tively shows the association. [only ANM150/ANM300]
Output switches output trigger to high/ low [mainly for use with LUA IV.2.d]
Page 57
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

ANC300_feature_code.vi
ANC300_feature_code.vi writes feature codes to enable / disable special
features. [III.2.d]
ANC300_pattern.vi
This sub-vi writes a new stepping pattern [28 data points] for the selected
axis and direction, and respectively reads the programmed pattern. Empty
fields will be filled with “0”. [IV.2.c]
ANC300_filter.vi
This sub-vi writes and reads the filter settings for the selected axis.
set /get determines whether the value is written or read.
Available are the settings:
ANM300 OFF 16Hz 160Hz -
ANM200 1.6Hz 16Hz 160Hz 1600Hz
ANC300_communicate.vi
This sub-VI is used by other vis to handle the communication to the ANC300.
A given command is written to the console. After certain waiting time the
answer is read and interpreted.
Page 58

V. Upgrades and Add-ons
V.1. Firmware Upgrade
At some point, a new firmware might be available for the ANC300. The fol-
lowing step-by-step description explains how to load this new firmware.
Method A:
1. Copy the update file on a FAT16 or FAT32 formatted USB stick.
Place it in the root directory of the stick.
2. Switch on the ANC300 and wait for the initialization to finish.
3. Plug in the USB stick to the USB master port of the ANC300.
4. The ANC300 will ask whether to search for an update. Click “OK”.
5. In case a mating update is found, the ANC300 will ask whether to
load the specific update. Again, click “OK” to load the update.
6. Wait for the update procedure to finalize and do not switch off
until the procedure is finished. During the update procedure, the
ANC300 might restart once or twice.
7. The update is finished when the main screen comes up again.
8. Remove the USB stick.
9. The controller is now ready to work with the new firmware.
Method B:
1. Connect the ANC300 to a LAN and manually select a suitable IP
address.
2. On your computer, open a command window.
3. Type “FTP <IP-address>” and start an FTP session with the
ANC300.
4. Login as user “update” with password “123456” (default).
5. Select binary protocol and upload the update file.
6. In case a mating update file is sent, the ANC300 will load and in-
stall the update. During the update procedure, the ANC300 might
restart once or twice.
7. Wait for the update procedure to finalize and do not switch off
until the procedure is finished.
8. The update is finished when the main screen comes up again.
9. The controller is now ready to work with the new firmware.
Page 59
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

V.2. Removal of an Axis Module
WARNING. Risk of electric shock. If covers are opened, there is a risk to
touch hazardous voltages. If malfunction is suspected, immediately con-
tact attocube systems for repair or replacement. Modified or opened elec-
tronics cannot be covered by the attocube warranty anymore. Only person-
nel trained in the servicing and maintenance of this equipment should re-
move its covers or attempt any repairs or adjustments. Follow the General
Accident Prevention Rules.
CAUTION. Risk of damage. Plugging or unplugging modules of the elec-
tronics while connected to power line will irreversibly damage them. Inter-
nal capacitors need to be discharged before plugging in or out compo-
nents. To replace modules, disconnect the ANC300 from mains power and
wait for about 5 minutes before proceeding.
CAUTION. Risk of damage. The components shown are sensitive to static
charges. Please use proper care when working with such electronics de-
vices. Avoid static charges by having a grounded wristband on while work-
ing with the components or otherwise grounding yourself.
To open the housing, unscrew the two screws on the front side of the re-
spective axis. The boards are connected to a backplate by a connector, so
some force is required to pull them out. If possible, open a blank cover
next to the module and hence get a better grip on the frontplate. Other-
wise, use the BNC connectors (attach e.g. a T-piece) or the dials and care-
fully pull on them to withdraw the module.
When pulling the module out, have an eye on the solder joints on the left
side of the module. Avoid any contact with the metallic front plate of the
neighboring module.
As soon as you have pulled out the module, please make sure to store it in
an ESD safe environment to prevent damages.
Finally, close the opening by attaching a blank cover plate and tightening
the screws.
Note. The ANC300 may not be used with the front cover open.
Page 60

V.3. Installation of an Axis Module
WARNING. Risk of electric shock. If covers are opened, there is a risk to
touch hazardous voltages. If malfunction is suspected, immediately con-
tact attocube systems for repair or replacement. Modified or opened elec-
tronics cannot be covered by the attocube warranty anymore. Only person-
nel trained in the servicing and maintenance of this equipment should re-
move its covers or attempt any repairs or adjustments. Follow the General
Accident Prevention Rules.
CAUTION. Risk of damage. Plugging or unplugging modules of the elec-
tronics while connected to power line will irreversibly damage them. Inter-
nal capacitors need to be discharged before plugging in or out compo-
nents. To replace modules, disconnect the ANC300 from mains power and
wait for about 5 minutes before proceeding.
CAUTION. Risk of damage. The components shown are sensitive to static
charges. Please use proper care when working with such electronics de-
vices. Avoid static charges by having a grounded wristband on while work-
ing with the components or otherwise grounding yourself.
Figure 15: Right and left side of an ANM300 module.
After mains and all other cabling have been removed, open the cover of a
free slot in the ANC300. Carefully insert the module taking care not to
touch the electronics with bare hands to avoid damages due to static elec-
tricity.
When inserting the module be sure to have the board sliding in the lower
and upper rail to ensure a proper connection of the module connector.
Firmly press the module into the connector.
After tightening the frontplate screws, the ANC300 can be switched on
again. Please check that the start-up screen lists the new module.
Page 61
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

VI. Preventive Maintenance
WARNING. Risk of electric shock. If covers are opened, there is a risk to
touch hazardous voltages. If malfunction is suspected, immediately con-
tact attocube systems for repair or replacement. Modified or opened elec-
tronics cannot be covered by the attocube warranty anymore. Only person-
nel trained in the servicing and maintenance of this equipment should re-
move its covers or attempt any repairs or adjustments. Follow the General
Accident Prevention Rules. Maintenance is limited to safety testing and
cleaning as described in the following sections.
Note: Please note that you may void the warranty for the ANC300 in case
unauthorized persons have opened the housing or unauthorized parts or
actions have been employed. This is especially true in case of the usage of
fuses not meeting the specifications.
VI.1. Safety Testing
Safety testing in accordance with local regulations, should be performed
on a regular basis, (typically annually for an instrument in daily use).
CAUTION. Risk of damage. The instrument contains a power supply filter.
Insulation testing of the power supply connector should be performed us-
ing a DC voltage.
VI.2. Fuses
See section II.2.b for fuse specifications and exchange of fuses.
VI.3. Cleaning
WARNING. Risk of electric shock. If water gets inside the casing, there is
a fire hazard, as well as a risk of electric shock. To avoid such:
• Disconnect the power supply before cleaning the unit.
• Never allow water to get inside the case.
• Do not saturate the unit.
• Do not use any type of abrasive pad, scouring powder, or solvent,
e.g. alcohol or benzene.
The fascia may be cleaned with a soft cloth, lightly dampened with water
or a mild detergent.
Page 62

VII. Questions & Answers
Note: Any time you call for technical support, the firmware version and date,
and the serial numbers (CPU, modules, housing) are essential to trouble-
shoot a problem. They can be queried with the “ver” and “ser” commands on
the console.
Q) The positioner is not moving properly.
A) This might have several reasons. Double-check the following:
- Connect the outputs of the ANC300 to an oscilloscope. Set to e.g. 1000Hz
and 20V. Does it show a sawtooth pattern? If the output is correct, there
might be a problem of the attached circuitry. If there is no output at all,
check the fuses at first.
- Check all internal and external fuses of the ANC300. In most cases a fuse
blows due to a short-circuit or an overload of the ANC300. Check any at-
tached circuitry on shorts.
- Check the mains voltage level. If the voltage differs more than ±10% toler-
ance from the nominal voltage level, the internal voltages might be af-
fected and too low or too high. As a consequence, the controller might be-
come unstable, fuses may blow or it may not work at all.
- Is the cabling low-ohmic (less than 5 Ohm)? If not, the positioners step ef-
ficiency will go down or stop the positioner completely.
- If the problem is related to the positioner, please refer to the positioner
manual.
Q) The ANC300 has no output and makes/made a clicking sound.
A) The ANC300 features short-circuit protection and turns off all outputs when
it detects too high currents. Please check your setup and cabling. It may be
required to re-start the ANC300 in case the clicking cannot be stopped.
Q) One axis of the ANC300 has no output and the red LED on one or more
modules is blinking.
A) The ANM modules feature overheat protection and shut down when too
much heat is generated. Please ensure that you are operating within the volt-
age and frequency limits and that proper airflow is maintained to the unit and
the ventilation holes are not blocked.
Also, the LEDs will blink red if the 150V supply voltage is not present. In this
case switch off and check all fuses (internal and external ones).
Q) Can the axis control system be controlled by GPIB interfaces?
A) The controller features an USB, and an Ethernet port, which can easily be
programmed with simple text commands. Labview drivers and some sample
VIs are supplied with the system. Currently attocube systems does not offer a
GPIB interface for the ANC300.
Q) I want to reduce the heat load on the cryostat. Can I connect the posi-
tioners using resistive wires?
A) Resistive wires are not recommended. A resistance of 10 Ohms or more may
be enough to prevent the positioners from working, as they require high cur-
rents (at low temperature about 0.5 to 1 A maximum). Alternatively, one can
use superconducting wires reducing the heat transfer without increasing the
resistance, or resistive wires with big diameters, respectively. Also, we suggest
applying a combination of different techniques.
Page 63
© 2001-2023 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject
to change without notice.

Main Office:
attocube systems AG
Eglfinger Weg 2
D-85540 Haar
Germany
www.attocube.com
Phone +49 89 420 797 0
Fax +49 89 420 797 201 90
E-Mail info@attocube.com
North America Support Hotline:
Phone +1 510 649 9245
South America Support Hotline:
Phone +1 510 649 9245
For technical queries, contact:
support@attcube.com
Page 64