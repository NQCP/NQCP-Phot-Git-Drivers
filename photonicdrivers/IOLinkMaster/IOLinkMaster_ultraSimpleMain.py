
import requests

ipadr='10.209.67.95'
inputPort=1
datapath = 'iolinkdevice/pdin'

url = f"http://{ipadr}/iolinkmaster/port[{inputPort}]/{datapath}/getdata"
print(url)
response = requests.get(url).json()
print(response)
print(response["data"]['value'])
hex_number = response["data"]['value']

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


binary_number = hex_to_binary(hex_number)
flow_bin, temp_bin, dummy = split_binary(binary_number)

flow_decimal = binary_to_decimal(flow_bin)
temp_decimal = binary_to_decimal(temp_bin)

print("Original Hex:", hex_number)
print("Binary:", binary_number)
print("flowBin:", flow_bin, "TempBin:", temp_bin, "Dummy:", dummy)
print("Decimal flowBin:", flow_decimal)
print("Decimal tempBin:", temp_decimal)

print(str(float(flow_decimal*0.016 + 0)) + " L/min")
print(str(float(temp_decimal*0.1 + 0)) + " C")
