"""Keithley2450_Driver.query with a fake socket (no hardware): a stale reply is dropped, a reply split over several
recv calls is joined (2026-11-09: a stale *IDN? reply shifted every later answer by one)."""
import socket

from photonicdrivers.Keithley.Keithley2450_Driver import Keithley2450_Driver


class FakeSocket:
    """Holds bytes 'on the wire'; sendall queues the instrument's reply for the query sent."""

    def __init__(self, waiting=b"", replies=None, split=False):
        self.buffer, self.replies, self.split, self.timeout, self.sent = waiting, dict(replies or {}), split, 10, []

    def gettimeout(self):
        return self.timeout

    def settimeout(self, value):
        self.timeout = value

    def sendall(self, data):
        self.sent.append(data)
        self.buffer += self.replies[data.strip().decode()]

    def recv(self, n):
        if not self.buffer:
            if self.timeout == 0.0:
                raise BlockingIOError
            raise socket.timeout
        size = 3 if self.split else n
        chunk, self.buffer = self.buffer[:size], self.buffer[size:]
        return chunk


def driver_with(fake):
    driver = Keithley2450_Driver("10.0.0.1")
    driver.socket = fake
    return driver


def test_a_stale_reply_is_dropped():
    fake = FakeSocket(waiting=b"KEITHLEY INSTRUMENTS,MODEL 2450\n", replies={":OUTP:STAT?": b"0\n"})
    assert driver_with(fake).query(":OUTP:STAT?") == "0"
    assert fake.timeout == 10  # restored


def test_a_split_reply_is_joined():
    fake = FakeSocket(replies={":SOUR:VOLT:RANG?": b"2.000000E+02\n"}, split=True)
    assert driver_with(fake).query(":SOUR:VOLT:RANG?") == "2.000000E+02"


def test_successive_queries_stay_in_step():
    fake = FakeSocket(waiting=b"stale\n", replies={"*IDN?": b"KEITHLEY\n", ":OUTP:STAT?": b"1\n"})
    driver = driver_with(fake)
    assert [driver.query("*IDN?"), driver.query(":OUTP:STAT?")] == ["KEITHLEY", "1"]
