import time

from piezoKPZ101 import PiezoKPZ101

piezo = PiezoKPZ101("29252886")
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