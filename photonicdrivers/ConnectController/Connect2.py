from threading import Thread

import pygame

from photonicdrivers.Instruments.Settings.Console_Controller import Console_Controller


class Joystick:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Initialize the joystick module
        pygame.joystick.init()

        # Get count of joysticks
        self.joystick_count = pygame.joystick.get_count()

        # Initialize joystick object
        self.joystick = None
        self.observer_list = []

    def connect(self):
        # Check if there is at least one joystick connected
        if self.joystick_count > 0:
            # Get input from the first joystick
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            return True
        else:
            Console_Controller.print_message("No joystick connected.")
            return False

    def joystick_acquisition(self):
        # Main loop
        running = True
        while running:
            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update button and axis states
            self.notify_observers()

            # Add some delay to avoid excessive printing
            pygame.time.delay(100)

    def register_observer(self, observer):
        self.observer_list.append(observer)

    def notify_observers(self):
        for observer in self.observer_list:
            observer.update()

    def get_button(self, index):
        return self.joystick.get_button(index)

    def get_num_buttons(self):
        return self.joystick.get_numbuttons()

    def get_num_axes(self):
        return self.joystick.get_numaxes()

    def get_axis(self, index):
        return self.joystick.get_axis(index)

    def start_rumble(self):
        self.joystick.rumble(1,1,1)


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
                self.joystick.start_rumble()

                Console_Controller.print_message("Button {} clicked".format(i))

            # Check for button hold
            if button_state:
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


# Main loop to read input
def main():
    # Create JoystickHandler instance
    joystick = Joystick()
    joystick_listener = JoystickListener(joystick)
    joystick.register_observer(joystick_listener)
    joystick.connect()
    thread = Thread(target=joystick.joystick_acquisition)
    thread.start()


if __name__ == "__main__":
    main()
