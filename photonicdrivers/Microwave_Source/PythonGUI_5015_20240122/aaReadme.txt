The files in this directory demonstrate a Python/Tk GUI interface for the Valon 5015 synthesizer.

Program Notes
=============
Panels for CW Mode and Sweep Mode are fully implemented.

The Mode Panel changes the synthesizer Mode (CW or Sweep) and displays the corresponding software panel.
The "Main" and "Sweep" buttons on the top menu are used to display a different panel, without changing modes.

The File Menu includes 
    "Load Config" to read synthesizer values from disk.
    "Save Config" write the synthesizer's state to a disk file.

The Synthesizer Menu includes 
    "Read Registers"    Read values from the synthesizer into the Configuration Manager.
    "Write Registers"   Write values from the Configuration Manager to the synthesizer.
                        DOES NOT WORK in V5015CM version 1.0.
                        Fixed in version 1.1.
    "Reset"             Resstores the synthesizer to the factory presets.
    "Save to Flash"     Saves all synthesizer setting to non-volatile flash memory.
    "Recall from Flash" Restores synthesizer settings from flash memory.
    "Cleanse"           Removes all user-related information from the synthesizer.
    
List Mode support is added in version 2.0.

Telnet connection is not implemented.

Installation Notes
==================

V5015CM.py contains the program's 'main' entry point.  
At a shell (or cmd) prompt, type 

	python V5015cm.py

Or load this file into Idle, and press F5 to start execution.

Or on a Linux machine you can "chmod +x V5015CM.py"
    and treat is as an executable binary.

To run this program, you must use a version Python2.7.  Not Python3.
Your version of Python will need to include PySerial, including its 'tools' directory.

If you see a message "ImportError: No module named serial" then you need to install PySerial.
Get a shell prompt and type

	sudo pip install pyserial

Make sure that is is python2.7 that is getting updated.  If python3.x is the default on your machine, then try pip2 instead of pip.

If you see a message about a missing tools directory, get a shell prompt, and type:

	sudo pip install --upgrade pyserial

If pip isn't installed (on a Linux machine), type

	sudo apt-get install python-pip

and then repeat the pip command above.

V5015cm was tested with python2.7,
on a PC running Windows 7 and Windows 11
and on a laptop running Linux Mint 18,
and on a Raspberry Pi B+ running Raspbian.

To use Python3, at a minimum, you would need to modify the serial port module to convert back and forth between unicode and 8-bit characters.  I don't know what else.  Python3 also contains some incompatible changes in the Tkinter module.

You are free to use and modify these files, and share them.

There is some error handling code, but my feelings won't be hurt if you want to add more.

Peter McKone
