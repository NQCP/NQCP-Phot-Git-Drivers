"""
SME - Single Measurement mode operation.

Supported Communication modes
GPIB and TCPIP.
"""

# Basic Imports
import struct
import time
import logging

# Initialize the logger
logger = logging.getLogger("SME Operation")
logging.basicConfig(
    level=logging.INFO,
    encoding='utf-8',
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler('sme_operation.log', mode="w"),
    ],
)


class SME:
    def __init__(self, tsl, mpm):
        self.laser = tsl
        self.power_meter = mpm
        logger.info("Initialized SME process.")


    def configure_tsl(
        self,
        start_wavelength: float,
        stop_wavelength: float,
        step_wavelength: float,
        output_power: float,
        scan_speed: float,
    ):
        """Configure the TSL."""
        logger.info("Configuring TSL parameters.")

        # Reset and basic setup
        self.laser.write('*CLS')  # Clear status
        self.laser.write('*RST')  # Reset device

        # Sets the command set to Legacy.
        self.laser.write('SYST:COMM:COD 0')

        # Sets the command delimiter for GPIB communication.
        self.laser.write('SYST:COMM:GPIB:DEL 2')

        # Turn on output if off
        if int(self.laser.query('POW:STAT?')) == 0:
            self.laser.write('POW:STAT 1')
            while (
                int(self.laser.query('*OPC?')) == 0
            ):  # Queries the completion of operation.
                time.sleep(0.5)

        # Units and mode settings
        self.laser.write('POW:UNIT 0')  # Set power unit to dBm
        self.laser.write('WAV:UNIT 0')  # Set wavelength unit to nm
        self.laser.write('POW:ATT:AUT 1')  # Auto power control mode
        self.laser.write('COHCtrl 0')  # Disable coherence control
        self.laser.write('POW:SHUT 0')  # Open the internal shutter

        # Scan settings
        self.laser.write(f'POW {output_power}')  # Set output power
        self.laser.write(f'WAV:SWE:STAR {start_wavelength}')  # Set start wavelength
        self.laser.write(f'WAV:SWE:STOP {stop_wavelength}')  # Set stop wavelength
        self.laser.write(f'WAV:SWE:SPE {scan_speed}')  # Set sweep speed
        self.laser.write(f'TRIG:OUTP:STEP {step_wavelength}')  # Set trigger step size


    def configure_mpm(
        self,
        start_wavelength: float,
        stop_wavelength: float,
        step_wavelength: float,
        scan_speed: float,
        is_mpm_215: bool = False,
    ):
        """
        Configure the MPM.

        Parameters
            is_mpm_215: True if using an MPM-215 module, else False.
        """
        logger.info(f"Configuring MPM parameters. Is MPM 215: {is_mpm_215}")

        # Stop any ongoing measurements
        self.power_meter.write('STOP')
        # Set the mpm power unit to dBm
        self.power_meter.write('UNIT 0')
        self.power_meter.write('AUTO 1')
        measurement_mode = 'SWEEP2'

        # Trigger settings
        # Enable external trigger
        self.power_meter.write('TRIG 1')

        # Scan settings
        self.power_meter.write(f'WMOD {measurement_mode}')
        self.power_meter.write(f'WSET {start_wavelength},{stop_wavelength},{step_wavelength}')
        self.power_meter.write(f'SPE {scan_speed}')  # Set sweep speed

        time.sleep(0.5)

        # Force set the measurements mode if not set
        while True:
            if measurement_mode in self.power_meter.query('WMOD?'):
                break
            self.power_meter.write(f'WMOD {measurement_mode}')
        print("Set Sweep mode: ", self.power_meter.query('WMOD?'))


        # Set the expected read data count
        if not is_mpm_215:
            data_count = int((stop_wavelength - start_wavelength) / step_wavelength + 1)
            self.power_meter.write(f'LOGN {data_count}')


    def perform_scan(self, display_logging_status: bool = False):
        """Executes the wavelength sweep and triggers measurement."""
        logger.info(
            f"Performing Scan. Display logging status: {display_logging_status}."
        )

        print("\nStarting the SME process....\n")

        # Start MPM measurements
        self.power_meter.write('MEAS')

         # Start timer
        start_time = time.time()

        # Start TSL scan
        self.laser.write(':WAV:SWE 1')
        self.laser.write(':WAV:SWE:DEL 1')
        swe_count_in = int(self.laser.query(':WAV:SWE:COUN?'))
        swe_count = swe_count_in
        while swe_count-swe_count_in == 0:
            swe_count = int(self.laser.query(':WAV:SWE:COUN?'))
            time.sleep(0.1)
        self.laser.write(':WAV:SWE 0')
        # # Check TSL status and force set TSL to start scan if not started
        # scan_status = int(self.laser.query(':WAV:SWE?'))
        # time.sleep(0.2)
        # while scan_status != 4:
        #     scan_status = int(self.laser.query(':WAV:SWE?'))
        #     print(scan_status)
        #     time.sleep(0.2)
        # self.laser.write(':WAV:SWE 0')
        # # Issue software trigger to the TSL
        # print("siamo oltre")

       

        # # Wait for measurements to complete
        # while (
        #         int(self.power_meter.query("STAT?").split(',')[0]) == 0
        # ):
        #     # Print the MPM logging status
        #     if display_logging_status:
        #         status, count = self.power_meter.query("STAT?").split(',')
        #         print_string = f"Logging Status: {status}. Data Count: {count}"
        #         logger.debug(print_string)
        #         print(print_string)
        #     time.sleep(0.2)

        # Scan end time and calculate elapsed time
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 2)

        status, count = self.power_meter.query("STAT?").split(',')
        print_string = f"Logging Status: {status}. Total Data Count: {count}"
        logger.info(print_string)
        print(f"\n{print_string}")

        print_string = (
            f"SME process completed. \nScan elapsed time: {elapsed_time} seconds."
        )
        logger.info(print_string)
        print(f"\n{print_string}")
        # Stop logging first if necessary
        #self.power_meter.write("LOGS 0")

        # Request log data
        self.power_meter.write("LOGG? 0, 4")

        # Step 1: Read header
        header_start = self.power_meter.read_bytes(1)      # should be b'#'
        num_digits_byte = self.power_meter.read_bytes(1)   # ASCII digit
        num_digits = int(num_digits_byte.decode('ascii'))
        byte_count_ascii = self.power_meter.read_bytes(num_digits)  # total binary byte count
        byte_count = int(byte_count_ascii.decode('ascii'))

        print(f"Expecting {byte_count} bytes of binary data...")

        # Step 2: Read binary data
        binary_data = self.power_meter.read_bytes(byte_count)

        # Step 3: Convert to floats (little endian)
        num_floats = byte_count // 4
        log_values = list(struct.unpack('<' + 'f'*num_floats, binary_data))

        print(f"Received {len(log_values)} points") 
        return log_values