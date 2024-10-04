import numpy as np
from pylablib.devices.Thorlabs.elliptec import ElliptecMotor as motor
import serial

class ELLO14:
    # Class for controlling ELLO14 rotation stage
    def __init__(self, address):
        self.address = address

    def connect(self):
        self.rotation_stage = motor(conn='COM8', addrs=self.address, timeout = 2, scale = "stage")

    def close(self):
        self.rotation_stage.close()

    def move_to(self,angle):
        if angle < -360:
            angle = np.mod(angle,-360)
        if angle > 360:
            angle = np.mod(angle,360)
        self.rotation_stage.move_to(angle)

    def move_by(self, angle): # Value in degrees
        self.rotation_stage.move_by(angle)

    def home(self):
        self.rotation_stage.home()

    def get_position(self):
        return self.rotation_stage.get_position()
    
if __name__ == "__main__":
    rotation_mount = ELLO14(address="A")
    rotation_mount.connect()
    print(rotation_mount.get_position())


