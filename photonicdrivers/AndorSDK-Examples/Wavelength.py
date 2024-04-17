#!/usr/bin/env python
from pyAndorSpectrograph.spectrograph import ATSpectrograph

print("Wavelength Example")

print("Initializing Spectrograph")
spc = ATSpectrograph() #load the ATSpectrograph library

ret = spc.Initialize("")
print("Function Initialize returned {}".format(ret))

if ATSpectrograph.ATSPECTROGRAPH_SUCCESS==ret:

    (ret, devices) = spc.GetNumberDevices()
    print("Function GetNumberDevices returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
    print("\tNumber of devices: {}".format(devices))
    
    if devices > 0 :
        (ret, serial) = spc.GetSerialNumber(0, 64)
        print("Function GetSerialNumber returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
        print("\tSerial No: {}".format(serial))   
        
        (ret, present) = spc.IsWavelengthPresent(0)
        print("Function IsWavelengthPresent returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
        if present > 0 :
            print("\tWavelength drive IS present")
            
            (ret, grat) = spc.GetGrating(0)
            
            (ret, wave) = spc.GetWavelength(0)
            print("Function GetWavelength returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
            print("\tGrating {} wavelength (nm) : {}".format(grat, wave))     

            (ret, wavemin, wavemax) = spc.GetWavelengthLimits(0, grat)
            print("Function GetWavelengthLimits returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
            print("\tGrating {} min wavelength (nm): {} ".format(grat, wavemin))    
            print("\t\t  max wavelength (nm): {}".format(wavemax))     
            
            (ret, state) = spc.AtZeroOrder(0)
            print("Function AtZeroOrder returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
            if state > 0:
                print("\tGrating IS at zero order")
            else:
                print("\tGrating is NOT at zero order")
        else:
            print("\tWavelength drive is NOT present")
  
    ret = spc.Close()
    print("Function Close returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))

else:
  print("Cannot continue, could not initialise Spectrograph")
  
