import socket
import pyvisa
from instruments.Abstract.Identifiable import Identifiable

import Santec_FTDI as ftdi

class santec_MPM200(Identifiable):

    def __init__(self, port: int = 5000, ip_adress: str = "192.168.1.161"):

        self.serial_number = 25020089
        self.port = port
        self.ip_adress = ip_adress
        self.timeout = 2
        self.socket = None
    
    def connect(self):
        self.laser = ftdi.FTD2xx_helper(self.serial_number)

        #self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.socket.settimeout(self.timeout)
        #self.socket.connect((self.ip_adress, self.port))

    def get_id(self) -> str:
        return self.query('*IDN?')  

if __name__ == "__main__":

    # rm = pyvisa.ResourceManager()




    
    driver = santec_MPM200(port=5000, ip_adress="192.168.1.161")
    driver.connect()

    #available_resources = rm.list_resources()
    
    #for idx, resource in enumerate(available_resources, start=1):
    #        print(f"{idx}. {resource}")
