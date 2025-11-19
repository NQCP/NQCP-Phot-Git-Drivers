from labserver.Server.DriverFinder import DriverFinder
from photonicdrivers.Lakeshore335.Lakeshore335_Driver import Lakeshore335_Driver


finder = DriverFinder()
lakeshore: Lakeshore335_Driver = finder.get_driver("lakeshore_atto02")

t1, t2 = lakeshore.get_all_kelvin()
print(f"Sensor 1 Temperature: {t1} K")
print(f"Sensor 2 Temperature: {t2} K")

temp = lakeshore.get_monitor_output()
print(temp)