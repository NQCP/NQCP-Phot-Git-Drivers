#!/usr/bin/env python
from pyAndorSpectrograph.spectrograph import ATSpectrograph

print("Grating Example")

print("Initializing Spectrograph")
spc = ATSpectrograph() #Load the ATSpectrograph library

ret = spc.Initialize("")
print("Function Initialize returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))

if ATSpectrograph.ATSPECTROGRAPH_SUCCESS==ret:

    (ret, devices) = spc.GetNumberDevices()
    print("Function GetNumberDevices returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
    print("\tNumber of devices: {}".format(devices))
    
    if devices > 0 :
        (ret, serial) = spc.GetSerialNumber(0, 64)
        print("Function GetSerialNumber returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
        print("\tSerial No: {}".format(serial)) 
        
        (ret, present) = spc.IsGratingPresent(0)
        print("Function IsGratingPresent returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
        if present > 0 :
            print("\tTurret IS present")
            
            (ret, turret) = spc.GetTurret(0)
            print("Function GetTurret returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
            print("\tTurret: {}".format(turret))     

            (ret, gratings) = spc.GetNumberGratings(0)
            print("Function GetNumberGratings returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
            print("\tNumber of gratings: {}".format(gratings))     

            (ret, grat) = spc.GetGrating(0)
            print("Function GetGrating returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
            print("\tGrating no: {}".format(grat))  
            
            (ret, lines, blaze, home, offset) = spc.GetGratingInfo(0, grat, 64)
            print("Function GetGratingInfo returned {} ".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
            print("\tGrating no {}".format(grat))
            print("\tLines/mm: {}".format(lines))           
            print("\tBlaze: {}".format(blaze))
            print("\tHome: {}".format(home))
            print("\tOffset: {}".format(offset))
            
            (ret, offset) = spc.GetDetectorOffset(0, 0, 0)
            print("Function GetDetectorOffset returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
            print("\tOffset {}".format(offset))
        else:
            print("\tTurret is NOT present")            
    #Clean up
    ret = spc.Close()
    print("Function Close returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))

else:
  print("Cannot continue, could not initialize Spectrograph")
  
