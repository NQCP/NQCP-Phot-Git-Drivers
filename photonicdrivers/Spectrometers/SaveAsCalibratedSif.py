#!/usr/bin/env python
import time
import os
from pyAndorSpectrograph.spectrograph import ATSpectrograph
from pyAndorSDK2 import atmcd, atmcd_codes, atmcd_errors

print("Show Image Example")

print("Initializing Camera")
#Load libraries
sdk = atmcd()
spc = ATSpectrograph()
codes = atmcd_codes

#Initialize libraries
shm = spc.Initialize("")
print("Function Initialize returned {}".format(
    spc.GetFunctionReturnDescription(shm, 64)[1]))

ret = sdk.Initialize("")
print("Function Initialize returned {}".format(ret))

if atmcd_errors.Error_Codes.DRV_SUCCESS == ret:
    
    if ATSpectrograph.ATSPECTROGRAPH_SUCCESS==shm:
    #Configure camera
        ret = sdk.SetTemperature(-60)
        print("Function SetTemperature returned {} target temperature -60".format(ret))

        ret = sdk.CoolerON()
        print("Function CoolerON returned {}".format(ret))
        
        while ret != atmcd_errors.Error_Codes.DRV_TEMP_STABILIZED:
            time.sleep(5)
            (ret, temperature) = sdk.GetTemperature()
            print("Function GetTemperature returned {} current temperature = {}".format(
            ret, temperature), end="\r")

        print("")
        print("Temperature stabilized")
        
        ret = sdk.SetReadMode(codes.Read_Mode.IMAGE)
        print("Function SetReadMode returned {}".format(ret))
        
        ret = sdk.SetTriggerMode(codes.Trigger_Mode.INTERNAL)
        print("Function SetTriggerMode returned {}".format(ret))
        
        ret = sdk.SetAcquisitionMode(codes.Acquisition_Mode.SINGLE_SCAN)
        print("Function SetAcquisitionMode returned {}".format(ret))
        
        (ret, xpixels, ypixels) = sdk.GetDetector()
        print("Function GetDetector returned {} xpixel = {} ypixel = {} ".format(ret, xpixels, ypixels))
        
        ret = sdk.SetImage(1, 1, 1, xpixels, 1, ypixels)
        print("Function SetImage returned {}".format(ret))
        
        ret = sdk.SetExposureTime(0.05)
        print("Function SetExposureTime returned {}".format(ret))
    
    #Configure Spectrograph
        shm = spc.SetGrating(0, 1)
        print("Function SetGrating returned {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1]))

        (shm, grat) = spc.GetGrating(0)
        print("Function GetGrating returned: {} Grat".format(grat))

        shm = spc.SetWavelength(0, 300)
        print("Function SetWavelength returned: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1]))

        (shm, wave) = spc.GetWavelength(0)
        print("Function GetWavelength returned: {} Wavelength: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], wave))

        (shm, min, max) = spc.GetWavelengthLimits(0, grat)
        print("Function GetWavelengthLimits returned: {} Wavelength Min: {} Wavelength Max: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], min, max))
        

    #Start Acquisition
        ret = sdk.StartAcquisition()
        print("Function StartAcquisition returned {}".format(ret))

        ret = sdk.WaitForAcquisition()
        print("Function WaitForAcquisition returned {}".format(ret))
        
        imageSize = xpixels * ypixels
        
        (ret, xsize, ysize) = sdk.GetPixelSize()
        print("Function GetPixelSize returned {} xsize = {} ysize = {}".format(
            ret, xsize, ysize))

        shm = spc.SetNumberPixels(0, xpixels)
        print("Function SetNumberPixels returned: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1]))

        shm = spc.SetPixelWidth(0, xsize)
        print("Function SetPixelWidth returned: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1]))
            
        (shm, c0, c1, c2, c3) = spc.GetPixelCalibrationCoefficients(0)
        coeff = [c0,c1,c2,c3]
        ret = sdk.SaveAsCalibratedSif((os.getcwd()+"\image.sif"), 2, 1, coeff, 532)
        print("Function SaveAsCalibratedSif returned {}".format(ret))    
    

    #Clean up
        ret = sdk.ShutDown()
        print("Function Shutdown returned {}".format(ret))
        ret = spc.Close()
        print("Function Close returned {}".format(spc.GetFunctionReturnDescription(ret, 64)[1]))
else:
  print("Cannot continue, could not initialise Spectrograph")
  