from photonicdrivers.RotationMounts.Elliptec_Driver import Elliptec_Driver
from labserver.Server.DriverFinder import DriverFinder
f = DriverFinder()

d: Elliptec_Driver = f.get_driver("input_waveplates_atto02")

d.move_by(10, 3)
d.move_by(-10, 3)