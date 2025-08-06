# import API classes into the current namespace
from pulsestreamer import PulseStreamer, Sequence 
from photonicdrivers.Pulse_Streamer.Pulse_Streamer_82_Driver import Pulse_Streamer_82_Driver
# Connect to Pulse Streamer
ip_address= "10.209.69.141"
pulse_streamer_driver = Pulse_Streamer_82_Driver(ip_address=ip_address)
pulse_streamer_driver.connect()
print(pulse_streamer_driver.get_serial_number())
print(pulse_streamer_driver.is_connected())
print(pulse_streamer_driver.get_temperature())
print(pulse_streamer_driver.get_temperature())
pulse_streamer_driver.disconnect()
print(pulse_streamer_driver.is_connected())


