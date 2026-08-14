'''
Hardware bring-up script for a Vaunix LDA attenuator over USB.

Run this first when commissioning a unit. It enumerates what is attached, opens
the first device found, prints everything the device reports about itself, then
exercises attenuation, quantisation and range rejection.

Set TEST_MODE = True to run against the DLL's two simulated attenuators instead of
real hardware. That still exercises the full ctypes binding, which is where wrong
argtypes would surface, so it is worth doing before touching a real device.
'''

from photonicdrivers.Variable_Digital_Attenuator.Vaunix_LDA_Constants import (
    HAS_HIRES,
    describe_features,
)
from photonicdrivers.Variable_Digital_Attenuator.Vaunix_LDA_USB_Driver import (
    Vaunix_LDA_USB_Driver,
    set_test_mode,
)

TEST_MODE = False

# Leave as None to use the first enumerated device, or set it to pick a specific unit.
SERIAL_NUMBER = None

WORKING_FREQUENCY_MHZ = 6000
TARGET_ATTENUATION_DB = 31.5

if TEST_MODE:
    # The DLL invents two attenuators when test mode is on.
    set_test_mode(True)
    print("TEST MODE: talking to the DLL's simulated attenuators, not real hardware.\n")

print("Enumerating LDA devices on USB:")
devices = Vaunix_LDA_USB_Driver.list_usb_devices()
for device in devices:
    print(f"    devid={device.device_id}  serial={device.serial_number}  model={device.model_name}")

if not devices:
    raise SystemExit(
        "No LDA devices found. Check the USB cable, make sure the Vaunix GUI is closed "
        "(it claims the HID handle exclusively), or set TEST_MODE = True."
    )

serial_number = SERIAL_NUMBER if SERIAL_NUMBER is not None else devices[0].serial_number
print(f"\nUsing serial {serial_number}")

attenuator = Vaunix_LDA_USB_Driver(serial_number=serial_number)
attenuator.connect()

info = attenuator.get_device_info()
print("\nDevice info:")
print(f"    model               {info.model_name}")
print(f"    serial              {info.serial_number}")
print(f"    DLL version         {info.dll_version}")
print(f"    channels            {info.number_of_channels}")
print(f"    features            {describe_features(info.features)}")
print(f"    attenuation range   {info.min_attenuation_dB} .. {info.max_attenuation_dB} dB")
print(f"    attenuation step    {info.attenuation_step_dB} dB")
print(f"    frequency range     {info.min_frequency_MHz} .. {info.max_frequency_MHz} MHz")
print(f"    profile max length  {info.profile_max_length} points")

# The LDA-908V is a high-resolution part; the attenuation calibration is selected
# by working frequency, so this is worth confirming.
print(f"\nHAS_HIRES set: {bool(info.features & HAS_HIRES)}")

# Only a frequency-compensated model reports a working frequency range. The vendor's
# own demos gate these calls the same way, and the DLL's simulated LDA-102 has none.
if info.max_frequency_MHz > info.min_frequency_MHz:
    print(f"\nSetting working frequency to {WORKING_FREQUENCY_MHZ} MHz")
    attenuator.set_frequency_MHz(WORKING_FREQUENCY_MHZ)
    print(f"    reads back {attenuator.get_frequency_MHz()} MHz")
else:
    print("\nSkipping working frequency: this model reports no frequency range, so its")
    print("attenuation is not frequency-compensated.")

print(f"\nSetting attenuation to {TARGET_ATTENUATION_DB} dB")
attenuator.set_attenuation_dB(TARGET_ATTENUATION_DB)
print(f"    reads back {attenuator.get_attenuation_dB()} dB")

# The API unit is 0.05 dB but the hardware resolves 0.1 dB, so an off-grid request
# is quantised rather than rejected.
off_grid_dB = TARGET_ATTENUATION_DB + 0.03
print(f"\nSetting an off-grid {off_grid_dB} dB (expect quantisation to the {info.attenuation_step_dB} dB grid)")
attenuator.set_attenuation_dB(off_grid_dB)
print(f"    reads back {attenuator.get_attenuation_dB()} dB")

# Out of range is rejected rather than clamped, so a bad setpoint cannot silently
# become a plausible-looking measurement.
too_much_dB = info.max_attenuation_dB + 5
print(f"\nRequesting {too_much_dB} dB (expect ValueError)")
try:
    attenuator.set_attenuation_dB(too_much_dB)
    print("    ERROR: the out-of-range request was accepted")
except ValueError as error:
    print(f"    rejected as expected: {error}")

SWEEP_STRIDE_DB = 10.0
print(f"\nStepping through the range in {SWEEP_STRIDE_DB} dB strides:")
setpoint_dB = info.min_attenuation_dB
while setpoint_dB <= info.max_attenuation_dB:
    attenuator.set_attenuation_dB(setpoint_dB)
    print(f"    set {setpoint_dB:6.1f} dB -> read {attenuator.get_attenuation_dB():6.1f} dB")
    setpoint_dB += SWEEP_STRIDE_DB

print("\nReturning to 0 dB and disconnecting")
attenuator.set_attenuation_dB(info.min_attenuation_dB)
attenuator.disconnect()
print(f"is_connected after disconnect: {attenuator.is_connected()}")

