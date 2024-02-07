import json

class FlowMeterPF3W720:
    def __init__(self):
        print("init")

    def pdin(self, pinNumber):
        # Create the JSON command
        strCommand = {
            "code": "request",
            "cid": 1,
            "adr": "/iolinkmaster/port[" + pinNumber + "]/iolinkdevice/iolreadacyclic",
            "data": 0,
            "subindex": 0
        }
        jsonCommand = json.dumps(strCommand)
        return jsonCommand