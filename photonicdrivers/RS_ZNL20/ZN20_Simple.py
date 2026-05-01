from photonicdrivers.RS_ZNL20.RS_ZNL20_Driver import RS_ZNL20_Driver

vna_ip = "10.209.67.185"

vna_driver = RS_ZNL20_Driver(ip_address=vna_ip)
vna_driver.connect()
test = vna_driver.identify()
print(test)
vna_driver.disconnect()