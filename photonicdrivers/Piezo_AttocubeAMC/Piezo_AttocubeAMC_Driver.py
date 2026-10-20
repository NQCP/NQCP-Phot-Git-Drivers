from photonicdrivers.AttocubeAPI import AMC
from photonicdrivers.Abstract.Connectable import Connectable


def axis_to_id(axis: str | int) -> int:
    if isinstance(axis, str):
        axis_lower = axis.lower()
        if axis_lower == 'x':
            return 0
        if axis_lower == 'y':
            return 1
        if axis_lower == 'z':
            return 2
        raise ValueError(f"axis '{axis}' is not a valid axis. Use 'x', 'y', 'z', 0, 1, or 2.")

    if isinstance(axis, bool) or not isinstance(axis, int):
        raise TypeError("axis must be one of 'x', 'y', 'z', 0, 1, or 2.")

    if axis in (0, 1, 2):
        return axis

    raise ValueError(f"axis {axis} is not a valid axis. Use 'x', 'y', 'z', 0, 1, or 2.")


class Piezo_AttocubeAMC_Driver(Connectable):

    def __init__(self,ip_string: str, x_min_nm:int=100000, x_max_nm:int=4900000, y_min_nm:int=100000, y_max_nm:int=4900000, z_min_nm:int=300000, z_max_nm:int=4700000) -> None:
        self.ip_address = ip_string

        self.x_min = x_min_nm
        self.x_max = x_max_nm
        self.y_min = y_min_nm
        self.y_max = y_max_nm
        self.z_min = z_min_nm
        self.z_max = z_max_nm

        self.amc = AMC.Device(self.ip_address)

    def connect(self) -> None:
        self.amc = AMC.Device(self.ip_address)
        self.amc.connect()

    def disconnect(self) -> None:
        self.amc.close()

    def is_connected(self) -> bool:
        try:
            return bool(self.get_device_type())
        except Exception:
            return False

    def get_device_type(self):
        return self.amc.description.getDeviceType()

    def get_position(self) -> tuple[float,  float,  float]:
        x, y, z, v1, v2, v3 = self.amc.control.getPositionsAndVoltages()
        return x, y, z

    def get_control_amplitude(self, axis: str | int) -> float:
        return self.amc.control.getControlAmplitude(axis_to_id(axis))

    def get_control_frequency(self, axis: str | int) -> float:
        return self.amc.control.getControlFrequency(axis_to_id(axis))

    def get_control_dc_value(self, axis: str | int) -> float:
        return self.amc.control.getControlFixOutputVoltage(axis_to_id(axis))

    def set_position(self, x_nm:int=0, y_nm:int=0, z_nm:int=0, move_x:bool=False, move_y:bool=False, move_z:bool=False) -> None:
        '''
        Moves the piezo to the position specified by x_nm, y_nm,z_nm
        '''
        if not self.__check_position_limits(x_nm, y_nm, z_nm, move_x, move_y, move_z):
            error_details = self.__position_limit_error_message(x_nm, y_nm, z_nm, move_x, move_y, move_z)
            raise ValueError(
                "Requested piezo position is outside the allowed limits: "
                + error_details
                + ". Did not execute the move command."
            )

        for ax, mov in zip([0, 1, 2], [move_x, move_y, move_z]):
            if mov:
                self.set_control_move(ax, True)
        self.amc.control.MultiAxisPositioning(int(move_x), int(move_y), int(move_z), x_nm, y_nm, z_nm)

    def is_axis_moving(self) -> tuple[bool,  bool,  bool]:
        x_moving, y_moving, z_moving = self.amc.control.getStatusMovingAllAxes()
        return bool(x_moving), bool(y_moving), bool(z_moving)

    def set_control_move(self, axis: str | int, move: bool) -> None:
        self.amc.control.setControlMove(axis_to_id(axis), bool(move))

    def set_ground(self, axis: str | int, ground: bool):
        self.amc.move.setGroundAxis(axis_to_id(axis), bool(ground))

    ##################################### PRIVATE METHODS #####################################

    def __check_position_limits(self, x:int, y:int, z:int, move_x:bool, move_y:bool, move_z:bool) -> bool:
        if move_x:
            if x < self.x_min or x > self.x_max:
                return False

        if move_y:
            if y < self.y_min or y > self.y_max:
                return False

        if move_z:
            if z < self.z_min or z > self.z_max:
                return False

        return True

    def __position_limit_error_message(self, x:int, y:int, z:int, move_x:bool, move_y:bool, move_z:bool) -> str:
        messages = []
        if move_x and (x < self.x_min or x > self.x_max):
            messages.append(f"x target {x} nm is outside [{self.x_min}, {self.x_max}] nm")

        if move_y and (y < self.y_min or y > self.y_max):
            messages.append(f"y target {y} nm is outside [{self.y_min}, {self.y_max}] nm")

        if move_z and (z < self.z_min or z > self.z_max):
            messages.append(f"z target {z} nm is outside [{self.z_min}, {self.z_max}] nm")

        return "; ".join(messages)
