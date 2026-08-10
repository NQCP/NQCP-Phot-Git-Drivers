'''
Vendor constants, exceptions and unit conversions shared by the two Vaunix LDA drivers.

Transcribed from the Vaunix Lab Brick LDA SDK headers:

    LDA_SDK_06-08-2026/LDA_SDK_06-08-2026/Windows SDK/USB/USB/VNX_LDA_api.h
    LDA_SDK_06-08-2026/LDA_SDK_06-08-2026/Windows SDK/Ethernet/Ethernet/ldadrvr.h

This module holds no DLL handle and performs no I/O, so every helper here is
directly unit-testable without hardware. All DLL interaction lives in
Vaunix_LDA_USB_Driver.py and Vaunix_LDA_Ethernet_Driver.py.

UNITS
-----
The canonical internal unit for attenuation is 0.05 dB counts on BOTH transports.

The USB DLL exposes each attenuation function twice: a legacy name in 0.25 dB
units and a "...HR" name in 0.05 dB units. The Ethernet DLL has only the 0.05 dB
form, under the legacy name. To keep one scale factor across both drivers, the
USB driver calls the "...HR" names EXCLUSIVELY and never the 0.25 dB variants.
Every 0.25 dB USB function has an HR twin, so that rule has no exceptions --
do not "simplify" the USB driver to fnLDA_SetAttenuation.

Frequency is in 100 kHz units (MHz / 10) on both transports. Dwell, idle and
hold times are in milliseconds on both transports and need no conversion.
'''

from __future__ import annotations

import math

# ============================== status codes ==================================

# --- USB, from VNX_LDA_api.h. Every error code has the high bit set. ---
STATUS_OK = 0
INVALID_DEVID = 0x80000000
BAD_PARAMETER = 0x80010000
BAD_HID_IO = 0x80020000
DEVICE_NOT_READY = 0x80030000
FEATURE_NOT_SUPPORTED = 0x80040000

USB_STATUS_NAMES = {
    INVALID_DEVID: "INVALID_DEVID (device id is not in the DLL's table; re-enumerate)",
    BAD_PARAMETER: "BAD_PARAMETER (value out of range for this device)",
    BAD_HID_IO: "BAD_HID_IO (Windows HID I/O failure; device unplugged, or claimed by another process)",
    DEVICE_NOT_READY: "DEVICE_NOT_READY (device not opened, or the DLL's read thread has not populated it yet)",
    FEATURE_NOT_SUPPORTED: "FEATURE_NOT_SUPPORTED (this LDA model lacks the feature)",
}

# --- Ethernet, from ldadrvr.h. A single undifferentiated error code. ---
ETH_STATUS_OK = 0
ETH_STATUS_ERROR = 1

ETH_STATUS_NAMES = {
    ETH_STATUS_ERROR: (
        "STATUS_ERROR (the Ethernet DLL reports no further detail; usual causes: device not "
        "reachable, fnLDA_InitDevice not called, value out of range, or feature unsupported)"
    ),
}

# ============================ device status bits ==============================
# fnLDA_GetDeviceStatus, USB only. There is no equivalent over Ethernet.

DEV_CONNECTED = 0x00000001
DEV_OPENED = 0x00000002
SWP_ACTIVE = 0x00000004
SWP_UP = 0x00000008
SWP_REPEAT = 0x00000010
SWP_BIDIRECTIONAL = 0x00000020
PROFILE_ACTIVE = 0x00000040
DEV_LOCKED = 0x00002000
DEV_RDTHREAD = 0x00004000
DEV_V2FEATURES = 0x00008000
DEV_HIRES = 0x00010000

DEVSTATUS_MASK = SWP_ACTIVE | SWP_UP | SWP_REPEAT | SWP_BIDIRECTIONAL | PROFILE_ACTIVE

# ============================== feature bits =================================
# fnLDA_GetFeatures, both transports (different call shapes, same bit meanings).

DEFAULT_FEATURES = 0x00000000
HAS_BIDIR_RAMPS = 0x00000001
HAS_PROFILES = 0x00000002
HAS_HIRES = 0x00000004
HAS_4CHANNELS = 0x00000008
HAS_8CHANNELS = 0x00000010
HAS_LONG_PROFILE = 0x00000020
HAS_MCHANNELS = 0x00000040

FEATURE_NAMES = {
    HAS_BIDIR_RAMPS: "HAS_BIDIR_RAMPS",
    HAS_PROFILES: "HAS_PROFILES",
    HAS_HIRES: "HAS_HIRES",
    HAS_4CHANNELS: "HAS_4CHANNELS",
    HAS_8CHANNELS: "HAS_8CHANNELS",
    HAS_LONG_PROFILE: "HAS_LONG_PROFILE",
    HAS_MCHANNELS: "HAS_MCHANNELS",
}

# ================================== sizes ====================================

MAXDEVICES = 64        # largest device table the USB DLL will report
MAX_MODELNAME = 32     # USB;  Ethernet ldadrvr.h agrees
MAX_SWVERSION = 7      # Ethernet only -- 7 chars, so a buffer needs 8 with the NUL
MAX_NETBUFF = 16       # Ethernet only -- dotted-quad strings
PROFILE_MAX = 100      # nominal; always prefer fnLDA_GetProfileMaxLength from the device

# String out-buffer size used for every char* out-param. Comfortably above the
# largest of the above; the vendor Python example uses 32 for the same reason.
STRING_BUFFER_SIZE = 32

# ============================== profile modes ================================
# fnLDA_StartProfile mode argument.

PROFILE_OFF = 0
PROFILE_ONCE = 1
PROFILE_REPEAT = 2

# ================================ IP modes ===================================
# fnLDA_GetIPMode, Ethernet only.

IP_MODE_STATIC = 0
IP_MODE_DHCP = 1

IP_MODE_NAMES = {IP_MODE_STATIC: "static", IP_MODE_DHCP: "DHCP"}

# ================================ exceptions =================================


class Vaunix_LDA_Error(RuntimeError):
    '''
    An error reported by one of the Vaunix LDA DLLs.
    '''


class Vaunix_LDA_Feature_Error(Vaunix_LDA_Error):
    '''
    The connected unit does not have the requested feature, i.e. the relevant
    fnLDA_GetFeatures bit is clear. This is a runtime property of the hardware.
    '''


class Vaunix_LDA_Transport_Error(NotImplementedError):
    '''
    This transport's DLL does not export the entry point the method needs. This
    is a static fact about the SDK, not a property of the connected unit, so it
    is raised regardless of which device is attached.
    '''


# ============================ unit conversions ===============================

DB_PER_COUNT = 0.05
COUNTS_PER_DB = 20
MHZ_PER_FREQ_COUNT = 0.1
FREQ_COUNTS_PER_MHZ = 10


def round_half_up(value: float) -> int:
    '''
    Round half away from zero.

    Python's built-in round() is banker's rounding, so round(2.5) == 2 while
    round(3.5) == 4. Applied to attenuation counts that makes neighbouring
    setpoints quantise inconsistently, so it is not used anywhere in these drivers.
    '''
    if value >= 0:
        return int(math.floor(value + 0.5))
    return -int(math.floor(-value + 0.5))


def u32(value: int) -> int:
    '''
    Reinterpret a signed C int return value as the unsigned 32-bit status code the
    DLL actually sent.

    ctypes gives every one of these entry points a restype of c_int, so the error
    code 0x80010000 arrives in Python as -2147418112. Masking recovers the code.
    '''
    return value & 0xFFFFFFFF


def db_to_counts(attenuation_dB: float) -> int:
    '''
    Convert attenuation in dB to the device's 0.05 dB counts.
    '''
    return round_half_up(attenuation_dB * COUNTS_PER_DB)


def counts_to_db(counts: int) -> float:
    '''
    Convert the device's 0.05 dB counts to attenuation in dB.
    '''
    return counts * DB_PER_COUNT


def mhz_to_counts(frequency_MHz: float) -> int:
    '''
    Convert a frequency in MHz to the device's 100 kHz counts.
    '''
    return round_half_up(frequency_MHz * FREQ_COUNTS_PER_MHZ)


def counts_to_mhz(counts: int) -> float:
    '''
    Convert the device's 100 kHz counts to a frequency in MHz.
    '''
    return counts * MHZ_PER_FREQ_COUNT


def describe_features(features: int) -> str:
    '''
    Render a fnLDA_GetFeatures bitfield as a human-readable string, for error
    messages and device info dumps.
    '''
    names = [name for bit, name in FEATURE_NAMES.items() if features & bit]
    return f"0x{features:08X} (" + (" | ".join(sorted(names)) if names else "no optional features") + ")"
