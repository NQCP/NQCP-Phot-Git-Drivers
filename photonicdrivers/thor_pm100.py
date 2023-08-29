import qcodes as qc
from qcodes import validators as vals
from qcodes.instrument import (
    VisaInstrument,
)
from qcodes.parameters import ManualParameter, MultiParameter
from qcodes.logger import start_all_logging


class PM100(VisaInstrument):
    """
    QCoDeS driver
    """

    start_all_logging()

    # all instrument constructors should accept **kwargs and pass them on to
    # super().__init__
    def __init__(self, name, address, **kwargs):
        # supplying the terminator means you don't need to remove it from every response
        super().__init__(name, address, timeout=10, terminator="\n", **kwargs)
        self.add_parameter("idn", label="ID number", get_cmd="*IDN?")
        self.add_parameter("power", label="Power", get_cmd="measure:power?", unit="W")
        self.add_parameter(
            "wavelength",
            label="Wavelength",
            get_cmd="sense:correction:WAVelength?",
            unit="nm",
        )
        self.add_parameter(
            "beamdiameter",
            label="Beam diameter",
            get_cmd="sense:correction:beamdiameter?",
            unit="mm",
        )
        self.add_parameter(
            "bandwidth",
            label="Bandwidth",
            get_cmd="input:pdiode:filter:lpass:state?",
            unit="nm",
        )
        self.add_parameter(
            "averaging", label="Averaging", get_cmd="sense:average:count?", unit="times"
        )
