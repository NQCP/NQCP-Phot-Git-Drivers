# Open a known device by resource string
from anyvisa import AnyVisa

#USB example:      "TCPIP0::10.10.4.77::PM5020_07::INSTR"
#Serial example    "TCPIP0::10.10.4.77::PM5020_07::INSTR"
#Ethernet example  "TCPIP0::10.10.4.77::PM5020_07::INSTR"
#BLE example       "TCPIP0::10.10.4.77::PM5020_07::INSTR"

#Use with pattern to ensure all resources are released finally
print(AnyVisa.FindResources())
with AnyVisa.TL_Open("TCPIP0::10.209.67.184::PM5020_07::INSTR") as device:
    #print device resource string and used library (pyvisa or tlvisa)
    print(device,device.lib())
    #print device identification
    print(device.auto_query("*IDN?"))
