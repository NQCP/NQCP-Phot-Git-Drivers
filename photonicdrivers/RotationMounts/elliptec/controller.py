"""This module contains the Controller class, which is the base class for all devices."""

import sys
import serial
from serial import Serial
from tools import parse


class Controller:
    """Class for controlling the Elliptec devices via serial port. This is a general class,
    subclasses are implemented for each device type."""

    last_position = None
    last_response = None
    last_status = None

    def __init__(
        self,
        port,
        baudrate=9600,
        bytesize=8,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=2,
        write_timeout=0.5,
        debug=True,
    ):
        self.port = port
        self. baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.timeout = timeout
        self.write_timeout = write_timeout
        self.debug = debug 
        self.connection: Serial = None 

    def connect(self):
        try:
            self.connection = serial.Serial(
                port = self.port,
                baudrate=self.baudrate,
                bytesize=self.bytesize,
                parity=self.parity,
                stopbits=self.stopbits,
                timeout=self.timeout,
                write_timeout=self.write_timeout,
            )
        except serial.SerialException:
            print("Could not open port {port}.")
            # TODO: nicer/more logical shutdown (this kills the entire app?)
            sys.exit()

        self.port = self.port

        if self.s.is_open:
            if self.debug:
                print(f"Controller on port {self.port}: Connection established!")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def read_response(self):
        """Reads the response from the controller."""
        response = self.s.read_until(b"\r\n")  # Waiting until response read

        if self.debug:
            print("RX:", response)

        status = parse(response, debug=self.debug)

        # Setting properties of last response/status/position
        self.last_response = response
        self.last_status = status
        # print('STATUS:', status)
        if status is not None:
            if not isinstance(status, dict):
                if status[1] == "PO":
                    self.last_position = status[1]

        return status

    def send_instruction(self, instruction, address="0", message=None):
        """Sends an instruction to the controller. Expects a response which is returned."""
        # Encode inputs
        addr = address.encode("utf-8")
        inst = instruction  # .encode('utf-8') # Already encoded
        # Compose command
        command = addr + inst
        # Append command if necessary
        if message is not None:
            # Convert to hex if the message is a number
            if isinstance(message, int):
                mesg = message.to_bytes(4, "big", signed=True).hex().upper()
            else:
                mesg = message

            command += mesg.encode("utf-8")

        if self.debug:
            print("TX:", command)
        # Execute the command and wait for a response
        self.s.write(command)  # This actually executes the command
        response = self.read_response()

        return response

    def disconnect(self):
        """Closes the serial connection."""
        if self.connection.is_open:
            self.connection.close()
            print("Connection is closed!")
