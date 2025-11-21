from photonicdrivers.Oscilloscopes.Rigol.DHO924S import RigolDHO924SDriver

ip_address = "10.209.64.205"
driver = RigolDHO924SDriver(ip_address)

driver.connect()
print(driver.identify())
driver.disconnect()