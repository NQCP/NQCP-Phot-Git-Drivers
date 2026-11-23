Picomotor Controller (8742 & 8743-CL)
Python Samples Code Documentation

The Python samples were developed with Python version 3.5.4.

The following packages were installed:
PythonNet 2.3.0 – This package allows Python code to call .NET methods.
NumPy 1.15.2 – This package allows the use of arrays in Python code.

USB Sample.py

This sample demonstrates how to use the .NET interface (UsbDllWrap.dll) of the Newport USB Driver to
communicate with any supported device via the USB port.  The Newport USB Driver software is installed when
the application software for a supported device is installed.   The default installation folder is

“C:\Program Files\Newport\Newport USB Driver”.

The DLLs can be found in the \Bin folder and the documentation can be found in the \Docs folder.
UsbDllWrap.dll must be copied to the same folder where the Python sample code is located.

OpenMultipleDevices_8742.py

This sample demonstrates how to use the Picomotor command library for mixed devices (CmdLib8742.dll)
and the device I/O library (DeviceIOLib.dll).  All the DLLs required for this sample are installed with the
New Focus Picomotor Application.

The following DLLs must be copied to the same folder where the Python sample code is located:
CmdLib8742.dll, DeviceIOLib.dll, UsbDllWrap.dll, NpEthernet.dll and
NpSerial.dll.

This sample will work for both the 8742 and 8743-CL Picomotor controllers.

© 2020 MKS Instruments, Inc.
All rights reserved

 1 of 1

