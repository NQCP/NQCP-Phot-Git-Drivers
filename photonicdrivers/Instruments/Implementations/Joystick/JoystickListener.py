from photonicdrivers.Instruments.Settings.Console_Controller import Console_Controller


class JoystickListener:
    def __init__(self, joystick):
        self.joystick = joystick
        self.button_states = {}
        self.axis_states = {}

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
                Console_Controller.print_message("Button {} clicked".format(i))

            # Check for button hold
            if button_state:
                self.joystick.start_rumble()
                Console_Controller.print_message("Button {} held".format(i))

            # Check for button release
            if not button_state and self.button_states[i]:
                Console_Controller.print_message("Button {} released".format(i))

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
                Console_Controller.print_message("Axis {} moved to {:.2f}".format(i, axis_value))

            # Update axis state in the dictionary
            self.axis_states[i] = axis_value