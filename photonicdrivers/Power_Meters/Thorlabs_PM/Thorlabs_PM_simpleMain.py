import pyvisa
from Thorlabs_PM import Thorlabs_PM100D_driver


print("hello")
# Open a VISA resource manager
rm = pyvisa.ResourceManager()

print("hello")

# List available VISA resources (instruments)
available_resources = rm.list_resources()

print("hello")

# Print the list of available resources
print("Available VISA resources:")
for idx, resource in enumerate(available_resources, start=1):
    print(f"{idx}. {resource}")

print("hello")

# Open a VISA instrument connection
powerMeter = Thorlabs_PM100D_driver(rm, "USB0::0x1313::0x807A::M01044633::INSTR")

powerMeter.connect()
print(powerMeter.get_detector_power())
print(powerMeter.get_power_meter_wavelength())
print(powerMeter.get_units())
print(powerMeter.get_averaging())
powerMeter.disconnect()

# Close the instrument connection
rm.close()


