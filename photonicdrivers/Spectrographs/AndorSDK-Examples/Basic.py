#!/usr/bin/env python
from pyAndorSpectrograph.spectrograph import ATSpectrograph

print("Basic Example")

print("Initialising Spectrograph")
spc = ATSpectrograph() #Load the ATSpectrograph library

shm = spc.Initialize("")
print("Function Initialize returned {}".format(spc.GetFunctionReturnDescription(shm, 64)[1]))

if ATSpectrograph.ATSPECTROGRAPH_SUCCESS==shm:

    (ret, devices) = spc.GetNumberDevices()
    print("Function GetNumberDevices returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
    print("\tNumber of devices: {}".format(devices))
    
    for index in range(devices):
        (ret, serial) = spc.GetSerialNumber(index, 64)
        print("Function GetSerialNumber returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
        print("\tSerial No: {}".format(serial))
        
        (ret, FocalLength, AngularDeviation, FocalTilt) = spc.EepromGetOpticalParams(index)
        print("Function EepromGetOpticalParams {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
        print("\tFocal Length: {}".format(FocalLength))         
        print("\tAngular Deviation: {}".format(AngularDeviation))
        print("\tFocal Tilt: {}".format(FocalTilt))
  
    ret = spc.Close()
    print("Function Close returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))

else:
  print("Cannot continue, could not initialise Spectrograph")
  
