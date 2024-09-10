import pyvisa
from photonicdrivers.Power_Meters.Thorlabs_PM.Thorlabs_PM100D_Driver import Thorlabs_PM100D_Driver


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
powerMeter = Thorlabs_PM100D_Driver("USB0::0x1313::0x807A::M01044633::INSTR")

powerMeter.connect()
print(powerMeter.get_power())
print(powerMeter.get_wavelength())
print(powerMeter.get_units())
print(powerMeter.get_averaging())
powerMeter.disconnect()

# Close the instrument connection
rm.close()


