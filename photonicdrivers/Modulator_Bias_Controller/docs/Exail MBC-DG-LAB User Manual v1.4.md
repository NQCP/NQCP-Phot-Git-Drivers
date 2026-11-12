MODULATOR BIAS CONTROLLER
MBC-DG-LAB
USER MANUAL
Version 1.4
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57
25000 Besançon, France www.photonics.ixblue.com

Legal Notice ................................................................................................................ 3
Disclaimers ............................................................................................................. 3
About this Manual ....................................................................................................... 3
Purpose ................................................................................................................... 3
Audience ................................................................................................................. 3
Prerequisites ........................................................................................................... 3
Terms and Symbols in this Manual ......................................................................... 3
Electrical Safety ...................................................................................................... 4
Ventilation of the MBC-DG-LAB .............................................................................. 4
Contacting exail PSD: ............................................................................................. 4
General Information .................................................................................................... 5
Mach-Zehnder intensity modulators ........................................................................ 5
Product Overview .................................................................................................... 6
Principle .................................................................................................................. 6
Mechanical Dimensions .......................................................................................... 8
Getting started ............................................................................................................ 9
Standard Accessories ............................................................................................. 9
Installation and first time operation ......................................................................... 9
Operation ...................................................................................................................11
Selecting Auto/Manual mode ................................................................................ 11
Selecting transfer level .......................................................................................... 11
Auto Calibration .................................................................................................... 11
Adjusting dithering frequency ................................................................................ 11
Adjusting dithering amplitude ................................................................................ 11
Adjusting the photocurrent gain circuit .................................................................. 11
Troubleshoot: .............................................................................................................12
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57 2
25000 Besançon, France www.photonics.ixblue.com

Legal Notice
Disclaimers
No warranties : This documentation is provided « as is » without any express or
implied warranty of any kind.
Limitation of Liability : exail does not assume any liability arising out of the application
or use of any products, or software described herein. In no event shall exail be liable for any
damage whatsoever (including, without limitation, consequential or incidental damages,
damages for lot of profits, or otherwise) arising out of the use of the information provided in
this documentation.
The contents of this publication have been carefully checked for accuracy. However,
exail makes no warranty as to the completeness, correctness, or accuracy of the information
contained within this documentation. In the interest of continued product improvement, exail
further reserves the right to make any change in any products describers herein without
notice. This publication is subject to change without notice.
About this Manual
Purpose
The purpose of this instruction manual is to explain how to set up the MBC-DG-LAB
and to utilize the various features of the product.
Audience
This manual is designed to professionals with the necessary technical background
and prerequisites needed to use fiber optics components, including Mach-Zehnder lithium
niobate modulators, and the related test equipments and accessories.
Prerequisites
Reader is assumed to be familiar with fiber optics technology.
Terms and Symbols in this Manual
The following terms and symbols may appear throughout this manual :
WARNING : Warning statement identify conditions or practices that could result in injury or
loss of life
CAUTION : Caution statement identify conditions or practices that could result in damage to
this product or other property
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57 3
25000 Besançon, France www.photonics.ixblue.com

Electrical Safety

|     |          | Do not attempt to perform servicing or maintenance  |     |     |     |     |
| --- | -------- | --------------------------------------------------- | --- | --- | --- | --- |
|     | WARNING  |                                                     |     |     |     |     |
To avoid personal injury, do not operate this instrument without
the protective cover of the chassis. Do not make any service or
maintenance of any kind to the system.
Refer servicing only to authorized personnel from exail.

|     |          | Operate under the proper environmental conditions.   |     |     |     |     |
| --- | -------- | ---------------------------------------------------- | --- | --- | --- | --- |
|     | WARNING  |                                                      |     |     |     |     |
The MBC-DG-LAB is designed for indoor use, only. To avoid
the possibility of injury, do not expose this instrument to rain or
|     |     | excessive  | moisture.  | Do  not  operate  | the  instrument  | in  the  |
| --- | --- | ---------- | ---------- | ----------------- | ---------------- | -------- |
presence of flammable gases or fumes.

Ventilation of the MBC-DG-LAB

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
WARNING  Do not cover the MBC-DG-LAB with any covering or overlay.

Contacting exail PSD:

For application oriented questions, for questions related to service, please contact exail PSD
Besançon
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
     exail
|   Photonic Solutions Business Unit  |     |     | T. : +33 3 81 85 31 80  |     |     |     |
| ----------------------------------- | --- | --- | ----------------------- | --- | --- | --- |
4
| 3, rue Sophie Germain, TEMIS  |     |     | F. : +33 3 81 85 15 57    |     |     |     |
| ----------------------------- | --- | --- | ------------------------- | --- | --- | --- |
|   25000 Besançon, France      |     |     | www.photonics.ixblue.com  |     |     |     |

General Information
Mach-Zehnder intensity modulators
Lithium niobate (LiNbO3) Mach-Zehnder intensity modulators are external modulators
that have been widely used since the mid-nineties, mostly in long haul optical networks for
their ability to modulate optical signal from 1300 nm and 1550 nm laser diodes with short
transition times and without chirp. Thanks to their broad wavelength performance, they
currently also offer modulation solutions to 1064 nm and other near infrared lasers.
Mach-Zehnder modulators are interferometric devices and exhibit a sine transfer
function (Figure 1). Although highly stable components, their operating point can suffer slow
drift due to variations of external conditions and that drift may result in variations of key
performances like extinction ratio.
In order to adjust the operating point of Mach-Zehnder modulators independently from
the high frequency modulation signal applied, they can be designed with two sets of
electrodes: one set of electrodes, the RF Electrodes, is used to apply the RF signal (PRBS
data stream, analog signal, short pulses…). The second set of electrodes, the DC Bias
Electrodes, is generally used to adjust with a fixed voltage the working point of the
modulator. Figure 2 illustrate the typical electrode architecture of Mach-Zehnder modulator.
Figure 1 : transfer function of a Mach-Zehnder modulator and data output vs data input at
QUAD+ and QUAD- operating point
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57 5
25000 Besançon, France www.photonics.ixblue.com

Figure 2 : typical electrode and waveguide architecture of a Mach-Zehnder modulator
Product Overview
MBC is a bias controller specially designed to stabilize the operating point of LiNb03
Mach-Zehnder modulators by monitoring the bias voltage applied on the DC electrodes of
the devices.
The MBC controllers can lock any modulator and allows for continuous tuning of the
operating point. The continuous format such as ERZ (Electrical Return to Zero) where the
operating point must be set at 33% or 66% of the maximum transmission.
Principle
Figure 3: basic scheme of a modulation set-up including a modulator bias controller and an
external monitoring photodiode
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57 6
25000 Besançon, France www.photonics.ixblue.com

A Mach-Zehnder modulator is illuminated by a laser at the optical input. The data
stream is applied to the RF electrodes. At the output of the MZ modulator, a fiber coupler
with a strong imbalance (10:90 or 1:99) allows to detect a small portion of the transmitted
light with a monitoring photodiode. The signal is amplified and processed in order to control
the stability of the operating point. Any deviation is compensated by a new value of the
electrical bias voltage applied by the feedback loop in order to maintain the operating point at
the desired position.

The principle of operation of the MBC is based on the generation of a very low
frequency and low amplitude electrical signal (dither signal), which is summed to the DC bias
voltage. Any deviation from the working point creates harmonics that can be measured and
compared by frequency analysis and by signal processing carried out by a specific algorithm,
developed by exail, in order to retrieve the sign and the amplitude of the deviation.

The modulator is polarized in quadrature QUAD+ or QUAD- as the second harmonic
is null. Otherwise, the modulator can be polarized on MIN or MAX as the first order is null.
Any other transmission state is also possible thanks to a dedicated algorithm function.
F F T  A m p litu d e
|     |     | M A X | fd 2 x f  |         |     |
| --- | --- | ----- | --------- | ------- | --- |
|     |     |       | ith e r d | ith e r |     |
1
0,9
| F F | T  A m p litu d e |     | F F T  A | m p litu d e |     |
| --- | ----------------- | --- | -------- | ------------ | --- |
0,8
0,7
|     | fd 2 f            | 0,6 | fd  | 2 f               |     |
| --- | ----------------- | --- | --- | ----------------- | --- |
|     | x                 |     |     | x                 |     |
|     | ith e r d ith e r |     |     | ith e r d ith e r |     |
0,5
|     | Q U A D  + |     | Q U | A D  - |     |
| --- | ---------- | --- | --- | ------ | --- |
0,4
0,3
0,2
0,1
|     | F F T  A | m p litu d e |     |     |     |
| --- | -------- | ------------ | --- | --- | --- |
0
| -5 -4 | -3 -2 | -1 0 | 1 2 | 3 4 | 5   |
| ----- | ----- | ---- | --- | --- | --- |
M IN
M IN
|     | fd  | 2 f                 |     |     |     |
| --- | --- | ------------------- | --- | --- | --- |
|     |     | ith e r x d ith e r |     |     |     |

     exail
  Photonic Solutions Business Unit  T. : +33 3 81 85 31 80
7
3, rue Sophie Germain, TEMIS  F. : +33 3 81 85 15 57
  25000 Besançon, France  www.photonics.ixblue.com

Mechanical Dimensions
221mm x 221mm x 44mm
MBC LAB:
<1> Power button
<2> Control LED
Lock: MBC is locked to the fixed point (still active when laser light is off)
Scan: MBC is performing a scan. If flashing, no signal detected.
<3> Bias Modulator connector (BNC)
<4> Input Optical Connector
<5> Output optical connector (coupler option)
<6> Power supply connector (Jack 3.5mm, 12V 500mA)
<7> USB connector
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57 8
25000 Besançon, France www.photonics.ixblue.com

Getting started
Standard Accessories
User Manual
Interface User Manual
Cord Kit
USB Cord
AC-DC Power Supply
Installation and first time operation
Proceed as follow to install the MBC-DG-LAB:
▪ Set MBC LAB on a flat stable surface
▪ Connect the power supply plug-in to the power supply connector <6>
▪ Connect the modulator optical output through a tap coupler for "no coupler option",
directly for "coupler option" to "In"-connector of the MBC-Lab(<4>).See optical
connection schemes bellow.
▪ Connect the BNC cable to "DC-Bias" (<3>) and the black (Ground) and red (DC Bias)
wires to the bias electrode of the modulator.
▪ Switch on the laser to illuminate the modulator at the desired optical power level
▪ Power ON the MBC-DG-LAB <1>
▪ A procedure of initialization by scanning the Vbias range from –10V to +10V will start
to adjust automatically the operating point by use of the initial conditions
▪ After stabilization, the RF signal can be applied and the parameters of the MBC can
be modified.
▪ Any change of the dither frequency results in a new search of the operating point by
scanning of the bias voltage from –10V to +10V.
Setup with an external coupler (no Setup with an internal coupler (coupler
coupler option): option):
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57 9
25000 Besançon, France www.photonics.ixblue.com

IMPORTANT NOTES:
1- The optical signal processing in the MBC is such that the value of the RF amplitude
voltage is limited. The limit is 0.75V and the MBC will not work correctly if the RF signal with
a larger amplitude is applied to the modulator.
A 0.75V amplitude is equivalent to a 1.5V peak-to-peak value and the majority of the
applications operate with a lower RF signal: typically 0.5V amplitude (or 1V peak-to-peak).
Thus, in spite of that restriction, the MBC will operate correctly with most of the application.
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57 10
25000 Besançon, France www.photonics.ixblue.com

Operation
For more information on the way to set parameters, please refer to the GUI interface
handbook.
Selecting Auto/Manual mode
One can choose between two operation modes: AUTO or MANUAL.
In AUTO mode, the board searches the bias value corresponding to the selected transfer
level.
In MANUAL mode, one set the DC bias value, and no dither is applied to DC Bias.
Selecting transfer level
Transfer Level is characterized by its level in % (MIN is 0, MAX is 100, QUAD+ is +50,
QUAD – is –50). In general for digital NRZ and analog signals, the transfer level is set to
QUAD. For pulse application, MIN point is privileged.
Auto Calibration
Auto Calibration will set the parameter dither amplitude and photodiode gains to an optimum,
depending on the chosen transfer level point: Quad, Min or Max. The board will switch to
Auto mode at the end of the calibration sequence.
Adjusting dithering frequency
The MBC allows the user to adjust the dithering frequency between 400 Hz and 1400 Hz. It
is set by default at 1000Hz. This feature proves especially useful to avoid any interference
between the RF signal and the dithering signal or when more than one modulator with MBC
are used in the same link.
Adjusting dithering amplitude
The MBC allows the user to adjust the dithering amplitude between 10 mV and 1 V. This
feature proves especially useful to optimize the overall performance of the MBC and to adapt
to various conditions such as modulator Vpi or photodiode response. In auto calibration
mode dither amplitude is set to 3% of the Vpi in Quad mode and 0.2% in Min and Max mode.
Increasing dither, in general 20 to 50mVpp can help for feedback loop stabilization at low
optical power (-20dBm on photodiode for example).
After modifying this parameter, one must do a scan restart.
Adjusting the photocurrent gain circuit
The MBC 2 offers 127 different gain values for the photocurrent circuit so as to adapt to the
largest variety of applications and to offer the widest dynamic range for the input
photocurrent. For Quad mode it is recommended to keep the gain under 110, otherwise the
feedback loop may oscillate.
After modifying this parameter, one must do a scan restart.
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57 11
25000 Besançon, France www.photonics.ixblue.com

It must be noticed that the photocurrent range within a gain position may slightly vary
with the operating mode and the dithering amplitude. The Min mode requires less
photocurrent than the Quad+ mode due to the higher sensitivity of the detection. Also, higher
dithering amplitude will make the detection easier and will lower the low limit of the photo
current range.
Troubleshoot:
Shifted Quad point Quad point can be shifted, when the optical power illuminating the
photodiode is too high. It will happen when the photodiode current
increase over 500µA at max point. Optical power onto the photodiode
has to be decreased.
Feedback loop If the feedback loop oscillates fast, one should increase the dither
oscillation amplitude (10 to 50mVpp) and reduce the photodiode gain (10 to 20).
If it doesn’t work, one should check that the optical power on the
photodiode at MAX point is sufficient to obtain a minimum of 8.5µA at
the output of the photodiode.
exail
Photonic Solutions Business Unit T. : +33 3 81 85 31 80
3, rue Sophie Germain, TEMIS F. : +33 3 81 85 15 57 12
25000 Besançon, France www.photonics.ixblue.com