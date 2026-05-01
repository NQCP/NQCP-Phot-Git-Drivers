# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:58:47 2020

@author: Ocean Insight Inc.
"""

from ctypes.wintypes import LONG
from pickletools import long1
from oceandirect.od_logger import od_logger
from oceandirect.OceanDirectAPI import OceanDirectAPI, OceanDirectError, FeatureID, Spectrometer
import time

# create stream logger
logger = od_logger()
serialNumber = ""

def revision(device):
    try:
        fwVersion = device.Advanced.get_revision_firmware()
        print("revision(device): fwVersion   =  %s " % fwVersion)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("revision(device): get_revision_firmware() / %d = %s" % (errorCode, errorMsg))

    try:
        fpgaVersion = device.Advanced.get_revision_fpga()
        print("revision(device): fpgaVersion =  %s " % fpgaVersion)
        print("")
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("revision(device): get_revision_fpga() / %d = %s" % (errorCode, errorMsg))
    print("")


def setScanAverage(device, scanToAve):
    try:
        device.set_scans_to_average(scanToAve)
    except OceanDirectError as err:
        [errorCode, errorMsg] = err.get_error_details()
        print("setScanAverage(): ERROR with code/scanToAverage, %d = %s ************" % (errorCode, scanToAve))


def setIntegrationTime(device, intTimeUs):
    try:
        device.set_integration_time(intTimeUs)
    except OceanDirectError as e:
        [errorCode, errorMsg] = e.get_error_details()
        print("setIntegrationTime(): ERROR with code/set_integration_time(), %d = %s ************" % (errorCode, errorMsg))


def sr2ScanAveraging(device):
    minIntTime = device.get_minimum_integration_time()
    minAveIntTime = device.get_minimum_averaging_integration_time()
    maxIntTime = device.get_maximum_integration_time()
    intTime = device.get_integration_time()
    scanAve = device.get_scans_to_average()
        

    print("sr2ScanAveraging(): minIntTime    =  %d" % minIntTime)
    print("sr2ScanAveraging(): maxIntTime    =  %d" % maxIntTime)
    print("sr2ScanAveraging(): minAveIntTime =  %d" % minAveIntTime)
    print("sr2ScanAveraging(): intTime       =  %d" % intTime)
    print("sr2ScanAveraging(): get scans_to_average =  %d" % scanAve)
    print("")

    intTime = 205
    print("sr2ScanAveraging(): set intTime   =  %d / expecting no exception" % intTime, flush=True)
    setIntegrationTime(device, intTime)

    intTime = device.get_integration_time()
    print("sr2ScanAveraging(): get intTime   =  %d" % intTime, flush=True)

    scanAve = 8
    print("sr2ScanAveraging(): set scans_to_average   =  %d / expecting exception" % scanAve, flush=True)
    setScanAverage(device, scanAve)

    print("\n")
    scanAve = 1
    print("sr2ScanAveraging(): set scans_to_average   =  %d / expecting no exception" % scanAve, flush=True)
    setScanAverage(device, scanAve)


#----------------------------------------------------------------------------------------
# Main program starts here :-P
#----------------------------------------------------------------------------------------
if __name__ == '__main__':
    od = OceanDirectAPI()

    (major, minor, point) = od.get_api_version_numbers()
    print("API Version   : %d.%d.%d " % (major, minor, point))

    #look for usb devices only.
    device_count = od.find_usb_devices()

    print("Total Device  :  %d" % device_count)
    #device_count = 2

    if device_count == 0:
        print("No device found.")
    else:
        device_ids = od.get_device_ids()
        print("Device ids    : ", device_ids)
        print("\n")

        for id in device_ids:
            print("**********************************************")
            print("Device ID    : %d   " % id)

            device       = od.open_device(id)
            serialNumber = device.get_serial_number()
            print("Serial Number: %s \n" % serialNumber)

            revision(device)
            sr2ScanAveraging(device)

            print("\n[END] Closing device [%s]!" % serialNumber)
            print("")
            od.close_device(id)
            
    od.shutdown()
    print("**** exiting program ****")


