from photonicdrivers.Power_Meters.Thorlabs_PM.Thorlabs_PM_TLMPX_Driver import Thorlabs_PM_TLMPX_Driver

# resourceName = "USB0::0x1313::0x8078::P0041989::INSTR"
#resourceName = "USB0::0x1313::0x8078::P0045344::INSTR"
resourceName = "TCPIP0::10.209.67.196::2000::SOCKET"
power_meter = Thorlabs_PM_TLMPX_Driver(resourceName)
power_meter.connect()


power = power_meter.get_power()
print(power)
print(type(power))


print("ID: ")
print(power_meter.get_idn())

wavelength = power_meter.get_wavelength()
print(wavelength)
print(type(wavelength))

wavelength = power_meter.get_min_wavelength()
print(wavelength)
print(type(wavelength))

wavelength = power_meter.get_max_wavelength()
print(wavelength)
print(type(wavelength))

power_meter.set_wavelength(940)
wavelength = power_meter.get_wavelength()
print(wavelength)
print(type(wavelength))

power_meter.set_power_unit("dBm")
power_unit = power_meter.get_power_unit()
print(power_unit)

power = power_meter.get_power()
print(power)
print(type(power))

power_meter.set_power_unit("W")
power_unit = power_meter.get_power_unit()
print(power_unit)

power = power_meter.get_power()
print(power)
print(type(power))

power_meter.disconnect()