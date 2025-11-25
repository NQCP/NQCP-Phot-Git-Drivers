from photonicdrivers.Oscilloscopes.Rigol.RigolDHO924S_Driver import RigolDHO924SDriver

ip_address = "10.209.64.205"
driver = RigolDHO924SDriver(ip_address)

driver.connect()
print(driver.identify())
driver.disconnect()