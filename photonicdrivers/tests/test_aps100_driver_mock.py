"""APS100_PS_Driver against a mock of the supply's serial port (no hardware): the channel-safe methods added after
the 2026-11-11 17:22 event (an X sign flip ended with the sweep and ULIM 2.150 kG on channel 1 = Z)."""
import threading

import pytest

import photonicdrivers.Magnets.APS100_PS_Driver as aps_module
from photonicdrivers.Magnets.APS100_PS_Driver import APS100_PS_Driver
from photonicdrivers.Mocks.APS100_Serial_Mock import APS100_Serial_Mock


@pytest.fixture(autouse=True)
def fast_time(monkeypatch):
    """No real waiting: sleeps are skipped and the clock advances 0.5 s per sleep."""
    clock = {"t": 0.0}
    monkeypatch.setattr(aps_module.time, "sleep", lambda s: clock.__setitem__("t", clock["t"] + max(s, 1e-3)))
    monkeypatch.setattr(aps_module.time, "time", lambda: clock["t"])
    return clock


def make_driver():
    driver = APS100_PS_Driver(com_port="COM_MOCK")
    driver.connection = APS100_Serial_Mock()
    return driver


def test_select_channel_checks_and_retries():
    driver = make_driver()
    driver.connection.ignore_chan = 1                 # the first CHAN is ignored
    driver.select_channel(2)
    assert driver.connection.selected == 2


def test_select_channel_raises_when_never_selected():
    driver = make_driver()
    driver.connection.ignore_chan = 10
    with pytest.raises(RuntimeError, match="channel 2 not selected"):
        driver.select_channel(2)


def test_ramp_channel_to_sign_flip_stays_on_its_channel():
    driver = make_driver()
    ps = driver.connection
    assert driver.ramp_channel_to(2, -2.15, relative_tolerance=0.05, absolute_tolerance=0.01) == pytest.approx(-2.15)
    assert driver.ramp_channel_to(2, 0.0) == pytest.approx(0.0)
    assert ps.channels[2]["mode"] == "Standby"
    assert driver.ramp_channel_to(2, 2.15, relative_tolerance=0.05, absolute_tolerance=0.01) == pytest.approx(2.15)
    assert ps.channels[1]["out"] == 0.0 and ps.channels[1]["ulim"] == 0.0


def test_start_sweep_refuses_when_channel_switched_before_sweep():
    """Another client's CHAN 1 right after our ULIM (the 17:22 hypothesis): no SWEEP is sent at all."""
    driver = make_driver()
    ps = driver.connection
    ps.hijack_after = {"ULIM": 1}
    with pytest.raises(RuntimeError):
        driver.start_sweep(2, 2.15)
    assert not any(cmd.startswith("SWEEP ") and cmd != "SWEEP?" for _, cmd in ps.log)
    assert ps.channels[1]["mode"] == "Standby" and ps.channels[1]["out"] == 0.0


def test_old_path_reproduces_the_event():
    """The old sequence (set_channel, set_upper_limit, ramp_up) with the same hijack sweeps channel 1 = Z:
    what happened on 2026-11-11. Kept as a record of the failure mode."""
    driver = make_driver()
    ps = driver.connection
    driver.set_channel(2)
    ps.hijack_after = {"UNITS?": 1}                   # set_upper_limit asks UNITS? before ULIM
    driver.set_upper_limit(2.15, "kG")
    driver.ramp_up(wait_while_ramping=False)
    assert ps.channels[1]["ulim"] == pytest.approx(2.15) and ps.channels[1]["mode"] == "Sweeping up"


def test_wait_for_sweep_stops_when_the_other_channel_moves():
    driver = make_driver()
    ps = driver.connection
    driver.start_sweep(2, 1.0)
    ps.channels[1].update(mode="Sweeping up", target=2.15, ulim=2.15)     # the wrong channel starts moving
    with pytest.raises(RuntimeError, match="channel 1 moved"):
        driver.wait_for_sweep(2, 1.0, relative_tolerance=0.05, absolute_tolerance=0.01, watch_channel=1)
    assert ps.channels[1]["mode"] == "Pause"


def test_wait_for_sweep_raises_if_sweep_stops_short():
    driver = make_driver()
    ps = driver.connection
    driver.start_sweep(2, 1.0)
    ps.channels[2].update(mode="Pause", target=None)
    with pytest.raises(RuntimeError, match="stopped"):
        driver.wait_for_sweep(2, 1.0, relative_tolerance=0.05, absolute_tolerance=0.01)


def test_wait_for_sweep_times_out():
    driver = make_driver()
    driver.start_sweep(2, 1.0)
    driver.connection.step_kG = 0.0                   # never moves
    with pytest.raises(RuntimeError, match="did not reach"):
        driver.wait_for_sweep(2, 1.0, relative_tolerance=0.05, absolute_tolerance=0.01, timeout_s=10)


def test_concurrent_reader_cannot_split_a_ramp():
    """A second client reads Z the old way (set_channel(1) then get_field) in a loop while X flips sign."""
    driver = make_driver()
    ps = driver.connection
    stop = threading.Event()

    def other_client():
        while not stop.is_set():
            driver.set_channel(1)
            driver.get_field()

    reader = threading.Thread(target=other_client)
    reader.start()
    try:
        for target in (-2.15, 0.0, 2.15, 0.0):
            driver.ramp_channel_to(2, target, relative_tolerance=0.05, absolute_tolerance=0.01, watch_channel=1)
    finally:
        stop.set()
        reader.join()
    assert ps.channels[1]["out"] == 0.0 and ps.channels[1]["ulim"] == 0.0 and ps.channels[1]["mode"] == "Standby"
    sweeps = [(ch, cmd) for ch, cmd in ps.log if cmd.startswith(("SWEEP UP", "SWEEP DOWN", "SWEEP ZERO", "ULIM ",
                                                                  "LLIM "))]
    assert sweeps and all(ch == 2 for ch, _ in sweeps), sweeps


def test_old_ramp_up_polls_its_own_channel():
    """The old ramp_up now polls the channel it swept, even if another client switches channels meanwhile."""
    driver = make_driver()
    ps = driver.connection
    driver.set_channel(2)
    driver.set_upper_limit(1.0, "kG")
    ps.hijack_after = {"SWEEP UP": 1}                 # someone selects channel 1 right after our SWEEP UP
    driver.ramp_up(target_relative_tolerance=0.05, target_absolute_tolerance=0.01)
    assert ps.channels[2]["out"] == pytest.approx(1.0)
