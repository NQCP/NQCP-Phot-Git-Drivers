import requests
# from FlowMeterPF3W720 import FlowMeterPF3W720
from photonicdrivers.IOLinkMaster.FlowMeterPF3W720_Driver import FlowMeterPF3W720_Driver

class IOLinkMaster_Driver:
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

    ##################### PRIVATE METHODS ###########################

    def __query(self, url_ending):
        url = f"http://{self.ip}/iolinkmaster{url_ending}"
        return requests.get(url).json()