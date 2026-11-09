"""Keithley2450_Driver's methods run locally, their SCPI relayed through another driver's write / query - e.g. the
LabServer's proxy on kk4labserver01 while its driver predates the hardware-timed methods (2026-11-09: the server
could not be restarted until the next day).

The relayed driver may be the old one, whose query() does ONE recv(4096) without draining a stale reply: a long
reply can arrive cut (2026-11-09: 74 of 150 fields), and the rest would be read as the answer to the next query. So
every query is sent with ';*IDN?' appended and read on (remote read()) until the reply ends with ';' + the 2450's
identity (learnt once at the start); a reply without it is refused. A query that the 2450 does not answer (an error)
comes back as the identity alone: returned as ''.

NOT *OPC? (the first version, 2026-11-09 23:30): *OPC? waits until the running list sweep has finished, so the
server's query timed out after 10 s, every later command queued behind it - including :ABOR and the output off - and
protocol 65 test 3 lost its run (the 2450 finished the list on its own and rested at 0 V).
"""
import time

from photonicdrivers.Keithley.Keithley2450_Driver import Keithley2450_Driver

_SENTINEL_QUERY = "*IDN?"


class Keithley2450_SCPI_Relay(Keithley2450_Driver):

    def __init__(self, remote_driver, max_reads: int = 50, reconnect: bool = False):
        """remote_driver: any object with write(command), query(command) -> str and read() -> str talking to the
        2450 (the LabServer proxy of Keithley2450_Driver). reconnect: close and reopen the remote's socket first, so
        no stale reply of an earlier session is waiting in it."""
        self.remote = remote_driver
        self.max_reads = int(max_reads)
        self.ip_address, self.port, self.socket = None, None, None
        if reconnect:
            self.remote.disconnect()
            time.sleep(0.5)
            self.remote.connect()
            time.sleep(0.5)
        identity = self.remote.query(_SENTINEL_QUERY)
        if not identity or not identity.startswith("KEITHLEY") or "2450" not in identity or any(
                c in identity for c in ";\n"):           # a stale reply in front of it: not clean
            raise RuntimeError(f"Keithley2450 relay: *IDN? answered {identity!r} - not a clean 2450 connection")
        self.identity = identity.strip()

    def connect(self):
        return self.remote.connect()

    def disconnect(self):
        return self.remote.disconnect()

    def is_connected(self):
        return self.remote.is_connected()

    def write(self, command):
        self.remote.write(command)

    def query(self, command):
        reply = self.remote.query(f"{command};{_SENTINEL_QUERY}")
        if reply is None:
            raise RuntimeError(f"Keithley2450 relay: no reply to {command!r} (socket error or timeout on the server)")
        reads = 0
        while not self._complete(reply):
            if reads >= self.max_reads:
                raise RuntimeError(f"Keithley2450 relay: the reply to {command!r} never ended with the identity after "
                                   f"{reads} further reads ({len(reply)} characters)")
            more = self.remote.read()
            if more is None:
                raise RuntimeError(f"Keithley2450 relay: the reply to {command!r} stopped after {len(reply)} characters")
            reply += more
            reads += 1
        # Compared without spaces: the server strips every piece, so a space at a cut is lost (the identity has
        # spaces; the numeric replies have none).
        reply, identity = reply.replace(" ", ""), self.identity.replace(" ", "")
        return "" if reply == identity else reply[:-(len(identity) + 1)]

    def _complete(self, reply: str) -> bool:
        reply, identity = reply.replace(" ", "").strip(), self.identity.replace(" ", "")
        return reply == identity or reply.endswith(";" + identity)
