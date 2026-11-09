"""Keithley2450_Driver's hardware-timed methods (source list, list sweep, trigger-model templates, buffer) against a
fake socket: the exact SCPI sent and the parsing of the replies. No hardware (added 2026-11-09)."""
import pytest

from photonicdrivers.tests.test_keithley2450_driver_query import FakeSocket as QueryFakeSocket, driver_with


class FakeSocket(QueryFakeSocket):
    """As the query test's fake, but a command without a reply (a write) queues nothing."""

    def sendall(self, data):
        self.sent.append(data)
        self.buffer += self.replies.get(data.strip().decode(), b"")


def sent(fake):
    return [s.decode().strip() for s in fake.sent]


def test_source_list_is_sent_in_commands_of_100_values():
    fake = FakeSocket()
    values = [(-40.0 if i % 2 else 40.0) for i in range(250)]
    driver_with(fake).set_source_list(values)
    commands = sent(fake)
    assert len(commands) == 3
    assert commands[0].startswith(":SOUR:LIST:VOLT 40.0, -40.0")
    assert commands[1].startswith(":SOUR:LIST:VOLT:APP ") and commands[2].startswith(":SOUR:LIST:VOLT:APP ")
    numbers = [float(x) for c in commands for x in c.split(" ", 1)[1].split(",")]
    assert numbers == values


def test_source_list_refuses_empty_and_too_long():
    driver = driver_with(FakeSocket())
    with pytest.raises(ValueError):
        driver.set_source_list([])
    with pytest.raises(ValueError):
        driver.set_source_list([0.0] * 2501)


def test_list_sweep_and_its_limits():
    fake = FakeSocket()
    driver = driver_with(fake)
    driver.configure_list_sweep(start_index=1, delay_s=0.005, count=100, fail_abort=False)
    assert sent(fake) == [':SOUR:SWE:VOLT:LIST 1, 0.005, 100, OFF, "defbuffer1"']
    for bad in (dict(delay_s=1e-5), dict(count=-1)):
        with pytest.raises(ValueError):
            driver.configure_list_sweep(**bad)


def test_trigger_templates_in_both_syntaxes():
    fake = FakeSocket()
    driver = driver_with(fake)
    driver.load_duration_loop(60, 0.01)
    driver.load_duration_loop(60, 0.01, syntax="legacy")
    driver.load_simple_loop(10, 0.1)
    driver.load_simple_loop(10, 0.1, syntax="legacy")
    assert sent(fake) == [':TRIG:LOAD "DurationLoop", 60.0, 0.01, "defbuffer1"',
                          ':TRIG:LOAD:LOOP:DUR 60.0, 0.01, "defbuffer1"',
                          ':TRIG:LOAD "SimpleLoop", 10, 0.1, "defbuffer1"',
                          ':TRIG:LOAD:LOOP:SIMP 10, 0.1, "defbuffer1"']
    with pytest.raises(ValueError):
        driver.load_duration_loop(10, syntax="tsp")


def test_measurement_settings():
    fake = FakeSocket()
    driver = driver_with(fake)
    driver.set_sense_function("current")
    driver.set_measurement_nplc(0.01)
    driver.set_measurement_autozero(False)
    driver.set_source_readback(True)
    driver.set_source_delay(0)
    assert sent(fake) == [':SENS:FUNC "CURR"', ":SENS:CURR:NPLC 0.01", ":SENS:CURR:AZER OFF",
                          ":SOUR:VOLT:READ:BACK ON", ":SOUR:VOLT:DEL 0.0"]
    with pytest.raises(ValueError):
        driver.set_measurement_nplc(0.001)


def test_trigger_state_and_buffer_count():
    fake = FakeSocket(replies={":TRIG:STAT?": b"RUNNING;RUNNING;3\n", ':TRAC:ACT? "defbuffer1"': b"1234\n"})
    driver = driver_with(fake)
    assert driver.get_trigger_state() == "RUNNING"
    assert driver.get_buffer_count() == 1234


def test_buffer_data_is_read_in_chunks_and_split_by_element():
    replies = {':TRAC:DATA? 1, 2, "defbuffer1", READ, SOUR, REL': b"1.0E-9,40.0,0.0,2.0E-9,-40.0,0.005\n",
               ':TRAC:DATA? 3, 3, "defbuffer1", READ, SOUR, REL': b"3.0E-9,40.0,0.010\n"}
    driver = driver_with(FakeSocket(replies=replies))
    data = driver.get_buffer_data(1, 3, elements=("reading", "source", "relative_time"), chunk=2)
    assert data == {"reading": [1e-9, 2e-9, 3e-9], "source": [40.0, -40.0, 40.0], "relative_time": [0.0, 0.005, 0.010]}


def test_buffer_data_refuses_a_short_reply():
    driver = driver_with(FakeSocket(replies={':TRAC:DATA? 1, 2, "defbuffer1", READ, REL': b"1.0E-9,0.0\n"}))
    with pytest.raises(RuntimeError):
        driver.get_buffer_data(1, 2)
