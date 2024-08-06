class FlowMeterPF3W720:
    def __init__(self):
        print("initialising a flowmeter")

    def getUrl_pdin_getData(self, pinNumber):
        # The url ending is device specific
        return f"/port[{pinNumber}]/iolinkdevice/pdin/getdata"
    
    def pdin_iolreadacyclic(self, pinNumber):
        pass
    
    def convert_pdinData(self, response_raw_hex):
        binary_number = self.__hex_to_binary(response_raw_hex)
        flow_bin, temp_bin, dummy = self.__split_binary(binary_number)

        flow_decimal = self.__binary_to_decimal(flow_bin)
        temp_decimal = self.__binary_to_decimal(temp_bin)

        flow_converted = flow_decimal*0.016 + 0      # L/min
        temp_converted = temp_decimal*0.1 + 0        # C

        return flow_converted, temp_converted


    #################################### PRIVATE METHODS ####################################

    def __hex_to_binary(self, hex_str):
        hexInt = int(hex_str, 16)
        # print(hexInt)
        # convert the hexInt to binaryInt. 
        binary_number = bin(hexInt)
        # print(binary_number)
        binary_number = binary_number[2:].zfill(48)
        # print(binary_number)
        return binary_number

    def __split_binary(self, binary_number):
        flow_bin = binary_number[:16]
        temp_bin = binary_number[16:32]
        dummy = binary_number[32:]
        return flow_bin, temp_bin, dummy

    def __binary_to_decimal(self, binary_number):
        decimal_number = int(binary_number, 2)
        return decimal_number