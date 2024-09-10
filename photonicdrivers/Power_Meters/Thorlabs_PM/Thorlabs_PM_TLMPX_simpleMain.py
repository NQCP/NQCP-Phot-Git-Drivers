from photonicdrivers.Power_Meters.Thorlabs_PM.Thorlabs_PM_TLMPX_Driver import Thorlabs_PM_TLMPX_Driver

resourceName = "USB0::0x1313::0x8078::P0041989::INSTR"
power_meter = Thorlabs_PM_TLMPX_Driver(resourceName)
power_meter.connect()
print("power: ")
power = power_meter.get_power()
print(power)
print(type(power))
print("ID: ")
print(power_meter.get_idn())

power_meter.disconnect()