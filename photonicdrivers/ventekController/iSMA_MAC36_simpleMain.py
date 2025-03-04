from photonicdrivers.ventekController.ISMA_MAC36_Driver import ISMA_MAC36_Driver
#from iSMA_MAC36 import KK4Info

# Define the Modbus server IP address and port
SERVER_HOST = '10.209.67.120'  # Change this to your Modbus server IP address
SERVER_PORT = 502           # Change this to your Modbus server port

# Define the Modbus slave ID
SLAVE_ID = 10  # Change this to your Modbus slave ID

# Define the Modbus register address to read
REGISTER_ADDRESS = 0

controller = ISMA_MAC36_Driver(SERVER_HOST,SERVER_PORT,SLAVE_ID)
info = controller.queryKK4Info()
#print(info)
print(info.IBI01_TT001)

controller.disconnect()