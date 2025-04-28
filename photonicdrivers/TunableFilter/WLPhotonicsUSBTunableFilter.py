"""
Created on Mon Feb 10 12:46:02 2025
Modified later
 
@author: Marcus Albrechtsen <m.albrechtsen@nbi.ku.dk>
 
Basic Python driver to connnect and control USB-tunable fiber-pigtailed grating filters from WL Photonics.
The device is often called Silicon labs something in device manager.
"""
 
import time
import serial
import re
import numpy as np
from photonicdrivers.Abstract.Connectable import Connectable

class WLPhotonicsUSBTunableFilter(Connectable):
    # Error codes and their corresponding descriptions
    ERROR_CODES = {
        "4": "Busy",
        "5": "Wait",
        "6": "Command in progress",
        "7": "Command received",
        "8": "Empty input",
        "40": "Error command",
        "41": "Error Value or value Over limit",
        "42": "Not in range",
        "43": "Error response",
        "44": "Error in initialization",
        "45": "Error Check sum",
        "46": "Error in erasing memory",
        "47": "Over time",
        "50": "Error address",
        "51": "Error length",
        "52": "Error format",
        "53": "Error ID",
        "54": "Error in writing EEPROM/Flash memory",
        "55": "Error in reading EEPROM/Flash memory"
    }
   
    def __init__(self, port: str, baudrate:int=115200, timeout:float=1, wavelength_offset:float=-0.2):
        """Initialize the connection to a tunable filter over USB with an optional wavelength offset."""
        self.wavelength_offset = float(wavelength_offset)  # Ensure it's a float
        self.lower_limit = None
        self.upper_limit = None
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
       
    def connect(self):
        self.instr = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
 
        # Run DEV? to extract device information, including range and serial number
        self.get_device_info()
 
    def disconnect(self):
        """Closes the serial connection safely."""
        if self.instr and self.instr.is_open:
            self.instr.close()
        self.instr = None
 
    def is_connected(self):
        """Check if the device is connected."""
        return self.get_device_info() is not None

    def send_command(self, command, wait_time=2.0, poll_interval=0.1):
        """Send a command to the tunable filter and return the response."""
        if not self.instr or not self.instr.is_open:
            print("Error: Serial port is not open.")
            return None
   
        try:
            # Write the command to the device
            self.instr.write((command + '\r\n').encode())
           
            # Initialize variables
            start_time = time.time()  # Start time for timeout handling
            response_lines = []  # List to store response lines
           
            while True:
                # Read one line from the device
                line = self.instr.readline().decode().strip()
               
                if line:  # Ignore empty lines
                    response_lines.append(line)
   
                # Check if the response contains "OK", which signals the end of the command's response
                if "OK" in line:
                    break
                if line.startswith("ER:"):
                    error_code = line.split(" ")[1].strip()
                    error = None
                    if error_code in self.ERROR_CODES:
                        error = self.ERROR_CODES[error_code]
                    raise Exception(f"Error response from device: {error} ({error_code})")
                # Timeout condition: if time elapsed exceeds wait_time, raise TimeoutError
                if time.time() - start_time > wait_time:
                    raise TimeoutError(f"Command timed out after {wait_time} seconds.")
   
                # Sleep before retrying to check for the next response line
                time.sleep(poll_interval)
   
            # Join the response lines into a single string and return it
            full_response = "\n".join(response_lines)
   
            # If the response contains any error codes, print the relevant error message
            for line in response_lines:
                if line in self.ERROR_CODES:
                    print(f"Error: {self.ERROR_CODES[line]} ({line})")
                    break
   
            return full_response if full_response else "No response received."
   
        except serial.SerialException as e:
            print(f"Serial communication error: {e}")
            return None

    def set_wavelength(self, wavelength):
        """Set the filter wavelength in nm, applying the wavelength offset."""
        adjusted_wavelength = float(wavelength + self.wavelength_offset) # Apply offset between grating setpoint and true wavelength from wavemeter
       
        if not (self.lower_limit <= adjusted_wavelength <= self.upper_limit):
            print(f"Error: Target wavelength {wavelength} nm (adjusted: {adjusted_wavelength} nm) is out of range ({self.lower_limit} - {self.upper_limit} nm).")
            return
       
        # Pre-movement position is 0.2 nm below target, to always move towards target from blue to have consistent offset (e.g., offset is 148.5 pm versus 155.5 pm blue compared to CW laser, Santec)
        pre_move_wavelength = max(self.lower_limit, adjusted_wavelength - 1) # Never go outside of range
        command = f'WL{pre_move_wavelength}'
        response = self.send_command(command)
        time.sleep(0.1) # We let the device rest to be sure we move consistently
       
        command = f'WL{adjusted_wavelength}'
        response = self.send_command(command)
        time.sleep(0.1) # We let the device rest briefly to ensure it has converged
       
        # Read the response, discard the "OK" part
        if response:
            # wavelength_set_value = response.split()[2] # We do not actually need this
            wavelength_actual_value = self.get_wavelength()
            print(f"Wavelength set to: {wavelength:.4f}, actual value after 100ms wait is: {wavelength_actual_value}")  # Print only the first part of the response (wavelength set)
           
        return response
 
    def get_device_info(self):
        """Returns serial number, wavelength range, and status of the device."""
        command = "DEV?"
        response = self.send_command(command)
       
        if response:
            # Print the raw response for debugging purposes
            # Split response by newlines
            dev_info = response.splitlines()
            print(f"{dev_info[0]}") # Prints serial number and factory calibration date
           
            if len(dev_info) >= 2:
                serial_match = re.search(r"SN\((\d+)\)", dev_info[0])
                if serial_match:
                    self.serial_number = serial_match.group(1)
                else:
                    print("Error: Serial number not found in the response.")
                    self.serial_number = None
               
                range_str = dev_info[1]  # Format: "WL Range: 1200.000~1300.000nm(Step: 0.001~0.005)"
               
                # Regex to extract lower and upper limits and step size
                range_match = re.match(r"WL Range: (\d+\.\d+|\d+)~(\d+\.\d+|\d+)nm",  range_str)
               
                if range_match:
                    self.lower_limit = float(range_match.group(1))
                    self.upper_limit = float(range_match.group(2))
                    print(f"Wavelength Range: {self.lower_limit} nm to {self.upper_limit} nm.\n")
                else:
                    print("Error parsing wavelength range from device response.")
            else:
                print(f"Error: Unexpected response format from device. Received {len(dev_info)} lines instead of 2 or more.")
                print("Response:", dev_info)
       
        return response
 
    def get_wavelength(self):
        """Returns the current wavelength set in the device."""
        return None
        # The device fails with error 53 (Error ID) when executing this command
        # command = "WL?"
        # response = self.send_command(command)
        # if response:
        #     return response.splitlines()[0].replace("Wavelength:", "").strip()
        # return None
 
    def go_to_zero(self):
        """Send 'z' command to go to zero position."""
        command = "z"
        response = self.send_command(command)
        if response:
            print("Zero position set:", response)
       
           
        # grating filter takes longer to zero and is not ready when it says it is. 2 seconds seems to be enough.
        # Additionally, the next time set wavelength is called there seems to be some lag in going there so we call it once here.
        time.sleep(2)
        center_wavelength = 0.5 * (self.lower_limit + self.upper_limit)
        self.set_wavelength(center_wavelength)
        time.sleep(0.5)
       
        return response
 
    def set_wavelength_offset(self, offset):
        """Set a new wavelength offset."""
        self.wavelength_offset = float(offset)
        print(f"Wavelength offset set to {self.wavelength_offset}")
        return self.wavelength_offset
 
# Define a main script to run in case this is run as a script and not used as a class.
if __name__ == "__main__":
    try:
        wl_start = 1298.98
        wl_end = wl_start+0.2
        wl_step = 10e-3
        wavelengths = np.arange(wl_start, wl_end + wl_step, wl_step)  # 1240 to 1245 nm
 
        # Here you can run the device as a script
        filter_device = WLPhotonicsUSBTunableFilter(wavelength_offset=0.0)
        for wl in wavelengths:
            filter_device.set_wavelength(wl)
           
            time.sleep(0.2)
 
        # filter_device.set_wavelength(wl_start)        
       
 
    except PermissionError as e:
        # Handle specific serial port errors (e.g., port is locked or denied access)
        print(f"PermissionError: Could not access the port. Error details: {e}")
 
    except TimeoutError as e:
        # Handle timeout errors when the device doesn't respond in time
        print(f"TimeoutError: {e}")
 
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected error occurred: {e}")
   
    finally:
        # Ensure the serial connection is closed properly, even if an error occurs
        try:
            filter_device.close()
        except AttributeError:
            print("Device object was not created, no connection to close.")
        except Exception as e:
            print(f"Error closing the serial port: {e}")
 