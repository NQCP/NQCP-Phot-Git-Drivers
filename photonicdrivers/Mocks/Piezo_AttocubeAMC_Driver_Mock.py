from photonicdrivers.Abstract.Connectable import Connectable
import numpy as np


class Piezo_AttocubeAMC_Driver_Mock(Connectable):
    def __init__(
        self,
        x_min_nm: int = -5_000_000,
        x_max_nm: int = 5_000_000,
        y_min_nm: int = -5_000_000,
        y_max_nm: int = 5_000_000,
        z_min_nm: int = -5_000_000,
        z_max_nm: int = 5_000_000,
        initial_position_nm: tuple[float, float, float] = (0.0, 0.0, 0.0),
        x_position_error_std_nm: float = 0.0,
        y_position_error_std_nm: float = 0.0,
        random_seed: int | None = None,
    ) -> None:
        self.x_min = x_min_nm
        self.x_max = x_max_nm
        self.y_min = y_min_nm
        self.y_max = y_max_nm
        self.z_min = z_min_nm
        self.z_max = z_max_nm
        self.x_position_error_std_nm = float(x_position_error_std_nm)
        self.y_position_error_std_nm = float(y_position_error_std_nm)
        self._rng = np.random.default_rng(random_seed)
        self.position = tuple(float(value) for value in initial_position_nm)
        self.connected = True
        self.command_history: list[tuple[float, float, float, bool, bool, bool]] = []
        self.actual_position_history: list[tuple[float, float, float]] = []
        self.position_error_history: list[tuple[float, float, float]] = []

    def connect(self) -> None:
        self.connected = True

    def disconnect(self) -> None:
        self.connected = False

    def is_connected(self) -> bool:
        return bool(self.connected)

    def get_device_type(self) -> str:
        return "Mock Piezo Attocube AMC"

    def get_position(self) -> tuple[float, float, float]:
        return self.position

    def get_x(self) -> float:
        return self.position[0]

    def get_y(self) -> float:
        return self.position[1]

    def get_z(self) -> float:
        return self.position[2]

    def set_position(
        self,
        x_nm: int = 0,
        y_nm: int = 0,
        z_nm: int = 0,
        move_x: bool = False,
        move_y: bool = False,
        move_z: bool = False,
        wait_while_moving: bool = True,
    ) -> None:
        x0, y0, z0 = self.position
        x_error = self._sample_position_error(self.x_position_error_std_nm) if move_x else 0.0
        y_error = self._sample_position_error(self.y_position_error_std_nm) if move_y else 0.0
        x = float(x_nm) + x_error if move_x else x0
        y = float(y_nm) + y_error if move_y else y0
        z = float(z_nm) if move_z else z0
        self._check_limits(x, y, z, move_x, move_y, move_z)

        self.position = (x, y, z)
        self.command_history.append((float(x_nm), float(y_nm), float(z_nm), bool(move_x), bool(move_y), bool(move_z)))
        self.actual_position_history.append(self.position)
        self.position_error_history.append((x_error, y_error, 0.0))

    def set_position_relative(
        self,
        x_nm: int = 0,
        y_nm: int = 0,
        z_nm: int = 0,
        move_x: bool = False,
        move_y: bool = False,
        move_z: bool = False,
        wait_while_moving: bool = True,
    ) -> None:
        x0, y0, z0 = self.position
        self.set_position(
            x_nm=int(x0 + x_nm),
            y_nm=int(y0 + y_nm),
            z_nm=int(z0 + z_nm),
            move_x=move_x,
            move_y=move_y,
            move_z=move_z,
            wait_while_moving=wait_while_moving,
        )

    def set_x(self, position: int) -> None:
        self.set_position(x_nm=int(position), move_x=True)

    def set_y(self, position: int) -> None:
        self.set_position(y_nm=int(position), move_y=True)

    def set_z(self, position: int) -> None:
        self.set_position(z_nm=int(position), move_z=True)

    def is_axis_moving(self) -> tuple[bool, bool, bool]:
        return False, False, False

    def set_ground(self, axis: str, ground: bool) -> None:
        return None

    def set_ground_all(self, ground: bool) -> None:
        return None

    def _sample_position_error(self, std_nm: float) -> float:
        if std_nm <= 0.0:
            return 0.0
        return float(self._rng.normal(loc=0.0, scale=float(std_nm)))

    def _check_limits(
        self,
        x_nm: float,
        y_nm: float,
        z_nm: float,
        move_x: bool,
        move_y: bool,
        move_z: bool,
    ) -> None:
        if move_x and not (self.x_min <= x_nm <= self.x_max):
            raise ValueError(f"x target {x_nm} nm is outside [{self.x_min}, {self.x_max}] nm")
        if move_y and not (self.y_min <= y_nm <= self.y_max):
            raise ValueError(f"y target {y_nm} nm is outside [{self.y_min}, {self.y_max}] nm")
        if move_z and not (self.z_min <= z_nm <= self.z_max):
            raise ValueError(f"z target {z_nm} nm is outside [{self.z_min}, {self.z_max}] nm")
