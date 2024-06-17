## Python sample script to communicate with RLS Picus laser

import pyvisa

from photonicdrivers.Controller.Instruments.Implementations.Lasers.Picos.Picos_Q_OEM import Picos_Q_OEM

rm = pyvisa.ResourceManager()
print(rm.list_resources())

picos = Picos_Q_OEM(rm, 'ASRL3::INSTR')
picos.connect()
picos.turn_on_emission()

picos.turn_off_emission()

picos.disconnect()