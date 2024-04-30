from IOLinkMaster import IOLinkMaster

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.settimeout(5) # sets the timeout of the receive command. 
# server_address = ('10.209.67.95',80) #IP address, port
# sock.connect(server_address)

# print('I got this far!')

# r = requests.post('http://10.209.67.95:80', json={"code":"request","cid":1,"adr":"/iolinkmaster/port[2]/iolinkdevice/pdin/getdata"})
# print(r.json)

# print('I got this far again!')

IOLink = IOLinkMaster('10.209.67.95',80)
IOLink.getFlowAndTemp('2')
IOLink.closeConnection()
