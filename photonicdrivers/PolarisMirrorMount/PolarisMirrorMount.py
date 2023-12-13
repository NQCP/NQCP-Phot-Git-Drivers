# this is a class for the polaris mirror mount

import os
import sys
import math

# script_dir = os.path.dirname(os.path.realpath(__file__))
# project_root = os.path.abspath(os.path.join(script_dir, '..'))
# sys.path.append(project_root)

# sys.path.append("../Piezo_kpz101")  # Add the parent directory to the Python path
# from Piezo_kpz101.piezoKPZ101 import PiezoKPZ101

# sys.path.append(r'C:\Users\psj335\OneDrive - University of Copenhagen\PhotonicDrivers\photonicdrivers\Piezo_KPZ101')
# from piezoKPZ101 import PiezoKPZ101

from photonicdrivers.Piezo_kpz101.piezoKPZ101 import PiezoKPZ101

# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
# from Piezo_kpz101.piezoKPZ101 import PiezoKPZ101

class Polaris:
    def __init__(self, _kpz101SerialNoX, _kpz101SerialNoY, _dist = 0):
        self.PiezoX = PiezoKPZ101(_kpz101SerialNoX)
        self.PiezoY = PiezoKPZ101(_kpz101SerialNoY)

        self.PiezoX.enable()
        self.PiezoY.enable()

        print("initiated")
        self.anglePerVoltage = 1 # unit: urad per V
        self.dist = _dist # the distance from the mirror to the object in metres

    def moveAngle(self, angleX, angleY):
        voltageX = angleX/self.anglePerVoltage
        voltageY = angleY/self.anglePerVoltage

        self.PiezoX.SetOutputVoltage(voltageX)
        self.PiezoY.SetOutputVoltage(voltageY)

    def moveDistance(self, distX, distY):
        if self.dist == 0: 
            print("Error: the distance from the mirror to the object is not defined. Cannot use moveDistance function")
        else:
            angleX = math.atan2(distX, self.dist)
            angleY = math.atan2(distY, self.dist)
            self.moveAngle(angleX,angleY)


        




# if __name__ == "__main__":
#     piezo = Polaris("29252886")