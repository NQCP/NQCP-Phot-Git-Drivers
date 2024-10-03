import numpy as np
from pylablib.devices.Thorlabs.elliptec import ElliptecMotor as m

class ELLO14:
    # Class for controlling ELLO14 rotation stage
    def __init__(self,config,server):

        self.name = config['name']
        self.address = config['address']
        self.connect()

        # syntax sugar: add write channels
        self.write_channels = {f'{self.name}: Set position': lambda x: self.move_by(x)}

    def connect(self):
        self.rotation_stage = m(self.address, timeout = 2, scale = "stage")

    def close(self):
        self.rotation_stage.close()

    def move_to(self,Value): # Value in degrees
        # move_to method raises error if Value is out of range [0,360].
        # This is fixed by if-statement below
        if Value < -360:
            Value = np.mod(Value,-360)
        if Value > 360:
            Value = np.mod(Value,360)
        self.rotation_stage.move_to(Value)

    def move_by(self,Value): # Value in degrees
        self.rotation_stage.move_by(Value)

    def home(self):
        self.rotation_stage.home()

    def get_position(self):
        return self.rotation_stage.get_position()

