from photonicdrivers.Abstract.Connectable import Connectable
import pyvisa
import logging
from typing import Optional


class Santec_TSL570_driver(Connectable):
    def __init__(
        self,
        ip_address: str,
        port_number: str,
        resource_manager: pyvisa.ResourceManager = None,
        prints_enabled=False,
    ):
        self.prints_enabled = prints_enabled
        if resource_manager is not None:
            self.resource_manager = resource_manager
        else:
            self.resource_manager = pyvisa.ResourceManager()
        self.ip_address = ip_address
        self.port_number = port_number

    def connect(self):
        """
        Connects to laser
        """
        try:
            self.laser = self.resource_manager.open_resource(
                f"TCPIP0::{self.ip_address}::{self.port_number}::SOCKET",
                write_termination="\n",
                read_termination="\r",
            )
            if self.prints_enabled:
                logging.info("Succesfully connected to laser.")
        except Exception as e:
            if self.prints_enabled:
                logging.error(f"Couldn't connect to the laser due to the error: {e}")
            else:
                raise

    def disconnect(self):
        """
        Closes the connections to laser
        """
        self.laser.close()
        if self.prints_enabled:
            print("Connection to laser closed.")

    def is_connected(self):
        try:
            return bool(self.get_idn() is not None)
        except Exception as e:
            if self.prints_enabled:
                logging.error(f"Couldn't get ID due to the error: {e}")
            return False

    def get_idn(self):
        """
        Retrieves the identification string of the Santec TSL-570 laser.
        """
        return_msg = self.laser.query("*IDN?")
        return_msg_split = return_msg.split(",")
        manufacturer = return_msg_split[0]
        model = return_msg_split[1]
        serial_number = return_msg_split[2]
        firmware_version = return_msg_split[3]
        if self.prints_enabled:
            print("Identification string returned:")
            print(f"- Manufacturer: {manufacturer}")
            print(f"- Model: {model}")
            print(f"- Serial number: {serial_number}")
            print(f"- Firmware version: {firmware_version}")
        else:
            return manufacturer, model, serial_number, firmware_version

    def get_wavelength(self) -> float:
        """
        Gets and returns the current set wavelength

        Args:
            None
        Returns:
            float: wavelength in nm
        """
        msg = ":WAV?"
        return_msg = self.laser.query(msg)
        wavelength_in_nm = float(return_msg) * 1e9
        return wavelength_in_nm
    
    def get_wavelength_unit(self) -> str:
        
        """
        OBS not sure if this code work!!
        Check!

        Get wavelength unit of the laser wavelength [nm]

        Args:
            None
        Returns:
            str: wavelength unit of the laser
        """
        msg = ":WAV:UNIT?"
        return_msg = self.laser.query(msg)
        return return_msg

    def get_power(self) -> float:
        """
        Get power [dBm] of the laser

        Args:
            None
        Returns:
            float: power of the laser
        """
        msg = ":POW?"
        return_msg = self.laser.query(msg)
        power_value = float(return_msg)
        return power_value

    def get_power_unit(self) -> str:
        """
        Get power unit of the laser power [dBm or mW]

        Args:
            None
        Returns:
            str: power unit of the laser

        """
        msg = ":POW:UNIT?"
        return_msg = self.laser.query(msg)
        if return_msg:
            return "dBm"
        else:
            return "mW"

    def set_power_unit(self, unit: str) -> None:
        """
        OBS: This code has not been tested!

        Set power unit of the laser power [dBm or mW]

        Args:
            unit (str): Desired unit, either 'dBm' or 'mW'
        """
        unit = unit.strip().lower()
        if unit == "dbm":
            cmd = ":POW:UNIT DBM"
        elif unit == "mw":
            cmd = ":POW:UNIT MW"
        else:
            raise ValueError("Invalid unit. Must be 'dBm' or 'mW'.")

        self.laser.write(cmd)

    def get_emission_status(self) -> int:
        """
        Get laser emission status

        Args:
            None
        Returns:
            int: 1 if laser is ON, 0 if laser is OFF
        """
        msg = ":POW:STAT?"
        return_msg = self.laser.query(msg)
        emission_status = int(return_msg)
        return emission_status

    def get_operation_status(self) -> int:
        """
        Get laser operation status, that is, if a command is in operation

        Args:
            None
        Returns:
            int: 0 if laser is in operation, 1 if laser is not in operation
        """
        msg = "*OPC?"
        return_msg = self.laser.query(msg)
        operation_status = int(return_msg)
        return operation_status

    def wait_for_operation_complete(
        self, poll_interval_s: float = 0.1, timeout_s: Optional[float] = None
    ) -> bool:
        """
        Wait until the instrument reports operation complete.

        Returns:
            bool: True when complete, False if timeout is reached.
        """
        from time import sleep, time

        start_time = time()
        while self.get_operation_status() == 0:
            if timeout_s is not None and (time() - start_time) > timeout_s:
                return False
            sleep(poll_interval_s)
        return True

    def set_wavelength(self, wavelength_nm: float) -> None:
        """
        Set wavelength [nm] of the laser

        Args:
            wavelength_nm (float): wavelength in nm
        Returns:
            None
        """

        msg = ":WAVelength  " + str(wavelength_nm) # + "e-9"
        self.laser.write(msg)

    def clear_status(self) -> None:
        """Clear instrument status registers."""
        self.laser.write("*CLS")

    def reset(self) -> None:
        """Reset instrument to default state."""
        self.laser.write("*RST")

    def set_legacy_command_set(self, enabled: bool) -> None:
        """Select legacy (True) or modern (False) command set."""
        self.laser.write(f"SYST:COMM:COD {0 if enabled else 1}")

    def set_gpib_delimiter(self, delimiter: int) -> None:
        """Set GPIB command delimiter."""
        self.laser.write(f"SYST:COMM:GPIB:DEL {delimiter}")

    def set_auto_power_attenuation(self, enabled: bool) -> None:
        """Enable or disable automatic power attenuation mode."""
        self.laser.write(f"POW:ATT:AUT {1 if enabled else 0}")

    def set_coherence_control(self, enabled: bool) -> None:
        """Enable or disable coherence control."""
        self.laser.write(f"COHCtrl {1 if enabled else 0}")

    def set_shutter_open(self, is_open: bool) -> None:
        """Open or close the internal shutter."""
        self.laser.write(f"POW:SHUT {0 if is_open else 1}")

    def set_sweep_start_wavelength(self, wavelength_nm: float) -> None:
        """Set wavelength sweep start in nm."""
        self.laser.write(f":WAV:SWE:STAR {wavelength_nm}")

    def set_sweep_stop_wavelength(self, wavelength_nm: float) -> None:
        """Set wavelength sweep stop in nm."""
        self.laser.write(f":WAV:SWE:STOP {wavelength_nm}")

    def set_sweep_speed(self, speed_nm_per_s: float) -> None:
        """Set wavelength sweep speed in nm/s."""
        self.laser.write(f":WAV:SWE:SPE {speed_nm_per_s}")

    def get_sweep_speed(self) -> float:
        """Get configured wavelength sweep speed in nm/s."""
        return float(self.laser.query(":WAV:SWE:SPE?").strip())

    def set_trigger_output_step(self, step_wavelength_nm: float) -> None:
        """Set trigger output step size in nm."""
        self.laser.write(f":TRIG:OUTP:STEP {step_wavelength_nm}")

    def set_sweep_cycles(self, cycles: int) -> None:
        """Set number of sweep cycles."""
        self.laser.write(f":WAV:SWE:CYCL {cycles}")

    def start_sweep(self) -> None:
        """Start wavelength sweep."""
        self.laser.write(":WAV:SWE 1")

    def get_sweep_status(self) -> int:
        """Get sweep status; 0 indicates finished."""
        return int(self.laser.query(":WAV:SWE?").strip())

    def set_wavelength_unit(self, unit: str):
        
        # OBS: This code has not been tested!

        unit = unit.strip().lower()
        if unit == "nm":
            cmd = ":WAV:UNIT NM"
        elif unit == "um":
            cmd = ":WAV:UNIT UM"
        else:
            raise ValueError("Invalid unit. Must be 'nm' or 'um'.")

        self.laser.write(cmd)

    def set_power(self, power_dBm: float):
        """
        Set power [dBm] of the laser
        """
        power_dBm_decimal = "{:.2e}".format(power_dBm)
        msg = ":POW " + str(power_dBm_decimal)
        self.laser.write(msg)

    def set_emission_status(self, emission: bool):
        """
        Set laser emission ON or OFF: emission = True to turn ON laser, emission = False to turn OFF laser

        Args:
            emission (bool): True to turn ON laser, False to turn OFF laser
        Returns:
            None
        """
        if emission:
            emission_int = 1
        else:
            emission_int = 0
        msg = ":POW:STAT " + str(emission_int)
        self.laser.write(msg)

    ####################### BLANKET FUNCTIONS #######################

    def write(self, message: str):
        """
        Write a message to the laser

        Args:
            message (str): message to write
        Returns:
            None
        """
        self.laser.write(message)

    def query(self, message: str):
        """
        Query a message to the laser
        """
        return self.laser.query(message)

    def read(self):
        """
        Read a message from the laser
        """
        return self.laser.read()


if __name__ == "__main__":


    # Check if the driver works
    from time import sleep

    rm = pyvisa.ResourceManager()
    santec = Santec_TSL570_driver(
        resource_manager = rm,
        ip_address="10.209.69.95",
        port_number="5000")
    santec.connect()
    santec.get_idn()

    # check all getter methods
    print("Wavelength [nm]: ", santec.get_wavelength())
    print("Power unit: ", santec.get_power_unit())
    print("Power: ", santec.get_power())
    print("Emission status: ", santec.get_emission_status())

    # check all setter methods
    santec.set_wavelength(1270.41)
    print("Operation status:", santec.get_operation_status())
    sleep_time = 0.01
    sleep(sleep_time)
    print(f"Operation status after {sleep_time}s sleep:", santec.get_operation_status())
    print("Wavelength [nm]: ", santec.get_wavelength())

    santec.set_power(-10)
    sleep_time = 0.1
    sleep(sleep_time)
    print("Power: ", santec.get_power())
    santec.set_emission_status(True)

    santec.disconnect()
    print("\nDone.")
