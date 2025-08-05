from pyAndorSDK2 import atmcd, atmcd_codes, atmcd_errors, CameraCapabilities

sdk = atmcd()  # Load the atmcd library
codes = atmcd_codes

ret = sdk.Initialize("")  # Initialize camera
helper = CameraCapabilities.CapabilityHelper(sdk)
print("Function Initialize returned {}".format(ret))

if atmcd_errors.Error_Codes.DRV_SUCCESS == ret:

    (ret, iSerialNumber) = sdk.GetCameraSerialNumber()
    print("Function GetCameraSerialNumber returned {} Serial No: {}".format(
        ret, iSerialNumber))
    helper.print_acquisition_modes()

    helper.print_get_functions()

    helper.print_read_modes()

    helper.print_FTRead_modes()

    # Clean up
    ret = sdk.ShutDown()
    print("Function Shutdown returned {}".format(ret))

else:
    print("Cannot continue, could not initialise camera")
