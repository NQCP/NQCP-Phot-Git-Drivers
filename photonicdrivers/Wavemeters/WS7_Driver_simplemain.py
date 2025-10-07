from photonicdrivers.Wavemeters.WS7_Driver import WS7_Driver
import time

ws = WS7_Driver("C:\Windows\System32\wlmData.dll")
ws.connect()
print(ws.is_connected())

ch = 1 
ws.set_exposure(channel=ch, exposure_ms=100)

ws.start_measurement()

time.sleep(1)
print("Wavelength (nm): ", ws.get_wavelength_nm(channel=ch))
ws.stop_measurement()