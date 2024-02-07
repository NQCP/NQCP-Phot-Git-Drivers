from IOLinkMaster import IOLinkMaster

IOLink = IOLinkMaster('10.209.xx.xx',0)
IOLink.getFlowAndTemp()
IOLink.closeConnection()


def hex_to_binary(hexStr):
    hexInt = int(hexStr, 16)
    print(hexInt)
    # convert the hexInt to binaryInt. 
    binary_number = bin(hexInt)
    print(binary_number)
    binary_number = binary_number[2:].zfill(48)
    print(binary_number)
    return binary_number

def split_binary(binary_number):
    flow_bin = binary_number[:16]
    temp_bin = binary_number[16:32]
    dummy = binary_number[32:]
    return flow_bin, temp_bin, dummy

def binary_to_decimal(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number

# Example usage
hex_number = "000000E00002"

binary_number = hex_to_binary(hex_number)
flow_bin, temp_bin, dummy = split_binary(binary_number)

flow_decimal = binary_to_decimal(flow_bin)
temp_decimal = binary_to_decimal(temp_bin)

print("Original Hex:", hex_number)
print("Binary:", binary_number)
print("flowBin:", flow_bin, "TempBin:", temp_bin, "Dummy:", dummy)
print("Decimal flowBin:", flow_decimal)
print("Decimal tempBin:", temp_decimal)