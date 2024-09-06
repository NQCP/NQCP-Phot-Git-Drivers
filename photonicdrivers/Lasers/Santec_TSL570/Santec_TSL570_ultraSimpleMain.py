# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 13:42:41 2024

@author: dtk791
"""

import os
import clr 
import sys


"""
This ulta_simple version is inspired by "Write your own script (Python)" from
Santec's GitHub page:  https://github.com/santec-corporation/Santec_USB_Control_Scripts
"""

# =============================================================================
# CONNECT TO SANTEC
# =============================================================================

# Checking and Accessing the DLL (Santec_FTDI) [make sure the DLLs are in the same directory as the script]
assembly_path = r".\dll_files"  # device-class path
sys.path.append(assembly_path)
ref = clr.AddReference(r"Santec_FTDI")

# Importing the main method from the DLL
import Santec_FTDI as ftdi

# Calling the FTD2xx_helper class from the Santec_FTDI dll. 
ftdi_class = ftdi.FTD2xx_helper

# ListDevices() returns the list of all Santec instruments
list_of_devices = ftdi_class.ListDevices()

for device in list_of_devices:    
  print('\nDetected Instruments:-')
  print(f'\nDevice Name: {device.Description},  Serial Number: {device.SerialNumber}')
  
# The serial number of the laser can be found in the tag, at the back of the laser box. 

serial_number = '24040112'

# Here parameter is the Serial number of the instrument in string format
santec = ftdi.FTD2xx_helper(serial_number)    

idn_query = santec.QueryIdn()
# Output: SANTEC INS-(ModelNumber), SerialNumber, VersionNumber
print('\n' + idn_query)

print('\n')
wav_query = santec.Query(':WAV?')
print(wav_query.rstrip('\r')+' m')



santec.CloseUsbConnection()

#%%
