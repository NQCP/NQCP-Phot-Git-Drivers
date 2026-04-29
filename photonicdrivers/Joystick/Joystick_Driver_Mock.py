from photonicdrivers.Abstract.Connectable import Connectable
from photonicdrivers.Joystick.Joystick_Driver import PSControllerState, no_input_state
class Joystick_Driver_Mock(Connectable):
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False    

    def is_connected(self):
        return self.connected
    
    def get_state(self) -> PSControllerState:
        return no_input_state()