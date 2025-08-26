from photonicdrivers.Magnets.APS100_PS_Driver import APS100_PS_Driver
from time import sleep

# COM6 is PS Y, COM4 is XZ

# com_port = 'COM6'
ip = '10.209.67.152'
port = 4444
ps = APS100_PS_Driver(IP_address=ip, IP_port=port)
ps.connect()



# print("getting ID:")
# print(ps.get_id())
print(ps.set_control_remote())

# print("getting channel:")
# print(ps.get_channel())

# print(ps.get_current())
ps.set_unit("kG")
# print(ps.get_unit())

# ps.set_upper_limit(1, "kG")
# print(ps.get_upper_limit()[0])
# ps.ramp_up(wait_while_ramping=True, target_relative_tolerance=0.05)
# print(ps.get_current())
# ps.ramp_to_zero(wait_while_ramping=True)
# print(ps.get_current())
# print(ps.get_field())

ps.disconnect()