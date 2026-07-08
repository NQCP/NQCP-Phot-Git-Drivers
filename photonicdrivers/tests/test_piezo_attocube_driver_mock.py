import pytest
import numpy as np
import photonicdrivers.Mocks.Piezo_AttocubeAMC_Driver_Mock as piezo_mock_module

from photonicdrivers.Mocks.Piezo_AttocubeAMC_Driver_Mock import PiezoHoningConfig, Piezo_AttocubeAMC_Driver_Mock
from photonicdrivers.Piezo_AttocubeAMC.Piezo_AttocubeAMC_Driver import Piezo_AttocubeAMC_Driver, axis_to_id


def test_attocube_mock_stores_nm_positions_and_moves_selected_axes():
    driver = Piezo_AttocubeAMC_Driver_Mock(initial_position_nm=(1.0, 2.0, 3.0))

    driver.set_position(x_nm=100, y_nm=200, z_nm=300, move_x=True, move_y=True, move_z=False)

    assert driver.get_position() == (100.0, 200.0, 3.0)
    assert driver.command_history[-1] == (100.0, 200.0, 300.0, True, True, False)


def test_attocube_mock_rejects_out_of_range_moves():
    driver = Piezo_AttocubeAMC_Driver_Mock(x_min_nm=-10, x_max_nm=10)

    with pytest.raises(ValueError, match="x target"):
        driver.set_position(x_nm=11, move_x=True)

    assert driver.get_position() == (0.0, 0.0, 0.0)


def test_attocube_mock_can_apply_configurable_xy_landing_error():
    driver = Piezo_AttocubeAMC_Driver_Mock(
        x_position_error_std_nm=1000.0,
        y_position_error_std_nm=1000.0,
        random_seed=123,
    )
    expected_errors = np.random.default_rng(123).normal(loc=0.0, scale=1000.0, size=2)

    driver.set_position(x_nm=10_000, y_nm=20_000, move_x=True, move_y=True)

    assert driver.get_position() == pytest.approx((
        10_000.0 + expected_errors[0],
        20_000.0 + expected_errors[1],
        0.0,
    ))
    assert driver.command_history[-1] == (10_000.0, 20_000.0, 0.0, True, True, False)
    assert driver.position_error_history[-1] == pytest.approx((expected_errors[0], expected_errors[1], 0.0))


def test_attocube_mock_distance_error_scales_with_move_distance():
    driver = Piezo_AttocubeAMC_Driver_Mock(
        xy_distance_error_floor_nm=500.0,
        xy_distance_error_per_nm=0.02,
        xy_distance_error_cap_nm=3000.0,
        random_seed=123,
    )
    expected_std = np.hypot(500.0, 0.02 * 100_000.0)
    expected_errors = np.random.default_rng(123).normal(loc=0.0, scale=expected_std, size=2)

    driver.set_position(x_nm=100_000, y_nm=0, move_x=True, move_y=True)

    assert driver.position_error_history[-1] == pytest.approx((expected_errors[0], expected_errors[1], 0.0))
    assert driver.get_position() == pytest.approx((100_000.0 + expected_errors[0], expected_errors[1], 0.0))


def test_attocube_mock_distance_error_has_floor_for_small_moves():
    driver = Piezo_AttocubeAMC_Driver_Mock(
        xy_distance_error_floor_nm=500.0,
        xy_distance_error_per_nm=0.02,
        random_seed=123,
    )
    expected_std = np.hypot(500.0, 0.02 * 1_000.0)
    expected_errors = np.random.default_rng(123).normal(loc=0.0, scale=expected_std, size=2)

    driver.set_position(x_nm=1_000, y_nm=0, move_x=True, move_y=True)

    assert driver.position_error_history[-1] == pytest.approx((expected_errors[0], expected_errors[1], 0.0))


def test_attocube_mock_distance_error_is_capped():
    driver = Piezo_AttocubeAMC_Driver_Mock(
        xy_distance_error_floor_nm=500.0,
        xy_distance_error_per_nm=0.02,
        xy_distance_error_cap_nm=3000.0,
        random_seed=123,
    )
    expected_errors = np.random.default_rng(123).normal(loc=0.0, scale=3000.0, size=2)

    driver.set_position(x_nm=1_000_000, y_nm=0, move_x=True, move_y=True)

    assert driver.position_error_history[-1] == pytest.approx((expected_errors[0], expected_errors[1], 0.0))


def test_attocube_mock_bounded_distance_error_stays_inside_radius():
    driver = Piezo_AttocubeAMC_Driver_Mock(
        xy_distance_error_floor_nm=500.0,
        xy_distance_error_per_nm=0.02,
        xy_distance_error_cap_nm=3000.0,
        xy_error_mode="bounded",
        random_seed=123,
    )

    driver.set_position(x_nm=1_000_000, y_nm=0, move_x=True, move_y=True)

    x_error, y_error, _ = driver.position_error_history[-1]
    assert np.hypot(x_error, y_error) <= 3000.0


def test_attocube_mock_connect_state_and_motion_status():
    driver = Piezo_AttocubeAMC_Driver_Mock()

    assert driver.is_connected()
    assert driver.is_axis_moving() == (False, False, False)

    driver.disconnect()
    assert not driver.is_connected()

    driver.connect()
    assert driver.is_connected()


def test_attocube_mock_gradual_motion_interpolates_along_straight_line(monkeypatch):
    now = 0.0
    monkeypatch.setattr(piezo_mock_module.time, "monotonic", lambda: now)
    driver = Piezo_AttocubeAMC_Driver_Mock(movement_speed_nm_per_s=10.0)

    driver.set_position(x_nm=6, y_nm=8, move_x=True, move_y=True)

    assert driver.get_position() == (0.0, 0.0, 0.0)
    assert driver.is_axis_moving() == (True, True, False)

    now = 0.5
    assert driver.get_position() == pytest.approx((3.0, 4.0, 0.0))
    assert driver.is_axis_moving() == (True, True, False)

    now = 1.0
    assert driver.get_position() == pytest.approx((6.0, 8.0, 0.0))
    assert driver.is_axis_moving() == (False, False, False)


def test_attocube_mock_honing_config_has_defaults():
    config = PiezoHoningConfig()

    assert config.time_constant_s > 0.0
    assert config.stop_radius_nm >= 0.0
    assert config.hover_noise_floor_nm >= 0.0
    assert config.hover_noise_slow_nm >= 0.0
    assert config.hover_speed_ref_nm_per_s > 0.0


def test_attocube_mock_honing_none_preserves_noisy_landing_behavior():
    driver = Piezo_AttocubeAMC_Driver_Mock(
        xy_distance_error_floor_nm=1000.0,
        xy_distance_error_per_nm=0.0,
        honing=None,
        random_seed=123,
    )
    expected_errors = np.random.default_rng(123).normal(loc=0.0, scale=1000.0, size=2)

    driver.set_position(x_nm=10_000, y_nm=0, move_x=True, move_y=True)

    assert driver.get_position() == pytest.approx((10_000.0 + expected_errors[0], expected_errors[1], 0.0))
    assert driver.is_axis_moving() == (False, False, False)


def test_attocube_mock_honing_decays_to_requested_target(monkeypatch):
    now = 0.0
    monkeypatch.setattr(piezo_mock_module.time, "monotonic", lambda: now)
    driver = Piezo_AttocubeAMC_Driver_Mock(
        xy_distance_error_floor_nm=1000.0,
        xy_distance_error_per_nm=0.0,
        movement_speed_nm_per_s=10_000.0,
        honing=PiezoHoningConfig(
            time_constant_s=0.1,
            stop_radius_nm=100.0,
            hover_noise_floor_nm=0.0,
            hover_noise_slow_nm=0.0,
        ),
        random_seed=123,
    )

    driver.set_position(x_nm=10_000, y_nm=0, move_x=True, move_y=True)

    now = 1.2
    assert driver.is_axis_moving() == (True, True, False)
    assert np.linalg.norm(np.array(driver.get_position()[:2]) - np.array([10_000.0, 0.0])) > 100.0

    now = 1.6
    assert driver.is_axis_moving() == (False, False, False)
    assert np.linalg.norm(np.array(driver.get_position()[:2]) - np.array([10_000.0, 0.0])) <= 100.0


def test_attocube_mock_gradual_motion_retargets_from_current_position(monkeypatch):
    now = 0.0
    monkeypatch.setattr(piezo_mock_module.time, "monotonic", lambda: now)
    driver = Piezo_AttocubeAMC_Driver_Mock(movement_speed_nm_per_s=10.0)
    driver.set_position(x_nm=10, move_x=True)

    now = 0.4
    driver.set_position(x_nm=4, y_nm=3, move_x=True, move_y=True)

    assert driver.get_position() == pytest.approx((4.0, 0.0, 0.0))
    now = 0.55
    assert driver.get_position() == pytest.approx((4.0, 1.5, 0.0))
    now = 0.71
    assert driver.get_position() == pytest.approx((4.0, 3.0, 0.0))
    assert driver.is_axis_moving() == (False, False, False)


def test_attocube_mock_ground_freezes_moving_axis(monkeypatch):
    now = 0.0
    monkeypatch.setattr(piezo_mock_module.time, "monotonic", lambda: now)
    driver = Piezo_AttocubeAMC_Driver_Mock(movement_speed_nm_per_s=10.0)
    driver.set_position(x_nm=6, y_nm=8, move_x=True, move_y=True)

    now = 0.5
    driver.set_ground("x", True)

    assert driver.get_position() == pytest.approx((3.0, 4.0, 0.0))
    assert driver.is_axis_moving() == (False, True, False)

    now = 0.9
    assert driver.get_position() == pytest.approx((3.0, 8.0, 0.0))
    assert driver.is_axis_moving() == (False, False, False)


def test_attocube_mock_rejects_nonpositive_gradual_motion_speed():
    with pytest.raises(ValueError, match="movement_speed_nm_per_s"):
        Piezo_AttocubeAMC_Driver_Mock(movement_speed_nm_per_s=0.0)

    with pytest.raises(ValueError, match="movement_speed_nm_per_s"):
        Piezo_AttocubeAMC_Driver_Mock(movement_speed_nm_per_s=-1.0)


def test_attocube_mock_rejects_invalid_distance_error_settings():
    with pytest.raises(ValueError, match="xy_distance_error_floor_nm"):
        Piezo_AttocubeAMC_Driver_Mock(xy_distance_error_floor_nm=-1.0)

    with pytest.raises(ValueError, match="xy_distance_error_per_nm"):
        Piezo_AttocubeAMC_Driver_Mock(xy_distance_error_per_nm=-1.0)

    with pytest.raises(ValueError, match="xy_distance_error_cap_nm"):
        Piezo_AttocubeAMC_Driver_Mock(xy_distance_error_cap_nm=-1.0)

    with pytest.raises(ValueError, match="xy_error_mode"):
        Piezo_AttocubeAMC_Driver_Mock(xy_error_mode="invalid")


def test_attocube_mock_rejects_invalid_honing_settings():
    with pytest.raises(ValueError, match="time_constant_s"):
        Piezo_AttocubeAMC_Driver_Mock(honing=PiezoHoningConfig(time_constant_s=0.0))

    with pytest.raises(ValueError, match="stop_radius_nm"):
        Piezo_AttocubeAMC_Driver_Mock(honing=PiezoHoningConfig(stop_radius_nm=-1.0))

    with pytest.raises(ValueError, match="hover_noise_floor_nm"):
        Piezo_AttocubeAMC_Driver_Mock(honing=PiezoHoningConfig(hover_noise_floor_nm=-1.0))

    with pytest.raises(ValueError, match="hover_noise_slow_nm"):
        Piezo_AttocubeAMC_Driver_Mock(honing=PiezoHoningConfig(hover_noise_slow_nm=-1.0))

    with pytest.raises(ValueError, match="hover_speed_ref_nm_per_s"):
        Piezo_AttocubeAMC_Driver_Mock(honing=PiezoHoningConfig(hover_speed_ref_nm_per_s=0.0))


def test_axis_to_id_accepts_only_xyz_or_axis_numbers():
    assert axis_to_id("x") == 0
    assert axis_to_id("Y") == 1
    assert axis_to_id("z") == 2
    assert axis_to_id(0) == 0
    assert axis_to_id(1) == 1
    assert axis_to_id(2) == 2

    with pytest.raises(ValueError):
        axis_to_id("a")
    with pytest.raises(ValueError):
        axis_to_id(3)
    with pytest.raises(TypeError):
        axis_to_id(True)


def test_attocube_mock_validates_ground_and_control_move_axes():
    driver = Piezo_AttocubeAMC_Driver_Mock()

    driver.set_ground("x", True)
    driver.set_ground(2, True)
    driver.set_control_move("y", True)
    driver.set_control_move(1, False)

    assert driver.ground_enabled == [True, False, True]
    assert driver.control_move_enabled == [False, False, False]

    with pytest.raises(ValueError):
        driver.set_ground("invalid", True)
    with pytest.raises(ValueError):
        driver.set_control_move(3, True)


class _FakeControl:
    def __init__(self):
        self.control_move_history = []
        self.positioning_history = []

    def setControlMove(self, axis, move):
        self.control_move_history.append((axis, move))

    def MultiAxisPositioning(self, move_x, move_y, move_z, x_nm, y_nm, z_nm):
        self.positioning_history.append((move_x, move_y, move_z, x_nm, y_nm, z_nm))


class _FakeAMC:
    def __init__(self):
        self.control = _FakeControl()


def _make_attocube_driver_without_connection():
    driver = Piezo_AttocubeAMC_Driver.__new__(Piezo_AttocubeAMC_Driver)
    driver.x_min = 0
    driver.x_max = 10
    driver.y_min = 100
    driver.y_max = 200
    driver.z_min = -5
    driver.z_max = 5
    driver.amc = _FakeAMC()
    return driver


def test_attocube_driver_limit_error_lists_all_out_of_range_axes():
    driver = _make_attocube_driver_without_connection()

    with pytest.raises(ValueError) as exc_info:
        driver.set_position(x_nm=11, y_nm=99, z_nm=0, move_x=True, move_y=True, move_z=True)

    message = str(exc_info.value)
    assert "x target 11 nm is outside [0, 10] nm" in message
    assert "y target 99 nm is outside [100, 200] nm" in message
    assert "z target" not in message
    assert driver.amc.control.control_move_history == []
    assert driver.amc.control.positioning_history == []
