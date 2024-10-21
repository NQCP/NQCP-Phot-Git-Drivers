import serial
import time

COM_PORT = 'COM8'
BAUD_RATE = 9600

device = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
device.write(b'*IDN?\n')
time.sleep(0.5)
response = device.readline().decode('utf-8').strip()