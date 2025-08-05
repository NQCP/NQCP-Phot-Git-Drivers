import time
import numpy as np
import matplotlib.pyplot as plt
from pyAndorSDK2 import atmcd, atmcd_codes, atmcd_errors

sdk = atmcd()  # Load the atmcd library
codes = atmcd_codes
ret = sdk.Initialize("")  # Initialize camera
print("Function Initialize returned {}".format(ret))

if atmcd_errors.Error_Codes.DRV_SUCCESS == ret:
    # Configure the acquisition
    ret = sdk.SetTemperature(-60)
    print("Function SetTemperature returned {} target temperature -60".format(ret))

    ret = sdk.CoolerON()
    print("Function CoolerOn returned {}".format(ret))

    while ret != atmcd_errors.Error_Codes.DRV_TEMP_STABILIZED:
        time.sleep(5)
        (ret, temperature) = sdk.GetTemperature()
        print("Function GetTemperature returned {} current temperature = {}".format(
            ret, temperature), end="\r")

    print("")
    print("Temperature stabilized")

    ret = sdk.SetAcquisitionMode(codes.Acquisition_Mode.RUN_TILL_ABORT)
    print("Function SetAcquisitionMode returned {} mode = Run Till Abort".format(ret))

    ret = sdk.SetReadMode(codes.Read_Mode.IMAGE)
    print("Function SetReadMode returned {} mode = Image".format(ret))

    ret = sdk.SetTriggerMode(codes.Trigger_Mode.INTERNAL)
    print("Function SetTriggerMode returned {} mode = Internal".format(ret))

    (ret, xpixels, ypixels) = sdk.GetDetector()
    print("Function GetDetector returned {} xpixels = {} ypixels = {}".format(
        ret, xpixels, ypixels))

    ret = sdk.SetImage(1, 1, 1, xpixels, 1, ypixels)
    print("Function SetImage returned {} hbin = 1 vbin = 1 hstart = 1 hend = {} vstart = 1 vend = {}".format(
        ret, xpixels, ypixels))

    ret = sdk.SetExposureTime(0.2)
    print("Function SetExposureTime returned {} time = 0.2s".format(ret))

    # Perform Acquisition
    ret = sdk.StartAcquisition()
    print("Function StartAcquisition returned {}".format(ret))

    imageSize = xpixels * ypixels
    fig, imgwindow = plt.subplots()

    while True:
        # Get most recent image, format array to be be displayed as image then add image to window instance
        try:
            if plt.fignum_exists(fig.number):
                imgwindow.cla()
                (ret, index) = sdk.GetTotalNumberImagesAcquired()
                (ret, arr) = sdk.GetMostRecentImage16(imageSize)
                print("Function GetMostRecentImage16 returned {} first pixel = {} size = {}".format(
                    ret, arr[0], imageSize), end="\r")
                arr = np.reshape(arr, (xpixels, ypixels))
                imgwindow.matshow(arr)
                imgwindow.set_title("Image number: {}".format(index))
                plt.pause(0.1)
            else:
                raise Exception(
                    "can't invoke " '"update"' " command: application has been destroyed")

        except Exception as e:
            # In event of error display error message and break out of loop
            plt.close()
            print("")
            print(e)
            break

    # Clean up
    print("")
    ret = sdk.ShutDown()
    print("Function Shutdown returned {}".format(ret))

else:
    print("Cannot continue, could not initialise camera {}".format(ret))
