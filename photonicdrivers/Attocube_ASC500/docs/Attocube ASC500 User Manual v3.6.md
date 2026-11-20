Version: 3.5
Modified: July 20
Products: ASC500
User Manual
ASC500
SPM Controller & Software
attocube systems AG, Eglfinger Weg 2, D – 85540 Haar bei München, Germany
Phone: +49 89 420 797 0 Fax: +49 89 4207 9720 190
E-Mail: info@attocube.com www.attocube.com
For technical queries, contact:
support@attocube.com
attocube systems office Munich:
Phone +49 89 420 797 0
Fax +49 89 420 797 201 90

Table of Contents
Table of Contents ............................................................................... 3
1 Introduction ............................................................................ 5
1.1 System Overview ..................................................................... 5
1.2 Safety Information .................................................................. 5
1.2.1 Warnings…………………………… ................................................... 6
1.3 Declarations of Conformity ..................................................... 8
1.4 Waste Electrical and Electronic Equipment (WEEE) Directive 9
2 Hardware Description ........................................................... 10
2.1 Mechanical Installation ......................................................... 10
2.2 Electrical Installation ............................................................. 11
2.2.1 Connecting to the Voltage Supply ......................................... 11
2.2.2 Fuses …………………………… ....................................................... 11
2.3 Front and Rear Panel Connections ........................................ 12
2.3.1 Front Panel ASC500 v1 .......................................................... 12
2.3.2 Rear Panel ASC500 v1............................................................ 12
2.3.3 Cable description ASC500 v1 ................................................. 13
2.3.4 Front Panel ASC500 v2 .......................................................... 14
2.3.5 Back Panel ASC500 v2 ........................................................... 15
2.3.6 Front Panel ASC500 v3 .......................................................... 16
2.3.7 Back Panel ASC500 v3 ........................................................... 16
3 Description of the Controller................................................. 18
3.1 Key Features and Benefits ..................................................... 18
3.2 Hardware Specifications ........................................................ 18
3.3 General Functionality ............................................................ 19
3.4 Hardware Requirements and Operating Systems ................. 20
3.5 Hardware Driver Installation ................................................. 20
4 Data handling ........................................................................ 23
4.1 Quick guide for data saving ................................................... 23
4.1.1 The Data Channel Configuration dialogue ............................ 23
4.1.2 The Snapshot Preset Configuration ....................................... 26
4.2 Data handling details ............................................................. 27
4.2.1 Signals, data channels and data groups ................................ 27
4.2.2 Internal Signal Flow ............................................................... 28
4.2.3 Data processing chain ........................................................... 29
4.2.4 Sample Time and Average ..................................................... 30
4.2.5 Data Channel Configuration (DCC) in detail .......................... 31
4.2.6 DCC usage .............................................................................. 32
4.2.7 Saving the data ...................................................................... 33
4.2.8 Parameter File ....................................................................... 37
4.2.9 Snapshot Presets ................................................................... 37
5 Operating the Controller: General Usage and Overview ...... 40
5.1 Software Installation and Getting Started ............................. 40
5.2 Description of Main Daisy Program....................................... 41
5.2.1 The main toolbar ................................................................... 41
5.2.2 The menu bar ........................................................................ 43
5.2.3 Loading a profile .................................................................... 48
5.3 Profile configuration .............................................................. 48
5.3.1 User-configurable GUI appearance ....................................... 49
Page 3
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

5.3.2 Aliases menu ......................................................................... 49
5.3.3 New signal and parameter names in v2.5 and later .............. 50
5.4 General Usage and Description of Common GUI Controls .... 51
5.4.1 Text Edit Boxes ...................................................................... 51
5.4.2 Context Menu........................................................................ 52
5.4.3 Frame View context menu .................................................... 53
5.4.4 Display wizard ....................................................................... 53
6 Description of the default AFM layout .................................. 56
6.1 The Output Limits .................................................................. 56
6.2 The Scan Control ................................................................... 60
6.2.1 Scan, line and pixel trigger .................................................... 64
6.2.2 Step Scanner Control (discontinued) .................................... 65
6.2.3 Lithography ........................................................................... 65
6.3 The Z Control ......................................................................... 69
6.3.1 Details…………………………… ..................................................... 70
6.3.2 Slope Compensation ............................................................. 70
6.3.3 Setpoint Modulation ............................................................. 74
6.4 The Scan Data Displays .......................................................... 75
6.4.1 Frame View ........................................................................... 75
6.4.2 Scan Data Display: Line View Tab .......................................... 76
6.4.3 Example for Shifting, Moving and Zooming the Scan Area ... 78
6.5 The main functions tab section ............................................. 81
6.5.1 Phase Locked Loop (PLL tab) ................................................. 81
6.5.2 LF Lockin…………………………… .................................................. 82
6.5.3 Lever Excitation ..................................................................... 83
6.5.4 Coarse…………………………… ..................................................... 84
6.5.5 Autoapproach ........................................................................ 86
6.5.6 Path…………………………………. ................................................... 89
6.5.7 Dual Pass…………………………… ................................................. 92
6.5.8 Crosslink…………………………… .................................................. 94
6.5.9 DAC Outputs .......................................................................... 94
6.5.10 Scan…………………………… ......................................................... 95
6.6 1-dimensional data displays .................................................. 95
6.6.1 Resonance View .................................................................... 95
6.6.2 Line View…………………………… ................................................. 97
6.6.3 Frequency Analysis View ....................................................... 98
6.6.4 Spectroscopy Tab(s) .............................................................. 99
6.6.5 Soft Spec…………………………… ................................................ 101
6.7 Working Examples ............................................................... 102
6.7.1 Setting up the PLL ................................................................ 102
6.7.2 Using the Q-control feature ................................................ 109
7 Firmware Upgrade .............................................................. 113
8 Preventive Maintenance ..................................................... 114
8.1 Safety Testing ...................................................................... 114
8.2 Fuses .................................................................................... 114
8.3 Cleaning ............................................................................... 114
Page 4

1 Introduction
1.1 System Overview
The SPM Scan Controller ASC500 is a complete scan control unit providing
the suitable signals for the use with the attoCFM Confocal Microscope,
the attoAFM Atomic Force Microscope and the attoSNOM Near-Field
Optical Microscope as well as any other homebuilt or commercial
scanning probe microscope.
The modular and flexible digital SPM controller, ASC500, combines state
of the art hardware with innovative software concepts and offers an
unmatched variety of controlling possibilities, enabling the customer to
perform many different scanning probe microscopy applications. All
desirable functions and high-end specifications are available to control
the experiment of your choice. The flexible, FPGA-based architecture
allows the on demand implementation of your particular requirements.
1.2 Safety Information
For the continuing safety of the operators of this equipment, and the
protection of the equipment itself, the operator should take note of the
Warnings, Cautions, and Notes throughout this handbook and, where
visible, on the product itself.
The following safety symbols may be used on the equipment:
Warning, risk of danger. Refer to the handbook for details on this hazard.
Warning, risk of electric shock. High voltages present.
Warning, laser radiation. Do not stare into beam. Class 1M Laser product.
Functional (EMC) earth/ground terminal.
Page 5
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

The following safety symbols may be used throughout the handbook:
Warning. An instruction which draws attention to the risk of injury or
death.
Caution. An instruction which draws attention to the risks of damage to
the product, process or surroundings.
Note. Clarification of an instruction or additional information.
1.2.1 Warnings……………………………
The unit may only be connected to an earthed and fused supply of 110 to 230 V.
The equipment, as described herein, is designed for use by personnel
properly trained in the use and handling of mains powered electrical
equipment. Only personnel trained in the servicing and maintenance of
this equipment should remove its covers or attempt any repairs or
adjustments. If malfunction is suspected, immediately return the part to
attocube systems for repair or replacement. There are no user-
serviceable parts inside the electronics. Modified or opened electronics
cannot be covered by the attocube warranty anymore. Take special care
if connecting products from other manufacturers. Follow the General
Accident Prevention Rules.
If this equipment is used in a manner not specified by the manufacturer,
the protection provided by the equipment may be impaired. Do not
operate the instrument outside its rated supply voltages or environmental
range. In particular, excessive moisture may impair safety.
Never connect any cabling to the electronics when contacts are exposed!
Never connect any cabling to the electronics when the electronics is not
in GND mode! Avoid shorts. Be careful not to cause a short circuiting
between the contacts in the BNC or any other connector.
For laboratory use only. This unit is intended for operation from a normal,
single phase supply in the temperature range 5° to 40°C, 20% to 80% RH.
Page 6

Page 7
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

1.3 Declarations of Conformity
For Customers in Europe
This equipment has been tested and found to comply with the EC
Directives 89/336/EEC ‘EMC Directive’ and 73/23/EEC ‘Low Voltage
Directive’ as amended by 93/68/EEC.
Compliance was demonstrated by conformance to the following
specifications which have been listed in the Official Journal of the
European Communities:
Safety EN61010: 2001
EMC EN61326: 1997
Page 8

1.4 Waste Electrical and Electronic Equipment (WEEE) Directive
Compliance
As required by the Waste Electrical and Electronic Equipment (WEEE)
Directive of the European Community and the corresponding national
laws, attocube systems offers all end users in the EC the possibility to
return "end of life" units without incurring disposal charges.
This offer is valid for attocube systems electrical and electronic
equipment:
 sold after August 13th 2005,
 marked correspondingly with the crossed out "wheelie bin" logo
(see logo to the left),
 sold to a company or institute within the EC,
DE16963721  currently owned by a company or institute within the EC,
 still complete, not disassembled, and not contaminated.
As the WEEE directive applies to self-contained operational electrical and
electronic products, this "end of life" take back service does not refer to
other attocube products, such as
 pure OEM products, that means assemblies to be built into a unit
by the user (e. g. OEM electronic drivers),
 components,
 mechanics and optics,
 left over parts of units disassembled by the user (PCB's, housings
etc.).
If you wish to return an attocube unit for waste recovery, please contact
attocube systems or your nearest dealer for further information.
Waste treatment on your own responsibility
If you do not return an "end of life" unit to attocube systems, you must
hand it to a company specialized in waste recovery. Do not dispose of the
unit in a litter bin or at a public waste disposal site.
Ecological background
It is well known that WEEE pollutes the environment by releasing toxic
products during decomposition. The aim of the European RoHS directive
is to reduce the content of toxic substances in electronic products in the
future.
The intent of the WEEE directive is to enforce the recycling of WEEE. A
controlled recycling of end of live products will thereby avoid negative
impacts on the environment.
Page 9
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

2 Hardware Description
2.1 Mechanical Installation
Siting
Unpack all components and retain all packing material and shipping
containers for your future shipping needs. When placing the controller,
do not obstruct the ventilation slots in any way. Make also sure that the
controller is not placed close to any liquids or moisture source.
Carefully unpack and visually inspect the controller for any damage. Place
all components on a flat and clean surface.
Caution. When siting the unit, it should be positioned so as not to impede
the operation of the rear panel power supply plug and switch. Ensure that
proper airflow is maintained to the unit. Do not obscure the ventilation
holes
Warning. Operation outside the following environmental limits may
adversely affect operator safety:
Indoor use only
Maximum altitude 2000 m
Temperature range 5°C to 40°C
Maximum humidity less than 80% RH (non-condensing) at 31°C
To ensure reliable operation the unit should not be exposed to corrosive
agents, excessive moisture, heat or dust. If the unit has been stored at a
low temperature or in an environment of high humidity, it must be
allowed to reach ambient conditions before being powered up.
Note. In applications requiring the highest level of accuracy and
reproducibility, it is recommended that the controller unit is powered up
approximately 30 minutes before use, in order to allow the internal
temperature to stabilize.
Caution. Do not connect cabling longer than 3m. Longer cabling may
increase the sensitivity of the device to external influences.
Page 10

2.2 Electrical Installation
2.2.1 Connecting to the Voltage Supply
Warnings. The unit must be connected only to an earthed and fused
supply of 110 to 230V.
Use only power supply cables supplied by attocube systems, other cables
may not be rated to the same current. The unit is shipped with
appropriate power cables for use in the UK, Europe, and the USA. When
shipped to other territories the appropriate power plug must be fitted by
the user.
2.2.2 Fuses ……………………………
Two T 4 A/250 V fuses are located on the back panel for the mains voltage.
Note. When replacing fuses:
Switch off the power and disconnect the power cord before removing the
fuse cover.
Always replace broken fuses with a fuse of the same rating and type.
Page 11
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

2.3 Front and Rear Panel Connections
2.3.1 Front Panel ASC500 v1
Software development for v1 ASC500 was ceased around 2010.
Figure 1: Front panel of the ASC500.
On the front panel of the ASC500 v1, there is only the green “ON”-
LED indicating the power status of the unit. If the unit is on, the LED
is lit.
2.3.2 Rear Panel ASC500 v1
Figure 2: Back panel of the ASC500 v1 scan controller.
On the back panel, there are:
- the main power switch,
- the fuse holder (see fuse description above),
- the main power supply connector,
(110/220 V, 50 – 60 Hz, max. 20 VA),
- an earth terminal for additional connection of the unit to
earth,
- the functional ground for connecting a setup to the
electronics ground,
- 3 power connectors for supplying additional hardware
- the AFM connector (high speed input and output),
- the main SPM outputs,
- the connector for the iBox (discontinued),
- the USB connector for connection to a PC,
- the serial connector to connect to the ANC150.
Page 12

2.3.3 Cable description ASC500 v1
Power supply:
Use the power cable to connect the ASC500 to the 100, 115 or 220 V
jack.
USB cable from computer to ASC500:
Use the USB connector to connect to your computer.
ASC500-iBox:
Connect the cable attached to the ASC500-iBox to the respective
connector of the ASC500 and the round pin connector for the power
supply.
Main cable - Signal In- and Outputs:
Use the main cable and connect it to the respective connector. The
BNC connectors are connected to the setup as follows:
ADC 1: sensor signal
ADC 2: optional input
ADC 3: optional input
DAC 1: optional output
DAC 2: optional output
x-Out: connects to the voltage amplifier for x-axis (e.g. ANC200)
y-Out: connects to the voltage amplifier for y-axis (e.g. ANC200)
z-Out: connects to the voltage amplifier for z-axis (e.g. ANC200)
AFM cable – High Speed Signal In- and Output:
Use the AFM cable and connect it to the respective connector. The
BNC connectors are connected to the AFM setup as follows:
Fosc: high frequency sensor signal (e.g. AFM tapping mode)
as feedback input
Fexc: high frequency excitation signal
Warning. Do not, under any circumstances attempt to connect the
digital I/O to any external equipment that is not galvanically isolated
from the mains or is connected to a voltage higher than the limits
specified. In addition to the damage that may occur to the controller
there is a risk of serious injury and fire hazard.
Page 13
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

2.3.4  Front Panel ASC500 v2
  Since end of 2008, v2 hardware of the ASC500 controller is available.
The latest supported software version is V26. Implementation of
new features was ceased 2016, bugs are continuously being fixed.

Figure 3: Front panel of the ASC500 v2. The break-out cable of v1 was replaced by easily accessible BNC
connectors at the front panel. Please note that both input and output ranges and sampling rate of all
converters are indicated directly below the connector plugs.
  With the new hardware versions, most connections to and from the
controller are available on the front panel. Different sections in the
front panel combine the plugs for certain functionalities like inputs,
outputs, trigger ports, etc. The different sections are (from left to
right):
iBox connection: The iBox (discontinued) connector is to be plugged
into this socket.
| External:  | There  are  two  | 8  bit  LVTTL  | (low  voltage  TTL,  | 3.3 V)  |
| ---------- | ---------------- | -------------- | -------------------- | ------- |
connectors, one for input and one for output triggering. Connectors
are 9-pin D-sub (Pin 9 is GND).
On the left, the pin numbering for the sub-D connector of the
External lines is shown. The upper input connector (labeled ‘1’ or
‘IN’) is used for TTL inputs:
|     | Input pin   | Usage                     |     |     |
| --- | ----------- | ------------------------- | --- | --- |
|     | 1           | Counter input             |     |     |
|     | 2           | Reserved                  |     |     |
|     | 3           | External Handshake SYNC   |     |     |

|     | 4-8  | Reserved  |     |     |
| --- | ---- | --------- | --- | --- |

|     | 9   | GND  |     |     |
| --- | --- | ---- | --- | --- |
  The output connector (labeled ‘2’ or ‘OUT’) is used as follows:

|     | Output pin   | Usage                                     |     |     |
| --- | ------------ | ----------------------------------------- | --- | --- |
|     | 1            | Pixelclock output (see section 6.2.1 for  |     |     |
details6.2)
|     | 2   | Lineclock output             |                   |      |
| --- | --- | ---------------------------- | ----------------- | ---- |
|     | 3   | Frameclock output            |                   |      |
|     | 4   | External Handshake SYNC OUT  |                   |      |
|     | 5   | Shutter  (used               | by  lithography,  | see  |
section 6.2.3)
|     | 6-8  | Reserved  |     |     |
| --- | ---- | --------- | --- | --- |
|     | 9    | GND       |     |     |

Page 14

ADC section: There are six ADC inputs available, labeled 1 through
6, with 18 bit 400 kS/s each.
DAC section: There are four DAC outputs available (+/-10 V, 16 bit,
200 kS/s). Two additional modulation ports, labeled MOD1 and
MOD2 can be used to add any analog voltage to the outputs of DAC1
and DAC2, respectively.
SCAN section: The SCAN section provides the outputs of the scan
engine: Xout, Yout and Zout. In addition, there is a modulation input
for the Zout that gives you the possibility to externally modulate the
voltage output to the z scanner.
HF section: This section provides the high frequency inputs and
outputs (50 MS/s) of the controller. There are two independent
groups of in- and outputs. Each group features 16 bit, 50 MS/s ADCs
and DACs, as well as SYNC out (same output frequency than OUT
with +/- 5V amplitude) and MON out (pre-amplified IN signal). Only
one of the two HF channels can work at a time.
AUX power: This connector provides stable +/- 15 V and +/- 5 V for
external devices. Maximum current is 200 mA at 5 V and 100 mA at
15 V. The connector is a 5pin Binder series 440.
2.3.5 Back Panel ASC500 v2
The back panel of the ASC500 generation v2, features two new
possibilities to connect the controller to other devices. There is a
digital serial interface (called NSL A and NSL B) and a LAN connector.
Figure 4: Back panel of the ASC500 v2. Please note the new digital interface (NSL) and the LAN connection.
The connectors from left to right are the following:
Power connection: Connection to mains. The ASC500 features auto
range for 110 - 115 V and 230 V, 50..60 Hz.
Ground: 4 mm plug for connecting to earth and housing GND.
Voltage indicators: Shows correct availability of internal DC
voltages.
NSL A/B: Digital serial interface to connect to attocube ANC350
Step/Scan-Controller. 9 pin D-sub connector.
USB: USB 2.0 interface to connect to the PC.
Page 15
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Serial: Serial interface to connect to attocube ANC150 /ANC300
Step-Controller. RJ45 connector.
LAN: LAN 100 Mbit connection to the PC.
2.3.6 Front Panel ASC500 v3
In 2013 attocube released its new, version 3 controller. The design
was kept similar to V2 though two ports were added to the back
panel to enable connectivity to attocube’s FPS3010 displacement
sensor.
ASC500 v3 currently runs with V27 software where the last release
can be requested from attocube support support@attocube.com.
Figure 5: Front panel of the ASC500 v3. It is identical to the v2.
The connectors on the front plate of v2 and v3 are identical. For
more information see 2.3.4
2.3.7 Back Panel ASC500 v3
The back panel of the ASC500 generation 3 features SENSOR X and
SENSOR Y connectors to establish a link to the FPS3010. This enables
optical readout of the sample position to eliminate the non-linearity
of the scanner piezos (Closed Loop Scanning functionality). The rest
is similar to the v2 back panel.
Figure 6: Back panel of the ASC500 v3. Compared to v2 two HDMI ports have been added (SENSOR X/Y).
The connectors will be described in more detail from left to right:
Power connection: Connection to mains. The ASC500 features auto
range for 110 - 115 V and 230 V, 50..60 Hz.
Page 16

Ground: 4 mm plug for connecting to earth and housing GND.
Voltage indicators: Shows correct availability of internal DC
voltages.
Sensor X/Y: These ports can be used to connect to the FPS3010.
HDMI ports.
NSL A/B: Digital serial interface to connect to attocube ANC350
Step/Scan-Controller. 9 pin D-sub connector.
USB: USB 2.0 interface to connect to the PC.
Serial: Serial interface to connect to attocube ANC150 /ANC300
Step-Controller. RJ45 connector.
LAN: LAN 100 Mbit connection to the PC.
Page 17
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

3 Description of the Controller
3.1 Key Features and Benefits
AFM/SNOM Control  18 bit 400 kS/s ADC input-channel for AFM contact mode
signal
 digital measurement of frequency and phase for AFM non-
contact mode with feedback
 DDS for oscillation excitation / frequency range 1 kHz to
400kHz
 14 bit 40 MS/s ADC input-channel for measurement of the
amplitude dampening (new v2 version: 16 bit 50 MS/s)
 digital PI feedback loop for z controller
CFM Control  18 bit 400 kS/s ADC input-channel for CFM signal
 counter input for connection to single photon counter
STM Control  18 bit 400 kS/s ADC input-channel for measurement of
tunneling current
 16 bit 200 kS/s DAC output-channel for gap voltage
 modulation input for gap voltage
 digital PI feedback loop for z controller
Scan Generation  2D xy-scan generator with 4 MHz pixel frequency
 16 bit resolution, effective resolution of 20bit in full range
mode
 hardware crosstalk compensation
 hardware slope compensation
 slew rate controlled movement
 direct vectorized positioning
Other  counter input: i.e. 24 bit 10 MHz min. pulse width 50 ns
 online data processing: digital filter, low-pass, averaging,
offset correction, calibration, FFT
3.2 Hardware Specifications
Inputs (ADC1-6) Voltage range: +/- 10 V
Max. allowed voltage: +/- 15 V
Converter resolution: 18 bit
Voltage resolution: 76 µV
Update rate: 400 kHz
Input resistance: 10 kOhm
INL +/- 2.5 LSB
DNL + 1.75/-1 LSB
Offsets: +/- 60 mV
Outputs (X-, Y-, Z-Out) The Z-Out output to the z scanner features an 18 bit resolution with
possible 14 bit attenuation. The scan outputs are designed in a way
that you will never reach the digital bit resolution limit!
Page 18

|                   | Voltage range:                        |     | +/- 10 V (uni- or bipolar)  |     |
| ----------------- | ------------------------------------- | --- | --------------------------- | --- |
|                   | Max. output current:                  |     | +/- 20 mA                   |     |
|                   | Converter resolution:                 |     | 16 bit (18 bit for Z-Out)   |     |
|                   | Programmable attenuation:             |     | 14 bit                      |     |
|                   | Programmable offset:                  |     | +/- 10 V                    |     |
|                   | Offset resolution:                    |     | 16 bit                      |     |
|                   | Max. resolution in small range mode:  |     | 16 bit over 1.2 mV          |     |
|                   | Update rate:                          |     | 4 MHz                       |     |
| Outputs (DAC1-4)  | Voltage range:                        |     | +/- 10 V                    |     |
|                   | Max. output current:                  |     | +/- 20 mA                   |     |
|                   | Converter resolution:                 |     | 16 bit                      |     |
|                   | Voltage resolution:                   |     | 305 µV                      |     |
|                   | Update rate:                          |     | 200 kHz                     |     |
|                   | INL:                                  |     | +/- 1 LSB                   |     |
|                   | DNL:                                  |     | +/- 1 LSB                   |     |
| External          | External 1:                           |     | 8 LVTTL inputs (Pin 1-8)    |     |
|                   | External 2:                           |     | 8 LVTTL outputs (Pin 1-8)   |     |
|                   | GND Pin:                              |     | Pin 9                       |     |
|                   | Pulse Level:                          |     | 3.3 V                       |     |
3.3  General Functionality
  Scanning probe microscopy works by scanning a probe across a
sample or the sample under the probe and thereby recording certain
physical variables. The ASC500 controller and software controls the
|     | scan  position  | and  movement,  | acquires  several  | signals  |
| --- | --------------- | --------------- | ------------------ | -------- |
simultaneously during the scan and saves the acquired images.
Furthermore, it offers a feedback option for AFM measurements in
feedback mode.
In order to perform the scan, the software calculates voltage ramps
depending on the scan amplitude, the scan speed and the number
of pixels of the image. The voltage ramps will be amplified by one of
attocube’s high voltage amplifiers (ANC200, ANC250, ANC300, and
ANC350) and applied to the piezos moving the sample in X-, Y- and
Z-direction. The imaging process is done in a line-by-line scanning
manner. During the displacement in X-direction, called the fast axis,
the Y-position remains constant. The X-direction will be scanned in
both forward and backward direction, leading to two images: the
forward and backward image. All signals are acquired during both
forward and backward motion.
In case of scanning in feedback mode, the feedback loop will keep
the sensor value as close as possible to the value called Setpoint by
controlling the output on the z-piezo.

Page 19
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Y (slow axis)
Line 3
Backward
Line 2
Forward
Line 1
X (fast axis)
Figure 7: Movement of the tip during the scan. The scanners therefore move the exact opposite way.
3.4 Hardware Requirements and Operating Systems
The minimum system requirements are the following: a recent
multicore processor, 1 GB RAM, 100 GB hard disk, and an HD
monitor. The current version of the software is available for
Windows 7, the appropriate drivers for the software are delivered
with the system.
3.5 Hardware Driver Installation
The controller is connected to the computer via USB. Software and
drivers are either installed on the computer delivered with the
system or included on a CD. In the latter case, please copy the
software (folder ‘ASC500_Software’) and the drivers (folder
‘ASC500_Driver’) from the CD onto your computer.
When the ASC500 is connected to the computer and switched on
for the first time, the computer should recognize the new
hardware. Please follow the steps below to install the driver.
Since October 2014 the Software is shipped with an installer
executable file. Installing this will automatically install all required
drivers.
Page 20

Go to Control Panel -> Device Manager, and
search for the new device. Right click to
select Update Driver Software.
Select Browse my computer for driver
software.
Browse to select the directory where you
have stored the ASC500 driver(s) and click
Next.
(Note that there are separate driver files for
Windows Vista / Windows 7 32 bit and 64
bit versions.)
Click on Install…
Page 21
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

…to start the driver installation.
Click Close to finish the installation
procedure.
Page 22

4 Data handling
Any successful experiment relies on a safe and reliable storage of its
outcome. Moreover, the quality of a measurement may not be
immediately apparent so the data has to be analyzed in a second
step. The format of the stored data has to be compatible to all tools
the user might want to employ. In this sense, the act of saving the
experimental outcome is a task of major importance in the course of
the experiment. In the design of the ASC500 and its software, this
importance was especially emphasized.
The software allows for fast and flexible procedures of data storage:
 data can be saved on a time base from microseconds to
hours
 data can be saved in a multiple of 1D, 2D and 3D file formats
 user defined data groups can be saved by one single mouse
click
 automatic snapshots and text files containing parameters
are generated
 all file formats are compatible to all major analyzing
software (SPIP, MountainsMap, Gwyddion, Wsxm, ...) or can
be directly viewed in the Windows Explorer
The following chapter will explain in detail the data storage
capabilities of the ASC500 controller.
4.1 Quick guide for data saving
The next section will give a short overview and provide a quick entry
on how to use the controller’s data storage capabilities. The following
sections will give all necessary details for getting the maximum
flexibility and time efficiency out of the product.
4.1.1 The Data Channel Configuration dialogue
The central point for all data related processes in the ASC500 is the
Data Channel Configuration dialogue (DCC). It is used to define what
signals are accessible in the various modules of the controller and
how these signals are saved. The DCC is accessible from various
points of the graphical user interface (GUI) via the icon that is shown
to the left.
Page 23
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Figure 8: The Data Channel Configuration dialogue.
Figure 8 shows the DCC in a typical SPM configuration. In the bottom
half of the window the Line and FFT tab can be found, in which one
can set the saving configurations for the Line View and Frequency
analyzis tab in the Main Control. The Filename textbox defines the
name of the saved file and must not be empty. Via the Signal drop-
down list the channel to be saved can be chosen. To record multiple
channels, one can add additional channels via the Add button
underneath the Line and FFT tab. The SampleTime textbox sets the
time interval between to samples. It is unit sensitive and will
automatically add the last correct unit if the input is just a number. It
recognizes the units ms (millisecond) and µs (microsecond) which can
also be written as us. The AVG checkbox defines, whether the saved
value corresponds to a specific readout at the moment of sampling
(unchecked) or if it is averaged over one SampleTime (checked). For
Page 24

optimal results, we recommend to keep this box checked. As the Raw
and Displayed data for the Line and FFT tab are identical, the Ascii
and Bin. checkboxes will always be disabled. If the Log checkbox is
active, the raw data is stored continuously in ASCII formt. The Snapsh
and ASCII checkboxes enable the storage of the data in PNG and/or
CSV format if one of the SNAPSHOT icons (shown to the left) is
pressed.
The SCAN data group on the top of the DCC is responsible for all data
collected during an xy raster scan and is thus of major importance.
Normally, at least two channels will be defined here:
 One will be the topography signal, defined as the output of
the z controller. The corresponding signal is called Z out inv
as shown in the example above.
 The other could be the error signal of the z controller. For
contact mode AFM, this would be the deflection signal
usually connected to ADC1. For non-contact AFM, it would
be the output of the lock-in called HF 1 Ampl. For STM, it
would be the tunneling current, again usually connected to
ADC1.
The AVG, RAW BIN, RAW ASCII and DISPLAYED SNAPSH checkboxes
should all be checked to save the SCAN data in a binary data format,
a text type data format and as a snapshot image. The Checkboxes
under Raw and Displayed differentiate between the unchanged
recorded data and the data displayed as an image in the main control
that might be different depending on the Underground Filter
settings. Any number of additional data channels can be added by
clicking the ADD button. As the SCAN data is resolved in a special
manner, a continuous storage is not possible, thus the Log checkbox
will always be disabled.
For most experiments, one or more spectroscopy and/or resonance
features will be necessary. The data channels needed for these
operations can be created in one of the Spec tabs and the Resonance
tab.
DCC Spectroscopy Tab
Page 25
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

DCC Resonance Tab
With the settings shown above, all of the basic experiments in
scanning probe microscopy can be done. Scan data will be recorded
on several channels simultaneously, spectroscopy and resonance
experiments can be done and any given signal can be examined in a
line and FFT display. The recorded data can be stored to the hard disk
by clicking on one of the snapshot icons in a display. The snapshot
trigger in a SCAN display will save the data of all SCAN data channels
simultaneously. The data will be stored in a multitude of formats: For
example, the SCAN data of Figure 8 will be saved in averaged binary
type format and in addition as a picture file. There will be separate
files for both forward and backward scan direction. There will also be
a snapshot of the SCAN line view and an extra text file with all the
relevant scan parameters. All of this will be saved by a single mouse
click and all files will automatically be numbered and grouped.
The time of the data saving will depend on the type of snapshot icon
that is used for triggering the data storage.
The Snapshot Immediate will save all data in its current state: It may
be a half-filled SCAN image or any arbitrary fraction of a LINE display.
Snapshot Delayed will save the data at the next completion of the
underlying operation. A SCAN will be saved when the scan area has
been completed, a spectroscopy will be saved once the sweep range
has been swept through.
Snapshot Repeat will turn the Snapshot Delayed function on an
endless cycle. The cycle can be stopped with a following click on the
Snapshot Repeat button.
4.1.2 The Snapshot Preset Configuration
A click on the snapshot icons within a display will trigger the data
storage of the complete data group that corresponds to the display.
I.e. a snapshot trigger in a SCAN display will save all data channels
belonging to SCAN. To save a multiple of data groups simultaneously,
the SNAPSHOT PRESET functionality can be used:
Page 26

For each preset, any combination of data groups can be chosen. Only
data groups with at least one data channel are allowed in the preset
configuration dialogue. Any number of presets can be added with the
Add button.
To trigger the data storage of a preset, the preset icons shown to the
left can be used. The icons can be found in the main status line of the
Daisy program. To reach the Snapshot Preset Configuration dialogue,
the leftmost icon has to be clicked. The drop-down list is used to
choose the preset for the next saving process. The preset snapshot
icons work similar to their local display counterparts described in the
section above.
After this short overview, the next section will give details and
background on the data handling and saving capabilities of the
ASC500 SPM controller.
4.2 Data handling details
4.2.1 Signals, data channels and data groups
A signal is a stream of data that can have two origins:
1. The signal is directly sampled through one of the input
connectors. This would be called an external signal. There
are 8 external signals that are named after its input
connector (ADC1, ..., HF1 IN, ..., Counter)
2. The signal is generated within the ASC500 (internal signal).
Internal signals could be the output of a PI controller (Z_out)
or a lock-in (HF 1 Ampl, HF 1 Phase).
Signals are routed into data channels. A data channel combines the
measurement data with some secondary data that carries additional
information like the position within an image or a time stamp.
It is common that several different signals are measured in the same
context and need the same secondary data. One typical example
would be a scan where multiple signals should be recorded parallel
and hence combined with the same location information. Therefore
data channels are divided into different groups depending on the
context of the data.
Furthermore the same signal is often needed in different context and
hence data channels at the same time. For example, the deflection
read-out of an AFM (connected to the ADC1 input) could be used for
recording the topography and feeding the FFT module at the same
time. The ADC1 signal would then be used in two data channels, one
Page 27
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

belonging to the data group SCAN and one belonging to the data
group FFT.
Up to 14 data channels can be used at the same time.
4.2.2 Internal Signal Flow
The ASC500 SPM controller features a very flexible architecture.
There are many different ways to route the signals between the
internal controller modules to gain maximum functionality. Figure 9
gives an overview of this internal signal flow. The most important
controller functions are illustrated by boxes. Each controller function
is connected to other functions via data lines. Data lines attached to
the left of a controller module show all possible input signals for the
respective controller function. Data lines starting from the right side
or from the bottom of a controller module show the possible output
signals generated or altered by the module.
For example, in a standard non-contact mode AFM measurement,
the intensity signal would be attached to the HF IN connector on the
front panel. The signal that is carrying the lever information is HF 1
which is automatically routed into the high frequency HF Lock-In. The
lock-in demodulates the HF 1 and generates the HF 1 Ampl signal
which can then be used both as an input value for the Z Controller
and also to feed a two-dimensional display during the scan in the
Data Collection module.
Page 28

Figure 9: Internal Signal Flow Diagram. This diagram gives an overview on the relation between input and
output connectors, the names of the signals and the most important controller functions. Data flow direction
is from left to right (otherwise indicated). Each controller function is depicted by a box, all possible input
signal are shown on the input side of the box, the output signal are shown to the right of the box.
The controller modules shown in Figure 9 are explained in more
detail in section Operating the Controller of this manual.
4.2.3 Data processing chain
The diagram of the data processing chain is shown in Figure 10. All
signals are either captured or generated within the physical unit of
the ASC500 controller. The data is subsequently averaged according
to the user’s settings (defined in the DCC, see 4.2.5). After
transmission to the PC via USB, the data is stored in a buffer. The
content of the buffer can be saved directly to hard disk, choosing
from various types of file formats. In addition, it can be routed to a
display (optionally via one or more filtering stages). The content of
the display can then again be saved either in a Windows picture
format (for fast overview via Windows explorer) or in a data format
that now includes the filter stages (pre-processed or as-displayed
data).
Page 29
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Figure 10: The data flow chain of the ASC500
4.2.4 Sample Time and Average
All internal and external signals use an internal general time base of
2.5 µs. This time corresponds to the 400 kHz sampling frequency of
the general ADC inputs. In some cases, data is needed only in a slower
repetition rate. In the Daisy GUI, the repetition time for signals is
called Sample Time. If the Sample Time is set to a value larger than
the time base of 2.5 µs, data has to be reduced. The user can choose
from two options on how to reduce the data:
1. Averaging ON: All values recorded within a Sample Time are
averaged.
2. Averaging OFF: The first value of the Sample Time sets the signal
value and during the rest of the sample time, all other incoming data
is ignored.
The data reduction is done in the ASC500 controller in order to
reduce the traffic on the USB connection between ASC500 and PC as
much as possible.
The Sample Time of all channels within one data group will be equal.
However, there are two exceptions: The LINE and FFT groups leave it
to the user to define a separate sample time for each channel. For all
groups, the Sample Time is defined in the respective parts of the GUI
corresponding to the data group. For example, the Sample Time for
the SCAN group is set via choosing the scan speed. The Average
Page 30

option can be set in the DCC. It is set to Average ON for all channels
per default.
4.2.5 Data Channel Configuration (DCC) in detail
A central point for the configuration of the data processing chain is
the Data Channel Configuration dialogue (DCC). It can be accessed
from various points in the graphical user interface by clicking on the
DCC button shown to the left. In the DCC, data channels are created
and signals are assigned to the data channels.
The DCC is also the place to select file format for the data saving. It
is important to .
The data channels are sorted in the following groups:
SCAN data associated with the scan motion. Each data point
is referenced within a 2-dimensional frame and has
been recorded in either forward or backward direction.
Data from the SCAN group can be represented in either
a two dimensional display (called a frame view) or as a
one dimensional display showing single or multiple
lines of the scan.
DUAL PASS data associated with the Dual Pass Mode (see 6.5.7
Dual Pass…………………………… on page 92. If he dual
pass mode is set to ON, the data group 2nd PASS
represents the data collected during each second line.
Since the origin of the data is very similar to the data
of the SCAN group, it can be viewed with the same
display types.
SPEC1, SPEC2, SPEC3
data associated with the Spectroscopy feature. It will
be displayed in a 1D type display.
RESONANCE data associated with the Resonance feature.
Representation: Two 1D type displays, usually showing
the amplitude and phase of a lever against frequency.
SOFT SPEC data associated with the Soft Spectroscopy feature.
Representation: 1D display.
Page 31
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

The above image shows the lower part of the DCC with both LINE and
FFT data groups.
LINE no data association. Any signal can be shown against
time. Representation: 1D line, multiple 1D line.
FFT no data association. Any signal can be shown in
frequency space: Representation: 1D line.
4.2.6 DCC usage
Before the experiment is started, the data channel configuration has
to be defined in the DCC. After the definition, the data channel
configuration can be saved by saving the GUI profile under File – Save
Profile or Save As. The different sections of the DCC are described in
more detail below.
1 – Using the Add button, a new data channel can be created in the
current data group. Up to 14 data channels can be distributed at the
same time between the data groups. Please note that it is not
possible to add data channels during operation. For Examples, during
a scan no channel can be added.
2 – The current filename index number is shown here. It will be
automatically increased with each saving process. This number
cannot be edited.
3 – Reset the File No to 0.
4 – Filename used for storing the data of the data channel.
5 – The Signal that will be routed into the data channel.
6 – Average button. The signal will be averaged over its sample time.
See 4.2.4 for more details.
7, 8, 9, 10, 11 – Here, the file and data format for the disk storage of
the data can be defined. There are in general five possible formats.
Page 32

Not every data group has all five formats available. A more detailed
description of the formats is given in section 4.2.7.
12 – The Remove button will remove the corresponding data channel
from the data group. Please note that the first data channel of both
LINE and FFT data group cannot be removed.
4.2.7 Saving the data
Available options There are several options for the storage of each data channel. In
general, the data can be saved in either RAW or as DISPLAYED (see
Figure 10 for clarity). RAW means that the data is taken from the
buffer, i.e. before any filtering. For example, SCAN data will be saved
without the underground filter if the RAW option is chosen. The
DISPLAYED option will save the data as it is shown in the
corresponding display, i.e. after the filter stages. NOTE: the
frequency spectrum of the FFT display is achieved through an “FFT
filter.” To save the spectrum you must select one of the DISPLAYED
formats.
RAW ASCII: The data of the channel will be saved in an ASCII type
format. The data will be stored as recorded. For SCAN and similar
data groups, there will be one file for forward and one for the
backward direction. This format is available for SCAN, 2nd PASS,
SPEC1-3, CALIB and SOFT SPEC data groups.
RAW BIN: The data of the channel will be saved in a binary format.
The data will be stored as recorded. For SCAN and similar data, there
will be one file for forward and one for backward direction. This
format is available for SCAN, 2nd PASS and STEP SCAN data groups.
LOG: The LOG option is only accessible for LINE data. This option will
write the data to a file as a stream of points, one point with each
Sample Time. The resulting file will be of ASCII (text) type. Please note
that LOG files can get very large, so it is advisable to use the log
function only with large Sample Times. The logging is started and
stopped by using the Snapshot Repeat button in the respective LINE
display.
DISPLAYED SNAPSHOT: If checked, the data will be saved as a screen
snapshot of the current display. It will be saved in a PNG file format
by default, but the format can be changed using the Settings –
Preferences – File Output – Snapshot Format. This feature is
especially useful to provide an overview on the stored data. Later it
can be quickly browsed using the Windows Explorer. NOTE: As with
all DISPLAYED save options, data will only be saved if the channel is
shown in a DAISY display. For SCAN channels, both forward and
backward scan snapshots will be saved, even if only one direction is
shown on the screen.
DISPLAYED ASCII: The content of the display that shows the data
channel will be stored in a text type format. In contrast to the RAW
ASCII option, the file will contain all data changes resulting from the
filters the data might have passed. Again, the data will only be saved
if the data is shown in a display at the time of the saving trigger.
Page 33
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Triggering data storage
Each display in the Daisy GUI contains three buttons for issuing a
saving trigger (shown to the left). These buttons will be used to
trigger the process of data storage
The Save Immediate button will save the data in its current state, i.e.
a scan frame that is half filled or a fraction of a LINE VIEW line.
The Save Delayed button will store the data when the corresponding
data unit is completed for the next time. This means that a scan will
be saved once the frame is finished and a spectroscopy will be saved
as soon as it is completed. A save icon will appear above the top right
corner of the corresponding display to note that a data storage
process is pending.
A third option is the SAVE REPEAT button. With this button pressed,
the data will be repeatedly saved in a manner that is equal to the
SAVE DELAYED option. For example, a scan will be repeatedly saved
every time the complete scan area has been imaged. The procedure
can be stopped by a second click on the SAVE REPEAT button. For
LINE data, the SAVE REPEAT button can have two meanings: 1. If the
LOG option in the DCC is chosen, the data will be saved as a
continuous data stream in one file, one data point for each sample
time. 2. If the LOG option in the DCC is not chosen, the SAVE REPEAT
for LINE data will work similar to all other data groups: data will be
saved at the moment the display is full.
Triggering the data storage will always save all channels of the data
group. For example, a click on a SAVE button in a frame display will
write all data belonging to the SCAN data group to the hard disk. This
will be both the 2D image, but also the 1D data of the corresponding
scan line view (meaning the line view that shows the scan data line
per line). There are, however, two exceptions for this rule: The LINE
and FFT data group behave differently: Here, a SAVE trigger will only
store the data channel shown in the display where the SAVE is
triggered. If there are several displays with LINE information and all
of them need to be stored to hard disk, the user needs to click on all
corresponding SAVE buttons. Another possibility is to use the
Snapshot Preset option of the DAISY GUI to combine any combination
of data channels to be saved with one mouse click (see next section
4.2.9). The reason for the different behaviour of LINE and FFT data
compared to all other data groups is that the time scales of various
LINE or FFT displays may be very different. One LINE view could show
a signal on a microsecond time scale, while another LINE display
could very slowly log data from for example a temperature
controller. The splitting of both LINE’s saving process allows for a
separate data storage for either long term or short term data. The
differences between LINE/FFT compared to other data groups is also
highlighted in the splitting of the DCC, where LINE and FFT are shown
in the extra lower part of the DCC window.
Filename Convention
Page 34

The filename will be composed from several parts. The name starts
with a prefix referencing the data group followed by an index
number. The index number will automatically increment after each
saving cycle. The next part of the filename is the data channel name
as entered by the user in the DCC. This is followed by an extension
providing some closer description of the file. For SCAN data, this
could be ‘fwd’ or ‘bwd’, denoting the scan direction. It could also be
the name of the display in case the data is saved AS DISPLAYED.
Finally, the Windows filename extension shows the file format. A
large number of files can be created by one save trigger. These files’
filenames will all start with the same prefix, so it will be immediately
clear that they are all based on the same data.
Here are several examples:
SC002-Topography-bwd.asc
This filename is composed as follows:
SC SCAN data group
002 index
TOPOGRAPHY name taken from DCC
BWD backward scan
.ASC 2D ASCII type format
S1002-Tunnel Current-Spectroscopy 1.png
S1 data group SPEC1
002 index number
TUNNEL CURRENT Name from DCC
SPECTROSCOPY 1 Name of the display that was the origin of the
snapshot. The existence of the display name within the filename is a
sign that the data was saved as DISPLAYED.
.PNG picture file format
The name of the display can be changed by clicking Rename in the
right-click context menu of the respective display (section5.4.2).
If a filename is already used in the target directory, DAISY will
automatically add a ‘[number]’ part to the filename to avoid conflicts
and to guarantee a successful storage of the data.
Target directory All files will be stored in the same directory. This directory can be
changed at any time under Settings – Preferences – File Output -
Target Directory.
File formats All data saved by Daisy will contain a file header that is readable with
any standard text editor. A typical file header looks as follows:
# Daisy line view snapshot
# 2011-02-01T07:26:35
# display: FFT Display
# x-pixels: 813
# x-unit: Hz
# y-unit: V
X ; Y
Page 35
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

In this case, an FFT display was saved with a content of 813 pairs of
voltage versus frequency data points, in the unit of Hz.
After the header, the file contains the measurement data in either
ASCII or binary format (depending on the file format type). In case of
an ASCII file format, the data is written in a form similar to the last
line of the header: Two columns separated by a semicolon.
The following table provides an overview on the available file format
types:
ASC BCRF PNG CSV
SCAN + + + -
SCAN LINE - - + +
DUALPASS + + + -
SPEC 1-3 - - + +
CALIB - - + +
SOFT SPEC - - + +
STEP SCAN + + + -
LINE - - + +
FFT - - + +
Note: SCAN LINE data is not a separate data group but belongs to the
SCAN data group and is saved by the same trigger. SCAN LINE data is
only available AS DISPLAYED and will thus be saved automatically if
one of the DISPLAYED checkboxes in the SCAN section of the DCC is
marked.
ASC Format The ASC format is used for 2D data (SCAN, DUAL PASS). The data will
be written to a file as ASCII text. The resulting files can be opened in
a text editor or any standard image analysing software. Due to the
nature of text files, the file size will be 2-5 times larger than its binary
counterpart BCRF. There are two slightly different versions of the ASC
file format:
 The data points are separated by a line feed.
 Data within one scan line are separated by a TAB and the
end of a scan line is marked by a line feed (line oriented).
To choose between these two options, a checkbox under Settings –
Preferences – File Output – ASC Format can be used.
BCRF Format The BCRF is the binary counterpart of the ASC format and can be used
for the same data (2D data). After the ASCII header, the data points
are saved in a binary format which leads to a file size reduction of up
to 5.
PNG Format This format is a picture type format for screen snapshots. It is
available for all data and display types. The content of the display is
saved to hard disk as it is shown on the screen. For SCAN and DUAL
PASS, the forward and backward scan direction is always saved into
a separate file (even if only one direction is shown in the display).
Page 36

Post processing of the data is not possible with this format. Still,
saving screenshots provides an easy overview over collected data.
The format can be switched between JPEG, BMP and others under
Settings – Preferences – Snapshot Format.
CSV Format The CSV (comma separated values) format is an ASCII/text type file
format for 1D data (LINE, SPEC1-3, FFT). CSV can be imported to every
program that is capable of analysing data sorted in columns and rows
(Excel, Origin, Sigmaplot, SciLab, …)
The CSV files generated by daisy comprises of a header of several
lines masked by #. Different datapoints are separated by CR LF;
different fields by SP;SP. The first line after the header is not a data
point but the title of the columns.
# Daisy frameless snapshot
# 2017-06-20T14:36:37
# display: channel resonance_ampl
# x-pixels: 8
# x-unit: Hz
# y-unit: V
X ; Y
25000.076 ; 0.0594836835
25009.019 ; 0.0600328565
25017.962 ; 0.0594307108
25026.9049 ; 0.0590073759
25035.8479 ; 0.0590793473
25044.7909 ; 0.0586746387
25053.7339 ; 0.0588722247
25062.6769 ; 0.0590837431
4.2.8 Parameter File
For each data storage cycle the software can create an additional text
file, the Parameter File. The Parameter File will contain the most
important parameters that were set in the Daisy GUI at the time of
the saving process. The filename is parameter.txt with a prefix equal
to the prefixes of the corresponding data files. The file is readable
with any text editor. The user can add an arbitrary text to the
Parameter File via Displays – Snashot Comments. The creation of
Parameter File can be omitted under Settings – Preferences – File
Output – Parameter file.
4.2.9 Snapshot Presets
Often during an experiment, several data groups need to be saved at
the same time. For example, FFT and LINE data are a common couple
because they represent complementary information of the same
Page 37
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

physical origin. Also, SCAN and LINE data might be interesting to save
together, if for example the LINE data represents an additional
parameter of the measurement. The DAISY GUI is equipped with
functionality to combine several data groups in presets and save all
data with one mouse click. Moreover, different presets can be
defined and activated via a simple drop down list. Thus a very flexible
and powerful tool for data saving is at hand of the user.
To enter the Snapshot Presets Configuration dialogue, the user has
to click on the button, shown on the left, in the status line of the
DAISY. In the following menu, the data groups can be assigned to
certain presets. Each preset will be represented by one line in the
dialogue.
7
8
9
10
1 2 3 4 5 6
1 – The Remove button is used to remove a preset from the list.
2 – Name of the preset. This is used to identify the preset in the
trigger dropdown list (shown on the left).
3 – Index number of next data filename.
4 – Reset index number to zero.
5 – The Add button is used to add another preset to the list. There is
no limit to the number of presets.
6 – The Close button closes the dialogue.
7 – Data Groups: all data groups with active data channels are visible.
For LINE and FFT data, each separate channel is shown separately
because these channels could potentially be stored separately. For
all other data groups, all data channels of the group is stored
simultaneously.
8 – This line shows either the number of active data channels in the
group or the name of the data channels for LINE or FFT group.
9 – DCC shortcut. To change the data channel configuration, a click
on this icon leads to the DCC.
10 – These checkboxes are used to add the corresponding data group
to the preset.
Snapshot Preset Filename The filenames created by the snapshot presets are composed
Convention similarly to the filenames from data group storage. The difference is
Page 38

the prefix numbers. All filenames saved by a snapshot preset begin
with the preset name.
1) Prefix: Preset name+ 3-digit number. P0 corresponds to the
first preset, P1 to the second and so on
2) Data channel name
3) Name of the source display
4) For SCAN data: denotation of scan directions; fwd or bwd
5) Filename extension
Example:
P0001-ln_1-Line View.csv
This filename is composed as follows:
P0 preset name
001 index number
ln_1 data channel name taken from the DCC
Line View name of the display (marks the data that was
saved AS DISPLAYED)
.csv text type data format (‘comma separated values’)
How to trigger a snapshot preset
The data storage of a Snapshot Preset is done via one of the three
snapshot buttons shown to the left. These buttons can be found in
the main status line of the Daisy program. The usage of these buttons
is very similar to the snapshot icons from the data group storage (see
page 34).
Page 39
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

5 Operating the Controller: General Usage and Overview
This chapter gives a general overview on the Daisy software and its
functionalities.
5.1 Software Installation and Getting Started
Make sure your controller is switched off.
The attocube ASC500 software Daisy is distributed in two different
formats: an installer executable and a zip folder.
Double clicking the executable will start an installation routine that
will install the drivers, copy all necessary files to the hard drive and
create a desktop shortcut.
If the drivers are already installed it is also possible to simply unpack
the content of the zip folder to your hard drive and run the file
‘daisy.exe’.
Switch on the controller.
Open the ‘daisy.exe’ file. If your firewall is
activated, the following error message
appears. Choose “Unblock” to go on.
Now, the ASC500 hardware is
automatically booted and the window as
shown to the left appears.
Remark: by booting the hardware, all FPGA
and DSP code is transferred from the
computer to the controller, thus defining
its functionalities. Please note that
upgrading to a new software version
requires starting the new version of the
Daisy program and rebooting the
controller. All changes will be automatically
programmed into the hardware.
Page 40

5.2 Description of Main Daisy Program
After booting, the main program is running (see
image below). It enables the connection to the
hardware and handles data inputs and outputs.
Also, it can reboot the controller and send new
boot code. Yet, for controlling parameters and
outputs of the ASC500, a profile has to be loaded
that defines the graphical user interface (GUI). A
profile (*.ngp) consists of saved settings and a
panel (*.ngc). Hence, user settings can be saved
with the profile.
On the lower right there are three status LEDs
(from left to right):
- the server is connected to the hardware
(green LED),
- the server is receiving data (green),
- an overload error occurred (red).
5.2.1 The main toolbar
Load/ Save Profile. Profiles and panels can also be loaded and saved
with the File menu.
Close/ Detach/ Collect Panel. If you have loaded one or several panels,
it is possible to detach them from the server application or re-collect
them also by using the Window menu.
Always on top. If this button is checked, Daisy windows will always stay
on top of other windows running on the computer.
Display wizard. You can open additional data windows using the
display wizard. Please see section 5.4.4 on page 53 for further
information.
Warning messages. Press this button to show the warning messages
window. This window can also be configured to pop up on every new
message by clicking the checkbox Popup on new Message. From the
window you can clear the whole list, or check single messages to delete
them.
Page 41
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Snapshot Presets: Data of different context can be saved within one
mouse click. The Snapshot Preset icons shown to the left are used for
this functionality. Further details on data handling and saving are given
in section 4.
Start/ Shutdown Server. The server application on the PC as well as
the hardware can be booted or shut down using the Server menu. The
boot messages from the server program can also be opened here. In
case of problems, the Server Output can help to trace a problem.
Daisy settings. Open the preferences dialog to change certain global
settings.
The File Output tab features the following settings:
Data Save Path: Set the target directory in which all
data / snapshots will be saved by selecting a path with
the Open icon to the right.
Profile Save Path: Set the target directory in which the
profiles will be saved.
Snapshot Format: You can choose between bmp, png,
ppm, xbm & xpm file formats for the snapshots.
Text Format: For 2D data, choose between Line
Oriented ASC and one data point per line. For multiple
curves, use multiple columns in .csv files or
alternatively, write multiple curves one after another.
The Behavior tab features the following settings:
Confirmations: Check the corresponding boxes if you
want to be notified before exiting the program, and
before overwriting panels respectively.
Displays: Check the corresponding boxes to activate
Always on Top for the displays, and for enabling 3
dimensional data displays (available upon right-
clicking in a frame view). Since this functionality is not
supported by all PC hardware configuration, the 3D
views option is set to OFF by default.
Connectivity: Allows connection to the ASC 500 server
remotely. Use with care as the network often is not
reliable enough.
Page 42

Simulated Device: On Ethernet can be used to connect
to a Daisy that is connected to the same network as
the computer running the daisy software. Check
Simulated to start the Daisy in simulation mode
(without actually connecting to the ASC500
hardware).
Export settings: Check this box to show the Expert
Settings.
For any of the changes to take place you have to
restart Daisy.
5.2.2 The menu bar
In addition to the standard menu entries as already described above, there are the following options
available in the main menu bar:
The File menu contains the following entries:
Load Profile: Click here to load a profile (.ngp).
Load Panel: In addition to profiles (.ngp), there is also a
number of preconfigured panels (.ngc) available.
Reload: Use this option to reload the current profile. This
option is helpful if e.g. settings have been changed which
will only come into effect after reloading the profile.
Save Profile: Use this option to save you profile.
Quit: Exit the program.
The Window menu contains the following entries:
Detach: Use this option to detach the current display from
the main Daisy window. This option is particularly useful
when using more than one screen or very large screens.
Collect: Use this option to re-attach detached displays to
the main GUI window.
Close: Use this option to close the current display.
Close all: Use this option to close all displays at once.
Warnings Window: Shows the warnings message window
The last entry consists of all currently active / open displays;
use this to switch between the different windows.
The Displays menu contains the following entries:
Page 43
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Display Wizard: See the corresponding section above
(section 5.4.4).
Preset Snapshot: These entries can be used to configure
and trigger the preset snapshots (section 4.1.2).
Snapshot Comment: Here you can enter comments which
will be saved in the parameter file.
The Server menu contains the following entries:
Start & Shutdown: See the corresponding button
descriptions above (section 5.2.1)
Server Output: This opens a window which lists the
communication between the Daisy server and the
hardware.
Reboot Controller: Use this option to reboot the controller.
The Settings menu contains the following entries:
Daisy Settings: See the corresponding button description
above (section 5.2.1).
Output Data: This opens the DCC window, see description
in section 4.1.1.
Aliases: This opens a window to adjust the names of
different data channels and windows. It is described in
detail below (section 5.3.2).
Experiment Preferences: This opens a window with several
tabs for certain settings associated with program behaviors
during experiments (in contrast to the Daisy Settings
menu), which are described below (section 5.2.2.1)
Transfer Functions: This opens a window allowing to set
transfer functions. The details are described below (section
5.2.2.2).
The Help menu contains the following entries:
About Daisy: Here you can find information about the Daisy
software version as well as licensing issues.
About Hardware: Here you can find information about your
current ASC500 hardware.
5.2.2.1 Experiment Preferences Window
Page 44

In this tab, you can change the different
Feedback Clocks, which correspond to the
sampling time of the different Feedback loops.
Closed Loop Sensor: Inverts the axes if the
positive direction of the scanner matches the
negative direction of the sensor readout. This
item is only visible if the CL scanning upgrade is
unlocked in the ASC500.
Scanner Acceleration: This can be used to
prevent quick change of direction at the end of
a scanline to reduce shaking.
Page 45
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

The ASC500 has a dedicated input port for low-
voltage TTL pulses. Within the software, a
counting procedure keeps track on the number
of received TTL pulses. It can be used to display
the number of counts in any line or frame view.
To use the counter, please connect the source of
the pulses to pin 1 of the External In connector
(see Figure 3 in section 2.3.4).
Please note that the ASC500 accepts only low-voltage TTL pulses, i.e.
pulses with an amplitude of 3.3 V. The maximum repetition rate is 20
MHz.
To activate the Counter in the software, go to Experiment Preferences
tab and enter an Exposure Time for the counter. The exposure time is
the time interval in which the incoming pulses are accumulated. The
exposure time can range between 2.5 µs and 163 ms in 2.5 µs steps.
The counter signal can be chosen in all line and frame displays. If the
sample time of the display is larger than the exposure time, a number
of exposures can be averaged. In case the exposure time is larger than
the display’s sample time, a number of samples will be equal.
Page 46

This feature is not used anymore.
5.2.2.2 Transfer Functions Window
The Transfer Functions offers the following functionalities:
1. Conversion of the voltage values read by ADC inputs towards
physically meaningful units. For example, if a photo-detector is used to
collect your data, Daisy can display it in Watts. Use External Transfer
Function for the conversion.
2. Calibration of the ADC inputs. ADC voltage inputs usually show small
voltage offsets in the milli-Volt range. You can compensate for this
offset with the Internal Transfer Function.
3. Setting of a working point and an additional preamp gain. If you have
e.g. a small signal on a constant DC voltage, you can compensate for
this DC part and increase the gain for this channel.
External Transfer Function Gain: Enter the conversion factor in Unit/V. For example, if a photo-
detector with an amplification of 5e6 V/W is used (corresponding to
0.2 µW/V), you can enter either Gain = 0.2 and Unit = uW or Gain = 200
and Unit = nW. Please note that Daisy automatically displays the
Page 47
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

appropriate unit prefix (nano- or micro-Watt) independent of the Unit
setting.
Offset: Adds an offset to the signal.
Internal Transfer Function Factor: Use this factor to correct for an ADC gain different to 1. Please
note that the actual signal will be divided by this factor.
Offset: Offset value to be added on the respective ADC.
Active Compensations Bias Comp. Enable: Enable the active bias compensation.
Bias Comp.: Enter the DC offset on the input signal that is to be
subtracted.
5.2.3 Loading a profile
In order to perform a Scanning Probe Microscopy (SPM) measurement,
a profile needs to loaded, which defines the graphical user interface
(GUI):
Open a profile of your choice, e.g. “afm.ngp” for
atomic force microscopy.
After opening the GUI, the main panel appears
(see below). In the main panel, all functions of
the AFM can be controlled.
Special GUIs are available for all attocube
systems microscopes. These have been
developed to adapt for the use of the specific
instrument and hide some of the controls to
facilitate the usage. The according profile files
are shipped with the system.
5.3 Profile configuration
While preconfigured profiles (.ngp) are available for the most common
scanning probe methods, the new Daisy release v2.7 allows the user
to customize certain parts of the GUI. This will be described in the
following section. Besides, parameters (like output limits, scan ranges,
Page 48

slew rates etc.) are also stored in the profile, this allows every user of
the instrument to create his/her own profile.
5.3.1 User-configurable GUI appearance
By right-clicking on any of the tabs in the main GUI, the user can decide
whether to show, hide or detach it:
The order of the tabs can also be changed by dragging and dropping
any of the tabs to a new position within the tab bar.
The configuration of each tab section can be stored by creating a
customized profile.
5.3.2 Aliases menu
Since both the ASC500 hardware as well as the Daisy software serve
the purpose of a powerful generic, multipurpose SPM controller, many
of the signals, parameters and tab names within the software have
been kept generic. However, most users will only perform one or two
specific SPM methods and use a well-defined sets of parameters for
their experiments. To make life easier, the software offers the
possibility to rename most of the generic resources in the Aliases:
Page 49
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

In the corresponding tabs one can set new Aliases
for Input, Output or Internal signal names, change
the label of spectroscopies or coarse axes.
Note: In certain version of the Daisy software the new Aliases for the
resources will not come into effect until the current profile is saved
and reloaded.
5.3.3 New signal and parameter names in v2.5 and later
Starting from v2.5, several signals, parameters and tabs in the GUI have been renamed compared to previous
versions of the Daisy software (or have been equipped with the opportunity of aliases). The following table
lists the changes in order to help existing users with an updated Daisy software to get an overview of the
mapping between old and new names:
Signals
Previous name New name in v2.5
SPM Z out Z out
SPM Z out inv Z out inv
AFM signal HF 1
AFM df HF 1 df
AFM Aexc HF 1 OUT
AFM Aosc HF 1 Ampl
AFM Phase HF 1 Phase
LockIn Ampl LF Lockin Ampl
LockIn Phase LF Lockin Phase
Page 50

Tabs
Previous name New name in v2.5
Calibration Resonance
LockIn 2 separate tabs:
- LF LockIn
- Lever excitation (=HF 1)
2nd Pass Dual Pass
Pref tab removed!
see:
- Output Limits (section 6.1),
- Experiment settings (section 5.2.2),
and
- Transfer Functions (section 5.2.2)
Transfer moved to Settings menu → Transfer
functions (section 5.2.2):
all 6 transfer functions are now
combined
5.4 General Usage and Description of Common GUI Controls
5.4.1 Text Edit Boxes Most parameters of the experiment are controlled by entering
numbers into text edit boxes. The Daisy software provides a simple
and intuitive way of entering numbers.
Most numbers are accompanied by a physical unit. When entering or
changing a number, the units do not have to be entered. Just type the
number and press return; Daisy will automatically add the appropriate
unit. Most of the time, a unit such as ‘meter’ will come with a
convenient SI prefix like ‘nano’ and the edit box will show ‘nm’. There
are two ways of changing the prefix:
1. Enter a value greater than 1000 or less than 1. If you enter for
example 1200 and the old unit is ‘nm’, Daisy will change to
microns and show ‘1.2 µm’.
2. Type the new prefix behind the number. Entering ‘1.2u’ will
result in ‘1.2 µm’, regardless what the old prefix was. Use ‘p’
for pico-, ‘n’ for nano-, ‘u’ for micro-, ‘m’ for milli- and ‘k’ for
kilo.
If you do not enter a prefix, Daisy will keep the last prefix. The only
time you’ll have to enter the unit itself is when you want to change to
a number without prefix, like ‘5 Hz’. Please note that in this case it is
usually sufficient to enter the first letter of the unit, so ‘5h’ will result
in ‘5 Hz’. There are a few parameters without units. In these cases the
way to go back to a number without prefix is to either type 0.1 k or
1000 m.
Using the mouse wheel The mouse wheel can be used to conveniently edit the value of any
text edit box containing a number throughout the Daisy program. If
the cursor is positioned on a text field, the field’s value can be
Page 51
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

increased by turning the mouse wheel upward and decreased by
turning the mouse wheel downward.
The sensitivity of the mouse wheel increment can be set for each text
edit box separately by using the Step Width function in the field’s
context menu. It can be chosen between relative (default) or absolute
steps. Even without using the context menu, the sensitivity of the
mouse wheel can be increased by pressing the SHIFT and/or STRG key
during turning of the mouse wheel.
5.4.2 Context Menu By right-clicking on any graph window, one can open the
corresponding context menu. The functions that are available to the
graphs are the same throughout the program. The context menu is
shown on the left.
Ranges The X Range and Y Range of the graph can be explicitly set. Deactivate
the Automatic check-boxes to enter the range values manually. Please
note that it is not recommended to use the manual X Range
functionality. In the FFT graph, please use the Fmin/Fmax parameters
instead.
The Curves value allows for displaying several adjacent traces within
the same graph. The traces will be displayed in different colors for
clarity.
Click on Close to close the window.
Show Toolbar If the Show Toolbar button is activated, several toolbar icons will be
shown below the graph:
Rescale X range manually. This changes the status of the Automatic
checkbox in the Line View Ranges tab. Moving the mouse wheel while
hovering above the graph will change the shown range. Exact values
can be entered in the Line View Ranges tab.
Rescale Y range manually.
Page 52

These buttons represent the Frame Tools. When active, certain
operations to modify the data range can be performed. See the
description of the Frame Tools in the Data Display section 6.4.
Clear the display. The current data will be deleted and the graph will
start over. Useful if you have chosen a slow display.
Stop the display from being updated. The graph will stay until cleared
or Stop is pressed again.
Freeze Curve This function freezes the currently displayed curve to be used as a
reference. The frozen curve can be erased using the Clear Display
function.
Clear Display Use this option to clear the current display.
Rename Here you can rename the snapshot data of the current display.
Detach Window Use this function to detach the graph from the Daisy window into an
independent window. You can then resize this window and move it
wherever it suits you best. This is especially useful when you use a
system with two monitors. This function can also be accessed by
double-clicking on the graph.
You can reattach the window either by using the context menu of the
new stand-alone graph (Attach window), by right clicking on the empty
space in the Daisy window and selecting Attach Window, or by simply
closing the window.
5.4.3 Frame View context menu
The Frame view context menu mainly offers the same options as
described above, but in addition, one can also activate a 3 dimensional
data view (3D view), and/or change the Color Coding. One can choose
the colors which provide best contrast for the data.
5.4.4 Display wizard The Display Wizard is a powerful tool to personalize the GUI and to
open access to more data windows. It is possible to create line and
frame views (and combinations thereof) and to apply filters. The data
in these windows can be integrated into the automatic global snapshot
routine, giving you the possibility to save all interesting data with one
mouse click.
One example of use would be the Lift Mode, where one requires an
additional data display for the second pass data.
One can open a new display as described below:
First, click on the Display Wizard button.
Page 53
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

The first wizard window appears, where you can use the
pull-down menu to choose the data group for the new
display that you are about to create. The channels for
the data group can be modified in the now familiar DCC.
For more information see section 4.2.5.
For most of the data categories, there are preconfigured
Extensions available, but you can also select Create New
to manually choose the details of your new display.
If you select one of the preconfigured Extensions, simply
click Finish to start using the new display.
In case you choose a data display that either lacks a pre-
configuration, or that you would like to set up manually,
you are first asked to assign a name to the new display.
Click Next.
Now, configure the processing chain. Select the actions
and elements you want to use for the new display. In this
example, a frame display together with a scan direction
filter and an underground filter is selected. Highlight the
elements on the list to the left, then press the right arrow
button to add the element to the processing chain. The
processing chain will be executed from top to bottom, so
it is important to place the filter before the display. To do
this, highlight the filters in the processing chain list and
then press the up arrow button. Press Finish.
Page 54

The new window will appear. Detach it from the
Daisy window, or keep it as another tab within
your main window. The signal can be chosen via
the drop down list in the upper left of the
window. Set the Scan Direction Filter according
to your needs (forward or backward; Off means
forward and backward, watch out for the arrow
symbol in the upper left corner of the image as
it marks the displayed scan direction).Now the
new display is configured for the measurement
and ready to use.
Note: Not every combination of Trigger, Filter and type will result in a
reasonable display. For example, an underground filter is only valuable
in a SCAN type context.
If you have not done so already, please check
that your desired signal(s) are available as data
channels in the DCC (see section 4.1 for details.)
Page 55
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

6 Description of the default AFM layout
This layout can be loaded by loading the afm.ngp file. It is often already preset in the shortcut on the
desktop.
The GUI is organized in 6 main sections: in the upper half of the screen, the Output Limits (1), Scan Control
(2), Z Control (3) and the Scan Data Displays (4) are located, whereas the lower half contains tab section on
the left for the main parameter functions (5) and a right tab section for the spectroscopies (6), a frequency
analysis and the time-based line view.
6.1 The Output Limits
The upper left corner of the GUI hosts the
control section for the activation of all controller
outputs as well as the settings for their
corresponding limits.
Without the Output Active option activated no
voltages will be applied to any of the analog
outputs of the controller. Some digital functions
(Coarse positioning) will work without the
outputs being activated.
The controller is designed to operate variable
temperature SPM devices. The piezoelectric
Page 56

|     | scanners     |     | in these   | microscopes have strongly  |            |     |      |
| --- | ------------ | --- | ---------- | -------------------------- | ---------- | --- | ---- |
|     | temperature  |     | dependent  |                            | behavior.  |     | The  |
maximum applicable voltage and the maximum
|     | extension    |     | changes    | with  | temperature.  |      | To       |
| --- | ------------ | --- | ---------- | ----- | ------------- | ---- | -------- |
|     | accommodate  |     | this       | the   | controller    |      | offers   |
|     | temperature  |     | dependent  |       | limits        | and  | scaling  |
factors.
|     | These  | can  | be  defined  |     | in  the  | Output  | Limits  |
| --- | ------ | ---- | ------------ | --- | -------- | ------- | ------- |
window under the similarly named button.
The first tab contains the Scanner limits and
scaling details for RT and LT respectively. If a
temperature between RT and LT is chosen in the
main window the software uses an interpolation
formula to calculate the actual limits and scaling
|     | factors.  | There  | can  | be  | seen  in  | the  Current  |     |
| --- | --------- | ------ | ---- | --- | --------- | ------------- | --- |
Temperature table. For the max Voltage a linear
interpolation is used, whereas the Max range is
interpolated with a second order curve.
You can also find switches to toggle between
uni- and bipolar settings for all scanner outputs:
using the latter will also switch between max.

|     | voltage  | ranges  | of  | either  | 0..max  | (unipolar)  |     |
| --- | -------- | ------- | --- | ------- | ------- | ----------- | --- |
or -max..+max (bipolar).
|     | Furthermore,  |     | the  | presets  |     | for  Scanner  |     |
| --- | ------------- | --- | ---- | -------- | --- | ------------- | --- |
Adjustment Speed (which controls the rate at
which the tip position is moved upon changing
the position of the scan field), the slew rate of
the Z output and its polarity can be adjusted.
Feedback reserve defines an extra scan range
margin around the actual scan range which can
|     | be  | helpful  | in  CL  | scanning  | mode  | (check  | CL  |
| --- | --- | -------- | ------- | --------- | ----- | ------- | --- |
addendum).
Slewrate Z determines the maximum speed Zout
can be changed with.
Important Note: Choose all of these settings very carefully, since
wrong voltage ranges (also wrong polarity settings) may damage the
piezos of your scanners.

| Typical  values  | are  stored  | in  | the  respective  |     | profiles  | provided  | by  |
| ---------------- | ------------ | --- | ---------------- | --- | --------- | --------- | --- |
attocube and/or can be found in the respective manual of your
attocube microscope. If in doubt, please contact attocube’s technical
support.
Caution. The output limit is the voltage supplied by the ASC500
controller. This voltage is then typically fed into a voltage amplifier
(e.g. the ANC300) which amplifies this voltage by some factor before

Page 57
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

it is applied to the piezos. The amplification factor for different
attocube systems’ voltage amplifiers are:
ANC250 factor 20
ANC300 factor 15
ANC350 (7 axis) factor 14
Always take the amplification factor provided by your voltage
amplifier into account. Do not exceed the maximum allowed
voltage.
Output Active: With the Output Active button all electrical outputs of
the ASC500 controller can be enabled or deactivated. If disabled, all
electrical outputs are set to zero. The voltages are ramped to 0 with
the slew rates/Scanner adjustment speed defined in the Output limit
window. Therefore the switching procedure may take some seconds.
The LED to the right of Output Active indicates whether the outputs
are active (green) or not (red).
The second tab DAC Limits contains the min. and
max. voltages for all DAC outputs at RT and LT
respectively. Besides, the slew rate can be
adjusted.
As an additional safety feature, the user needs
to allow bipolar outputs for each DAC
separately by checking the corresponding box.
Note: Please be aware that also wrong DAC
limits may damage your hardware. For example
in case of the cantilever based AFM/MFM the
dither piezo, which is usually connected to
DAC1, has a similar temperature dependence
than the scanners.
Page 58

The third tab Readback Voltages contains
displays for the actual voltages of x, y and z (read
back from the controller).
Setting the overload capacity in the fourth tab
Expert Settings has an influence on the behavior
of the Slope Compensation feature (section
6.3.2)
Page 59
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

6.2 The Scan Control
The Scanner Ctrl is the control center of the scan
generation. All important scan parameters, such as
the number of Scan Lines and Scan Columns, Pixel
Size, and Sample Time can be entered here.
Furthermore, an offset for the scan area can be set
(Origin X and Origin Y).
The scan area can also be rotated by entering the
desired Rotation angle.
The green square displays the available Scan Range,
the blue rectangle the set Active Scan Area and the
red dot the actual position of the scanner. The grid in
the background depicts the global coordinates of the
system (if the CL scan engine is active).
The position of the red dot is calculated based on the
voltages. The software uses linear interpolation for
the actuator scaling. The position is calculated
according to the following formula:
𝑝(𝑥/𝑦)
𝑝(𝑥/𝑦) = 𝑚𝑎𝑥 𝑉(𝑥/𝑦)
𝑉(𝑥/𝑦)
𝑚𝑎𝑥
Where p and V are the position and the voltage and
the upper index denotes the axis (x or y). The max
signifies maximum value set in the Output limits
window.
Note: Rotation is done by hardware mixing of the x- and y-channels.
This has the great advantage of a smooth and step-free rotation as
compared to digital rotation.
Due to this analog mixing procedure, there is a small error to the
angle. A slight angle error of about +/-150mdeg may be visible in
certain check measurements.
Start/Stop, Scan Status LEDs These buttons are the main Scanner Ctrl. Their effect depends on the
state of the system.
The LEDs display the respective state of the system
Scanner Ready LED: Grey: output inactive
Yellow: Not available without CL scan engine running. If CL ON: The
scanner does not hold a steady position on the sample grid. The
position is shown nevertheless by the sample grid moving in respect to
the green square and red dot. This mode has to be used when moving
the coarse positioners.
Green: The scanner is active. If CL ON: The regulation keeps the red
dot stable in respect to the sample grid.
Page 60

Scanner Running LED: Grey: The scanner is neither moving to the start point of the blue scan
area.
Green: The scanner is moving.
Depending on the state of the scan engine the three buttons have different effects. This is also indicated by
switching icons. All states are depicted below:
Stop Scanner: no effect
Pause Scanner: no effect
Start Scanner: switch to CL regulation active
Stop Scanner: switch to CL regulation inactive
Pause Scanner: no effect
Start Scanner: go to start of scan area
Stop Scanner: switch to CL regulation inactive
Pause Scanner: no effect
Start Scanner: start scan
Stop Scanner: stop scan and move back to start point
Pause Scanner: pause scan (press pause again to resume, press start
to start a new scan from this point)
Start Scanner: start a new scan from this point
If the Single Scan button is active, the scanner will be stopped and
repositioned to the origin after one complete scan. If Single Scan is not
active, the scanner will run until you press either Stop or Pause Scan.
Origin X/Origin Y [pm/nm/µm]: Offset of the center of the active scan
area.
Range X/Range Y [pm/nm/µm]: Size of the scan area.
Scan Lines/Scan Columns: The number of pixels in x (columns) and y
(lines) direction that will be collected. The scan range will be Pixel Size
times the number of pixels in each direction. If the Fix X=Y button is
active, only square scan areas are allowed and each change in Scan
Lines or Scan Columns will immediately affect the complementary
parameter.
Pixel Size [nm]: The pixel size in nanometers. The pixels are squares
by definition.
Sample Time [µs]: Time for the collection of one image data point.
Please note that the Sample Time is usually much higher than the time
needed to acquire one data point (2.5 µs). If the Average button in the
Data Display window is not activated, Daisy will acquire one data point
and saves it to the image, then skips all data points for the rest of one
Sample Time. If Average is activated, then all data points within one
Sample Time will be acquired and averaged to give one image data
Page 61
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

point.
For a smooth scanning movement, the scanner is not stopped during
the Sample Time, but moves steadily to the next pixel.
Instead of the Sample Time, the user can choose to set and maintain
the following derived parameters:
Line Frequency: = 1/(Sample Time * Scan Columns *2). The factor two
is given for forward and backward measurement.
Scan Speed: = Pixel Size / Sample Time
Time per Frame: = Sample Time * Scan Columns * Scan Lines * 2
Dependent on which parameter is chosen, Daisy will try to keep this
parameter constant if other parameters are changed. For example, if
Time per Frame is selected and Scan Columns and Lines are decreased
(Fix x=y enabled), the Sample Time is increased accordingly. If the Pixel
Size is increased, the Scan Speed will increase accordingly to meet the
same Time per Frame.
Rotation [deg]: Enter a value between 0 and 360 degree. The Active
Scan Area will be rotated around the Origin.
Fix X=Y: Toggle between fixing the scan range to be equal in both
directions and allowing different ranges for X and Y.
Hold slow axis: Activate this option to always scan the same line.
Single Scan: Activate this option to automatically stop the scan upon
completion of the frame. If not on, the system will start a new scan
starting from the finishing point of the last scan.
Dual Pass: Use this option for the Dual Pass mode, see also section see
6.5.7 Dual Pass…………………………… on page 92. In this mode, every line
is scanned twice (fwd-bkwd, fwd-bkwd, next line).
The Scan Display The Scan Display gives an overview over the Sample Grid, Scan Range
and Active Scan Area. The Active scan Area is marked by the blue
rectangle and can be arbitrarily chosen within the total scan range
which is displayed as a green rectangle. A red dot marks the current
position of the scanner. The blue cross marks the center of rotation.
If the CL scan engine is active, movement of the positioners will be
visualized by a movement of the Scan range over the sample grid.
To change the active scan area, one can either enter the desired
parameters manually or adjust the Active Scan Area using the mouse.
There are three different possibilities to change the active scan area
with the mouse:
Page 62

Move: Position the mouse on the blue cross in the middle of the
Active Scan Area. The mouse pointer will change to a cross. Drag with
the left mouse button to reposition the scan area.
Resize: Position the mouse on the border of the Active Scan Area. The
mouse pointer will change to a rectangle. Drag the border with the left
mouse button until the desired size is reached. This will change the
Pixel Size, whereas the Scan Lines/Columns remain unchanged.
Rotate: Position the mouse somewhere between the border and the
middle of the Active Scan Area. The mouse pointer will change to a
circle. Drag to rotate.
Active Scan Area Manipulation One can use the Size Tools to change the Active Scan Area.
Tools
Enlarge: Enlarges the Active Scan Area by 19%.
Shrink: Shrinks the Active Scan Area by 19%.
Maximize: Sets the Active Scan Area to fill the total available scan
range. Rotation is set to zero. If Fix X=Y is active and the maximum
scan ranges are not equal, both Range X and Range Y are set to max.
Range X.
Rotate: Rotates the Active Scan Area by 90 degrees. This feature is
helpful if you want to quickly exchange the fast and slow scanning axis.
Home: This sets the origin to the middle of the scan range.
Point Cursor: Changes the curser to the point curser. Moving this into
the scan area causes a popup with the coordinate position of the
cursor.
Decoration It is possible to drag and drop an image from the Frame View display
to the Scan Area. It will be depicted at the coordinates it was
recorded. This can be especially helpful in closed loop scan mode to
find a certain area of the sample again after moving around.
Right clicking on the scan area will open up a menu that allows to use
the active scan area manipulation tools. You can also move the origin
of the background coordinate system to the current position of the
cursor.
To remove all decorations from the scan area click the Clear
Decoration button.
Active Scan Area Zoom Tools Use these icons to zoom in and out of the Scan Display. These tools do
not change the Active Scan Area.
Page 63
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

The mouse wheel can also be used to zoom in the scan display.
Zoom in
Zoom out
Zoom all: Shows the total available scan area.
Zoom Adjust: Shows the Active Scan Area.
Scan Details Click on Scan Details to display important additional scan parameters
which follow directly from the defined scan parameters.
Range X/Y: Size of the Active Scan Area.
Line Frequency: Line Frequency in Hertz. Please note
that Line Frequency is based on the time for forward
and backward scan of one line.
Frame Time: Time needed for the completion of one
up scan or one down scan.
Speed: Scan speed in micrometers per second.
Voltage Limit X/Y: The current voltage output limit as
defined in the Preferences Tab.
6.2.1 Scan, line and pixel trigger
To synchronize an external detector to the scanner motion one
option is to use the pixel-, line- and frame trigger accessible via the
sub-D 9 pin connector on the front panel (see 2.3.4).
Trigger pulse shape: LVTTL pulses (high active, 3.3 V) with 1µs pulse
length. The feature is automatically used when scanning and has no
corresponding settings in the ASC500 daisy software.
Pin 1, pixel trigger: During the continuous fast axis scan the data is
binned according to the sample time. At the start of each of these
bins the pixel trigger is sent.
Pin 2, line trigger: At the beginning of a slow axis movement
(typically y) a line trigger pulse is sent. Switching from forward to
backward direction is implemented as a step in y direction with 0
distance and micro second duration, also sending a line trigger.
Pin 3, frame trigger: A frame trigger pulse is sent at the beginning of
a new frame, synchronized with the first line trigger.
Page 64

Y (slow axis)
p p p
Line 3
p p p l
l
p p p
Line 2
p p p l
l p p p
Line 1
p p p l
f, l
X (fast axis)
Figure 11: Visualisation of a 3x3 scan and the respective frame (f), line (l) and pixel (p) triggers. After the
pixel trigger is generated, the data is recorded during movement along the fast axis for the given sample
time. The ‘zero length movements’ are highlighted red, and the binning is visualized with green arrows.
6.2.2 Step Scanner Control (discontinued)
Step Scanning is discontinued in Daisy v2.7. This tab is
a leftover and can only be accessed in simulation
mode.
6.2.3 Lithography
The Daisy Lithography module can be used for defining geometrical
shapes that will be retraced by the sensor head. It allows the
definition of arbitrary convex polygons and single points. Moreover,
a shutter can be controlled via TTL pulses to allow for exposition
control.
It has to be activated in the ASC500 hardware before the tab shows
up in the software.
Lithography can be operated in both closed loop and open loop
mode.
Shape definition The shape definition of the lithography pattern is done via a text file.
There are two basic shapes to define the lithography pattern:
Page 65
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Polygons and Points. Each of these basic shape definitions can be
combined with a command to control an optional shutter. An
example for a shape file is shown in Figure 12.
Figure 12: Example of a shape definition file.
The shape file must be an ASCII file with an nls extension. It must start
with a <ShapeFile Version”2”> command and end with a </ShapeFile>
command. In between, there can be any number of Polygon and Point
commands. Comments can be inserted enclosed in a <!-- and -->
respectively. All coordinates given in a shape definition file are
interpreted in nm and are relative to the center of the current scan
range.
The two basic definitions can be done via:
1. Polygon command:
<Polygon Attributes>
<Vertex X Y/>
<Vertex X Y/>
<Vertex X Y/>
</Polygon>
Page 66

The Attributes can be:
a. Spacing : the spacing of the filling pattern in nm (default:
1). The polygon will be written by meandering lines with
a line spacing given the Spacing attribute.
b. Speed: the scan speed during the writing of the polygon
in nm/s (default: 10000).
c. PosSpeed: the scan speed during the approach of the
polygon in nm/s (default: 10000).
d. Beam: controls a shutter via a TTL output. Beam on (1)
leads to high voltage on the TTL output, Beam off (2)
leads to GND voltage on the output connector. The
output connector for this functionality is pin number 5
of the External OUT connector (see section 2.3.4 on
page 14).
e. Handshake: Stop for handshake with external device
before scanning (Default: 0).
All attributes can be omitted. The default values will be used for
omitted attributes.
The polygon itself is defined via a sequence of vertices. Each
vertex has to be specified with a <Vertex/> command. It is
important to note that only convex polygon will result in a well-
defined output.
2. Point command
<Point X Y/>
a. X and Y: mandatory attributes in nm.
b. PosSpeed: the scan speed during the approach of the
point in nm/s (default 10000).
c. Wait: Wait time in ms after reaching the point
(default: 0).
d. Beam: Beam on (1) or off (0) during wait time
(default: 1).
To check the shape, the text file can be loaded into the Daisy software
where the shape will be displayed in the Lithography section of the
Scan Control widget. How this is done will be explained in the next
section.
Operation of lithography The lithography control is placed in the Litho tab of the Scan Control
widget. The tab is shown in Figure 13. The lithography tab is similar
to the scanner control tab. Some settings can be changed in both tabs
and the changes in one tab will immediately affect the other.
Page 67
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Figure 13: Lithography widget with shape definition. The shape that is
shown was produced by the shape definition file of Figure 12.
1 – load lithography definition file: upon a click on this button, a
Windows dialogue will appear to specify the lithography shape
definition file. After loading, the lithography shape will be shown in
the display.
2 – clear shape: with this button, any shape that is displayed will be
erased.
3 – the loaded shape is drawn into the actual scan range. It is worth
noting that the meandering lines of the lithography are only resolved
in the lower triangle of the shape. Here, a line spacing of 200 nm was
used. The single lines of the rectangle (spaced 75 nm apart) can only
be displayed using the zoom buttons in the lower left of the panel.
4 – here, the basic definition of the actual scan range can be set.
Changes will immediately affect the Scanner Ctrl Tab.
5 – Status LED: green is lithography is running.
6 – Start button: starts the lithography .
7 – Pause button: pauses the lithography. During pause, the shutter
will be closed and reopen upon ending of the pause in case its status
was open before the pause.
8 – Stop button: Stops the lithography. The shutter is closed and the
scanner moves to the origin.
Page 68

6.3 The Z Control
The Z control feedback loop controls the z-position of a sample with
respect to a probe. There are several Input Signals to choose from,
whereas the output of the loop is strictly connected to Z OUT. The
loop output is limited to a voltage ranging from 0 to Z Range. The
output can be additionally limited using the Z Limit min and Z limit
max settings.
The feedback loop always tries to modify z-out so that the input
signal, actual value, gets closer to the setpoint. Whether the loop
needs to be in negative or positive feedback, can be chosen with Inv.
Polarity. The proportional gain P is sensitive to sudden jumps in the
signal, whereas the integral gain I is sensitive to the integral of the
signal.
The main loop-controls are: The Loop On checkbox, the Retract
Button at the top as well as the indicator LEDs at the bottom. The
following states are possible:
Loop on: Enable the check box to switch on the loop. The LED
will turn green.
Loop off: If the box is unchecked, the feedback loop will hold the
position of z-out and will not react on changes of the input signal.
Retract: If Retract has been pressed, the loop is switched off and the
voltage is taken down to 0 (i.e. the tip is retracted from the sample).
Clipping: The Clipping LED is enabled, if the active loop reaches one
of the limits, i.e. either the lower limit, or the upper limit.
Adjusting: This LED indicates that the red bar is not yet synchronized
with the real z-out value (due to lower update rate).
Slope Compensation: This LED indicates that the Slope Compensation
is enabled.
Inv. Polarity: For experiments, in which the sensor signal increases
with decreasing sensor sample distance (e.g. in STM, the tip gets
closer with higher z-out voltage), leave this box unchecked. For
experiments, where the sensor signal decreases with decreasing
sensor sample distance (e.g. oscillation amplitude of a vibrating tip),
do check the box.
Page 69
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

6.3.1 Details……………………………
The details dialog allows to set some of the details of the Z Control
behavior. Different filters can be used on the Input signal before it is
fed into the PI loop. The easiest method to apply a low pass filter is to
increase Z Feedback Ts which controls the underlying time base of the
discrete PI controller. Increasing this value decreases the sensitivity
to high frequency noise on the input signal.
A more sophisticated way is to use a FIR (finite impulse response
filter) or IIR (infinite impulse response filter) to achieve a similar
effect.
6.3.2 Slope Compensation
The Slope Compensation is an important feature to compensate for a
tilt of the sample with respect to the horizontal plane. Quite often in
SPM experiments, the height of the investigated feature is much
smaller than its lateral dimension so the scan range will be large in x
and y and small in z. In this configuration even a small tilt of the
sample does disturb the image and masks smallest topographic
variations. To compensate for these sample tilts, the ASC500 features
a powerful Slope Compensation that enables scanning of a tilted plane
without any influence on the z controller. Once the Slope
Compensation is set and activated, the sample will be scanned as if it
was lying perfectly in the x-y plane.
This feature is also very handy when it comes to scans in “constant
height mode”, leaving the sensor sample distance constant even
without employing a z feedback.
The Slope Compensation settings can be reached through the Slope
Comp. button in the z controller widget. A window as shown to the
left will appear. The compensation values for both X and Y axis can be
entered separately in the Z/X and Z/Y box, respectively. The Slope
Compensation can be activated and deactivated using the Enable
checkbox.
A negative slope (of the forward scan) will be compensated by a
positive value and vice versa.
The slope compensation is realized by mixing of up to 20% of the x or
y scanner voltage respectively to the z scanner voltage. Z/X is the
percentage of the X extension that is mixed to the Z extension. The
maximum value is limited by the hardware to Z/X = 20% · V /V
max, x max,
· Z /X .
z max max
To set the correct values the compensates the sample tilt, it is best to
do the following:
1. Set the scan rotation to 0 degrees.
Page 70

2. Scan a line and change the Z/X factor of the Slope
Compensation until a flat line appears horizontal.
3. Set the scan rotation to 90 degrees and repeat the previous
step for the Z/Y factor.
Figure 14 shows typical line scans with and without Slope
Compensation for an AFM scan of the 25 nm high grating with a 4 µm
pitch. As can be seen in the image, the Slope Compensation acts on
the total scan range of the scanner; the two line scans displayed here
would meet at an x position of 0 µm, the offset between the white
and the red scan line is thus the result of the Slope Compensation
together with a scan field that does not include the x origin position.
Figure 14: A typical line scan before (red) and after (white) the sample
tilt is compensated by the Slope Compensation feature.
Since the slope compensation will change the Z OUT voltage abruptly
(with the Z slew rate set in the Output limit dialog), it is not
recommended to turn it on while the loop is ON. The sudden change
in the sample lift can easily damage an AFM tip.
Slope Compensation Details The Slope Compensation is realized internally by the analog
addition/subtraction of some part of the X OUT and Y OUT voltages
to the Z OUT voltage. A positive Slope Compensation of 20 % for both
X and Y axes will thus lead to a large additional voltage (called Slope
Compensation Voltage SCV) in the Z OUT voltage output if the scanner
moves to the upper right corner of the total scan range. If for example
the maximum allowed voltage for the x and y scanner is 4 V, the SCV
can vary between -1.6 V and 1.6 V (These voltages will typically be
amplified by a factor of 15 before applied to the scanner). If the SCV
would simply be added or subtracted to the Z OUT voltage, the
resulting voltage could possibly be either large enough to damage the
scanner piezo or negative enough to lead to some depolarization of
the scan piezo.
To prevent this from happening, a safety margin for the Z OUT voltage
is employed in the following way: for the actual settings of Z/X and
Page 71
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Z/Y, the maximum positive and negative SCV will be calculated
(‘maximum’ meaning the value of the SCV for a scanner position in
the upper right corner of the total scan range). If the Slope
Compensation is activated, the Z OUT voltage range will automatically
be reduced by the exact values of the SCV. This way, the sum of the Z
OUT voltage (as set by the z controller) and the SCV will never exceed
the maximum allowed voltage and no harm will be done to the
scanner.
The reduction of the z scan range is visualized in the z controller’s
display. The safety margin due to the slope compensation will be
shown purple in this display. Below, are several examples.
1 2 3 4
(1) The display shows a z scan range of 10 µm that is not
restricted because the Slope Compensation factors are
both set to zero. The full range of the scanner is
accessible for scanning.
(2) The display shows a z scan range with a restriction due
to the Slope Compensation by Z/X = 2.5% and Z/Y = -
2.5%. In this case1, 2.5 % of X OUT means 1 µm safety
margin in Z OUT. The positive factor for Z/X leads to a
reduction of 1 µm at the upper limit of the z scan range.
The negative Z/Y factor of -2.5% leads to a reduction of
the z scan range of 1 µm at the lower limit of the z scan
range. It is important to note that this reduction
automatically leads to an elevation of the z scanner’s
retract position.
1 X, Y scan range 40µm, Z scan range 10µm: 2.5% · 10µm = 1µm
Page 72

At the moment the Slope Compensation is activated, the scanner will
move the tip closer to the sample! However, this will not harm the tip
if the Slope Compensation is set correctly. Basically, the tip will be
driven closer to the sample only in those lateral positions, where the
sample is ‘far away’ from the tip due to its tilt.
Overload Capacity (3) As in (2), the display again shows a z scan range with a
restriction due to the Slope Compensation by Z/X = 2.5%
and Z/Y = - 2.5%. The fact that the restrictions are
smaller is due to another margin that has not been
discussed so far. The hardware parameter, Slope
Compensation Overload Capacity, will increase the
accessible z scan range. This parameter is related to the
fact that piezos in general have some tolerance in their
voltage ratings. A piezo rated for 0 V to 60 V can safely
be driven by a voltage of – 3 V to 63 V. This Overload
Capacity can be used to regain some or all of the z scan
range that is ‘lost’ to the Slope Compensation. In the
example shown above in (3), an Overload Capacity of 5%
has been employed to reduce the restrictions to 0.5µm
on each end of the z scan range. The Overload Capacity
can be set in the Output Limits – Expert Settings –
Overload Capacity section.
It is strongly recommended not to change the Overload
Capacity and leave the value that is set in this field by
the manufacturer. False settings of the Overload
Capacity may damage the piezo and will lead to a loss
of warranty.
(4) The display shows a 10 µm z scan range with the
following settings: Z/X = -3.75%, Z/Y = 1.75 %, Overload
Capacity = 5 %. The negative Slope Compensation factor
of 3.75 % together with the Overload Capacity leads to
restriction of 1 µm at the upper limit of the z scan range.
At the lower side, the positive Slope Compensation
factor of -1.75% will be diminished by the 5% Overload
Capacity, leaving a restriction of 200 nm at the lower
end of the z scan range. The retract position is elevated
to this value.
Notes a. The SCV will not be part of the internal signals Z OUT and Z
OUT INV. However, it will of course be a part of the Z OUT
voltage.
b. The Slope Compensation can be set at any time during a scan.
A change in the Slope Compensation will immediately lead to
a change in the Z OUT voltage. The speed of this change is
governed by the Z Slewrate that can be set under Output
Limits – Sanner Limits and Scaling – Slewrate Z. If the Z
Slewrate is faster than the speed of the z control loop, a
change in the Slope Compensation can potentially lead to a
tip degrading.
Page 73
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

c. The limits of +/- 20% voltage of the Slope Compensation are
set by hardware limits that where built into the ASC500.
These limits were designed to avoid an exceeding crosstalk
of noise from the X OUT and Y OUT voltage on the Z OUT
voltage.
6.3.3 Setpoint Modulation
This feature is useful to optimize the P-I parameters with a tip in
contact.
You can choose between Setpoint Mod. Off, Periodic Rectangle and
LF Lock In.
If you enable Periodic Rectangle, the setpoint of the feedback loop
will be switched with the given period between the value entered in
the feedback loop control and the value given in this dialog. Hence,
the setpoint modulation simulates an ultimately sharp feature. This
facilitates the tuning of the feedback loop accordingly.
The Periodic Rectangle function alters the setpoint between the
actual setpoint of the loop and Value with a switching time of Period.
If selecting LF LockIn one can use the signal of the LF LockIn to
modulate the setpoint to achieve a similar effect to above except of
it not being rectangular.
Caution: The Setpoint Modulation has an immediate effect on
setpoint of the feedback loop. It is recommended to enter meaningful
values before enabling this feature. Also, sensitive tips may be
damaged if the values for the feedback loop and the two setpoints
are not correctly chosen.
The physical unit of the P and I parameters of the feedback loop are
dependent on the input signal of the loop. The units are:
Input Signal P unit I unit
ADC 1..6 µm/V µm/V/s
HF 1 df µm/Hz µm/Hz/s
HF 1 Ampl µm/V µm/V/s
HF 1 Phase µm/deg µm/deg/s
LF Lockin Ampl µm/V µm/V/s
LF Lockin Phase µm/deg µm/deg/s
Page 74

6.4 The Scan Data Displays
In the main screen there are two display windows (left and
DCC
right display) showing the scanning results. In these windows
either images (Frame View) or line scans (Line View) can be
displayed. Furthermore, data can be saved and the scan area
can be modified.
The drop down menu at the top left of each window allows
for selecting the respective signal to be displayed. By
activating the Average button in the DCC all incoming data
within one sample time (as specified in the Scanner Ctrl) is
averaged before it is displayed on the screen. If Average is
deactivated, Daisy displays the first incoming data point at a
new scan position and then discards all further data within
this sample time.
In the Frame View the acquired data is shown in a xy-plot,
with the intensity color-coded as specified (see section 5.4.3
for a description of the context menu). In Line View the data
is shown as curves.
If the cursor is paused for a second over one of the displays
a pop-up window will display the physical coordinates of the
chosen point.
Also, you can double-click on the window to detach it from
the main window at any time, allowing for any user-defined
resizing or repositioning of the window on the screen.
6.4.1 Frame View
The drop down menu at the top of each window allows for selecting
the respective signal to be displayed. The available signals can be
defined in the DCC (see 4.1.1). To the right, the snapshot icons allows
for saving of the SCAN data as described in section 4.2.7. Below that
is the pull-down menu to select an Underground filter: this filter can
be used to subtract a function of 0th (Constant) or 1st order (Linear)
from each line to remove scan artefacts.
Range Tools: Below each frame display area the Range Tools are
shown. By pressing the Auto button, the range limits will be calculated
from the currently displayed values, i.e. the currently chosen color
scale will be spread to match the data which is displayed at the
moment of pressing the button. To further enhance the contrast or
highlight certain parts of the image, one can choose the range limits
manually by entering values to the left (Range Minimum) and to the
right (Range Maximum). It is also very convenient to use the mouse
wheel to change the Range settings. For this, just move the mouse
pointer on the respective input field and then use the mouse wheel
to continually change the setting. Use STRG or SHIFT key together
with the mouse wheel to change the sensitivity of the wheel (see also
section 5.4.1).
Page 75
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Scan Direction Switch: This button allows you to switch between
displaying either the Forward (data acquired in a left-to-right scan) or
Backward (right-to-left) data.
Please note that the following Selection tools are only shown when activated by right-clicking on the frame
view, see section 5.4.3.
Frame Zoom Tools: The Frame Zoom Tools allow for zooming in or
out. Please note that only integer zoom factors (or 1/integer factors)
are allowed to avoid aliasing effects. If the image size in any zoom
setting is larger than the available size in the Frame View window,
scroll bars appear.
Frame Tools: The Frame Tools are shown to the lower right of the
Frame View. The Frame Tools can be used to alter the current scan
area. The Frame Tools are advantageous when one wants to
reposition the scan area based on information that is currently shown
in the Frame View. It is possible to (from left to right):
- select a rectangle as new scan range,
- rotate the scan direction or measure distance of
two points,
- move the scan area by selecting a new center,
- select a new center of the scan area, or
- select a path for the Pathmode or
- create a grid for the Pathmode.
The rightmost button is used to accept the selections made. Please
note that you cannot use that Frame Tools until a scan image has been
taken.
6.4.2 Scan Data Display: Line View Tab
In the Line View Tab, single or multiple lines of the scan image can be displayed during scanning. The Line
View is constantly updated during scanning and shows the current values of the chosen Signal versus slow
axis position. Please note that a comment window appears if you stop the cursor over the line view graph,
displaying the actual position.
Page 76

You can use the Scan Direction Filter to either display the
Forward or the Backward scan. If the Scan Direction Filter is
turned off, then both forward and backward scans will be
displayed. You can increase the number of simultaneously
displayed lines using the Curves function in the Line View
Ranges context menu. Multiple lines are displayed in different
colors for better clarity.
Use the Zoom Tools to adjust the display range. You can also
use the Stop and Clear buttons and the right-click menu
as described in section 5.4.2.
Frame Tools: These buttons allow to set a new scan range
directly from the Line View graph of the Display. Choose the
Select New X Range button and then drag the two vertical lines
to enclose the desired new x-range (as shown in the graph).
Click on the Accept button and note how the active scan area
changes in the Scanner Ctrl. If the Fix X=Y button is activated,
the y scan range will be changed, too.
Page 77
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

6.4.3 Example for Shifting, Moving and Zooming the Scan Area
As an example, an image in the simulation mode of the
software was acquired. As can be seen below, the full scan
range of the xy scanner was 40 x 40 µm, and a 3x 3µm image
(blue square) was taken in the middle of the full range. Also,
the frame axes of the image are parallel to the x- and y-
direction of the scanner.
Page 78

To rotate the scan direction so that the artificial dot array
has a certain orientation to the frame axes, one has to
activate the button, then draw a line in the Frame View
window, as can be seen in the picture aside. Click on the
button to accept the choice. The next scan will be
carried out with the x-axis along the line.
All parameters in the Scanner Ctrl are automatically
adjusted and the blue square is rotated to show the new
scan area (see below).
Page 79
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

To choose a new center of scan, use the button. Click on
the new center in the Frame View and accept the selection
with .
The Scanner Ctrl will automatically adjust the scan area to be
centered on the new spot as close as possible within the
allowed maximum scan range of the scanner.
Finally, to zoom in on details of the image, use the button
and drag a rectangle around the area of interest. Please note
that the chosen rectangle is transformed to a square if the Fix
X=Y button in the Scanner Ctrl is activated.
Again, after accepting with the button, a new scan area will
be defined. The screen shot below shows the result of these
actions.
Page 80

It is possible to drag and drop the scan from the frame view window to the Scan Area of the Scanner Ctrl
window. It will then be shown as a decoration in the scan area (c.f. 6.2).
6.5 The main functions tab section
All main functions such as the PLL, Coarse Motion Control, Pathmode, Lock-In(s) & Q Control, Dual Pass and
DAC Outputs are located in the tab section on the lower left part of the GUI. The user can conveniently adjust
the order of the tabs as well as choose which tabs to show and which to hide, as described in section 5.3.1.
6.5.1 Phase Locked Loop (PLL tab)
A completely digital Phase Locked Loop (PLL) is integrated in
the ASC500. The PLL Tab contains the functionality needed
to control any type of oscillating appliance. It comprises two
PI loops for automated excitation frequency and amplitude
control. Note that the amplitude and frequency value can
also be addressed in the Lever Excitation tab (section 6.5.3).
Page 81
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

The configuration of the PLL loops is similar to the z controller (see
section 6.3). They can act in a certain range between Min and Max. P
and I parameters need to be chosen accordingly. The Inv. Polarity
checkbox inverts the logic of the loop. The green LED indicates an
active loop.
The two loops are internally bound to certain input and output signals,
which cannot be changed (see section 4.2.2). For the Amplitude loop,
the input signal is HF 1 Ampl. and the output signal is the excitation
amplitude Aexc. For the phase control loop, the input signal may be
chosen via a drop-down list: it could be either one of the ADCs or one
of the HF and LF Lockin signals. This leaves the user the choice to use
an external lock-in (connected to one of the ADCs) to drive the PLL.
In both loops one can use the Setpoint Modulation in order to find
reasonable P and I parameters.
For a working example on how to set up a measurement with the PLL
please see section 6.7.1.
6.5.2 LF Lockin……………………………
The low frequency Lock-In produces a reference signal with a certain
Amplitude and Frequency which is passed to the respective Output
Connector (DAC1 or/and DAC2).
The input signal (Input Connector) is then analyzed using the
demodulation values (Sensitivity Range, Phase Shift, and Integration
Time). The output channels of the LF Lockin are LF Lockin Ampl and LF
Lockin Phase. These can be selected as source for most displays.
Other than that, the LF Lockin settings work in complete analogy to
the ones for the HF Lockin (located in Lever excitation tab, see section
Page 82

6.5.3 Lever Excitation on page 83). HF 1 Sync Enable can be used to
lock the LF Lockin to the HF Lockin.
6.5.3 Lever Excitation
Some of the most common scanning probe techniques like
AFM or MFM use a mechanical oscillator given by a
cantilever or tuning fork to detect changes in the
interaction strength between the probe (e.g. AFM tip) and
the sample surface. In this AC mode (tapping mode) the
cantilever is excited (usually) at its resonance frequency,
and the resulting oscillation signal is recorded with a HF
Lock-In amplifier. In the ASC500, this functionality is
covered by the HF section, which is controlled via the Lever
Excitation tab:
Page 83
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

The input signal for this HF Lock-In is HF IN 1, the output is
both HF 1 Ampl and HF 1 Phase. Refer to section 4.2.2 for the
connection schematics.
The lock-in is configured with the following values:
Excitation The excitation signal is applied to HF 1 Out.
Amplitude: Amplitude of the output reference (peak to
peak). To change the range of this output use the Minimum
and Maximum values in the PLL Amplitude Control tab. This
can become necessary to increase the resolution when
outputting small amplitudes.
Frequency: Frequency of the reference output.
Note that these two values can also be addressed in the PLL
tab (see section 6.5.1). The resolution is also affected by the
Min and Max values in that tab.
Detection Sensitivity Range: Sensitivity of the Lock-In. If the signal
exceeds the Sensitivity Range, overflow may occur and
wrong values may be displayed. The maximum sensitivity is
5 V. Decreasing the Sensitivity increases the lock-in
resolution. To achieve maximum effect of the Q control
decrease the sensitivity range if possible.
Phase Shift: Can correct for constant phase shifts of the
Signal with respect to the reference. Note that this governs
only the output of HF 1 Phase. HF 1 Ampl measures the full
amplitude of the signal.
Auto Phase: Measures the phase difference at the selected
excitation frequency and sets it as the Phase Shift. If the
phase shift jumps to +-180° reset it to 0° and Auto Phase
again.
 Integration Time: Integration Time of the Lock-In. With
longer integration time the HF1 Ampl and Phase reacts
slower, though with having less noise.
Q Control The Q control can be used to reduce or increase the Q factor
of a resonator which corresponds to its sensitivity and
reaction speed. How to set up the Q control is discussed in a
working example in section 6.7.2.
Phase: This sets the phase parameter for the Q Control
functionality.
Feedback: This determines the feedback parameter of the
loop.
HF 2 Sync Out Use this checkbox to sync HF1 Out and HF2 Out.
6.5.4 Coarse……………………………
If the ASC500 Controller is used in combination with
attocube’s ANC300 positioner controller, the Daisy software
can be used to operate coarse positioner movement. To use
the coarse movement features, please make sure that the
Page 84

ASC500 is connected to the controller using the respective
cabling (see section 2.3.5).
Each Axis section can operate one axis of the coarse
positioners. Basic parameters of the coarse movement are
set in the Frequency and Amplitude fields. For further details
on these parameters, please see the respective manuals of
coarse positioners and coarse positioning controllers. The
Enable button will enable the coarse steps using the arrow
buttons in the lower part of the axis sections.
Be aware that the communication is unidirectional. Changes
in the ANC300 will not be taken over in the Daisy software.
The software will display one section for each active ANM
module in the ANC300, but it can only control the settings of
the ANM100 and ANM300 stepping modules.
The Step buttons initiate a single step movement.
The Cont buttons can be used for continuous movement. The
movement will start when the mouse button is pressed and
will stop when the button is released. If the text edit field
Max. Crs. Steps is set to a value > 0, the Cont. coarse
movement can be used to execute a well-defined number of
coarse steps. If, for example, the Max. Crs. Steps is set to 100
and the Cont. button is pressed for a sufficiently long time,
the movement will stop after exactly 100 steps. For safety
reasons, the movement will stop sooner if the button is
released before the total of 100 steps is completed. In case
the Max. Crs. Steps is set to zero, the movement will only be
stopped by the release of the mouse button.
Note. The Frequency and Amplitude values are programmed
to the coarse controller only if the value is changed and
confirmed. These edit boxes are in no way an indicator for
the values that are currently set in the coarse control device.
Page 85
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

6.5.5 Autoapproach
The Autoapproach is used to bring the tip into close
proximity of the sample surface. The procedure that is
employed for this task works as follows: the z scanner is
continuously expanded while the sensor signal is being
traced. When the stop condition is met, i.e. when the tip is
close to the sample, the system will immediately finish the
Autoapproach and enter the Target Mode. The Target Mode
can be defined to be either an activated z feedback loop or it
could also be a tip retract. If the stop condition is not met till
the maximum stroke of the z scanner, the z scanner will be
retracted and a number of coarse steps will be issued. After
this the procedure will be restarted.
There are two different ramp modes for the Autoapproach:
In the Ramp mode the z scanner expansion is done in a
constant speed. This speed must be chosen small enough so
that the tip is not damaged before the stop condition is met.
The alternative is to use the Loop mode, where the speed of
the z scanner expansion is defined through the z controller’s
I and setpoint parameters (the P parameter does not
contribute due to the definition of a proportional feedback
gain). As in normal feedback operation, the expansion speed
will be depending on the difference between the actual
sensor signal and the setpoint. This means that the Loop
mode will react on slow changes in the sensor signal (for
example due to long range forces) with an adaption of the
approach speed.
It is important to note that the parameters used to define
the Autoapproach behavior are partly set in the z controller
section of the Daisy GUI (section 6.3). Most importantly, the
sensor signal that is being traced for the stop condition is
defined through the Input Signal of the z feedback loop. In
case the Loop mode is used, of course all parameters of the
z feedback loop are taken as entered in the respective fields
of the z controller.
In Loop mode, the approach can come to a halt if the sensor
signal equals the setpoint before the threshold condition is
met. The system will be in a stable condition, but the
Autoapproach will still be active in the background. If this
behavior is to be avoided, the setpoint of the z controller and
the threshold value of the Autoapproach should be set to
equal values.
The Autoapproach can be manually stopped either by
clicking the Start button of the Autoapproach section while
the Autoapproach is running or by clicking on the Retract
button of the z controller. In the first case, the z scanner will
keep its current position; in the latter case, the z scanner will
be driven to zero (i.e. maximum distance between tip and
sample).
Page 86

Delay: Delay after coarse stepping. Stepping may induce
some noise or ringing in the experiment. The settling time
between the coarse step and the start of the z scanner
expansion can be defined here. During this time, the sensor
signal will not be traced for the threshold condition.
Z Input signal: This display shows the input signal used for
the Autoapproach procedure. The Z Input signal can be
changed in the Z Control section (see section 6.3).
Threshold: Value for the stop condition.
Stop Cond.: Defines if the threshold represents a lower or
upper boundary of the sensor signal range. In STM type
experiments, the Stop Condition will always be a “>” while in
non-contact AFM type experiments, the condition will be set
to “<”.
Speed: Approach speed for Ramp Mode.
Steps/Apr.: Defines the number of coarse steps that will be
executed after each scanner ramp. Usually, this value will be
defined depending on the stroke of the z scanner in relation
to the step width of the coarse device.
Apr. Mode: Approach mode; defines whether Loop or Ramp
mode is used. Details are given in the text above.
Target Mode: Defines the mode that is activated after the
stop condition was reached. It is possible to switch on the
feedback loop (Loop On), or to retract the tip (Retract).
Status LED: The status LED indicates whether the
Autoapproach is active or not.
Page 87
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Start: Press Start to start the Autoapproach.
Coarse Adjust: Additional to the axis’ coarse control, one can
issue single steps with the Autoapproach coarse axis. The
coarse adjust button is meant to set the contact range of the
tip within the z scanner stroke. Normally, after finishing the
Autoapproach the tip is in the upper part of the z scanner
range. Using the Coarse Adjust buttons, one can move the
contact point of the tip to a more convenient position in the
middle of the z scanner range (with better scanner linearity).
For that the Coarse Adjust button will deactivate the
feedback loop, trigger one coarse step and then restart the
feedback. This functionality can be used with the feedback
turned ON without any risk of damaging the tip.
Note: if the feedback was not active upon the triggering of
the Coarse Adjust, it will not be activated after the execution
of the coarse step.
No coarse: If this option is chosen, the coarse movement of
the Autoapproach will be deactivated.
The Autoapproach Details section includes all approach
parameters that will have to be set only once to configure a
certain hardware configuration.
Single Z-Piezo: Enable, if the z positioner piezo and the z scan
piezo are the same physical device. In this case, the ANC300
will be switched to EXT mode during the approach.
GND while apr.: When enabled, the coarse control device
will be switched to GND mode during z scanner expansion.
For lowest noise, this option should always be activated.
Coarse Axis: Defines the axis number of the z coarse
positioner. The attocube standard is to use Axis 7 as the z-
axis.
Coarse Dir.: Defines the coarse approach direction. Standard
is forward.
Coarse Device: Defines the coarse control device. The
possibilities to choose from are
1. ANC300/ANC350 for operation with an attocube
ANC300 or attocube ANC350. The connection to the
ANC300/ANC350 has to be done with a serial cable.
2. TTL via DAC2: Can be used to control any coarse
controller that can be triggered by a TTL pulse (5V
pulse amplitude). The connection has to be made
via the standard DAC2 output.
3. LVTTL via DAC2: Can be used to control any coarse
controller that can be triggered by a low voltage TTL
Page 88

pulse (2.2V pulse amplitude). The connection has to
be made via the standard DAC2 output.
4. ANC350 via NSL A/B: For operation with an
attocube ANC350. The connection is done via a
special NSL cable. For further information on this
connection, please contact attocube. When using
two ANC350 modules you can switch between the
two NSL channels.
6.5.6 Path………………………………….
The Pathmode is used for experiments that are defined on a
grid of points or on a number of randomly selected points of
the scan field. On each point, a number of actions can be
defined and grouped into action lists. Predefined actions
include any of the internal spectroscopies as well as
handshake actions (either manually or with external
instruments). The flexibility and diversity of this function
makes it a very powerful tool for the experimentalist.
The Pathmode is enabled using the Frame Tools of either
frame view (see section 6.4). To select a path, first click on
the button, then select points of interest in the data display.
These positions will be shown as small circles in the display,
with a line connecting the different points indicating the
path. After selecting the path, a click on the accept button
will initialize the Pathmode. Paths and grids can be saved,
edited and reloaded using the respective buttons in the Path
Control section of the Path tab.
Manual Handshake Manual Handshake: If this option is enabled, the user has to
confirm each step with the Proceed button (in the Manual
Handshake section). The scanner position on each point can
be manually altered using the Manual Positioning option in
the Scan tab described in section 6.5.10.
Page 89
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

External Handshake The External Handshake is used to integrate external devices
into the control capabilities of the ASC500. The interaction
between the ASC500 and the external device is done by
means of TTL pulses. For the definition of the SNYC
connector pins, see 2.3 Front and Rear Panel Connections on
page 12. The idea of the procedure is the following:
1. The ASC500 drives the tip to a certain spot of
interest (defined by the path mode).
2. A SNYC OUT TTL pulse is issued once the tip has
reached the target position to trigger the external
device.
3. The external device (for example a spectrometer)
executes a certain measurement task.
4. After the measurement is finished, the external
device issues another TTL pulse which triggers the
ASC500.
5. Upon receiving a SNYC IN TTL pulse, the ASC500
drives the tip to the next point (or repeat the
measurement circle).
To use this capability, the following conditions have to be
fulfilled:
a) The SYNC OUT line of the ASC500 must be
connected to the external device
b) The SYNC IN line of the ASC500 has to be connected
to the external device
c) The external device must be capable of being
triggered by a TTL pulse.
d) The external device must be capable of sending a
TTL pulse after the fulfillment of its measurement
task. If this is not possible, the ASC500 can also wait
a predefined amount of time at each spot before
moving to the next spot. The waiting time at each
point must be adjusted to make sure the external
device has finished its measurement task.
NOTE on TTL pulses:
The ASC500 TTL input and output lines are using low-voltage
TTL (LVTTL) pulses, i.e. pulses with a high level of 3.3 V.
However, the use of 5 V TTL pulses (also commonly used) will
not damage the input stage of the ASC500. Also, since the
threshold voltage for all TTL high levels is defined as 2.5 V,
communication with a 5 V-TTL device is guaranteed without
problems.
To setup the handshake procedure with the external device,
the External Handshake section of the Path tab is used. The
parameters will be explained in the following:
Page 90

Count: Number of handshake cycles to be executed per
point.
Pulse Time: Defines the length of the SYNC OUT pulse.
Handshake: If activated, the controller waits for a return
SYNC IN pulse (or until timeout). If deactivated, the tip will
smoothly move from point to point sending a SYNC OUT
whenever a new point is reached.
Timeout: Defines the maximum period of time the controller
is waiting for a SYNC IN pulse. After Timeout time has
elapsed, the controller will either proceed with the next
SYNC OUT pulse (if Count > 1) or the tip will move to the next
point. The Timeout can be deactivated by setting it to 0. In
this case, the tip will not move to the next pixel until a SYNC
input is sensed. Timeout can be used to control external
devices that do not have the capability to return a SYNC IN
TTL pulse.
Edge: Defines if the SYNC input TTL pulse will be triggered on
either Falling or Raising edge.
Test Handshake: Runs one cycle of the Handshake
procedure. A first click on this button will issue a SYNC OUT
TTL pulse. A second click will simulate the SNYC input pulse,
i.e. the tip will move to the next point (or repeat the cycle if
Count > 1). Note that a Timeout can occur before the second
click is done in which case the second click will not end the
cycle but instead start a new cycle.
Wait for Ack: This green LED is ON as long as the controller
is waiting for a SYNC IN pulse.
Action per point This section can be used to define the actions that have to
be performed at every point of the path.
You can chose an action with the dropdown menu and use
to add it to the sequence.
The buttons to the right can be used to load and save a series
of actions.
The available actions are:
- Manual Handshake, see description above
- Spec 1-3, the systems runs one of the
spectroscopies using all its parameters. For more
information on the Spectroscopy tool see Section
6.6.4
- External handshake see description above
- Move Z to home, this is identical to the retract
action of the z-loop. (Section 6.3)
- Autoapproach, performs the Autoapproach as
described in Section 6.5.5
Path Control The Path Control section can be used to load and save paths
and to start and stop the execution. On how to create a new
Page 91
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

path please see section 6.4.1. The LED indicates whether a
path is executed at the moment.
6.5.7 Dual Pass……………………………
The Dual Pass Mode changes the scan movement so that
each line is scanned twice (forward – backward – forward –
backward) before proceeding to the next scan line. Various
parameters can be altered during the second line pass,
including a constant height offset between first and the
second pass, sometimes referred to as Lift Mode. The Dual
Pass Mode is activated within the Scanner Ctrl; the
parameters used for the second line pass can be set in the
Dual pass Tab. The data from the second pass belongs to a
separate Data group called dual pass. To visualize the data,
please employ the Display Wizard to open new frame or line
views.
Dual Pass Feedback Mode: The Dual Pass Mode allows for
two different modes of operation:
1. Feedback: All the Alternative parameters, explained
in this section, will be applied during the second
pass. This way one can apply for example different
force during the second pass of an AFM scan by
adjusting the cavity tuning.
2. First Line Profile: This option records the sample
topography during the first pass. In the second pass,
the feedback is turned off and the tip is scanned
along the recorded topography plus the Lift Offset.
If made correctly the distance between tip and
sample is kept constant this way. This mode is
especially useful to image long range forces (i.e.
electrostatic or magnetic) without topographic side
effects.
Page 92

To display, record, and save the data from the
second pass, one employs the Display Wizard as
described in section 5.4.4 on page 53.
Below is a detailed description of the behavior with the First
Line Profile Option enabled:
The topography (i.e. Z out) information during the first line
pass (forward and backward) is recorded.
Before starting the second pass, the z feedback is stopped
and the tip is retracted to a certain height specified under
Lift Offset. The speed of this retraction movement is
governed by the Lift Slewrate. The scanner pauses for the
Wait Time in order to give the system the chance to settle.
The topography of the first line pass is repeated in the
defined offset height. At each point, the tip is at the well-
defined distance over the sample surface. Data recording on
each of the ‘normal’ frame views (i.e. those frame views
triggered by Scanner) is stopped. The second pass data is
recorded in data windows triggered by Second Line.
After completing the second pass (forward and backward)
the z feedback is turned on again and the scan is paused for
another Wait Time to let the system settle. The scanner is
moved to the next line and the first pass of the new line
started.
Lift Offset: Specify the distance between tip and surface
during the second pass. Please note that a positive value will
cause the tip to be lifted by this height. Negative values are
forbidden.
Wait Time: Defines the time the scanner is paused at the
beginning and the end of the second pass. Please note that
the Lift Slewrate may automatically be adapted to ensure
that the scanner has reached the defined lift height before
the wait time has ended (before the second pass). After
finishing the second pass, the z feedback will be turned on.
Please make sure that the Wait Time is long enough to give
the feedback the possibility to reach the first pass setpoint.
Lift Slewrate: Defines the voltage rate of change that is
applied to the z scanner to reach the lift height at the
beginning of the second pass.
Alternatives Active: This checkbox enables the alternative
values set for the second pass. This is useful to test the
settings of the second pass
Setpoint, DAC1…: Each line allows to set an alternative value
for these setting. When the checkbox is set, these alternative
parameter will be applied during the second pass.
Page 93
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Crosslink1, Crosslink2: These two allows the user to
selectively turn on the Crosslinks during the second pass.
Only the OFF-> ON direction is possible. A crosslink cannot
be turned off during the second pass.
Please note that some of these parameters only have an
effect if Feedback is selected under Second Pass Feedback
Mode.
6.5.8 Crosslink……………………………
The crosslink feature offers the option to link any input to
one of the DAC outputs. This can e.g. be used to stabilize the
working point of an AFM (crosslink Intensity to the Dither
(DAC1)).
To set up one of the two identical Generic Transfer Functions
you can select Input and Output channel, a starting value and
limits to the output channel and choose the Transfer
Function. This decides the kind of link between the two
channels. PI Feedback allows a PI control similar to e.g. the
Z-Control. Linear enables a direct coupling of input to the
output channel.
To find PI values for a specific application you can use the
Modulation functionality. This works similar to the setpoint
modulation explained in the Section 6.3.3
6.5.9 DAC Outputs
The ASC500 comprises four DAC outputs. They can be used
to output voltages from -10 to 10V. Notice that the voltages
can’t be set when Output Active is not ticked. The possible
output range can be limited in the Output Limits window.
Page 94

6.5.10 Scan……………………………
The scan window tab can be used for Manual Positioning,
moving in a certain direction by a certain Stepwidth with the
Scanners. The On/Off button (Use Sensor Position) for the
Closed Loop Scanning feature is also located here. For
detailed setup of the Closed Loop Scanning feature with FPS
and optical readout please see the corresponding addendum
to the ASC500 manual.
6.6 1-dimensional data displays
6.6.1 Resonance View
Use the Resonance View to find and characterize an oscillation
with frequency and phase response. By pressing the Start
button, the given frequency window will be scanned, while the
response from the HF Lock-in is imaged in the amplitude (left)
and in the phase window (right). Of course any data channels
can be plotted here after adding them in the DCC (check
section 4.2.5 Data Channel Configuration (DCC) in detail). See
section 4.2.2 for details on the internal signal flow.
Be aware that the PLL is connected after the frequency
sweeper. Therefore an activated PLL will effectively
compensate for the frequency sweep. Always turn off the PLL
before running a frequency sweep.
Page 95
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Start: The start frequency for the frequency sweep.
End: The stop frequency for the frequency sweep.
Points: The number of data points to be recorded and
displayed in the images to the right. With fewer points the
calibration run will be faster of course.
Fwd/Bwd: If enabled, after sweeping the frequency from Start
to End, the controller also collects the data from End to Start
and displays it in the same window.
Repeat: The frequency sweep will be repeated several times,
this can be done by entering a respective number in this field.
Please note that zero corresponds to no repetition.
Avg. Time: Specify here the measurement time per pixel. All
collected data during this measurement time will be averaged.
Delay: Enter a delay for each point after the new frequency
value has been set, before the data is taken. This can help to
avoid ringing after the excitation frequency has been changed.
Status LED: Indicates whether the frequency sweep is running.
Start: Starts the frequency sweep.
Select new window: Use this Frame Tool to select a new
frequency window from the amplitude or phase display.
Accepting this range will enter the new start and end values in
the Start, End field. This will also adjust the Min and Max of
the PLL. Keep in mind that a selection during the frequency
sweep running will not work.
Select frequency: If you select a point in the amplitude or
phase window, the respective value will be entered as the new
frequency.
Details: This opens up the Details window.
Page 96

Details:
Wait Start: This is a delay time before the calibration run is
started.
Wait Finish: This is a delay time after the calibration run is
stopped and the system returns to the main frequency as
given in the Lock-In Tab or Dual Pass Tab.
Loop Off: When this is checked the Loop is automatically
turned off before doing a Scan.
6.6.2 Line View……………………………
The Line View is the most elementary form of displaying data.
The data is displayed against time. Although it is a very basic
tool, the line view can be highly useful because of its simplicity
and versatility. It is capable of displaying data in the time range
from milliseconds to kiloseconds.
In the top right corner of the Line View tab, the input
signal can be chosen. You can display any signal of the
ASC500 here. Below the graph are the common tools
to change the display and save the displayed data
(described in detail in chapter 5.4.2).
Signal: Choose the input signal to be displayed in the
line view.
Sample Time: The time which corresponds to one
data point. Since the sampling speed of the ASC500
inputs is 400 kHz, the smallest value to be entered
here is 2.5 µs.
Average: With this check box you can activate data
averaging. This means that all incoming data
(frequency 400 kHz) within one Sample Time is
averaged before it is displayed in line view. If this is
unchecked only the first incoming data points is taken
in each Sample Time window.
Page 97
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

6.6.3 Frequency Analysis View
The Frequency Analysis allows for examination of signals in a
frequency domain representation. The ASC500 offers an
extremely powerful Frequency Analysis tool to help optimizing
the signal, analyzing mechanical or electrical noise and to
better understand properties of oscillating systems like
cantilevers or tuning forks. Signals can be analyzed in a
frequency range from DC to 200 kHz, with possible a frequency
resolution well below 1 Hz (depending on the range). Different
window functions can be used to reduce leakage and a number
of representations can be chosen to meet your application.
The image above shows the Frequency Analysis window. In the
top right corner of the tab, the input signal and the sample
time can be chosen. Above the graph, the FFT parameters can
be set. The graph itself is displayed in a frequency vs.
amplitude style. Please note that the unit of the amplitude axis
is automatically adjusted to the unit of the input signal as
specified in the Transfer Functions Panel.
Time Domain Parameters Signal: Specification of the input signal. One can choose
between any ADC or AFM input, lock-in data, or Z-Out.
Sample Time: One can choose the sample time for the FFT
input signal. The sample time determines the maximum
frequency which can be displayed in the spectrum. Enter
2.5 µs to access the full sampling speed of the ADC converters
(400 kHz), which will allow a FFT from DC to 200 kHz. Increase
the sample time in case the full frequency range is not needed
and also to gain higher frequency resolution. Also, higher
sample times reduce the CPU load.
Average: This button activates time domain averaging, i.e. all
incoming data within one Sample Time is averaged before it is
Page 98

processed by the FFT. One can use this averaging to reduce
aliasing artifacts in low frequency FFT data.
FFT Parameters Fmin/Fmax: Enter the frequency range you want to analyze
here. Fmax must be smaller or equal to 1/(2*Sample Time).
The status line below the input fields immediately shows the
frequency resolution corresponding to the chosen settings.
Window: Setting of the window function used for FFT
calculation. Choose from Rectangular, Hamming, Blackman,
and Flat Top to meet your requirements in either amplitude or
frequency resolution and leakage.
Average: Allows for applying a linear averaging to the FFT data.
In contrast to the time domain averaging, FFT averaging
calculates the mean value of several FFT traces, not input
values. Please note that high Average values may lead to long
update intervals of the FFT graph.
Y-Scaling: Choose between Magnitude[V], logarithmic
Magnitude [dBV], Power Density [dBm] and Power Spectrum
[dBm].
1/SQRT(Hz): Use this button to display the magnitudes
normalized by a 1 Hz factor.
6.6.4 Spectroscopy Tab(s)
With the spectroscopy tabs (Spec 1-3), one or more signals can be recorded while changing certain system
parameters. For example, you can sweep the gate voltage of a quantum dot and record the response of the
dot’s photoluminescence as a function of the gate voltage.
Note that you can change the name of these three tabs in the Aliases menu, see section 5.3.2 for details. In
the supplied images Spec 1 was renamed to z_spec.
There are three basic types of spectroscopies:
1. DAC Spectroscopy: Any of the four standard DAC
outputs can be used for spectroscopy purposes.
2. Z Spectroscopy: this type of spectroscopy will sweep
the Z Out voltage while recording any kind of internal
or external signal.
Page 99
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

3. Low Freq: low frequency spectroscopy changes the
frequency of the low frequency lock-in.
The type of spectroscopy is defined in the DAC drop-down list
of either of the three Spec tabs. All types of spectroscopies are
operated in the same way. For simplicity, we refer in the
following only to a Z-Spectroscopy.
The voltage is swept in a step-like way: the sweep range is
divided into a number of steps (Data Points). The first voltage
step is generated and is kept constant during the
measurement of the response signal. Only after the
measurement of the first data point is finished, the output
voltage changes to the next point.
The settings for this calibration are similar to those in the
Resonance tab.
Start: Specify the start position within the allowed z-range .
End: Specify the end position within the allowed z-range . If
End is smaller the Start, the output will be swept backwards.
Points: Specify the number of data points between Start and
End. Please note that this number is slightly altered once you
start the sweep. This is because of the quantized nature of the
digital output; the minimum step size of the 16 bit DAC output
is for example 300 µV.
Fwd/Bwd: If activated, the voltage is swept from Start to End
and then back to Start. If the end is not reached (for example
due to Limiter) the backward scan is omitted.
Repeat: If the measurement should be repeated
automatically, increase the Repeat value. Please note that by
default, the graph will only show one measurement trace. To
display more than one trace in the spectroscopy view, open
the Ranges dialog of the Spectroscopy View (see section 0 for
details).
Avg Time: Specify here the measurement time per pixel. All
collected data during this measurement time will be averaged.
Delay: Enter a delay for each point after the new value has
been set, before the data is taken.
Details: Opens the Details dialog window:
Page 100

Wait Start: Delay time before the spectroscopy is started.
Wait Finish: Delay time after the spectroscopy is finished.
Loop Off: Switches the feedback loop off during the
measurement. Especially with the Z-Spectroscopy, it is
important to switch the loop off; otherwise the loop override
the spectroscopy. When the spectroscopy measurement is
finished, the loop is automatically switched on again.
Limiter Active: Activates the Limiter. When a certain
condition is met the Spectroscopy will be stopped.
Limiter Source: Signal to trace during the measurement.
Limiter Value: Exact value for the limit criteria.
Limiter Sign: Stop when Value is exceeded or when the signal
falls below Value.
The end of the sweep range is the trigger for both Save
delayed at the end of the frame and backward sweep.
Therefore when a limiter is used it is possible that the data
won’t be saved automatically, and the backward scan won’t
happen.
The graph generated can be manipulated and saved using
general graph tools described in detail in section 5.4.2.
6.6.5 Soft Spec……………………………
The Soft Spec can be used similarly to Spec 1-3. The displayed
value can be selected in the top left corner of the tab.
Unlike for the other Spectroscopies you can use most any of
the input fields as the sweep variable.
To set up the sweep, right klick on the desired input field (e.g.
Amplitude in the Excitation tab) and choose Spectroscopy.
Page 101
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

The Soft Spectroscopy setup window opens up. Here you can
set the Start and End values of the sweep. Also you can
choose a number of Steps and the Delay between each
points.
Run starts the measurement and outputs the data in the Soft
Spec tab.
6.7 Working Examples
6.7.1 Setting up the PLL
A completely digital Phase Locked Loop (PLL) is integrated in
the ASC500. With the PLL, an advanced operation mode is
provided to control high Q oscillators (like tuning forks at low
temperatures). The PLL mode is an alternative to standard
non-contact mode operation. During the standard operation
the oscillator (tuning fork or cantilever) is driven at a fixed
frequency and the change in oscillation amplitude is used to
drive the z controller and to gain topographic information. This
mode will be called amplitude modulation mode in the
following sections, in contrast to frequency modulation or PLL
mode.
In a typical non-contact AFM measurement, the oscillating tip
is brought into the force field of the sample surface. Figure 15
shows the response of the oscillation properties of the tip on
the force gradient originating from the sample. PLL and
amplitude modulation mode differ in the way the controller
reacts to such changes in oscillation properties. In amplitude
modulation mode, the tip is constantly excited with the
frequency f0, i.e. the resonance frequency of the freely
oscillating lever.
Page 102

A f
π /2
f f f f
0 0
Figure 15: Amplitude and phase response of a driven oscillator in presence of a force gradient (black curve
shows response at no gradient, dark blue and light blue curves at increasing force gradient). f denotes the
0
resonance frequency of the oscillator without an applied force gradient. With increasing force, the amplitude
maximum is damped and shifts to lower frequencies. The phase response also shifts to lower frequencies and
the maximum slope of the curve decreases. The working points in amplitude modulation mode (red dots) and
in PLL mode (green dots) are displayed in the curves. The PLL mode traces the resonance frequency of the
oscillating lever.
Figure 15 demonstrates the different behavior of both
modes. The measured oscillation amplitude follows the red
dots. The measurement does not reflect the real amplitude
damping due to sample forces; the amplitude drops due to
the shape of the amplitude response curve. In PLL mode, the
excitation always follows the amplitude maximum (i.e. the
resonance frequency shown by the green dots), giving more
valuable physical information. The question is how it can be
achieved that the excitation always follows the resonance?
At the resonance frequency, the phase shift between input
and output signal is always /2. This fact is used in PLL mode
to control the excitation frequency. An extra proportional
integral control loop is operated to keep the excitation on
resonance. The input value for this loop is the phase
between excitation and oscillation signal as it is calculated by
the internal lock-in amplifier, the output value is the
excitation frequency or simpler the shift in excitation
frequency f. This control loop is called phase loop. The
frequency shift f is directly proportional to the force
gradient that affects the lever oscillation. Figure 16 shows a
schematic of the frequency-modulated AFM operation mode
that relies on the PLL. The output of the phase loop is used
as an input for the z controller, keeping the frequency shift
and thus the force on the tip constant.
Page 103
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Figure 16: Schematic of the PLL operation mode.
The PLL mode is an advanced mode to operate, in the sense
that two PI loops have to be operated at the same time.
Potential instabilities in one loop will directly affect the other
loop. The advantages are twofold:
1. The measured signal f will give a direct measure on
the force gradient acting on the tip.
2. The PLL allows higher scan speeds for high Q levers.
PLL controller P and I units The physical units of the P and I parameters of the feedback
controllers can be found here:
Amplitdue Control
Input signal P unit I unit
HF 1 Ampl V/V V/V/s
Frequency Control
Input Signal P unit I Unit
HF 1 Phase kHz/deg kHz/deg/s
ADC1 .. 6 kHz/V kHz/V/s
Operation of the PLL
Preparations Before employing the PLL, all relevant connections have to
be made. In particular, the signal from the oscillating lever
has to be connected to the HF IN 1 input and the dither signal
Page 104

has to be connected to HF OUT 1. With these connections,
the lever signal will be addressed via HF 1 within the Daisy
software, and the demodulated lock-in signal will be
HF 1 Ampl and HF 1 Phase.
While the PLL is running, a number of signals are interesting
to observe:
 HF 1 Phase: the phase between lever excitation and
lever oscillation. This is the input signal for the
phase loop.
 HF 1 Ampl: the amplitude of the lever oscillation. In
PLL mode this is a measure of the oscillation
damping due to sample forces.
 df: the frequency shift relative to the free
resonance frequency of the lever. This is the output
signal of the phase loop and at the same time the
input value of the Z Controller
 Z out inv: this is the output value of the Z Controller
that gives the topographic information.
Find the resonance of the cantilever using the Resonance
Resonance View
feature (section 6.6.1) of the ASC500.
Choose an appropriate excitation amplitude in the Lock In
tab and set the Integration Time of the lock in to a reasonable
value (500 µs .. 2 ms). After starting the Resonance, set the
excitation frequency to match the resonance frequency and
set the offset phase (under Lock In, High Frequency,
Demodulation, Phase Shift) so that the HF LI 1 Phase at the
resonance frequency is 0. The result should look similar to
Figure 17.
Figure 17: Recording amplitude and phase response of the lever using the Resonance tool. This picture is from
v26 daisy software.
Phase Loop settings The phase loop settings can be found in the PLL tab under
Frequency Control. Before you turn on the loop, the
following settings have to be made:
 Limit the range of the output frequency to gain
higher frequency resolution. A range of 1 to 2 kHz
Page 105
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

around the resonance is recommended. Insert the
appropriate values to the Min and Max fields.
 Choose the proportional and integral parameters
for the loop. Start with small values (P = 10 µ and
I = 1 mHz). The P/I const button always keeps the
ratio of P and I constant when one parameter is
changed.
 The input signal for the phase loop can be selected
in the Actual Value list. Mostly, this will be set to HF
1 Phase, so that the internal lock in is delivering the
phase signal. In case an external lock in amplifier is
used for the phase detection, connect it to one of
the ADC inputs and choose the respective ADC in
the Actual Value list.
 If the phase offset was correctly compensated (see
Preparations), the Setpoint value is 0 deg. Check the
Inv. Polarity button as the phase response has a
negative slope.
The phase loop can now be started by checking the Loop
button. The green LED will be turned on and the value in the
df field will by constantly updated to show the current value
of the frequency shift. The Frequency Control unit should
look similar to Figure 18.
Figure 18: Phase loop settings.
Page 106

Before the z controller is started, it is important to improve
the P and I settings of the phase loop. Open the Setpoint
Modulation window and choose HF 1 Phase and df to be
shown in the two Line Views. The Setpoint modulation will
periodically change the phase loop setpoint between two
values, simulating the loop response to a step function input.
Choose a Period of 1 s and an alternate setpoint Value of 5
deg. Start the setpoint modulation by checking the button.
Change the phase loop P and I parameters until the df line
view shows a stable step function with only a light overshoot
as shown in Figure 19. Now that the phase loop is stable and
optimized, the setpoint modulation has to be stopped.
Figure 19: Using the Setpoint Modulation to optimize the phase loop parameters.
Z controller settings Now the z controller can be employed. Choose df as the
Actual Value for the z controller. The polarity of the z
controller depends on the application: for application with
increasing frequency shift with increasing force on the tip
(mostly tuning forks) the z controller setpoint should be
positive and the Inv. Polarity button in the z controller should
be left unchecked. If the frequency shift decreases with
increasing force on the tip, the setpoint should be chosen
negative and the Inv. Polarity has to be checked. If the tip is
within z scanner reach of the sample, turn on the z feedback
using slow P and I parameters (if the tip is further away,
employ the Autoapproach). Start the scan with a low scan
speed ( ≤ 1 µm/s) and tune the z controller P and I parameter
until a stable and fast feedback is reached.
Figure 20 shows a measurement in PLL mode of a Si test
grating done in Daisy V2 (outdated version).
Page 107
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

Figure 20: Screenshot of PLL operation. The measurement was taken with an outdated daisy version.
Page 108

6.7.2 Using the Q-control feature
Any oscillating system showing resonance behavior can be
described by a Q factor. The Q factor is a measure of the
dissipative forces acting on the oscillating system.
In non-contact mode AFM, the Q factor is a function of the
internal damping of the lever (cantilever or tuning fork) and
the lever environment (fluid, ambient, high vacuum, and UHV).
The Q factor is a very important parameter for non-contact
AFM, because it determines or constrains important
measurement parameters such as sensitivity and scan speed.
Given a certain measurement environment and a certain lever,
the Q factor can be easily measured but it cannot be altered in
standard SPM applications. The ASC500 Q Control feature
enables changing the Q factor and thus gives access to the
control of important measurement parameters.
The Q control can be especially helpful in two situations:
1. Non-contact measurements in a low temperature
and/or UHV environment. Q factors in these
environments can get very high (up to 105-106),
resulting in very small damping of the oscillation
amplitude and thus to very large time constants for
changes in the oscillation amplitude (order of tens of
seconds). In amplitude modulation mode, the z
feedback control will work directly on this very slowly
changing oscillation signal, thus reducing the scan
speed significantly. Q reduction is a very effective way
to overcome these speed limits.
2. Measurements in a liquid environment typically show
very low Q factors (< 100). Increasing the Q factor
may give reasonable sensitivity for these
measurements.
6.7.2.1 Schematics To gain access of the control over the Q factor, a sophisticated
oscillation scheme is necessary. The excitation signal for the
lever is composed in the Signal Adder from two parts:
The first part is the fixed AC signal at the resonance frequency
of the lever, coming from the Lock-In amplifier.
The second part is the signal that is deduced from the
oscillation signal of the lever: The output of the lever is
demodulated by the internal Lock-In detector to obtain its
amplitude and phase (relative to the fixed excitation signal).
These signals are routed into a phase shifter and an amplitude
gain and a new oscillating signal is synthesized in the
Oscillation Generator, called Feedback Excitation.
One can show mathematically that feedback signals with a
phase shift of +/- /2 enhance or reduce the effective damping
in the system. The lever will behave exactly as if it was built in
Page 109
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

a different way or if the environment has changed. Below, one
can see the schematics of the Q control excitation.
The Q factor can be measured with the Resonance feature (see
section 6.6.1 on page 95). Find the FWHM (full width half
maximum) f from the amplitude vs. frequency plot to the left.
The Q factor is then calculated using the relationship:
Q = f / f
res
The Q Control controls can be found in the Lock In tab. There
are only two parameters and one Enable button. You can set
the phase shift between the cantilever oscillation and the
feedback excitation signal and the gain of the feedback signal.
Page 110

Enable: Turns the Q control on or off. Please note that turning
the Q control on or off may change the oscillation amplitude
of the lever significantly. Although this will not damage the tip,
you may want to use the excitation amplitude field Aexc (pp)
to reduce the excitation before checking or unchecking the
Enable button.
Phase: Sets the phase shift between the lever oscillation and
the feedback excitation signal. Although in theory this should
be either +90 deg or -90 deg, there are always additional phase
shifts due to electronic components in the signal path and due
to the (short but non-zero) time it takes for the ASC500 to
demodulate the signal. The best way to find the right value is
to change the Phase systematically while repeatedly doing the
Resonance (set the Curves value of both Resonance views to
10 or larger to have several frequency sweeps displayed in one
graph). For values differing from +/-90 deg phase, the
resonance frequency is shifted in frequency. By going stepwise
through the -180 deg .. +180 deg Phase range, one should see
the maximum of the amplitude resonance curve moving
around in a circle. Note the values for minimum resonance
peak if you want to reduce the Q factor or either note the
Phase value of the maximum if you want to enhance the Q
factor. If you don’t see any changes, increase the Feedback
value.
Feedback: This sets the gain of the feedback excitation signal.
The range of this value is 0 to 1. Please note that for values
above 0.5, the effective value of the fixed excitation is reduced
to strengthen the feedback excitation part. One can easily
Page 111
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

increase the fixed excitation if only loosing signal amplitude
and not seeing any impact on the Q control. For most
applications, a value of larger than 0.85 will be necessary to
effectively alter the Q factor.
The above examples show the Q reduction of a cantilever
based AFM at 4 K. The Q factor could be reduced by
approximately one order of magnitude (note that the original
amplitude response is not shown).
Please note that due to the self-excitation nature of the Q
control, the oscillating system can show rather strange
behavior far off the resonance frequency of the lever. This
does not have any consequences on the reproducible and
stable behavior of the Q control near the resonance frequency.
Page 112

7 Firmware Upgrade
At some point a new version of the “daisy.exe” might be
available for the ASC500. As there is no permanent firmware
inside the ASC500, all one has to do is to boot the controller
with the new software. This uploads the new hardware
program onto the controller.
So, all that needs to be done is to install the software as
written in section 5.1.
Page 113
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

8 Preventive Maintenance
Warning. The equipment contains no user serviceable parts. There is a risk
of severe electrical shock if the equipment is operated with the covers
removed. Only personnel authorized by attocube systems and trained in
the maintenance of this equipment should remove its covers or attempt
any repairs or adjustments. Maintenance is limited to safety testing and
cleaning as described in the following sections.
8.1 Safety Testing
Safety testing in accordance with local regulations, should be performed
on a regular basis, (typically annually for an instrument in daily use).
Caution. The instrument contains a power supply filter. Insulation testing
of the power supply connector should be performed using a DC voltage.
8.2 Fuses
Two T 4 A/250 V fuses are located on the back panel.
Note. When replacing fuses:
Switch off the power and disconnect the power cord before removing the
fuse cover.
Always replace broken fuses with a fuse of the same rating and type.
8.3 Cleaning
Warnings:
Disconnect the power supply before cleaning the unit.
Never allow water to get inside the case.
Do not use any type of abrasive pad, scouring powder, or solvent, e.g.
alcohol or benzene.
The front panel may be cleaned with a soft cloth, lightly dampened with
water or a mild detergent.
Page 114

Note. Any time you call for technical support, the software version and
the serial number are essential to trouble-shoot a problem. The serial
number is shown on the backside of the ASC500. the software version can
be queried in the “Help -> About” menu.
Page 115
© 2001-2020 attocube systems AG. Product and company names listed are trademarks or trade names of their respective
companies. Any rights not expressly granted herein are reserved. ATTENTION: Specifications and technical data are subject to
change without notice.

attocube systems AG
Eglfinger Weg 2
D-85540 Haar
Germany
Phone +49 89 420 797 0
Fax +49 89 420 797 201 90
E-Mail: info@attocube.com
www.attocube.com
Page 116