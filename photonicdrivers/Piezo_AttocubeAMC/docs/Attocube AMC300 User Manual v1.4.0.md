User Manual
AMC300

Version: 1.4.0
Modified: 06/2024
Products: AMC300 | attoDISCOVERY Software | AMC Webserver Application
© 2024 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are
subject to change without notice.

Table of Contents | Page 1
Table of Contents
1 Notes on This Manual ............................................................................................................ 4
1.1 Purpose and Availability ................................................................................................ 4
1.2 Symbols and Conventions ............................................................................................. 4
1.2.1 Warning Notes ................................................................................................... 4
1.2.2 Symbols .............................................................................................................. 4
1.2.3 Information mark up .......................................................................................... 5
2 Declarations ........................................................................................................................... 6
2.1 Declaration of Conformity ............................................................................................. 6
2.2 Waste Electrical and Electronic Equipment (WEEE) Directive ....................................... 7
3 Safety Information ................................................................................................................. 8
3.1 Important Warnings ...................................................................................................... 8
3.2 Labels on the Device ...................................................................................................... 9
4 Device Description ............................................................................................................... 10
4.1 Intended Use ............................................................................................................... 10
4.2 Characteristics ............................................................................................................. 10
4.3 Scope of Delivery ......................................................................................................... 10
4.4 Operation Requirements ............................................................................................. 11
4.5 Dimensions .................................................................................................................. 12
4.6 PC Requirements ......................................................................................................... 12
4.7 Hardware Interfaces .................................................................................................... 12
4.7.1 Operator Panel (Table Top Version) ................................................................. 12
4.7.2 Operator Panel (Rack Version) ......................................................................... 13
4.7.3 Operator Panel (Double Rack Version) ............................................................ 13
4.7.4 Connector Panel ............................................................................................... 14
4.7.5 Remote Controller ............................................................................................ 15
4.7.6 Positioner Control Cable for Room Temperature Applications ........................ 16
4.7.7 Positioner Control Cable for Vacuum Applications .......................................... 18
4.7.8 Extension Cable for Vacuum Applications ........................................................ 22
5 Graphical User Interfaces ..................................................................................................... 24
5.1 attoDISCOVERY Software ............................................................................................ 24
5.1.1 "Find Devices" Screen ...................................................................................... 24
5.1.2 "Operation" Screen .......................................................................................... 26
5.2 Webserver Application ................................................................................................ 32
5.2.1 "Navigation" Screen ......................................................................................... 32
5.2.2 "Configuration" Screen..................................................................................... 36
5.2.3 "Interface" Screen ............................................................................................ 39
5.2.4 "About" Screen ................................................................................................. 42
5.2.5 "Controller Configuration" Screen ................................................................... 43
5.3 Touch Panel Application .............................................................................................. 44
5.3.1 Page Composition ............................................................................................ 44
5.3.2 "Main" Page ..................................................................................................... 48
5.3.3 "Axis Overview" Page ....................................................................................... 51
5.3.4 "Axis Settings" Page ......................................................................................... 51
5.3.5 "Controller Config" Page .................................................................................. 53
5.3.6 "Diagnostic Tools" Page ................................................................................... 54
6 Device Setup ........................................................................................................................ 55

Page 2 | Table of Contents
6.1 Unpacking and Positioning .......................................................................................... 55
6.2 Mounting the Rack and Double Rack Device ............................................................... 55
6.3 Connecting to Voltage Supply ..................................................................................... 56
6.4 Connecting to PC via USB ............................................................................................ 56
6.5 Connecting to Network ............................................................................................... 56
6.5.1 Establishing the Cable Connection ................................................................... 56
6.5.2 Configuring the Network Settings .................................................................... 57
6.6 Connecting Remote Controller .................................................................................... 58
6.6.1 Establishing a Cable Connection ...................................................................... 58
6.6.2 Establishing a Wireless Connection .................................................................. 58
6.6.3 Pairing Remote Controller and Device ............................................................. 58
6.6.4 Discarding the Pairing Connection ................................................................... 59
6.6.5 Switching off the Remote Controller ................................................................ 59
6.7 Configuring Remote Controller ................................................................................... 59
6.8 Connecting Positioner ................................................................................................. 60
6.9 Disconnecting Positioner ............................................................................................. 60
6.10 Installing the attoDISCOVERY Software ....................................................................... 61
7 Device Start-Up .................................................................................................................... 62
7.1 Switching On the Device .............................................................................................. 62
7.2 Switching On the Remote Controller ........................................................................... 62
8 Operation ............................................................................................................................. 63
8.1 Restoring Former Axis Selection .................................................................................. 63
8.2 Labeling Entities........................................................................................................... 64
8.2.1 Labeling Device ................................................................................................ 64
8.2.2 Labeling Axes .................................................................................................... 64
8.3 Activating and Deactivating Axis ................................................................................. 65
8.4 Configuring Axis ........................................................................................................... 66
8.4.1 Specifying Positioner Type ............................................................................... 66
8.4.2 Adjusting Axis Parameters................................................................................ 66
8.4.3 Loading Standard Axis Parameters ................................................................... 68
8.5 Open loop Positioning ................................................................................................. 69
8.5.1 Adjusting Motion Parameters .......................................................................... 69
8.5.2 Controlling Movements.................................................................................... 70
8.6 Closed Loop Positioning............................................................................................... 71
8.6.1 Activating Closed Loop Positioning .................................................................. 71
8.6.2 Moving Defined Distances................................................................................ 71
8.6.3 Moving to Defined Target ................................................................................ 72
9 Device Shut-Off .................................................................................................................... 73
9.1 Switching Off the Remote Controller .......................................................................... 73
9.2 Switching Off the Device ............................................................................................. 73
10 Update, Upgrade and Maintenance .................................................................................... 74
10.1 Adding Private Key and Certificate .............................................................................. 74
10.2 Updating Firmware ...................................................................................................... 75
10.3 Upgrading Device ........................................................................................................ 76
11 Troubleshooting ................................................................................................................... 77
11.1 Checking for Physical Network Connection ................................................................. 77
11.2 Physical Network Connection Present......................................................................... 78

Table of Contents | Page 3
11.2.1 Accessing Webserver Application .................................................................... 78
11.2.2 Resetting Device to Factory Defaults ............................................................... 78
11.3 Physical Network Connection Not Present .................................................................. 79
11.3.1 Reading out Network Settings.......................................................................... 79
11.3.2 Adjusting Network Settings .............................................................................. 79
11.3.3 Resetting Device to Factory Defaults ............................................................... 80
11.4 Measuring the Positioner Performance ...................................................................... 81
12 Optional On-Device Features and Upgrades........................................................................ 82
12.1 Dual- and Tri-Channel Upgrades .................................................................................. 82
12.2 /IO Feature Package .................................................................................................... 82
12.2.1 Pin Assignments ............................................................................................... 83
12.2.2 Output Modes and Parameters........................................................................ 85
12.2.3 Input Modes and Parameters........................................................................... 86
12.3 /PRO Feature Package ................................................................................................. 90
12.4 AMC/IDS Closed Loop Feature Package (Beta) ............................................................ 90
12.4.1 AMC/IDS Closed Loop Setup ............................................................................ 90
12.4.2 AMC/IDS Closed Loop Feature ......................................................................... 91
12.4.3 AMC/IDS Closed Loop Settings ......................................................................... 91
12.4.4 IDS Control ....................................................................................................... 94
12.4.5 Closed Loop Functions ..................................................................................... 97
12.4.6 Fine Tuning control loop .................................................................................. 97
12.5 Microscopy Upgrade ................................................................................................... 99
12.5.1 Use GPIOs with ASC500 .................................................................................... 99
12.5.2 Shared Lines for RES-position read-out .......................................................... 100
12.5.3 Hardware connection for usage within microscopy systems ......................... 100
13 System Integration ............................................................................................................. 102

  Page 4  |  Notes on This Manual
1  Notes on This Manual
1.1 Purpose and Availability
This user manual applies to the AMC300, also referred to as "device" in this document.
The user manual explains the installation and operation of the device. It contains instructions
for the appropriate use and the maintenance of the device.
o  Read this manual before setting up and using the device.
o  Always keep this manual easily accessible for all device users.
1.2 Symbols and Conventions
1.2.1 Warning Notes
|     |  WARNING  |     |
| --- | --------- | --- |
This is warning information about hazards that can cause death or severe injuries if the

suitable precautions are not taken.
|     |     |     |
| --- | --- | --- |
|     |     |     |
CAUTION
This is warning information about hazards that can cause injuries if the suitable precautions
  are not taken.
|     |     |     |
| --- | --- | --- |
|     |     |     |
NOTE
This is warning information about hazards that can cause property damages if the suitable

precautions are not taken.
|     |     |     |
| --- | --- | --- |
1.2.2 Symbols
For the continuing safety of the operator of this equipment and the protection of the
equipment itself, the operator must take notice of the warning symbols and notes throughout
this manual and - where applicable - on the device itself.
The following safety symbols are used in this manual:
|     |     |     |
| --- | --- | --- |
PPPrrrooottteeeccctttiiivvveee   EEEaaarrrttthhh

        Risk of electric shock! High voltages present. May cause injury or death when touched.

|     |     |     |
| --- | --- | --- |

Notes on This Manual | Page 5
General hazard! May cause injury or death if the suitable precautions are not taken.
May cause damage to the device, the process, or the surroundings if the suitable precautions
are not taken.
1.2.3 Information mark up
To improve traceability, the following design conventions are used in this document:
- Names of elements like folders, files, screens, options etc. are marked by "double
quotes".
- Prerequisites for actions are displayed with a leading check: ✓.
- Instruction steps which are part of a sequence are displayed with leading ordinal
number.
- Instruction steps which are variable or alternative are displayed with leading circle: o.
- Results of instruction parts are displayed with a leading arrow: →.
- References to parts of graphics are displayed in bold cardinal numbers.
- Software code or program text as well as file names are displayed in monospace
font.
- Variables and wildcards are displayed in italic font.
- Keys and buttons are marked by [square brackets].
- References to internal document parts are displayed in orange font.
TIP
This note provides additional information to simplify your work.

Page 6 | Declarations
2 Declarations
2.1 Declaration of Conformity
2.1.1.1 For Customers in Europe
This equipment has been tested and found to comply with the EC Directives 2014/30/EU "EMC
Directive" and 2014/35/EU "Low Voltage Directive".
Compliance was demonstrated by conformance to the following specifications, which have
been listed in the Official Journal of the European Communities:
- Safety EN61010-1:2010
- EMC EN61326-1: 2013
2.1.1.2 For North American Customers
This equipment has been tested and found to comply with the limits for a Class B digital device,
pursuant to Part 15 of the FCC Rules and meets all requirements of the Canadian Interference-
Causing Equipment Standard ICES-003 for digital apparatus. These limits are designed to
provide reasonable protection against harmful interference in a residential installation. This
equipment generates, uses, and can radiate radio frequency energy and, if not installed and
used in accordance with the instructions, may cause harmful interference to radio
communications. However, there is no guarantee that interference will not occur in a
particular installation. If this equipment does cause harmful interference to radio or television
reception, which can be determined by turning the equipment off and on, the user is
encouraged to try to correct the interference by one or more of the following measures:
o Reorient or relocate the receiving antenna.
o Increase the separation between the equipment and receiver.
o Connect the equipment into an outlet on a circuit different from that to which the receiver
is connected.
o Consult the dealer or an experienced radio technician for help.
Changes or modifications to the device that are not explicitly approved by attocube could void
the user's authority to operate the equipment.

Declarations | Page 7
2.2 Waste Electrical and Electronic Equipment
(WEEE) Directive
2.2.1.1 Compliance
As required by the Waste Electrical and Electronic Equipment (WEEE) Directive of the
European Community and the corresponding national laws, attocube offers all end users within
the European Union (EU) the possibility to return "end of life" units without incurring disposal
charges.
This offer is valid for attocube's electrical and electronic equipment:
- sold after August 13th 2005,
- marked correspondingly with the crossed out "wheelie bin" logo (see logo to the left),
- sold to a company or institute within the EU,
- currently owned by a company or institute within the EU,
- still complete, not disassembled, and not contaminated.
As the WEEE directive applies to self- contained operational electrical and electronic products,
this "end of life" take back service does not refer to other attocube products, such as
- pure OEM products, that means assemblies to be built into a unit by the user (e. g.
OEM electronic drivers),
- components,
- mechanics and optics,
- left over parts of units disassembled by the user (PCBs, housings etc.).
If you wish to return an attocube unit for waste recovery, please contact attocube or your
nearest dealer for further information.
2.2.1.2 Waste Treatment on Your Own Responsibility
If you do not return an "end of life" unit to attocube systems, you must hand it to a company
specialized in waste recovery. Do not dispose of the unit in a litter bin or at a public waste
disposal site.
2.2.1.3 Ecological Background
It is well known that WEEE pollutes the environment by releasing toxic products during
decomposition. The aim of the European RoHS directive is to reduce the content of toxic
substances in electronic products in the future.
The intent of the WEEE directive is to enforce the recycling of WEEE. A controlled recycling of
end of life products will thereby avoid negative impacts on the environment.

Page 8 | Safety Information
3 Safety Information
3.1 Important Warnings
WARNING
Risk of electric shock!
Inappropriate handling of the device may cause death, severe injury or material damage.
o Never remove the device's protective covers or attempt any repair or adjustment!
o Immediately shut off the device, disconnect the mains supply and contact attocube
in case of any suspected malfunction!
o Never connect any cabling to the electronics when the outputs are enabled!
o Be careful not to create short-circuits on the connectors or anywhere in the
cabling!
CAUTION
General hazard!
The device's operation under inappropriate conditions may lead to injury or material
damage.
o Do not operate the device outside its dedicated supply voltage or environmental
limits as specified in 4.4.
o Do not operate the device unless you are properly trained in the use and handling
of mains powered electrical equipment.
NOTE
Servicing and maintenance is only allowed to persons with explicit authorization of
attocube. There are no user serviceable parts on the device. Modified or open electronics
are no longer covered by attocube's warranty.
o Do not open the device.
o For servicing and repair always contact attocube.
NOTE
Unauthorized updates can lead to a permanent malfunction and are not covered by
attocube's warranty.
o Do not update the firmware of the device without authorization of attocube.

Safety Information | Page 9
3.2 Labels on the Device
The following labels can be found on the device.
Figure 1 Labels on the device
No. Label Explanation
1 AMC300 type label
QR-Code Link to device support
S/N Serial number
Type Product name
Power Rated power
Manufactured Year of manufacture
FCC FCC conformity
CE CE conformity
Crossed out wheelie bin Disposal advice for EU

Page 10 | Device Description
4 Device Description
4.1 Intended Use
The AMC300 is a controller for the simultaneous operation of up to three positioners out of
attocube's ANP series positioners. Depending on the customer's choice, the set of positioners
controlled can be an arbitrary combination of one to three dimensional, linear, rotary or
goniometric positioners with open loop or closed loop feedback.
The typical field of application are user steered or automated processes in laboratory and
industrial use.
4.2 Characteristics
The AMC300 is available as table top version, as rack version or as double rack version
comprising two separate devices. The rack versions are apt for being installed in a regular 19"
rack.
It provides four operation interfaces:
- the attoDISCOVERY software
- the AMC webserver application
- an integrated touch panel display
- a remote controller
An additional *.DLL library, delivered with each device, allows the integration of the
controller's functionalities into customized systems.
TIP
Consult the interface manual for the description of software commands and wrappers
provided for system integration.
The basic version can be upgraded and extended by several optional device feature an upgrade
packages (see section 10).
4.3 Scope of Delivery
The following components are part of the delivery:
- Positioning controller AMC300
- IEC power cord (suitable for use in UK, Europe or USA)
NOTE
The device is shipped with appropriate power cables for usage in the UK, Europe or the USA.
When shipped to other territories, the appropriate power plug has to be provided by the
user.
- USB-to-Ethernet adapter
- Ethernet cable
- USB flash drive with attoDISCOVERY software, dynamic link library and documentation
- Remote controller with Bluetooth USB receiver and USB cable

Device Description | Page 11
4.4 Operation Requirements
CAUTION
Wrong operation
If the AMC300 is used in a manner not specified in this manual or by attocube, the
protection provided by the device may be impaired!
o Only use the device in accordance with this manual.
CAUTION
Inappropriate working conditions!
The device's operation under inappropriate conditions may lead to injury or material
damage.
o Do not operate the device outdoor.
o Do not operate the device outside its dedicated voltage supply and environmental
limits.
CAUTION
Wrong cabling!
Inadequate equipment may cause electric shocks or fire.
o Only use power supply cables provided by attocube!
The following environmental limits have to be observed when operating the device.
Parameter Value
Supply voltage 100 V to 240 V AC
Line frequency 50 Hz to 60 Hz
Operational area Indoor use only
Maximum altitude 2000 m
Minimum temperature 5 °C
Maximum temperature 40 °C
Relative humidity at about 30 °C < 80 % (non-condensing)
Overvoltage category II
Pollution degree 2
NOTE
The contact with chemicals, humidity or dirt may damage the device.
o Do not expose the device to corrosive agents, excessive moisture, heat, dust or
other damaging environmental conditions.
o To clean the device only use clean and dry cloths.
o If the device has been stored at a low temperature or in an environment of high
humidity it must be allowed to reach ambient conditions before being started.

  Page 12  |  Device Description
4.5 Dimensions
Parameter  Table top version  Rack version  Double rack version
Dimensions  220 mm x 220 mm x  483 mm (19 inch) x  483 mm (19 inch) x
|         | 88 mm   | 260 mm x 88.1 mm  | 260 mm x 88.1 mm  |
| ------- | ------- | ----------------- | ----------------- |
| Weight  | 2800 g  | 3050 g            | 5850 g            |

TIP

For further information on the device's technical data, consult the corresponding
specification sheet.

4.6 PC Requirements
The following requirements have to be met by the connected PC.
| Parameter  | Value  |     |     |
| ---------- | ------ | --- | --- |
Processor design  Any PC or mobile device with a working and up-to-date
browser installed.
| Interface  | USB 2.0 or Ethernet RJ45  |     |     |
| ---------- | ------------------------- | --- | --- |
4.7 Hardware Interfaces
4.7.1 Operator Panel (Table Top Version)

Figure 2  Operator panel, table top version
| 1  Touch panel   |     | Operate the device, see sections 5.3 and 8  |     |
| ---------------- | --- | ------------------------------------------- | --- |
| 2  Power button  |     | Switch the device on or off                 |     |

Device Description | Page 13
4.7.2 Operator Panel (Rack Version)
Figure 3 Operator panel, rack version
1 USB socket additional USB-A for multiple connection purposes
2 Power button Switch the device on and off
3 Touch panel Operate the device, see sections 5.3 and 8
4.7.3 Operator Panel (Double Rack Version)
Figure 4 Operator panel, double rack version
1 USB socket additional USB-A for multiple connection purposes
2 Power button Switch the device on and off
3 Touch panel Operate the device, see sections 5.3 and 8

Page 14 | Device Description
4.7.4 Connector Panel
Figure 5 Connector panel
1 GPIO socket Trigger signal connection (in and out)
2 Ethernet uplink socket Network connection
3 Ethernet downlink socket Daisy-chaining connection (/PRO upgrade required)
4 USB socket USB-A for multiple connection purposes
5 Sensor IN socket Interferometer input connection
6 Power supply socket Power supply connection
7 Axis 1 socket Positioning signal connection
8 Axis 2 socket Positioning signal connection
9 Axis 3 socket Positioning signal connection

|     |     |     | Device Description  | |  Page 15  |
| --- | --- | --- | ------------------- | ----------- |
4.7.5 Remote Controller
With the wireless remote controller, it is possible to control and drive positioners without PC.

Figure 6  Controls of the remote controller
|     | 1  [L1] button  | (configurable)  |     |     |
| --- | --------------- | --------------- | --- | --- |
|     | 2  [L2] button  | (configurable)  |     |     |
3  [SHARE] button  Pair the remote control with the device (simultaneously
hold the [SHARE] and the PS button)
|     | 4  Light bars           | Indicates the active profile  |     |     |
| --- | ----------------------- | ----------------------------- | --- | --- |
|     | 5  [OPTIONS] button     | Switch profile                |     |     |
|     | 6  [R2] button          | (configurable)                |     |     |
|     | 7  [R1] button          | (configurable)                |     |     |
|     | 8  Directional buttons  | (configurable)                |     |     |
|     | 9  Left stick           | (configurable)                |     |     |
10  Display  Receive optic and haptic feedback on status of controlling
functions
|     | 11  PS button       | Switch the remote control on and off  |     |     |
| --- | ------------------- | ------------------------------------- | --- | --- |
|     | 12  Right stick     | (configurable)                        |     |     |
|     | 13  Symbol buttons  | (configurable)                        |     |     |
|     |                     |                                       |     |     |
TIP

Please refer to the manual of the remote controller for information on its structure and
functioning.
|     |     |     |     |     |
| --- | --- | --- | --- | --- |

Page 16 | Device Description
4.7.6 Positioner Control Cable for Room Temperature
Applications
The device is delivered with the following positioner control cable for room temperature
applications.
NOTE
When connecting customized cables certain cabling restrictions must be obeyed in order to
guarantee an optimal positioning and detecting performance.
o Do not to connect cabling with a wire resistance > 5 Ω.
o Use EMV housings as enclosure for the D-Sub connectors.
o Use extra shielded twisted pair wires for the piezo voltage supply.
o Do not connect any cable > 5 m.
o Do not connect the Piezo- pin of the AMC300 positioner control cable to ground
(e.g. via Oszi).
Figure 7 Positioner control cable AMC300/RES, for room temperature applications
1 26 pin D-Sub connector Positioning signal connection (device side)
2 5 pin socket Positioning signal connection (positioner side)
The pins of the device's positioner control cables are assigned as follows:

|     |     |     |     | Device Description  | |  Page 17  |
| --- | --- | --- | --- | ------------------- | ----------- |
Controller side (26 pin D-Sub)  Signal Name  Wire Color  Positioner side
|     |         |                 |                |     |     |
| --- | ------- | --------------- | -------------- | --- | --- |
|     |         |                 |                |     |     |
|     | 1       | Piezo+/OP2      | Brown          | 1   |     |
|     | 4       | Piezo-/ON12     | White          | 2   |     |
|     | 13      | GND             | Green          | 5   |     |
|     | 20      | V0/U2+          | Yellow         | 3   |     |
|     | 21      | GSENSE/U1-      | Gray (blue)    | 5   |     |
|     | 22      | TAP/U1+         | Blue           | 4   |     |
|     | 19      | VOREF/U2-       | Purple         | 3   |     |
|     | 21      | GSENSE/U1-      | Gray (purple)  | 5   |     |
|     | 11      | (Inner) shield  |                |     |     |
|     | 17, 18  | Jumper          |                |     |     |
|     | 1, 2    | Jumper          |                |     |     |
|     | 4, 5    | Jumper          |                |     |     |
|     | 16      | General shield  |                |     |     |
|     |         |                 |                |     |     |

Page 18 | Device Description
4.7.7 Positioner Control Cable for Vacuum Applications
For vacuum applications, the following positioner control cable can be ordered separately.
NOTE
When connecting customized cables certain cabling restrictions must be obeyed in order to
guarantee an optimal positioning and detecting performance.
o Do not to connect cabling with a wire resistance > 5 Ω.
o Use EMV housings as enclosure for the D-Sub connectors.
o Use extra shielded twisted pair wires for the piezo voltage supply.
o Do not connect any cable > 5 m.
o Do not connect the Piezo- pin of the AMC300 positioner control cable to ground
(e.g. via Oszi).
Figure 8 Positioner control cable AMC300/RES, for vacuum applications
1 26 pin D-Sub connector Positioning signal connection (device side)
2 15 pin D-Sub connector Positioning signal connection (vacuum feedthrough side)
The pins of the device's positioner control cables are assigned as follows.

|     |     |     |     | Device Description  | |  Page 19  |
| --- | --- | --- | --- | ------------------- | ----------- |
4.7.7.1 Pin Assignment for Axis 1
Controller side, axis 1 (26 pin D-Sub)  Signal Name  Wire Color  Feedthrough side
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     | 1       | Piezo+/OP2      | Brown          | 8   |     |
| --- | ------- | --------------- | -------------- | --- | --- |
|     | 4       | Piezo-/ON12     | White          | 15  |     |
|     | 13      | GND             | Green          | 4   |     |
|     | 20      | V0/U2+          | Yellow         | 5   |     |
|     | 21      | GSENSE/U1-      | Gray (blue)    | 4   |     |
|     | 22      | TAP/U1+         | Blue           | 12  |     |
|     | 19      | VOREF/U2-       | Purple         | 5   |     |
|     | 21      | GSENSE/U1-      | Gray (purple)  | 4   |     |
|     | 11      | (Inner) shield  | Silver         |     |     |
|     | 17, 18  | Jumper          |                |     |     |
|     | 1, 2    | Jumper          |                |     |     |
|     | 4, 5    | Jumper          |                |     |     |
|     | 16      | General shield  | Silver         |     |     |
|     |         |                 |                |     |     |

  Page 20  |  Device Description
4.7.7.2 Pin Assignment for Axis 2
Controller side, axis 2 (26 pin D-Sub)  Signal Name  Wire Color  Feedthrough side
|     |     |     |     |
| --- | --- | --- | --- |

| 1       | Piezo+/OP2      | Brown          | 7   |
| ------- | --------------- | -------------- | --- |
| 4       | Piezo-/ON12     | White          | 14  |
| 13      | GND             | Green          | 10  |
| 20      | V0/U2+          | Yellow         | 11  |
| 21      | GSENSE/U1-      | Gray (blue)    | 10  |
| 22      | TAP/U1+         | Blue           | 3   |
| 19      | VOREF/U2-       | Purple         | 11  |
| 21      | GSENSE/U1-      | Gray (purple)  | 10  |
| 11      | (Inner) shield  | Silver         |     |
| 17, 18  | Jumper          |                |     |
| 1, 2    | Jumper          |                |     |
| 4, 5    | Jumper          |                |     |
| 16      | General shield  | Silver         |     |

|     |     |     |     | Device Description  | |  Page 21  |
| --- | --- | --- | --- | ------------------- | ----------- |
4.7.7.3 Pin Assignment for Axis 3
Controller side, axis 3 (26 pin D-Sub)  Signal Name  Wire Color  Feedthrough side
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     | 1       | Piezo+/OP2      | Brown          | 6   |     |
| --- | ------- | --------------- | -------------- | --- | --- |
|     | 4       | Piezo-/ON12     | White          | 13  |     |
|     | 13      | GND             | Green          | 1   |     |
|     | 20      | V0/U2+          | Yellow         | 2   |     |
|     | 21      | GSENSE/U1-      | Gray (blue)    | 1   |     |
|     | 22      | TAP/U1+         | Blue           | 9   |     |
|     | 19      | VOREF/U2-       | Purple         | 2   |     |
|     | 21      | GSENSE/U1-      | Gray (purple)  | 1   |     |
|     | 11      | (Inner) shield  | Silver         |     |     |
|     | 17, 18  | Jumper          |                |     |     |
|     | 1, 2    | Jumper          |                |     |     |
|     | 4, 5    | Jumper          |                |     |     |
|     | 16      | General shield  | Silver         |     |     |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Page 22 | Device Description
4.7.8 Extension Cable for Vacuum Applications
For vacuum applications, the following attocube vacuum extension cable for the control of
positioners with resistive position readout (AVC/RES) can be ordered separately.
NOTE
When connecting customized cables certain cabling restrictions must be obeyed in order to
guarantee an optimal positioning and detecting performance.
o Do not to connect cabling with a wire resistance > 5 Ω.
o Use EMV housings as enclosure for the D-Sub connectors.
o Use extra shielded twisted pair wires for the piezo voltage supply.
o Do not connect any cable > 5 m.
o Do not connect the Piezo- pin of the AMC300 positioner control cable to ground
(e.g. via Oszi).
Figure 9 attocube vacuum extension cable AVC/RES, for positioners with resistive readout
1 15 pin D-Sub connector Positioning control and sensor connection (feedthrough
side)
2 2 pin connector Positioning control connection (positioner side)
3 2 pin connector Positioning control connection (positioner side)
4 2 pin connector Positioning control connection (positioner side)
5 3 pin connector Positioning sensor connection (positioner side)
6 3 pin connector Positioning sensor connection (positioner side)
7 3 pin connector Positioning sensor connection (positioner side)
The pins of the positioner control cables are assigned as follows:

|     |     |     |     | Device Description  | |  Page 23  |
| --- | --- | --- | --- | ------------------- | ----------- |
Feedthrough side (15 pin D-Sub)  Signal Name  Wire Color  Positioner side
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     | 1   | Piezo +1  | Copper  | 2/1  |     |
| --- | --- | --------- | ------- | ---- | --- |
|     | 9   | Piezo -1  | Copper  | 2/2  |     |
|     | 2   | Piezo +2  | Copper  | 3/1  |     |
|     | 10  | Piezo -2  | Copper  | 3/2  |     |
|     | 3   | Piezo +3  | Copper  | 4/1  |     |
|     | 11  | Piezo -3  | Copper  | 4/2  |     |
|     | 4   | RES 1+    | Copper  | 5/1  |     |
|     | 12  | RES 1S    | Copper  | 5/2  |     |
|     | 5   | RES 1-    | Copper  | 5/3  |     |
|     | 13  | RES 2+    | Copper  | 6/1  |     |
|     | 6   | RES 2S    | Copper  | 6/2  |     |
|     | 14  | RES 2-    | Copper  | 6/3  |     |
|     | 7   | RES 3+    | Copper  | 7/1  |     |
|     | 15  | RES 3S    | Copper  | 7/2  |     |
|     | 8   | RES 3-    | Copper  | 7/3  |     |
|     |     |           |         |      |     |

Page 24 | Graphical User Interfaces
5 Graphical User Interfaces
5.1 attoDISCOVERY Software
The attoDISCOVERY software is a PC-based application for controlling and analyzing positioner
movements.
Access If the software is installed it can be called up via the respective desktop icon or start menu
entry.
5.1.1 "Find Devices" Screen
Access The "Find Devices" screen is the start screen of the actual attoDISCOVERY software. From the
"Operation" screen it can be accessed by clicking [Back] (Figure 12/1).
5.1.1.1 Overview
The "Find Devices" screen is the actual start screen of the attoDISCOVERY software. It displays
the AMC300 and AMC100 devices connected to the respective network subnet. Each controller
is displayed in a separate tile.
TIP
When the software is started for the first time, a folder named attocube containing a file
named staticDevices.json is created in your user's folder at the PC.
In this file you can specify IP addresses of controllers that will automatically be connected,
even if they are not directly connected to the PC's network subnet.
Figure 10 "Find Devices" screen
1 [Next] Open the "Operation" screen (see section 5.1.2)
2 [Refresh list] Refresh the list of available controllers
3 Controller tile Read out and adapt controller properties (see below)
TIP
[Next] is not available unless you have selected at least one axis.

Graphical User Interfaces | Page 25
5.1.1.2 Controller Tile
The controller tile
- displays several controller and connection properties.
- allows you to label the controller and the axes, see section 8.2.
- allows you to select the axes to be displayed and controlled on the "Operation"
screen, see section 5.1.2.
Controls
Figure 11 Controller tile
1 Controller type field Read out the controller type and activated features
2 Controller name field Read out and adapt the controller name, see section
8.2.1
3 Controller SN and IP field Read out the controller's serial number and IP address
4 Axis selection checkbox Select axis to be displayed and controlled on the
"Operation" screen
5 Axis name field Read out and adapt the axis name, see section 8.2.2
6 [Device Page] Open the webserver application's "Configuration" screen
for configuring the device settings, see section 5.2.2
TIP
To select and use axes of various devices, the /PRO upgrade must be activated on all of the
controllers.

Page 26 | Graphical User Interfaces
5.1.2 "Operation" Screen
The "Operation" screen is the screen where the actual positioning process takes place.
Access The "Operation" screen can be accessed via the "Find Devices" screen's [Next] button.
5.1.2.1 Overview
The "Operation" screen displays the formerly selected axes (Figure 11/4), each in a separate
tile.
TIP
The headers of the active axes are displayed orange. The headers of the inactive axes are
displayed gray.
Figure 12 "Operation" screen
1 [Back] Open the "Find Devices" screen, see section 5.1.1
2 Axis tile Control axis, see section 8
5.1.2.2 Axis Tile, Operation View
The operation view of the axis tile is the default view on the axis parameters. It allows you to
- read out the axis' name and status.
- open the axis configuration.
- perform the actual positioning, see sections 8.5 and 8.6.
- measure the connected positioner's performance, see section 11.4.
NOTE
Position values for ANP series positioners are specified in micrometers or millidegrees,
respectively.

Graphical User Interfaces | Page 27
Controls
Figure 13 Axis tile, operation view (fully expanded)
1 Axis activation checkbox Activate or deactivate the axis, see section 8.3
2 Configuration link Open the axis' configuration view
3 Axis status bar Read out the axis' current status, see table below
4 Open loop movement controls Control open loop positioning movements, see table
below and section 8.5.2
5 "Amplitude" field Set the amplitude applied for a motion step, see section
8.5.1
6 "Frequency" field Set the frequency of motion steps, see section 8.5.1
7 "DC Value" field Set the DC value for manual position adjustment (/PRO
upgrade required), see section 8.5.1
8 [Closed Loop Functions] Expand closed loop functions, see section 8.6
9 Position display Read out current position
10 [-] Move defined distance in negative direction, see section
8.6.2
11 Distance field Set motion distance, see section 8.6.2
12 [+] Move defined distance in positive direction, see section
8.6.2
13 "Move to target" button Start movement to the defined target position, see
section 8.6.3
14 Target field Set motion target position, see section 8.6.3
15 [Diagnostic Tools] Expand diagnostic tools, see section 11.4
16 [Start] Start positioner property measurement, see section 11.4
17 Positioner property display Read out positioner performance measurement results,
see table below
18 Temperature display Read out the temperature status of the AMC, see table
below

Page 28 | Graphical User Interfaces
19 [Start] Start positioner performance tests, see table below
20 Status display Read out current performance test status
21 [Results] Download results of performance tests to be evaluated
by attocube support team
Axis status The axis status bar indicates the current status of the axis. The following states are possible:
Status message Description
positioner not connected No positioner connected
output not enabled Positioner connected, axis not activated
ready Positioner connected, axis activated, waiting for order
moving Positioner moving
in target range Positioner is within specified target range around target
position (and keeps regulating on the target position)
Forward limit reached Positioner reached insurmountable obstacle in positive
direction
backward limit reached Positioner reached insurmountable obstacle in negative
direction
grounded Positioner is in target range and grounded
compensating Rotation Compensation feature is compensating X/Y runout
Positioning controls The following control elements (Figure 13/4) are available for open loop movement control.
Control element Function
Move continuously in negative direction
Move stepwise in negative direction
Stop any movement
(including closed loop positioning movements)
Move stepwise in positive direction
Move continuously in positive direction
TIP
The number of steps implemented with each stepwise move can be adapted when /PRO
upgrade is activated.

|                    |                                                   |              |                        | Graphical User Interfaces  | |  Page 29  |
| ------------------ | ------------------------------------------------- | ------------ | ---------------------- | -------------------------- | ----------- |
| Motion parameters  | The following motion parameters can be adjusted.  |              |                        |                            |             |
|                    | Parameter                                         | Value range  | Related motion aspect  |                            |             |
|                    | Amplitude                                         | 0 – 60 V     | Step size              |                            |             |
Frequency  3 – 5000 Hz  Step repetition rate at continuous movement
|     | DC Value  | 0 – 60 V  | Manual fine adjustment of position  |     |     |
| --- | --------- | --------- | ----------------------------------- | --- | --- |
|     |           |           |                                     |     |     |
TIP

The power limit is dynamic, depending on the measured capacitance of the positioner. The
smaller the capacitance, the higher frequencies are possible for all axes.

| Measurements  | The following positioner properties can be measured.  |     |              |     |     |
| ------------- | ----------------------------------------------------- | --- | ------------ | --- | --- |
|               | Property                                              |     | Description  |     |     |
Capacitance (C)  Electrical capacitance of the positioner, including
cabling, the results are displayed directly
Resistance (R)  Electrical resistance of the positioner, including cabling,
the results are displayed directly
Temperature  Device temperature (ok, medium, high, critical)
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
NOTE
The measurement of the electrical capacitance (C) and electrical resistance (R) will be

started automatically every time an axis is activated - if not changed under “Auto measure C
and R” (Figure 14/17). Also be aware of the fact that the positioner will be moved slightly (a
few μm) within those measurements. The procedure will take a few seconds.
NOTE
The device temperature is an indicator for the overall functioning of the positioning system.

Connection or positioner errors are most likely if the device temperature is critical.
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
If the device shows a critical temperature it will deactivate all axes outputs for security reasons
in case of any further heating.
Performance   The following positioner performance aspects can be tested. attocube support team evaluates
the results with special tools.
|     | Performance aspect  |     | Test procedure  |     |     |
| --- | ------------------- | --- | --------------- | --- | --- |
Voltage  Performs 1000 steps with different amplitudes in both
directions.
|     | Velocity  |     | Moves over the positioning range twice in both  |     |     |
| --- | --------- | --- | ----------------------------------------------- | --- | --- |
directions.
|     | Feedback  |     | Performs 12 steps in both directions  |     |     |
| --- | --------- | --- | ------------------------------------- | --- | --- |
|     |           |     |                                       |     |     |
NOTE
By clicking [Results], the performance test results will be encoded and directly sent to

attocube.
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Page 30 | Graphical User Interfaces
5.1.2.3 Axis Tile, Configuration View
The options and functions available in the axis tile's configuration view depend on the device
configuration and the positioners you employ. It allows you to
- specify the positioner type.
- adapt various positioner performance options.
- read out certain axis properties.
TIP
Changes applied in the axis tile's configuration view are applied automatically, i. e. without
having to be confirmed by pressing a respective button.
Access The axis tile's configuration view can be accessed via the operation view's configuration link
(Figure 13/2).
Controls
Figure 14 Axis tile, configuration view
1 Return button Open the axis' operation view
2 Axis status bar Read out the axis' current status
3 "Positioner" field Select the positioner type (default: ANPx101)
4 "Number of steps" field Set the number of steps carried out with each stepwise
move (/PRO upgrade required)
5 "Sensor type" field Select the used sensor (AMC/IDS – Closed loop feature
required, default: Internal (RES) )
6 "Sensor power" field Select the feedback power value for the position sensor
(/RES positioner required, default: 0 dB)
7 "Target range" field Set the range regarded as "in target" for closed loop
positioning, see section 8.4.2
8 "Motion control threshold" Set position deviation that triggers automatic
compensation (AMC/IDS closed loop only)
9 "Fine positioning range" field Set the range where the fine positioning slew rate is used
in closed loop operation
10 "Fine positioning slew rate" Select the fine positioning speed. Slower speed results in
a more accurate position

Graphical User Interfaces | Page 31
11 "Configuration upload" button Upload a standardized positioner configuration – the
“LUT-file” (/RES positioner required)
12 "Status" Read out positioner serial number (as specified in
positioner configuration, see "Configuration upload")
13 "Ground on target" checkbox Activate or deactivate the positioner's being grounded on
target (/RES positioner required, default: deactivated)
14 "Ground target range" field Set the range regarded as "in target" for the positioner's
being grounded on target (/RES positioner required)
15 "Stop on end of travel" Activate or deactivate the positioner's being stopped
checkbox when faced with physical obstacles (/PRO upgrade
required)
16 "Disable sensor" checkbox Activate or deactivate position feedback (/RES positioner
required, default: deactivated)
17 "Auto measure C and R" Activate or deactivate automatic measurement of the
positioner's capacitance when axis is activated (default:
activated)
Sensor Power Within the drop-down menu for the sensor power (Figure 14/6) you can choose between four
different values:
- 0 dB (per default)
- -10 dB
- -15 dB
- -20 dB
With the adjustment of the sensor power one can affect the heat input of the system.
However, with lowering the sensor power also the signal-to-noise-ratio might get worse, what
could cause a lowering of the stability of the position controlling. The stability of the system as
well as the heat input strongly depends on the whole setup, the environment and other
parameters of each application. Especially for applications in the mK-range it is suggested to
adjust and test different sensor powers for the individual setup to find the optimum in low
heat input, good signal-to-noise-ratio and high positioning stability.
Within the drop-down menu for the fine positioning slew rate (Figure 14/10) you can choose
Fine positioning slew
between four different pre-sets:
rate
- slow
- slow-medium
- medium-fast
- fast
With the slew rate one can affect the fine positioning behavior of the positioners to avoid
unwanted stepping and blindly following noise after reaching the desired target position. After
the position is within the definable fine positioning range (Figure 14/9) around the target
position, the speed of the positioner is adjusted. When set to "slow", the speed is decreased to
a minimum, while the default behavior is "fast". Resultantly, "slow" does not follow high
frequency disturbances on the position. Therefore, "slow" represents a very fine positioning,
whereby "fast" represents a coarse positioning. This option does not affect the speed of the
positioning when targeting a position outside of the "fine positioning range".

Page 32 | Graphical User Interfaces
5.2 Webserver Application
The webserver application is a browser-based application for controlling and analyzing
positioner movements as well as for the controller device's configuration and maintenance.
Access If PC and device are connected to the same LAN and subnet, the webserver application can be
started by typing one of the following information into a browser's address line:
- the device's IP address
- the device's serial number (without slashes) followed by .local
TIP
For each device a separate browser window must be used.
5.2.1 "Navigation" Screen
The "Navigation" screen is the screen where the actual positioning process takes place.
Access The "Navigation" screen can be accessed via the [Navigation] button in the application's
header.
5.2.1.1 Overview
The "Navigation" screen displays all of the controller's three axes, each in a separate tile.
TIP
The headers of the active axes are displayed orange. The headers of the inactive axes are
displayed gray.
Figure 15 "Navigation" screen
1 Header Navigate between screens
2 Axis tile Control axis, see section 8
3 "Rotation Compensation" Activate and configure rotation compensation
section (Rotation compensation upgrade required)
4 [Controller Configuration] Configure the remote controller

Graphical User Interfaces | Page 33
5.2.1.2 Axis Tile, Operation View
The operation view of the axis tile is the default view on the axis parameters. It allows you to
- read out the axis' name and status.
- open the axis configuration.
- perform the actual positioning, see sections 8.5 and 8.6.
- measure the connected positioner's performance, see section 11.4.
NOTE
Position values for AN* positioners are specified in micrometers or millidegrees,
respectively.
Controls
Figure 16 Axis tile, operation view (fully expanded)
1 Axis activation checkbox Activate or deactivate the axis, see section 8.3
2 Configuration link Open the axis' configuration view
3 Axis status bar Read out the axis' current status, see table in section
5.1.2
4 Open loop movement controls Control open loop positioning movements, see table in
section 5.1.2 and section 8.5.2
5 "Amplitude" field Set the amplitude applied for a motion step, see section
8.5.1
6 "Frequency" field Set the frequency of motion steps, see section 8.5.1
7 "DC Value" field Set the DC value for manual position adjustment (/PRO
upgrade required), see section 8.5.1
8 [Closed Loop Functions] Expand closed loop functions, see section 8.6
9 Position display Read out current position

Page 34 | Graphical User Interfaces
10 [-] Move defined distance in negative direction, see section
8.6.2
11 Distance field Set motion distance, see section 8.6.2
12 [+] Move defined distance in positive direction, see section
8.6.2
13 "Move to target" button Start movement to the defined target position, see
section 8.6.3
14 Target field Set motion target position, see section 8.6.3
15 [Diagnostic Tools] Expand diagnostic tools, see section 11.4
16 [Start] Start positioner property measurement, see section 11.4
17 Positioner property display Read out positioner performance measurement results
18 Temperature display Read out the temperature status of the AMC
19 [Start] Start positioner performance tests
20 Status display Read out current performance test status
21 [Results] Download results of performance tests to be evaluated
by attocube’s support team
TIP
Some further explanation of the axis tile's operation view controls is given in section 5.1.2.
5.2.1.3 Axis Tile, Configuration View
The options and functions available in the axis tile's configuration view depend on the device
configuration and the positioners you employ. It allows you to
- specify the positioner type.
- adapt various positioner performance options.
- read out certain axis properties.
TIP
Changes applied in the axis tile's configuration view are applied automatically, i. e. without
having to be confirmed by pressing a respective button.
Access The axis tile's configuration view can be accessed via the operation view's configuration link
(Figure 16/2).

Graphical User Interfaces | Page 35
Controls
Figure 17 Axis tile, configuration view
1 Return button Open the axis' operation view
2 Axis status bar Read out the axis' current status
3 "Positioner" field Select the positioner type (default: ANPx101)
4 "Number of steps" field Set the number of steps carried out with each stepwise
move (/PRO upgrade required)
5 "Sensor type" field Select the used sensor (AMC/IDS – Closed loop feature
required, default: Internal (RES) )
6 "Sensor power" field Select the feedback power value for the position sensor
(/RES positioner required, default: 0 dB)
7 "Target range" field Set the range regarded as "in target" for closed loop
positioning, see section 8.4.2
8 "Motion control threshold" Set position deviation that triggers automatic
compensation (AMC/IDS closed loop only)
9 "Fine positioning range" field Set the range where the fine positioning slew rate is used
in closed loop operation
10 "Fine positioning slew rate" Select the fine positioning speed. Slower speed results in
a more accurate position
11 "Configuration upload" button Upload a standardized positioner configuration – the
“LUT-file” (/RES positioner required)
12 "Status" Read out positioner serial number (as specified in
positioner configuration, see "Configuration upload")
13 "Ground on target" checkbox Activate or deactivate the positioner's being grounded on
target (/RES positioner required, default: deactivated)
14 "Ground target range" field Set the range regarded as "in target" for the positioner's
being grounded on target (/RES positioner required)
15 "Stop on end of travel" Activate or deactivate the positioner's being stopped
checkbox when faced with physical obstacles (/PRO upgrade
required)
16 "Disable sensor" checkbox Activate or deactivate position feedback (/RES positioner
required, default: deactivated)
17 "Auto measure C and R" Activate or deactivate automatic measurement of the
positioner's capacitance when axis is activated (default:
activated)

Page 36 | Graphical User Interfaces
5.2.2 "Configuration" Screen
On the "Configuration" screen you can
- adapt certain controller and connection properties.
- update the device's firmware.
- upgrade its feature package.
Access The "Configuration" screen can be accessed via the [Configuration] button in the application's
header and via the [Device Page] button on the attoDISCOVERY's controller tiles (Figure 11/6).
5.2.2.1 Overview
Figure 18 "Configuration" screen
1 "Networking" section Adapt the network settings
2 "Device Name" section Rename the device and the axes
3 "Secure Access over HTTPS" Enable secure HTTPS access
section
4 "Firmware Update" section Update the device's firmware
5 "Feature Upgrade" section Activate features and upgrades

Graphical User Interfaces | Page 37
5.2.2.2 „Axis Setup/RES Sensors“ Section
In the „Axis Setup/RES Sensors“ section you can adapt the measurement mode of the AMC300.
The AMC300 supports two measurement modes for the lock-in measurement of the RES
position, those are “Individual per axis” and “Shared”(line).
Controls
Figure 19 "Axis Setup / RES Sensors" section, static configuration
Individual per axis: each axis’ position is measured on a different frequency; this mode reduces
noise coupling between axes, while requiring more cabling.
Shared (line/MIC-Mode): each axis is measured on the same frequency, within this mode the
number of required cables can be reduced; more coupling noise is expected on the position
readout.
Both measurement modes are also available in a ‘low frequency’ version. It might be necessary
to use the low frequency version, if the cables from the AMC300 to the positioners exceed the
standard length. Please contact the attocube’s support team, if you need further instructions
on that topic.
NOTE
Not only the required wires for the position readout but also the wires to connect the piezo
(U and U per direction of movement) to the electronics can be reduced. Depending
Step+ Step-
on the configuration of your controller, the common potential U will exhibit a constant
Step-
negative voltage when the axis is switched on, while for a deactivated axis the potential will
be GND. Therefore, please make sure to not interconnect the U on the motion controller
Step-
side to prevent a short circuit. This cabling will require the axis which shares U to be
Step-
powered on in order to drive the other axes.
TIP
For more information see the setMode function of the RES interface in the Interface Manual
or attocubes Technical note TN04 “Numbers of Wires”.

Page 38 | Graphical User Interfaces
5.2.2.3 "Networking" Section
In the "Networking" section you can adapt the network settings used by the device for
connection to a LAN.
Controls
Figure 20 "Networking" section, static configuration
1 "IP mode" field Select the IP mode (default: DHCP)
2 "IP address" field Enter device's IP address
3 "Subnet mask" field Enter IP subnet mask
4 "Default gateway" field Enter default gateway address
5 "DNS resolver" fields Enter DNS resolver address (optional)
6 "Proxy server setting" field Enter the proxy server address (optional)
7 [Test internet connection] Check the connection to the internet
8 "Device reachable at" display Read out device's DNS name
5.2.2.4 "Device Name" Section
The "Device Name" section allows you to label the device and its axes.
Controls
Figure 21 "Device Name" section
1 "Device name" field Enter the device's name
2 "Axis name" fields Enter the axis' name (default: Ax…)
TIP
Note that all axes of a device must have different names.

Graphical User Interfaces | Page 39
5.2.3 "Interface" Screen
On the "Interface" screen, the settings for incoming and outgoing trigger communication can
be configured each in a separate tile. The tiles are divided in three sections corresponding to
the axes.
For the parameters and value ranges that are related to a certain protocol, consult section
12.2.
TIP
For trigger communication the /IO feature upgrade is required.
Access The "Interface" screen can be accessed via the [Interface] button in the application's header.
5.2.3.1 Overview
Figure 22 "Interface" screen
1 "Real Time Input" tile Configure real time input
2 "Real Time Output" tile Configure real time output

Page 40 | Graphical User Interfaces
5.2.3.2 "Real Time Input" Tile
On the "Real Time Input" tile you set the communication mode and the parameters for the
interpretation of incoming position commands.
TIP
To allow you a comfortable adjustment of the parameters, the real time input is not applied
until it is activated explicitly.
Controls
Figure 23 "Real Time Input" tile, "Axis" section
1 "Mode" field Select input mode
2 Parameter fields Adapt input parameters
(vary according to input mode)
3 [Disable] Deactivate real-time input
4 [Enable] Activate real-time input
5 Activation indicator Read out the activation status of trigger input
communication (green: trigger input is enabled)
6 [Discard] Discard all changes
7 [Apply] Save all changes
The number and the designation of the parameter fields depends on the selected input mode.

Graphical User Interfaces | Page 41
5.2.3.3 "Real Time Output" Tile, "Global parameters" Section
In the "Global parameters" section you specify the signal mode for the trigger output
communication.
Controls
Figure 24 "Real Time Output" tile, "Global parameters" section
1 "Signal Mode" field Select signal mode
5.2.3.4 "Real Time Output" Tile, "Axis" Section
In the "Axis" section you adapt the signal type for trigger output communication, and its
parameters.
Controls
Figure 25 "Real Time Output" tile, "Axis" section
1 "Mode" field Select output mode
2 Parameter fields Adapt output parameters
(vary according to output mode)
3 [Discard] Discard all changes
4 [Apply] Save all changes
The number and the designation of the parameter fields depends on the selected output
mode.

Page 42 | Graphical User Interfaces
5.2.4 "About" Screen
The "About" screen enables you to reset or reboot the device and provides you with
comprehensive information on
- the device itself, the software used, and the features and upgrades activated.
- the manufacturer.
- sources of integrated software parts.
- activated licenses.
TIP
As the information of the "About" screen may be relevant for servicing, updating, upgrading
and maintaining the device or its parts, prepare to retrieve the information and provide it to
attocube in case of questions and servicing requests.
Access The "About" screen can be accessed via the [About] button in the application's header.
Controls
Figure 26 "About" screen, detail
1 "Manufacturer" section Read out manufacturer information
2 "Version" section Read out device information
3 [System reboot] Reboot device
4 [Factory reset] Restore factory settings (see 11.2.2)
5 "On-Device Features" section Read out active features and upgrades

Graphical User Interfaces | Page 43
5.2.5 "Controller Configuration" Screen
On the "Controller Configuration" screen the remote controller can be configured.
TIP
The configurations can be stored to two separate profiles, named "yellow" and "red". A
profile can be configured regardless of whether it is currently active or not.
Access The "Controller Configuration" screen can be accessed via the [Controller Configuration]
button on the "Navigation" screen.
Controls
Figure 27 "Controller Configuration" screen
1 Remote controller status Read out remote controller status
section
2 [Disconnect Controller] Unpair / remove remote controller from device
3 Button function fields (stepwise Select stepwise movement function for the respective
movement) remote controller button
4 [Back to Navigation] Open "Navigation" screen
5 Button function fields Select continuous movement function for the respective
(continuous movement) remote controller button
6 Remote controller with profile Read out the profile currently selected for controlling via
indicator (light bars) the color-coded light bars
7 [Reset all profiles] Reset all configurations in all profiles to delivery status
8 [Profile to edit] field Select profile to be configured

Page 44 | Graphical User Interfaces
5.3 Touch Panel Application
The device's touch panel (Figure 2/1) serves as the interface of the device-internal touch panel
application for controlling the device. The remote control can also be configured with the
touch panel application.
NOTE
The touch panel can be damaged if it is touched with anything but the fingers or a suitable
pen.
TIP
A non-responding display can be refreshed by swiping down with the finger on the display.
A switched-off display can be switched on again by tapping anywhere on the display.
5.3.1 Page Composition
The touch panel application's pages have some common elements to be described below.
5.3.1.1 Overview
The screen of the touch panel is divided into the following sections.
Controls
Figure 28 Touch panel screen sections
1 Header Switch between pages
2 Control section Control device and read out information
3 Remote controller status bar Read out remote controller status (see below)
4 Locking bar Lock and unlock the touch panel (see below)
5 [Info] Open the "Version" overlay (see below)

|     |     |     | Graphical User Interfaces  | |  Page 45  |
| --- | --- | --- | -------------------------- | ----------- |
5.3.1.2 Remote Controller Status Bar
The remote controller status bar provides information about the connection and the charging
status of the remote controller.
Controls

Figure 29 Remote controller status bar
1  Connection status display  Read out connection status, see table below
2  Battery status display  Read out battery charge level (if connected)
3  Bluetooth status display  Read out Bluetooth status, see table below

| Connection status  | Status  | Description  |     |     |
| ------------------ | ------- | ------------ | --- | --- |
Controller connected and  Remote controller is connected via USB or Bluetooth and
|     | enabled  | recognized by the software  |     |     |
| --- | -------- | --------------------------- | --- | --- |
Controller not connected  Remote controller not recognized by the software of the
AMC300

| Bluetooth status  | Status               | Description                                    |     |     |
| ----------------- | -------------------- | ---------------------------------------------- | --- | --- |
|                   | Not available        | No Bluetooth adapter connected to the device   |     |     |
|                   | Waiting for pairing  | Connected, ready for pairing                   |     |     |
|                   | Pairing…             | Pairing in progress                            |     |     |
Not connected  Device is paired with a remote controller, but Bluetooth
connection is interrupted (e.g. remote controller out of reach)
|     | Connecting…  | Connecting in progress  |     |     |
| --- | ------------ | ----------------------- | --- | --- |
Connected  The remote controller is connected to the device via Bluetooth
|     |     |     |     |     |
| --- | --- | --- | --- | --- |

Page 46 | Graphical User Interfaces
5.3.1.3 Locking Bar
Via the locking bar you can deactivate or lock the display, to prevent any values from being
changed unintentionally.
Controls
Figure 30 Locking bar
1 Display locking control, Lock touch panel
unlocked
2 Display activation control Switch off display
3 Display locking control, locked Unlock touch panel
4 Control section, locked

Graphical User Interfaces | Page 47
5.3.1.4 "Version" Overlay
The "Version" overlay provides you with comprehensive information about the device and its
current firmware version. It also enables you to reboot the device or to reset it without the
need for a PC being connected. The network settings can also be adjusted here.
Access The "Version" overlay can be accessed from every page by tapping [Info] (Figure 28/5).
Controls
Figure 31 "Version" overlay
1 "Version" section Read out device information
2 [Factory reset] Restore factory settings (see 11.3.3)
3 [System reboot] Reboot device
4 [Change IP] Open the "Networking" overlay

Page 48 | Graphical User Interfaces
5.3.1.5 Numerical Input Overlay
The numerical input overlay always appears when a field for numerical input is touched.
Controls
Figure 32 Numerical input field, example: target position setting
1 Numeric keys Type in numerical values
2 Parameter display Read out parameter to be adapted and its current value
3 [←] Delete last digit
4 [C] Delete entire input
5 [x] Discard input and close overlay
6 [✓] Confirm input and close overlay
5.3.2 "Main" Page
The "Main" page is the page where the actual positioning process takes place. It displays the
parameter values of each axis in a row and allows you to adapt these values.
Access The "Main" page can be accessed via the [Main] button in the application's header.

Graphical User Interfaces | Page 49
5.3.2.1 Overview
Figure 33 "Main" page
1 "Axis" column Read out axis' number and open the axis' settings
2 "Mode" column Read out and adapt axis' controlling status, see below
3 "Position" column Read out and adapt axis position (adapting only in closed
loop mode), see section 8.6
4 "Preset" column Read out and adapt preset axis parameter profile, see
sections 8.4.2 and 8.5.1
5 "Step" column Set the number of steps carried out with each stepwise
move, see sections 8.4.2
An axis with connected positioner can be activated by pressing the "Mode" symbol in the
corresponding row for more than 1 second.
5.3.2.2 Connection and Control Mode Indicators
On the "Mode" and the "Position" column of an axis you can read out the connection and
control status of the axis.
The available options are displayed in the following table.
Controls Description
No positioner is connected.
A positioner is connected, but controlling is not activated
for this axis.
A positioner is connected and controlling is activated. The
control mode is closed loop positioning.
A positioner is connected and controlling is activated. The
control mode is open loop positioning.
TIP
The color of the current position provides additional information to simplify your work.

Page 50 | Graphical User Interfaces
5.3.2.3 "Position" Column, Closed Loop Control
In the closed loop control mode the "Position" column allows not only to read out the current
position, but also to adapt it.
Controls
Figure 34 Axis row, positioning controls in closed loop mode
1 Row of an axis not in motion
2 Row of an axis in motion
3 Target field Open numerical input overlay to enter target position
4 "Start moving" button Start moving to target position
5 "Stop moving" button Stop at current position
6 "Current position" display Current axis position
5.3.2.4 "Preset" Column
By tapping on the "Preset" column of an axis you can select one of three preset combination of
values for amplitude, frequency and target range. The values of the selected set are applied to
the axis.
The preset designations correspond to typical use cases and are as follows:
- LT – low temperature use
- RT – room temperature use
- CC – custom configuration
TIP
The preset values can be adapted individually on the "Axis Settings" page, see 5.3.4.

Graphical User Interfaces | Page 51
5.3.3 "Axis Overview" Page
The "Axis Overview" page provides an additional way to access the settings of an axis.
Access The "Axis Overview" page can be accessed via the [Axis Overview] button in the application's
header.
Controls
Figure 35 "Axis Overview" page
The settings page of an axis can be opened by tapping on the respective axis' button.
5.3.4 "Axis Settings" Page
The "Axis Settings" page provides different controls to adjust motion parameters or general
axis parameters. The motion parameters are arranged as profiles, i.e. sets of settings which can
be adapted to the axis as a whole.
TIP
The axis profile can be changed in the respective axis row on the "Main" page (Figure 33/4).
Access The "Axis Settings" page can be accessed by tapping on the respective axis' number on the
"Main" page (Figure 33/1), or by tapping on the axis' button on the "Axis Overview" page
(Figure 35).

Page 52 | Graphical User Interfaces
Controls
Figure 36 "Axis Settings" page
1 Axis number field Switch axis
2 "Positioner" field Select type of connected positioner
3 "Current" column Read out values currently applied to the selected axis
4 "LT" profile column Open the numerical input overlay to adapt the preset's
respective value
5 Positioner status Read out the current axis status
6 "RT" profile column Open the numerical input overlay to adapt the preset's
respective value
7 "CC" profile column Open the numerical input overlay to adapt the preset's
respective value
8 [Enable Axis] Activate or deactivate selected axis
9 [Enable Sensor] Activate or deactivate position feedback (/RES positioner
required
10 [Ground Axis] Ground positioner
11 [Apply] Save all changes

Graphical User Interfaces | Page 53
5.3.5 "Controller Config" Page
On the "Controller Config" page the remote controller can be configured.
TIP
The configurations can be stored to two separate profiles, named "yellow" and "red". A
profile can be configured regardless of whether it is currently active or not.
Access The "Controller Config" page can be accessed via the [Controller Config] button in the
application's header.
Controls
Figure 37 "Controller Config" page
1 Button function fields (stepwise Select stepwise movement function for the respective
movement) remote controller button
2 Button function fields Select continuous movement function for the respective
(continuous movement) remote controller button
3 [Profile to edit] field Select profile to be configured
4 [Reset all profiles] Reset all configurations in all profiles to delivery status
5 [Remove Controller] Unpair / remove remote controller from device

Page 54 | Graphical User Interfaces
5.3.6 "Diagnostic Tools" Page
On the "Diagnostic Tools" page you can measure the performance of the connected
positioners.
Access The "Diagnostic Tools" page can be accessed via the [Diagnostic Tools] button in the
application's header.
Controls
Figure 38 "Diagnostic Tools" page
1 "Axis" column Read out number of the axis to be tested
2 [Start] Start measuring capacitance, resistance and power for the
respective axis
3 "C" column Read out last measured capacitance value of the respective
axis
4 "R" column Read out last measured resistance value of the respective axis
5 "Temperature" column Read out device temperature

Device Setup | Page 55
6 Device Setup
6.1 Unpacking and Positioning
1. Carefully unpack the device and its accessories.
2. Inspect the device and the accessories for any damage. Contact attocube in case of any
detected damage.
3. Place all components on a flat and clean surface.
NOTE
Inadequate positioning may lead to malfunctions or damage the device.
o Position the device in such a way that the it can easily be disconnected from the
mains supply.
o Do not obscure the ventilation slots. Make sure that proper airflow is maintained to
the unit.
o Observe the operation requirements specified in section 4.4.
6.2 Mounting the Rack and Double Rack Device
NOTE
If handled by only one person, the device might fall and be damaged.
o Always work in pairs when installing the device.
1. Grab the device at its handles and attach it to the rack, matching its screw holes
(Figure 39/1) to the threaded holes in the rack.
Figure 39 Mounting the rack device

Page 56 | Device Setup
2. Screw in the device's fixing screws (Figure 39/2) at their designated positions
(Figure 39/1).
6.3 Connecting to Voltage Supply
CAUTION
Wrong cabling!
Inadequate equipment may cause electric shocks or fire.
o Always use power supply cables provided by attocube!
1. Connect the power cable to the mains supply socket.
2. Connect the power cable to the device's power supply socket.
TIP
The sockets for outgoing voltage (Figure 5/7-9) are insulated and do not conduct power
unless there are positioners connected.
6.4 Connecting to PC via USB
✓ The PC fulfills the requirements specified in section 4.6.
✓ You are logged in to the PC with administrator rights.
1. Plug in the USB connector of the USB-to-Ethernet adapter (part of the delivery) into the
USB port of your PC.
→ The driver is installed automatically.
2. Plug in the connector of the Ethernet cable into the corresponding socket at the adapter.
3. Plug in the opposite connector of the Ethernet cable into the device's Ethernet uplink
socket (Figure 5/2).
You can connect several AMC300 devices to the PC via USB. Therefore, an Ethernet switch
must be interposed between the USB-to-Ethernet adapter and the devices. An Ethernet switch
is not part of the delivery.
6.5 Connecting to Network
6.5.1 Establishing the Cable Connection
✓ The PC fulfills the requirements specified in section 4.6.
1. Plug the connector of the Ethernet cable into the Ethernet socket of your PC or of the
respective LAN router.
2. Plug the opposite connector of the Ethernet cable into the device's Ethernet uplink socket
(Figure 5/2).
You can connect several AMC300 devices to the network via separate Ethernet cables or by
interposing an Ethernet switch between PC / router and the devices. An Ethernet switch is not
part of the delivery.

Device Setup | Page 57
Alternatively, you can daisy-chain the network devices, connecting them via their Ethernet
uplink and downlink (Figure 5/3) sockets.
TIP
The use of the device's Ethernet downlink socket requires the /PRO upgrade.
6.5.2 Configuring the Network Settings
If you are not using the device as DHCP server, its IP address and the network configuration
must be adapted, to operate the device within a LAN.
NOTE
Assigning an unavailable IP address or one which has already been assigned to another
device, will cause networking problems.
o Make sure the chosen IP address is available for your network and is not already in
use.
WebApp ✓ The PC fulfills the requirements specified in section 4.6.
✓ PC and device are connected to the same LAN.
✓ The "Configuration" screen is opened, see section 5.2.2.
1. Navigate to the "Networking" section and select Static configuration or DCHP
from the "IP Mode" field (Figure 20/1).
→ Additional controls become available.
2. Adapt the values in the fields of the "Networking" section to your network specification.
3. Click on [Apply].
Touch panel ✓ The "Version" overlay is opened, see section 5.3.1.
1. Tap on [Change IP] (Figure 31/5).
→ The "Networking" overlay opens.
2. Tap into the field, the value of which you want to adapt.
3. Adapt the value to your network specification and confirm the upcoming prompt.
→ A pen symbol behind the "Networking" overlay's respective field indicates that the
value has been adapted.
4. If required, adapt further networking settings accordingly.
5. Tap on [Apply].

Page 58 | Device Setup
6.6 Connecting Remote Controller
The remote controller can be connected to the device via USB or wirelessly via Bluetooth.
6.6.1 Establishing a Cable Connection
1. Plug the USB-micro-B connector of the USB cable (part of the delivery) into the remote
controller's USB socket.
2. Plug the USB-A connector of the cable into the device's USB socket (Figure 5/4).
6.6.2 Establishing a Wireless Connection
o Plug the Bluetooth receiver (part of the delivery) into the device's USB socket (Figure 5/4).
6.6.3 Pairing Remote Controller and Device
TIP
Pairing is not required when the remote controller is connected via cable.
✓ A wireless connection between the device and the remote controller has been established.
✓ The device is switched on.
✓ The remote controller is switched off.
✓ The Bluetooth receiver connected to the device's USB socket lights blue.
1. Simultaneously hold the remote controller's [SHARE] (Figure 6/3) and PS button
(Figure 6/11) until the light bar on the controller's back (Figure 6/4) starts blinking rapidly.
→ The Bluetooth status display (Figure 29/3) on the touch panel shows the status
Pairing.
2. Verify that the Bluetooth status display shows the message Connected.
TIP
The pairing has to be done only once. The device will remember the paired controller until a
firmware reset is done.
Note that only one controller can be paired with the device at a time. If you want to pair
another controller with the device, you will have to discard the current pairing connection, see
section 6.6.4.

Device Setup | Page 59
6.6.4 Discarding the Pairing Connection
As only one remote controller can be paired with the device at a time, the pairing connection
of a connected remote controller must be discarded before another controller can be paired
with the device.
WebApp ✓ The "Controller Configuration" screen is opened.
o Click on [Disconnect Controller] (Figure 27/2).
→ The current pairing connection is discarded.
Touch panel ✓ The "Controller Config" page is opened.
o Tap on [Remove Controller] (Figure 37/8).
→ The current pairing connection is discarded.
6.6.5 Switching off the Remote Controller
The remote controller can be switched off by pressing the PS button for 10 seconds.
6.7 Configuring Remote Controller
The keys of the remote controller can be assigned functions according to your individual
controlling preferences.
TIP
The profile activated for controlling is independent from the profile that is selected for
configuration. You might, e.g. configure profile red while profile yellow is active for
controlling.
WebApp ✓ The remote controller is connected and paired with the device, see section 6.6.
✓ The "Navigation" screen is opened, see section 5.2.1.
1. Click on [Controller Configuration].
→ The "Controller Configuration" screen opens.
2. Tap on [Profile to edit].
3. From the drop-down menu, select the profile to be configured.
4. Click on the field corresponding to the button you want to assign a function to.
5. From the drop-down menu, select the desired function.
→ The configuration takes effect immediately. For testing, the configured profile must
be also active for controlling.

Page 60 | Device Setup
Touch panel ✓ The remote controller is connected and paired with the device, see section 6.6.
✓ The "Controller Config" page is opened, see section 5.3.5.
1. Tap on [Profile to edit].
2. From the drop-down menu, select the profile to be configured.
3. Tap on the field corresponding to the button you want to assign a function to.
4. From the drop-down menu, select the desired function.
→ The configuration takes effect immediately. For testing, the configured profile must
be also active for controlling.
6.8 Connecting Positioner
CAUTION
Wrong connection!
Inadequate connections may cause injury and are likely to damage the device or interfere
with an appropriate functioning.
o When connecting the device to customer hardware, carefully take note of the
warnings and specifications given in section 13!
1. Plug in the positioner control cable into the positioner's connector or the vacuum
feedthrough's socket, accordingly.
TIP
Use the test adapter to directly connect a positioner control cable to a positioner for
vacuum use.
2. Plug in the D-Sub connector of the positioner control cable into one of the corresponding
sockets at the device (Figure 5/7, 8, 9).
6.9 Disconnecting Positioner
CAUTION
Risk of electric shock
Contact with live connectors can cause injuries or material damage.
o Always deactivate an axis before disconnecting the corresponding positioner!
A positioner can be disconnected at any time in the process, e.g. for changing positioners to be
controlled by the device.
✓ The respective axis is deactivated, see section 8.3.
o To disconnect a positioner, unplug the positioner control cable from the device or from
the positioner's socket.

Device Setup | Page 61
6.10 Installing the attoDISCOVERY Software
✓ You are logged in to the PC with administrator rights.
1. Connect the USB flash drive contained in the scope of delivery to your PC.
2. Open a file explorer window and navigate to the USB flash drive's folder.
3. Double-click on the installation file fitting your operating system (.exe for Windows,
.deb for Linux).
4. Follow the instructions of the installation wizard.
TIP
When the software is started for the first time, a folder named attocube containing a file
named staticDevices.json is created in your user's folder at the PC.
In this file you can specify IP addresses of controllers that will automatically be connected,
even if they are not directly connected to the PC's network subnet.

Page 62 | Device Start-Up
7 Device Start-Up
7.1 Switching On the Device
o Press the device's power button (Figure 2/2 or Figure 3/2, respectively).
o Start up your PC.
7.2 Switching On the Remote Controller
o Press the remote controller's PS button (Figure 6/2) shortly, until the light bar on the
controller's back (Figure 6/4) turns on.
NOTE
If the remote controller is not charged it might turn off immediately after connecting.
o Regularly check the remote controller's charging status at the touch panel's remote
controller status bar.
o Make sure the remote controller is always sufficiently charged.
o For charging, connect the remote controller to any USB power supply via USB
cable.
TIP
If connected to the device via USB cable for charging, the remote controller can
simultaneously be used for controlling.

Operation | Page 63
8 Operation
In the course of this section, instructions on the fulfillment of some typical application tasks are
given.
TIP
For a concise description of all of the device's controlling functions, see section 0.
8.1 Restoring Former Axis Selection
When starting the software, attoDISCOVERY automatically checks the connected networks for
devices (identified by serial number) that were also connected when the software ran the last
time. If so, the "Restore Selection" dialog opens.
The "Restore Selection" dialog allows you to comfortably restore the last axis selection, i.e. the
axes to be controlled.
TIP
Make use of the "Restore selection" option if you repeatedly use the axes in the same
setting, e.g. a constant experimental arrangement.
attoDISCOVERY ✓ The "Restore Selection" dialog is opened after software start.
Figure 40 "Restore Selection" dialog
o To restore the last axis selection, click [Ok] (Figure 40/1).
o To discard the last axis selection, click [Cancel] (Figure 40/2).

Page 64 | Operation
8.2 Labeling Entities
The options to label devices and axes provide a way to increase transparency, especially when
working with the same experimental arrangements over larger periods of time or with varying
personnel.
8.2.1 Labeling Device
attoDISCOVERY ✓ The "Find Devices" screen is opened, see section 5.1.1.
1. At the respective controller tile, click on the controller name field (Figure 11/2).
2. Type in the device name of your choice.
3. Click on [Apply].
→ The settings are saved.
WebApp ✓ The "Configuration" screen is opened, see section 5.2.2.
1. In the "Device Name" section, click on the "Device Name" field (Figure 21/1).
2. Type in the device name of your choice.
3. Click anywhere else on the "Configuration" screen or press [Enter].
→ The settings are saved.
8.2.2 Labeling Axes
TIP
Make use of the axis labeling option to secure transparency of the axis' assignments (e.g. to
the positioning dimension) over time and personnel changes.
NOTE
The axis connected to a device must have different names.
attoDISCOVERY ✓ The "Find Devices" screen is opened, see section 5.1.1.
1. At the respective controller tile, click on the name field of the axis to be labeled
(Figure 11/5).
2. Type in the axis name of your choice.
3. Click on [Apply].
→ The settings are saved.
WebApp ✓ The "Configuration" screen is opened, see section 5.2.2.
1. In the "Device Name" section, click on the name field of the axis to be labeled
(Figure 21/2).
2. Type in the axis name of your choice.
3. Click anywhere else on the "Configuration" screen or press [Enter].
→ The settings are saved.

Operation | Page 65
8.3 Activating and Deactivating Axis
Before you can control and configure an axis you have to activate it. An axis must always be
deactivated before the corresponding positioner is disconnected or the device is switched off.
NOTE
Under rare circumstances, it is possible that older positioners of attocube's industrial line
are not detected properly by the device, regardless of their physical connection status.
o Contact the attocube support, if a connected positioner is not detected by the
device.
attoDISCOVERY ✓ The "Operation" screen is opened, see section 5.1.2.
o To activate an axis, check the axis activation checkbox (Figure 13/1) of the corresponding
axis tile.
→ The axis is activated.
o To deactivate an axis, uncheck the axis activation checkbox (Figure 13/1) of the
corresponding axis tile.
→ The axis is deactivated.
WebApp ✓ The "Navigation" screen is opened, see section 5.2.1.
o To activate an axis, check the axis activation checkbox (Figure 16/1) of the corresponding
axis tile.
→ The axis is activated.
o To deactivate an axis, uncheck the axis activation checkbox (Figure 16/1) of the
corresponding axis tile.
→ The axis is deactivated.
Touch panel ✓ The "Main" page is opened, see section 5.3.2.
o To activate an axis, press the "Mode" field of the corresponding axis' row for more than
1 second (Figure 33/2).
→ The axis is activated.
o To deactivate an axis, press the "Mode" field of the corresponding axis' row for more than
1 second (Figure 33/2).
→ The axis is deactivated.

Page 66 | Operation
8.4 Configuring Axis
8.4.1 Specifying Positioner Type
In order to "tell" the device e.g. whether movements are linear or rotational etc. you always
have to specify the positioner type after connecting a positioner.
TIP
Per default an ANPx101 positioner is selected.
attoDISCOVERY ✓ The "Operation" screen is opened, see section 5.1.2.
✓ The axis tile's configuration view is opened.
1. Click on the "Positioner" field (Figure 14/3).
2. From the drop-down menu, select the desired positioner type.
WebApp ✓ The "Navigation" screen is opened, see section 5.2.1.
✓ The axis tile's configuration view is opened.
1. Click on the "Positioner" field (Figure 17/3).
2. From the drop-down menu, select the desired positioner type.
Touch panel ✓ The "Axis Settings" page of the respective axis is opened, see section 5.3.4.
1. Tap on the "Positioner" field (Figure 36/2).
2. From the drop-down menu, select the desired positioner type.
8.4.2 Adjusting Axis Parameters
The device allows you to adjust various parameters of your positioning tasks, always depending
on the active control mode and the activated features.
Examples for adjustable actuator parameters are:
- the number of steps that are implemented with each stepwise move (/PRO upgrade
required)
- the range in which a positioner is regarded as "in target"
- whether the positioner stops the attempt to move when it is confronted with physical
obstacles
- whether the positioner is grounded when it is in the defined target range
Adjustable sensor parameters are:
- the sensor activity itself
- the sensor's feedback power

Operation | Page 67
attoDISCOVERY ✓ The "Operation" screen is opened, see section 5.1.2.
✓ The axis tile's configuration view is opened.
1. Click on the field, the value of which you want to adapt.
2. Select or type in the desired value.
3. Click anywhere else on the axis tile.
→ The settings are saved.
WebApp ✓ The "Navigation" screen is opened, see section 5.2.1.
✓ The axis tile's configuration view is opened.
1. Click on the field, the value of which you want to adapt.
2. Select or type in the desired value.
3. Click anywhere else on the axis tile.
→ The settings are saved.
Touch panel ✓ The "Main" page is opened, see section 5.3.2.
✓ The respective axis is activated.
1. To change the steps applied with a stepwise move, tap various times on the "Step" field of
the axis' row (Figure 33/5).
TIP
The possible values for "Step" are 1, 10 and 100.
2. To change further parameters, tap on the "Axis" field in the axis' row (Figure 33/1).
→ The "Axis Settings" page opens.
3. To activate or deactivate the sensor, tap on [Enable Sensor] (Figure 36/9).
→ The button's indicator changes its color (green: activated, red: deactivated).
4. To ground the axis on target, tap on [Ground Axis] (Figure 36/10).
→ The button's indicator changes its color (green: activated, red: deactivated).
3. To adapt the target range, tap on the "Target range" field of desired profile's column
(Figure 36/4, 6, 7).
→ The numerical input overlay opens.
4. Type in the desired target range value and confirm (Figure 32/6).
5. Tap on [Apply] (Figure 36/11).
→ The settings are saved.
6. To change the active preset, tap on [Main] in the application's header (Figure 28/1).
→ The "Main" page opens.
7. Tap various times on the "Preset" field of the axis' row (Figure 33/4), until the desired
preset value appears.
TIP
The possible values for "Preset" are LT, RT and CC.

Page 68 | Operation
8.4.3 Loading Standard Axis Parameters
attoDISCOVERY ✓ The "Operation" screen is opened, see section 5.1.2.
✓ The axis tile's configuration view is opened.
1. Click on the "Configuration Upload" button (Figure 14/8).
→ A file explorer opens.
2. Navigate to the desired configuration file's folder.
3. Click on the file and confirm.
→ The axis configuration is uploaded and applied.
WebApp ✓ The "Navigation" screen is opened, see section 5.2.1.
✓ The axis tile's configuration view is opened.
1. Click on the "Configuration Upload" button (Figure 17/8).
→ A file explorer opens.
2. Navigate to the desired configuration file's folder.
3. Click on the file and confirm.
→ The axis configuration is uploaded and applied.

Operation | Page 69
8.5 Open loop Positioning
The open loop positioning mode operates without position feedback from the positioner.
The position on the axis can be varied without any absolute position information. Motion
aspects like speed and step size depend on the physical motion parameters you set for the
movement.
TIP
For additional information on the motion-related significance of amplitude and frequency,
consult the positioner's manual.
8.5.1 Adjusting Motion Parameters
attoDISCOVERY ✓ The "Operation" screen is opened, see section 5.1.2.
✓ The respective axis is activated (required only for DC value adjustment), see section 8.3.
✓ The axis tile's operation view is opened.
1. To adapt the step size, type in the desired value into the amplitude setting field
(Figure 13/5).
2. To adapt the step repetition rate, type in the desired value into the frequency setting field
(Figure 13/6).
3. To set the DC value for manual position adjustment, type in the desired value into the DC
value setting field (Figure 13/7).
4. Click anywhere else on the axis tile.
→ The settings are saved.
WebApp ✓ The "Navigation" screen is opened, see section 5.2.1.
✓ The respective axis is activated (required only for DC value adjustment), see section 8.3.
✓ The axis tile's operation view is opened.
1. To adapt the step size, type in the desired value into the amplitude setting field
(Figure 16/5).
2. To adapt the step repetition rate, type in the desired value into the frequency setting field
(Figure 16/6).
3. To manually adjust the position, type in the desired value into the DC value setting field
(Figure 16/7).
4. Click anywhere else on the axis tile.
→ The settings are saved.
Touch panel ✓ The "Axis Settings" page of the respective axis is opened, see section 5.3.4.
1. To adapt the step size, tap on the "Amplitude" field of the desired profile's column
(Figure 36/4, 6, 7).
→ The numerical input overlay opens.
2. Type in the desired amplitude value and confirm (Figure 32/6).
3. To adapt the step repetition rate, tap on the "Frequency" field of the desired profile's
column (Figure 36/4, 6, 7).
→ The numerical input overlay opens.

Page 70 | Operation
4. Type in the desired frequency value and confirm (Figure 32/6).
5. Tap on [Apply] (Figure 36/11).
→ The settings are saved.
6. To change the active preset, tap on [Main] in the application's header (Figure 28/1).
→ The "Main" page opens.
7. Tap various times on the "Preset" field of the axis' row (Figure 33/4), until the desired
preset value appears.
TIP
The possible values for "Preset" are LT, RT and CC.
8.5.2 Controlling Movements
attoDISCOVERY ✓ The "Operation" screen is opened, see section 5.1.2.
✓ The respective axis is activated, see section 8.3.
✓ The axis tile's operation view is opened.
o Click on the open loop positioning controls (Figure 13/4) to initiate or stop a movement.
WebApp ✓ The "Navigation" screen is opened, see section 5.2.1.
✓ The respective axis is activated, see section 8.3.
✓ The axis tile's operation view is opened.
o Click on the open loop positioning controls (Figure 16/4) to initiate or stop a movement.
Remote controller ✓ The remote controller is connected and paired with the device, see section 6.6.
✓ Movement commands for the respective axis have been assigned to remote controller
keys, see section 6.7.
o Press the remote controller keys assigned to the axis to initiate or stop a movement.

Operation | Page 71
8.6 Closed Loop Positioning
The closed loop positioning mode operates with active position feedback from the positioner.
NOTE
Closed loop positioning is only available for positioners with /RES encoding.
Refer to the specification sheets of the positioner for information on the motion
specifications in closed loop mode.
8.6.1 Activating Closed Loop Positioning
To perform positioning, the corresponding controls must be activated first.
attoDISCOVERY ✓ The "Operation" screen is opened, see section 5.1.2.
✓ The respective axis is activated, see section 8.3.
✓ The axis tile's operation view is opened.
o Click on [Closed Loop Functions] (Figure 13/8).
→ The closed loop positioning controls are expanded.
WebApp ✓ The "Navigation" screen is opened, see section 5.2.1.
✓ The respective axis is activated, see section 8.3.
✓ The axis tile's operation view is opened.
o Click on [Closed Loop Functions] (Figure 16/8).
→ The closed loop positioning controls are expanded.
Touch panel ✓ The "Main" page is opened, see section 5.3.2.
✓ The respective axis is activated, see section 8.3.
o Tap on [Closed Loop] in the axis row's "Mode" column (Figure 33/2).
→ The "Closed Loop" icon lights up.
8.6.2 Moving Defined Distances
attoDISCOVERY ✓ The "Operation" screen is opened, see section 5.1.2.
✓ The respective axis is activated, see section 8.3.
✓ The axis tile's operation view is opened.
✓ Closed loop positioning is activated, see section 8.6.1.
1. Into the distance field (Figure 13/11), type in the desired absolute movement distance (in
µm).
o To move the defined distance in positive direction, click on [+] (Figure 13/12).
o To move the defined distance in negative direction, click on [-] (Figure 13/10).

Page 72 | Operation
WebApp ✓ The "Navigation" screen is opened, see section 5.2.1.
✓ The respective axis is activated, see section 8.3.
✓ The axis tile's operation view is opened.
✓ Closed loop positioning is activated, see section 8.6.1.
1. Into the distance field (Figure 16/11), type in the desired absolute movement distance (in
µm).
o To move the defined distance in positive direction, click on [+] (Figure 16/12).
o To move the defined distance in negative direction, click on [-] (Figure 16/10).
8.6.3 Moving to Defined Target
attoDISCOVERY ✓ The "Operation" screen is opened, see section 5.1.2.
✓ The respective axis is activated, see section 8.3.
✓ The axis tile's operation view is opened.
✓ Closed loop positioning is activated, see section 8.6.1.
1. Into the target field (Figure 13/14), type in the desired target position (in µm).
2. Click on the "Move to target" button (Figure 13/13).
→ The positioner is moved to the defined target position.
WebApp ✓ The "Navigation" screen is opened, see section 5.2.1.
✓ The respective axis is activated, see section 8.3.
✓ The axis tile's operation view is opened.
✓ Closed loop positioning is activated, see section 8.6.1.
1. Into the target field (Figure 16/14), type in the desired target position (in µm).
2. Click on the "Move to target" button (Figure 16/13).
→ The positioner is moved to the defined target position.
Touch panel ✓ The "Main" page is opened, see section 5.3.2.
✓ The respective axis is activated, see section 8.3.
✓ Closed loop positioning is activated, see section 8.6.1.
1. Tap on the axis' target field (Figure 34/3).
→ The numerical input overlay opens.
2. Type in the desired target position (in µm) and confirm (Figure 32/6).
→ The settings are saved.
3. Tap on the "Start moving" button (Figure 34/4).
→ The positioner is moved to the defined target position.
4. If required, tap on the "Stop moving" button (Figure 34/5), to interrupt the movement.
→ The positioner's movement is stopped.

Device Shut-Off | Page 73
9 Device Shut-Off
9.1 Switching Off the Remote Controller
o Press and hold the remote controller's PS button (Figure 6/2), until the light bar on the
controller's back (Figure 6/4) turns off.
9.2 Switching Off the Device
TIP
To allow an independent functioning of the device (e.g. for automated experimental
arrangements), the device works properly even when the software is closed.
CAUTION
Risk of electric shock
Contact with power guiding connectors can cause injuries or material damage.
o Always deactivate all axes before shutting off the device.
✓ All axes are deactivated, see section 8.3.
1. Close the PC-based device control software applications.
2. Press the device's power button (Figure 2/2 or Figure 3/2, respectively).
→ The device is switched off.

Page 74 | Update, Upgrade and Maintenance
10 Update, Upgrade and Maintenance
All update, upgrade and maintenance procedures are carried out in the webserver application.
NOTE
There are no user serviceable parts inside the controller!
NOTE
Please refer to the manual of the remote controller for information on its maintenance
requirements.
10.1 Adding Private Key and Certificate
The device is provided with a proper certificate for secure access over HTTPS. However, you
can also add your own private key and a certificate to be used for HTTPS communication.
NOTE
It is recommended to upload your private key over a SSL connection secured by the
attocube certificate. This pre-installed certificate is self-signed and will cause a warning
message issued by the browser. Confirm this warning.
NOTE
The private key and the certificate must be uploaded in the PEM format. Otherwise they
might not be applied and your device might not be accessible via HTTPS.
o Before uploading, double check if key and certificate are in the correct format.
✓ The webserver application's "Configuration" screen is opened.
1. Navigate to the "Secure Access over HTTPS" section.
2. Copy the private key (in PEM format) to the clipboard.
Figure 41 "Configuration" screen, "Secure Access over HTTPS" section
3. Click on the "Private Key" field (Figure 41/1) and paste the clipboard contents.
4. Copy the certificate (in PEM format) to the clipboard.
5. Click on the "Certificate" field (Figure 41/2) and paste the clipboard contents.
6. Click on [Apply] (Figure 41/3).
→ The key and the certificate are uploaded and applied.
7. To test the key, try to establish a HTTPS connection.

Update, Upgrade and Maintenance | Page 75
10.2 Updating Firmware
attocube provides occasional updates in the form of image files. The files are delivered in a zip
folder. attocube informs you when an update for your device is available.
NOTE
Unauthorized updates can lead to a permanent malfunction and are not covered by
attocube's warranty.
o Contact attocube for technical support, before updating the device firmware.
✓ The update file has been downloaded, unpacked from the zip folder and stored to your PC.
✓ The webserver application's "Configuration" screen is opened.
1. Navigate to the "Firmware Update" section.
Figure 42 "Configuration" screen, "Firmware Update" section
2. Click on the browse button (Figure 42/2).
→ A file explorer window is opened.
3. Navigate to the update file's folder.
4. Select the file ending on ".image" and click [Open].
→ The file is uploaded and its name is displayed in the file name field (Figure 42/1).
→ After the successful upload additional controls are displayed.
NOTE
It is essential to the update process that the device is constantly connected to the PC during
the reboot!
o Do not disconnect the device until the connection to the webserver application is
established again.
5. Click on [Install & Reboot].
→ The update is installed and the device is rebooted.

Page 76 | Update, Upgrade and Maintenance
10.3 Upgrading Device
To increase your performance using the AMC300, attocube provides you with additional
features and upgrades. License files are delivered for this purpose.
TIP
Contact attocube for available upgrades.
✓ The license file has been downloaded and stored to your PC.
✓ The webserver application's "Configuration" screen is opened.
1. Navigate to the "Feature Upgrade" section.
Figure 43 "Configuration" screen, "Feature Upgrade" section
2. Click on the browse button (Figure 43/2).
→ A file explorer window is opened.
3. Navigate to the license file's folder.
4. Select the file ending on ".gpg" and click [Open].
→ The file is uploaded and its name is displayed in the file name field (Figure 43/1).
→ After the successful upload additional controls are displayed.
NOTE
It is essential to the upgrade process that the device is constantly connected to the PC
during the reboot!
o Do not disconnect the device until the connection to the webserver application is
established again.
5. Click on [Install & Reboot].
→ The upgrade is installed and the device is rebooted.

Troubleshooting | Page 77
11 Troubleshooting
NOTE
Unauthorized error handling may result in permanent malfunction and is not covered by
attocube's warranty.
o Do not take any action not proposed for troubleshooting in this document.
o If problems occur that are not mentioned in this section, contact attocube for help.
o If the problems cannot be solved by the proposed action, contact attocube for
help.
11.1 Checking for Physical Network Connection
If no network connection between the device and the PC is established, check for the presence
of a physical network connection.
1. Make sure at least one minute has passed since the device's start up, so it had enough
time to boot. If still no connection is established, continue with step 2.
TIP
You can tell if the device boots from a short noise produced by its fan, approximately ten
seconds after start up.
2. If no /PRO features are active, make sure that the device's Ethernet uplink socket
(Figure 5/2) is used for connection.
3. Check if the indicator light next to the device's Ethernet socket is blinking.
o The device is connected to the PC via USB-to-Ethernet adapter and the indicator light
is not blinking: Continue with step 4.
o Else: Continue with step 5.
4. Disconnect the USB-to-Ethernet adapter from your PC and connect it again. If still no
connection is established, continue with step 5.
5. Reboot the device by switching it off and on again at the power button (Figure 2/2 or
Figure 3/2).
6. Check if a network connection is established after the reboot.
o A connection is established: If required, solve further problems according to section
11.2.
o No connection is established: Continue with section 11.3.

Page 78 | Troubleshooting
11.2 Physical Network Connection Present
Follow the instructions in this section to solve problems when the device is connected to the
network.
11.2.1 Accessing Webserver Application
If you cannot access to the device using the webserver application with the right IP address,
take the following steps until the problem is solved:
1. Try opening the webserver application with the latest version of Google Chrome or Mozilla
Firefox. If the problem is not solved, continue with step 2.
2. Erase the cookies and history of your web browser.
3. Try opening the webserver application. If the problem is not solved, continue with step 4.
4. Type in the device's serial number (without slashes) followed by .local into the
browser's address line. Press [Enter]. If the problem is not solved, continue with step 5.
5. Retrieve and, if required, adapt the network settings to make sure the device can be
reached via network. See section 11.3.
11.2.2 Resetting Device to Factory Defaults
You can reset the device to the factory defaults using the touch panel application or the
webserver application.
Touch panel ✓ The "Version" overlay is opened.
1. Tap on [Factory reset] (Figure 31/2).
→ The reset takes effect after the device's next boot.
2. Tap on [System reboot] (Figure 31/3).
→ The reboot is carried out and the factory default settings are restored.
WebApp ✓ The "About" screen is opened.
NOTE
Following the instructions of this section will delete your customized network configuration.
o For resetting the device without losing the network settings, use the touch panel
application or see section 11.3.3.
1. Click on [Factory Reset] (Figure 26/4).
→ A dialog window is opened.
2. Click on [OK] to confirm the reset.
→ The reset takes effect after the device's next boot.
3. Click on [System Reboot] (Figure 26/3).
→ A dialog window is opened.
4. Click on [OK] to confirm the reboot.
→ The reboot is carried out and the factory default settings are restored.

Troubleshooting | Page 79
11.3 Physical Network Connection Not Present
If no network connection to the device is available, a USB flash drive can be used to perform
some basic problem solving tasks.
NOTE
The USB flash drive must be FAT32-formatted.
11.3.1 Reading out Network Settings
✓ The FAT32-formatted USB flash drive is connected to your PC.
✓ The device is shut off.
1. On your PC, open a file explorer and navigate to the USB flash drive's root folder.
2. Create a new empty folder named attoDeviceIP.
3. Disconnect the flash drive from your PC and connect it to the device's USB socket
(Figure 5/4 or Figure 3/1).
4. Switch on the device by pressing its power button (Figure 2/2 or Figure 3/2).
→ A .json file containing the network information stored on the device is created.
5. When the booting is finished, disconnect the flash drive from the device and connect it to
the PC.
6. Open a file explorer, navigate to the flash drive's folder and open the folder
attoDeviceIP.
7. Open the file attoIPconfig.json with a plain text editor application.
8. Read out the network information from the file.
11.3.2 Adjusting Network Settings
This section instructs you how to adjust the network settings with no physical network
connection present.
TIP
The method described here can be used as fallback. A more straightforward way to adjust
the network settings directly at the device is provided by the touch panel application (see
section 6.5.2).
✓ The device's network settings have been read out, see section 11.3.2.
✓ The USB flash drive containing the device's network information is connected to your PC.
✓ The device is shut off.
1. Open a file explorer, navigate to the flash drive's folder and open the folder
attoDeviceIP.
2. Open the file attoIPconfig.json with a plain text editor application.
NOTE
The structure of the information contained in the file is essential to the further process.
o Make sure only to adapt variable values.
o Do not modify variable names or the syntax of the information.

Page 80 | Troubleshooting
3. Modify the network information contained in the file according to the desired settings.
Save and close the file.
4. Disconnect the flash drive from your PC and connect it to the device's USB socket
(Figure 5/4 or Figure 3/1).
5. Switch on the device by pressing its power button (Figure 2/2 or Figure 3/2).
→ The network settings are changed according to your adaptions.
11.3.3 Resetting Device to Factory Defaults
This section provides information on how to reset the device to the factory defaults using the
webserver application.
TIP
A more straightforward way to reset the device to the factory defaults (without the risk of
losing the network settings) is provided by the touch panel application (see section 11.2.2).
The first subsection instructs you on taking precautions to preserve the network settings when
a reset is performed. If preserving the device's network settings is not required you can skip
the first subsection.
11.3.3.1 Taking Precautions to Save Network Settings
✓ The FAT32-formatted USB flash drive is connected to your PC.
1. On your PC, open a file explorer and navigate to the USB flash drive's root folder.
2. Create a new empty folder named attoDeviceIP.
3. Continue with the next subsection.
→ The device's network information will be read out before the reset and be written to
the device when it is rebooted.
11.3.3.2 Resetting Device
✓ The FAT32-formatted USB flash drive is connected to your PC.
✓ The device is shut off.
1. On your PC, open a file explorer and navigate to the USB flash drive's root folder.
2. Create a new empty folder named attoreset.
3. Disconnect the flash drive from your PC and connect it to the device's USB socket
(Figure 5/4 or Figure 3/1).
4. Switch on the device by pressing its power button (Figure 2/2 or Figure 3/2).
→ The device is reset to the factory defaults.

Troubleshooting | Page 81
11.4 Measuring the Positioner Performance
In case a positioner or positioner cable damage is suspected, some significant aspects of the
positioner's performance can be measured.
attoDISCOVERY ✓ The "Operation" screen is opened, see section 5.1.2.
✓ The respective axis is activated, see section 8.3.
✓ The axis tile's operation view is opened.
✓ Closed loop positioning is activated, see section 8.6.1.
1. Click on [Diagnostic tools] (Figure 13/15).
→ The diagnostic tools controls are expanded.
2. Click on [Start] (Figure 13/16).
→ The measurement is carried out.
3. Read out the measured values from the "Positioner property display" section
(Figure 13/17).
WebApp ✓ The "Navigation" screen is opened, see section 5.2.1.
✓ The respective axis is activated, see section 8.3.
✓ The axis tile's operation view is opened.
✓ Closed loop positioning is activated, see section 8.6.1.
1. Click on [Diagnostic tools] (Figure 16/15).
→ The diagnostic tools controls are expanded.
2. Click on [Start] (Figure 16/16).
→ The measurement is carried out.
3. Read out the measured values from the "Positioner property display" section
(Figure 16/17).
Touch panel ✓ The "Diagnostic Tools" page is opened, see section 5.3.6.
✓ The respective axis is activated, see section 8.3.
1. In the row of the axis the positioner of which is to be measured, tap on [Start]
(Figure 38/2).
→ The measurement is carried out.
2. Read out the measured values from the measurement categories' respective columns.

Page 82 | Optional On-Device Features and Upgrades
12 Optional On-Device Features and
Upgrades
attocube offers various upgrades to facilitate and improve your work with the device.
TIP
Contact attocube for available features and upgrades.
12.1 Dual- and Tri-Channel Upgrades
The device's basic 'single-channel' version can be upgraded with the 'dual-channel' upgrade.
This upgrade allows you to simultaneously drive two positioners.
The upgraded 'dual-channel' version or an original 'dual-channel' device can be further
upgraded to the 'tri-channel' version to simultaneously drive three positioners.
Figure 44 Dual-Channel and Tri-Channel upgrade icons (shown within the "About" screen)
12.2 /IO Feature Package
The /IO feature upgrade allows you to
- trigger positioning movements by input signals.
- send the axis' positioning information to an external interpreter.
Figure 45 /IO feature icon (shown within the "About" screen)

|         |                  |     | Optional On-Device Features and Upgrades  |     | |  Page 83  |
| ------- | ---------------- | --- | ----------------------------------------- | --- | ----------- |
| 12.2.1  | Pin Assignments  |     |                                           |     |             |
The GPIO socket at the device's connector panel (Figure 5/1) can be used for the
communication of trigger signals.
Each position signal consists of two parts transmitted via different pins. The semantics of a
signal depend on the used communication protocol. A third pin communicates error signals.
The pins of the 37 pin D-Sub socket are assigned as follows.

Figure 46 GPIO socket, pin assignment
|     | Pin  Protocol function  |     |          |          |     |
| --- | ----------------------- | --- | -------- | -------- | --- |
|     | AquadB                  |     | Trigger  | Stepper  |     |
Axis 1
|     | 1   | A+  | UP+    | Step-Pulse+  |     |
| --- | --- | --- | ------ | ------------ | --- |
|     | 20  | A-  | UP-    | Step-Pulse-  |     |
|     | 2   | B+  | DOWN+  | Direction+   |     |
Input
|     | 21  | B-      | DOWN-      | Direction-  |     |
| --- | --- | ------- | ---------- | ----------- | --- |
|     | 3   | Error+  | Error+     | Error+      |     |
|     | 22  | GND     | GND        | GND         |     |
|     | 4   | A+      | n/a        |             |     |
|     | 23  | A-      | n/a        |             |     |
|     | 5   | B+      | Trigger +  |             |     |
Output  n/a
|     | 24  | B-      | Trigger -  |     |     |
| --- | --- | ------- | ---------- | --- | --- |
|     | 6   | Error+  | n/a        |     |     |
|     | 25  | GND     | GND        |     |     |
Axis 2
|     | 7   | A+  | UP+    | Step-Pulse+  |     |
| --- | --- | --- | ------ | ------------ | --- |
|     | 26  | A-  | UP-    | Step-Pulse-  |     |
|     | 8   | B+  | DOWN+  | Direction+   |     |
Input
|     | 27  | B-      | DOWN-   | Direction-  |     |
| --- | --- | ------- | ------- | ----------- | --- |
|     | 9   | Error+  | Error+  | Error+      |     |
|     | 28  | GND     | GND     | GND         |     |
|     | 10  | A+      | n/a     |             |     |
|     | 29  | A-      | n/a     |             |     |
Output  n/a
|     | 11  | B+  | Trigger +  |     |     |
| --- | --- | --- | ---------- | --- | --- |
|     | 30  | B-  | Trigger -  |     |     |

  Page 84  |  Optional On-Device Features and Upgrades
  Pin  Protocol function
| AquadB  |         | Trigger  | Stepper  |     |
| ------- | ------- | -------- | -------- | --- |
| 12      | Error+  | n/a      |          |     |
| 31      | GND     | GND      |          |     |
Axis 3
| 13  | A+  | UP+    |     | Step-Pulse+  |
| --- | --- | ------ | --- | ------------ |
| 32  | A-  | UP-    |     | Step-Pulse-  |
| 14  | B+  | DOWN+  |     | Direction+   |
Input
| 33  | B-      | DOWN-      |     | Direction-  |
| --- | ------- | ---------- | --- | ----------- |
| 15  | Error+  | Error+     |     | Error+      |
| 34  | GND     | GND        |     | GND         |
| 16  | A+      | n/a        |     |             |
| 35  | A-      | n/a        |     |             |
| 17  | B+      | Trigger +  |     |             |
Output  n/a
| 36  | B-      | Trigger -  |     |     |
| --- | ------- | ---------- | --- | --- |
| 18  | Error+  | n/a        |     |     |
| 37  | GND     | GND        |     |     |

|                                      |     | Optional On-Device Features and Upgrades  | |  Page 85  |
| ------------------------------------ | --- | ----------------------------------------- | ----------- |
| 12.2.2  Output Modes and Parameters  |     |                                           |             |
For outgoing communication, the following communication protocols are supported:
-
AquadB
-  Trigger
   TIP

The output mode and parameters can be adjusted on the webserver application's
"Interface" screen, see section 5.2.3.

| 12.2.2.1  AquadB  |     |     |     |
| ----------------- | --- | --- | --- |
According to the logic of AquadB, the signals on lines A and B designate the increment of the
position change. The direction of the position change is defined by whether signal A (positive)
or B (negative) is leading the signal. AquadB is available in LVTTL and LVDS mode.
| Parameter  | Value range  | Related communication aspect  |     |
| ---------- | ------------ | ----------------------------- | --- |
40 – 1,280 ns
| Clock  |     | Minimal signal emitting period  |     |
| ------ | --- | ------------------------------- | --- |
(in steps of 40 ns)
| Resolution         | 0.001 – 64.93 nm  | Position change resolution  |     |
| ------------------ | ----------------- | --------------------------- | --- |
|                    |                   |                             |     |
| 12.2.2.2  Trigger  |                   |                             |     |
The trigger output indicates that the positioner is within a certain position range, i.e. on the
inside or on the outside of a specified area.
| Parameter  | Value range  | Related communication aspect  |     |
| ---------- | ------------ | ----------------------------- | --- |
Position low  0.000 – n nm (depending on  Lower limit of the respective area
positioner travel range)
Position high  0.000 – n nm (depending on  Upper limit of the respective area
positioner travel range)
Trigger polarity  Active high / Active low  Signal emission when inside or
when outside the area
Epsilon  0.000 – n nm (depending on  Tolerance range around upper and
|     | positioner travel range)  | lower area limits (hysteresis to  |     |
| --- | ------------------------- | --------------------------------- | --- |
avoid signal glitches)

Page 86 | Optional On-Device Features and Upgrades
12.2.3 Input Modes and Parameters
For incoming communication, the following communication protocols are supported:
- AquadB
- Stepper
- Trigger
TIP
The input mode and parameters can be adjusted on the webserver application's "Interface"
screen, see section 5.2.3.
12.2.3.1 General Information
For using the real time inputs, respect the following guidance:
- Only high flanks are evaluated
- Voltage should be between 0 -3.3V
- Minimum voltage difference is 900 mV
- Minimum flank high is 30ns
12.2.3.2 AquadB
The AquadB protocol is an incremental protocol that only transfers information about the
change of the measured position. The user continuously needs to keep reading out the
position as there is no information about the absolute value of the current position (in case of
real time output).
Parameter Value range Related communication aspect
Loop mode "open loop"/ "closed Motion valued in metric distance or motion
loop" steps
Change/steps per n nm (closed loop)/ Position change resolution
pulse n steps (open loop)
Th e AquadB protocol is d efined by the Parameters R esolution and Clock. The signal is encoded
over two different 2-level-channels, A and B. The levels’ amplitude is either LVTTL or LVDS (one
at a time):
• Single-ended with LVTTL levels
• Differential with LVDS levels
A measured position change of size Resolution in the encoder results in a state change of
either A or B, depending on the change direction. This is sometimes also referred to X4-
Encoding. This way, the AquadB interface allows transmitting both the displacement and
direction of the target movement.

Optional On-Device Features and Upgrades | Page 87
Figure 47: Signal pattern of a AquadB transfer
Figure 47 illustrates how to calculate the current position from the A/B signals. In an A-leads-B
situation, the position has to be incremented and vice-versa in a B-leads-A situation the
position has to be decremented.
Another way of visualizing the AquadB protocol is to plot Channel A and B against each other,
which creates a square. In Figure 48, a signal change of 90° represents, depending of the
direction, a displacement of ± Resolution. Going counterclockwise represents an increment in
position (B-leads-A) and going clockwise represents a decrement in position (A-leads-B). From
this way of visualizing the AquadB protocol it also becomes clear that only one channel can
change its state at a time.
Figure 48: Interpretating the AquadB signal lines as a square pattern
Resolution and clock
The scaling and the update rate of the A/B outputs are defined by Resolution and Clock (see
Figure 49.

Page 88 | Optional On-Device Features and Upgrades
Figure 49: IDS WebApp real time interface configuration
Resolution
The resolution defines the position resolution of the real-time interface. The resolution of the
AquadB interface is user adjustable and ranges from 1 nm to 1677 nm. We recommend to start
to use a high resolution for the first test, afterwards you can decrease the resolution and adjust
it to the application.
Clock
The clock defines the minimal period at which the quadrature signal increment can be
outputted. The fastest possible clock setting is 40 ns (i.e. 25 MHz), equal to the update interval
of the absolute distance accumulator. The slowest setting is 10 240 ns (i.e. 98 kHz). The clock is
programmable in integer multiples of 40 ns.
Maximum input velocity
The maximum velocity the AquadB protocol can represent is the position change per state
change of A/B (Resolution) divided by the frequency at which the A/B channels are able to
change their state (Clock).
maximum velocity = Resolution / Clock.
As a result, when choosing the right Resolution, there is always a trade-off between the
maximum velocity the AquadB protocol can transmit and the resolution of the transmitted
position. Choosing the right Clock is simpler, as there are no negative side-effects when just
choosing the fastest possible rate (40ns) the providing system (e.g. a DAQ-Card) can handle,
other than resulting in larger datasets.
12.2.3.3 Stepper
According to the logic of Stepper, the signal on line A designates the increment of the position
change, while the signal on line B designates the direction of the position change. Stepper is
available in LVTTL and LVDS mode and can be applied in open loop and closed loop mode.
Parameter Value range Related communication aspect
Loop mode "open loop"/ "closed Motion valued in metric distance or motion
loop" steps
Change/steps per n nm (closed loop)/ Position change resolution
pulse n steps (open loop)

|                    |     | Optional On-Device Features and Upgrades  | |  Page 89  |
| ------------------ | --- | ----------------------------------------- | ----------- |
| 12.2.3.4  Trigger  |     |                                           |             |
According to the logic of Trigger, the signal on line A designates the increment of the position
change in positive direction, while the signal on line B designates the increment in negative
direction. Trigger is available in LVTTL and LVDS mode and can be applied in open loop and
closed loop mode.
| Parameter  | Value range  | Related communication aspect  |     |
| ---------- | ------------ | ----------------------------- | --- |
Loop mode  "open loop"/ "closed  Motion valued in metric distance or motion
|                   | loop"                 | steps                       |     |
| ----------------- | --------------------- | --------------------------- | --- |
| Change/steps per  | n nm (closed loop)/   | Position change resolution  |     |
| pulse             | n steps (open loop)   |                             |     |

Page 90 | Optional On-Device Features and Upgrades
12.3 /PRO Feature Package
The /PRO feature upgrade activates the following enhanced features:
- controlling multiple devices with one single attoDISCOVERY application
- daisy-chaining via the device's Ethernet up- and downlink sockets
- setting the number of steps that are implemented with each stepwise move
- setting the DC level for manual position adjustment
- activating end-of-travel detection
- stopping movement on end-of-travel
Figure 50 /PRO feature icon (shown within the "About" screen)
12.4 AMC/IDS Closed Loop Feature Package (Beta)
The AMC/IDS closed loop feature enables the position feedback and the closed loop
positioning of the positioner using attocube's IDS3010 as an external interferometric
displacement sensor. The contactless method of operation of the IDS3010 allows
measurements on the target/probe, which enables an enhanced positioning performance of
the point of interest.
With this feature and an additional equipment provided by attocube it is possible to operate
any kind of the attocube's positioners in closed loop regardless of the presence of the internal
sensor. For more information on the AMC/IDS closed loop performance or setup information,
please contact attocube directly and/or visit the attocube homepage.
NOTE
This feature is only available if the /PRO feature and the IDS Closed loop
feature are activated on the AMC300, too.
12.4.1 AMC/IDS Closed Loop Setup
For information about the general setup of the IDS3010, please refer to the manuals provided
with the interferometric sensor. The network and HSSL cables should be used for the
connection between AMC300 and IDS3010. Please pay attention to the labelling of the HSSL
cable ends because of the unidirectional information transfer. The network cable is
bidirectional and should be connected to the Ethernet downlink socket at the device’s
connector panel (Figure 5/ Figure 7).
NOTE

Optional On-Device Features and Upgrades | Page 91
The IDS should be the first external device to connect to the AMC. If there
are already devices connected as USB, etc., please undock them and
connect the IDS first. Then the other devices can be connected.
The AMC300 axes numbers are related to the IDS3010 axes and have to be
combined accordingly. Furthermore, the AMC300 axes 1 and 2 are coupled
and allow only identical sensor type selection for both axes. By switching
sensor type on one of these two axes, the second axis switches
automatically, too. The AMC300 axis 3 works independently of the other
axes.
12.4.2 AMC/IDS Closed Loop Feature
To ensure that the AMC/IDS closed loop feature is activated on the AMC, please check if the
feature is listed among the other on-device features in the WebApp on the “About” screen
(Figure 51).
Figure 51: Activated AMC/IDS closed loop feature
12.4.3 AMC/IDS Closed Loop Settings
The AMC/IDS closed loop settings are located in the configuration view of the axis.

Page 92 | Optional On-Device Features and Upgrades
Figure 52: Axis tile, Closed loop settings
1 Sensor Type selection field
2 Inverse IDS direction checkbox
3 Motion Control Threshold setting field
4 Stop on IDS stop limit checkbox
5 Lower stop limit setting field
6 Upper stop limit setting field
12.4.3.1 Sensor Type selection
Sensor type selection for the closed loop positioning (RES or IDS).
Webapp ✓ The “Navigation” screen is opened.
✓ The axis tile's operation view is opened.
1. Click on the arrow of the sensor type (Figure 52/1).
→ A drop-down list with the available sensor types appears.
2. Click onto the sensor type to be applied.
NOTE
RES is the default sensor type setting. The IDS can only be set as a sensor
type if the IDS is connected to the AMC. After connection loss to the IDS, the
sensor type will be set to default.
12.4.3.2 Inverse IDS direction
Adaption of the IDS measurement direction to the positioner movement direction.
Webapp ✓ The “Navigation” screen is opened.
✓ The axis tile's operation view is opened.
1. To activate the option “inverse IDS direction”, check the inverse IDS direction checkbox
(Figure 52/2).

Optional On-Device Features and Upgrades | Page 93
2. To deactivate the option "inverse IDS direction", uncheck the inverse IDS direction
checkbox (Figure 52/2).
NOTE
The option “inverse IDS direction” is available if the IDS is the sensor source.
Per default, this function is deactivated. Check the IDS measurement
direction immediately after setup by moving the positioner stepwise in one
direction.
12.4.3.3 Motion Control Threshold
Threshold range within the closed loop controlled movement stops to regulate, e.g. to prevent
the undesired mechanical noise regulation.
Webapp ✓ The “Navigation” screen is opened
✓ The axis tile's operation view is opened.
1. To set the motion control threshold, type the desired value in pm into the “motion control
threshold” setting field (Figure 52/3).
NOTE
The default setting for motion control threshold is 6 000 pm (6 nm).
12.4.3.4 IDS Stop limit settings
In case of too low / high alignment signal or beam interruption, the IDS measurement
interrupts or cannot be initialized at all. The AMC/IDS closed loop allows a deactivation of the
positioner’s attempt to travel to prevent the measurement interruption. Provided the option is
activated, the actuator is automatically turned off by reaching the position set by “lower stop
limit” and “upper stop limit”.
However, it is possible to move the positioner stepwise beyond the limits. The positioner will
stop after each step if there are no physical obstacles.
NOTE
The options “set lower IDS stop limit”, “set upper IDS stop limit” and “stop
on IDS stop limit” are available if the IDS is the sensor source.
Webapp
✓ The “Navigation” screen is opened.
✓ The axis tile's operation view is opened.
o To set the lower IDS stop limit, type the desired position in pm into the “lower stop limit”
setting field (Figure 52/5).
o To set the upper IDS stop limit, type the desired position in pm into the “upper stop limit”
setting field (Figure 52/6).
o To activate the option "stop on IDS stop limit", check the stop on IDS stop limit checkbox
(Figure 52/4).
o To deactivate the option "stop on IDS stop limit ", uncheck the stop on IDS stop limit
checkbox.

Page 94 | Optional On-Device Features and Upgrades
NOTE
The option "stop on IDS stop limit" by default is deactivated. The limit
settings are 0 pm by default. After the first change of these settings, the
values will be saved for the next measurements. The upper and lower IDS
stop limit settings will be adjusted by changing the reference position (refer
to chapter 12.4.5.1).
12.4.4 IDS Control
The most important IDS control functions are available in the AMC300 web interface (Figure
53). For more IDS functions please refer to the IDS3010 manuals.
NOTE
If the IDS is connected to the AMC, it is not more callable by its old IP
address and cannot be operated as standalone device via Webapp. It is still
possible to operate the IDS via APIs during AMC/IDS closed loop application.
Please use the connected AMC IP address for IDS device connection via API.
By IDS disconnection from the AMC, the IDS gets its IP address back and can
be operated as usual.
Figure 53: “Navigation” screen, IDS control section
1 Pilot laser checkbox
2 Optics alignment [Start] / [Stop]
3 Distance measurement [Start] / [Stop]
4 Environmental compensation unit checkbox
5 Status of environmental compensation unit (connected / disconnected)
6 Temperature display (ECU measured)
7 Relative humidity display (ECU measured)
8 Pressure display (ECU measured)

Optional On-Device Features and Upgrades | Page 95
9 Measured refractive index display (determined from ECU parameters)
10 Used refractive index display (from ECU or manual set)
NOTE
These functions are disabled if the IDS3010 is not connected to the AMC300.
12.4.4.1 IDS Pilot Laser
Enabling pilot laser (visible red laser) to ease the optical alignment.
Webapp ✓ The “Navigation” screen is opened.
o To activate the pilot laser, check the pilot laser checkbox (Figure 53/1).
o To deactivate the pilot laser, uncheck the pilot laser checkbox (Figure 53/1).
NOTE
The pilot laser is active for 15 minutes after activation of the checkbox.
Afterwards it disables automatically.
12.4.4.2 Optics Alignment
Enabling optics alignment to check and maximize the signal contrast of each axis.
The signal contrast is displayed for each axis individually, which has IDS as a sensor source
(Figure 54/1).
Figure 54: “Navigation” screen, (IDS) “Closed Loop Functions” section
1 Signal contrast display
2 Axis [Reset]
3 Position display
4 Reference position display
Webapp
✓ The “Navigation” screen is opened
o To start optics alignment, press the “Start” button of the optics alignment (Figure 53/2).
o To stop optics alignment, press the “Stop” button of the optics alignment (Figure 53/2).

Page 96 | Optional On-Device Features and Upgrades
NOTE
Optics alignment function is applied to all axes simultaneously.
We recommend the interferometric contrast (in per mil ‰) to be higher
than 500 ‰. Moreover, the target as well as the sensor head should be
adjusted to achieve relative constant alignment signal over the whole
measurement range.
If the alignment signal is not high enough for entire positioner movement
range, please use the “stop on IDS stop limit” options, to prevent the
measurement interruption.
Furthermore, optics alignment needs to be stopped in order to enable the
displacement measurement and cannot be started if the measurement is
running.
12.4.4.3 IDS Distance Measurement
Initialization of the interferometric distance measurement. The target location at the moment
of the initialization is displayed as an absolute reference position relative to the sensor head
for each axis individually, which has IDS as a sensor source (Figure 54/4). The position displays
value relative to the reference position (Figure 54/3).
Webapp ✓ The “Navigation” screen is opened.
o For measurement initialization, press the “Start” button of the distance measurement
(Figure 53/3).
o To stop measurement, press the “Stop” button of the distance measurement (Figure
53/3).
NOTE
Measurement function is applied to all axes simultaneously. The
measurement initialization requires a time up to two minutes.
After AMC reboot during the measurement, the measurement will be start
automatically again. Please be aware of the reference position settings.
12.4.4.4 Environmental Compensation Configuration
At non-vacuum condition, the refractive index of air needs to be compensated. For
compensation, the environmental compensation unit (ECU) can be used. After activation of the
ECU, the ECU parameters as temperature, relative humidity, pressure and measured refractive
index will be displayed (Figure 53/6-9). The actual refractive index used for compensation will
be displayed by “Used refractive index” (Figure 53/10). There are further options for manual
setting of the refractive index. For more information about these options, please refer to the
IDS3010 manuals.
Webapp ✓ The “Navigation” screen is opened.
o To enable the environmental compensation, check the “Enabled” checkbox (Figure 53/4).
o To disable the environmental compensation, uncheck the “Enabled” checkbox (Figure
53/4).

Optional On-Device Features and Upgrades | Page 97
NOTE
If the compensation is off, the value 1 is used as refractive index (vacuum).
12.4.5 Closed Loop Functions
After distance measurement initialization, the closed loop positioning can be applied. For
general closed loop operation please refer to chapter 8.6. The IDS specific closed loop
functions are described below.
12.4.5.1 Reset Axis
According to the external location of the IDS sensor source, the reference position of the axis is
freely selectable. The reference position is firstly set during the measurement initialization.
Afterwards, the positioner movement takes place relative to the defined reference position.
This reference position can be changed by reset of axis at the desired position. The positioner
location at that moment will be set as a new reference position. This option can be used
multiple times during the measurement for each axis individually.
NOTE
If the IDS stop limits are set, they will be changed according to the new
reference position automatically, so there is no need to adjust these
settings.
Webapp
✓ The “Navigation” screen is opened.
o To reset the axis, press the “Reset” button of the axis (Figure 54/2).
12.4.5.2 Sensitivity setting
The sensitivity setting is a function to affect the controller gain regarding the indirect relation
between approach velocity and stability. The value for sensitivity can be set in range between 1
and 10, where 1 represents the fastest velocity and 10 the slowest one, respectively. This
function is only available in APIs. The default sensitivity setting is 5 for AMC/IDS closed loop.
12.4.5.3 Crosstalk Threshold setting
The crosstalk threshold setting will be used in positioner stack applications to adjust the
positioner control in stack while moving another axis. This function is only available in APIs.
12.4.6 Fine Tuning control loop
For successful closed loop operation with the IDS as encoder the closed loop (control
parameters need to be adapted).
In the positioner profile the parameters are optimized for small loads and not stacked
positioners. In case of positioner stacks or higher loads please adjust the settings by using the
function setActorParametersJson. In the following a python example is shown:

Page 98 | Optional On-Device Features and Upgrades
import AMC
import IDS
pos = AMC.Device(#ipAMC)
pos.connect()
pos.control.setActorParametersJson(i,"{\"type\":\"ANPx312\",\"dc_slewrate\":10,\"sen
sitivity\":6,\"dc_range\":500}")
ids = IDS.Device(#ipAMC)
ids.connect()
ids.displacement.setAverageN(10) #Number between 0-24 see documentation
The important parameters are:
- Sensitivity
- DC_Slewrate
- DC_Range
- Average of IDS
In general, the higher the load and or the lower the first resonance frequency the settings
need to be adjusted the following:
- dc_slewrate → decreasing
- dc_range → increasing
- sensitivity → increasing
- average IDS → 3db cutoff filter in the range of lowest resonance frequency
For example setting sets an further questions, please contact attocube support.

Optional On-Device Features and Upgrades | Page 99
12.5 Microscopy Upgrade
The Microscopy Upgrade is activated if the AMC300 is used within an attocube microscope
system. The Microscopy Upgrade allows you that
- the GPIO port can be configured to trigger single steps with attocube’s SPM-controller
ASC500 (see section 12.5.1).
- for the read out of the RES-position, all three axis use the same ground and supply
line (see section 12.5.2).
Figure 55 Microscopy Upgrade icon (shown within "About" screen)
12.5.1 Use GPIOs with ASC500
Figure 56 NSL-/Mic-mode option for the GPIO mode within the "Interface" screen
To control the AMC300 with the ASC500, a so-called NSL-cable included in the AMC300 (with
activated Microscopy Upgrade) delivery is needed. Connect the NSL-plug of the cable to the
ASC500 and the other connector with the GPIO port of the AMC300. Please refer to the
ASC500 manual to find the correct settings for its NSL ports.
With the Microscopy Upgrade, you can find an additional GPIO Mode in the “Interface” screen
of the AMC300 Web-Application, which is called “NSL- / MIC-mode”. By choosing that option,
the ‘Real Time Input’-area changes its appearance as shown in the figure above. If a trigger

Page 100 | Optional On-Device Features and Upgrades
signal is sent from the ASC500 to the AMC300, a single step is triggered on a certain axis. By
changing the “NSL axis”, you can define on which axis the single steps are performed.
NOTE
When the “Microscopy Upgrade” is activated, the settings are automatically switched to
“NSL-/MIC-mode”.
12.5.2 Shared Lines for RES-position read-out
Figure 57 Shared mode option for axis setup/ RES sensors within the "Configuration" screen
In order to reduce the number of cables, which have to be connected to the positioners in the
insert, the ground and supply wires for the RES elements are used by all three axis, if the
“shared (line)”-option is active.
This mode is also available in a ‘low frequency’ version. It might be necessary to use the low
frequency version, if the cables from the AMC300 to the positioners exceed the standard
length.
For more information see the setMode function of the RES interface in the Interface Manual or
contact the attocube’s support team, if you need further instructions on that topic.
TIP
With reducing the number of cables, the heat load can be lowered – what is crucial for all
low temperature experiments. Find out more about this topic within attocube’s technical
note TN04.
NOTE
When the “Microscopy Upgrade” is activated, the settings are automatically switched to
“shared”.
12.5.3 Hardware connection for usage within
microscopy systems
The AMC300 needs to be connected to attocube’s SPM controller ASC500 and (via the ACC100
or ACC50) to the microscopy insert. For the latter connection, one or two dedicated

Optional On-Device Features and Upgrades | Page 101
AMC300 – ACC100/ACC50 break-out panels (BOP) can be used (see Figure 58). Each BOP has
three D-Sub HD 26-Pin connectors and one 12-Pin Fischer connector. The three D-Sub
connectors are meant to be for the connection with the three D-Sub HD 26-Pin connectors on
the back of the AMC300 (see Figure 5/7-9). The dedicated “AMC300 RES-cable for MIC” fits
perfectly. The 12-Pin Fischer connector is for the connection with the MIC-Insert.
Figure 58 AMC300 - ASC500 break-out panel
The AMC300’s GPIO port (see Figure 5/1) will be used to connect the device to the ASC500.
The dedicated NSL-cable ASC500-AMC300 must be used here.
If the setup requires more than three positioner axis, a double-rack version of the AMC300 will
be used. A second BOP including the appropriate cables is then needed. Moreover, an Ethernet
cable and USB-stick is required for Daisy-chaining.

Page 102 | System Integration
13 System Integration
The device can be integrated with external systems or devices by
- combining it with third party hardware
- establishing incoming and outgoing trigger connections (/IO upgrade required), see
section 12.2
- controlling it with individual software interfaces (see interface manual).
CAUTION
General hazard!
Inadequate hardware connections may cause injury and are likely to damage the device or
interfere with an appropriate functioning.
o Always contact attocube for technical support, before combining the device with
third party hardware.
o Do carefully observe the information in this section when combining the device
with third party hardware.
NOTE
attocube is not liable for any damages resulting from an unauthorized combination of the
device with third party hardware. Unauthorized combination with third party hardware is
not covered by attocube's warranty.

attocube systems AG
Eglfinger Weg 2
85540 Haar, Germany
Phone: +49 89 420 797 0
E-Mail: info@attocube.com
www.attocube.com
For technical queries, contact:
support@attocube.com
Regional US Sales Representatives:
West Coast: Arcadia, CA
Phone: +1 510 631 2154
Southwest: Henderson, NV
Phone: +1 510 631 1784
Midwest: Delaware, OH
Phone: +1 510 631 133