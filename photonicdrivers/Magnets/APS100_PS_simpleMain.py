from photonicdrivers.Magnets.APS100_PS_Driver import APS100_PS_Driver

# COM6 is PS Y, COM4 is XZ

com_port = 'COM4'

ps = APS100_PS_Driver(com_port)
ps.connect()
print(ps.get_id())
print(ps.get_channel())
print(ps.get_current())
ps.disconnect()