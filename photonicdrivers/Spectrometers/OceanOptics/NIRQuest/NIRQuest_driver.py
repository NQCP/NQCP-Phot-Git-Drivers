# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 14:38:25 2024

@author: NQCPW
"""
import os
import sys
current_directory = os.path.dirname(__file__)
sys.path.insert(0, current_directory)

from oceandirect.od_logger import od_logger
from oceandirect.OceanDirectAPI import OceanDirectAPI, OceanDirectError
import numpy as np

class NIRQuest_driver():
    
    def __init__(self, integration_time_in_s = 1, num_averages = 1):
        self.logger = od_logger()
        self.od_api = OceanDirectAPI()
        self.device_ids = []
        self.device_count = 0
        self.num_averages = num_averages 
        self.integration_time_in_s = integration_time_in_s 

    def initialize_api(self):
        self.device_count = self.od_api.find_usb_devices()
        self.device_ids = self.od_api.get_device_ids()
        major, minor, point = self.od_api.get_api_version_numbers()
        print(f"API Version  : {major}.{minor}.{point}")
        print(f"Total Devices: {self.device_count}")
        
        if self.device_count == 0:
            print("No devices found.")
        else:
            print(f"Found {self.device_count} devices.")

    def get_spectrum_formatted(self, device):
        try:
            device.set_electric_dark_correction_usage(False)
            integration_time = self.integration_time_in_s 
            device.set_integration_time(int(integration_time * 1e6))

            print(f"Reading spectra for device s/n = {device.get_serial_number()}", flush=True)
            spectra = device.get_formatted_spectrum()
            wavelengths = device.get_wavelengths()
            return spectra
        except OceanDirectError as e:
            self.logger.error(e.get_error_details())
            return None, None

    def get_average_spectrum_formatted(self, device):
        """New version: Retrieves an averaged spectrum over `num_averages` readings."""
        try:
            device.set_electric_dark_correction_usage(False)
            integration_time = self.integration_time_in_s 
            device.set_integration_time(int(integration_time * 1e6))

            print(f"Averaging spectra for device s/n = {device.get_serial_number()}", flush=True)
            spectra = None
            for i in range(self.num_averages):  # Average over `num_averages` readings
                current_spectrum = device.get_formatted_spectrum()
                if spectra is None:
                    spectra = current_spectrum
                else:
                    spectra = [x + y for x, y in zip(spectra, current_spectrum)]
            # Average the accumulated spectra
            spectra = np.array(spectra)/ self.num_averages 
            return spectra
        except OceanDirectError as e:
            self.logger.error(e.get_error_details())
            return None
        
    def run(self, use_averaging=False):
        self.initialize_api()
        
        for device_id in self.device_ids:
            device = self.od_api.open_device(device_id)
            serial_number = device.get_serial_number()
            
            print(f"Device ID     : {device_id}")
            print(f"Serial Number : {serial_number}")
            
            if use_averaging:
                spectra = self.get_average_spectrum_formatted(device)
            else:
                spectra = self.get_spectrum_formatted(device)
                
            wavelengths = device.get_wavelengths() if spectra is not None else None
            
            print(f'Max counts: {np.max(spectra)}')
            print("Closing device.")
            self.od_api.close_device(device_id)
            
            return wavelengths, spectra

if __name__ == '__main__':
    
    spectrometer = NIRQuest_driver()
    
    x_data, y_data = spectrometer.run(use_averaging=False)
    
    import matplotlib.pyplot as plt
    
    plt.figure()
    plt.plot(x_data, y_data)
    plt.title('Acquired spectrum')
    plt.xlabel('Wavelength [nm]')
    plt.ylabel('Counts [a.u.]')
    plt.tight_layout()

