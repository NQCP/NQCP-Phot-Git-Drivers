# import ctypes

# import pefile

# dll_path = r"C:\Users\Public\Documents\NKT Photonics\SDK\Examples\DLL_Example_Python\NKTPDLL.dll"
# pe = pefile.PE(dll_path)

from photonicdrivers.Lasers.SuperK.SuperK_Driver import SuperK_Driver

laser_driver=SuperK_Driver()
laser_driver.connect()
print(laser_driver.is_connected())
laser_driver.set_power_level(75)

import time
laser_driver.enable_emission()
time.sleep(2)
print(laser_driver.get_emission_status())
time.sleep(2)
print(laser_driver.disable_emission())
print(laser_driver.get_emission_status())
print(laser_driver.get_power_level())
laser_driver.disconnect()

print(laser_driver.is_connected())




