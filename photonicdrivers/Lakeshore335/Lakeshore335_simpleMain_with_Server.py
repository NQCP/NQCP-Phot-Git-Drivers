from labserver.Server.DriverFinder import DriverFinder
from photonicdrivers.Lakeshore335.Lakeshore335_Driver import Lakeshore335_Driver


finder = DriverFinder()
lakeshore: Lakeshore335_Driver = finder.get_driver("lakeshore_atto02")

t1, t2 = lakeshore.get_all_kelvin()
print(f"Sensor 1 Temperature: {t1} K")
print(f"Sensor 2 Temperature: {t2} K")

# # code for checking that things work even without the server :)
# lakeshore.connection.set_temperature_limit(1, 15)
# lakeshore.connection.set_heater_range(1, 1)
# hr = lakeshore.connection.get_heater_range(1)
# print(f"heater range {hr}")
# lakeshore.connection.set_control_setpoint(1, 5)
# st = lakeshore.connection.get_control_setpoint(1)
# print(st)