"""Module for slider stages. Inherits from elliptec.Motor."""
from devices import devices
from motor import Motor


class Slider(Motor):
    """Slider class for elliptec devices. Inherits from elliptec.Motor."""

    def __init__(self, controller, address="0", debug=True):
        # Patch parent object - elliptec.Motor(port, baud, bytesize, parity)
        super().__init__(controller=controller, address=address, debug=debug)

    ## Setting and getting slots
    def get_slot(self):
        """Finds at which slot the slider is at the moment."""
        status = self.get("position")
        slot = self.extract_slot_from_status(status)
        return slot

    def set_slot(self, slot):
        """Moves the slider to a particular slot."""
        position = self.slot_to_pos(slot)
        status = self.move("absolute", (position))
        slot = self.extract_slot_from_status(status)
        return slot

    def jog(self, direction="forward"):
        """Jogs by the jog distance in a particular direction."""
        if direction in ["backward", "forward"]:
            status = self.move(direction)
            slot = self.extract_slot_from_status(status)
            return slot
        else:
            return None

    # Helper functions
    def extract_slot_from_status(self, status):
        """Extracts slot from status."""
        # If status is telling us current position
        if status:
            if status[1] == "PO":
                position = status[2]
                slot = self.pos_to_slot(position)
                return slot

        return None

    def pos_to_slot(self, posval, accuracy=5):
        """Converts position value to slot number."""
        positions = devices[self.motor_type]["positions"]
        closest_position = min(positions, key=lambda x: abs(x - posval))
        if abs(closest_position - posval) > accuracy:
            return None
        else:
            slot = positions.index(closest_position) + 1
            return slot

    def slot_to_pos(self, slot):
        """Converts slot number to position value."""
        positions = devices[self.motor_type]["positions"]
        # If slot within range
        if slot - 1 in list(range(len(positions))):
            return positions[slot - 1]
