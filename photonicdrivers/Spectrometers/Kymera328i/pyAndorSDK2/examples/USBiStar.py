from pyAndorSDK2 import atmcd, atmcd_codes, atmcd_errors

sdk = atmcd()  # Load the atmcd library
codes = atmcd_codes

ret = sdk.Initialize("")  # Initialize camera
print("Function Initialize returned {}".format(ret))

if atmcd_errors.Error_Codes.DRV_SUCCESS == ret:

    (ret, iSerialNumber) = sdk.GetCameraSerialNumber()
    print("Function GetCameraSerialNumber returned {} Serial No {}".format(
        ret, iSerialNumber))

    # Configure the acquisition
    ret = sdk.SetAcquisitionMode(codes.Acquisition_Mode.SINGLE_SCAN)
    print("Function SetAcquisitionMode returned {} mode = Single Scan".format(ret))

    ret = sdk.SetReadMode(codes.Read_Mode.IMAGE)
    print("Function SetReadMode returned {} mode = FVB".format(ret))

    ret = sdk.SetTriggerMode(codes.Trigger_Mode.INTERNAL)
    print("Function SetTriggerMode returned {} mode = Internal".format(ret))

    (ret, xpixels, ypixels) = sdk.GetDetector()
    print("Function GetDetector returned {} xpixels = {} ypixels = {}".format(
        ret, xpixels, ypixels))

    ret = sdk.SetExposureTime(0.01)
    print("Function SetExposureTime returned {} time = 0.01s".format(ret))

    ret = sdk.SetGateMode(codes.Gate_Mode.GATE_USING_DDG)
    print("Function SetGateMode returned {} mode = Gate using DDG".format(ret))

    ret = sdk.SetDDGGateTime(0, 1000000000)
    print("Function SetDDGGateTime returned {} gate width = 1 ms".format(ret))

    ret = sdk.SetDDGExternalOutputEnabled(0, 1)
    print("Function SetDDGExternalOutputEnabled returned {} Output A enabled".format(ret))

    ret = sdk.SetDDGExternalOutputTime(0, 1000000000, 2000000000)
    print("Function SetDDGExternalOutputTime returned {} output delay = 1 ms, width = 2ms".format(ret))

    ret = sdk.SetDDGInsertionDelay(1)
    print("Function SetDDGInsertionDelay returned {} mode = Fast".format(ret))

    ret = sdk.SetDDGIntelligate(1)
    print("Function SetDDGIntelligate returned {} mode = MCP gating ON".format(ret))

    ret = sdk.SetMCPGain(10)
    print("Function SetMCPGain returned {} gain = 10".format(ret))

    (ret, fminExposure, fAccumulate, fKinetic) = sdk.GetAcquisitionTimings()
    print("Function GetAcquisitionTimings returned {} exposure = {} accumulate = {} kinetic = {}".format(
        ret, fminExposure, fAccumulate, fKinetic))

    ret = sdk.PrepareAcquisition()
    print("Function PrepareAcquisition returned {}".format(ret))

    # Perform Acquisition
    ret = sdk.StartAcquisition()
    print("Function StartAcquisition returned {}".format(ret))

    ret = sdk.WaitForAcquisition()
    print("Function WaitForAcquisition returned {}".format(ret))

    imageSize = xpixels
    (ret, arr, validfirst, validlast) = sdk.GetImages16(1, 1, imageSize)
    print("Function GetImages16 returned {} first pixel = {} size = {}".format(
        ret, arr[0], imageSize))

    (ret, status) = sdk.GetPhosphorStatus()
    print("Function GetPhosphorStatus returned {} status = {}".format(ret, status))

    # Clean up
    ret = sdk.ShutDown()
    print("Function Shutdown returned {}".format(ret))

else:
    print("Cannot continue, could not initialize camera")
