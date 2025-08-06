from pyAndorSDK2 import atmcd, atmcd_errors

sdk = atmcd()  # Load the atmcd library
ret = sdk.Initialize("")  # Initialize camera
print("Function Initialize returned {}".format(ret))

if atmcd_errors.Error_Codes.DRV_SUCCESS == ret:
    HSSpeeds = []
    VSSpeeds = []
    amp_modes = []

    (ret, ADchannel) = sdk.GetNumberADChannels()
    print("Function GetNumberADChannels returned {} number of available channels {}".format(
        ret, ADchannel))
    for channel in range(0, ADchannel):
        (ret, speed) = sdk.GetNumberHSSpeeds(channel, 0)
        print("Function GetNumberHSSpeeds {} number of available speeds {}".format(
            ret, speed))
        for x in range(0, speed):
            (ret, speed) = sdk.GetHSSpeed(channel, 0, x)
            HSSpeeds.append(speed)

        print("Available HSSpeeds in MHz {} ".format(HSSpeeds))

        (ret, speed) = sdk.GetNumberVSSpeeds()
        print("Function GetNumberVSSpeeds {} number of available speeds {}".format(
            ret, speed))
        for x in range(0, speed):
            (ret, speed) = sdk.GetVSSpeed(x)
            VSSpeeds.append(speed)
        print("Available VSSpeeds in us {}".format(VSSpeeds))

        (ret, index, speed) = sdk.GetFastestRecommendedVSSpeed()
        print("Recommended VSSpeed {} index {}".format(speed, index))

        (ret, amps) = sdk.GetNumberAmp()
        print("Function GetNumberAmp returned {} number of amplifiers {}".format(ret, amps))
        for x in range(0, amps):
            (ret, name) = sdk.GetAmpDesc(x, 21)
            amp_modes.append(name)

        print("Available amplifier modes {}".format(amp_modes))

    # Clean up
    ret = sdk.ShutDown()
    print("Function ShutDown returned {}".format(ret))

else:
    print("Cannot continue, could not initialise camera {}".format(ret))
