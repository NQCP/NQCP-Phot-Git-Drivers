import time

from photonicdrivers.Piezo_KPZ101.PiezoKPZ101_Driver import PiezoKPZ101_Driver

piezo = PiezoKPZ101_Driver("29252886")
piezo.enable()
piezo.setZero()
time.sleep(1)
piezo.getStatus()

output = piezo.getOutputVoltage()
print(output)
time.sleep(0.5)
piezo.setOutputVoltage("4.0")
time.sleep(0.5)
output = piezo.getOutputVoltage()
print(f'Moved to Voltage {output}')

# piezo.setZero()
time.sleep(0.5)
output = piezo.getOutputVoltage()
print(f'Moved to Voltage {output}')

piezo.disable()
time.sleep(1)
piezo.getStatus()