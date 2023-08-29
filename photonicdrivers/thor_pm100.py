from qcodes import validators as vals
from qcodes.instrument import VisaInstrument
from qcodes.logger import start_all_logging
from typing import Any

class PM100(VisaInstrument):
    """
    QCoDeS driver
    """

    start_all_logging()

    # all instrument constructors should accept **kwargs and pass them on to
    # super().__init__
    def __init__(self, name: str, address: str, **kwargs: Any) -> None:
        # supplying the terminator means you don't need to remove it from every response
        super().__init__(name, address, timeout=10, terminator="\n", **kwargs)
        self.add_parameter(
            "power", label="Power", get_cmd="measure:power?", unit="W", get_parser=float
        )
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
            get_parser=float,
        )
        self.add_parameter(
            "bandwidth",
            label="Bandwidth",
            get_cmd="input:pdiode:filter:lpass:state?",
            unit="nm",
            get_parser=float,
        )
        self.add_parameter(
            "averaging",
            label="Averaging",
            get_cmd="sense:average:count?",
            unit="times",
            get_parser=int,
        )

        self.add_parameter(
            "power_range",
            label="Power range",
            get_cmd="sense:power:range?",
            set_cmd="sense:power:range {}",
            unit="W",
            get_parser=float,
        )

        self.add_parameter(
            "power_range_auto",
            label="Power range auto",
            get_cmd="sense:power:range:auto?",
            set_cmd="sense:power:range:auto {}",
        )
