# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:42:47 2024

@author: NQCPW
"""

from oceandirect.od_logger import od_logger
from oceandirect.OceanDirectAPI import OceanDirectAPI, OceanDirectError, Spectrometer, FeatureID

from time import sleep

logger = od_logger()


if __name__ == '__main__':
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
        
            
            print("SPECTROMETER feature supported  = %s" % device.is_feature_id_enabled(FeatureID.SPECTROMETER))
            print("THERMOELECTRIC feature supported  = %s" % device.is_feature_id_enabled(FeatureID.THERMOELECTRIC))
            print("IRRADIANCE_CAL feature supported  = %s" % device.is_feature_id_enabled(FeatureID.IRRADIANCE_CAL))
            print("EEPROM feature supported  = %s" % device.is_feature_id_enabled(FeatureID.EEPROM))
            print("STROBE_LAMP feature supported  = %s" % device.is_feature_id_enabled(FeatureID.STROBE_LAMP))
            print("WAVELENGTH_CAL feature supported  = %s" % device.is_feature_id_enabled(FeatureID.WAVELENGTH_CAL))
            print("NONLINEARITY_CAL feature supported  = %s" % device.is_feature_id_enabled(FeatureID.NONLINEARITY_CAL))
            print("STRAYLIGHT_CAL feature supported  = %s" % device.is_feature_id_enabled(FeatureID.STRAYLIGHT_CAL))
            print("RAW_BUS_ACCESS feature supported  = %s" % device.is_feature_id_enabled(FeatureID.RAW_BUS_ACCESS))
            print("CONTINUOUS_STROBE feature supported  = %s" % device.is_feature_id_enabled(FeatureID.CONTINUOUS_STROBE))
            print("LIGHT_SOURCE feature supported  = %s" % device.is_feature_id_enabled(FeatureID.LIGHT_SOURCE))
            print("TEMPERATURE feature supported  = %s" % device.is_feature_id_enabled(FeatureID.TEMPERATURE))
            
            print("OPTICAL_BENCH feature supported  = %s" % device.is_feature_id_enabled(FeatureID.OPTICAL_BENCH))
            print("REVISION feature supported  = %s" % device.is_feature_id_enabled(FeatureID.REVISION))
            print("PROCESSING feature supported  = %s" % device.is_feature_id_enabled(FeatureID.PROCESSING))
            print("DATA_BUFFER feature supported  = %s" % device.is_feature_id_enabled(FeatureID.DATA_BUFFER))
            print("ACQUISITION_DELAY feature supported  = %s" % device.is_feature_id_enabled(FeatureID.ACQUISITION_DELAY))
            print("PIXEL_BINNING feature supported  = %s" % device.is_feature_id_enabled(FeatureID.PIXEL_BINNING))
            print("GPIO feature supported  = %s" % device.is_feature_id_enabled(FeatureID.GPIO))
            print("SINGLE_STROBE feature supported  = %s" % device.is_feature_id_enabled(FeatureID.SINGLE_STROBE))
            print("QUERY_STATUS feature supported  = %s" % device.is_feature_id_enabled(FeatureID.QUERY_STATUS))
            print("BACK_TO_BACK feature supported  = %s" % device.is_feature_id_enabled(FeatureID.BACK_TO_BACK))
            print("LED_ACTIVITY feature supported  = %s" % device.is_feature_id_enabled(FeatureID.LED_ACTIVITY))
            print("TIME_META feature supported  = %s" % device.is_feature_id_enabled(FeatureID.TIME_META))
            
            print("DHCP feature supported  = %s" % device.is_feature_id_enabled(FeatureID.DHCP))
            print("IPV4_ADDRESS feature supported  = %s" % device.is_feature_id_enabled(FeatureID.IPV4_ADDRESS))
            print("PIXEL feature supported  = %s" % device.is_feature_id_enabled(FeatureID.PIXEL))
            print("AUTO_NULLING feature supported  = %s" % device.is_feature_id_enabled(FeatureID.AUTO_NULLING))
            print("USER_STRING feature supported  = %s" % device.is_feature_id_enabled(FeatureID.USER_STRING))
            print("DEVICE_INFORMATION feature supported  = %s" % device.is_feature_id_enabled(FeatureID.DEVICE_INFORMATION))
            print("DEVICE_ALIAS feature supported  = %s" % device.is_feature_id_enabled(FeatureID.DEVICE_ALIAS))
            print("SERIAL_PORT feature supported  = %s" % device.is_feature_id_enabled(FeatureID.SERIAL_PORT))
            print("SPECTRUM_ACQUISITION_CONTROL feature supported  = %s" % device.is_feature_id_enabled(FeatureID.SPECTRUM_ACQUISITION_CONTROL))
            print("NETWORK_CONFIGURATION feature supported  = %s" % device.is_feature_id_enabled(FeatureID.NETWORK_CONFIGURATION))
            print("ETHERNET feature supported  = %s" % device.is_feature_id_enabled(FeatureID.ETHERNET))
            print("SHUTTER feature supported  = %s" % device.is_feature_id_enabled(FeatureID.SHUTTER))
            print("HIGH_GAIN_MODE feature supported  = %s" % device.is_feature_id_enabled(FeatureID.HIGH_GAIN_MODE))
            
            
            print("\nClosing device!\n")
            
            od.close_device(id)

    print("**** exiting program ****")

