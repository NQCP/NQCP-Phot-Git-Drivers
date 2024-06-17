# this is a class for the polaris mirror mount

import math
from photonicdrivers.Instruments.Implementations.PicoMotor.Picomotor8742 import PicoMotor


class NewFocusMirrorMount:



    def __init__(self, serial_number_x=None, serial_number_y=None, distance=0):
        self.pico_motor_x = PicoMotor(port=0)
        self.pico_motor_y = PicoMotor(port=1)
        self.distance = distance
        self.angle_per_voltage = 1
        self.max_voltage = 0
        self.min_voltage = 0
        self.max_angle = 0
        self.min_angle = 0


    def move_angle(self, angle_x, angle_y):
        voltage_x = angle_x / self.angle_per_voltage
        voltage_y = angle_y/ self.angle_per_voltage

        self.pico_motor_x.set_output_voltage(voltage_x)
        self.pico_motor_y.set_output_voltage(voltage_y)

    def move_distance(self, distance_x, distance_y):
        if self.distance == 0:
            print("Error: the distance from the mirror to the object is not defined. Cannot use moveDistance function")
        else:
            angle_x = math.atan2(distance_x, self.distance)
            angle_y = math.atan2(distance_y, self.distance)
            self.move_angle(angle_x, angle_y)

if __name__ == "__main__":
    piezo = NewFocusMirrorMount("10.209.67.98", 3)