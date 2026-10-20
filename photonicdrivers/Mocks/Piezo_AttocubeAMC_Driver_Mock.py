from photonicdrivers.Abstract.Connectable import Connectable
from photonicdrivers.Piezo_AttocubeAMC.Piezo_AttocubeAMC_Driver import axis_to_id
from dataclasses import dataclass
import numpy as np
import time


@dataclass(frozen=True)
class PiezoHoningConfig:
    time_constant_s: float = 0.02
    stop_radius_nm: float = 100.0
    hover_noise_floor_nm: float = 25.0
    hover_noise_slow_nm: float = 75.0
    hover_speed_ref_nm_per_s: float = 50_000.0


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
        xy_distance_error_floor_nm: float = 0.0,
        xy_distance_error_per_nm: float = 0.0,
        xy_distance_error_cap_nm: float | None = None,
        xy_error_mode: str = "gaussian",
        movement_speed_nm_per_s: float | None = None,
        honing: PiezoHoningConfig | None = None,
        random_seed: int | None = None,
    ) -> None:
        if movement_speed_nm_per_s is not None and movement_speed_nm_per_s <= 0.0:
            raise ValueError("movement_speed_nm_per_s must be positive or None")
        if xy_distance_error_floor_nm < 0.0:
            raise ValueError("xy_distance_error_floor_nm must be >= 0")
        if xy_distance_error_per_nm < 0.0:
            raise ValueError("xy_distance_error_per_nm must be >= 0")
        if xy_distance_error_cap_nm is not None and xy_distance_error_cap_nm < 0.0:
            raise ValueError("xy_distance_error_cap_nm must be >= 0 or None")
        if xy_error_mode not in {"gaussian", "bounded"}:
            raise ValueError("xy_error_mode must be 'gaussian' or 'bounded'")
        self._validate_honing(honing)

        self.x_min = x_min_nm
        self.x_max = x_max_nm
        self.y_min = y_min_nm
        self.y_max = y_max_nm
        self.z_min = z_min_nm
        self.z_max = z_max_nm
        self.x_position_error_std_nm = float(x_position_error_std_nm)
        self.y_position_error_std_nm = float(y_position_error_std_nm)
        self.xy_distance_error_floor_nm = float(xy_distance_error_floor_nm)
        self.xy_distance_error_per_nm = float(xy_distance_error_per_nm)
        self.xy_distance_error_cap_nm = None if xy_distance_error_cap_nm is None else float(xy_distance_error_cap_nm)
        self.xy_error_mode = xy_error_mode
        self.movement_speed_nm_per_s = None if movement_speed_nm_per_s is None else float(movement_speed_nm_per_s)
        self.honing = honing
        self._rng = np.random.default_rng(random_seed)
        self.position = tuple(float(value) for value in initial_position_nm)
        self._motion_start_position = self.position
        self._motion_target_position = self.position
        self._motion_requested_position = self.position
        self._motion_started_at = 0.0
        self._motion_duration_s = 0.0
        self._motion_phase = "idle"
        self._moving_axes = (False, False, False)
        self.connected = True
        self.command_history: list[tuple[float, float, float, bool, bool, bool]] = []
        self.actual_position_history: list[tuple[float, float, float]] = []
        self.position_error_history: list[tuple[float, float, float]] = []
        self.control_move_enabled = [False, False, False]
        self.ground_enabled = [False, False, False]

    def connect(self) -> None:
        self.connected = True

    def disconnect(self) -> None:
        self.connected = False

    def is_connected(self) -> bool:
        return bool(self.connected)

    def get_device_type(self) -> str:
        return "Mock Piezo Attocube AMC"

    def get_position(self) -> tuple[float, float, float]:
        self._advance_motion()
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
    ) -> None:
        x0, y0, z0 = self.get_position()
        requested_position = (
            float(x_nm) if move_x else x0,
            float(y_nm) if move_y else y0,
            float(z_nm) if move_z else z0,
        )
        distance_error_std = self._distance_error_std_nm(
            start=(x0, y0, z0),
            target=requested_position,
            moving_axes=(bool(move_x), bool(move_y), bool(move_z)),
        )
        x_std = self._combined_error_std_nm(self.x_position_error_std_nm, distance_error_std) if move_x else 0.0
        y_std = self._combined_error_std_nm(self.y_position_error_std_nm, distance_error_std) if move_y else 0.0
        x_error, y_error = self._sample_xy_error(x_std, y_std, move_x, move_y)
        x = requested_position[0] + x_error if move_x else x0
        y = requested_position[1] + y_error if move_y else y0
        z = float(z_nm) if move_z else z0
        self._check_limits(x, y, z, move_x, move_y, move_z)

        target_position = (x, y, z)
        if self.movement_speed_nm_per_s is None:
            self.position = target_position
            if self.honing is None:
                self._clear_motion()
            else:
                self._start_honing(requested_position, (bool(move_x), bool(move_y), bool(move_z)))
        else:
            self._start_motion(target_position, (bool(move_x), bool(move_y), bool(move_z)), requested_position)

        self.command_history.append((float(x_nm), float(y_nm), float(z_nm), bool(move_x), bool(move_y), bool(move_z)))
        self.actual_position_history.append(target_position)
        self.position_error_history.append((x_error, y_error, 0.0))

    def is_axis_moving(self) -> tuple[bool, bool, bool]:
        self._advance_motion()
        return self._moving_axes

    def set_control_move(self, axis: str | int, move: bool) -> None:
        self.control_move_enabled[axis_to_id(axis)] = bool(move)

    def set_ground(self, axis: str | int, ground: bool) -> None:
        axis_id = axis_to_id(axis)
        self._advance_motion()
        self.ground_enabled[axis_id] = bool(ground)
        if ground and self._moving_axes[axis_id]:
            moving_axes = list(self._moving_axes)
            moving_axes[axis_id] = False
            self._restart_remaining_motion(tuple(moving_axes))

    def _validate_honing(self, honing: PiezoHoningConfig | None) -> None:
        if honing is None:
            return
        if honing.time_constant_s <= 0.0:
            raise ValueError("honing.time_constant_s must be > 0")
        if honing.stop_radius_nm < 0.0:
            raise ValueError("honing.stop_radius_nm must be >= 0")
        if honing.hover_noise_floor_nm < 0.0:
            raise ValueError("honing.hover_noise_floor_nm must be >= 0")
        if honing.hover_noise_slow_nm < 0.0:
            raise ValueError("honing.hover_noise_slow_nm must be >= 0")
        if honing.hover_speed_ref_nm_per_s <= 0.0:
            raise ValueError("honing.hover_speed_ref_nm_per_s must be > 0")

    def _sample_position_error(self, std_nm: float) -> float:
        if std_nm <= 0.0:
            return 0.0
        return float(self._rng.normal(loc=0.0, scale=float(std_nm)))

    def _sample_xy_error(
        self,
        x_std_nm: float,
        y_std_nm: float,
        move_x: bool,
        move_y: bool,
    ) -> tuple[float, float]:
        if self.xy_error_mode == "gaussian":
            return (
                self._sample_position_error(x_std_nm) if move_x else 0.0,
                self._sample_position_error(y_std_nm) if move_y else 0.0,
            )

        radius_nm = max(float(x_std_nm), float(y_std_nm))
        if radius_nm <= 0.0:
            return 0.0, 0.0
        angle = float(self._rng.uniform(0.0, 2.0 * np.pi))
        radius = radius_nm * float(np.sqrt(self._rng.random()))
        x_error = radius * float(np.cos(angle)) if move_x else 0.0
        y_error = radius * float(np.sin(angle)) if move_y else 0.0
        return x_error, y_error

    def _combined_error_std_nm(self, axis_std_nm: float, distance_std_nm: float) -> float:
        return float(np.hypot(float(axis_std_nm), float(distance_std_nm)))

    def _distance_error_std_nm(
        self,
        start: tuple[float, float, float],
        target: tuple[float, float, float],
        moving_axes: tuple[bool, bool, bool],
    ) -> float:
        if self.xy_distance_error_floor_nm == 0.0 and self.xy_distance_error_per_nm == 0.0:
            return 0.0
        xy_distance_nm = self._motion_distance_nm(start[:2] + (0.0,), target[:2] + (0.0,), moving_axes[:2] + (False,))
        std_nm = float(np.hypot(self.xy_distance_error_floor_nm, self.xy_distance_error_per_nm * xy_distance_nm))
        if self.xy_distance_error_cap_nm is not None:
            std_nm = min(std_nm, self.xy_distance_error_cap_nm)
        return std_nm

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

    def _start_motion(
        self,
        target_position: tuple[float, float, float],
        moving_axes: tuple[bool, bool, bool],
        requested_position: tuple[float, float, float] | None = None,
    ) -> None:
        moving_axes = tuple(bool(axis) for axis in moving_axes)
        self._motion_start_position = self.position
        self._motion_target_position = target_position
        self._motion_requested_position = target_position if requested_position is None else requested_position
        self._motion_started_at = time.monotonic()
        self._motion_phase = "coarse"
        self._moving_axes = moving_axes
        distance_nm = self._motion_distance_nm(self.position, target_position, moving_axes)
        self._motion_duration_s = distance_nm / float(self.movement_speed_nm_per_s)
        if distance_nm == 0.0:
            self.position = target_position
            if self.honing is None:
                self._clear_motion()
            else:
                self._start_honing(self._motion_requested_position, moving_axes)

    def _start_honing(
        self,
        requested_position: tuple[float, float, float],
        moving_axes: tuple[bool, bool, bool],
    ) -> None:
        if self._is_within_honing_stop_radius(self.position, requested_position, moving_axes):
            self.position = self._final_honed_position(requested_position, moving_axes)
            self._clear_motion()
            return

        self._motion_start_position = self.position
        self._motion_target_position = requested_position
        self._motion_requested_position = requested_position
        self._motion_started_at = time.monotonic()
        self._motion_duration_s = 0.0
        self._motion_phase = "honing"
        self._moving_axes = moving_axes

    def _advance_motion(self) -> None:
        if not any(self._moving_axes):
            return

        if self._motion_phase == "honing":
            self._advance_honing()
            return

        elapsed_s = time.monotonic() - self._motion_started_at
        if elapsed_s >= self._motion_duration_s:
            self.position = self._motion_target_position
            if self.honing is None:
                self._clear_motion()
            else:
                self._start_honing(self._motion_requested_position, self._moving_axes)
            return

        fraction = max(0.0, elapsed_s / self._motion_duration_s)
        self.position = tuple(
            start + fraction * (target - start) if moving else current
            for start, target, current, moving in zip(
                self._motion_start_position,
                self._motion_target_position,
                self.position,
                self._moving_axes,
            )
        )

    def _advance_honing(self) -> None:
        honing = self.honing
        if honing is None:
            self._clear_motion()
            return

        elapsed_s = max(0.0, time.monotonic() - self._motion_started_at)
        decay = float(np.exp(-elapsed_s / honing.time_constant_s))
        systematic_position = tuple(
            requested + (start - requested) * decay if moving else current
            for start, requested, current, moving in zip(
                self._motion_start_position,
                self._motion_requested_position,
                self.position,
                self._moving_axes,
            )
        )

        if self._is_within_honing_stop_radius(systematic_position, self._motion_requested_position, self._moving_axes):
            self.position = self._final_honed_position(self._motion_requested_position, self._moving_axes)
            self._clear_motion()
            return

        noise = self._sample_hover_noise(systematic_position)
        self.position = tuple(
            systematic + offset if moving else current
            for systematic, offset, current, moving in zip(systematic_position, noise, self.position, self._moving_axes)
        )

    def _restart_remaining_motion(self, moving_axes: tuple[bool, bool, bool]) -> None:
        if any(moving_axes):
            target = tuple(
                target if moving else current
                for target, current, moving in zip(self._motion_target_position, self.position, moving_axes)
            )
            requested = tuple(
                requested if moving else current
                for requested, current, moving in zip(self._motion_requested_position, self.position, moving_axes)
            )
            self._start_motion(target, moving_axes, requested)
        else:
            self._clear_motion()

    def _clear_motion(self) -> None:
        self._motion_start_position = self.position
        self._motion_target_position = self.position
        self._motion_requested_position = self.position
        self._motion_started_at = 0.0
        self._motion_duration_s = 0.0
        self._motion_phase = "idle"
        self._moving_axes = (False, False, False)

    def _is_within_honing_stop_radius(
        self,
        position: tuple[float, float, float],
        target: tuple[float, float, float],
        moving_axes: tuple[bool, bool, bool],
    ) -> bool:
        if self.honing is None:
            return True
        return self._motion_distance_nm(position, target, moving_axes) <= self.honing.stop_radius_nm

    def _sample_hover_noise(self, systematic_position: tuple[float, float, float]) -> tuple[float, float, float]:
        honing = self.honing
        if honing is None:
            return 0.0, 0.0, 0.0

        error_nm = self._motion_distance_nm(systematic_position, self._motion_requested_position, self._moving_axes)
        effective_speed_nm_per_s = error_nm / honing.time_constant_s
        noise_std_nm = honing.hover_noise_floor_nm + honing.hover_noise_slow_nm / (
            1.0 + effective_speed_nm_per_s / honing.hover_speed_ref_nm_per_s
        )
        x_noise = self._sample_position_error(noise_std_nm) if self._moving_axes[0] else 0.0
        y_noise = self._sample_position_error(noise_std_nm) if self._moving_axes[1] else 0.0
        z_noise = self._sample_position_error(noise_std_nm) if self._moving_axes[2] else 0.0
        return x_noise, y_noise, z_noise

    def _final_honed_position(
        self,
        requested_position: tuple[float, float, float],
        moving_axes: tuple[bool, bool, bool],
    ) -> tuple[float, float, float]:
        honing = self.honing
        if honing is None or honing.stop_radius_nm == 0.0:
            return requested_position

        radius_nm = 0.5 * honing.stop_radius_nm
        x_error, y_error = self._sample_bounded_xy_error(radius_nm, moving_axes[0], moving_axes[1])
        z_error = self._rng.uniform(-radius_nm, radius_nm) if moving_axes[2] else 0.0
        return (
            requested_position[0] + x_error if moving_axes[0] else self.position[0],
            requested_position[1] + y_error if moving_axes[1] else self.position[1],
            requested_position[2] + z_error if moving_axes[2] else self.position[2],
        )

    def _sample_bounded_xy_error(self, radius_nm: float, move_x: bool, move_y: bool) -> tuple[float, float]:
        if radius_nm <= 0.0 or not (move_x or move_y):
            return 0.0, 0.0
        if move_x and move_y:
            angle = float(self._rng.uniform(0.0, 2.0 * np.pi))
            radius = radius_nm * float(np.sqrt(self._rng.random()))
            return radius * float(np.cos(angle)), radius * float(np.sin(angle))
        error = float(self._rng.uniform(-radius_nm, radius_nm))
        return (error, 0.0) if move_x else (0.0, error)

    def _motion_distance_nm(
        self,
        start: tuple[float, float, float],
        target: tuple[float, float, float],
        moving_axes: tuple[bool, bool, bool],
    ) -> float:
        delta = [
            target_value - start_value if moving else 0.0
            for start_value, target_value, moving in zip(start, target, moving_axes)
        ]
        return float(np.linalg.norm(delta))
