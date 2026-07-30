from photonicdrivers.SNSPDs.FilesFromManufacturer.WebSQController_Retina import WebSQController
from photonicdrivers.Abstract.Connectable import Connectable

class SNSPD_02_SQ_Driver(Connectable):
    def __init__(self, ip_address: str) -> None:
        self.ip_address = f"http://{ip_address}"
        self.websq_retina = WebSQController(self.ip_address)
        self.connected:bool = False

    def connect(self) -> None:
        if not self.connected:
            try: 
                self.get_settings()
                self.connected = True
                print("Successfully connected to WebSQController at " + self.ip_address)
            except Exception as error:
                print(f"Failed to connect. Error: {error}")
                self.connected = False

    def disconnect(self) -> None:
        self.connected = False

    def is_connected(self) -> bool:
        return self.connected       
     
    def get_ip_address(self) -> str:
        return self.ip_address    
    
    def get_temperature_stage_1(self) -> float:
        # This function returns the latest temperature for stage 1. See the WebSQController_Retina.py script from the manufacturer        
        latest_temperature = self.websq_retina.getTemperatures()
        return latest_temperature[1]
    
    def get_temperature_stage_2(self) -> float:
        # This function returns the latest temperature for stage 2. See the WebSQController_Retina.py script from the manufacturer        
        latest_temperature = self.websq_retina.getTemperatures()
        return latest_temperature[0]
    
    def get_temperature_unit(self) -> str:
        return "K"
    
    def set_integration_time(self, integration_time_ms:int) -> None:
        #intTime in (ms) should be in steps of 10ms.
        self.websq_retina.setIntTime(integration_time_ms)

    def get_integration_time(self) -> float:
        return self.websq_retina.getIntTime()
 
    def get_bias_currents(self) -> list:
        return self.websq_retina.getBiasI()
    
    def set_bias_currents(self) -> list:
        return self.websq_retina.setBiasI()
    
    def get_settings(self) -> dict:
        return self.websq_retina.getSettings()
    
