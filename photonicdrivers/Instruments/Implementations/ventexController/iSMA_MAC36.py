# class to communicate with the iSMA_MAC36 controller that control the Ventek cooling system

from pymodbus.client import ModbusTcpClient #  conda install conda-forge::pymodbus 
from pymodbus import pymodbus_apply_logging_config # to enable debug mode
import struct

class iSMA_MAC36:
    def __init__(self, _ip_address, _port=502, _slave_id=1, _debug=False) -> None:
        # _ip_address: IP of the Modbus TCP server
        # _port: port of the Modbus TCP server. Default is 502
        # _slace_ID: slave ID of the device
        
        print('Inilialisting iSMA_MAC36 class')
        
        if _debug == True:
            print('Enabling debugging mode')
            pymodbus_apply_logging_config("DEBUG")

        self.ip_address = _ip_address
        self.port = _port
        self.slave_id = _slave_id

        # Connect to the Modbus TCP server
        self.client = ModbusTcpClient(self.ip_address, self.port)

        # Open the connection
        self.client.connect()

    
    def closeConnection(self):
        self.client.close()

    def queryKK4Info(self):
        # this function is hardcoded to return the registers relevant for the KK4 lab
        output = self.queryInputRegisters(0,44)
        uInt16Array = output.registers
        floatArray = self.__array_uint16_to_float32(uInt16Array)
        kk4Info = KK4Info(floatArray)
        return kk4Info
        

    def queryInputRegisters(self, registerStart, length):
        # for 3xxxx registers
        return self.client.read_input_registers(registerStart, length, self.slave_id)


    def queryHoldingRegisters(self, registerStart, length):
        # for 4xxxx registers
        return self.client.read_holding_registers(registerStart, length, self.slave_id)

    ##################### PRIVATE METHODS ###########################

    def __array_uint16_to_float32(self, uint16_array):
        # Check if the length of the input array is even
        if len(uint16_array) % 2 != 0:
            raise ValueError("Input array length must be even")

        float_array = []
        for i in range(0, len(uint16_array), 2):
            msb = uint16_array[i] # most significant bit
            lsb = uint16_array[i + 1] # least significant bit

            # Pack the two uint16 values into a byte string
            byte_string = struct.pack('>HH', msb, lsb)

            # Unpack the byte string as a single float32 value
            # >f specifies a float with big-endian (most to least significant bit) byte order
            float_value = struct.unpack('>f', byte_string)[0]

            # Round the number to just two decimals
            float_rounded = "{:.2f}".format(float_value)

            float_array.append(float_rounded)

        return float_array    


class KK4Info:
    # a class to make it easy to identify which values correspond to which variables
    def __init__(self, floatArray):
        print(floatArray)
        # blank = floatArray[0]
        self.IBI01_ACT_SP = floatArray[1]
        self.IBI01_TT001 = floatArray[2]
        self.IBI01_MK201 = floatArray[3]
        self.IBI01_FC = floatArray[4]
        self.IBI01_P = floatArray[5]
        self.IBI01_I = floatArray[6]
        self.IBI01_D = floatArray[7]

        self.IBI02_ACT_SP = floatArray[8]
        self.IBI02_TT001 = floatArray[9]
        self.IBI02_MK201 = floatArray[10]
        self.IBI02_FC = floatArray[11]
        self.IBI02_P = floatArray[12]
        self.IBI02_I = floatArray[13]
        self.IBI02_D = floatArray[14]

        self.IBI03_ACT_SP = floatArray[15]
        self.IBI03_TT001 = floatArray[16]
        self.IBI03_MK201 = floatArray[17]
        self.IBI03_FC = floatArray[18]
        self.IBI03_P = floatArray[19]
        self.IBI03_I = floatArray[20]
        self.IBI03_D = floatArray[21]