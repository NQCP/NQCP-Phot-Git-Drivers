from photonicdrivers.ANC300.ANC300_Driver import ANC300_Driver

d = ANC300_Driver("ASRL9::INSTR")
d.connect()
print(d.get_version())