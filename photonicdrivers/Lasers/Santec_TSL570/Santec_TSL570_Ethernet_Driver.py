from photonicdrivers.Abstract.Connectable import Connectable
import pyvisa
import logging


class Santec_TSL570_driver(Connectable):
    def __init__(
        self,
        resource_manager=None,
        ip_address: str = "",
        port_number: str = "",
        prints_enabled=True,
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
            return self.get_idn() is not None
        except:
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
            emission = 1
        else:
            emission = 0
        msg = ":POW:STAT " + str(emission)
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
    from time import sleep

    rm = pyvisa.ResourceManager()
    santec = Santec_TSL570_driver(resource_manager=rm, ip_address="10.209.69.95")
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
    santec.set_emission_status(0)

    santec.disconnect()
    print("\nDone.")
