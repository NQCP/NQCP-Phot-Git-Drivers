import pytest
import numpy as np

from photonicdrivers.Mocks.Piezo_AttocubeAMC_Driver_Mock import Piezo_AttocubeAMC_Driver_Mock


def test_attocube_mock_stores_nm_positions_and_moves_selected_axes():
    driver = Piezo_AttocubeAMC_Driver_Mock(initial_position_nm=(1.0, 2.0, 3.0))

    driver.set_position(x_nm=100, y_nm=200, z_nm=300, move_x=True, move_y=True, move_z=False)

    assert driver.get_position() == (100.0, 200.0, 3.0)
    assert driver.command_history[-1] == (100.0, 200.0, 300.0, True, True, False)


def test_attocube_mock_relative_move_uses_current_position():
    driver = Piezo_AttocubeAMC_Driver_Mock(initial_position_nm=(100.0, 200.0, 300.0))

    driver.set_position_relative(x_nm=10, y_nm=-20, z_nm=30, move_x=True, move_y=True, move_z=True)

    assert driver.get_position() == (110.0, 180.0, 330.0)


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


def test_attocube_mock_connect_state_and_motion_status():
    driver = Piezo_AttocubeAMC_Driver_Mock()

    assert driver.is_connected()
    assert driver.is_axis_moving() == (False, False, False)

    driver.disconnect()
    assert not driver.is_connected()

    driver.connect()
    assert driver.is_connected()
