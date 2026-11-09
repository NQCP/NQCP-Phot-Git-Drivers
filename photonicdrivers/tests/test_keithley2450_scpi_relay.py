"""Keithley2450_SCPI_Relay against a fake remote that behaves like the OLD server driver (one recv per query: a long
reply arrives in pieces, the rest is fetched with read()). No hardware (2026-11-09)."""
import pytest

from photonicdrivers.Keithley.Keithley2450_SCPI_Relay import Keithley2450_SCPI_Relay


class OldServerDriver:
    """write / query / read as the server's driver before 2026-11-09: query returns at most `piece` characters of
    the instrument's reply, read() the next piece; nothing is drained."""

    def __init__(self, replies, piece=4096):
        self.replies, self.piece, self.pending, self.sent = replies, piece, "", []

    def write(self, command):
        self.sent.append(command)

    def query(self, command):
        self.sent.append(command)
        self.pending += self.replies[command] + "\n"
        return self.read()

    def read(self):
        chunk, self.pending = self.pending[:self.piece], self.pending[self.piece:]
        return chunk.strip() if chunk else None


def test_a_short_query_carries_the_sentinel_and_drops_it():
    remote = OldServerDriver({":TRIG:STAT?;*OPC?": "IDLE;IDLE;5;1"})
    relay = Keithley2450_SCPI_Relay(remote)
    assert relay.get_trigger_state() == "IDLE"
    assert remote.sent == [":TRIG:STAT?;*OPC?"]


def test_a_long_reply_in_pieces_is_joined_and_nothing_is_left_behind():
    data = ",".join(f"{k * 1e-12:.6E},{40.0:.6E},{k * 0.05:.6E}" for k in range(500))
    remote = OldServerDriver({':TRAC:DATA? 1, 500, "defbuffer1", READ, SOUR, REL;*OPC?': data + ";1"}, piece=4096)
    relay = Keithley2450_SCPI_Relay(remote)
    out = relay.get_buffer_data(1, 500, ("reading", "source", "relative_time"))
    assert len(out["reading"]) == 500 and out["relative_time"][-1] == pytest.approx(499 * 0.05)
    assert remote.pending == ""


def test_an_unanswered_query_returns_empty():
    remote = OldServerDriver({":BOGUS?;*OPC?": "1"})
    assert Keithley2450_SCPI_Relay(remote).query(":BOGUS?") == ""


def test_a_reply_that_never_completes_raises():
    remote = OldServerDriver({":TRAC:ACT? \"defbuffer1\";*OPC?": "12"})   # the sentinel never comes
    with pytest.raises(RuntimeError):
        Keithley2450_SCPI_Relay(remote).get_buffer_count()


def test_writes_pass_through_unchanged():
    remote = OldServerDriver({})
    relay = Keithley2450_SCPI_Relay(remote)
    relay.set_source_list([0.0, 1.0, 0.0])
    relay.set_voltage(0)
    relay.set_output(1)
    assert remote.sent == [":SOUR:LIST:VOLT 0.0, 1.0, 0.0", ":SOUR:VOLT:LEV:IMM:AMPL 0", ":OUTP:STAT 1"]
