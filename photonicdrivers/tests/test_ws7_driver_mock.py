"""WS7_Driver against the wlmData.dll mock (no wavemeter)."""
import pytest

from photonicdrivers.Mocks.WS7_DLL_Mock import WS7_DLL_Mock
from photonicdrivers.Wavemeters.WS7_Driver import WS7_Driver


def make_driver(**kwargs):
    driver = WS7_Driver.__new__(WS7_Driver)        # skip __init__: it loads the real DLL
    driver._dll = WS7_DLL_Mock(**kwargs)
    driver._bind_functions()
    driver.exposure_limits = None
    return driver


def test_power_per_channel_in_uW():
    driver = make_driver()
    driver._dll.power_uW[2] = 123.4
    assert driver.get_power_uW(2) == pytest.approx(123.4)
    assert driver.get_power_uW(1) == pytest.approx(10.0)


def test_power_is_none_when_not_measuring():
    driver = make_driver()
    driver._dll.measuring = False
    assert driver.get_power_uW(1) is None


@pytest.mark.parametrize("code", [-3, -4, -6])
def test_power_error_codes_raise(code):
    driver = make_driver()
    driver._dll.errors[1] = code
    with pytest.raises(RuntimeError, match=str(code)):
        driver.get_power_uW(1)


def test_missing_channel_raises():
    driver = make_driver(channels=4)
    with pytest.raises(RuntimeError, match="-6"):
        driver.get_power_uW(5)


def test_frequency_and_wavelength_unchanged():
    driver = make_driver()
    assert driver.get_frequency_THz(1) == pytest.approx(226.130)
    assert driver.get_frequency_GHz(1) == pytest.approx(226130.0)
    assert driver.get_wavelength_nm(1) == pytest.approx(299792458.0 / 226.130e12 * 1e9)


def test_switch_mode_channel_and_count():
    driver = make_driver(channels=4)
    assert driver.get_switch_mode() is True
    assert driver.get_channels_count() == 4
    driver._dll.switch_channel = 3
    assert driver.get_switch_channel() == 3


def test_set_switch_channel_only_in_non_switch_mode():
    driver = make_driver()
    driver.set_switch_channel(2)
    assert driver.get_switch_channel() == 1           # switch mode on: no effect
    driver._dll.switch_mode = 0
    driver.set_switch_channel(2)
    assert driver.get_switch_channel() == 2


def test_channel_states_round_trip():
    driver = make_driver()
    assert driver.get_switch_channel_states(3) == (True, True)
    driver.set_switch_channel_states(3, use=False, show=True)
    assert driver.get_switch_channel_states(3) == (False, True)
    assert driver._dll.channel_states[3] == [0, 1]


def test_channel_states_bad_channel_raises():
    driver = make_driver(channels=4)
    with pytest.raises(RuntimeError):
        driver.get_switch_channel_states(5)


def test_exposure_value_and_mode():
    driver = make_driver()
    driver._dll.exposure_ms[(2, 1)] = 12
    driver._dll.exposure_ms[(2, 2)] = 40
    assert driver.get_exposure_ms(2) == 12
    assert driver.get_exposure_ms(2, array=2) == 40
    assert driver.get_exposure_mode_auto(2) is True
    driver.set_exposure_mode_auto(2, False)
    assert driver.get_exposure_mode_auto(2) is False
    driver.set_exposure(2, 30)                         # unchanged: manual + both arrays
    assert driver.get_exposure_mode_auto(2) is False and driver.get_exposure_ms(2, 2) == 30
