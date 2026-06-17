from photonicdrivers.SNSPDs.FilesFromManufacturer.WebSQController import WebSQController
from photonicdrivers.Abstract.Connectable import Connectable


class SNSPD_02_SQ_Driver(Connectable):
    def __init__(self,_ip_string: str) -> None:
        self.ip_address = _ip_string
        self.websq_retina = WebSQController(self.ip_address)

    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    def is_connected(self) -> bool:
        status = False
        try: 
            settings = self.websq_retina.reloadSettings() 
            if settings is not None:
                status = True
        except: 
                status = False
        return status       
     
    def get_ip_address(self) -> str:
        return self.ip_address    
    
    def get_temperature_stage_1(self) -> float:
        # This function returns the latest temperature for stage 1. See the WebSQController.py script from the manufacturer        
        latest_temperature = self.websq_retina.getTemperatures()
        return latest_temperature[1]
    
    def get_temperature_stage_2(self) -> float:
        # This function returns the latest temperature for stage 2. See the WebSQController.py script from the manufacturer        
        latest_temperature = self.websq_retina.getTemperatures()
        return latest_temperature[0]
    
    def set_integration_time(self, integration_time_ms:int) -> None:
        #intTime in (ms) should be in steps of 10ms.
        self.websq_retina.setIntTime(integration_time_ms)

    def get_integration_time(self) -> float:
        return self.websq_retina.getIntTime()
 
    def get_bias_currents(self) -> list:
        return self.websq_retina.getBiasI()
    
    def set_bias_currents(self) -> list:
        return self.websq_retina.setBiasI()
    