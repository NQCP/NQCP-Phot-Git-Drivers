# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 13:42:41 2024

@author: dtk791
"""

from photonicdrivers.Lasers.Santec_TSL570.Santec_TSL570_Ethernet_Driver import Santec_TSL570_driver


laser = Santec_TSL570_driver(resource_manager=None, ip_address = "10.209.69.95", port_number = "5000", prints_enabled = False)

laser.connect()
laser.set_wavelength(1300)
wavelength = laser.get_wavelength()
print(wavelength)
print(laser.set_wavelength_unit(unit="nm"))
print(laser.get_wavelength_unit())

# testing setting a sweep scan
laser.write(':WAV:SWE:CYCL 1')  # Set to 1 cycle

laser.write(':WAV:SWE 1')  # Start wavelength 1260 nm

print(f"number of cycles is {laser.query(':WAV:SWE:CYCL?')}")   # No delay between sweeps

print(f"number of wavelength points is {laser.query(':READout:POINts?')}")  # Read number of points

laser.disconnect()




