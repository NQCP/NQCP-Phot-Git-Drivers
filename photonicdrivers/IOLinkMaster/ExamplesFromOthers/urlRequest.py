import requests
import warnings
from bitstring import BitArray
# 



SD0548_flavor = ('SD0542', 'SD0548', 'SDG350', 'SDG450', 'SDG550', 'SDG750', 'SDG850')
SD0541_flavor = ('SD0541')
SD0547_flavor = ('SD0547')

SD054x_ARRAY = {
        'SD0541': 'float:32, int:16, int:8, int:8, int:16, int:8, int:4, int:2, bool, bool',
        'SD0542': 'float:32, int:16, int:8, int:8, int:16, int:8, int:8, int:16, int:8, int:4, int:2,  bool, bool',
        'SD0547': 'float:32, int:32, int:8, int:8, int:16, int:8, int:4, int:2, bool, bool',
        'SD0548': 'float:32, int:16, int:8, int:8, int:16, int:8, int:8, int:16, int:8, int:4, int:2,  bool, bool',
        }

FLOW_EXP = {
        'STA-Di2-008': -2,
        'MA-Di2-015': -2,
        'MA-Di2-020': -1,
        'MA-Di2-025': -1,
        'MA-Di2-032': -1,
        'MA-Di2-040': -1,
        'MA-Di2-050': -1,
        'STA-Di2-050': 0,
        'STA-Di2-065': 0,
        'STA-Di2-080': 0,
        'STA-Di2-100': 0,
        'STA-Di2-125': 0,
        'STA-Di2-150': 1,
        'STA-Di2-200': 1,
        'STA-Di2-250': 1,
        'RO-Ri2-040': -1,
        'RO-Ri2-050': 0,
        'RO-Ri2-065': 0,
        'RO-Ri2-080': 0,
        'RO-Ri2-100': 0,
        'RO-Ri2-125': 0,
        'RO-Ri2-150': 1,
        'RO-Ri2-200': 1,
        'RO-Ri2-250': 1,
        'RO-Ri2-300': 1,
        'RO-Ri2-450': 1,
        }

def getdata_from_iolinkmaster(
        datapath,
        ipadr,
        port,
        ):
    url = f"http://{ipadr}/iolinkmaster/port[{port}]/{datapath}/getdata"
    print(url)
    response = requests.get(url).json()
    print(response)
    if response['code'] != 200:
        raise ConnectionError(f"IoT-Core diagnostic code {response['code']}")
    return response

def decode_processdata(
        processdata_hex,
        sdtype,
        flow_exp=None,
        debug=False
        ):
    # return None
    if sdtype in SD0548_flavor:
        processdata_unpacked = BitArray(hex=processdata_hex).unpack(SD054x_ARRAY['SD0548'])
        processdata = {
                'TOTALISATOR': processdata_unpacked[0],
                'TEMPERATURE': processdata_unpacked[4] * 10**processdata_unpacked[5],
                'PRESSURE': processdata_unpacked[7] * 10**processdata_unpacked[8],
                'DEVICESTATUS': processdata_unpacked[9],
                'OUT2': processdata_unpacked[11],
                'OUT1': processdata_unpacked[12],
                }
    elif sdtype in SD0541_flavor:
        processdata_unpacked = BitArray(hex=processdata_hex).unpack(SD054x_ARRAY['SD0541'])
        processdata = {
                'TOTALISATOR': processdata_unpacked[0],
                'TEMPERATURE': processdata_unpacked[4] * 10**processdata_unpacked[5],
                'DEVICESTATUS': processdata_unpacked[6],
                'OUT2': processdata_unpacked[8],
                'OUT1': processdata_unpacked[9],
                }
    elif sdtype in SD0547_flavor:
        processdata_unpacked = BitArray(hex=processdata_hex).unpack(SD054x_ARRAY['SD0547'])
        processdata = {
                'TOTALISATOR': processdata_unpacked[0],
                'TEMPERATURE': processdata_unpacked[4] * 10**processdata_unpacked[5],
                'DEVICESTATUS': processdata_unpacked[6],
                'OUT2': processdata_unpacked[8],
                'OUT1': processdata_unpacked[9],
                }
    if flow_exp is not None:
        processdata['FLOW'] = processdata_unpacked[1] * 10**flow_exp
    else:
        processdata['FLOW'] = processdata_unpacked[1] * 10**processdata_unpacked[2]
    if debug:
        return processdata, processdata_unpacked, processdata_hex
    else:
        return processdata

class PBCo_IOLink_SDSensor():

    def __init__(self,
                 ipadr,
                 port,
                 ):
        self.ipadr = ipadr
        self.port = port
        applicationtag_query = getdata_from_iolinkmaster('iolinkdevice/pdin', ipadr, port) 
        print(applicationtag_query)
        self.product = applicationtag_query['data']['value']
        print(self.product)
        # if self.product not in FLOW_EXP:
        #     warnings.warn(f"Device {self.product} is not a valid PBCo SD-sensor.")
        # self.__flow_exp = FLOW_EXP.get(self.product, None)
        self.__sdtype = getdata_from_iolinkmaster('iolinkdevice/productname', ipadr, port)['data']['value']

    def get_process_data(self):
        process_data = getdata_from_iolinkmaster('iolinkdevice/pdin', self.ipadr, self.port) 
        return decode_processdata(
                process_data['data']['value'],
                self.__sdtype,
                self.__flow_exp
                )