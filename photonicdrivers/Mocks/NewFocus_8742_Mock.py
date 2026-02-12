from photonicdrivers.Abstract.Connectable import Connectable
import math
import numpy as np
class NewFocus_8742_Mock(Connectable):
    def __init__(self, skew_negative: bool=False, prnt=False, name: str | None=None, instant_move=True):
        self.connected = False

        self.axis_positions: list[float] = [0.0, 0.0, 0.0, 0.0]
        self.move_history = []
        self.move_command_counts: dict[int, int] = {1: 0, 2: 0, 3: 0, 4: 0}
        self.total_move_commands = 0

        self.skew_negative = skew_negative
        self.prnt = prnt
        self.name = name
        self.instant_move = instant_move
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
        axis_number = int(axis_number_str)
        if self.skew_negative and distance_str < 0:
            actual_dist = self._stretch(distance_str)
        else:
            actual_dist = distance_str
        # -1 due to 1-indexing of ports
        self.axis_positions[axis_number - 1] += actual_dist
        if self.name is not None:
            print(f"Moving axis {axis_number} {actual_dist}" + f" for {self.name}")

        self.move_history.append([axis_number, distance_str]) # Move history is issued commands, not actual distances moved
        if axis_number not in self.move_command_counts:
            self.move_command_counts[axis_number] = 0
        self.move_command_counts[axis_number] += 1
        self.total_move_commands += 1

    def get_axis_move_command_count(self, axis_number: int) -> int:
        return int(self.move_command_counts.get(int(axis_number), 0))

    def get_move_command_counts(self) -> dict[int, int]:
        return dict(self.move_command_counts)

    def get_total_move_command_count(self) -> int:
        return int(self.total_move_commands)

    def reset_move_command_counts(self):
        self.move_command_counts = {1: 0, 2: 0, 3: 0, 4: 0}
        self.total_move_commands = 0

    def get_target_position(self, axis_number_str):
        pass

    def is_moving(self, axis_number_str):
        return False

    def write_custom_command(self, commandStr):
        pass

    def disconnect(self):
        self.connected = False

    def connect(self) -> None:
        self.connected = True

    def is_connected(self) -> bool:
        return self.connected
