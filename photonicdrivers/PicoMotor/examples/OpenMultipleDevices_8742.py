import sys
import os
import inspect
# Import the .NET Common Language Runtime (CLR) to allow interaction with .NET
import clr
import numpy as np

print ("Python %s\n\n" % (sys.version,))

strCurrFile = os.path.abspath (inspect.stack()[0][1])
print ("Executing File = %s\n" % strCurrFile)

# Initialize the DLL folder path to where the DLLs are located
strPathDllFolder = os.path.dirname (strCurrFile)
print ("Executing Dir  = %s\n" % strPathDllFolder)

# Add the DLL folder path to the system search path (before adding references)
sys.path.append (strPathDllFolder)

# Add a reference to each .NET assembly required
clr.AddReference ("DeviceIOLib")
clr.AddReference ("CmdLib8742")

# Import a class from a namespace
from Newport.DeviceIOLib import *
from NewFocus.PicomotorApp import CmdLib8742
from System.Text import StringBuilder

print ("Waiting for device discovery...")
# Call the class constructor to create an object
deviceIO = DeviceIOLib (True)
cmdLib8742 = CmdLib8742 (deviceIO)

# Set up USB to only discover picomotors
deviceIO.SetUSBProductID (0x4000);

# Discover USB and Ethernet devices - delay 5 seconds
deviceIO.DiscoverDevices (5, 5000)

# Get the list of discovered devices
strDeviceKeys = np.array ([])
strDeviceKeys = deviceIO.GetDeviceKeys ()
nDeviceCount = deviceIO.GetDeviceCount ()
print ("Device Count = %d\n" % nDeviceCount)

if (nDeviceCount > 0) :
    strBldr = StringBuilder (64)
    n = 0

    # For each device key in the list
    for oDeviceKey in strDeviceKeys :
        strDeviceKey = str (oDeviceKey)
        n = n + 1
        print ("Device Key[%d] = %s" % (n, strDeviceKey))
        
        # If the device was opened
        if (deviceIO.Open (strDeviceKey)) :

            strModel = ""
            strSerialNum = ""
            strFwVersion = ""
            strFwDate = ""
            nReturn = -1

            nReturn, strModel, strSerialNum, strFwVersion, strFwDate = cmdLib8742.IdentifyInstrument (strDeviceKey, strModel, strSerialNum, strFwVersion, strFwDate)
            print ("Return Value = %s" % nReturn)
            print ("Model = %s" % strModel)
            print ("Serial Num = %s" % strSerialNum)
            print ("Fw Version = %s" % strFwVersion)
            print ("Fw Date = %s\n" % strFwDate)

            strCmd = "*IDN?"
            strBldr.Remove (0, strBldr.Length)
            nReturn = deviceIO.Query (strDeviceKey, strCmd, strBldr)
            print ("Return Status = %d" % nReturn)
            print ("*IDN Response = %s\n\n" % strBldr.ToString ())

            #Close the device
            nReturn = deviceIO.Close (strDeviceKey)
else :
    print ("No devices discovered.\n")

# Shut down all communication
cmdLib8742.Shutdown ()
deviceIO.Shutdown ()
