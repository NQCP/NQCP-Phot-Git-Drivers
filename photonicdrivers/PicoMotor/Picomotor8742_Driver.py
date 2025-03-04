# code for communicating with the PicoMotor from NewFocus model 8742 via USB

import socket

import usb.core
from matplotlib import pyplot as plt

from photonicdrivers.Abstract.Connectable import Connectable

# 'usb' is part of the pyusb package (which has dependencies in the libusb package).
# Neither package is included in the .toml file, because installing the packages with pip does not work.
# Instead the packages should be INSTALLED WITH CONDA using:
# conda install conda-forge::pyusb
# installing pyusb like this will also install its dependencies (libusb) and add the .dll files from libusb to the PATH environment
# Documentation:
# https://docs.circuitpython.org/en/latest/shared-bindings/usb/core/index.html#usb.core.Device
# https://itecnote.com/tecnote/python-pyusb-reading-from-a-usb-device/


class NewFocus_8742_Driver(Connectable):
    def __init__(self, vendor_ID_Hex=None, product_ID_Hex=None, IP_adress=None, port=None):
        print("Initialising instance of PicoMotor class")

        self.termChar = '\r'  # the termination character THIS IS NEVER USED, BECAUSE IT SHOULD BE SAVED IN A WAY THAT PRESERVES THE TERMINATION CHARACTER TYPE

        self.connectionType = None
        self.dev = None
        self.vendor_ID_Hex = vendor_ID_Hex
        self.product_ID_Hex = product_ID_Hex
        self.IP_adress = IP_adress
        self.port = port

        print(vendor_ID_Hex)
        print(product_ID_Hex)

    def get_product_ID(self):
        self._write_command('*IDN?')
        response = self._read_command()
        return response

    def get_IP_address(self):
        self._write_command('IPADDR?')
        response = self._read_command()
        return response

    def get_host_name(self):
        self._write_command('HOSTNAME?')
        response = self._read_command()
        return response

    def get_MAC_address(self):
        self._write_command('MACADDR?')
        response = self._read_command()  # returns decimal string. For example: 5827809, 292293
        # The first number is the NewFocus specific identifier. The second is device specific
        if self.connectionType == 'USB':
            response = self._convert_to_MAC_address(response)

        return response

    def move_target_position(self, axis_number_str):
        """
        Moves a given axis of the Picomotor to a specified target position.

        @param axis_number_str: {0,1,2,3}
        """
        self._write_command(str(axis_number_str) + 'PA')

    def move_relative_position(self, axis_number_str, distance_str):
        """
        Moves a given axis of the Picomotor a relative position given by the distance parameter.

        @param axis_number_str: Parameter to identify the axis to be moved: {1,2,3,4}
        @param distance_str: The distance to moved: int32
        @return: None
        """
        self._write_command(str(axis_number_str) + 'PR' + str(distance_str))

    def get_target_position(self, axis_number_str):
        """
        Returns the position of the target axis
        @param axis_number_str: Parameter to identify the axis to be moved: {1,2,3,4}
        @return: The distance of the target axis
        """

        self._write_command(str(axis_number_str) + 'PR?')
        response = self._read_command()
        return response

    def write_custom_command(self, commandStr):
        self._write_command(commandStr)
        response = self._read_command()
        return response

    def disconnect(self):
        if self.connectionType == 'USB':
            usb.util.dispose_resources(self.dev)
            print("connection closed")

        elif self.connectionType == 'Ethernet':
            self.sock.close()

        else:
            print('ERROR in PicoMotorClass - connection has not been initialised properly')

    def connect(self) -> None:
        if self.vendor_ID_Hex is not None and self.product_ID_Hex is not None:
            # open a usb connection
            print('Connecting via USB')
            self.connectionType = 'USB'

            self.endpointIn = 0x2
            self.endpointOut = 0x81
            self.timeOut = 1000  # ms

            self.dev = usb.core.find(idVendor=self.vendor_ID_Hex, idProduct=self.product_ID_Hex)
            print(self.dev)


        elif self.IP_adress is not None and self.port is not None:
            # open an ethernet connection
            print('Connecting via ethernet')
            self.connectionType = 'Ethernet'

            # Create a TCP/IP socket
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(5)  # sets the timeout of the receive command.
            self.server_address = (self.IP_adress, self.port)  # IP address, port
            self.sock.connect(self.server_address)

            # For some reason, there is some output ready immediately after connection has been created.
            # The format might be a telnet command?
            print('Immediate output from device:')
            print(self.sock.recv(1024))
        else:
            print("Insufficient arguments for initialising the PicoMotor class")

    def is_connected(self) -> bool:
        try:
            return self.get_product_ID() is not  None
        except:
            return False

    def load_settings(self) -> dict:
        pass

    ##################### PRIVATE METHODS ###########################

    def _write_command(self, command):
        if self.connectionType == 'USB':
            commandString = command + self.termChar
            self.dev.write(self.endpointIn, commandString, self.timeOut)

        elif self.connectionType == 'Ethernet':
            commandString = command + self.termChar
            self.sock.sendall(commandString.encode())

        else:
            print('ERROR in PicoMotorClass - connection has not been initialised properly')

    def _read_command(self, bitsToRead=4096):
        if self.connectionType == 'USB':
            response_ASCII = self.dev.read(self.endpointOut, bitsToRead, self.timeOut)

            # Convert response from ASCII to string 
            # using method 2 from https://www.geeksforgeeks.org/python-ways-to-convert-list-of-ascii-value-to-string/
            response = ''.join(map(chr, response_ASCII))
            return response

        elif self.connectionType == 'Ethernet':
            response = self.sock.recv(bitsToRead)

            # remove the newline characters if present
            if b"\r\n" in response:
                response, dummy = response.split(b'\r\n')

            # convert from byte string to string
            response = response.decode('utf-8')
            return response

        else:
            print('ERROR in PicoMotorClass - connection has not been initialised properly')

    def _convert_to_MAC_address(self, MAC_string):
        # Converting the decimal numbers to HEX
        MAC1, MAC2 = MAC_string.split(', ')
        MAC1_dec = int(MAC1)  # cast to int decimal
        MAC1_hex = format(MAC1_dec, '06X')  # format to 6 digit hex
        MAC2_dec = int(MAC2)
        MAC2_hex = format(MAC2_dec, '06X')
        MAC_joinedStr = MAC1_hex + MAC2_hex  # joining the two numbers into a 12 digit hex, which is the MAC address
        # print(MAC_joinedStr)

        return MAC_joinedStr

# This is clearly an instrument
class PicoMotor_Driver:

    def __init__(self, driver: NewFocus_8742_Driver, axis_number: int):
        self.driver = driver
        self.axis_number = axis_number

    def move_target_position(self):
        """
        Moves a given axis of the Picomotor to a specified target position.

        @param axis_number_str: {1,2,3,4}
        """

        try:
            self.driver.move_target_position(self.axis_number)
        except Exception as exception:
            print(exception)

    def move_relative_position(self, distance: int):
        """
        Moves a given axis of the Picomotor a relative position given by the distance parameter.

        @param axis_number: Parameter to identify the axis to be moved: {1,2,3,4}
        @param distance: The distance to moved: int32
        @return: None
        """
        try:
            self.driver.move_relative_position(self.axis_number, distance)
        except Exception as exception:
            print(exception)


if __name__ == "__main__":
    # Create JoystickHandler instance

    pico_motor_controller = NewFocus_8742_Driver()
    pico_motor_controller.connect()
    pico_motor_x = PicoMotor_Driver(pico_motor_controller, 1)
    pico_motor_y = PicoMotor_Driver(pico_motor_controller, 2)

    while True:
        plt.pause(0.01)
        pico_motor_x.move_relative_position(1)
        plt.pause(0.01)
        pico_motor_y.move_relative_position(1)


