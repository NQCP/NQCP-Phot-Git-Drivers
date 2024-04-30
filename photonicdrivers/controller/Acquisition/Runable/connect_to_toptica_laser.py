import matplotlib.pyplot as plt
import numpy as np
import pyvisa as visa

from photonicdrivers.controller.Instruments.Implementations.Lasers.Toptica_CTL950.Toptica_CTL950 import Toptica_CTL950

resource_manager = visa.ResourceManager()
print(resource_manager.list_resources())

toptica_laser = Toptica_CTL950(IP_address='10.209.67.103')
toptica_laser.connect()
toptica_laser.enable_emission()
toptica_laser.set_power_stabilization(True)
toptica_laser.print_emission_status()

wavelength_list = range(toptica_laser.get_min_wavelength(), toptica_laser.get_max_wavelength(), 1)

for wavelength_nm in wavelength_list:
    print(wavelength_nm)
    toptica_laser.set_wavelength(wavelength_nm)



