'''
Hardware bring-up script for a Vaunix LDA attenuator over Ethernet.

There is no discovery API on Windows, so set IP_ADDRESS below to the unit's address
before running. Find it with the Vaunix GUI over USB, or from the device's own web
interface.

The most useful check here is that the serial number reported over Ethernet matches
the one the USB driver reports for the same physical box -- that is the strongest
single confirmation that both ctypes bindings are correct.
'''

from photonicdrivers.Variable_Digital_Attenautor.Vaunix_LDA_Constants import (
    Vaunix_LDA_Transport_Error,
    describe_features,
)
from photonicdrivers.Variable_Digital_Attenautor.Vaunix_LDA_Ethernet_Driver import (
    Vaunix_LDA_Ethernet_Driver,
)

IP_ADDRESS = "192.168.100.5"

# Set to the serial number printed on the unit to have connect() verify that the
# device at IP_ADDRESS is really the one you meant. Leave as None to skip the check.
EXPECTED_SERIAL_NUMBER = None

WORKING_FREQUENCY_MHZ = 6000
TARGET_ATTENUATION_DB = 31.5

print(f"Connecting to the LDA at {IP_ADDRESS}")
attenuator = Vaunix_LDA_Ethernet_Driver(
    ip_address=IP_ADDRESS,
    serial_number=EXPECTED_SERIAL_NUMBER,
)
attenuator.connect()

info = attenuator.get_device_info()
print("\nDevice info:")
print(f"    model               {info.model_name}")
print(f"    serial              {info.serial_number}")
print(f"    firmware            {info.software_version}")
print(f"    DLL version         {info.dll_version}")
print(f"    channels            {info.number_of_channels}")
print(f"    features            {describe_features(info.features)}")
print(f"    attenuation range   {info.min_attenuation_dB} .. {info.max_attenuation_dB} dB")
print(f"    attenuation step    {info.attenuation_step_dB} dB  (from the constructor, not the device)")
print(f"    frequency range     {info.min_frequency_MHz} .. {info.max_frequency_MHz} MHz")
print(f"    profile max length  {info.profile_max_length} points")

print("\nNetwork configuration:")
print(f"    ip address          {attenuator.get_ip_address()}")
print(f"    netmask             {attenuator.get_netmask()}")
print(f"    gateway             {attenuator.get_gateway()}")
print(f"    address mode        {attenuator.get_ip_mode()}")

print(f"\nSetting working frequency to {WORKING_FREQUENCY_MHZ} MHz")
attenuator.set_frequency_MHz(WORKING_FREQUENCY_MHZ)
print(f"    reads back {attenuator.get_frequency_MHz()} MHz")

print(f"\nSetting attenuation to {TARGET_ATTENUATION_DB} dB")
attenuator.set_attenuation_dB(TARGET_ATTENUATION_DB)
print(f"    reads back {attenuator.get_attenuation_dB()} dB")

off_grid_dB = TARGET_ATTENUATION_DB + 0.03
print(f"\nSetting an off-grid {off_grid_dB} dB (expect quantisation to the {info.attenuation_step_dB} dB grid)")
attenuator.set_attenuation_dB(off_grid_dB)
print(f"    reads back {attenuator.get_attenuation_dB()} dB")

too_much_dB = info.max_attenuation_dB + 5
print(f"\nRequesting {too_much_dB} dB (expect ValueError)")
try:
    attenuator.set_attenuation_dB(too_much_dB)
    print("    ERROR: the out-of-range request was accepted")
except ValueError as error:
    print(f"    rejected as expected: {error}")

# ldadrvr.h documents fnLDA_GetProfileIndex as unsupported over Ethernet, and the
# exported symbol returns success with a meaningless value, so the driver blocks it.
print("\nCalling get_profile_index (expect Vaunix_LDA_Transport_Error)")
try:
    attenuator.get_profile_index()
    print("    ERROR: the unsupported call was allowed through")
except Vaunix_LDA_Transport_Error as error:
    print(f"    blocked as expected: {error}")

print("\nReturning to 0 dB and disconnecting")
attenuator.set_attenuation_dB(info.min_attenuation_dB)
attenuator.disconnect()
print(f"is_connected: {attenuator.is_connected()}")
