HighFinesse Tutorial
Control the wavemeter with your
own application via the net work
September 14, 2022

Overview Further information
This tutorial shows you how to …
… control the wavemeter with your own
application via the network.
This guide is intended to give you a short introduction on how to control
a HighFinesse non-standalone wavemeter or laser spectrum analyzer.
It is discussed how to use the LongTerm application and Python example
that can be used as a starting point for your own application controlling
HighFinesse User Manual
the wavemeter via the network. WLM Network Solution

Network Switch
1 2
Ethernet
External Software Wavemeter Meter Software
USB
Client-PC Server-PC
Connect the wavemete to a computer in the network.
Make sure the proper version of Visual C++ Redistributable for Visual Studio
Download the HighFinesse NetAccess
for your operating system is installed. You can download it here:
Accesories from the link below
https://support.microsoft.com/en-us/help/2977003/
https://
the-latest-supported-visual-c-downloads
www.highfinesse-downloads.com/
Then please run the vc_redist.x64.exe (vc_redist.x86.exe for 32 bit) download/
on both the Server and Client PC. edcsc5ypvsua

| 3   | 4   | 5   |
| --- | --- | --- |
Open …
ZIP  HighFinesse NetAccess Accessories.zip  HighFinesse NetAccess Accessories
Type: ZIP archive Type: Folder
Find the ZIP archive
HighFinesse Extract the ZIP archive Open the extracted folder
| NetAccess Accessories | HighFinesse | HighFinesse |
| --------------------- | ----------- | ----------- |
on the USB stick. NetAccess Accessories. NetAccess Accessories.

| 6   | 7   | 8   |
| --- | --- | --- |
Copy …
Copy …
Open …
Example LongTerm
Type: Folder
| Copy the folder wlmData Server | Copy the folder |     |
| ------------------------------ | --------------- | --- |
to your Server-PC and start the Example Longterm Open the folder
| wlmDataServer.exe. | to your client-PC. | Example LongTerm … |
| ------------------ | ------------------ | ------------------ |

| 9   | 10  | 11  |
| --- | --- | --- |
Open … with texteditor
Replace the factory set IP address
by the address of the server-PC.
This information is available by
… and open the file wlmData.ini Find the factory set IP address running ipnconfig/all in the command
| with an texteditor. | in this file. | prompt. |
| ------------------- | ------------- | ------- |

12 13
Open …
For a more detailed description
of the application see:
Save … and close
HighFinesse Tutorial
Introduction LongTerm.pdf
Start the LongTerm.exe.
This program allows you to log
the wavelength and additional The following pages will show
measurement data. you how to …
Save the file wlmData.ini It also allows you to … collect the wavelength data
… and close this file. save the data as an ASCII file. using the Callback procedure.

| 14  | 15  | 16  |
| --- | --- | --- |
Open …
Close …
Example Python
Type: Folder
DataDemo_Callback network dll
Type: Folder
Now browse to the folder
|     | Example Python/               | Add the correct IP address to     |
| --- | ----------------------------- | --------------------------------- |
|     | DataDemo_Callback network dll | the wlmData.ini just as described |
Close the LongTerm application. and copy it to your client-PC. in step .
  9

17 18
Open …
This script shows you how to
efficiently collect the wavelength
data using the Callback procedure.
This is a good starting point for
your own application in Python.
Follow the instruction in the
External Access Guide.pdf to
write your own code.
If you would like to have a
deeper understanding on the
HighFinesse NetAccess solution
If you using a 32-Python Version
please take a look in the …
replace the wlmData.dll by the Open DataDemo_Callback.py
32-bit version that is located in the with a suitabel program (for example … HighFinesse NetAccess
subfolder Windows 32 bit dll Spyder). userguide and manual.

HighFinesse GmbH T + 49 (0) 7071 - 53 918 0 Additional information
Wöhrdstraße 4 F + 49 (0) 7071 - 53 918 99 and distributors:
72072 Tübingen, Germany M info@highfinesse.com www.highfinesse.com
© HighFinesse GmbH 2022 · Contact: service@highfinesse.de