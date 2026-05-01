import sys
sys.path.append(r'C:\gitRepositories\pyrpl')
import pyrpl

class Red_Pitaya_Driver:
    def __init__(self, config: str = 'default'):
        self.config = config
        self.device = None

    def get_id(self) -> str:
        if self.device:
            return "Red Pitaya (pyrpl)"
        return "Not connected"

    def connect(self):
        self.device = pyrpl.RedPitaya(config=self.config)

    def disconnect(self):
        if self.device:
            del self.device
            self.device = None

    def is_connected(self) -> bool:
        return self.device is not None
