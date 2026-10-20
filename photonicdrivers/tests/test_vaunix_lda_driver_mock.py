import pytest

from photonicdrivers.Mocks.Vaunix_LDA_Driver_Mock import Vaunix_LDA_Driver_Mock
from photonicdrivers.Variable_Digital_Attenautor.Vaunix_LDA_Constants import (
    BAD_HID_IO,
    BAD_PARAMETER,
    DEVICE_NOT_READY,
    INVALID_DEVID,
    HAS_BIDIR_RAMPS,
    HAS_HIRES,
    HAS_MCHANNELS,
    HAS_PROFILES,
    PROFILE_ACTIVE,
    SWP_ACTIVE,
    Vaunix_LDA_Error,
    Vaunix_LDA_Feature_Error,
    Vaunix_LDA_Transport_Error,
    counts_to_db,
    counts_to_mhz,
    db_to_counts,
    describe_features,
    mhz_to_counts,
    round_half_up,
    u32,
)


# ==================== pure conversion helpers, no mock needed ====================


def test_u32_recovers_error_codes_that_ctypes_delivers_as_negative():
    # restype=c_int makes the DLL's 0x80010000 arrive in Python as -2147418112.
    assert u32(-2147483648) == INVALID_DEVID
    assert u32(-2147418112) == BAD_PARAMETER
    assert u32(-2147352576) == BAD_HID_IO
    assert u32(-2147287040) == DEVICE_NOT_READY
    # Legal values pass through untouched, including zero.
    assert u32(0) == 0
    assert u32(1800) == 1800

    # Every error code has bit 31 set; no legal return value does. That is what the
    # drivers' usb_checked() relies on to tell the two apart.
    for code in (INVALID_DEVID, BAD_PARAMETER, BAD_HID_IO, DEVICE_NOT_READY):
        assert code & 0x80000000
    for value in (0, 1, 1800, 80000):
        assert not value & 0x80000000


def test_round_half_up_is_not_bankers_rounding():
    # Python's round() would give 2 here, which would make neighbouring setpoints
    # quantise inconsistently.
    assert round_half_up(2.5) == 3
    assert round_half_up(3.5) == 4
    assert round_half_up(-2.5) == -3
    assert round_half_up(0.4999) == 0


def test_attenuation_counts_round_trip():
    assert db_to_counts(0.0) == 0
    assert db_to_counts(0.05) == 1
    assert db_to_counts(0.1) == 2
    assert db_to_counts(31.5) == 630
    # An LDA-908V reports 1800 counts of range, i.e. 90 dB.
    assert db_to_counts(90.0) == 1800
    assert counts_to_db(1800) == pytest.approx(90.0)
    assert counts_to_db(db_to_counts(63.25)) == pytest.approx(63.25)


def test_frequency_counts_round_trip():
    # 100 kHz units: an LDA-908V spans 2000..80000 counts.
    assert mhz_to_counts(200.0) == 2000
    assert mhz_to_counts(8000.0) == 80000
    assert mhz_to_counts(6000.0) == 60000
    assert counts_to_mhz(60000) == pytest.approx(6000.0)


def test_describe_features_names_the_bits():
    described = describe_features(HAS_BIDIR_RAMPS | HAS_PROFILES | HAS_HIRES)
    assert "0x00000007" in described
    assert "HAS_HIRES" in described
    assert "HAS_PROFILES" in described
    assert "no optional features" in describe_features(0)


# ==================== lifecycle ====================


def test_is_connected_tracks_connect_and_disconnect():
    driver = Vaunix_LDA_Driver_Mock()

    assert driver.is_connected() is False

    driver.connect()
    assert driver.is_connected() is True

    driver.disconnect()
    assert driver.is_connected() is False


def test_methods_before_connect_raise():
    driver = Vaunix_LDA_Driver_Mock()

    with pytest.raises(Vaunix_LDA_Error, match="requires an open connection"):
        driver.get_attenuation_dB()


def test_context_manager_connects_and_disconnects():
    driver = Vaunix_LDA_Driver_Mock()

    with driver as attenuator:
        assert attenuator.is_connected() is True

    assert driver.is_connected() is False


# ==================== attenuation ====================


def test_attenuation_round_trips_on_the_step_grid():
    driver = Vaunix_LDA_Driver_Mock()
    driver.connect()

    driver.set_attenuation_dB(31.5)

    assert driver.get_attenuation_dB() == pytest.approx(31.5)
    assert ("set_attenuation_dB", 1, 31.5) in driver.command_history


def test_off_grid_attenuation_is_quantized_to_the_hardware_step():
    driver = Vaunix_LDA_Driver_Mock()
    driver.connect()

    # The API unit is 0.05 dB but the LDA-908V resolves 0.1 dB, so 31.53 dB is not
    # representable and must land on the nearest 0.1 dB point.
    driver.set_attenuation_dB(31.53)
    assert driver.get_attenuation_dB() == pytest.approx(31.5)

    driver.set_attenuation_dB(31.57)
    assert driver.get_attenuation_dB() == pytest.approx(31.6)


def test_attenuation_at_the_exact_limits_is_accepted():
    driver = Vaunix_LDA_Driver_Mock()
    driver.connect()

    driver.set_attenuation_dB(0.0)
    assert driver.get_attenuation_dB() == pytest.approx(0.0)

    driver.set_attenuation_dB(90.0)
    assert driver.get_attenuation_dB() == pytest.approx(90.0)


def test_out_of_range_attenuation_is_rejected_not_clamped():
    driver = Vaunix_LDA_Driver_Mock()
    driver.connect()
    driver.set_attenuation_dB(10.0)

    with pytest.raises(ValueError, match=r"outside \[0.0, 90.0\] dB"):
        driver.set_attenuation_dB(95.0)

    with pytest.raises(ValueError, match=r"outside \[0.0, 90.0\] dB"):
        driver.set_attenuation_dB(-1.0)

    # A rejected request must not have moved the attenuator.
    assert driver.get_attenuation_dB() == pytest.approx(10.0)


def test_quantization_near_the_top_does_not_overshoot_the_limit():
    driver = Vaunix_LDA_Driver_Mock()
    driver.connect()

    # Rounding 89.99 up would give 1800 counts exactly; anything above the limit
    # must be pulled back rather than sent to the device.
    driver.set_attenuation_dB(89.99)
    assert driver.get_attenuation_dB() <= 90.0


def test_reported_limits_match_an_lda_908v():
    driver = Vaunix_LDA_Driver_Mock()
    driver.connect()

    assert driver.get_min_attenuation_dB() == pytest.approx(0.0)
    assert driver.get_max_attenuation_dB() == pytest.approx(90.0)
    assert driver.get_attenuation_step_dB() == pytest.approx(0.1)
    assert driver.get_min_frequency_MHz() == pytest.approx(200.0)
    assert driver.get_max_frequency_MHz() == pytest.approx(8000.0)
    assert driver.get_number_of_channels() == 1


# ==================== channels ====================


def test_channel_bounds_are_enforced_and_one_indexed():
    driver = Vaunix_LDA_Driver_Mock(number_of_channels=4)
    driver.connect()

    driver.set_channel(4)
    assert driver.get_channel() == 4

    with pytest.raises(ValueError, match=r"channel=0 is outside \[1, 4\]"):
        driver.set_channel(0)

    with pytest.raises(ValueError, match=r"channel=5 is outside \[1, 4\]"):
        driver.set_channel(5)


def test_reading_with_a_channel_argument_leaves_that_channel_selected():
    driver = Vaunix_LDA_Driver_Mock(number_of_channels=4)
    driver.connect()
    driver.set_attenuation_dB(12.0, channel=3)

    assert driver.get_attenuation_dB(channel=3) == pytest.approx(12.0)
    # Documented behaviour: the selection is deliberately not restored.
    assert driver.get_channel() == 3


def test_attenuation_is_tracked_per_channel():
    driver = Vaunix_LDA_Driver_Mock(number_of_channels=2)
    driver.connect()

    driver.set_attenuation_dB(5.0, channel=1)
    driver.set_attenuation_dB(20.0, channel=2)

    assert driver.get_attenuation_dB(channel=1) == pytest.approx(5.0)
    assert driver.get_attenuation_dB(channel=2) == pytest.approx(20.0)


# ==================== working frequency ====================


def test_frequency_round_trips_and_rejects_out_of_band_values():
    driver = Vaunix_LDA_Driver_Mock()
    driver.connect()

    driver.set_frequency_MHz(6000)
    assert driver.get_frequency_MHz() == pytest.approx(6000.0)

    with pytest.raises(ValueError, match=r"outside \[200.0, 8000.0\] MHz"):
        driver.set_frequency_MHz(100.0)

    with pytest.raises(ValueError, match=r"outside \[200.0, 8000.0\] MHz"):
        driver.set_frequency_MHz(9000.0)


# ==================== ramp ====================


def test_ramp_configuration_round_trips():
    driver = Vaunix_LDA_Driver_Mock()
    driver.connect()

    driver.set_ramp_start_dB(0.0)
    driver.set_ramp_end_dB(20.0)
    driver.set_ramp_step_dB(1.0)
    driver.set_ramp_dwell_time_ms(100)
    driver.set_ramp_idle_time_ms(0)

    assert driver.get_ramp_start_dB() == pytest.approx(0.0)
    assert driver.get_ramp_end_dB() == pytest.approx(20.0)
    assert driver.get_ramp_step_dB() == pytest.approx(1.0)
    assert driver.get_ramp_dwell_time_ms() == 100


def test_start_and_stop_ramp_are_visible_in_device_status():
    driver = Vaunix_LDA_Driver_Mock()
    driver.connect()

    assert driver.is_ramping() is False

    driver.start_ramp()
    assert driver.is_ramping() is True
    assert driver.get_device_status() & SWP_ACTIVE

    driver.stop_ramp()
    assert driver.is_ramping() is False
    assert not driver.get_device_status() & SWP_ACTIVE


def test_dwell_time_below_the_hardware_minimum_is_rejected():
    driver = Vaunix_LDA_Driver_Mock()
    driver.connect()

    with pytest.raises(ValueError, match="at least 1 ms"):
        driver.set_ramp_dwell_time_ms(0)

    # Idle time, unlike dwell time, legitimately allows zero.
    driver.set_ramp_idle_time_ms(0)
    assert driver.get_ramp_idle_time_ms() == 0


def test_zero_ramp_step_is_rejected():
    driver = Vaunix_LDA_Driver_Mock()
    driver.connect()

    with pytest.raises(ValueError, match="step=0"):
        driver.set_ramp_step_dB(0.0)


# ==================== profile ====================


def test_set_profile_writes_every_point_and_the_count():
    driver = Vaunix_LDA_Driver_Mock()
    driver.connect()

    driver.set_profile_dB([0.0, 10.0, 20.0, 30.0])

    assert driver.get_profile_count() == 4
    assert driver.get_profile_element_dB(0) == pytest.approx(0.0)
    assert driver.get_profile_element_dB(3) == pytest.approx(30.0)


def test_profile_index_bounds_are_enforced_and_zero_based():
    driver = Vaunix_LDA_Driver_Mock(profile_max_length=50)
    driver.connect()

    driver.set_profile_element_dB(0, 1.0)
    driver.set_profile_element_dB(49, 2.0)

    with pytest.raises(ValueError, match=r"index=-1 is outside \[0, 49\]"):
        driver.set_profile_element_dB(-1, 1.0)

    with pytest.raises(ValueError, match=r"index=50 is outside \[0, 49\]"):
        driver.set_profile_element_dB(50, 1.0)


def test_profile_longer_than_the_device_memory_is_rejected():
    driver = Vaunix_LDA_Driver_Mock(profile_max_length=8)
    driver.connect()

    with pytest.raises(ValueError, match="holds at most 8"):
        driver.set_profile_dB([1.0] * 9)


def test_start_and_stop_profile_are_visible_in_device_status():
    driver = Vaunix_LDA_Driver_Mock()
    driver.connect()

    driver.set_profile_dB([0.0, 5.0])
    driver.start_profile(repeat=True)

    assert driver.is_profile_playing() is True
    assert driver.get_device_status() & PROFILE_ACTIVE

    driver.stop_profile()
    assert driver.is_profile_playing() is False


# ==================== feature gating ====================


def test_profile_methods_raise_when_the_device_lacks_the_feature():
    driver = Vaunix_LDA_Driver_Mock(features=HAS_HIRES)
    driver.connect()

    with pytest.raises(Vaunix_LDA_Feature_Error, match="requires HAS_PROFILES"):
        driver.start_profile()

    with pytest.raises(Vaunix_LDA_Feature_Error, match="requires HAS_PROFILES"):
        driver.set_profile_element_dB(0, 1.0)


def test_bidirectional_ramp_methods_raise_when_the_device_lacks_the_feature():
    driver = Vaunix_LDA_Driver_Mock(features=HAS_HIRES | HAS_PROFILES)
    driver.connect()

    with pytest.raises(Vaunix_LDA_Feature_Error, match="requires HAS_BIDIR_RAMPS"):
        driver.set_ramp_bidirectional(True)

    with pytest.raises(Vaunix_LDA_Feature_Error, match="requires HAS_BIDIR_RAMPS"):
        driver.get_ramp_hold_time_ms()

    # The single-phase ramp is still available.
    driver.set_ramp_dwell_time_ms(10)
    assert driver.get_ramp_dwell_time_ms() == 10


# ==================== transport gating ====================


def test_network_getters_are_unavailable_over_usb():
    driver = Vaunix_LDA_Driver_Mock(connection_type="USB")
    driver.connect()

    for method in (driver.get_ip_address, driver.get_netmask, driver.get_gateway,
                   driver.get_ip_mode, driver.get_software_version):
        with pytest.raises(Vaunix_LDA_Transport_Error, match="not available over USB"):
            method()


def test_status_polling_and_multichannel_are_unavailable_over_ethernet():
    driver = Vaunix_LDA_Driver_Mock(connection_type="Ethernet")
    driver.connect()

    with pytest.raises(Vaunix_LDA_Transport_Error, match="not available over Ethernet"):
        driver.is_ramping()

    with pytest.raises(Vaunix_LDA_Transport_Error, match="not available over Ethernet"):
        driver.is_profile_playing()

    with pytest.raises(Vaunix_LDA_Transport_Error, match="not available over Ethernet"):
        driver.get_device_status()

    with pytest.raises(Vaunix_LDA_Transport_Error, match="not available over Ethernet"):
        driver.get_profile_index()

    with pytest.raises(Vaunix_LDA_Transport_Error, match="not available over Ethernet"):
        driver.set_attenuation_multichannel_dB(10.0, [1])


def test_network_getters_work_over_ethernet():
    driver = Vaunix_LDA_Driver_Mock(connection_type="Ethernet")
    driver.connect()

    assert driver.get_connection_type() == "Ethernet"
    assert driver.get_ip_address() == "192.168.100.5"
    assert driver.get_ip_mode() == "static"
    assert driver.get_software_version() == "1.7"


def test_transport_error_is_a_not_implemented_error():
    # Callers branch on this distinction: a missing DLL export is a static fact,
    # unlike a feature bit that depends on the connected unit.
    assert issubclass(Vaunix_LDA_Transport_Error, NotImplementedError)
    assert issubclass(Vaunix_LDA_Feature_Error, Vaunix_LDA_Error)
    assert issubclass(Vaunix_LDA_Error, RuntimeError)


# ==================== multichannel ====================


def test_multichannel_set_applies_to_every_named_channel():
    driver = Vaunix_LDA_Driver_Mock(
        connection_type="USB",
        number_of_channels=8,
        features=HAS_HIRES | HAS_PROFILES | HAS_BIDIR_RAMPS | HAS_MCHANNELS,
    )
    driver.connect()

    driver.set_attenuation_multichannel_dB(15.0, [2, 4, 5])

    assert driver.get_attenuation_dB(channel=2) == pytest.approx(15.0)
    assert driver.get_attenuation_dB(channel=4) == pytest.approx(15.0)
    assert driver.get_attenuation_dB(channel=5) == pytest.approx(15.0)
    assert driver.get_attenuation_dB(channel=1) == pytest.approx(0.0)


def test_multichannel_set_requires_the_feature_bit():
    driver = Vaunix_LDA_Driver_Mock(connection_type="USB", number_of_channels=8, features=HAS_HIRES)
    driver.connect()

    with pytest.raises(Vaunix_LDA_Feature_Error, match="requires HAS_MCHANNELS"):
        driver.set_attenuation_multichannel_dB(15.0, [1, 2])


# ==================== misc ====================


def test_rf_path_toggles():
    driver = Vaunix_LDA_Driver_Mock()
    driver.connect()

    driver.set_rf_on(False)
    assert driver.get_rf_on() is False

    driver.set_rf_on(True)
    assert driver.get_rf_on() is True


def test_save_settings_is_recorded():
    driver = Vaunix_LDA_Driver_Mock()
    driver.connect()

    driver.save_settings()
    driver.save_settings()

    assert driver.saved_settings_count == 2
    assert ("save_settings",) in driver.command_history
