from photonicdrivers.Abstract.Connectable import Connectable
from photonicdrivers.Joystick.Joystick_Driver import PSControllerState, no_input_state
class Joystick_Driver_Mock(Connectable):
    def __init__(self):
        pass

    def disconnect(self):
        pass

    def is_connected(self):
        return True
    def get_state(self) -> PSControllerState:
        return no_input_state()