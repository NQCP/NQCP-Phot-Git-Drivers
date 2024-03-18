import pyvisa as visa
from typing import Sequence, List


def comma_sequence_to_list(sequence: str):
    if not sequence:
        return []
    return [x.strip() for x in sequence.split(',')]


def is_ok(message: str) -> bool:
    return message == '0, "No error"' or message == '0,"No error"'


class QDAC2:
    """
    Simple wrapper for communicating with a QDAC-II.

    Use like this on USB:

    import qdac2
    import common.connection as conn
    device = conn.find_qdac2_on_usb()
    qdac = qdac2.QDAC2(device)
    print(qdac.status())
    """

    def __init__(self, visa_resource: visa.Resource):
        self._dac = visa_resource
        self._dac.write_termination = '\n'
        self._dac.read_termination = '\n'
        self._dac.baud_rate = 921600
        self._dac.timeout = 1000  # ms
        self._record_commands = False

    def status(self) -> str:
        """
        Return the error status of the instrument.
        """
        return self.query('syst:err:all?')

    def sequence(self, cmds: Sequence[str]):
        """
        Send a sequence of SCPI commands to the QDAC
        """
        for cmd in cmds:
            self._write(cmd)
            errors = self.query('syst:err:all?')
            if is_ok(errors):
                return
            raise ValueError(f'Error: {errors} while executing {cmds}')

    def command(self, cmd: str):
        """
        Send a SCPI command to the QDAC
        """
        self._write(cmd)
        errors = self.query('syst:err:all?')
        if is_ok(errors):
            return
        raise ValueError(f'Error: {errors} after executing {cmd}')

    def query(self, cmd: str) -> str:
        """
        Send a SCPI query to the QDAC
        """
        if self._record_commands:
            self._scpi_sent.append(cmd)
        try:
            answer = self._dac.query(cmd)
        except visa.errors.VisaIOError as error:
            msg = f'QDAC failed query (1st try): {repr(error)}'
            print(msg)
            answer = self._dac.query(cmd)
        return answer

    def clear(self) -> None:
        """
        Function to reset the VISA message queue of the instrument.
        """
        self._dac.clear()

    # ----------------------------------------------------------------------
    # Debugging and testing

    def start_recording_scpi(self) -> None:
        """
        Record all SCPI commands sent to the instrument

        Any previous recordings are removed.  To inspect the SCPI commands sent
        to the instrument, call get_recorded_scpi_commands().
        """
        self._scpi_sent: List[str] = []
        self._record_commands = True

    def get_recorded_scpi_commands(self) -> Sequence[str]:
        """
        Returns the SCPI commands sent to the instrument
        """
        commands = self._scpi_sent
        self._scpi_sent = []
        return commands

    # ----------------------------------------------------------------------

    def _write(self, cmd: str) -> None:
        if self._record_commands:
            self._scpi_sent.append(cmd)
        self._dac.write(cmd)
