import ctypes
import glob
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)
print("Script directory", script_dir)
# Construct the relative path to the DLL directory
dll_directory = os.path.join(script_dir, '..', 'dlls')
print("Dll_directory", dll_directory)
# Find all DLL files in the specified directory
dll_files = glob.glob(os.path.join(dll_directory, "*.dll"))

# Load each DLL file
for dll in dll_files:
    try:
        ctypes.cdll.LoadLibrary(dll)
        #print(f"Successfully loaded {dll}")
    except Exception as e:
        print(f"Failed to load {dll}: {e}")