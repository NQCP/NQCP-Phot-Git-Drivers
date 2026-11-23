Application note

|     |     |     |     |     |
| --- | --- | --- | --- | --- |

MBC-DG-LAB Protocol

MBC-DG-LAB uses an USB to RS232 converter  to communicate. Below, the list of commands:
Communication Channel:
RS232 link settings:
115200bps
1 stop bit
No parity
No data flow control
Set command:
Allows you to change parameters
Commands  Parameters  Possible values (#)  Step  Unit  Examples
| AC ####   | Auto Calibration         | QUAD/MIN/MAX     | NA  NA   | AC QUAD   |
| --------- | ------------------------ | ---------------- | -------- | --------- |
| RM ####   | Running mode             | AUTO or MAN      | NA  NA   | RM AUTO   |
| TL #####  | Transfer level           | -1000 to 1000    | 1  %*10  | TL –233   |
| DA ####   | Dither amplitude         | 1 to 1000        | 1  mV    | DA 110    |
| DF ####   | Dither frequency         | 400 to 1400      | 40  Hz   | DF 720    |
| PG #      | Photodiode gain          | 1 to 127         | 1        | PG 3      |
| PP ####   | Photodiode polarity      | INV or NOT       |          | PP INV    |
| BV #####  | BIAS value               | -10000 to 10000  | 1  mV    | BV +4521  |
| SR        | Scan Restart             | NA               | NA  NA   | SR        |
| SC        | send all MBC parameters  | NA               | NA  NA   | SC        |
SV #  Save MBC parameters to one of the  1/2/3  NA  NA  SV 1
config.
LD #  Load MBC parameters to one of the  1/2/3  NA   NA  LD 3
config.
Each command ends by a carriage return (carriage return ‘CR’ code ASCII 13)
If the command is valid, the system returns the sent value or « OK »
If an error happens, the system returns: « ERR »

Ce document et son contenu sont la propriété de Photline. Ils ne peuvent pas être reproduits, communiqués ou utilisés par des tiers
sans son autorisation écrite préalable. / This document, together with its contents, is the property of Photline. It must not be  Page 1/2
reproduced, communicated or disclosed to a third party without express written consent.

Application note

|     |     |     |     |
| --- | --- | --- | --- |

 GET commands:
Returns a parameter’s value
| Commands  | Parameters    | Possible returned values  | Units  |
| --------- | ------------- | ------------------------- | ------ |
|           | Running mode  | AUTO or MAN               | NA     |
RM?
| TL?  | Transfer level       | -1000 to 1000    | %   |
| ---- | -------------------- | ---------------- | --- |
| DA?  | Dither amplitude     | 1 to 1000        | mV  |
| DF?  | Dither frequency     | 400 to 1400      | Hz  |
| PG?  | Photodiode gain      | 1 to 127         | -   |
| PP?  | Photodiode polarity  | INV or NOT       |     |
| BV?  | BIAS value           | -10000 to 10000  | mV  |
| SN   | Card serial number   | 000001           |     |
| F    | Firmware version     |  V2.1            |     |

Each command ends by a carriage return (carriage return ‘CR’ code ASCII 13)
If the command is valid, the system returns the value of the corresponding parameter.
If an error happens, the system returns: « ERR »

Ce document et son contenu sont la propriété de Photline. Ils ne peuvent pas être reproduits, communiqués ou utilisés par des tiers
sans son autorisation écrite préalable. / This document, together with its contents, is the property of Photline. It must not be  Page 2/2
reproduced, communicated or disclosed to a third party without express written consent.