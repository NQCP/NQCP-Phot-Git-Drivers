from typing import Literal
from photonicdrivers.Abstract.Connectable import Connectable
import requests
from enum import Enum
# Lan port is only open to the computer running the control software. 
# If enabled in the control software, access remotely via port 49098 
LAN_PORT = 49099

class OnOffError(Enum):
    Off = 0
    On = 1
    Error = 2

def flatten_value_nodes(values_dict: dict[str, dict]):
    flattened_values = {}
    for (k, v) in values_dict.items():
        dict_key = strip_prefix(k)
        if dict_key in flattened_values:
            raise Exception(f"dict key {dict_key} already found in flattened value nodes")
        if "content" in v:
            latest_value = v["content"]["latest_value"]
            # Value not present
            if latest_value is None or latest_value["value"] is None or latest_value["value"] == "":
                value = None
            else:
                value = convert_to_python_type(latest_value["value"], v["type"])
            flattened_values[dict_key] = value
    return flattened_values

def convert_to_python_type(value: str, typ: str):
    if value == "":
        raise ValueError(f"Attempting conversion of empty string is not allowed (Expected value of type {typ})")

    if "Value.Number.Float" in typ:
        return float(value)
    if typ == "Value.Number.Integer.Enumeration.yesNo" or typ == "Value.Number.Integer.Enumeration.Boolean":
        return bool(value)
    if typ == "Value.Number.Integer.Enumeration.onOffError":
        return OnOffError(int(value))
    
    raise ValueError(f"No conversion for {typ} exists")

def strip_prefix(s: str):
    return s.split('.')[-1]


def filter_type(data: dict, filter_types: list[type] | None = None):
    return {k: v for k, v in data.items() if filter_types is None or type(v) in filter_types}

class BlueForsFridge_Driver(Connectable):
    """Driver for interacting with the BlueFors Control Software application programmatically"""
    def __init__(self, host="http://localhost", port=LAN_PORT):
        self.port = port
        self.url = f"{host}:{self.port}"
        self.session = None

    def connect(self, jumpstart=True):
        self.session = requests.Session()
        if jumpstart:
            self._jumpstart_connection()
    
    def _jumpstart_connection(self):
        # The timeout is a simple hack. The first request attempt in the HTTP session seems to always fail
        # (and then successfully retries). Subsequent requests in the same session will not be delayed.
        # If you happen to know a more elegant and simple way to avoid this issue with the TCP connection, please fix!
        # When trying in a browser, the first request is usually 300 ms compared to single digits afterwards.
        # The 10^-9 value is completely arbitrary.
        try:
            self.session.get(self._request_url("system"), timeout=10 ** -9)
        except:
            pass

    def disconnect(self):
        self.session = None

    def is_connected(self) -> bool:
        try:
            return self.session.get(self._request_url("system")).status_code == 200
        except:
            return False

    def get_from_root(self, path: str, query=None) -> dict:
        """Extract information directly from the API"""
        return self._get(path, query)

    def get_values(self, metric_path: str | None, query=None, flatten:bool=True) -> dict:
        """Return metric(s) of interest from the control software"""
        path = "values/mapper/bf"
        if metric_path is not None:
            path += f"/{metric_path}"

        # Every node in the value tree is a dictionary itself
        data: dict = self.get_from_root(path, query)["data"]

        return flatten_value_nodes(data) if flatten else data

    ### Convenience methods that return normalized data ###
    def get_temperatures(self) -> dict[str, float]:
        node_values = self.get_values("temperatures")
        return filter_type(node_values, [float])
    
    def get_pressures(self) -> dict[str, float]:
        node_values = self.get_values("pressures")
        return filter_type(node_values, [float])
    
    def get_valves(self) -> dict[str, OnOffError]:
        node_values = self.get_values("valves")
        return filter_type(node_values, [OnOffError])
    
    def get_pumps(self) -> dict[str, OnOffError]:
        node_values = self.get_values("pumps")
        return filter_type(node_values, [OnOffError])

    def get_heaters(self) -> dict[str, OnOffError]:
        node_values = self.get_values("heaters")
        return filter_type(node_values, [OnOffError])
    
    def set_heater(self, heater_name: Literal['hs-still', 'hs-mc', 'ext', 'heater'], state: bool):
        payload = {"data": {f"mapper.bf.heaters.{heater_name}": {"content": {"value": int(state)}}}}
        response = self._post_values(payload)
        return response
    
    def set_hs_still_heater(self, state: bool):
        return self.set_heater("hs-still", state)

    def set_hs_mc_heater(self, state: bool):
        return self.set_heater("hs-mc", state)

    def set_ext_heater(self, state: bool):
        return self.set_heater("ext", state)

    def set_4k_heater(self, state: bool):
        return self.set_heater("heater", state)

    def set_all_heaters(self, state: bool):
        payload = {
            "data": {
                "mapper.bf.heaters.hs-still": {"content": {"value": int(state)}},
                "mapper.bf.heaters.hs-mc": {"content": {"value": int(state)}},
                "mapper.bf.heaters.ext": {"content": {"value": int(state)}},
                "mapper.bf.heaters.heater": {"content": {"value": int(state)}},
            }
        }

        return self._post_values(payload)
    
    def _post_values(self, payload:dict) -> dict:
        response = self.session.post("http://localhost:49099/values/?prettyprint=1&fields=name;value;status", json=payload)
        return response.json()

    def _get(self, endpoint: str, query=None) -> dict:
        response = self.session.get(self._request_url(endpoint), params=query)
        return response.json()

    def _request_url(self, endpoint: str) -> str:
        return f"{self.url}/{endpoint}"
