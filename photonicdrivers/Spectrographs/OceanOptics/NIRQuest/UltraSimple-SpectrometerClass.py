# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:42:47 2024

@author: NQCPW
"""

from oceandirect.od_logger import od_logger
from oceandirect.OceanDirectAPI import OceanDirectAPI, OceanDirectError, Spectrometer, FeatureID

from time import sleep

logger = od_logger()

def get_spec_formatted(device, sn):
    try:
        #device.set_electric_dark_correction_usage(False);
        #device.set_nonlinearity_correction_usage(False);

        integration_time = 0.1 #time in s
        device.set_integration_time(int(integration_time*1e6));

        print("Reading spectra for dev s/n = %s" % sn, flush=True)
        for i in range(1):
            spectra = device.get_formatted_spectrum()
            # print("spectra[100,200,300,400]: %d, %d, %d, %d" % (spectra[100], spectra[200], spectra[300], spectra[400]), flush=True)
    except OceanDirectError as e:
        logger.error(e.get_error_details())
    return spectra

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
            
            temp_C_before = device.Advanced.get_tec_temperature_degrees_C()
            # device.Advanced.set_temperature_setpoint_degrees_C(-10.0)
            # device.Advanced.set_tec_enable(True)
            
            # sleep(5)
            
            # temp_C_after = device.Advanced.get_tec_temperature_degrees_C()

            test_spectra = get_spec_formatted(device, serialNumber)
            test_wavelengths = device.get_wavelengths()
            
            supported = device.is_feature_id_enabled(FeatureID.THERMOELECTRIC)
            print("gpio(device): GPIO feature supported  = %s" % supported)
            
            # test = device.Advanced.is_light_source_enabled()
          
            
            print("Closing device!\n")
            od.close_device(id)

    print("**** exiting program ****")

import matplotlib.pyplot as plt


plt.close('all')

plt.figure()
plt.plot(test_wavelengths, test_spectra)
plt.xlabel('Wavelength [nm]')
plt.ylabel('Counts')

import pandas 

# df =  pandas.DataFrame({'Wavelength [nm]': test_wavelengths,
#               'Counts [#]': test_spectra})
# df.to_csv('NKT_off.csv', index=False)  

