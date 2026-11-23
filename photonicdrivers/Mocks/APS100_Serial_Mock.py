"""A stand-in for the serial port of an Attocube APS100 dual-channel magnet supply, for testing APS100_PS_Driver.

Answers like the supply as the driver sees it over USB: every command line is echoed back first, then a query's
reply (CHAN?, UNITS?, IOUT?, ULIM?, LLIM?, SWEEP?). Each channel has its own output, limits and sweep; a sweeping
channel moves `step_kG` toward its target at every IOUT?/SWEEP? read (so a test needs no real time).

Fault hooks:
- ignore_chan: the next n "CHAN" commands are ignored (seen 2026-11-11 right after a sweep to zero);
- hijack_after: {command prefix: channel} - right after that command, the selected channel switches to the given
  one, as if another client of the same supply had sent "CHAN n" in between (the 2026-11-11 17:22 hypothesis).
Use: driver = APS100_PS_Driver(com_port="COM_MOCK"); driver.connection = APS100_Serial_Mock().
"""
import threading


class APS100_Serial_Mock:
    def __init__(self, step_kG: float = 0.5):
        self.step_kG = step_kG
        self.selected = 1
        self.channels = {ch: {"out": 0.0, "ulim": 0.0, "llim": 0.0, "mode": "Standby", "target": None,
                              "units": "kG"} for ch in (1, 2)}
        self.ignore_chan = 0
        self.hijack_after = {}
        self.log = []                 # (selected channel, command) for every command received
        self._lines = []
        self._mutex = threading.Lock()

    # ------------------------------------------------------------------ serial.Serial interface
    def write(self, data: bytes):
        command = data.decode("utf-8").strip()
        with self._mutex:
            self.log.append((self.selected, command))
            self._lines.append(command)                       # the echo
            reply = self._handle(command)
            if reply is not None:
                self._lines.append(reply)
            for prefix, channel in list(self.hijack_after.items()):
                if command.startswith(prefix):
                    self.selected = channel
                    del self.hijack_after[prefix]

    def readline(self) -> bytes:
        with self._mutex:
            return (self._lines.pop(0) + "\r\n").encode("utf-8") if self._lines else b""

    def reset_input_buffer(self):
        with self._mutex:
            self._lines.clear()

    def close(self):
        pass

    # ------------------------------------------------------------------ the supply
    def _advance(self):
        for c in self.channels.values():
            if c["target"] is None:
                continue
            d = c["target"] - c["out"]
            if abs(d) <= self.step_kG:
                c["out"] = c["target"]
                if c["mode"] == "Sweeping to zero":
                    c["mode"], c["target"] = "Standby", None
            else:
                c["out"] += self.step_kG if d > 0 else -self.step_kG

    def _handle(self, command: str):
        c = self.channels[self.selected]
        if command == "*IDN?;*ESE 12;*ESE?":
            return "Attocube,APS100,mock"
        if command.startswith("CHAN?"):
            return str(self.selected)
        if command.startswith("CHAN "):
            if self.ignore_chan:
                self.ignore_chan -= 1
            else:
                self.selected = int(command.split()[1])
            return None
        if command == "UNITS?":
            return c["units"]
        if command.startswith("UNITS "):
            c["units"] = "kG" if command.split()[1] in ("kG", "G", "T") else command.split()[1]
            return None
        if command == "IOUT?":
            self._advance()
            return f"{c['out']:.3f}kG"
        if command == "ULIM?":
            return f"{c['ulim']:.3f}kG"
        if command == "LLIM?":
            return f"{c['llim']:.3f}kG"
        if command.startswith("ULIM "):
            c["ulim"] = float(command.split()[1])
            return None
        if command.startswith("LLIM "):
            c["llim"] = float(command.split()[1])
            return None
        if command == "SWEEP?":
            self._advance()
            return c["mode"]
        if command == "SWEEP UP":
            c["mode"], c["target"] = "Sweeping up", c["ulim"]
        elif command == "SWEEP DOWN":
            c["mode"], c["target"] = "Sweeping down", c["llim"]
        elif command == "SWEEP ZERO":
            c["mode"], c["target"] = "Sweeping to zero", 0.0
        elif command == "SWEEP PAUSE":
            c["mode"], c["target"] = "Pause", None
        return None
