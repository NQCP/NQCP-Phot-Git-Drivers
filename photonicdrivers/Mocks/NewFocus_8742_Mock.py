from photonicdrivers.Abstract.Connectable import Connectable

class NewFocus_8742_Mock(Connectable):
    def __init__(self):
        self.axis_positions = [0, 0, 0, 0]
        self.move_history = []

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

    def move_relative_position(self, axis_number_str, distance_str):
        self.axis_positions[axis_number_str] += distance_str
        self.move_history.append([axis_number_str, distance_str])

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