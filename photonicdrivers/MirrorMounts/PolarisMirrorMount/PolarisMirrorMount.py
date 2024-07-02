# this is a class for the polaris mirror mount

import math

from photonicdrivers.Piezo_KPZ101.PiezoKPZ101 import PiezoKPZ101

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