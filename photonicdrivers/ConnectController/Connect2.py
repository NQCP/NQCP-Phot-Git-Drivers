from threading import Thread

from photonicdrivers.Instruments.Implementations.Joystick.Joystick import Joystick
from photonicdrivers.Instruments.Implementations.MirrorMounts.NewFocusMirrorMount.NewFocusMirrorMount import \
    NewFocusMirrorMount

# Main loop to read input
if __name__ == "__main__":
    # Create JoystickHandler instance
    joystick = Joystick()
    mirror_mount = NewFocusMirrorMount(joystick)
    joystick.register_observer(mirror_mount)

    joystick.connect()
    thread = Thread(target=joystick.joystick_acquisition)
    thread.start()


