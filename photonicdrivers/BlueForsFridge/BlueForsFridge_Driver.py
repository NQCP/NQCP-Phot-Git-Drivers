from typing import Any, Literal
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
        return bool(int(value))
    if typ == "Value.Number.Integer.Enumeration.onOffError":
        return OnOffError(int(value))
    
    raise ValueError(f"No conversion for {typ} exists")

def strip_prefix(s: str):
    return s.split('.')[-1]


def filter_type(data: dict, filter_types: list[type] | None = None):
    return {k: v for k, v in data.items() if filter_types is None or type(v) in filter_types}

class BlueForsFridge_Driver(Connectable):
    """Driver for interacting with the BlueFors Control Software application programmatically"""
    _FORBIDDEN_VALVES = {"v15", "v17", "v18"}
    _NO_PROMPT_VALVES = {"v13"}
    _FSE_HEATER_NR = 4
    _FSE_HEATER_VALUES_PATH = "driver.bftc2.data.heaters.heater_4"

    def __init__(self, host="http://localhost", port=LAN_PORT):
        self.port = port
        self.url = f"{host}:{self.port}"
        self.session: requests.Session | None = None

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
        session = self.session
        if session is None:
            return
        try:
            session.get(self._request_url("system"), timeout=10 ** -9)
        except Exception:
            pass

    def disconnect(self):
        self.session = None

    def is_connected(self) -> bool:
        session = self.session
        if session is None:
            return False
        try:
            return session.get(self._request_url("system")).status_code == 200
        except Exception:
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

    def get_pid_settings(self) -> dict[str, Any]:
        """Return PID-related settings for the FSE heater only."""
        response = self.get_from_root(f"values/{self._FSE_HEATER_VALUES_PATH}")
        data = response.get("data", response)

        if not isinstance(data, dict):
            return {}

        def extract_value(value_suffix: str) -> Any:
            expected_suffix = f".{value_suffix}"
            for key, node in data.items():
                if not isinstance(key, str) or not key.endswith(expected_suffix):
                    continue
                if not isinstance(node, dict):
                    continue
                content = node.get("content")
                if not isinstance(content, dict):
                    continue
                latest_value = content.get("latest_value")
                if not isinstance(latest_value, dict):
                    continue
                value = latest_value.get("value")
                if value in (None, ""):
                    return None
                typ = node.get("type")
                if not isinstance(typ, str):
                    return value
                return convert_to_python_type(value, typ)
            return None

        return {
            "active": extract_value("active"),
            "pid_mode": extract_value("pid_mode"),
            "setpoint": extract_value("setpoint"),
            "control_algorithm": extract_value("control_algorithm"),
            "control_algorithm_settings": {
                "proportional": extract_value("control_algorithm_settings.proportional"),
                "integral": extract_value("control_algorithm_settings.integral"),
                "derivative": extract_value("control_algorithm_settings.derivative"),
            },
            "max_power": extract_value("max_power"),
            "power": extract_value("power"),
            "resistance": extract_value("resistance"),
            "target_temperature": extract_value("target_temperature"),
        }
    
    def set_heater(self, heater_name: Literal['hs-still', 'hs-mc', 'ext', 'heater'], state: bool):
        payload = {"data": {f"mapper.bf.heaters.{heater_name}": {"content": {"value": int(state)}}}}
        response = self._post_values(payload)
        return response

    def set_valve(self, valve_name: str, state: bool):
        normalized_name = self._normalize_valve_name(valve_name)

        if normalized_name in self._FORBIDDEN_VALVES:
            raise ValueError(f"Valve {normalized_name} is forbidden and cannot be controlled via this API driver")

        if normalized_name not in self._NO_PROMPT_VALVES:
            input_answer = input(f"Valve {normalized_name} is not one of the commonly used valves. Are you sure you want to set it? (y/n)")
            if input_answer.lower() != 'y':
                print("Aborting valve control.")
                raise ValueError(f"Aborting control of valve {normalized_name} as per user request.")

        payload = {"data": {f"mapper.bf.valves.{normalized_name}": {"content": {"value": int(state)}}}}
        response = self._post_values(payload)
        return response

    def set_pump(self, pump_name: Literal['scroll1', 'scroll2', 'turbo1', 'turbo2', 'compressor'], state: bool):
        payload = {"data": {f"mapper.bf.pumps.{pump_name}": {"content": {"value": int(state)}}}}
        response = self._post_values(payload)
        return response

    def _normalize_valve_name(self, valve_name: str) -> str:
        normalized_name = valve_name.strip().lower()
        if not normalized_name.startswith("v"):
            raise ValueError(f"Valve name must be of form v<number>, got {valve_name!r}")

        valve_number_str = normalized_name[1:]
        if not valve_number_str.isdigit():
            raise ValueError(f"Valve name must be of form v<number>, got {valve_name!r}")

        valve_number = int(valve_number_str)
        if valve_number < 1 or valve_number > 23:
            raise ValueError(f"Valve number must be in [1, 23], got {valve_number}")

        return f"v{valve_number}"

    def configure_fse_temperature_pid_loop(
        self,
        setpoint: float,
        proportional: float,
        integral: float,
        derivative: float,
        *,
        max_power: float | None = None,
        resistance: float | None = None,
        active: bool = False,
    ) -> dict[str, Any]:
        """Configure PID control parameters for the FSE heater only."""
        payload: dict[str, Any] = {
            "pid_mode": 1,
            "control_algorithm": 1,
            "setpoint": setpoint,
            "control_algorithm_settings.proportional": proportional,
            "control_algorithm_settings.integral": integral,
            "control_algorithm_settings.derivative": derivative,
            "active": active,
        }
        if max_power is not None:
            payload["max_power"] = max_power
        if resistance is not None:
            payload["resistance"] = resistance

        return self._post_fse_heater_values(payload)

    def enable_fse_temperature_pid_loop(self) -> dict[str, Any]:
        """Enable PID mode on the FSE heater using the existing PID configuration."""
        payload = {
            "pid_mode": 1,
            "active": True,
        }
        return self._post_fse_heater_values(payload)

    def disable_fse_temperature_pid_loop(self, keep_heater_active: bool = False) -> dict[str, Any]:
        """Disable PID mode for the FSE heater only."""
        payload = {
            "pid_mode": 0,
            "active": keep_heater_active,
        }
        return self._post_fse_heater_values(payload)

    def _post_fse_heater_values(self, updates: dict[str, Any]) -> dict[str, Any]:
        data = {
            f"{self._FSE_HEATER_VALUES_PATH}.{key}": {"content": {"value": value}}
            for key, value in updates.items()
        }
        return self._post_values({"data": data})
    
    def _post_values(self, payload:dict) -> dict:
        self._validate_values_write_payload(payload)
        if self.session is None:
            raise RuntimeError("Driver is not connected. Call connect() before API calls.")
        response = self.session.post("http://localhost:49099/values/?prettyprint=1&fields=name;value;status", json=payload)
        return response.json()

    def _validate_values_write_payload(self, payload: dict[str, Any]) -> None:
        data = payload.get("data")
        if not isinstance(data, dict):
            return

        forbidden_targets = {f"mapper.bf.valves.{name}" for name in self._FORBIDDEN_VALVES}
        for target in data:
            if isinstance(target, str) and target.strip().lower() in forbidden_targets:
                raise ValueError(f"Target {target} is forbidden and cannot be controlled via this API driver")

    def _post(self, endpoint: str, payload: dict[str, Any]) -> dict[str, Any]:
        if self.session is None:
            raise RuntimeError("Driver is not connected. Call connect() before API calls.")
        response = self.session.post(self._request_url(endpoint), json=payload)
        return response.json()

    def _get(self, endpoint: str, query=None) -> dict:
        if self.session is None:
            raise RuntimeError("Driver is not connected. Call connect() before API calls.")
        response = self.session.get(self._request_url(endpoint), params=query)
        return response.json()

    def _request_url(self, endpoint: str) -> str:
        return f"{self.url}/{endpoint}"
