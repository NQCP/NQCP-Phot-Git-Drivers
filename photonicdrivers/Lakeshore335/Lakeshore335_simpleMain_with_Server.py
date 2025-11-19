from labserver.Server.DriverFinder import DriverFinder
from photonicdrivers.Lakeshore335.Lakeshore335_Driver import Lakeshore335_Driver


finder = DriverFinder()
lakeshore_driver: Lakeshore335_Driver = finder.get_driver("lakeshore_atto02")

t1, t2 = lakeshore_driver.get_all_kelvin()
print(f"Sensor 1 Temperature: {t1} K")
print(f"Sensor 2 Temperature: {t2} K")