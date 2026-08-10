from ctypes import *
import ctypes
import os
import time
import sys, getopt
from time import sleep

# Set the dll directory to the current directory
os.add_dll_directory(os.getcwd())
# Open the dll
vnx = cdll.VNX_atten64

# Set test mode to false
# This means that we will be using real devices
vnx.fnLDA_SetTestMode(False)

# Get the number of devices
devices_num = vnx.fnLDA_GetNumDevices()
# Create an array of device ids for connected devices
DeviceIDArray = c_int * devices_num
devices_list = DeviceIDArray()
# fill the array with the ID's of connected attenuators
vnx.fnLDA_GetDevInfo(devices_list)

if len(devices_list) > 0:
    # Select which device to use
    devid = 0
    if len(devices_list) == 1:
        devid = devices_list[0]
    else:
        while not devid in devices_list:
            print("Connected Devices:")
            for device in devices_list:
                print(f"\t({device}) {vnx.fnLDA_GetSerialNumber(device)}")
            try:
                devid = int(input("Select a device: "))
                if not devid in devices_list:
                    print("Invalid device selection")
            except ValueError:
                print("Invalid device selection")
            print()
    
    
    # Open selected device
    vnx.fnLDA_InitDevice(devid)
    
    # Get some basic information about device that we will need for later
    minAttenuation = int(vnx.fnLDA_GetMinAttenuation(devid) / 4)
    maxAttenuation = int(vnx.fnLDA_GetMaxAttenuation(devid) / 4)
    numChannels = vnx.fnLDA_GetNumChannels(devid)
    
    # Loop until the user decides to quit
    while True:
        # Prompt user for next action
        print("Select an option:")
        print("\t(1) Change channel")
        print("\t(2) Change attenuation")
        print("\t(3) Quit")

        choice = input("Enter your choice (1/2/3): ")
        print()

        if choice == '1':       # Set the channel
            
            try:
                channel = int(input(f"Enter a channel number between 1 and {numChannels}: "))
                if channel >=1 and channel <= numChannels:
                    print(f"Setting channel to {channel}...")
                    vnx.fnLDA_SetChannel(devid, channel)
                else:
                    print("Invalid channel selection")
            except ValueError:
                print("Invalid channel selection")
                
        elif choice == '2':     # Set the attenuation
            
            try:
                attenuation = float(input(f"Enter an attenuation value between {minAttenuation} and {maxAttenuation}: "))
                if attenuation >= minAttenuation and attenuation <= maxAttenuation:
                    print(f"Setting attenuation to {attenuation}...")
                    vnx.fnLDA_SetAttenuationHR(devid, int(attenuation * 20))
                else:
                    print("Invalid attenuation selection")
            except ValueError:
                print("Invalid attenuation selection")
                
        elif choice == '3':     # Quit
            
            print("Quitting...")
            vnx.fnLDA_CloseDevice(devid)
            break
        
        else:
                print("Invalid choice")
        print()
else:
    print("No device found")
                              
