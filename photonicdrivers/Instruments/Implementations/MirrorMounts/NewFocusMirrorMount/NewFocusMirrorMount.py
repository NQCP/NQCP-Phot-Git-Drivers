# this is a class for the polaris mirror mount

import math

import numpy as np
from matplotlib import pyplot as plt

from photonicdrivers.Instruments.Implementations.Joystick.Joystick import Joystick
from photonicdrivers.Instruments.Implementations.PicoMotor.Picomotor8742 import PicoMotorController, PicoMotor
from photonicdrivers.Instruments.Settings.Console_Controller import Console_Controller


class NewFocusMirrorMount:
    def __init__(self, joystick: Joystick):
        self.joystick = joystick
        self.button_states = {}
        self.axis_states = {}

        pico_motor_controller = PicoMotorController()
        pico_motor_controller.connect()
        self.pico_motor_x = PicoMotor(pico_motor_controller, 3)
        self.pico_motor_y = PicoMotor(pico_motor_controller, 4)
        self.pico_motor_x2 = PicoMotor(pico_motor_controller, 1)
        self.pico_motor_y2 = PicoMotor(pico_motor_controller, 2)

    def move_distance_x(self, distance):
        self.pico_motor_x.move_relative_position(distance)

    def move_distance_y(self, distance):
        self.pico_motor_y.move_relative_position(distance)

    def move_distance_x2(self, distance):
        self.pico_motor_x2.move_relative_position(distance)

    def move_distance_y2(self, distance):
        self.pico_motor_y2.move_relative_position(distance)

    def update(self):
        # Read button input
        for i in range(self.joystick.get_num_buttons()):

            # Get the current state of the button
            button_state = self.joystick.get_button(i)

            # If the button is not in the dictionary, add it with its initial state
            if i not in self.button_states:
                self.button_states[i] = button_state

            # Check for button click
            if button_state and not self.button_states[i]:
                self.joystick.start_rumble()
                Console_Controller.print_message("Button {} clicked".format(i))


            # Check for button hold
            if button_state:

                #self.joystick.start_rumble()
                Console_Controller.print_message("Button {} held".format(i), print_bool = False)

                speed = 2000

                if i == 3:
                    self.move_distance_x2(-speed)
                if i == 0:
                    self.move_distance_y2(-speed)
                if i == 2:
                    self.move_distance_x2(speed)
                if i == 1:
                    self.move_distance_y2(speed)
                if i == 14:
                    self.move_distance_x(-speed)
                if i == 11:
                    self.move_distance_y(-speed)
                if i == 13:
                    self.move_distance_x(speed)
                if i == 12:
                    self.move_distance_y(speed)


            # Check for button release
            if not button_state and self.button_states[i]:
                Console_Controller.print_message("Button {} released".format(i), print_bool = False)

            # Update button state in the dictionary
            self.button_states[i] = button_state



            # Read axis input
        for i in range(self.joystick.get_num_axes()):
            # Get the current state of the axis
            axis_value = self.joystick.get_axis(i)

            # If the axis is not in the dictionary, add it with its initial state
            if i not in self.axis_states:
                self.axis_states[i] = axis_value

            # Check for axis movement
            if axis_value != self.axis_states[i]:
                Console_Controller.print_message("Axis {} moved to {:.2f}".format(i, axis_value), print_bool = False)

            if np.abs(axis_value) > 0.1:
                if i == 0:
                    self.move_distance_x(-int(10*axis_value))
                if i == 1:
                    self.move_distance_y(int(10*axis_value))
                if i == 2:
                    self.move_distance_x2(-int(10*axis_value))
                if i == 3:
                    self.move_distance_y2(int(10*axis_value))



            # Update axis state in the dictionary
            self.axis_states[i] = axis_value



if __name__ == "__main__":
    # Create JoystickHandler instance
    joystick = Joystick()
    mirror_mount = NewFocusMirrorMount(joystick)
    joystick.register_observer(mirror_mount)

    joystick.connect()
    while True:
        plt.pause(0.01)
        mirror_mount.move_distance_x(1)
        plt.pause(0.01)
        mirror_mount.move_distance_y(1)

