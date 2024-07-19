import pyvisa as visa
from photonicdrivers.Lasers.Toptica.Toptica_DLC_Pro import Toptica_CTL950_driver


resource_manager = visa.ResourceManager()
print(resource_manager.list_resources())

toptica_laser = Toptica_CTL950_driver()
toptica_laser.connect(IP_address='10.209.67.103')
toptica_laser.set_diode(True)
toptica_laser.set_power_stabilization(True)
print(toptica_laser.get_emission_status())

wavelength_list = range(toptica_laser.get_min_wavelength(), toptica_laser.get_max_wavelength(), 1)

for wavelength_nm in wavelength_list:
    print(wavelength_nm)
    toptica_laser.set_wavelength(wavelength_nm)


print("done")
toptica_laser.disconnect()