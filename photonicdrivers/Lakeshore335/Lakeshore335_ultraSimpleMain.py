# https://pypi.org/project/lakeshore/
# https://lake-shore-python-driver.readthedocs.io/en/latest/model_335.html 

from lakeshore import Model335, Model335InputSensorSettings

# Connect to the first available Model 335 temperature controller over USB using a baud rate of 57600
my_model_335 = Model335(57600,com_port="COM5")

# Create a new instance of the input sensor settings class
# sensor_settings = Model335InputSensorSettings(my_model_335.InputSensorType.DIODE, True, False,
#                                               my_model_335.InputSensorUnits.KELVIN,
#                                               my_model_335.DiodeRange.TWO_POINT_FIVE_VOLTS)

# # Apply these settings to input A of the instrument
# my_model_335.set_input_sensor("A", sensor_settings)

# # Set diode excitation current on channel A to 10uA
# my_model_335.set_diode_excitation_current("A", my_model_335.DiodeCurrent.TEN_MICROAMPS)

# Collect instrument data
heater_output_1 = my_model_335.get_heater_output(1)
heater_output_2 = my_model_335.get_heater_output(2)
temperature_reading = my_model_335.get_all_kelvin_reading()

print(heater_output_1)
print(heater_output_2)
print(temperature_reading)

print(my_model_335.query('*IDN?'))
print(my_model_335.get_kelvin_reading(str(1)))
