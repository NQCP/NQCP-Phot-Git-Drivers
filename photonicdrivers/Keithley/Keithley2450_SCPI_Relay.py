"""Keithley2450_Driver's methods run locally, their SCPI relayed through another driver's write / query - e.g. the
LabServer's proxy on kk4labserver01 while its driver predates the hardware-timed methods (2026-11-09: the server
could not be restarted until the next day).

The relayed driver may be the old one, whose query() does ONE recv(4096) without draining a stale reply: a long
reply could arrive cut, and the rest would be read as the answer to the next query. So every query is sent with
';*OPC?' appended; the 2450 answers '<reply>;1' (SCPI: the replies of one message separated by ';'). The relay reads
on (remote read()) until the reply ends with that ';1' and refuses a reply without it. A query that the 2450 does
not answer (an error) comes back as '1' alone: returned as ''. NOT YET TESTED ON THE INSTRUMENT.
"""
from photonicdrivers.Keithley.Keithley2450_Driver import Keithley2450_Driver

_SENTINEL_QUERY = "*OPC?"


class Keithley2450_SCPI_Relay(Keithley2450_Driver):

    def __init__(self, remote_driver, max_reads: int = 50):
        """remote_driver: any object with write(command), query(command) -> str and read() -> str talking to the
        2450 (the LabServer proxy of Keithley2450_Driver)."""
        self.remote = remote_driver
        self.max_reads = int(max_reads)
        self.ip_address, self.port, self.socket = None, None, None

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
            raise RuntimeError(f"Keithley2450 relay: no reply to {command!r} (socket error on the server)")
        reads = 0
        while not self._complete(reply):
            if reads >= self.max_reads:
                raise RuntimeError(f"Keithley2450 relay: the reply to {command!r} never ended with ';1' after "
                                   f"{reads} further reads ({len(reply)} characters)")
            more = self.remote.read()
            if more is None:
                raise RuntimeError(f"Keithley2450 relay: the reply to {command!r} stopped after {len(reply)} characters")
            reply += more
            reads += 1
        reply = reply.strip()
        return "" if reply == "1" else reply[:-2]

    @staticmethod
    def _complete(reply: str) -> bool:
        reply = reply.strip()
        return reply == "1" or reply.endswith(";1")
