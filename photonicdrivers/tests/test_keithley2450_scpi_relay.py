"""Keithley2450_SCPI_Relay against a fake remote that behaves like the OLD server driver (one recv per query: a long
reply arrives in pieces, each stripped; the rest is fetched with read()). No hardware (2026-11-09)."""
import pytest

from photonicdrivers.Keithley.Keithley2450_SCPI_Relay import Keithley2450_SCPI_Relay

IDN = "KEITHLEY INSTRUMENTS,MODEL 2450,04612049,1.7.12b"


class OldServerDriver:
    """write / query / read as the server's driver before 2026-11-09: query returns at most `piece` characters of
    the instrument's reply (stripped), read() the next piece; nothing is drained. The 2450 answers the queries of
    one message joined by ';'."""

    def __init__(self, replies, piece=4096):
        self.replies = dict(replies, **{"*IDN?": IDN})
        self.piece, self.pending, self.sent, self.connects = piece, "", [], 0

    def connect(self):
        self.connects += 1

    def disconnect(self):
        self.pending = ""

    def write(self, command):
        self.sent.append(command)

    def query(self, command):
        self.sent.append(command)
        answers = [self.replies[c] for c in command.split(";") if self.replies.get(c) is not None]
        self.pending += ";".join(answers) + "\n"
        return self.read()

    def read(self):
        chunk, self.pending = self.pending[:self.piece], self.pending[self.piece:]
        return chunk.strip() if chunk else None


def test_the_identity_is_the_sentinel_never_opc():
    remote = OldServerDriver({":TRIG:STAT?": "RUNNING;RUNNING;5"})
    relay = Keithley2450_SCPI_Relay(remote)
    assert relay.get_trigger_state() == "RUNNING"
    assert remote.sent == ["*IDN?", ":TRIG:STAT?;*IDN?"]
    assert not any("*OPC?" in s for s in remote.sent)   # *OPC? waits for a running sweep (2026-11-09 23:30)


def test_a_long_reply_in_pieces_is_joined_and_nothing_is_left_behind():
    data = ",".join(f"{k * 1e-12:.6E},{40.0:.6E},{k * 0.05:.6E}" for k in range(500))
    remote = OldServerDriver({':TRAC:DATA? 1, 500, "defbuffer1", READ, SOUR, REL': data}, piece=1000)
    relay = Keithley2450_SCPI_Relay(remote)
    out = relay.get_buffer_data(1, 500, ("reading", "source", "relative_time"))
    assert len(out["reading"]) == 500 and out["relative_time"][-1] == pytest.approx(499 * 0.05)
    assert remote.pending == ""


def test_a_cut_at_a_space_of_the_identity_is_still_complete():
    data = "1.0E-9,0.0"
    reply = data + ";" + IDN
    cut = reply.index(" ") + 1                    # the piece ends just after the space; the server strips it
    remote = OldServerDriver({':TRAC:DATA? 1, 1, "defbuffer1", READ, REL': data}, piece=cut)
    remote.replies["*IDN?"] = IDN
    relay = Keithley2450_SCPI_Relay.__new__(Keithley2450_SCPI_Relay)
    relay.remote, relay.max_reads, relay.identity = remote, 50, IDN
    assert relay.get_buffer_data(1, 1) == {"reading": [1e-9], "relative_time": [0.0]}


def test_an_unanswered_query_returns_empty():
    remote = OldServerDriver({":BOGUS?": None})
    assert Keithley2450_SCPI_Relay(remote).query(":BOGUS?") == ""


def test_a_reply_that_never_completes_raises():
    class Truncating(OldServerDriver):
        def read(self):
            chunk = super().read()
            return chunk[:-5] if chunk and IDN in chunk and chunk != IDN else chunk   # the sentinel lost
    remote = Truncating({':TRAC:ACT? "defbuffer1"': "12"})
    relay = Keithley2450_SCPI_Relay(remote, max_reads=2)
    with pytest.raises(RuntimeError):
        relay.get_buffer_count()


def test_reconnect_starts_on_a_clean_socket():
    remote = OldServerDriver({})
    remote.pending = "RUNNING;RUNNING;6;1\n"            # a stale reply from an earlier session
    relay = Keithley2450_SCPI_Relay(remote, reconnect=True)
    assert relay.identity == IDN and remote.connects == 1


def test_a_stale_reply_without_reconnect_is_refused():
    remote = OldServerDriver({})
    remote.pending = "RUNNING;RUNNING;6;1\n"
    with pytest.raises(RuntimeError):
        Keithley2450_SCPI_Relay(remote)


def test_writes_pass_through_unchanged():
    remote = OldServerDriver({})
    relay = Keithley2450_SCPI_Relay(remote)
    relay.set_source_list([0.0, 1.0, 0.0])
    relay.set_voltage(0)
    relay.set_output(1)
    assert remote.sent[1:] == [":SOUR:LIST:VOLT 0.0, 1.0, 0.0", ":SOUR:VOLT:LEV:IMM:AMPL 0", ":OUTP:STAT 1"]
