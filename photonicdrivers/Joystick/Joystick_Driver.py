import pygame

from photonicdrivers.Abstract.Connectable import Connectable

class Joystick(Connectable):
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
            print("No joystick connected.")
            return False

    def disconnect(self):
        if self.joystick is not None:
            self.joystick.quit()
            self.joystick = None

    def is_connected(self):
        connected = False
        try:
            connected = self.joystick is not None and self.joystick.get_id() is not None
        finally:
            return connected


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
            pygame.time.delay(1)

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