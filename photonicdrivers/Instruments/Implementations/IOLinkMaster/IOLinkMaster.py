import socket

from FlowMeterPF3W720 import FlowMeterPF3W720


class IOLinkMaster:
    def __init__(self, IPAddress, PortNumber=0):
        # Create a TCP/IP socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(5) # sets the timeout of the receive command. 
        self.server_address = (IPAddress, PortNumber) #IP address, port
        self.socket.connect(self.server_address)

        # For some reason, there is some output ready immediately after connection has been created. 
        # The format might be a telnet command?
        #print('Immediate output from device:')
        #print(self.socket.recv(1024))

    def getFlowAndTemp(self, pinNumber):
        command = FlowMeterPF3W720.pdin(self, pinNumber)
        # dummy = '{"code":"request","cid":1,"adr":"/iolinkmaster/port[2]/iolinkdevice/pdin/getdata"}'
        self.__writeCommand(command)
        response = self.__readCommand()
        print(response)
        print('end of getflowandtemp')

    def closeConnection(self):
        self.socket.close()

    ##################### PRIVATE METHODS ###########################

    def __writeCommand(self, command):
        # commandString = command + self.termChar
        print(command)
        self.socket.sendall(command.encode('utf-8'))
    
    def __readCommand(self, bitsToRead=4096*16):
        response = self.socket.recv(bitsToRead)
        # print(response)

        # remove the newline characters if present
        # if b"\r\n" in response:
        #     response, dummy  = response.split(b'\r\n')

        # convert from byte string to string
        # response = response.decode('utf-8')
        return response