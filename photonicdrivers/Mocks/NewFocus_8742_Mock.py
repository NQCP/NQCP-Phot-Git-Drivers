from photonicdrivers.Abstract.Connectable import Connectable
import math
import numpy as np
class NewFocus_8742_Mock(Connectable):
    def __init__(self, skew_negative: bool=False):
        self.axis_positions: list[float] = [0.0, 0.0, 0.0, 0.0]
        self.move_history = []

        self.skew_negative = skew_negative

    def get_product_ID(self):
        return "product_ID"

    def get_IP_address(self):
        return "IP_address"

    def get_host_name(self):
        return "host_name"

    def get_MAC_address(self):
        return "MAC_address"

    def move_target_position(self, axis_number_str):
        pass

    def _stretch(self, x):
        k = 0.5
        decay_rate = 0.002
        return (x / (1 + k * np.exp(-np.abs(x) * decay_rate)))

    def move_relative_position(self, axis_number_str, distance_str):
        if self.skew_negative and distance_str < 0:
            actual_dist = self._stretch(distance_str)
        else:
            actual_dist = distance_str

        self.axis_positions[axis_number_str] += actual_dist
        self.move_history.append([axis_number_str, distance_str]) # Move history is issued commands, not actual distances moved

    def get_target_position(self, axis_number_str):
        pass

    def is_moving(self, axis_number_str):
        return False

    def write_custom_command(self, commandStr):
        pass

    def disconnect(self):
        pass

    def connect(self) -> None:
        pass

    def is_connected(self) -> bool:
        return True