# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:05:09 2024

@author: NQCP_

Trying to communicate with laser through python
"""

# #### IMPORT LIBRARIES ####
# import ctypes as ct

# #### LOAD .dll FILE ####
# # What is the ideal location for the dll? it should be the 64 version

# SEPIA2_LIB_DLL_NAME = "C:\\Users\\NQCP_\\OneDrive\\Desktop\\Control scripts\\PDL810_laser\\Sepia2_Lib64.dll"
# Sepia2_Lib = ct.WinDLL(SEPIA2_LIB_DLL_NAME)



# #### DEFINE FUNCTIONS ####
# # first define input and output type, then define function


# # decode_error : inputs error number and outputs explanation

# Sepia2_Lib.SEPIA2_LIB_DecodeError.argtypes = [ct.c_int, ct.c_char_p] # arguments: integer (error code), pointer to character buffer (string)
# Sepia2_Lib.SEPIA2_LIB_DecodeError.restype = ct.c_int # returns integer

# def decode_error(err_code):
#     # Create a buffer for the error string (64 characters)
#     error_string = ct.create_string_buffer(64)
    
#     # Call the function from the DLL
#     result = Sepia2_Lib.SEPIA2_LIB_DecodeError(err_code, error_string)
    
#     # Convert the result to a string
#     decoded_error = error_string.value.decode('utf-8')
    
#     # Return both the result and the error string
#     return result, decoded_error





###################################### write as classes

import ctypes as ct

class PDL810Controller:
    def __init__(self, dll_path="C:/gitRepositories/NQCP-Phot-Git-Drivers/photonicdrivers/Lasers/PDL_810/Sepia2_Lib64.dll"):
        """Initialize the PDL810 controller by loading the SEPIA2 DLL."""
        self.dll_path = dll_path
        self.Sepia2_Lib = ct.WinDLL(self.dll_path)

        # Define the error decoding function prototype
        self.Sepia2_Lib.SEPIA2_LIB_DecodeError.argtypes = [ct.c_int, ct.c_char_p]
        self.Sepia2_Lib.SEPIA2_LIB_DecodeError.restype = ct.c_int

    def decode_error(self, err_code):
        """Helper function to decode SEPIA2 error codes."""
        error_string = ct.create_string_buffer(64)
        self.Sepia2_Lib.SEPIA2_LIB_DecodeError(err_code, error_string)
        return error_string.value.decode('utf-8')

    def open_usb_device(self, iDevIdx):
        """Open the USB device and retrieve its product model and serial number."""
        # Define the function prototype for SEPIA2_USB_OpenDevice
        self.Sepia2_Lib.SEPIA2_USB_OpenDevice.argtypes = [
            ct.c_int,                # iDevIdx (int)
            ct.c_char_p,             # cProductModel (char*)
            ct.c_char_p              # cSerialNumber (char*)
        ]
        self.Sepia2_Lib.SEPIA2_USB_OpenDevice.restype = ct.c_int  # return type is int

        # Create buffers to store the product model and serial number
        product_model = ct.create_string_buffer(32)   # Buffer for the product model (32 chars)
        serial_number = ct.create_string_buffer(32)   # Buffer for the serial number (32 chars)

        # Call the function from the DLL
        result = self.Sepia2_Lib.SEPIA2_USB_OpenDevice(
            iDevIdx,
            product_model,   # Pass the buffer for product model
            serial_number    # Pass the buffer for serial number
        )

        # Check the result and raise an exception if there's an error
        if result != 0:
            raise Exception(f"Error opening USB device: {self.decode_error(result)}")

        # Return the product model and serial number as strings
        return product_model.value.decode('utf-8'), serial_number.value.decode('utf-8')
    
    def get_str_descriptor(self, iDevIdx):
        """Get the USB string descriptor for the device."""
        # Define the function prototype for SEPIA2_USB_GetStrDescriptor
        self.Sepia2_Lib.SEPIA2_USB_GetStrDescriptor.argtypes = [
            ct.c_int,        # iDevIdx (int)
            ct.c_char_p      # cDescriptor (char*)
        ]
        self.Sepia2_Lib.SEPIA2_USB_GetStrDescriptor.restype = ct.c_int  # return type is int
    
        # Create a buffer to store the string descriptor
        descriptor = ct.create_string_buffer(256)  # Assuming the descriptor can be up to 256 chars
    
        # Call the function from the DLL
        result = self.Sepia2_Lib.SEPIA2_USB_GetStrDescriptor(
            iDevIdx,
            descriptor   # Pass the buffer for the descriptor
        )
    
        # Check the result and raise an exception if there's an error
        if result != 0:
            raise Exception(f"Error getting USB string descriptor: {self.decode_error(result)}")
    
        # Return the descriptor as a string
        return descriptor.value.decode('utf-8')

    def get_module_info_by_map_idx(self, iDevIdx, iMapIdx):
            """Retrieve module info by map index."""
            # Define the function prototype for SEPIA2_FWR_GetModuleInfoByMapIdx
            self.Sepia2_Lib.SEPIA2_FWR_GetModuleInfoByMapIdx.argtypes = [
                ct.c_int,              # iDevIdx (int)
                ct.c_int,              # iMapIdx (int)
                ct.POINTER(ct.c_int),  # piSlotId (int*)
                ct.POINTER(ct.c_ubyte),# pbIsPrimary (unsigned char*)
                ct.POINTER(ct.c_ubyte),# pbIsBackPlane (unsigned char*)
                ct.POINTER(ct.c_ubyte) # pbHasUTC (unsigned char*)
            ]
            self.Sepia2_Lib.SEPIA2_FWR_GetModuleInfoByMapIdx.restype = ct.c_int  # return type is int
    
            # Create variables for output parameters
            piSlotId = ct.c_int()  # Slot ID will be stored here
            pbIsPrimary = ct.c_ubyte()  # Primary status will be stored here
            pbIsBackPlane = ct.c_ubyte()  # Backplane status will be stored here
            pbHasUTC = ct.c_ubyte()  # UTC status will be stored here
    
            # Call the function from the DLL
            result = self.Sepia2_Lib.SEPIA2_FWR_GetModuleInfoByMapIdx(
                iDevIdx,
                iMapIdx,
                ct.byref(piSlotId),      # Pass by reference to get the slot ID
                ct.byref(pbIsPrimary),   # Pass by reference to get primary status
                ct.byref(pbIsBackPlane), # Pass by reference to get backplane status
                ct.byref(pbHasUTC)       # Pass by reference to get UTC status
            )
    
            # Check the result and raise an exception if there's an error
            if result != 0:
                raise Exception(f"Error getting module info: {self.decode_error(result)}")
    
            # Return the results as a dictionary
            return {
                "SlotId": piSlotId.value,
                "IsPrimary": bool(pbIsPrimary.value),
                "IsBackPlane": bool(pbIsBackPlane.value),
                "HasUTC": bool(pbHasUTC.value)
            }


    def get_power_and_laser_leds(self, iDevIdx, iSlotId):
        """Get the Power and Laser Activity LED states."""
        # Define the function prototype for SEPIA2_SCM_GetPowerAndLaserLEDS
        self.Sepia2_Lib.SEPIA2_SCM_GetPowerAndLaserLEDS.argtypes = [
            ct.c_int,        # iDevIdx
            ct.c_int,        # iSlotId
            ct.POINTER(ct.c_ubyte),  # pbPowerLED (unsigned char*)
            ct.POINTER(ct.c_ubyte)   # pbLaserActLED (unsigned char*)
        ]
        self.Sepia2_Lib.SEPIA2_SCM_GetPowerAndLaserLEDS.restype = ct.c_int  # return type is int

        # Create buffers to store the result of the Power LED and Laser Activity LED
        power_led = ct.c_ubyte()   # Equivalent to unsigned char
        laser_led = ct.c_ubyte()   # Equivalent to unsigned char

        # Call the function from the DLL
        result = self.Sepia2_Lib.SEPIA2_SCM_GetPowerAndLaserLEDS(
            iDevIdx,
            iSlotId,
            ct.byref(power_led),  # Pass the reference to the buffer
            ct.byref(laser_led)   # Pass the reference to the buffer
        )

        # Check the result and raise an exception if there's an error
        if result != 0:
            raise Exception(f"Error getting Power and Laser LEDs: {self.decode_error(result)}")
        
        # Return the LED statuses as a tuple
        return power_led.value, laser_led.value
        
   #%%
laser = PDL810Controller()
print(laser.open_usb_device(0))
print(laser.get_str_descriptor(0))
print(laser.get_module_info_by_map_idx(0,1))
# print(laser.get_power_and_laser_leds(0, 200))
iDevIdx = 0
for iSlotId in range(900,1001):
            try:
                power_led, laser_led = laser.get_power_and_laser_leds(iDevIdx, iSlotId)
                print(f"Slot {iSlotId}: Power LED = {power_led}, Laser LED = {laser_led}")
            except Exception as e:
                print(f"Error or no module found at Slot {iSlotId}: {str(e)}")
