from photonicdrivers.Magnets.APS100_PS_Driver import APS100_PS_Driver
from time import sleep

# COM6 is PS Y, COM4 is XZ

com_port = 'COM6'

ps = APS100_PS_Driver(com_port)
ps.connect()
print("getting ID:")
print(ps.get_id())

# print("getting channel:")
# print(ps.get_channel())

print(ps.get_current())
print(ps.get_unit())

# print("setting mode:")
# print(ps.set_control_remote())

ps.set_current(0.5)
# ps.send_custom_command("SWEEP ZERO")

# print("getting mode:")
# print(ps.get_mode())
sleep(1)
print(ps.get_current())

ps.disconnect()