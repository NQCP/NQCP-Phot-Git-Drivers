# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
Python script to control Santec Instruments via FTDI USB.

Organization: santec holdings corp.
Version: 0.2.1
Last updated: Mon Feb 03 18:08:00 2025
"""

import sys
import time
import ctypes
import struct
import string
from ctypes import Array
from typing import List, Any

# Setup logging
import logging

# Configure the logging
logging.basicConfig(
    filename='output_python_ftdi.log',  # Name of the log file
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    level=logging.DEBUG  # Set the logging level
)


class FtNode(ctypes.Structure):
    _fields_ = [
        ("Flags", ctypes.c_uint32),
        ("Type", ctypes.c_uint32),
        ("ID", ctypes.c_uint32),
        ("LocId", ctypes.c_uint32),
        ("SerialNumber", ctypes.c_char * 16),
        ("Description", ctypes.c_char * 64),
        ("FTHandle", ctypes.c_void_p),
    ]


class FtProgramData(ctypes.Structure):
    _fields_ = [
        ("Signature1", ctypes.c_uint32),
        ("Signature2", ctypes.c_uint32),
        ("Version", ctypes.c_uint32),
        ("VendorId", ctypes.c_uint16),
        ("ProductId", ctypes.c_uint16),
        ("Manufacturer", ctypes.POINTER(ctypes.c_char)),
        ("ManufacturerId", ctypes.POINTER(ctypes.c_char)),
        ("Description", ctypes.POINTER(ctypes.c_char)),
        ("SerialNumber", ctypes.POINTER(ctypes.c_char)),
        ("MaxPower", ctypes.c_uint16),
        ("PnP", ctypes.c_uint16),
        ("SelfPowered", ctypes.c_uint16),
        ("RemoteWakeup", ctypes.c_uint16),
    ]


class Ftd2xxhelper(object):
    terminator = "\r"

    __slots__ = [
        "_selected_device_node",
        "_last_connected_serial_number",
        "_ft_handle",
        "_num_devices",
        "_ftdi_device_list",
        "_d2xx"
    ]

    def __init__(self, serial_number: str | bytes | None = None):
        logging.info(f"Ftd2xxhelper class initialized. Serial number: {serial_number}")
        self._selected_device_node = None
        self._last_connected_serial_number = None
        self._ft_handle = None
        self._num_devices = None
        self._ftdi_device_list = None
        self._d2xx = None
        logging.info("Ftd2xxhelper class properties set to None.")

        self._d2xx = self.load_library()
        # logging.info(f"Loaded library: {self._d2xx}.")
        if serial_number is not None:
            self.initialize(serial_number)

    @staticmethod
    def load_library():
        """Loads the FTDI D2XX library based on OS."""
        logging.info("Loading FTDI library")
        try:
            if sys.platform.startswith("linux"):
                lib_name = "libftd2xx.so"
            elif sys.platform.startswith("darwin"):
                lib_name = "libftd2xx.dylib"
            else:
                lib_name = "ftd2xx"

            logging.info(f"Attempting to load: {lib_name}")
            return ctypes.cdll.LoadLibrary(lib_name) \
                if sys.platform.startswith("linux") or sys.platform.startswith("darwin") \
                else ctypes.windll.LoadLibrary(lib_name)
        except OSError as e:
            logging.error(f"Failed to load FTDI library: {e}")
            raise RuntimeError(f"Failed to load FTDI library: {e}")

    @staticmethod
    def list_devices():
        """Lists connected FTDI devices and filters by manufacturer 'SANTEC'."""
        logging.info("Listing FTDI devices...")
        try:
            d2xx = Ftd2xxhelper.load_library()
        except RuntimeError as e:
            logging.error(f"Library load failed: {e}")
            return []

        numDevs = ctypes.c_long()
        if d2xx.FT_CreateDeviceInfoList(ctypes.byref(numDevs)) != 0:
            logging.error("Failed to create FTDI device list")
            return []

        logging.info(f"Number of FTDI devices detected: {numDevs.value}")
        if numDevs.value <= 0:
            return []

        t_devices = FtNode * numDevs.value
        devices = t_devices()
        if d2xx.FT_GetDeviceInfoList(devices, ctypes.byref(numDevs)) != 0:
            logging.error("Failed to retrieve FTDI device list")
            return []

        ftdiDeviceList = []
        for device in devices:
            ftHandle = ctypes.c_void_p()
            if d2xx.FT_OpenEx(device.SerialNumber, 1, ctypes.byref(ftHandle)) != 0:
                logging.error(f"Failed to open FTDI device: {device.SerialNumber}")
                continue

            eeprom = FtProgramData()
            eeprom.Signature1 = 0x00000000
            eeprom.Signature2 = 0xFFFFFFFF
            eeprom.Version = 2
            eeprom.Manufacturer = ctypes.create_string_buffer(32)
            eeprom.ManufacturerId = ctypes.create_string_buffer(16)
            eeprom.Description = ctypes.create_string_buffer(64)
            eeprom.SerialNumber = ctypes.create_string_buffer(16)

            try:
                if d2xx.FT_EE_Read(ftHandle, ctypes.byref(eeprom)) == 0:
                    manufacturer = ctypes.cast(eeprom.Manufacturer, ctypes.c_char_p).value
                    if manufacturer:
                        manufacturer_name = manufacturer.decode("ascii", errors="ignore").upper()
                        logging.info(f"Manufacturer: {manufacturer_name}")
                        if manufacturer_name == "SANTEC":
                            ftdiDeviceList.append(device)
            finally:
                d2xx.FT_Close(ftHandle)

        logging.info(f"Filtered FTDI device list: {ftdiDeviceList}")
        return ftdiDeviceList

    @staticmethod
    def __check(f):
        logging.info(f"Performing check: {f}")
        if f != 0:
            names = [
                "FT_OK",
                "FT_INVALID_HANDLE",
                "FT_DEVICE_NOT_FOUND",
                "FT_DEVICE_NOT_OPENED",
                "FT_IO_ERROR",
                "FT_INSUFFICIENT_RESOURCES",
                "FT_INVALID_PARAMETER",
                "FT_INVALID_BAUD_RATE",
                "FT_DEVICE_NOT_OPENED_FOR_ERASE",
                "FT_DEVICE_NOT_OPENED_FOR_WRITE",
                "FT_FAILED_TO_WRITE_DEVICE",
                "FT_EEPROM_READ_FAILED",
                "FT_EEPROM_WRITE_FAILED",
                "FT_EEPROM_ERASE_FAILED",
                "FT_EEPROM_NOT_PRESENT",
                "FT_EEPROM_NOT_PROGRAMMED",
                "FT_INVALID_ARGS",
                "FT_NOT_SUPPORTED",
                "FT_OTHER_ERROR",
            ]
            logging.error("Error: (status %d: %s)" % (f, names[f]))
            raise IOError("Error: (status %d: %s)" % (f, names[f]))

    def get_dev_info_list(self) -> Array[FtNode] | list[Any]:
        logging.info("Getting device info list.")
        numDevs = ctypes.c_long()
        Ftd2xxhelper.__check(self._d2xx.FT_CreateDeviceInfoList(ctypes.byref(numDevs)))
        self._num_devices = numDevs.value
        logging.info(f"numDevs value: {self._num_devices}")
        if numDevs.value > 0:
            t_devices = FtNode * numDevs.value
            devices = t_devices()
            Ftd2xxhelper.__check(
                self._d2xx.FT_GetDeviceInfoList(devices, ctypes.byref(numDevs))
            )
            self._ftdi_device_list = devices
            logging.info(f"Device info list: {devices}")
            return devices
        else:
            logging.info(f"Returning empty device info list.")
            return []

    def eeprom_data(self):
        logging.info("Eeprom data method.")
        # logging.info(f"Selected device node: {self._selected_device_node}")
        if self._selected_device_node is None:
            return None

        eeprom = FtProgramData()
        eeprom.Signature1 = 0x00000000
        eeprom.Signature2 = 0xFFFFFFFF
        eeprom.Version = 2
        eeprom.Manufacturer = ctypes.create_string_buffer(32)
        eeprom.ManufacturerId = ctypes.create_string_buffer(16)
        eeprom.Description = ctypes.create_string_buffer(64)
        eeprom.SerialNumber = ctypes.create_string_buffer(16)
        # logging.info(f"Eeprom: {eeprom}")

        try:
            Ftd2xxhelper.__check(
                self._d2xx.FT_EE_Read(self._ft_handle, ctypes.byref(eeprom))
            )
            # logging.info(f"Eeprom: {eeprom}")
            return eeprom
        except Exception as e:
            logging.error(f"Exception, {e}")
            return None

    def initialize(self, serialNumber: str | bytes | None = None):
        logging.info(f"Initializing device, Serial number: {serialNumber}")
        devs = self.get_dev_info_list()
        logging.info(f"Devices len: {len(devs)}, devices: {devs}")

        self._selected_device_node = None
        self._last_connected_serial_number = None

        if serialNumber is None:
            for dev in devs:
                if dev.Description.decode("ascii").startswith("SANTEC"):
                    self._selected_device_node = dev
                    self._last_connected_serial_number = dev.SerialNumber
                    break
        else:
            for dev in devs:
                if (
                        dev.SerialNumber == serialNumber
                        or dev.SerialNumber.decode("ascii") == serialNumber
                ):
                    self._selected_device_node = dev
                    self._last_connected_serial_number = dev.SerialNumber
                    break
        if self._selected_device_node is None:
            if serialNumber is None:
                logging.error("Value error, Failed to find Santec instruments")
                raise ValueError("Failed to find Santec instruments")
            logging.error(f"Value error, Failed to open device by serial number '{serialNumber}'")
            raise ValueError(f"Failed to open device by serial number '{serialNumber}'")
        self._ft_handle = ctypes.c_void_p()
        Ftd2xxhelper.__check(
            self._d2xx.FT_OpenEx(
                self._last_connected_serial_number, 1, ctypes.byref(self._ft_handle)
            )
        )

        eeprom = self.eeprom_data()
        # logging.info(f"Eeprom: {eeprom}")
        if eeprom is None:
            logging.error(f"Run time error, Failed to retrieve EEPROM data from the device "
                          f"(SN: {self._last_connected_serial_number}, "
                          f"Description: {self._selected_device_node.Description})")
            raise RuntimeError(
                f"Failed to retrieve EEPROM data from the device (SN: {self._last_connected_serial_number}, "
                f"Description: {self._selected_device_node.Description})"
            )
        manufacturer = ctypes.cast(eeprom.Manufacturer, ctypes.c_char_p)
        if manufacturer.value.decode("ascii").upper() == "SANTEC":
            self._initialize()
        logging.info("\nInitialization done.")

    def _initialize(self):
        logging.info("Start _initialize operation.")
        word_len = ctypes.c_ubyte(8)
        stop_bits = ctypes.c_ubyte(0)
        parity = ctypes.c_ubyte(0)
        Ftd2xxhelper.__check(
            self._d2xx.FT_SetDataCharacteristics(
                self._ft_handle, word_len, stop_bits, parity
            )
        )
        flowControl = ctypes.c_uint16(0x00)
        xon = ctypes.c_ubyte(17)
        x_off = ctypes.c_ubyte(19)
        Ftd2xxhelper.__check(
            self._d2xx.FT_SetFlowControl(self._ft_handle, flowControl, xon, x_off)
        )
        baud_rate = ctypes.c_uint64(9600)
        Ftd2xxhelper.__check(self._d2xx.FT_SetBaudRate(self._ft_handle, baud_rate))
        timeout = ctypes.c_uint64(1000)
        Ftd2xxhelper.__check(self._d2xx.FT_SetTimeouts(self._ft_handle, timeout, timeout))
        mask = ctypes.c_ubyte(0x00)
        enable = ctypes.c_ubyte(0x40)
        Ftd2xxhelper.__check(self._d2xx.FT_SetBitMode(self._ft_handle, mask, enable))
        logging.info("_initialize operation done.")

    def open_usb_connection(self):
        logging.info("Open USB connection.")
        self.initialize()

    def close_usb_connection(self):
        # logging.info(f"Closing USB connection, FT Handle: {self._ft_handle}")
        if self._ft_handle is not None:
            self._d2xx.FT_Close(self._ft_handle)
            self._ft_handle = None

    def disconnect(self):
        logging.info("Disconnect device.")
        self.close_usb_connection()

    def write(self, command: str):
        logging.info(f"Write operation, command: {command}")
        try:
            idx = command.index(self.terminator)
            logging.info(f"Idx: {idx}")
            if idx == 0:
                logging.error("Value error, The first character of the write command cannot be the command terminator")
                raise ValueError("The first character of the write command cannot be the command terminator")
            elif not command.endswith(self.terminator):
                command = command[:idx]
                logging.info(f"command: {command}")
        except ValueError as e:
            logging.error(f"Value error, {e}")
            command = command + self.terminator
            logging.info(f"command: {command}")
            # logging.info(f"FT handle: {self._ft_handle}")

        if self._ft_handle is None:
            self._ft_handle = ctypes.c_void_p()
            Ftd2xxhelper.__check(
                self._d2xx.FT_OpenEx(
                    self._last_connected_serial_number, 1, ctypes.byref(self._ft_handle)
                )
            )

        written = ctypes.c_uint()
        commandLen = len(command)
        cmd = (ctypes.c_ubyte * commandLen).from_buffer_copy(command.encode("ascii"))
        logging.info(f"cmd: {cmd}")
        Ftd2xxhelper.__check(
            self._d2xx.FT_Write(self._ft_handle, cmd, commandLen, ctypes.byref(written))
        )
        time.sleep(0.020)

    def read(self, maxTimeToWait: float = 0.020, totalNumberOfBytesToRead: int = 0):
        logging.info(f"Read operation, maxTimeToWait: {maxTimeToWait}, totalNumberOfBytesToRead: {totalNumberOfBytesToRead}")
        if self._ft_handle is None:
            self._ft_handle = ctypes.c_void_p()
            Ftd2xxhelper.__check(
                self._d2xx.FT_OpenEx(
                    self._last_connected_serial_number, 1, ctypes.byref(self._ft_handle)
                )
            )

        timeCounter = 0.0
        sleepTimer = 0.020

        binaryData = bytearray()
        read = False

        try:
            while timeCounter < maxTimeToWait:
                bytesRead = ctypes.c_uint()
                available = ctypes.c_uint()
                timeCounter += sleepTimer
                time.sleep(sleepTimer)
                Ftd2xxhelper.__check(
                    self._d2xx.FT_GetQueueStatus(self._ft_handle, ctypes.byref(available))
                )
                if available.value > 0:
                    read = True
                elif available.value == 0:
                    if read:
                        break
                    else:
                        continue
                arr = (ctypes.c_ubyte * available.value)()
                Ftd2xxhelper.__check(
                    self._d2xx.FT_Read(
                        self._ft_handle, arr, available, ctypes.byref(bytesRead)
                    )
                )
                buf = bytearray(arr)
                binaryData.extend(buf)

                if bytesRead.value > 0:
                    timeCounter = 0

                if (
                        0 < totalNumberOfBytesToRead <= len(binaryData)
                ):
                    break
        except RuntimeError as e:
            logging.error(f"Run time error: {e}")
            raise RuntimeError(e)

        # self.close_usb_connection()
        # logging.info(f"Binary data: {binaryData}")
        return binaryData

    def query_idn(self):
        logging.info("Query Idn")
        return self.query("*IDN?")

    def query(self, command: str, waitTime: int = 1):
        logging.info(f"Query operation, command: {command}, wait time: {waitTime}")
        if self._ft_handle is None:
            self._ft_handle = ctypes.c_void_p()
            Ftd2xxhelper.__check(
                self._d2xx.FT_OpenEx(
                    self._last_connected_serial_number, 1, ctypes.byref(self._ft_handle)
                )
            )

        self.write(command)

        arr = self.read(waitTime)

        response_str = ""
        try:
            response_str = arr.decode("ascii")
            logging.info(f"Response str: {response_str}")
        except UnicodeDecodeError:
            logging.error(f"UnicodeDecodeError, {response_str}, {arr}")
            print(arr)
            return response_str

        if len(response_str) < 3:
            return response_str.strip()
        elif response_str[0] == "\0":
            return response_str

        trimmed = self.__remove_prefix_from_result_if_not_hex(response_str.strip())
        logging.info(f"Trimmed response str: {trimmed}")

        try:
            idx = trimmed.rindex(self.terminator)
            logging.info(f"Idx: {idx}")
            if len(trimmed) - 2 > idx:
                trimmed = trimmed[(idx + 1):].strip()
                logging.info(f"Trimmed: {trimmed}")
        except ValueError as e:
            logging.error(f"Value error, {e}")
            pass

        if trimmed == response_str.strip():
            return trimmed

        return response_str

    @staticmethod
    def __remove_prefix_from_result_if_not_hex(result_str: str):
        logging.info(f"Remove prefix from result if not hex, result str: {result_str}, len: {len(result_str)}")
        if result_str is None or len(result_str) < 3:
            return result_str

        if result_str[0] == "\0":
            return result_str

        # if result_str[0] not in result_str.hexdigits or result_str[1] not in result_str.hexdigits:
        #     return result_str[2:]

        if result_str[0] not in string.hexdigits or result_str[1] not in string.hexdigits:
            return result_str[2:]

        logging.info(f"Result str: {result_str}, len: {len(result_str)}")
        return result_str

    def get_all_data_points_from_last_scan_scpi_command(self):
        logging.info("Get all data points from last scan using SCPI command.")
        getCountCommand = "READout:POINts?"
        getDataCommand = "READout:DATa?"

        points = 0
        response_str = self.query(getCountCommand)
        print(response_str)
        try:
            points = int(response_str)
        except ValueError:
            raise RuntimeError(
                f"Failed to retrieve a valid number of data points from the last scan: {response_str}"
            )

        if points > 200001:
            raise ValueError(
                f"The number of data points received from the last scan is too large: {points}"
            )

        self.write(getDataCommand)
        time.sleep(5)
        arr = self.read(1, points * 4)
        if len(arr) == 0:
            return arr

        if arr[0] != ord("#"):
            print(arr[0])
            raise ValueError(
                f"The value read was supposed to contain a # symbol as the first byte, but contained '{arr[0]}'"
            )

        b = chr(arr[1])
        try:
            val = int(b)
        except Exception as e:
            print(arr[1], b)
            raise ValueError(
                f"The value read was supposed to contain a number as the second byte, but contained '{b}', {e}"
            )

        b = "".join(map(chr, arr[2: 2 + val]))
        try:
            num = int(b)
        except Exception as e:
            print(arr[2: 2 + val], b)
            raise ValueError(
                f"The value read was supposed to contain a number, but contained '{b}', {e}"
            )

        offset = 2 + val
        return list(
            map(
                lambda x: struct.unpack(">f", x),
                Ftd2xxhelper.__chunks(arr[offset:], num, 4),
            )
        )

    def get_all_data_points_from_last_scan_santec_command(self):
        logging.info("Get all data points from last scan using Santec command.")
        getCountCommand = "TN"
        getDataCommand = "TA"

        points = int(self.query(getCountCommand))

        self.write(getDataCommand)
        arr = self.read(1, points * 4)

        if len(arr) != points * 4:
            raise ValueError(
                f"Invalid data with mismatch length returned, expect: {points}, got: {len(arr)}"
            )

        if sys.version_info[1] >= 12:
            import itertools

            return list(
                map(lambda x: int.from_bytes(x, "big"), itertools.batched(arr, 4))
            )

        return list(
            map(
                lambda x: int.from_bytes(x, "big"),
                Ftd2xxhelper.__chunks(arr, points, 4),
            )
        )

    @staticmethod
    def __chunks(arr: bytearray, length: int, n: int = 4):
        logging.info(f"Chunks, arr:{arr}, length: {length}, n: {n}")
        for i in range(0, length):
            yield arr[i * n: i * n + n]
