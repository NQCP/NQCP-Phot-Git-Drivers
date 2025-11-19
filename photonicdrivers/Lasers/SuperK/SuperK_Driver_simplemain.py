# import ctypes

# import pefile

# dll_path = r"C:\Users\Public\Documents\NKT Photonics\SDK\Examples\DLL_Example_Python\NKTPDLL.dll"
# pe = pefile.PE(dll_path)

from photonicdrivers.Lasers.SuperK.SuperK_Driver import SuperK_Driver

laser_driver=SuperK_Driver()

laser_driver.set_power_level(0)

#laser_driver.enable_emission()

#print(laser_driver.disable_emission())


