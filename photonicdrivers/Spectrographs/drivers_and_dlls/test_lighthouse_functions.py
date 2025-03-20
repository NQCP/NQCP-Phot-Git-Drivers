# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:58:47 2020

@author: Ocean Insight Inc.
"""

from ctypes.wintypes import LONG
from pickletools import long1
from oceandirect.LighthouseAPI import LighthouseAPI
from oceandirect.LighthouseTypes import OceanDirectError,  SpectrumWithMetadata
import time
from datetime import datetime



def get_spec_formatted(od: LighthouseAPI, id: int, spectraCount, integrationTime, fileName, writeToFile):
    print("get_spec_formatted(device):[START] Reading formatted spectra for dev s/n = %s" % serialNumber, flush=True)

    try:
        print("get_spec_formatted(device): set integration time(us) =  %d" % (integrationTime), flush=True)
        od.set_integration_time(id, integrationTime);
        print("get_spec_formatted(device): get integration time(us) =  %d" % (od.get_integration_time(id)), flush=True)

        scanAve = 4
        od.set_scans_to_average(id, scanAve)
        print("get_spec_formatted(device): set scan-average         =  %d" % (scanAve), flush=True)
        scanAve = od.get_scans_to_average(id)
        print("get_spec_formatted(device): get scan-average         =  %d" % (scanAve), flush=True)

        #value = od.get_integration_time()
        #print("get_spec_formatted(device): set integration time =  %d" % (integrationTime))
        #print("get_spec_formatted(device): get integration time =  %d" % (value))

        spectraLength = od.get_spectrum_length(id)
        print("get_spec_formatted(device): spectraLength =  %d" % (spectraLength), flush=True)
        
        if writeToFile == False:
            for i in range(spectraCount):
                spectra = od.get_spectrum(id)
                print("get_spec_formatted(device): spectra[%d] #%d =  %d, %d, %d, %d" %
                      (len(spectra), i, spectra[100], spectra[105], spectra[110], spectra[115]), flush=True)
        else:
            f = open(fileName, "w")
            for i in range(spectraCount):
                spectra = od.get_spectrum(id)
                print("get_spec_formatted(device): spectra =  %d, %d, %d, %d" %
                      (spectra[100], spectra[105], spectra[110], spectra[115]), flush=True)
                for x in range(spectraLength):
                    count = "{:.2f}, ".format(spectra[x])
                    f.write(count)
                f.write("\n")
            f.close()

        print("")
    except OceanDirectError as e:
        [errorCode, errorMsg] = e.get_error_details()
        print("get_spec_formatted(): ERROR with code/msg, %d = %s ************" % (errorCode, errorMsg))

def get_spec_raw_with_meta(od: LighthouseAPI, id: int, spectraCount, integrationTime, fileName, writeToFile):
    try:
        #50ms
        od.set_integration_time(integrationTime);

        print("[START] Reading spectra with metadata for dev s/n = %s" % serialNumber, flush=True)

        spectraLength = od.get_formatted_spectrum_length()
        print("get_spec_raw_with_meta(device): spectraLength =  %d" % (spectraLength), flush=True)

        for i in range(spectraCount):
            spectra = []
            timestamp = []

            total_spectra = od.get_raw_spectrum_with_metadata(spectra, timestamp, 5)

            if writeToFile == False:
                for i in range(total_spectra):
                    spectra = []
                    timestamp = []
                    total_spectra = od.get_raw_spectrum_with_metadata(spectra, timestamp, 3)

                    print("len1(spectra) =  %d" % (total_spectra) )

                    #print sample count on each spectra
                    for x in range(total_spectra):
                        print("spectra: %d, %d, %d, %d" % (spectra[x][100], spectra[x][105], spectra[x][110], spectra[x][115]), flush=True)
            else:
                f = open(fileName, "w")
                for i in range(spectraCount):
                    spectra = []
                    timestamp = []
                    total_spectra = od.get_raw_spectrum_with_metadata(spectra, timestamp, 3)

                    print("len2(spectra) =  %d" % (total_spectra), flush=True)

                    #print sample count on each spectra
                    for x in range(total_spectra):
                        print("spectra: %d, %d, %d, %d" % (spectra[x][100], spectra[x][105], spectra[x][110], spectra[x][115]), flush=True)

                        for y in spectra[x]:
                            count = "{:.2f}, ".format(y)
                            f.write(count)
                        f.write("\n")
                f.close()

        print("")
    except OceanDirectError as e:
        [errorCode, errorMsg] = e.get_error_details()
        print("get_spec_raw_with_meta(): ERROR with code/msg, %d = %s ************" % (errorCode, errorMsg))

def integrationTime(od: LighthouseAPI, id: int, intTimeUs):
    intIncrement = 0
    try:
        intIncrement = od.get_integration_time_increment(id)
        value        = od.get_integration_time(id)
        print("integrationTime(device): get integrationTime  =  %d" % value)
    except OceanDirectError as e:
        [errorCode, errorMsg] = e.get_error_details()
        print("integrationTime(): ERROR with code/integrationTimeIncrementUs, %d = %s ************" % (errorCode, errorMsg))

    print("integrationTime(device): get integrationTimeIncrement =  %d" % intIncrement)
    integrationTimeList = [8, 2000, 10000, 1300, 12514, 20205, 30000, 900, 65535, 100500, 1000500, 6000000, 10000000, 120000000, 12500, 65000100]
    #deviceTest = "sr2"
    #deviceTest = "sts3"
    #deviceTest = "nr"
    deviceTest = "other"

    for value in integrationTimeList:
        try:
            if deviceTest=="sr2" and (value == 8 or value==10000000 or value==65000100):
                print("integrationTime(device): set integrationTime   =  %d  ====> ********* expecting EXCEPTION!" % value)
            elif deviceTest=="sts3" and ((value % intIncrement) != 0 or value == 8 or value==10000000 or value==65000100):
                print("integrationTime(device): set integrationTime   =  %d  ====> ********* expecting EXCEPTION!" % value)
            elif deviceTest=="nr" and (value < 1000 or value>12000000):
                print("integrationTime(device): set integrationTime   =  %d  ====> ********* expecting EXCEPTION!" % value)
            else:
                print("integrationTime(device): set integrationTime   =  %d" % value)
            od.set_integration_time(id, value)
        except OceanDirectError as e:
            [errorCode, errorMsg] = e.get_error_details()
            print("integrationTime(): ERROR with code/setIntegrationTimeUs, %d = %s ************" % (errorCode, errorMsg))

        try:
            value = od.get_integration_time(id)
            print("integrationTime(device): get integrationTime   =  %d" % value)
        except OceanDirectError as e:
            [errorCode, errorMsg] = e.get_error_details()
            print("integrationTime(): ERROR with code/getIntegrationTimeUs, %d = %s ************" % (errorCode, value))
        print("")

    minAveIntTime = 0
    try:
        minAveIntTime = od.get_minimum_averaging_integration_time(id)
    except OceanDirectError as e:
        [errorCode, errorMsg] = e.get_error_details()
        print("integrationTime(): ERROR with code/get_minimum_averaging_integration_time(), %d = %s ************" % (errorCode, errorMsg))

    maxIntTime = 0
    try:
        maxIntTime = od.get_maximum_integration_time(id)
    except OceanDirectError as e:
        [errorCode, errorMsg] = e.get_error_details()
        print("integrationTime(): ERROR with code/get_maximum_integration_time(), %d = %s ************" % (errorCode, errorMsg))

    intTimeInc = 0
    try:
        intTimeInc = od.get_integration_time_increment(id)
    except OceanDirectError as e:
        [errorCode, errorMsg] = e.get_error_details()
        print("integrationTime(): ERROR with code/get_integration_time_increment(), %d = %s ************" % (errorCode, errorMsg))

    intTime = 0
    try:
        intTime = od.get_integration_time(id)
    except OceanDirectError as e:
        [errorCode, errorMsg] = e.get_error_details()
        print("integrationTime(): ERROR with code/get_integration_time(), %d = %s ************" % (errorCode, errorMsg))

    minIntTime = 0
    try:
        minIntTime = od.get_minimum_integration_time(id)
    except OceanDirectError as e:
        [errorCode, errorMsg] = e.get_error_details()
        print("integrationTime(): ERROR with code/get_minimum_integration_time(), %d = %s ************" % (errorCode, errorMsg))

    try:
        od.set_integration_time(id, intTimeUs)
    except OceanDirectError as e:
        [errorCode, errorMsg] = e.get_error_details()
        print("integrationTime(): ERROR with code/set_integration_time(), %d = %s ************" % (errorCode, errorMsg))
    
    intTime2 = od.get_integration_time(id)

    print("integrationTime(device): min integration time(us)     =  %d " % minIntTime)
    print("integrationTime(device): min ave integration time(us) =  %d " % minAveIntTime)
    print("integrationTime(device): max integration time(us)     =  %d " % maxIntTime)
    print("integrationTime(device): integration time inc(us)     =  %d " % intTimeInc)
    print("integrationTime(device): old integration time(us)     =  %d " % intTime)
    print("integrationTime(device): new integration time(us)     =  %d " % intTime2)
    print("")


def edcNLPixels(od: LighthouseAPI, id: int):
    maxIntensity = od.get_max_intensity();
    print("pixel(device): maxIntensity =  %d " % maxIntensity)

    #The devices below have no electric dark pixel. Calling the two methods
    #will throw an exception.
    #  -NIRQuest-256
    #  -NIRQuest-512
    #  -Ocean ST (STS3)
    #  -Ocean FX
    #  -Ocean SR6
    electricDarkPixelIndices = []

    try:
        electricDarkPixelCount   = od.get_number_electric_dark_pixels();
        print("pixel(device): electricDarkPixelCount        =  %d " % electricDarkPixelCount)
    except OceanDirectError as e:
        [errorCode, errorMsg] = e.get_error_details()
        print("edcNLPixels(): ERROR with code/get_number_electric_dark_pixels(), %d = %s ************" % (errorCode, errorMsg))

    try:
        electricDarkPixelIndices = od.get_electric_dark_pixel_indices();
        print("pixel(device): electricDarkPixelIndices size =  %d " % len(electricDarkPixelIndices))
    except OceanDirectError as e:
        [errorCode, errorMsg] = e.get_error_details()
        print("edcNLPixels(): ERROR with code/get_electric_dark_pixel_indices(), %d = %s ************" % (errorCode, errorMsg))

    for index in electricDarkPixelIndices:
        print("pixel(device): index =  %d " % index)
    print("")

def wavelength(od: LighthouseAPI, id: int):
    wavelengths = od.get_wavelengths(id);

    for w in wavelengths:
        print("wavelength(device): wavelengths =  %f " % w)
    print("")

def singleStrobe(od: LighthouseAPI, id: int):
    enable      = od.get_single_strobe_state(id)
    strobeWidth = od.get_single_strobe_width(id)
    strobeDelay = od.get_single_strobe_delay(id)

    print("singleStrobe(device): get default enable      =  %s " % enable)
    print("singleStrobe(device): get default strobeWidth =  %d " % strobeWidth)
    print("singleStrobe(device): get default strobeDelay =  %d " % strobeDelay)

    values = [False, True, False, True]
    for enable in values:
        od.set_single_strobe_state(id, enable);
        print("singleStrobe(device): set enable      =  %s " % enable)

        enable2 = od.get_single_strobe_state(id);
        print("singleStrobe(device): get enable      =  %s " % enable2)
        print("")

    od.set_single_strobe_state(id, True);
    enable = od.get_single_strobe_state(id)
    print("singleStrobe(device): enable(True)    =  %s " % enable)

    strobeWidthList = [300, 500, 600]
    for strobeWidth in strobeWidthList:
        od.set_single_strobe_width(id, strobeWidth)
        print("singleStrobe(device): set strobeWidth =  %d " % strobeWidth)
        strobeWidth = od.get_single_strobe_width(id)
        print("singleStrobe(device): get strobeWidth =  %d " % strobeWidth)
        print("")

    strobeDelayList = [222, 333, 444]
    for strobeDelay in strobeDelayList:
        od.set_single_strobe_delay(id, strobeDelay)
        print("singleStrobe(device): set strobeDelay =  %d " % strobeDelay)
        strobeDelay = od.get_single_strobe_delay(id)
        print("singleStrobe(device): get strobeDelay =  %d " % strobeDelay)
        print("")

    enable2 = od.get_single_strobe_state(id);
    print("singleStrobe(device): get enable      =  %s " % enable2)
    print("")

    try:
        delayMin = od.get_single_strobe_delay_minimum(id)
        print("singleStrobe(device): delayMin         =  %d " % delayMin)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("singleStrobe(device): get_single_strobe_delay_minimum() %d = %s" % (errorCode, errorMsg))

    try:
        delayMax = od.get_single_strobe_delay_maximum(id)
        print("singleStrobe(device): delayMax         =  %d " % delayMax)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("singleStrobe(device): get_single_strobe_delay_maximum() %d = %s" % (errorCode, errorMsg))

    try:
        delayInc = od.get_single_strobe_delay_increment(id)
        print("singleStrobe(device): delayInc         =  %d " % delayInc)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("singleStrobe(device): get_single_strobe_delay_increment() %d = %s" % (errorCode, errorMsg))

    try:
        widthMin = od.get_single_strobe_width_minimum(id)
        print("singleStrobe(device): widthMin         =  %d " % widthMin)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("singleStrobe(device): get_single_strobe_width_minimum() %d = %s" % (errorCode, errorMsg))

    try:
        widthMax = od.get_single_strobe_width_maximum(id)
        print("singleStrobe(device): widthMax         =  %d " % widthMax)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("singleStrobe(device): get_single_strobe_width_maximum() %d = %s" % (errorCode, errorMsg))

    try:
        widthInc = od.get_single_strobe_width_increment(id)
        print("singleStrobe(device): widthInc         =  %d " % widthInc)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("singleStrobe(device): get_single_strobe_width_increment() %d = %s" % (errorCode, errorMsg))
    print("")

def continuousStrobe(od: LighthouseAPI, id: int):
    periodInc = 0
    try:
        periodInc = od.get_continuous_strobe_period_increment(id)
        print("continuousStrobe(device): get period increment =  %d " % periodInc)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("continuousStrobe(device): get_continuous_strobe_period_increment() %d = %s" % (errorCode, errorMsg))

    try:
        strobePeriod = od.get_continuous_strobe_period(id)
        print("continuousStrobe(device): get strobePeriod    =  %d " % strobePeriod)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("continuousStrobe(device): get_continuous_strobe_period() %d = %s" % (errorCode, errorMsg))

    try:
        strobeEnable = od.get_continuous_strobe_state(id)
        print("continuousStrobe(device): get strobeEnable    =  %s " % strobeEnable)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details();
        print("continuousStrobe(device): get_continuous_strobe_enable() %d = %s" % (errorCode, errorMsg))
    print("")

    values = [False, True, False, True]
    for enable in values:
        try:
            od.set_continuous_strobe_state(id, enable)
            print("continuousStrobe(device): set strobeEnable    =  %s " % enable)
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details();
            print("continuousStrobe(device): set_continuous_strobe_enable() %d = %s" % (errorCode, errorMsg))

        try:
            strobeEnable = od.get_continuous_strobe_state(id)
            print("continuousStrobe(device): get strobeEnable    =  %s " % strobeEnable)
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details();
            print("continuousStrobe(device): get_continuous_strobe_enable() %d = %s" % (errorCode, errorMsg))
        print("")

    try:
        periodMin = od.get_continuous_strobe_period_minimum(id)
        print("continuousStrobe(device): get strobePeriodMin =  %d " % periodMin)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("continuousStrobe(device): get_continuous_strobe_period_minimum() %d = %s" % (errorCode, errorMsg))

    try:
        periodMax = od.get_continuous_strobe_period_maximum(id)
        print("continuousStrobe(device): get strobeperiodMax =  %d " % periodMax)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("continuousStrobe(device): get_continuous_strobe_period_maximum() %d = %s" % (errorCode, errorMsg))
    print("")

    #strobePeriodList = [1200, 1505, 800, 453]
    #strobePeriodList = [1200, 3400, 7500]
    strobePeriodList = [1200, 1505, 800, 453]
    #strobePeriodList = [1200, 7500]
    for period in strobePeriodList:
        #if (periodInc > 1) and ((period % periodInc) != 0):
        #    print("continuousStrobe(device): set strobePeriod   =  %d  ====> ********* expecting EXCEPTION!" % period)
        try:
            od.set_continuous_strobe_period(id, period)
            print("continuousStrobe(device): set strobePeriod   =  %d " % period)
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("continuousStrobe(device): set_continuous_strobe_period() %d = %s" % (errorCode, errorMsg))

        try:
            period = od.get_continuous_strobe_period(id)
            print("continuousStrobe(device): get strobePeriod   =  %d " % period)
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("continuousStrobe(device): get_continuous_strobe_period() %d = %s" % (errorCode, errorMsg))
        print("")
    print("")

def printBinary(value: int):
    bitCount = 32 #32 bits
    numValue = int(value)

    print("bits (%d) = " % numValue, end='')
    for i in range(32, -1, -1):
        print("%d " % ((numValue >> i) & 0x01), end='')

    print(" ")


def gpio(od: LighthouseAPI, id: int):
    tempCount = od.get_gpio_pin_count(id)
    print("gpio(device): pin count          =  %d " % tempCount)

    #printBinary(5)
    #printBinary(9)

    try:
        outputVector = od.get_gpio_output_enable(id)
        printBinary(outputVector)
        print("---------------------------------------------------------------\n\n")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("gpio(device): exception / %d = %s" % (errorCode, errorMsg))

    try:
        od.set_gpio_output_enable(id, 1, 0xFF)
        #bitOutput1 = od.get_gpio_output_enable(id, 0)
        print("gpio(device): set output vector bits / mask     =  00000000 / 1(True)")
        #print("gpio(device): get bit(0) output                 =  1(%s)" % bitOutput1)
        outputVector = od.get_gpio_output_enable(id)
        print("gpio(device): get output vector expected output =  00000001")
        printBinary(outputVector)
        print("\n")

        #set bit 1100 (3/4) to 1
        od.set_gpio_output_enable(id, 0xFF,  12)
        #od.set_gpio_output_enable(id, 2, 1)
        #od.set_gpio_output_enable(id, 3, 1)
        #bitOutput1 = od.get_gpio_output_enable(2)
        #bitOutput2 = od.get_gpio_output_enable(3)
        print("gpio(device): set output vector bits / mask     =  00000001 / 3(True),4(True)")
        #print("gpio(device): get bit(2,3) output               =  2(%s) / 3(%s)" % (bitOutput1, bitOutput2) )
        outputVector = od.get_gpio_output_enable(id)
        print("gpio(device): get output vector expected output =  00001101")
        printBinary(outputVector)
        print("\n")

        # set bit 1011 (1,2,4) to 1(0), 2(1), 4(0) 
        od.set_gpio_output_enable(id, 2, 11)
        #od.set_gpio_output_enable(id, 0, 0)
        #od.set_gpio_output_enable(id, 1, 1)
        #od.set_gpio_output_enable(id, 3, 0)
        #bitOutput1 = od.get_gpio_output_enable(0)
        #bitOutput2 = od.get_gpio_output_enable(1)
        #bitOutput3 = od.get_gpio_output_enable(3)
        print("gpio(device): set output vector bits / mask     =  00001101 / 1(False),2(True),4(False)")
        #print("gpio(device): get bit(0,1,3) output             =  0(%s) / 1(%s) / 3(%s)" % (bitOutput1, bitOutput2, bitOutput3))
        outputVector = od.get_gpio_output_enable(id)
        print("gpio(device): get output vector expected output =  00000110")
        printBinary(outputVector)
        print("\n")


        #set bit 1001 (1/4) to 1
        od.set_gpio_output_enable(id, 0xFF, 9)
        #od.set_gpio_output_enable(id, 0, 1)
        #od.set_gpio_output_enable(id, 3, 1)
        #bitOutput1 = od.get_gpio_output_enable1(0)
        #bitOutput2 = od.get_gpio_output_enable1(3)
        print("gpio(device): set output vector bits / mask     =  00000110 / 1(True),4(True)")
        #print("gpio(device): get bit(0,3) output               =  1(%s) / 4(%s)" % (bitOutput1, bitOutput2))
        outputVector = od.get_gpio_output_enable(id)
        print("gpio(device): get output vector expected output =  00001111")
        printBinary(outputVector)
        print("")
        print("---------------------------------------------------------------\n\n")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("gpio(device): gpio_output_bits() / %d = %s" % (errorCode, errorMsg))

    try:
        # set bit 0011 (1,2) to 1(1), 2(1)
        od.set_gpio_value(id, 0xFF, 3)
        #od.set_gpio_value(id, 0, 1)
        #od.set_gpio_value(id, 1, 1)
        #value1 = od.get_gpio_value(id, 0)
        #value2 = od.get_gpio_value(id, 1)
        print("gpio(device): set value vector values / mask   =  00000000 / 1(True), 2(True)")
        #print("gpio(device): get bit(0,1) value               =  0(%s) / 1(%s)" % (value1, value2))
        valueVector = od.get_gpio_value(id)
        print("gpio(device): get value vector expected values =  00000011")
        printBinary(valueVector)
        print("")

        # set bit 1100 (3,4) to 3(1), 4(1)
        od.set_gpio_value(id, 0xFF, 12);
        #od.set_gpio_value(id, 2, 1);
        #od.set_gpio_value(id, 3, 1);
        #value1 = od.get_gpio_value(2)
        #value2 = od.get_gpio_value(3)
        print("gpio(device): set value vector values / mask   =  00000011 / 3(True),4(True)")
        #print("gpio(device): get bit(2,3) value               =  2(%s) / 3(%s)" % (value1, value2))
        valueVector = od.get_gpio_value(id)
        print("gpio(device): get value vector expected values =  00001111")
        printBinary(valueVector)
        print("")

        # set bit 0101 (1,3) to 1(0), 3(0)
        od.set_gpio_value(id, 0, 5)
        #od.set_gpio_value(id, 0, 0)
        #od.set_gpio_value(id, 2, 0)
        #value1 = od.get_gpio_value(id, 0)
        #value2 = od.get_gpio_value(id, 2)
        print("gpio(device): set value vector values / mask   =  00001111 / 1(False), 3(False)")
        #print("gpio(device): get bit(0,2) value               =  0(%s) / 2(%s)" % (value1, value2))
        valueVector = od.get_gpio_value(id)
        print("gpio(device): get value vector expected values =  00001010")
        printBinary(valueVector)
        print("")

        # set bit 1010 (2,4) to 2(0), 4(0)
        od.set_gpio_value(id, 0, 10)
        #od.set_gpio_value(id, 1, 0)
        #od.set_gpio_value(id, 3, 0)
        #value1 = od.get_gpio_value(id, 1)
        #value2 = od.get_gpio_value(id, 3)
        print("gpio(device): set value vector values / mask   =  00001010 / 2(False), 4(False)")
        #print("gpio(device): get bit(1,3) value               =  1(%s) / 3(%s)" % (value1, value2))
        valueVector = od.get_gpio_value(id)
        print("gpio(device): get value vector expected values =  00000000")
        printBinary(valueVector)
        print("\n")

    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("gpio(device): exception / %d = %s" % (errorCode, errorMsg))

    ##Output bit masks
    #try:
    #    #15 = 1111
    #    od.set_gpio_output_enable(id, 15)
    #    print("gpio(device): set output mask(15)        =  00001111")

    #    mask = od.gpio_get_output_enable(id)
    #    print("gpio(device): expecting output mask (15) =  %d" % mask)
    #except OceanDirectError as err:
    #    [errorCode, errorMsg] = err.get_error_details()
    #    print("gpio(device): exception / %d = %s" % (errorCode, errorMsg))

    ##Value bit masks
    #try:
    #    #12 = 1100
    #    od.set_gpio_value(id, 12)
    #    print("")
    #    print("gpio(device): set value mask(12)        =  00001100")

    #    mask = od.gpio_get_value(id)
    #    print("gpio(device): expecting value mask (12) =  %d" % mask)
    #except OceanDirectError as err:
    #    [errorCode, errorMsg] = err.get_error_details()
    #    print("gpio(device): exception / %d = %s" % (errorCode, errorMsg))
    print("")


def gpioOVRead(od: LighthouseAPI, id: int):
    tempCount = od.get_gpio_pin_count()
    print("gpio(device): pin count          =  %d " % tempCount)

    try:
        outputVector = od.gpio_get_output_enable2()
        printBinary(outputVector)
        print("---------------------------------------------------------------\n\n")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("gpio(device): exception / %d = %s" % (errorCode, errorMsg))

    try:
        bitOutput0 = od.gpio_get_output_enable1(0)
        bitOutput1 = od.gpio_get_output_enable1(1)
        bitOutput2 = od.gpio_get_output_enable1(2)
        bitOutput3 = od.gpio_get_output_enable1(3)

        print("gpio(device): get bit(0) output                 =  0(%s)" % bitOutput0)
        print("gpio(device): get bit(0) output                 =  1(%s)" % bitOutput1)
        print("gpio(device): get bit(0) output                 =  2(%s)" % bitOutput2)
        print("gpio(device): get bit(0) output                 =  3(%s)" % bitOutput3)
        outputVector = od.gpio_get_output_enable2()
        print("gpio(device): get output vector expected output =  0011")
        printBinary(outputVector)
        print("\n")
        print("---------------------------------------------------------------\n\n")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("gpio(device): gpio_output_bits() / %d = %s" % (errorCode, errorMsg))

    try:
        value0 = od.gpio_get_value1(0)
        value1 = od.gpio_get_value1(1)
        value2 = od.gpio_get_value1(2)
        value3 = od.gpio_get_value1(3)
        print("gpio(device): get bit(0,1,3,4) value           =  3(%s) / 2(%s) / 1(%s) / 0(%s)" % (value3, value2, value1, value0))
        valueVector = od.gpio_get_value2()
        print("gpio(device): get value vector expected values =  1100")
        printBinary(valueVector)
        print("\n")

    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("gpio(device): exception / %d = %s" % (errorCode, errorMsg))
    print("")

def thermoElectric(od: LighthouseAPI, id: int):
    try:
        newSetpoint = -7.63
        #newSetpoint = -34.00  #QEPro will throw error
        #newSetpoint = -33.00  #QEPro minimum limit
        od.set_tec_temperature_setpoint(id, newSetpoint)
        print("thermoElectric(device): set setpoint temp =  %2.2f" % (newSetpoint))
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("thermoElectric(device): set_tec_temperature_setpoint / %d = %s" % (errorCode, errorMsg))

    try:
        curSetpoint = od.get_tec_temperature_setpoint(id)
        print("thermoElectric(device): get setpoint temp =  %2.2f" % (curSetpoint))
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("thermoElectric(device): get_tec_temperature_setpoint / %d = %s" % (errorCode, errorMsg))

    try:
        curTemp = od.get_tec_temperature(id)
        print("thermoElectric(device): get temperature   =  %2.2f" % (curTemp))
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("thermoElectric(device): get_tec_temperature / %d = %s" % (errorCode, errorMsg))

    try:
        curStable = od.get_tec_stable(id)
        print("thermoElectric(device): get stable        =  %s" % (curStable))
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("thermoElectric(device): get_tec_stable() / %d = %s" % (errorCode, errorMsg))
    print("")


def revision(od: LighthouseAPI, id: int):
    try:
        fwVersion = od.get_revision_firmware(id)
        print("revision(device): fwVersion   =  %s " % fwVersion)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("revision(device): get_revision_firmware() / %d = %s" % (errorCode, errorMsg))

    try:
        fpgaVersion = od.get_revision_fpga(id)
        print("revision(device): fpgaVersion =  %s " % fpgaVersion)
        print("")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("revision(device): get_revision_fpga() / %d = %s" % (errorCode, errorMsg))
    print("")

def serialNumberTest(od: LighthouseAPI, id: int):
    try:
        serialNumberText = od.get_serial_number(id)
        print("serialNumber(device): get1 serial#   =  %s " % serialNumberText)

        #serialNumberText = od.get_serial_number()
        #print("serialNumber(device): get2 serial#   =  %s " % serialNumberText)

        #MayaPro =  MAYP114989, Flame-S = FLMS00015, NirQuest = NQ2100012, USB4000=USB4F02542
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("serialNumber(device): get_serial_number() / %d = %s" % (errorCode, errorMsg))

    #Set serial command is in Admin installer
    #try:
    #    #newSerial = "MAYP114989"
    #    #newSerial = "FLMS00015"
    #    newSerial = "ST1234567890AB"
    #    #newSerial = "NQ2100012"
    #    #newSerial = "USB4F02542"
    #    #newSerial = "HR+D1892"
    #    #newSerial = "HR4P0045"
    #    #newSerial = "HDX000007"
    #    od.set_serial_number(newSerial)
    #    print("serialNumber(device): set serial#   =  %s " % newSerial)

    #    #MayaPro =  MAYP114989, Flame-S = FLMS00015,
    #except OceanDirectError as err:
    #    [errorCode, errorMsg] = err.get_error_details()
    #    print("serialNumber(device): set_serial_number() / %d = %s" % (errorCode, errorMsg))

    #try:
    #    #Read serial number and see if it was persisted successfully.
    #    serialNumberText = od.get_serial_number()
    #    print("serialNumber(device): get serial#   =  %s " % serialNumberText)

    #    #MayaPro =  MAYP114989
    #except OceanDirectError as err:
    #    [errorCode, errorMsg] = err.get_error_details()
    #    print("serialNumber(device): get_serial_number() / %d = %s" % (errorCode, errorMsg))
    print("")

def usbEndPoints(od: LighthouseAPI, id: int):
    usbPrimaryIn    = od.get_usb_endpoint_primary_in(id)
    usbPrimaryOut   = od.get_usb_endpoint_primary_out(id)
    usbSecondaryIn  = od.get_usb_endpoint_secondary_in(id)
    usbSecondaryOut = od.get_usb_endpoint_secondary_out(id)

    print("usbEndPoints(device): usb primary in    =  %s " % hex(usbPrimaryIn) )
    print("usbEndPoints(device): usb primary out   =  %s " % hex(usbPrimaryOut) )
    print("usbEndPoints(device): usb secondary in  =  %s " % hex(usbSecondaryIn) )
    print("usbEndPoints(device): usb secondary out =  %s " % hex(usbSecondaryOut) )
    print("")

def deviceInfo(od: LighthouseAPI, id: int):
    serialNumber = od.get_serial_number(id)
    print("deviceInfo(device): serialNumber      =  %s " % serialNumber)

    #HDX00851
    #serialNumber ="HR200117"
    #od.set_serial_number(serialNumber)
    #print("deviceInfo(device): set serialNumber  =  %s " % serialNumber)

    #serialNumber = od.get_serial_number()
    #print("deviceInfo(device): serialNumber      =  %s " % serialNumber)
    #print("deviceInfo(device): deviceModel       =  %s " % deviceModel)

    deviceType  = od.get_device_type(id)
    deviceModel = od.get_model(id)
    print("deviceInfo(device): deviceType        =  %s " % deviceType)
    print("deviceInfo(device): deviceModel       =  %s " % deviceModel)

    try:
        orig_manufacturer = od.get_device_original_manufacturer_string(id)
        orig_model        = od.get_device_original_model_string(id)
        manufacturer      = od.get_device_manufacturer_string(id)
        model             = od.get_device_model_string(id)

        print("deviceInfo(device): orig_manufacturer =  %s " % orig_manufacturer)
        print("deviceInfo(device): orig_model        =  %s " % orig_model)
        print("deviceInfo(device): manufacturer      =  %s " % manufacturer)
        print("deviceInfo(device): model             =  %s " % model)

        #manufacturer = "Ocean Insight Inc"
        #od.set_device_manufacturer_string(manufacturer)
        #print("deviceInfo(device): set manufacturer  =  %s " % manufacturer)

        #model = "Ocean HR2"
        model = "SR6"
        #od.set_device_model_string(model)
        #print("deviceInfo(device): set model         =  %s " % model)

        orig_vid = od.get_device_original_vid(id)
        orig_pid = od.get_device_original_pid(id)
        vid      = od.get_device_vid(id)
        pid      = od.get_device_pid(id)
        print("deviceInfo(device): orig vid          =  %s " % hex(orig_vid))
        print("deviceInfo(device): orid pid          =  %s " % hex(orig_pid))
        print("deviceInfo(device): vid               =  %s " % hex(vid))
        print("deviceInfo(device): pid               =  %s " % hex(pid))

        #commandList = od.get_command_list()
        #print("Command List:")
        #for x in commandList:
        #    print("  ===>  %d" %x)

    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("deviceInfo(device): %d = %s" % (errorCode, errorMsg))
    print("")

#NOTE: This command is not exposed to user so commenting this one for documentation purposes only.
#def commandList(device):
#    commandList = od.get_command_list()
#    print("Command List:")
#    for x in commandList:
#        print("  ===> %s  =  %d" % (hex(x), x))

def acquisitionDelay(od: LighthouseAPI, id: int):
    #od.set_acquisition_delay(120)
    #print("acquisitionDelay(device): set acqDelay 120")

    acqDelay    = 0
    acqDelayInc = 0
    acqDelayMin = 0
    acqDelayMax = 0

    try:
        acqDelay = od.get_acquisition_delay(id)

        print("acquisitionDelay(device): acqDelay     =  %d " % acqDelay)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("acquisitionDelay(device): get_acquisition_delay() / %d = %s" % (errorCode, errorMsg))

    try:
        acqDelayInc = od.get_acquisition_delay_increment(id)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("acquisitionDelay(device): get_acquisition_delay_increment() / %d = %s" % (errorCode, errorMsg))

    try:
        acqDelayMin = od.get_acquisition_delay_minimum(id)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("acquisitionDelay(device): get_acquisition_delay_minimum() / %d = %s" % (errorCode, errorMsg))

    try:
        acqDelayMax = od.get_acquisition_delay_maximum(id)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("acquisitionDelay(device): get_acquisition_delay_maximum() / %d = %s" % (errorCode, errorMsg))

    print("acquisitionDelay(device): acqDelay     =  %d " % acqDelay)
    print("acquisitionDelay(device): acqDelayInc  =  %d " % acqDelayInc)
    print("acquisitionDelay(device): acqDelayMin  =  %d " % acqDelayMin)
    print("acquisitionDelay(device): acqDelayMax  =  %d " % acqDelayMax)
    print("")

    #400us
    valueList = {200, 300, 400, 500}
    for value in valueList:
        od.set_acquisition_delay(id, value)
        print("acquisitionDelay(device): set acqDelay =  %d " % value)

        acqDelay = od.get_acquisition_delay(id)
        print("acquisitionDelay(device): get acqDelay(expected %d)  =  %d " % (value, acqDelay) )
        print("")


def nonlinearityCoefficients(od: LighthouseAPI, id: int):
    try:
        coeffsList = od.get_nonlinearity_coeffs()
        print("nonlinearity(device): total get coeffs  =  %d " % len(coeffsList))

        for coeffs in coeffsList:
            print("nonlinearity(device): get ===>  %.50f " % coeffs)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("nonlinearity(device): get_nonlinearity_coeffs() / %d = %s" % (errorCode, errorMsg))

    #try:
    #    #newCoeffsList = [0.87654321, 0.12e-2, 0.23e-3, 0.34e-4, 0.45e-5, 0.56e-6, 0.67e-7, 0.78e-8,]
    #USB4000
    #newCoeffsList = [ 0.97958100000000003504396772768814116716384887695312,
    #                    0.00000159281000000000008622220992737794631466385908,
    #                    -0.00000000005620699999999999910233529896984598552695,
    #                    0.00000000000000143702000000000002797396029586236165,
    #                    -0.00000000000000000001886460000000000001806976787037,
    #                    -0.00000000000000000000000021085899999999997878989801,
    #                    0.00000000000000000000000000000819496999999999996744,
    #                    -0.00000000000000000000000000000000006212340000000000]

    #STS3
    #newCoeffsList = [ 0.98212301731109619140625000000000000000000000000000,
    #                  0.00000076317002140058320946991443634033203125000000,
    #                  -0.00000000005521509985340067316883505554869771003723,
    #                  0.00000000000000287883798288750270000235786937992088,
    #                  -0.00000000000000000000000180026992421186521953652746,
    #                  0.00000000000000000000000000004368199901305366775283,
    #                  -0.00000000000000000000000000000000028773100983292636,
    #                  0.00000000000000000000000000000000000000000089542972]

    #od.set_nonlinearity_coeffs(newCoeffsList)

    #    print("")
    #    print("nonlinearity(device): total new coeffs  =  %d " % len(newCoeffsList))
    #    for coeffs in newCoeffsList:
    #        print("nonlinearity(device): set ===>  %.50f " % coeffs)
    #except OceanDirectError as err:
    #    [errorCode, errorMsg] = err.get_error_details()
    #    print("nonlinearity(device): get_nonlinearity_coeffs() / %d = %s" % (errorCode, errorMsg))

    coeffsCount = 0
    try:
        coeffsCount = od.get_nonlinearity_coeffs_count1()
        print("")
        print("nonlinearity(device): coeffsCount  =  %d " % coeffsCount)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("nonlinearity(device): get_nonlinearity_coeffs_count1() / %d = %s" % (errorCode, errorMsg), flush=True)

    try:
        coeffsCount = 3
        if coeffsCount > 0:
            print("")
            for index in range(coeffsCount):
                coeffs = od.get_nonlinearity_coeffs1(index)
                print("nonlinearity(device): get index/coeffs  =  %d / %0.50f " % (index, coeffs), flush=True)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("nonlinearity(device): get_nonlinearity_coeffs1() / %d = %s" % (errorCode, errorMsg))

    #try:
    #    newCoeffsList = [0.987654321, 0.912e-2, 0.923e-3, 0.934e-4, 0.945e-5, 0.956e-6, 0.967e-7, 0.978e-8]
    #    print("")
    #    #for index in range(len(newCoeffsList)):
    #    #    coeffs = od.set_nonlinearity_coeffs1(index, newCoeffsList[index])
    #    #    print("nonlinearity(device): set index/coeffs  =  %d / %0.15f " % (index, newCoeffsList[index]), flush=True)
    #except OceanDirectError as err:
    #    [errorCode, errorMsg] = err.get_error_details()
    #    print("nonlinearity(device): set_nonlinearity_coeffs1() / %d = %s" % (errorCode, errorMsg))
    print("")


def spectraCorrection(od: LighthouseAPI, id: int):
    try:
        od.set_electric_dark_correction_usage(True)
        print("spectraCorrection(): set electric dark correction =  True" )

        value = od.get_electric_dark_correction_usage()
        print("spectraCorrection(): get electric dark correction =  %s" % value)

        od.set_electric_dark_correction_usage(False)
        print("spectraCorrection(): set electric dark correction =  False")

        value = od.get_electric_dark_correction_usage()
        print("spectraCorrection(): get electric dark correction =  %s" % value)

        od.set_nonlinearity_correction_usage(True)
        print("spectraCorrection(): set nonlinearity correction =  True")

        value = od.get_nonlinearity_correction_usage()
        print("spectraCorrection(): get nonlinearity correction =  %s" % value)

        od.set_nonlinearity_correction_usage(False)
        print("spectraCorrection(): set nonlinearity correction =  False")

        value = od.get_nonlinearity_correction_usage()
        print("spectraCorrection(): get nonlinearity correction =  %s" % value)

    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("spectraCorrection(device): ipv4_set_dhcp_enable() / %d = %s" % (errorCode, errorMsg))
    print("")

def ledState(od: LighthouseAPI, id: int):
    od.set_led_state(id, True)
    print("ledState(): set LED =  True" )

    state = od.get_led_state(id)
    print("ledState(): get LED =  %s" % state)

    for i in range(10):
        try:
            od.set_led_state(id, True)
            print("ledState(): set LED =  True" )

            state = od.get_led_state(id)
            print("ledState(): get LED =  %s" % state)
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("ledState(device): set/get LED() / %d = %s" % (errorCode, errorMsg))

        time.sleep(0.5)
        try:
            od.set_led_state(id, False)
            print("ledState(): set LED =  False")

            state = od.get_led_state(id)
            print("ledState(): get LED =  %s" % state)

        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("ledState(device): set/get LED() / %d = %s" % (errorCode, errorMsg))
        time.sleep(0.5)
    print("")


def deviceAlias(od: LighthouseAPI, id: int):
    try:
        deviceAlias = od.get_device_alias(id)
        print("deviceAlias(): deviceAlias     =  %s" % deviceAlias)

        #deviceAlias = "dev-alias-12"
        #od.set_device_alias(id, deviceAlias)
        #print("deviceAlias(): new deviceAlias =  %s" % deviceAlias)

        deviceAlias = od.get_device_alias(id)
        print("deviceAlias(): deviceAlias     =  %s" % deviceAlias)

    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("deviceAlias(device): set/get / %d = %s" % (errorCode, errorMsg))
    print("")

def userString(od: LighthouseAPI, id: int):
    try:
        #OBP2.0 - STS3/SR2 user string commands
        userStringValue = od.get_user_string(id)
        print("userString(): get user string =  %s" % userStringValue)

        userStringValue = "user-str-100"
        od.set_user_string(id, userStringValue)
        print("userString(): set user string =  %s" % userStringValue)

        userStringValue = od.get_user_string(id)
        print("userString(): value     =  %s" % userStringValue)

    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("userString(device): set/get / %d = %s" % (errorCode, errorMsg))
    print("")

def scanToAverageBoxcar(od: LighthouseAPI, id: int, scanToAve, boxcarWidth):
    try:
        value = od.get_scans_to_average()
        print("scanToAverageBoxcar(): cur scans_to_average        =  %d" % value)

        value = od.get_integration_time()
        print("scanToAverageBoxcar(): current integrationTimeUs   =  %d" % value)

        minAveIntTime = od.get_minimum_averaging_integration_time()
        print("scanToAverageBoxcar(): minAverageIntegrationTimeUs =  %d" % minAveIntTime)
        print("")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("scanToAverageBoxcar(): set/get / %d = %s" % (errorCode, errorMsg))


    try:
        print("scanToAverageBoxcar(): set_scans_to_average        =  %d" % scanToAve)
        od.set_scans_to_average(scanToAve)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("scanToAverageBoxcar(): ERROR with code/set_scans_to_average, %d = %s ************" % (errorCode, scanToAve))

    try:
        value = od.get_scans_to_average()
        print("scanToAverageBoxcar(): get_scans_to_average        =  %d" % value)

    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("scanToAverageBoxcar(device): set/get / %d = %s" % (errorCode, errorMsg))

    try:
        od.set_boxcar_width(boxcarWidth)
        print("scanToAverageBoxcar(): set_boxcar_width            =  %d" % boxcarWidth)

        value = od.get_boxcar_width()
        print("scanToAverageBoxcar(): get_boxcar_width            =  %d" % value)

    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("scanToAverageBoxcar(): set/get / %d = %s" % (errorCode, errorMsg))
    print("")

def scanToAverageWithMinimumAveragingTime(od: LighthouseAPI, id: int):
    # no exception here
    print("scanToAverageWithMinimumAveragingTime(): integrationTime(us)/ScanAve =  600 / 1 - GOOD, no exception")
    integrationTime(device, 600)
    scanToAverageBoxcar(device, 1, 0)

    print("scanToAverageWithMinimumAveragingTime(): integrationTime(us)/ScanAve =  112 / 1 - GOOD, no exception")
    integrationTime(device, 112)
    scanToAverageBoxcar(device, 1, 0)

    print("scanToAverageWithMinimumAveragingTime(): integrationTime(us)/ScanAve =  112 / 5 - BAD, exception expected")
    # exception willbe thrown here
    scanToAverageBoxcar(device, 5, 0)

    print("scanToAverageWithMinimumAveragingTime(): integrationTime(us)/ScanAve =  400 / 4 - GOOD, no exception")
    integrationTime(device, 400)
    scanToAverageBoxcar(device, 4, 0)

    # no exception here
    print("scanToAverageWithMinimumAveragingTime(): integrationTime(us)/ScanAve =  200 / 4 - BAD, exception expected")
    value = od.get_integration_time();
    print("scanToAverageWithMinimumAveragingTime(): current intTime(us)  =  %d" % value)
    value = od.get_scans_to_average();
    print("scanToAverageWithMinimumAveragingTime(): cur scans_to_average =  %d" % value)
    integrationTime(device, 200)

    print("scanToAverageWithMinimumAveragingTime(): integrationTime(us)/ScanAve =  400 / 6 - GOOD, no exception")
    value = od.get_integration_time();
    print("scanToAverageWithMinimumAveragingTime(): current intTime(us)  =  %d" % value)
    value = od.get_scans_to_average();
    print("scanToAverageWithMinimumAveragingTime(): cur scans_to_average =  %d" % value)
    scanToAverageBoxcar(device, 6, 0)

def scanToAverageWithNoMinimumAveragingTime(od: LighthouseAPI, id: int):
    # no exception here
    print("scanToAverageWithNoMinimumAveragingTime(): integrationTime(us)/ScanAve =  600 / 1")
    integrationTime(device, 600)
    scanToAverageBoxcar(device, 1, 0)

    print("scanToAverageWithNoMinimumAveragingTime(): integrationTime(us)/ScanAve =  112 / 1")
    integrationTime(device, 112)
    scanToAverageBoxcar(device, 1, 0)

    print("scanToAverageWithNoMinimumAveragingTime(): integrationTime(us)/ScanAve =  112 / 5")
    # exception willbe thrown here
    scanToAverageBoxcar(device, 5, 0)

    print("scanToAverageWithNoMinimumAveragingTime(): integrationTime(us)/ScanAve =  400 / 4")
    integrationTime(device, 400)
    scanToAverageBoxcar(device, 4, 0)

    # no exception here
    print("scanToAverageWithNoMinimumAveragingTime(): integrationTime(us)/ScanAve =  200 / 4")
    value = od.get_integration_time();
    print("scanToAverageWithNoMinimumAveragingTime(): current intTime(us)  =  %d" % value)
    value = od.get_scans_to_average();
    print("scanToAverageWithNoMinimumAveragingTime(): cur scans_to_average =  %d" % value)
    integrationTime(device, 200)

    print("scanToAverageWithNoMinimumAveragingTime(): integrationTime(us)/ScanAve =  400 / 6")
    value = od.get_integration_time();
    print("scanToAverageWithNoMinimumAveragingTime(): current intTime(us)  =  %d" % value)
    value = od.get_scans_to_average();
    print("scanToAverageWithNoMinimumAveragingTime(): cur scans_to_average =  %d" % value)
    scanToAverageBoxcar(device, 6, 0)

def electricNonlinearityCorrection(od: LighthouseAPI, id: int):
    #If the unit doesn't have optical dark pixels (ex: SR6) then
    #OD will throw an exception.
    try:
        statusList = [True, False, True]
        for state in statusList:
            od.set_electric_dark_correction_usage(state)
            print("electricNonlinearityCorrection(): set EDC state =  %s" % state)

            value = od.get_electric_dark_correction_usage()
            print("electricNonlinearityCorrection(): get EDC state =  %s" % value)
            print("")
            time.sleep(0.75)

        for state in statusList:
            od.set_nonlinearity_correction_usage(state)
            print("electricNonlinearityCorrection(): set NLC state =  %s" % state)

            value = od.get_nonlinearity_correction_usage()
            print("electricNonlinearityCorrection(): set NLC state =  %s" % value)
            print("")
            time.sleep(0.75)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("electricNonlinearityCorrection(device): set/get / %d = %s" % (errorCode, errorMsg))
    print("")

def autoNulling(od: LighthouseAPI, id: int):
    try:
        maxADCCount = od.get_autonull_maximum_adc_count(id)
        print("autoNulling(device): get maxADCCount =  %d" % maxADCCount)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("autoNulling(device): set/get / %d = %s" % (errorCode, errorMsg))

    try:
        baseline = od.get_autonull_baseline_level(id)
        print("autoNulling(device): get baseline    =  %d" % baseline)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("autoNulling(device): get_autonull_baseline_level() %d = %s" % (errorCode, errorMsg))

    try:
        saturation = od.get_autonull_saturation_level(id)
        print("autoNulling(device): get saturation  =  %d" % saturation)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("autoNulling(device): get_autonull_saturation_level() %d = %s" % (errorCode, errorMsg))
    print("")

def baudRate(od: LighthouseAPI, id: int):
    try:
        baudRate = od.get_baud_rate(id)
        print("baudRate(): get baudRate =  %d" % baudRate)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("baudRate(device): get_baud_rate / %d = %s" % (errorCode, errorMsg))

    #try:
    #    #300, 600, 1200, 2400, 9600, 14400, 19200, 38400, 57600, 115200
    #    od.set_baud_rate(115200)
    #    print("baudRate(): set baudRate =  115200")
    #except OceanDirectError as err:
    #    [errorCode, errorMsg] = err.get_error_details()
    #    print("baudRate(device): set_baud_rate / %d = %s" % (errorCode, errorMsg))

    #try:
    #    baudRate = od.get_baud_rate()
    #    print("baudRate(): get baudRate =  %d" % baudRate)
    #except OceanDirectError as err:
    #    [errorCode, errorMsg] = err.get_error_details()
    #    print("baudRate(device): get_baud_rate / %d = %s" % (errorCode, errorMsg))

    try:
        print("baudRate(): save settings to flash")
        od.save_settings_to_flash(id)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("baudRate(device): save_settings_to_flash / %d = %s" % (errorCode, errorMsg))
    print("")

def wavelengthCoefficients(device):
    """
    Set wavelength coefficient function was moved into the admin package.
    """
    try:
        wavelengthCoeffs = od.get_wavelength_coeffs()
        print("wavelengthCoefficients(): total wavelength coeffs =  %d" % len(wavelengthCoeffs) )
        for x in wavelengthCoeffs:
            print("===> %.50f" % x)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("wavelengthCoefficients(device): get_wavelength_coeffs / %d = %s" % (errorCode, errorMsg))

    try:
        # 298.6974487305
        # 0.4584049881
        # 0.0000001230
        # 0.0000000039

        #coeffs = [298.6974487305, 0.4584049881, 0.0000001230, 0.0000000039]

        #USB4000
        #coeffs = [346.68839000000002670276, 0.21748600000000001264, -0.00000583756000000000, -0.00000000036649000000]

        #HR2000+ES
        #coeffs = [222.69744873047000055521493777632713317871093750000000,
        #          1.45840498805049989528015430551022291183471679687500,
        #          2.00001230352969994186196345253847539424896240234375,
        #          3.00000000387020016034966829465702176094055175781250]

        #HR4000
        #coeffs = [100.697448730538774, 0.558404988143864, 0.00000022338740, 0.000000004989485]

        #STS3
        #coeffs = [190.5084075927734375,
        #          0.392986714839935302734375,
        #          -0.00002088843939418438822031021118164062500000000000,
        #          -0.00000000109719799912255666640703566372394561767578]


        #od.set_wavelength_coeffs(coeffs)
        print("")
        #print("wavelengthCoefficients(): set new wavelength coeffs")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("wavelengthCoefficients(device): set_wavelength_coeffs / %d = %s" % (errorCode, errorMsg))
    print("")

def triggerMode(od: LighthouseAPI, id: int, triggerModes: list[int])->None:
    for mode in triggerModes:
        try:
            print("triggerMode(device):  set trigger =  %d" % mode)
            od.set_trigger_mode(id, mode)
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("triggerMode(device): set trigger mode / %d = %s" % (errorCode, errorMsg))

        try:
            triggerMode = od.get_trigger_mode(id)
            print("triggerMode(device):  get trigger =  %d" % triggerMode)
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("triggerMode(device): get trigger mode / %d = %s" % (errorCode, errorMsg))
        print("")

    try:
        #reset trigger mode to free running
        print("triggerMode(device):  reset trigger to 0(free running)")
        od.set_trigger_mode(id, 0)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("triggerMode(device): set/get trigger mode / %d = %s" % (errorCode, errorMsg))

    print("")

def pixelInfo(od: LighthouseAPI, id: int):
    try:
        spectrumSize = od.get_spectrum_length(id)
        print("pixelInfo(): get_spectrum_length = %d" % (spectrumSize) )

    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("pixelInfo(device): get_spectrum_length / %d = %s" % (errorCode, errorMsg))
    print("")

    try:
        range = od.get_active_pixel_indices(id)
        print("pixelInfo(): get_active_pixel_indices, list =  %s" % " ".join(list(map(str,range))) )
        print("pixelInfo(): get_active_pixel_indices, list =  ", range )
        for x in range:
            #print("===> %d" % x)
            print(f"===> {x}")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("pixelInfo(device): get_active_pixel_indices / %d = %s" % (errorCode, errorMsg))
    print("")

    try:
        range = od.get_electric_dark_pixel_indices(id)
        print("pixelInfo(): get_electric_dark_pixel_indices, list =  %s" % " ".join(list(map(str, range))))
        print(f"pixelInfo(): get_electric_dark_pixel_indices, list =  {range}")
        for x in range:
            #print("===> %d" % x)
            print(f"===> {x}")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("pixelInfo(device): get_electric_dark_pixel_indices / %d = %s" % (errorCode, errorMsg))
    print("")

    try:
        range = od.get_transition_pixel_indices(id)
        print(f"pixelInfo(): get_transition_pixel_indices, list =  {range}")
        for x in range:
            print("===> %d" % x)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("pixelInfo(device): get_transition_pixel_indices / %d = %s" % (errorCode, errorMsg))
    print("")

    try:
        range = od.get_bad_pixel_indices(id)
        print("pixelInfo(): get_bad_pixel_indices")
        for x in range:
            print("===> %d" % x)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("pixelInfo(device): get_bad_pixel_indices / %d = %s" % (errorCode, errorMsg))
    print("")

    #try:
    #    badPixelIndices = [200, 201, 300, 301]
    #    od.set_bad_pixel_indices(badPixelIndices)
    #    print("")
    #    print("pixelInfo(): set_bad_pixel_indices")
    #except OceanDirectError as err:
    #    [errorCode, errorMsg] = err.get_error_details()
    #    print("pixelInfo(device): set_bad_pixel_indices / %d = %s" % (errorCode, errorMsg))
    #print("")


def darkSpectrumCorrection2(od: LighthouseAPI, id: int, allFunctionTest):
    edcSupported = False
    try:
        edcSupported = od.get_electric_dark_correction_usage()
        
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): get_electric_dark_correction_usage / %d = %s" % (errorCode, errorMsg))

    print("darkSpectrumCorrection(): using EDC =  %s \n" %  edcSupported)
    spectrumSize = od.get_formatted_spectrum_length()

    #lets create a sample dark spectrum
    darkSpectrum1 = [100.0 for i in range(spectrumSize)]
    darkSpectrum2 = [200.0 for i in range(spectrumSize)]

    #For STS3, it will throw an exception when the commented command below are called because
    #by default it does not support electric dark correction.
    #od.get_electric_dark_correction_usage()
    #od.get_nonlinearity_correction_usage()
    #od.set_electric_dark_correction_usage(True)
    #od.set_nonlinearity_correction_usage(True)

    try:
        #test for empty dark - expecting error code 10
        print("darkSpectrumCorrection(): set_stored_dark_spectrum(EMPTY_DARK) ====> ********* expecting EXCEPTION!")
        od.set_stored_dark_spectrum([])
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): set_stored_dark_spectrum / %d = %s" % (errorCode, errorMsg)) 
    print("")

    try:
        print("darkSpectrumCorrection(): set_stored_dark_spectrum(DARK)")
        od.set_stored_dark_spectrum(darkSpectrum1)
        darkSpectrum = od.get_stored_dark_spectrum()
        print("darkSpectrumCorrection(): get darkSpectrum, expecting =  100, 100, 100, 100, 100")
        print("darkSpectrumCorrection(): get darkSpectrum, actual    =  %d, %d, %d, %d, %d" % 
              (darkSpectrum[100], darkSpectrum[101], darkSpectrum[102], darkSpectrum[103], darkSpectrum[104]))

        print("")
        print("darkSpectrumCorrection(): read spectra and use EDC/NLC")
        illuminatedSpectrum = od.get_formatted_spectrum()
        print("darkSpectrumCorrection(): illuminatedSpectrum         =  %d, %d, %d, %d, %d" % 
              (illuminatedSpectrum[100], illuminatedSpectrum[101], illuminatedSpectrum[102],
               illuminatedSpectrum[103], illuminatedSpectrum[104]))
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): get_stored_dark_spectrum / %d = %s" % (errorCode, errorMsg))

    try:
        print("")
        print("darkSpectrumCorrection(): get_dark_corrected_spectrum1(EMPTY_DARK) ====> ********* expecting EXCEPTION!")

        spectra2 = od.get_dark_corrected_spectrum1([])
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): get_dark_corrected_spectrum1 / %d = %s" % (errorCode, errorMsg))

    try:
        print("")
        print("darkSpectrumCorrection(): get_dark_corrected_spectrum1(DARK)")
        if edcSupported:
            print("darkSpectrumCorrection(): EDC enabled ====> ********* expecting EXCEPTION!")

        illuminatedSpectrum = od.get_formatted_spectrum()
        spectra2 = od.get_dark_corrected_spectrum1(darkSpectrum2)
        print("darkSpectrumCorrection(): illuminatedSpectrum         =  %d, %d, %d, %d, %d" % 
              (illuminatedSpectrum[100], illuminatedSpectrum[101], illuminatedSpectrum[102],
               illuminatedSpectrum[103], illuminatedSpectrum[104]))
        print("darkSpectrumCorrection(): dark correction (minus 200) =  %d, %d, %d, %d, %d" % 
              (spectra2[100], spectra2[101], spectra2[102], spectra2[103], spectra2[104]))
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): get_dark_corrected_spectrum1 / %d = %s" % (errorCode, errorMsg))

    try:
        print("")
        print("darkSpectrumCorrection(): dark_correct_spectrum1(EMPTY_ILLUMINATED) ====> ********* expecting EXCEPTION!")

        spectra2 = od.dark_correct_spectrum1([])
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): dark_correct_spectrum1 / %d = %s" % (errorCode, errorMsg))

    try:
        print("")
        print("darkSpectrumCorrection(): dark_correct_spectrum1(ILLUMINATED)")
        if edcSupported:
            print("darkSpectrumCorrection(): EDC enabled ====> ********* expecting EXCEPTION!")

        illuminatedSpectrum = od.get_formatted_spectrum()
        spectra2 = od.dark_correct_spectrum1(illuminatedSpectrum)
        print("darkSpectrumCorrection(): illuminatedSpectrum         =  %d, %d, %d, %d, %d" % 
              (illuminatedSpectrum[100], illuminatedSpectrum[101], illuminatedSpectrum[102],
               illuminatedSpectrum[103], illuminatedSpectrum[104]))
        print("darkSpectrumCorrection(): dark correction (minus 100) =  %d, %d, %d, %d, %d" % 
              (spectra2[100], spectra2[101], spectra2[102], spectra2[103], spectra2[104]))
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): dark_correct_spectrum1 / %d = %s" % (errorCode, errorMsg))

    try:
        print("")
        print("darkSpectrumCorrection(): get_dark_corrected_spectrum2()")
        if edcSupported:
            print("darkSpectrumCorrection(): EDC enabled ====> ********* expecting EXCEPTION!")
        spectra2 = od.get_dark_corrected_spectrum2()
        print("darkSpectrumCorrection(): dark correction (minus 100) =  %d, %d, %d, %d, %d" % 
              (spectra2[100], spectra2[101], spectra2[102], spectra2[103], spectra2[104]))
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): get_dark_corrected_spectrum2 / %d = %s" % (errorCode, errorMsg))

    try:
        # Test for empty list
        print("")
        print("darkSpectrumCorrection(): get_dark_corrected_spectrum2(DARK_EMPTY, ILLUMINATED) ====> ********* expecting EXCEPTION!")
        illuminatedSpectrum = od.get_formatted_spectrum()
        spectra2 = od.dark_correct_spectrum2([], illuminatedSpectrum)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): dark_correct_spectrum2 / %d = %s" % (errorCode, errorMsg))

    try:
        # Test for empty list
        print("")
        print("darkSpectrumCorrection(): get_dark_corrected_spectrum2(DARK, ILLUMINATED_EMPTY) ====> ********* expecting EXCEPTION!")
        spectra2 = od.dark_correct_spectrum2(darkSpectrum2, [])
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): dark_correct_spectrum2 / %d = %s" % (errorCode, errorMsg))


    if allFunctionTest:
        try:
            # Potential double correction here. OcenDirect don't know if the passed illuminated spectra was already corrected or not.
            print("")
            print("darkSpectrumCorrection(): get_dark_corrected_spectrum2(DARK, ILLUMINATED)")
            illuminatedSpectrum = od.get_formatted_spectrum()
            spectra2 = od.dark_correct_spectrum2(darkSpectrum2, illuminatedSpectrum)
            print("darkSpectrumCorrection(): illuminatedSpectrum         =  %d, %d, %d, %d, %d" % 
                  (illuminatedSpectrum[100], illuminatedSpectrum[101], illuminatedSpectrum[102],
                   illuminatedSpectrum[103], illuminatedSpectrum[104]))
            print("darkSpectrumCorrection(): dark correction (minus 200) =  %d, %d, %d, %d, %d" % 
                  (spectra2[100], spectra2[101], spectra2[102], spectra2[103], spectra2[104]))
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("darkSpectrumCorrection(device): dark_correct_spectrum2 / %d = %s" % (errorCode, errorMsg))

    try:
        print("")
        print("darkSpectrumCorrection(): get_nonlinearity_corrected_spectrum1(DARK_EMPTY) ====> ********* expecting EXCEPTION!")

        spectra2 = od.get_nonlinearity_corrected_spectrum1([])
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): get_nonlinearity_corrected_spectrum1 / %d = %s" % (errorCode, errorMsg))

    try:
        print("")
        print("darkSpectrumCorrection(): get_nonlinearity_corrected_spectrum1(DARK)")
        if edcSupported:
            print("darkSpectrumCorrection(): EDC enabled ====> ********* expecting EXCEPTION!")

        spectra2 = od.get_nonlinearity_corrected_spectrum1(darkSpectrum2)
        print("darkSpectrumCorrection(): nonlinearity correction (minus 200) =  %.3f, %.3f, %.3f, %.3f, %.3f" % 
              (spectra2[100], spectra2[101], spectra2[102], spectra2[103], spectra2[104]))
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): get_nonlinearity_corrected_spectrum1 / %d = %s" % (errorCode, errorMsg))

    try:
        print("")
        print("darkSpectrumCorrection(): nonlinearity_correct_spectrum1(EMPTY_ILLUMINATED) ====> ********* expecting EXCEPTION!")

        spectra2 = od.nonlinearity_correct_spectrum1([])
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): nonlinearity_correct_spectrum1 / %d = %s" % (errorCode, errorMsg))

    try:
        print("")
        print("darkSpectrumCorrection(): nonlinearity_correct_spectrum1(ILLUMINATED)")
        if edcSupported:
            print("darkSpectrumCorrection(): EDC enabled ====> ********* expecting EXCEPTION!")

        illuminatedSpectrum = od.get_formatted_spectrum()
        spectra2 = od.nonlinearity_correct_spectrum1(illuminatedSpectrum)
        print("darkSpectrumCorrection(): illuminatedSpectrum                 =  %d, %d, %d, %d, %d" % 
              (illuminatedSpectrum[100], illuminatedSpectrum[101], illuminatedSpectrum[102],
               illuminatedSpectrum[103], illuminatedSpectrum[104]))
        print("darkSpectrumCorrection(): nonlinearity correction (minus 100) =  %.3f, %.3f, %.3f, %.3f, %.3f" % 
              (spectra2[100], spectra2[101], spectra2[102], spectra2[103], spectra2[104]))
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): nonlinearity_correct_spectrum1 / %d = %s" % (errorCode, errorMsg))

    try:
        print("")
        print("darkSpectrumCorrection(): get_nonlinearity_corrected_spectrum2")
        if edcSupported:
            print("darkSpectrumCorrection(): EDC enabled ====> ********* expecting EXCEPTION!")

        spectra2 = od.get_nonlinearity_corrected_spectrum2()
        print("darkSpectrumCorrection(): nonlinearity correction (minus 100) = %.3f, %.3f, %.3f, %.3f, %.3f" % 
              (spectra2[100], spectra2[101], spectra2[102], spectra2[103], spectra2[104]))
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): get_nonlinearity_corrected_spectrum2 / %d = %s" % (errorCode, errorMsg))

    try:
        # Test for empty list
        print("")
        print("darkSpectrumCorrection(): nonlinearity_correct_spectrum2(EMPTY_DARK, ILLUMINATED) ====> ********* expecting EXCEPTION!")
        illuminatedSpectrum = od.get_formatted_spectrum()
        spectra2 = od.nonlinearity_correct_spectrum2([], illuminatedSpectrum)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): nonlinearity_correct_spectrum2 / %d = %s" % (errorCode, errorMsg))

    try:
        # Test for empty list
        print("")
        print("darkSpectrumCorrection(): nonlinearity_correct_spectrum2(DARK, EMPTY_ILLUMINATED) ====> ********* expecting EXCEPTION!")
        spectra2 = od.nonlinearity_correct_spectrum2(darkSpectrum2, [])
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): nonlinearity_correct_spectrum2 / %d = %s" % (errorCode, errorMsg))

    if allFunctionTest:
        try:
            # Potential double correction here. OcenDirect don't know if the passed illuminated spectra was already corrected or not.
            print("")
            print("darkSpectrumCorrection(): nonlinearity_correct_spectrum2(DARK, ILLUMINATED)")
            illuminatedSpectrum = od.get_formatted_spectrum()
            spectra2 = od.nonlinearity_correct_spectrum2(darkSpectrum2, illuminatedSpectrum)
            print("darkSpectrumCorrection(): illuminatedSpectrum                 =  %d, %d, %d, %d, %d" % 
                  (illuminatedSpectrum[100], illuminatedSpectrum[101], illuminatedSpectrum[102],
                   illuminatedSpectrum[103], illuminatedSpectrum[104]))
            print("darkSpectrumCorrection(): nonlinearity correction (minus 200) =  %.3f, %.3f, %.3f, %.3f, %.3f" % 
                  (spectra2[100], spectra2[101], spectra2[102], spectra2[103], spectra2[104]))

        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("darkSpectrumCorrection(device): nonlinearity_correct_spectrum2 / %d = %s" % (errorCode, errorMsg))

    print("")


def darkSpectrumCorrection(od: LighthouseAPI, id: int):
    edcSupported = False
    try:
        edcSupported = od.get_electric_dark_correction_usage()
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("darkSpectrumCorrection(device): get_electric_dark_correction_usage / %d = %s" % (errorCode, errorMsg))
    darkSpectrumCorrection2(device, True)

    if edcSupported:
        print("")
        print("-------------------------------------------------------------------------------------")
        print("Disable EDC/NLC")

        try:
            od.set_electric_dark_correction_usage(False)
            od.set_nonlinearity_correction_usage(False)
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("darkSpectrumCorrection(device): set_electric_dark_correction_usage / %d = %s" % (errorCode, errorMsg))

        print("")
        darkSpectrumCorrection2(device, False)

def edcNLCFlagVerification(od: LighthouseAPI, id: int):
    print("")
    try:
        flagList = [True, False, True]

        print("")
        for value in flagList:
            print("edcNLCFlagVerification():  set_electric_dark_correction_usage(%s)" % (value), flush=True)
            od.set_electric_dark_correction_usage(value)
            print("edcNLCFlagVerification():  set_nonlinearity_correction_usage(%s)" % (value), flush=True)
            od.set_nonlinearity_correction_usage(value)
            print("edcNLCFlagVerification():  set_electric_dark_running_average_usage(%s)" % (value), flush=True)

            retValue1 = od.get_electric_dark_correction_usage()
            retValue2 = od.get_nonlinearity_correction_usage()

            print("edcNLCFlagVerification():  get_electric_dark_correction_usage()      =  %s" % (retValue1), flush=True)
            print("edcNLCFlagVerification():  get_nonlinearity_correction_usage()       =  %s" % (retValue2), flush=True)
            print("")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("edcNLCFlagVerification(device): exception / %d = %s" % (errorCode, errorMsg))

def edcNLCReadSpectra(od: LighthouseAPI, id: int, edcFlag, nlcFlag):
    print("")
    print("edcNLCReadSpectra(): edcFlag =  %s" % edcFlag)
    print("edcNLCReadSpectra(): nlcFlag =  %s" % nlcFlag)

    try:
        #If the device dont support EDC correction but you try to enable it then OceanDirect will
        #throw an exception. The following devices dont have electric dark pixels:
        # -NirQuest-256
        # -NirQuest-512
        # -Ocean ST (STS3)
        # -Ocean FX

        od.set_electric_dark_correction_usage(edcFlag)
        od.set_nonlinearity_correction_usage(nlcFlag)
        get_spec_formatted(device, 1, 100000, "sr2_boxcar0.txt", False)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("edcNLCReadSpectra(device): set_electric_dark_correction_usage / %d = %s" % (errorCode, errorMsg))

def lamp(od: LighthouseAPI, id: int):
    print("")
    try:
        print("lamp(): lamp ON =  %s" % od.get_lamp_state(id))
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("lamp(device): get_lamp_state / %d = %s" % (errorCode, errorMsg))

    lampState = [True, False, True, False]
    for state in lampState:
        try:
            od.set_lamp_state(id, state)
            print("lamp(): set lamp ON =  %s" % state)
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("lamp(device): set_enable_lamp / %d = %s" % (errorCode, errorMsg))

        try:
            print("lamp(): get lamp ON =  %s" % od.get_lamp_state(id))
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("lamp(device): get_lamp_state / %d = %s" % (errorCode, errorMsg))

    print("")

def obp2SpectraScanAveraging(od: LighthouseAPI, id: int):
    #let's use immediate electric dark corrections
    #od.set_electric_dark_running_average_usage(False)
    od.set_electric_dark_correction_usage(False)
    od.set_nonlinearity_correction_usage(False)
    scanToAverageBoxcar(device, 1, 0)
    get_spec_formatted(device, 5, 100000, "sr4_100ms_ave1__edc_false_nlc_false.txt", True)

    od.set_electric_dark_correction_usage(True)
    od.set_nonlinearity_correction_usage(False)
    get_spec_formatted(device, 5, 100000, "sr4_100ms_ave1__edc_true_nlc_false.txt", True)

    od.set_electric_dark_correction_usage(True)
    od.set_nonlinearity_correction_usage(True)
    get_spec_formatted(device, 5, 100000, "sr4_100ms_ave1__edc_true_nlc_true.txt", True)

    od.set_electric_dark_correction_usage(False)
    od.set_nonlinearity_correction_usage(False)
    scanToAverageBoxcar(device, 25, 0)
    get_spec_formatted(device, 5, 100000, "sr4_100ms_ave25__edc_false_nlc_false.txt", True)

    od.set_electric_dark_correction_usage(True)
    od.set_nonlinearity_correction_usage(False)
    get_spec_formatted(device, 5, 100000, "sr4_100ms_ave25__edc_true_nlc_false.txt", True)

    od.set_electric_dark_correction_usage(True)
    od.set_nonlinearity_correction_usage(True)
    get_spec_formatted(device, 5, 100000, "sr4_100ms_ave25__edc_true_nlc_true.txt", True)



def read_gpio_direction(od: LighthouseAPI, id: int, pin_count: int):
    try:
        for i in range(pin_count):
            value = od.gpio_get_output_enable1(i)
            print("pin #%s =  %d" % (i, value) )
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("read_gpio_direction(): set/get / %d = %s" % (errorCode, errorMsg)) 

def set_gpio_direction(od: LighthouseAPI, id: int, pin_count: int, isOutput: bool):
    try:
        for i in range(pin_count):
            od.gpio_set_output_enable1(i, isOutput)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("read_gpio_direction(): set/get / %d = %s" % (errorCode, errorMsg)) 

def gpio_direction(od: LighthouseAPI, id: int, pin_count: int):
    #read current pin direction
    print("Reading GPIO Pin Direction (1=output, 0=input)")
    read_gpio_direction(device, pin_count)

    #set it all to 0=input
    print("\n")
    print("Setting all GPIO Pin to 0=input")
    set_gpio_direction(device, pin_count, False)

    #read pin direction - all should be 0=input
    print("\n")
    print("Reading all GPIO Pin - expecting all 0=input")
    read_gpio_direction(device, pin_count)

    #set it all to 1=output
    print("\n")
    print("Setting all GPIO Pin to 1=output")
    set_gpio_direction(device, pin_count, True)

    #read pin direction - all should be 1=output
    print("\n")
    print("Reading all GPIO Pin - expecting all 1=output")
    read_gpio_direction(device, pin_count)

def get_gpio_value(od: LighthouseAPI, id: int, pin_count: int):
    try:
        for i in range(pin_count):
            value =  od.gpio_get_value1(i)
            print("pin #%d =  %s" % (i, value))
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("get_gpio_value(): set/get / %d = %s" % (errorCode, errorMsg)) 

def set_gpio_value(od: LighthouseAPI, id: int, pin_count: int, isHigh: bool):
    try:
        for i in range(pin_count):
            od.gpio_set_value1(i, isHigh)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("set_gpio_value(): set/get / %d = %s" % (errorCode, errorMsg)) 

def printBits(pin_count: int, bitMask: int):
    for i in range(pin_count):
        value = (bitMask & 1) != 0
        bitMask = bitMask >> 1
        print("pin #%d =  %s" % (i, value))


def gpio_value(od: LighthouseAPI, id: int, pin_count: int):
    print("\n")
    print("Setting all GPIO Alternate Pin to 0=gpio pin")
    set_gpio_alternate(device, pin_count, False)

    print("\n")
    print("Setting all GPIO Pin Direction to 1=output")
    set_gpio_direction(device, pin_count, True)
    #print("Setting all GPIO Pin to 0=input");
    #set_gpio_direction(device, pin_count, False);

    #set it all to 1=high
    print("\n")
    print("Setting all GPIO Pin Value to 1=high")
    set_gpio_value(device, pin_count, True)

    #read pin direction - all should be 1=high
    print("\n")
    print("Reading all GPIO Pin Value - expecting all 1=high")
    get_gpio_value(device, pin_count)

    #set it all to 0=low
    print("\n")
    print("Setting all GPIO Pin Value to 0=low")
    set_gpio_value(device, pin_count, False)

    #read pin direction - all should be 1=high
    print("\n")
    print("Reading all GPIO Pin Value - expecting all 0=low")
    get_gpio_value(device, pin_count)


def shutter(dod: LighthouseAPI, id: int):
    #shutterState = [True, False, True, False]
    #for state in shutterState:
    #    od.set_shutter_open(state)
    #    print("shutter(): set shutter state = %s" % state)
    #    currentState = od.get_shutter_state()
    #    print("shutter(): get shutter state = %s \n" % currentState)
    #    time.sleep(2)

    try:
        currentState = od.get_shutter_state()
        print("shutter(): get shutter state = %s \n" % currentState)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("shutter(): get_shutter_state {} = {}".format(errorCode, errorMsg)) 


def resetDevice(dod: LighthouseAPI, id: int, probeUSB: bool):
    for i in range(3):
        print('resetDevice(): resetting device')
        try:
            od.reset_device()
            print('resetDevice(): resetting device done!')
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("resetDevice(): set {} = {}".format(errorCode, errorMsg)) 

        try:
            od.close_device()
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("resetDevice(): set {} = {}".format(errorCode, errorMsg)) 

        time.sleep(10)
        device_count = 0
        if probeUSB:
            device_count = od.find_usb_devices()
        else:
            device_count = od.find_devices()

        print("resetDevice(): total Device =  %d" % device_count)

        if device_count == 0:
            print('resetDevice(): No device found!')
        else:
            try:
                deviceIds = od.get_device_ids()

                print('deviceIds =  ', deviceIds)
                device = od.open_device(deviceIds[0])
                serialNumber = od.get_serial_number()
                print("resetDevice(): serial Number: %s \n" % serialNumber)

                get_spec_formatted(device, 10, 100000, "sr4_100ms_ave1.txt", False)

                if i == 2:
                    od.close_device(deviceIds[0])
            except OceanDirectError as err:
                [errorCode, errorMsg] = err.get_error_details()
                print("resetDevice(): set {} = {}".format(errorCode, errorMsg)) 

def integrationTimeTest(od: LighthouseAPI, id: int) -> None:
    
    startTime = datetime.now()
    od.set_integration_time(20000)
    endTime = datetime.now()
    
    delta = endTime - startTime
    print("integrationTimeTest(): set integration time = 20000us")
    print("integrationTimeTest(): start                = %s" % startTime )
    print("integrationTimeTest(): end                  = %s" % endTime )
    print("integrationTimeTest(): duration             = %dus \n" % delta.microseconds )


    startTime = datetime.now()
    od.set_trigger_mode(1)
    endTime = datetime.now()
    print("integrationTimeTest(): set trigger mode = 1")
    print("integrationTimeTest(): start                = %s" % startTime )
    print("integrationTimeTest(): end                  = %s" % endTime )
    print("integrationTimeTest(): duration             = %dus" % delta.microseconds )


def manualBoxcarCorrection(od: LighthouseAPI, id: int, spectraCount: int)->None:
    try:
        od.set_electric_dark_correction_usage(False)
        od.set_nonlinearity_correction_usage(False)
        od.set_integration_time(200000);
        print("[START] Reading spectra for dev s/n = %s" % serialNumber, flush=True)

        for i in range(spectraCount):
            spectra = od.get_formatted_spectrum()
            spectraOrig = spectra.copy()
            print("Before boxcar correction: %d, %d, %d, %d, %d, %d, %d, %d" % (spectraOrig[200], spectraOrig[201],
                  spectraOrig[202], spectraOrig[203], spectraOrig[204],
                  spectraOrig[205], spectraOrig[206], spectraOrig[207]), flush=True)

            try:
                spectra = od.boxcar_correct_spectrum(spectra, 2)
                print("After boxcar correcton  : %d, %d, %d, %d, %d, %d, %d, %d \n" % (spectra[200], spectra[201],
                      spectra[202], spectra[203], spectra[204], spectra[205], spectra[206], spectra[207]), flush=True)
            except OceanDirectError as e:
                [errorCode, errorMsg] = e.get_error_details()
                print("manualBoxcarCorrection(): ERROR with code/msg, %d = %s ************" % (errorCode, errorMsg))
    except OceanDirectError as e:
        [errorCode, errorMsg] = e.get_error_details()
        print("manualBoxcarCorrection(): ERROR with code/msg, %d = %s ************" % (errorCode, errorMsg))
    print("")


def obp2NetworkConfiguration(od: LighthouseAPI, id: int)->None:
    #True means use static ip
    ipAssignedModeList = [True, False, True, False]
    for value in ipAssignedModeList:
        try:
            print("set_ip_address_assigned_mode() =  %s" % value)
            od.set_ip_address_assigned_mode(value)
        except OceanDirectError as err:
            [errorCode, errorMsg] = err.get_error_details()
            print("obp2NetworkConfiguration(): set_ip_address_assigned_mode code/msg, %d = %s" % (errorCode, errorMsg))

        try:
            retval = od.get_ip_address_assigned_mode()
            print("get_ip_address_assigned_mode() =  %s" % retval)
        except OceanDirectError as err:
            print("obp2NetworkConfiguration(): get_ip_address_assigned_mode code/msg, %d = %s" % (errorCode, errorMsg))

    #try:
    #    ipv4Address    = [192, 168, 50, 178]
    #    subnetMask     = [255, 255, 255, 0] 
    #    defaultGateway = [192, 168, 50, 1]
    #    dnsServer      = [192, 168, 50, 254]

    #    print("")
    #    od.set_manual_network_configuration(ipv4Address, subnetMask, defaultGateway, dnsServer)
    #    print("obp2NetworkConfiguration(): set_manual_network_configuration()")
    #    print("ipv4Address    =  %s" % ".".join(list(map(str, ipv4Address))) )
    #    print("subnetMask     =  %s" % ".".join(list(map(str, subnetMask))) )
    #    print("defaultGateway =  %s" % ".".join(list(map(str, defaultGateway))) )
    #    print("dnsServer      =  %s" % ".".join(list(map(str, dnsServer))) )
    #    print("")
    #except OceanDirectError as err:
    #    [errorCode, errorMsg] = err.get_error_details()
    #    print("obp2NetworkConfiguration(): set_manual_network_configuration code/msg, %d = %s" % (errorCode, errorMsg))

    try:
        (ipv4Address, subnetMask, defaultGateway, dnsServer) = od.get_manual_network_configuration()
        print("")
        print("obp2NetworkConfiguration(): get_manual_network_configuration()")
        print("ipv4Address    =  %s" % ".".join(list(map(str, ipv4Address))) )
        print("subnetMask     =  %s" % ".".join(list(map(str, subnetMask))) )
        print("defaultGateway =  %s" % ".".join(list(map(str, defaultGateway))) )
        print("dnsServer      =  %s" % ".".join(list(map(str, dnsServer))) )
        print("")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("obp2NetworkConfiguration(): get_manual_network_configuration code/msg, %d = %s" % (errorCode, errorMsg))

    try:
        (manualAssignment, ipv4Address, subnetMask, defaultGateway, dnsServer) = od.get_network_configuration()
        print("")
        print("obp2NetworkConfiguration(): get_network_configuration()")
        print("manualAssignment  =  %s" % manualAssignment)
        print("ipv4Address       =  %s" % ".".join(list(map(str, ipv4Address))) )
        print("subnetMask        =  %s" % ".".join(list(map(str, subnetMask))) )
        print("defaultGateway    =  %s" % ".".join(list(map(str, defaultGateway))) )
        print("dnsServer         =  %s" % ".".join(list(map(str, dnsServer))) )
        print("")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("obp2NetworkConfiguration(): get_network_configuration code/msg, %d = %s" % (errorCode, errorMsg))

    #print("---------------------------------------------------------")
    #ipAssignedModeList = [False, True, False, True]
    #for value in ipAssignedModeList:
    #    try:
    #        od.set_ip_address_assigned_mode(value)
    #        print("set_ip_address_assigned_mode()                 =  %s" % value)

    #        retval = od.get_ip_address_assigned_mode()
    #        print("get_ip_address_assigned_mode()                 =  %s" % retval)

    #        (manualAssignment, ipv4Address, subnetMask, defaultGateway, dnsServer) = od.get_network_configuration()
    #        print("get_network_configuration(), manualAssignment  =  %s" % manualAssignment)
    #        print("")
    #    except OceanDirectError as err:
    #        print("obp2NetworkConfiguration(): get_network_configuration {} = {}".format(errorCode, errorMsg)) 



#----------------------------------------------------------------------------------------
# Main program starts here :-P
#----------------------------------------------------------------------------------------
if __name__ == '__main__':
    od = LighthouseAPI()

    (major, minor, point) = od.get_api_version_numbers()
    print("API Version   : %d.%d.%d " % (major, minor, point))

    #manually add network devices
    #od.add_network_device("192.168.50.170", "OceanSR6")
    #device_count = 1

    #NOTE:
    #look for network and usb devices. This probing is much slower! Put the
    #function call within the loop and add some delay too
    #device_count = od.find_devices()
    #for i in range(1):
    #    device_count = od.find_devices()

    #There are 3 network devices. We will keep probing until we sees them all.
    #while True:
    #    device_count = od.find_devices()
    #    print("Network Device Count =  %d" % device_count)
    #    if device_count == 3:
    #        print("...we found all 3 units...breaking loop.\n")
    #        break
    #    else:
    #        print("...sleeping and try again\n")
    #        time.sleep(0.3)

    #look for usb devices only.
    device_count = od.find_usb_devices()
    print("Total Device  :  %d" % device_count)

    #device_count = 0
    if device_count == 0:
        print("No device found.")
    else:
        networkIds = od.get_network_device_ids()
        print("Network Device ids: ", networkIds)

        device_ids = od.get_device_ids()
        print("Device ids    : ", device_ids)
        print("\n")

        for id in device_ids:
            print("**********************************************")
            print("Device ID    : %d   " % id)

            try:
                od.open_device(id)
            except OceanDirectError as err:
                [errorCode, errorMsg] = err.get_error_details()
                print("main(): open_device() %d = %s" % (errorCode, errorMsg))

            serialNumber = od.get_serial_number(id)
            print("Serial Number: %s \n" % serialNumber)

            revision(od, id)

            #value = od.get_scans_to_average();
            #print("scanToAverageWithMinimumAveragingTime(): cur scans_to_average =  %d" % value)

            #manualBoxcarCorrection(device, 2)
            #serialNumberTest(od, id)           #USB4000/NirQuest256/HR2000+ES/HR4000/NR      ==> OK
            #integrationTime(od, id, 15000)     #USB4000/NirQuest256/HR2000+ES/HR4000/HR6/NR  ==> OK   has ERROR
            
            #Issue: REPORTED BY CHINA TEAM
            #Depending on the FW version, the lighthouse units will take around 100ms just to set the integration time or trigger mode. However
            #when using an older FW, we don't have this issue. This is more on FW issue as changing FPGA doesn't have any effect.
            #integrationTimeTest(device).
            
            #1,2,3 - these are supported lighthouse trigger modes.
            #triggerMode(od, id, [0,1,2])       #Comm - SR6 - OK-TCP/IP4 (dynamic) Lighthouse
            #triggerMode(od, id, [0,1,2,3])     #MayaPro and Flame-S have the same command and trigger modes
                                                #NOTE: MayaPro has FW bug. Get trigger mode always returns 0.
                                                #      Flame-S works well.

            #resetDevice(od, id, True)          #NOTE: comment the close_device() call below.
            #resetDevice(od, id, False)         #Comm - SR6 - OK-TCP/IP4 (dynamic) Lighthouse

            #speedTestPerSecond(od, id, 3800)   #==> OK

            #feature_enabled(od, id)
            #spectraCorrection(od, id)

            #acquisitionDelay(od, id)          #Comm - SR6 - OK-TCP/IP4 (dynamic) Lighthouse
            #pixelInfo(od, id)                 #Comm - SR6 - OK-TCP/IP4 (dynamic) Lighthouse

            #scanToAverageWithMinimumAveragingTime(od, id)    #SR2 only
            #scanToAverageWithNoMinimumAveragingTime(od, id)  #NR ==> OK

            #get_spec_formatted(od, id, 10, 500000, "sr2_nlc_001.txt", False)  #Comm - SR6 - OK-TCP/IP4 (dynamic) Lighthouse


            #shutter(od, id)                          #OceanNR only so far


            #edcNLCReadSpectra(od, id, False, False)  #USB4000, NirQuest256, HR4000
            #edcNLCReadSpectra(od, id, False, True)
            #edcNLCReadSpectra(od, id, True, False)
            #edcNLCReadSpectra(od, id, True, True)


            #obp2SpectraScanAveraging(device)
            #get_spec_formatted(od, id, 20, 100000, "sr4_100ms_ave1.txt", False)

            #scanToAverageBoxcar(od, id, 4, 0)
            #get_spec_formatted(od, id, 5, 100000, "sr4_100ms_ave1.txt", True)

            #scanToAverageBoxcar(od, id, 25, 0)
            #get_spec_formatted(od, id, 5, 100000, "sr4_100ms_ave25.txt", True)


            #get_spec_raw_with_meta(od, id, 5, 100000, "sr2_boxcar4.txt", False)    #OK-TCP/IP4 Lighthouse
            #scanToAverageWithMinimumAveragingTime(od, id)   # TODO: 5/24/2022 - waiting for Alex/Greg reply. 
                                                             #       Does SR4 have min averaging integration time.
            #scanToAverageBoxcar(od, id, 1, 0)
            #print("*********************************")
            #scanToAverageBoxcar(od, id, 4, 0)
            #print("*********************************")
            #scanToAverageBoxcar(od, id, 10, 0)

            #--------------------------------------
            #NOTE:
            #For QEPro, disable EDC/NLC correction since it seems that my unit has bug. The electric dark 
            #pixel count is big which resulted the in 0 value after EDC.
            #--------------------------------------
            #od.set_electric_dark_correction_usage(False)  #  ==> OK
            #od.set_nonlinearity_correction_usage(False)   #  ==> OK
            #get_spec_formatted(od, id, 10, 100000, "sr2_boxcar4.txt", False)
            #get_spec_raw_with_meta(od, id, 2, 100000, "sr2_boxcar4.txt", False) ==> OK

            #--------------------------------------
            #The following devices has no EDC and will throw and exception.
            # STS3, FX, NIRQuest-256/512
            #--------------------------------------
            #edcNLCFlagVerification(od, id)
            #edcNLPixels(od, id)                #USB4000/NirQuest256(not supported), HR2000+ES, HR4000

            #wavelength(od, id)                  #Comm - SR6 - OK-TCP/IP4 (dynamic) Lighthouse
            #singleStrobe(od, id)               #Comm - SR6 - OK-TCP/IP4 (dynamic) Lighthouse
            #continuousStrobe(od, id)           #Comm - SR6 - OK-TCP/IP4 (dynamic) Lighthouse

            #--------------------------------------
            #Set and Get data command won't work for:
            #   NIRQuest256, USB4000, Flame-T, HR2000+ES
            #
            #Possible FW/FPGA bug and this issue is already forwarded to EE team (Alex). 
            #--------------------------------------
            gpio(od, id)                       #USB4000/HR4000/HR6/NR  ==> #OK-TCP/IP4 Lighthouse
            #gpioOVRead(od, id)

           
            #NOTE: moved to Admin installer
            #temperature(od, id)                #USB4000/NirQuest256/HR2000+ES/HR4000/HR6(ERROR)   ==> OK
            
            #thermoElectric(od, id)             #NR, QEPro  ==> OK

            #usbEndPoints(od, id)               #USB4000/NirQuest256/HR2000+ES/HR4000/HR6/NR       ==> OK
            #deviceInfo(od, id)                 #USB4000/NirQuest256/HR2000+ES/HR4000 = (N/A), NR  ==> OK
            #wavelengthCoefficients(od, id)     #USB4000/HR2000+ES/HR4000/NR  ==> OK
            #nonlinearityCoefficients(od, id)   #USB4000/HR2000+ES/HR4000/NR  ==> OK

            #lamp(od, id)
            #ledState(od, id)                   #USB4000 (N/A)/HR4000, NirQuest256 (Not Supported), HR6/NR    ==> OK
            #deviceAlias(od, id)                #USB4000/NirQuest256/HR2000+ES/HR4000/HR4000 = (N/A), HR6/NR  ==> OK
            #userString(od, id)                 #USB4000/NirQuest256/HR2000+ES/HR4000/HR4000 = (N/A), HR6/NR  ==> OK

            #--------------------------------------
            #The following devices will throw an exception because 
            #they don't have electric dark pixels.
            #   NIRQuest256/512, Ocean FX, Ocean ST(STS3)
            #--------------------------------------
            #electricNonlinearityCorrection(device)  #USB4000, HR2000+ES
            #autoNulling(od, id)                     #USB4000/NirQuest256/HR2000+ES/HR4000 = (N/A), NR ==> OK
            #baudRate(od, id)                        #USB4000/NirQuest256/HR2000+ES/HR4000/HR6/NR = (N/A)
            #darkSpectrumCorrection(device)          #USB4000/NirQuest256/HR2000+ES/HR4000

            #obp2NetworkConfiguration(device)

            print("\n[END] Closing device [%s]!" % serialNumber)
            print("")
            od.close_device(id)
            
    od.shutdown()
    print("**** exiting program ****")






#----------------------------------------------------------------------------------------
# Lighthouse Comm testing using dynamic ip address
#----------------------------------------------------------------------------------------
if __name__ == '__main__2222':
    od = LighthouseAPI()
    (major, minor, point) = od.get_api_version_numbers()
    print("API Version   : %d.%d.%d " % (major, minor, point))

    #manually add network devices
    id = od.add_network_device("192.168.50.200", "OceanHR2")
    print("Network device id:  %d" % id)

    #NOTE:
    #look for network and usb devices. This probing is much slower! Put the
    #function call within the loop and add some delay too
    #device_count = od.find_devices()
    #device_count = od.find_usb_devices()
    #for i in range(1):
    #    device_count = od.find_devices()

    #There are 3 network devices. We will keep probing until we sees them all.
    #while True:
    #    device_count = od.find_devices()
    #    print("Network Device Count =  %d" % device_count)
    #    if device_count == 3:
    #        print("...we found all 3 units...breaking loop.\n")
    #        break
    #    else:
    #        print("...sleeping and try again\n")
    #        time.sleep(0.3)


    device_count = 1
    print("Total Device  :  %d" % device_count)

    
    if device_count == 0:
        print("No device found.")
    else:
        networkIds = od.get_network_device_ids()
        print("Network Device ids: ", networkIds)

        device_ids = od.get_device_ids()
        print("All Device ids    : ", device_ids)
        print("\n")

        for id in device_ids:
            print("**********************************************")
            print("Device ID    : %d   " % id)

            try:
                device = od.open_device(id)
            except OceanDirectError as err:
                [errorCode, errorMsg] = err.get_error_details()
                print("main(): open_device() %d = %s" % (errorCode, errorMsg))

            serialNumber = od.get_serial_number()
            print("Serial Number: %s \n" % serialNumber)

            revision(device)

            #manualBoxcarCorrection(device, 2)
            #serialNumberTest(od, device)       #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #integrationTime(device, 15000)     #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            
            #Issue: REPORTED BY CHINA TEAM
            #Depending on the FW version, the lighthouse units will take around 100ms just to set the integration time or trigger mode. However
            #when using an older FW, we don't have this issue. This is more on FW issue as changing FPGA doesn't have any effect.
            #integrationTimeTest(device).
            
            #1,2,3 - these are supported lighthouse trigger modes.
            #triggerMode(device, [0,1,2])       #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #resetDevice(device, False)         #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
                                                #NOTE: test HR4 with netgear. Device freeze, possible wifi interruption?

            #spectraCorrection(device)
            #acquisitionDelay(device)           #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #pixelInfo(device)                  #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            
            #obp2ExternalTriggerModeTest(device)

            #scanToAverageWithMinimumAveragingTime(device)     #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #scanToAverageWithNoMinimumAveragingTime(device)   #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
                                                               #NR ==> OK
            #get_spec_formatted(device, 10, 200000, "sr2_nlc_001.txt", False)  #Comm - SR6,SR4,HR4 - OK-TCP/IP4 (dynamic) Lighthouse
                                                               #HR4 - FW/FPGA get spectra command bug fixed in 2.0.7FW.


            #shutter(device)                          #Comm - (SR6,SR4,HR4,HR2) (not supported) - OK-TCP/IP4 (dynamic) Lighthouse

            #edcNLCReadSpectra(device, False, False)  #USB4000, NirQuest256, HR4000
            #edcNLCReadSpectra(device, False, True)
            #edcNLCReadSpectra(device, True, False)
            #edcNLCReadSpectra(device, True, True)

            #obp2SpectraScanAveraging(device)
            #get_spec_formatted(device, 100000000000, 100000, "sr4_100ms_ave1.txt", False)

            #scanToAverageBoxcar(device, 14, 4)                                   #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse 
            get_spec_formatted(device, 25, 100000, "sr4_100ms_ave1.txt", True)   #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse 
                                                                                  #HSAM - fixed on FW 2.0.7
                                                                                  #HR4  - fixed on FW 2.0.7. Need further testing.
            #get_spec_raw_with_meta(device, 5, 100000, "sr2_boxcar4.txt", False)  #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse 

            #scanToAverageBoxcar(device, 25, 0)
            #get_spec_formatted(device, 5, 100000, "sr4_100ms_ave25.txt", True)

            #scanToAverageWithMinimumAveragingTime(device)   # TODO: 5/24/2022 - waiting for Alex/Greg reply. 
                                                             # Does SR4 have min averaging integration time.
            #scanToAverageBoxcar(device, 1, 0)
            #print("*********************************")
            #scanToAverageBoxcar(device, 4, 0)
            #print("*********************************")
            #scanToAverageBoxcar(device, 10, 0)

            #get_spec_formatted(device, 10, 100000, "sr2_boxcar4.txt", False)
            #get_spec_raw_with_meta(device, 2, 100000, "sr2_boxcar4.txt", False) ==> OK
            #unformattedSpectra(device)

            #edcNLCFlagVerification(device)     #Comm - SR6(no EDP),SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #edcNLPixels(device)                #Comm - SR6(no EDP),SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #wavelength(device)                 #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #singleStrobe(device)               #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #continuousStrobe(device)           #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse

            #gpio(device)                       #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #thermoElectric(device)             #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse

            #temperature(device)                #NOTE: MOVED to admin
            #opticalBench(device)               #NOTE: MOVED to admin
            #irradCalibration(device)           #NOTE: MOVED to Admin

            #usbEndPoints(device)               #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #deviceInfo(device)                 #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #wavelengthCoefficients(device)     #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #nonlinearityCoefficients(device)   #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse

            #lamp(device)                       #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #lightSource(device)                #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #backToBackScan(device)             #Comm - (SR6,SR4,HR4,HR2) (not supported) - OK-TCP/IP4 (dynamic) Lighthouse
            #dataBuffer(device)                 #Comm - (SR6,SR4,HR4,HR2) (not supported) - OK-TCP/IP4 (dynamic) Lighthouse
            #dhcp(device)                       #Comm - (SR6,SR4,HR4,HR2) (not supported) - OK-TCP/IP4 (dynamic) Lighthouse
            #staticIPAddress(device)            

            #ledState(device)                   #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #deviceAlias(device)                #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #userString(device)                 #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse

            #electricNonlinearityCorrection(device)  #Comm - SR6(no EDP),SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #autoNulling(device)                     #Comm - SR6,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse
            #baudRate(device)                        #USB4000/NirQuest256/HR2000+ES/HR4000/HR6/NR = (N/A)
            #darkSpectrumCorrection(device)          #Comm - SR6,SR4,HR4,HR2 - OK-TCP/IP4 (dynamic) Lighthouse

            #networkConfiguration(device)            #Comm - (SR6,SR4,HR4,HR2) (not supported) - OK-TCP/IP4 (dynamic) Lighthouse
            #ethernet(device)                        #Comm - (SR6,HR4,SR4,HR2) (not supported) - OK-TCP/IP4 (dynamic) Lighthouse
            #ipAddress(device)                       #Comm - (SR6,SR4,HR4,HR2) (not supported) - OK-TCP/IP4 (dynamic) Lighthouse
            #setEthernetSettings(device, [10, 20, 30, 160], [10, 20, 30, 1])  #Comm - (SR6,SR4,HR4,HR2) (not supported) - OK-TCP/IP4 (dynamic) Lighthouse
            #obp2NetworkConfiguration(device)        #Comm - HR2 - OK-TCP/IP4 (dynamic) Lighthouse

            print("\n[END] Closing device [%s]!" % serialNumber)
            print("")
            od.close_device(id)
            
    od.shutdown()
    print("**** exiting program ****")


