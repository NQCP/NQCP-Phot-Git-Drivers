CPA 3.xxx.x Digital Panel User Manual
Effective Date: 2020/06/16 Page 1 of 25 IMC096

Table Of Contents
Screen Flow Diagram ............................................................................................................................................ 3
Status Menu Tab ..................................................................................................................................................... 4
Status / Simple ........................................................................................................................................................ 5
Status / All Inputs .................................................................................................................................................. 6
Status / Events ......................................................................................................................................................... 7
Status / Pressures .................................................................................................................................................. 8
Status / Locked Outs ............................................................................................................................................. 9
Status / Diagnostics ............................................................................................................................................ 10
Settings Menu Tab ............................................................................................................................................... 11
Settings / Date, Time, Units ............................................................................................................................. 12
Settings / About ................................................................................................................................................... 13
Settings / Sensing Options .............................................................................................................................. 14
Settings / Cold Head ........................................................................................................................................... 15
Settings / Inverter – (if applicable) ............................................................................................................. 16
Settings / User Options ..................................................................................................................................... 17
Networking Tab ................................................................................................................................................... 18
Communications Protocols ............................................................................................................................. 19
Effective Date: 2020/06/16 Page 2 of 25 IMC096

Screen	Flow	Diagram
This is a general flow diagram of the screens available.  The "All Inputs Screen" is the default starting screen.
| Status Tab               |     |   Settings Tab  |                             |   Network Tab  |     |
| ------------------------ | --- | --------------- | --------------------------- | -------------- | --- |
|   Simple Screen          |     |                 | Date / Time / Units Screen  |                |     |
|   All Inputs Screen      |     |                 | About Screen                |                |     |
|   Events Screen          |     |                 | Sensing Options Screen      |                |     |
|   Pressure Screen        |     |                 | Cold Head Screen            |                |     |
|   Lockout Status Screen  |     |                 | Inverter Screen             |                |     |
|   Diagnostics Screen     |     |                 | User Options Screen         |                |     |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

| Effective Date: 2020/06/16  |     |     | Page 3 of 25  |     | IMC096  |
| --------------------------- | --- | --- | ------------- | --- | ------- |

Status Menu Tab
Legacy UI
This screen allows the operator to navigate between various status screens or to adjacent
menu screens.
Effective Date: 2020/06/16 Page 4 of 25 IMC096

Status / Simple
Legacy UI
The left dial indicates the low or gas input pressure and the right dial indicates the high or
output pressure. Status about the running state of the compressor will be displayed on
the Feedback Label. The bottom right Hours number tracks the total hours of operation
the compressor has been running.
Effective Date: 2020/06/16 Page 5 of 25 IMC096

Status / All Inputs
Legacy UI
The "All Inputs" screen is designed to give the user a complete picture of all the
temperatures and pressures being monitored by the system. The Coolant In & Out icons
will change depending on the system attached. The pressure readings are a result of
averaging data over a 20 second period. If the compressor has an inverter, inverter
current and frequency information is also displayed on the left of the screen along with
detected cryocooler RPM. This RPM is detected via gas pulses.
Effective Date: 2020/06/16 Page 6 of 25 IMC096

Status / Events
The "Events" is an event logging window. It will hold up to 200 events. The format of the
time stamping is Day - Time.
Effective Date: 2020/06/16 Page 7 of 25 IMC096

Status / Pressures
The pressure monitoring mode has a time span of 2 seconds. The high and low pressures
scales are independent and auto adjust based on captured data. A pause button is
provided to allow closer examination of the charts.
Effective Date: 2020/06/16 Page 8 of 25 IMC096

Status / Locked Outs
If the compressor experiences 6 or more errors in under an hour, it will shut down and
begin a cooling timer. This screen will show you what issues have occurred over the last
hour.
Effective Date: 2020/06/16 Page 9 of 25 IMC096

Status / Diagnostics
The diagnostics screen is used to indicate the status of the different digital inputs and
outputs. This screen is useful for diagnosing running issues if they arise. If you click on the
Review Trip Points button the next screen will appear allowing the operator to review
what temperatures and pressures this system will alarm at.
Effective Date: 2020/06/16 Page 10 of 25 IMC096

Settings Menu Tab
Effective Date: 2020/06/16 Page 11 of 25 IMC096

Settings / Date, Time, Units
To adjust the time and date, click on the section you wish to change then use the up and
down arrows to make the changes. The segment may not highlight even though you click
on it. Just try changing the value after you have clicked on the item you wish to change.
Effective Date: 2020/06/16 Page 12 of 25 IMC096

Settings / About
All pertinent version info is stored here.
Effective Date: 2020/06/16 Page 13 of 25 IMC096

Settings / Sensing Options
This screen allows the operator to disable a single sensor, the sensor may be ignored
allowing the compressor to run until such time that the sensor can be replaced. This is
also where the use of Legacy UI can be enabled. The Good Range Indicators only applies
to temperature scales in the Legacy UI format.
Effective Date: 2020/06/16 Page 14 of 25 IMC096

Settings / Cold Head
This screen allows inspection of the parameters used to operate the cryocooler. Note the
Amp Driver Parameters only properly update while the system is not running. Smoothing can
be used to try and reduce the amount of motor vibration in the cryocooler.
Effective Date: 2020/06/16 Page 15 of 25 IMC096

Settings / Inverter – (if applicable)
This screen allows inspection of the parameters used to operate the inverter. Different
controls will become active when you are allowed to change them. To help in configuring PID
functionality, there are input boxes that you can enter properties of the sensor being used to
provide feedback. You enter the range of the sensor and the desired target value in the Scale
Range column, then enter the output signal range in the Signal Range column. The See
Inverter Errors button will bring of the screen below. Any errors detected will illuminate.
Effective Date: 2020/06/16 Page 16 of 25 IMC096

Settings / User Options
Different operator levels provide access to special features. The general user should be
logged in as "user" with no password.
Effective Date: 2020/06/16 Page 17 of 25 IMC096

Networking Tab
This page shows the IP data that gets assigned to the device by its network. By connecting
to the compressor via serial port or by Ethernet it is possible to remotely monitor and
operate the compressor. Compressors with a single DB-9 port only support RS-232.
Compressors with two DB-9 ports also provide an RS-485 port.
Effective Date: 2020/06/16 Page 18 of 25 IMC096

Communications Protocols
The serial port uses Modbus RTU protocol and the Ethernet port uses ModbusTCP. More
information about these protocols can be found here:
http://modbus.org/docs/PI_MBUS_300.pdf
The registers used for this protocol are as follows:
 30,001 - Operating State (int)
 30,002 - Compressor Running (int)
 30,029 - Pressure Scale (int)
 30,030 - Temp Scale (int)
 30,031 - Panel Serial Number (int)
 30,032 - Model Major + Minor Numbers (int)
 30,033 - Software Rev (int)
 30,034 - Detected RPM in 1/100th Scale (int)
 30,035 - Software Variant (int)
 30,036 - Inverter Frequency in 1/10th Hz (int)
 30,037 - Inverter Current in 1/10th Amps (int)
 30,038…039 - Build Order Number (int32)
 30,040 - Coolant In Temp in 1/10th Scale (int)
 30,041 - Coolant Out Temp in 1/10th Scale (int)
 30,042 - Oil Temp in 1/10th Scale (int)
 30,043 - Helium Temp in 1/10th Scale (int)
 30,044 - Low Pressure in 1/10th Scale (int)
 30,045 - Low Pressure Average in 1/10th Scale (int)
 30,046 - High Pressure in 1/10th Scale (int)
 30,047 - High Pressure Average in 1/10th Scale (int)
 30,048 - Delta Pressure Average in 1/10th Scale (int)
 30,049 - Motor Current in 1/10th Scale (int)
 30,050…051 - Hours Of Operation in 1/10th Scale (int32)
 30,052…053 - Warning State (int32)
 30,054…055 - Alarm State (int32)

 40,001 - Enable / Disable the compressor (int)
Effective Date: 2020/06/16 Page 19 of 25 IMC096

The ‘Input’ registers give the data in integer format but in 1/10 scale size.  For example, a
temperature of 65.8 will be multiplied by 10 then placed in the register.  This is an effort
to send fractional information in an easy to extract format.  Simply read the input registers
and converter the integer into a format that can handle decimal points then divide by 10.
The Holding register 40,001 is used to signal the compressor to turn on and off.
Note: All Modbus registers used in the previous generation of panel as well as SMDP are
still supported for backwards compatibility.
Developers	Note: When introducing Modbus to our compressors it was found that there
is a conflict as to how to refer to registers depending on who implemented it.  0 indexed
based or 1 indexed based.  This document refers to the registers by the literal number you
send when doing a query.  For example, to get input registers 30001 on a compressor with
the ID of 16 you will send the bytes:
  0x10, 0x04, 0x00, 0x01, 0x00, 0x01, 0x63, 0x4B
|     |     |     |     |   Checksum                    |     |
| --- | --- | --- | --- | ----------------------------- | --- |
|     |     |     |     |   How Many Registers to Read  |     |
|     |     |     |     |   Register Number             |     |
|     |     |     |     |   Input Register Get Command  |     |
|     |     |     |     |   Compressor ID               |     |

| 	   |     | 	   |     |     |     |
| --- | --- | --- | --- | --- | --- |

| Effective Date: 2020/06/16  |     |     | Page 20 of 25  |     | IMC096  |
| --------------------------- | --- | --- | -------------- | --- | ------- |

Values To Use
Holding register 40001:
0x00FF - turn the compressor OFF
0x0001-Turn the compressor ON
Input Register 30001: (operating state)
0: Idling - ready to start
2: Starting
3: Running
5: Stopping
6: Error Lockout
7: Error
8: Helium Cool Down
9: Power related Error
16: Recovered from Error
Input Register 30002: (Compressor Energized)
0: Off
1: On
Input Register 30029: (Pressure)
0:PSI
1: Bar
2: KPA
Input Register 30030: (Temperature)
0:Fahrenheit
1: Celsius
2: Kelvin
Effective Date: 2020/06/16 Page 21 of 25 IMC096

Input Register 30032: Model Numbers
  The upper 8 bits contain the Major model number and the lower 8 bits contain the
  Minor model number.
  Major Model Numbers consist of
|     | 1:   800 Series  |     |     |     |
| --- | ---------------- | --- | --- | --- |
|     | 2:   900 Series  |     |     |     |
|     | 3:  1000 Series  |     |     |     |
|     | 4:  1100 Series  |     |     |     |
|     | 5:  2800 Series  |     |     |     |
  Minor Model Numbers consist of:
|     | 1:  A1    |     | 13:  07  |     |
| --- | --------- | --- | -------- | --- |
|     | 2:  01    |     | 14:  H7  |     |
|     | 3:  02    |     | 15:  I7  |     |
|     | 4:  03    |     | 16:  08  |     |
|     | 5:  H3    |     | 17:  09  |     |
|     | 6:   I3   |     | 18:  9C  |     |
|     | 7:   04   |     | 19:  10  |     |
|     | 8:  H4    |     | 20:  1I  |     |
|     | 9:  05    |     | 21:  11  |     |
|     | 10:  H5   |     | 22:  12  |     |
|     | 11:  I6   |     | 23:  13  |     |
|     | 12:   06  |     | 24:  14  |     |
  Example:  A 289C compressor will give a Major of 5 and a Minor of 18.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |

| Effective Date: 2020/06/16  |     |     | Page 22 of 25  | IMC096  |
| --------------------------- | --- | --- | -------------- | ------- |

Input Register 30052 - 30053: (Warnings)
0: No warnings
1: Coolant IN running High
2: Coolant IN running Low
4: Coolant OUT running High
8: Coolant OUT running Low
16: Oil running High
32: Oil running Low
64: Helium running High
128: Helium running Low
256: Low Pressure running High
512: Low Pressure running Low
1024: High Pressure running High
2048: High Pressure running Low
4096: Delta Pressure running High
8192: Delta Pressure running Low
131072: Static Pressure running High
262144: Static Pressure running Low
524288: Cold head motor Stall
Effective Date: 2020/06/16 Page 23 of 25 IMC096

Input Register 30054 - 30055: (Errors)
0: No Errors
1: Coolant IN High
2: Coolant IN Low
4: Coolant OUT High
8: Coolant OUT Low
16: Oil High
32: Oil Low
64: Helium High
128: Helium Low
256: Low Pressure High
512: Low Pressure Low
1024: High Pressure High
2048: High Pressure Low
4096: Delta Pressure High
8192: Delta Pressure Low
16384: Motor Current Low
32768: Three Phase Error
65536: Power Supply Error
131072: Static Pressure High
262144: Static Pressure Low
Effective Date: 2020/06/16 Page 24 of 25 IMC096

15 Pin Remote Control
The 15-pin control port documentation is available on request.
RS‐232 Pinout (Comm 1)
1.
2. Rx.
3. Tx.
4.
5. Gnd.
6.
7.
8.
9.
RS‐485 Pinout (Comm 2)
1.
2. D+.
3. D‐
4.
5. Gnd.
6.
7.
8.
9.
Effective Date: 2020/06/16 Page 25 of 25 IMC096