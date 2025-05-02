import pygame

from dataclasses import dataclass

from photonicdrivers.Abstract.Connectable import Connectable

PS4_CONTROLLER_NAME = "PS4 Controller"
PS5_CONTROLLER_NAME = "Sony Interactive Entertainment Wireless Controller"

@dataclass
class PSControllerState:
    Cross: bool
    Circle: bool
    Square: bool
    Triangle: bool
    LeftBumper: bool
    RightBumper: bool
    Share: bool
    Options: bool
    LeftStickPressed: bool
    RightStickPressed: bool
    PSButton: bool
    LeftStickX: float
    LeftStickY: float
    RightStickX: float
    RightStickY: float

class Joystick_Driver(Connectable):
    def __init__(self):
        pygame.init()

        self.joystick = None

    def connect(self, joystick_index=0):
        # Check that connecting to the given joystick index is possible
        joystick_count = pygame.joystick.get_count()
        if joystick_count < joystick_index + 1:
            raise ValueError(f"Joystick index is out of range (found {joystick_count} joysticks but expected at least {joystick_index + 1})")
        
        self.joystick = pygame.joystick.Joystick(joystick_index)
        self.joystick.init()
        self.joystick_name = self.joystick.get_name()
            

    def disconnect(self):
        if self.joystick is not None:
            self.joystick = None

    def is_connected(self):
        try:
            pygame.event.pump()
            return self.joystick is not None and self.joystick.get_id() is not None
        except Exception:
            return False
        
    def get_state(self) -> PSControllerState:
        """
        Read and return the state of a connected PS4 or PS5 controller
        """
        if self.joystick is None:
            raise Exception("No joystick object is connected (uninitialized)")
        pygame.event.pump()
        j = self.joystick


        if self.joystick_name == PS4_CONTROLLER_NAME:
            # Holding joysticks up gives a negative value, for some reason. So we flip the sign of joystick Ys
            return PSControllerState(
                Cross=j.get_button(0),
                Circle=j.get_button(1),
                Square=j.get_button(2),
                Triangle=j.get_button(3),
                LeftBumper=j.get_button(9),
                RightBumper=j.get_button(10),
                Share=j.get_button(4),
                Options=j.get_button(6),
                LeftStickPressed=j.get_button(7),
                RightStickPressed=j.get_button(8),
                PSButton=j.get_button(5),
                LeftStickX=j.get_axis(0),
                LeftStickY=-j.get_axis(1),
                RightStickX=j.get_axis(2),
                RightStickY=-j.get_axis(3))

        elif self.joystick_name == PS5_CONTROLLER_NAME:
            # I don't actually know if PS5 joystick Y value is inverted too. Check please!
            return PSControllerState(
                Cross=j.get_button(0),
                Circle=j.get_button(1),
                Square=j.get_button(2),
                Triangle=j.get_button(3),
                LeftBumper=j.get_button(4),
                RightBumper=j.get_button(5),
                Share=j.get_button(8),
                Options=j.get_button(9),
                LeftStickPressed=j.get_button(11),
                RightStickPressed=j.get_button(12),
                PSButton=j.get_button(10),
                LeftStickX=j.get_axis(0),
                LeftStickY=-j.get_axis(1),
                RightStickX=j.get_axis(3),
                RightStickY=-j.get_axis(4))
        else:
            raise NotImplementedError(f"Unsupported controller: {self.joystick_name}")
