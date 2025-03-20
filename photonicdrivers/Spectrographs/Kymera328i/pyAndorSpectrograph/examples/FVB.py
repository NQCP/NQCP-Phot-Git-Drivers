#!/usr/bin/env python
from pyAndorSDK2 import atmcd, atmcd_codes, atmcd_errors
from pyAndorSpectrograph.spectrograph import ATSpectrograph

print("FVB Example")

print("Initializing Camera")
#Load libraries
cam = atmcd()
spc = ATSpectrograph()
codes = atmcd_codes

#Initialize libraries
shm = spc.Initialize("")
print("Function Initialize returned {}".format(
    spc.GetFunctionReturnDescription(shm, 64)[1]))

ret = cam.Initialize("")
print("Function Initialize returned {}".format(ret))

if atmcd_errors.Error_Codes.DRV_SUCCESS == ret:

    (ret, iSerialNumber) = cam.GetCameraSerialNumber()
    print("Function GetCameraSerialNumber returned {} Serial No: {}".format(
        ret, iSerialNumber))

    # configure the acquisition
    ret = cam.CoolerON()
    print("Function CoolerON returned {}".format(ret))

    ret = cam.SetAcquisitionMode(codes.Acquisition_Mode.SINGLE_SCAN)
    print("Function SetAcquisitionMode returned {} mode = Single Scan".format(ret))

    ret = cam.SetReadMode(codes.Read_Mode.FULL_VERTICAL_BINNING)
    print("Function SetReadMode returned {} mode = FVB".format(ret))

    ret = cam.SetTriggerMode(codes.Trigger_Mode.INTERNAL)
    print("Function SetTriggerMode returned {} mode = Internal".format(ret))

    (ret, xpixels, ypixels) = cam.GetDetector()
    print("Function GetDetector returned {} xpixels ={} ypixels = {}".format(
        ret, xpixels, ypixels))

    ret = cam.SetImage(1, 1, 1, xpixels, 1, ypixels)
    print("Function SetImage returned {} hbin = 1 vbin = 1 hstart = 1 hend = {} vstart = 1 vend = {}".format(
        ret, xpixels, ypixels))

    ret = cam.SetExposureTime(0.01)
    print("Function SetExposureTime returned {} time = 0.01s".format(ret))

    (ret, fminExposure, fAccumulate, fKinetic) = cam.GetAcquisitionTimings()
    print("Function GetAcquisitionTimings returned {} exposure = {} accumulate = {} kinetic = {}".format(
        ret, fminExposure, fAccumulate, fKinetic))

    ret = cam.PrepareAcquisition()
    print("Function PrepareAcquisition returned {}".format(ret))

    if ATSpectrograph.ATSPECTROGRAPH_SUCCESS == shm:
        (shm, serial) = spc.GetSerialNumber(0, 64)
        print("Function GetSerialNumber returned : {} Serial No: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], serial))

        (shm, present) = spc.IsAccessoryPresent(0)
        print("Function IsAccessoryPresent returned: {} present: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], present))

        (shm, present) = spc.IsSlitPresent(0, 1)
        print("Function IsSlitPresent returned: {} present: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], present))

        (shm, present) = spc.IsFilterPresent(0)
        print("Function IsFilterPresent returned: {} present: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], present))

        (shm, present) = spc.IsFlipperMirrorPresent(0, 1)
        print("Function IsFlipperMirrorPresent returned: {} present: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], present))

        (shm, present) = spc.IsFocusMirrorPresent(0)
        print("Function IsFocusMirrorPresent returned: {} present: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], present))

        (shm, present) = spc.IsGratingPresent(0)
        print("Function GratingIsPresent returned: {} present: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], present))

        (shm, present) = spc.IsIrisPresent(0, 1)
        print("Function IsIrisPresent returned: {} present: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], present))

        (shm, info) = spc.GetFilterInfo(0, 1, 64)
        print("Function GetFilterInfo returned: {} Info: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], info))

        (shm, info) = spc.IsShutterModePossible(0, 1)
        print("Function IsShutterModePossible returned: {} Info: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], info))

        (shm, present) = spc.IsShutterPresent(0)
        print("Function IsShutterPresent returned: {} present: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], present))

        (shm, present) = spc.IsSlitPresent(0, 3)
        print("Function IsSlitPresent returned: {} present: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], present))

        (shm, present) = spc.IsWavelengthPresent(0)
        print("Function IsWavelengthPresent returned: {} present: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], present))

        (shm, pos) = spc.GetFlipperMirrorMaxPosition(0, 1)
        print("Function GetFlipperMirrorMaxPosition returned: {} Pos: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], pos))

        shm = spc.SetGrating(0, 1)
        print("Function SetGrating returned {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1]))

        (shm, grat) = spc.GetGrating(0)
        print("Function GetGrating returned: {} Grat".format(grat))

        shm = spc.SetWavelength(0, 700)
        print("Function SetWavelength returned: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1]))

        (shm, wave) = spc.GetWavelength(0)
        print("Function GetWavelength returned: {} Wavelength: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], wave))

        (shm, min, max) = spc.GetWavelengthLimits(0, grat)
        print("Function GetWavelengthLimits returned: {} Wavelength Min: {} Wavelength Max: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1], min, max))

        # Perform Acquisition
        ret = cam.StartAcquisition()
        print("Function StartAcquisition returned {}".format(ret))

        ret = cam.WaitForAcquisition()
        print("Function WaitForAcquisition returned {}".format(ret))

        imageSize = xpixels
        (ret, arr, validfirst, validlast) = cam.GetImages16(1, 1, imageSize)
        print("Function GetImages16 returned {} first pixel = {} size = {}".format(
            ret, arr[0], imageSize))

        (ret, xsize, ysize) = cam.GetPixelSize()
        print("Function GetPixelSize returned {} xsize = {} ysize = {}".format(
            ret, xsize, ysize))

        shm = spc.SetNumberPixels(0, xpixels)
        print("Function SetNumberPixels returned: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1]))

        shm = spc.SetPixelWidth(0, xsize)
        print("Function SetPixelWidth returned: {}".format(
            spc.GetFunctionReturnDescription(shm, 64)[1]))

        (shm, calibrationValues) = spc.GetCalibration(0, xpixels)
        print("Function GetCalibration returned: {}, {}, {}, {},".format(
            spc.GetFunctionReturnDescription(shm, 64)[1],
            calibrationValues[0],
            calibrationValues[1],
            calibrationValues[2]))
            
    # Clean up
    ret = cam.ShutDown()
    print("Function Shutdown returned {}".format(ret))

    shm = spc.Close()
    print("Function Close returned {}".format(
        spc.GetFunctionReturnDescription(shm, 64)[1]))

else:
    print("Cannot continue, could not initialize camera")
