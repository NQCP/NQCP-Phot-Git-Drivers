from photonicdrivers.Magnets.APS100_PS_Driver import APS100_PS_Driver

com_port = 'COM6'

ps = APS100_PS_Driver(com_port)
ps.connect()
print(ps.get_id())
ps.disconnect()