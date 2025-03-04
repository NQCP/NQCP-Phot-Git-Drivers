import requests
from photonicdrivers.Abstract.Connectable import Connectable
from photonicdrivers.IOLinkMaster.FlowMeterPF3W720_Driver import FlowMeterPF3W720_Driver

class IOLinkMaster_Driver(Connectable):
    def __init__(self, IPAddress):
        self.ip = IPAddress
        print("Initalising an IO master")
        self.flowMeter = FlowMeterPF3W720_Driver()

    def getFlowAndTemp(self, pinNumber):
        url_ending = self.flowMeter.getUrl_pdin_getData(pinNumber)
        response_raw = self.__query(url_ending)
        data_hex = response_raw["data"]['value']
        response = self.flowMeter.convert_pdinData(data_hex)
        return response
    
    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    """CHECK IF THE RESPONSE CODE IS 200!!!"""
    def is_connected(self):
        try:
            return requests.get(self.__base_url(), timeout=2).status_code == 200
        except:
            return False
    ##################### PRIVATE METHODS ###########################

    def __query(self, url_ending):
        url = self.__base_url() + {url_ending}
        return requests.get(url).json()
    
    def __base_url(self) -> str:
        return f"http://{self.ip}/iolinkmaster"
