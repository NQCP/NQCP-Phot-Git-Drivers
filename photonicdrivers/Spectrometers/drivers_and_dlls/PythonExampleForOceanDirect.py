# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:58:47 2020

@author: Ocean Insight Inc.
"""

from oceandirect.OceanDirectAPI import OceanDirectAPI, OceanDirectError, FeatureID

def printBinary(value):
    bitCount = 32 #32 bits
    numValue = int(value)

    print("bits (%d) = " % numValue, end='')
    for i in range(32, -1, -1):
        print("%d " % ((numValue >> i) & 0x01), end='')

    print(" ")

def acquisitionDelay(device):
    #device.set_acquisition_delay(120)
    #print("acquisitionDelay(device): set acqDelay 120")

    acqDelay    = device.get_acquisition_delay()
    acqDelayInc = device.get_acquisition_delay_increment()
    acqDelayMin = device.get_acquisition_delay_minimum()
    acqDelayMax = device.get_acquisition_delay_maximum()

    print("acquisitionDelay(device): acqDelay     =  %d " % acqDelay)
    print("acquisitionDelay(device): acqDelayInc  =  %d " % acqDelayInc)
    print("acquisitionDelay(device): acqDelayMin  =  %d " % acqDelayMin)
    print("acquisitionDelay(device): acqDelayMax  =  %d " % acqDelayMax)
    print("")

    #400us
    value = 400
    device.set_acquisition_delay(value)
    print("acquisitionDelay(device): set acqDelay =  %d " % value)

    acqDelay = device.get_acquisition_delay()
    print("acquisitionDelay(device): get acqDelay(expected 400)  =  %d " % acqDelay)
    print("")


def gpio(device):
    supported = device.is_feature_id_enabled(FeatureID.GPIO)
    print("gpio(device): GPIO feature supported  = %s" % supported)

    if not supported:
        print("")
        return

    tempCount = device.Advanced.get_gpio_pin_count()
    print("gpio(device): pin count          =  %d " % tempCount)

    try:
        outputVector = device.Advanced.gpio_get_output_enable2()
        printBinary(outputVector)
        print("---------------------------------------------------------------\n\n")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("gpio(device): exception / %d = %s" % (errorCode, errorMsg))

    try:
        device.Advanced.gpio_set_output_enable1(0, 1)
        bitOutput1 = device.Advanced.gpio_get_output_enable1(0)
        print("gpio(device): set output vector bits / mask     =  00000000 / 0(True)")
        print("gpio(device): get bit(0) output                 =  0(%s)" % bitOutput1)
        outputVector = device.Advanced.gpio_get_output_enable2()
        print("gpio(device): get output vector expected output =  00000001")
        printBinary(outputVector)
        print("\n")

        device.Advanced.gpio_set_output_enable1(2, 1)
        device.Advanced.gpio_set_output_enable1(3, 1)
        bitOutput1 = device.Advanced.gpio_get_output_enable1(2)
        bitOutput2 = device.Advanced.gpio_get_output_enable1(3)
        print("gpio(device): set output vector bits / mask     =  00000001 / 2(True),3(True)")
        print("gpio(device): get bit(2,3) output               =  2(%s) / 3(%s)" % (bitOutput1, bitOutput2) )
        outputVector = device.Advanced.gpio_get_output_enable2()
        print("gpio(device): get output vector expected output =  00001101")
        printBinary(outputVector)
        print("\n")

        device.Advanced.gpio_set_output_enable1(0, 0)
        device.Advanced.gpio_set_output_enable1(1, 1)
        device.Advanced.gpio_set_output_enable1(3, 0)
        bitOutput1 = device.Advanced.gpio_get_output_enable1(0)
        bitOutput2 = device.Advanced.gpio_get_output_enable1(1)
        bitOutput3 = device.Advanced.gpio_get_output_enable1(3)
        print("gpio(device): set output vector bits / mask     =  00001101 / 0(False),True(1),3(False)")
        print("gpio(device): get bit(0,1,3) output             =  0(%s) / 1(%s) / 3(%s)" % (bitOutput1, bitOutput2, bitOutput3))
        outputVector = device.Advanced.gpio_get_output_enable2()
        print("gpio(device): get output vector expected output =  00000110")
        printBinary(outputVector)
        print("\n")

        device.Advanced.gpio_set_output_enable1(0, 1)
        device.Advanced.gpio_set_output_enable1(3, 1)
        bitOutput1 = device.Advanced.gpio_get_output_enable1(0)
        bitOutput2 = device.Advanced.gpio_get_output_enable1(3)
        print("gpio(device): set output vector bits / mask     =  00000110 / 0(True),3(True)")
        print("gpio(device): get bit(0,3) output               =  0(%s) / 3(%s)" % (bitOutput1, bitOutput2))
        outputVector = device.Advanced.gpio_get_output_enable2()
        print("gpio(device): get output vector expected output =  00001111")
        printBinary(outputVector)
        print("")
        print("---------------------------------------------------------------\n\n")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("gpio(device): gpio_output_bits() / %d = %s" % (errorCode, errorMsg))

    try:
        device.Advanced.gpio_set_value1(0, 1)
        device.Advanced.gpio_set_value1(1, 1)
        value1 = device.Advanced.gpio_get_value1(0)
        value2 = device.Advanced.gpio_get_value1(1)
        print("gpio(device): set value vector values / mask   =  00000000 / 0(True), 1(True)")
        print("gpio(device): get bit(0,1) value               =  0(%s) / 1(%s)" % (value1, value2))
        valueVector = device.Advanced.gpio_get_value2()
        print("gpio(device): get value vector expected values =  00000011")
        printBinary(valueVector)
        print("")

        device.Advanced.gpio_set_value1(2, 1);
        device.Advanced.gpio_set_value1(3, 1);
        value1 = device.Advanced.gpio_get_value1(2)
        value2 = device.Advanced.gpio_get_value1(3)
        print("gpio(device): set value vector values / mask   =  00000011 / 2(True),3(True)")
        print("gpio(device): get bit(2,3) value               =  2(%s) / 3(%s)" % (value1, value2))
        valueVector = device.Advanced.gpio_get_value2()
        print("gpio(device): get value vector expected values =  00001111")
        printBinary(valueVector)
        print("")

        device.Advanced.gpio_set_value1(0, 0)
        device.Advanced.gpio_set_value1(2, 0)
        value1 = device.Advanced.gpio_get_value1(0)
        value2 = device.Advanced.gpio_get_value1(2)
        print("gpio(device): set value vector values / mask   =  00001111 / 0(False), 2(False)")
        print("gpio(device): get bit(0,2) value               =  0(%s) / 2(%s)" % (value1, value2))
        valueVector = device.Advanced.gpio_get_value2()
        print("gpio(device): get value vector expected values =  00001010")
        printBinary(valueVector)
        print("")

        device.Advanced.gpio_set_value1(1, 0)
        device.Advanced.gpio_set_value1(3, 0)
        value1 = device.Advanced.gpio_get_value1(1)
        value2 = device.Advanced.gpio_get_value1(3)
        print("gpio(device): set value vector values / mask   =  00001010 / 1(False), 3(False)")
        print("gpio(device): get bit(1,3) value               =  1(%s) / 3(%s)" % (value1, value2))
        valueVector = device.Advanced.gpio_get_value2()
        print("gpio(device): get value vector expected values =  00000000")
        printBinary(valueVector)
        print("\n")

    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("gpio(device): exception / %d = %s" % (errorCode, errorMsg))

    #Output bit masks
    try:
        #15 = 1111
        device.Advanced.gpio_set_output_enable2(15)
        print("gpio(device): set output mask(15)        =  00001111")

        mask = device.Advanced.gpio_get_output_enable2()
        print("gpio(device): expecting output mask (15) =  %d" % mask)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("gpio(device): exception / %d = %s" % (errorCode, errorMsg))

    #Value bit masks
    try:
        #12 = 1100
        device.Advanced.gpio_set_value2(12)
        print("")
        print("gpio(device): set value mask(12)        =  00001100")

        mask = device.Advanced.gpio_get_value2()
        print("gpio(device): expecting value mask (12) =  %d" % mask)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("gpio(device): exception / %d = %s" % (errorCode, errorMsg))
    print("")

def singleStrobe(device):
    values = [False, True]
    for enable in values:
        device.Advanced.set_single_strobe_enable(enable);
        print("singleStrobe(device): set enable      =  %s " % enable)

        enable2 = device.Advanced.get_single_strobe_enable();
        print("singleStrobe(device): get enable      =  %s " % enable2)
        print("")

    device.Advanced.set_single_strobe_enable(True);
    enable = device.Advanced.get_single_strobe_enable()
    print("singleStrobe(device): enable(True)    =  %s " % enable)


    strobeWidth = 552
    device.Advanced.set_single_strobe_width(strobeWidth)
    print("singleStrobe(device): set strobeWidth =  %d " % strobeWidth)
    strobeWidth = device.Advanced.get_single_strobe_width()
    print("singleStrobe(device): get strobeWidth =  %d " % strobeWidth)
    print("")

    strobeDelay = 322
    device.Advanced.set_single_strobe_delay(strobeDelay)
    print("singleStrobe(device): set strobeDelay =  %d " % strobeDelay)
    strobeDelay = device.Advanced.get_single_strobe_delay()
    print("singleStrobe(device): get strobeDelay =  %d " % strobeDelay)
    print("")

    enable2 = device.Advanced.get_single_strobe_enable();
    print("singleStrobe(device): get enable      =  %s " % enable2)
    print("")

    try:
        delayMin = device.Advanced.get_single_strobe_delay_minimum()
        print("singleStrobe(device): delayMin         =  %d " % delayMin)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("singleStrobe(device): get_single_strobe_delay_minimum() %d = %s" % (errorCode, errorMsg))

    try:
        delayMax = device.Advanced.get_single_strobe_delay_maximum()
        print("singleStrobe(device): delayMax         =  %d " % delayMax)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("singleStrobe(device): get_single_strobe_delay_maximum() %d = %s" % (errorCode, errorMsg))

    try:
        delayInc = device.Advanced.get_single_strobe_delay_increment()
        print("singleStrobe(device): delayInc         =  %d " % delayInc)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("singleStrobe(device): get_single_strobe_delay_increment() %d = %s" % (errorCode, errorMsg))

    try:
        widthMin = device.Advanced.get_single_strobe_width_minimum()
        print("singleStrobe(device): widthMin         =  %d " % widthMin)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("singleStrobe(device): get_single_strobe_width_minimum() %d = %s" % (errorCode, errorMsg))

    try:
        widthMax = device.Advanced.get_single_strobe_width_maximum()
        print("singleStrobe(device): widthMax         =  %d " % widthMax)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("singleStrobe(device): get_single_strobe_width_maximum() %d = %s" % (errorCode, errorMsg))

    try:
        widthInc = device.Advanced.get_single_strobe_width_increment()
        print("singleStrobe(device): widthInc         =  %d " % widthInc)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("singleStrobe(device): get_single_strobe_width_increment() %d = %s" % (errorCode, errorMsg))

    try:
        cycleMax = device.Advanced.get_single_strobe_cycle_maximum()
        print("singleStrobe(device): cycleMax         =  %d " % cycleMax)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("singleStrobe(device): get_single_strobe_cycle_maximum() %d = %s" % (errorCode, errorMsg))
    print("")

def continuousStrobe(device):
    periodInc = 0
    try:
        periodInc = device.Advanced.get_continuous_strobe_period_increment()
        print("continuousStrobe(device): period increment =  %d " % periodInc)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("continuousStrobe(device): get_continuous_strobe_period_increment() %d = %s" % (errorCode, errorMsg))

    strobePeriod = device.Advanced.get_continuous_strobe_period()
    print("continuousStrobe(device): get strobePeriod =  %d " % strobePeriod)

    strobeEnable = device.Advanced.get_continuous_strobe_enable()
    print("continuousStrobe(device): get strobeEnable =  %s " % strobeEnable)

    values = [False, True]
    for enable in values:
        device.Advanced.set_continuous_strobe_enable(False)
        print("continuousStrobe(device): get strobeEnable =  %s " % enable)
        strobeEnable = device.Advanced.get_continuous_strobe_enable()
        print("continuousStrobe(device): set strobeEnable =  %s " % enable)
        print("")

    try:
        periodMin = device.Advanced.get_continuous_strobe_period_minimum()
        print("continuousStrobe(device): periodMin          =  %d " % periodMin)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("continuousStrobe(device): get_continuous_strobe_period_minimum() %d = %s" % (errorCode, errorMsg))

    try:
        periodMax = device.Advanced.get_continuous_strobe_period_maximum()
        print("continuousStrobe(device): periodMax          =  %d " % periodMax)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("continuousStrobe(device): get_continuous_strobe_period_maximum() %d = %s" % (errorCode, errorMsg))



    strobePeriodList = [1200, 1505, 800, 453]
    for period in strobePeriodList:
        if (periodInc > 1) and ((period % periodInc) != 0):
            print("continuousStrobe(device): set strobePeriod =  %d  ====> ********* expecting EXCEPTION!" % period)

        try:
            device.Advanced.set_continuous_strobe_period(period)
            print("continuousStrobe(device): set strobePeriod =  %d " % period)
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("continuousStrobe(device): set_continuous_strobe_period() %d = %s" % (errorCode, errorMsg))

        try:
            period = device.Advanced.get_continuous_strobe_period()
            print("continuousStrobe(device): get strobePeriod =  %d " % period)
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("continuousStrobe(device): get_continuous_strobe_period() %d = %s" % (errorCode, errorMsg))
        print("")

    try:
        strobeWidth = 216
        device.Advanced.set_continuous_strobe_width(strobeWidth)
        print("continuousStrobe(device): set strobeWidth    =  %d " % strobeWidth)

        strobeWidth = device.Advanced.get_continuous_strobe_width()
        print("continuousStrobe(device): get strobeWidth    =  %d " % strobeWidth)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("continuousStrobe(device): %d = %s" % (errorCode, errorMsg))

    print("")

def scanToAverageBoxcar(device, scanToAve, boxcarWidth):
    try:
        value = device.get_scans_to_average()
        print("scanToAverageBoxcar(): cur scans_to_average        =  %d" % value)

        value = device.get_integration_time()
        print("scanToAverageBoxcar(): current integrationTimeUs   =  %d" % value)

        minAveIntTime = device.get_minimum_averaging_integration_time()
        print("scanToAverageBoxcar(): minAverageIntegrationTimeUs =  %d" % minAveIntTime)
        print("")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("scanToAverageBoxcar(): set/get / %d = %s" % (errorCode, errorMsg))

    try:
        print("scanToAverageBoxcar(): set_scans_to_average        =  %d" % scanToAve)
        device.set_scans_to_average(scanToAve)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("scanToAverageBoxcar(): ERROR with code/scanToAverage, %d = %s ************" % (errorCode, scanToAve))

    try:
        value = device.get_scans_to_average()
        print("scanToAverageBoxcar(): get_scans_to_average        =  %d" % value)

    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("scanToAverageBoxcar(device): set/get / %d = %s" % (errorCode, errorMsg))

    try:
        device.set_boxcar_width(boxcarWidth)
        print("scanToAverageBoxcar(): set_boxcar_width            =  %d" % boxcarWidth)

        value = device.get_boxcar_width()
        print("scanToAverageBoxcar(): get_boxcar_width            =  %d" % value)

    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("scanToAverageBoxcar(): set/get / %d = %s" % (errorCode, errorMsg))
    print("")

def get_spec_formatted(device, sn):
    try:
        #100ms
        device.set_integration_time(100000);

        print("Reading spectra for dev s/n = %s" % sn, flush=True)
        for i in range(10):
            spectra = device.get_formatted_spectrum()
            print("spectra[100]: %d, %d, %d, %d" % (spectra[100], spectra[101], spectra[102], spectra[103]), flush=True)
    except OceanDirectError as e:
        [errorCode, errorMsg] = err.get_error_details()
        print("get_spec_formatted(device): exception / %d = %s" % (errorCode, errorMsg))

def get_spec_raw_with_meta(device, sn):
    try:
        #100ms
        device.set_integration_time(100000);

        print("[START] Reading spectra for dev s/n = %s" % sn, flush=True)
        for i in range(10):
            spectra = []
            timestamp = []
            total_spectra = device.Advanced.get_raw_spectrum_with_metadata(spectra, timestamp, 3)

            print("len(spectra) =  %d" % (total_spectra) )

            #print sample count on each spectra
            for x in range(total_spectra):
                print("spectraWithMetadata: %d ==>  %d, %d, %d, %d" % (timestamp[x], spectra[x][100], spectra[x][101], spectra[x][102], spectra[x][103]))
    except OceanDirectError as e:
        [errorCode, errorMsg] = err.get_error_details()
        print("get_spec_raw_with_meta(device): exception / %d = %s" % (errorCode, errorMsg))


if __name__ == '__main__':

    #
    # To test this file quickly, do the following:
    # 1. Copy this file into <install_folder>\Python (ex: C:\Program Files\Ocean Insight\OceanDirect SDK-1.31.0\Python)
    # 2. Open a window shell and go to that folder
    # 3. Run this command:  python3 .\PythonExampleForOceanDirect.py
    #

    od = OceanDirectAPI()
    device_count = od.find_usb_devices()
    device_ids = od.get_device_ids()

    device_count = len(device_ids)
    (major, minor, point) = od.get_api_version_numbers()

    print("API Version  : %d.%d.%d " % (major, minor, point))
    print("Total Device : %d     \n" % device_count)

    if device_count == 0:
        print("No device found.")
    else:
        for id in device_ids:
            device       = od.open_device(id)
            serialNumber = device.get_serial_number()

            print("First Device : %d       " % id)
            print("Serial Number: %s     \n" % serialNumber)

            acquisitionDelay(device)
            #scanToAverageBoxcar(device, 10, 0)
            get_spec_formatted(device, serialNumber)
            #If devices don't support metadata then you will get an exception.
            #get_spec_raw_with_meta(device, serialNumber)
            #gpio(device)
            #singleStrobe(device)
            #continuousStrobe(device)

            print("Closing device!\n")
            od.close_device(id)

    print("**** exiting program ****")
    

