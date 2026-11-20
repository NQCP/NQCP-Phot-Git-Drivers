"""
Deprecated compatibility shim for the Santec TSL-570 USB/FTDI driver.

The TSL-570 is driven over ethernet, and maintaining a second USB driver meant writing
every command twice. This module now re-exports Santec_TSL570_Ethernet_Driver so that
existing scripts and notebooks importing this path keep working.

Import photonicdrivers.Lasers.Santec_TSL570.Santec_TSL570_Ethernet_Driver directly in
new code. Note that Santec_TSL570_driver now takes ip_address and port_number, not a
USB serial number.
"""

import warnings

from photonicdrivers.Lasers.Santec_TSL570.Santec_TSL570_Ethernet_Driver import *  # noqa: F401,F403

warnings.warn(
    "Santec_TSL570_Driver is deprecated. Import Santec_TSL570_Ethernet_Driver instead; "
    "the USB/FTDI driver has been removed.",
    DeprecationWarning,
    stacklevel=2,
)
