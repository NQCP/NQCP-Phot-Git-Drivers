"""
SME - Single Measurement mode operation.

Supported Instruments
TSL series and MPM series.

Supported Communication modes
GPIB and TCPIP.
"""
# Import the SME class
from sme_operation import SME
import matplotlib.pyplot as plt
import numpy as np
%matplotlib qt
def main(tsl, mpm):
    """Main workflow to initialize, configure, and perform the sweep."""
    # Create an instance and initialize SME class
    sme = SME(tsl, mpm)

    # Collect user inputs
    power = float(-15)  # in dBm
    start_wavelength = float(1240)
    stop_wavelength = float(1370)
    speed = float(20)  # in nm/s
    step = float(0.1)

    # Configure TSL and MPM parameters
    sme.configure_tsl(start_wavelength, stop_wavelength, step, power, speed)

    sme.configure_mpm(
        start_wavelength,
        stop_wavelength,
        step,
        speed,
        is_mpm_215=False,
    )  # Set is_mpm_215 to True if using MPM-215 module


    # Perform sweep
    # Set display_logging_status True to print the MPM logging status
    g = sme.perform_scan(display_logging_status=True)
    v_every4 = g#[3::4]  # index 3 is the 4th element (0-based indexing)
    p_watts = 10**(np.array(v_every4)/10-3)
    print(v_every4)  # Output: [40 80]

    # Plot
    plt.plot(np.arange(start_wavelength,stop_wavelength,step), p_watts[0:len(np.arange(start_wavelength,stop_wavelength,step))])
    plt.xlabel("spettro (nm)")
    plt.ylabel('Watt')
    plt.title('')
    plt.show()


if __name__ == "__main__":
    
    from photonicdrivers.Lasers.Santec_TSL570.Santec_TSL570_Ethernet_Driver import (
        Santec_TSL570_driver,
    )
    from photonicdrivers.Power_Meters.MPM220.Santec_MPM220_driver import (
        santec_MPM220_driver,
    )


    # Connect to the TSL and MPM instruments

    tsl_instrument = Santec_TSL570_driver(
        ip_address="10.209.69.95", port_number="5000", prints_enabled=False
    )
    tsl_instrument.connect()

    mpm_instrument = santec_MPM220_driver(address="GPIB0::16::INSTR")
    mpm_instrument.connect()

    if not tsl_instrument or not mpm_instrument:
        raise Exception("Could not connect to TSL / MPM instrument(s).")

    print("Connected to the instruments:")
    print(tsl_instrument.query("*IDN?"))
    print(mpm_instrument.query("*IDN?"))

    # Execute the main function
    main(tsl_instrument, mpm_instrument)

    tsl_instrument.disconnect()
    mpm_instrument.disconnect()
