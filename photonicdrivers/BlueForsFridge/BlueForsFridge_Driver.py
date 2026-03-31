from typing import Any, Literal
from photonicdrivers.Abstract.Connectable import Connectable
import requests
from enum import Enum
# Lan port is only open to the computer running the control software.
# If enabled in the control software, access remotely via port 49098
LAN_PORT = 49099
TC_PORT = 5001

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
    if "Value.Number.Integer" in typ:
        return int(value)
    
    raise ValueError(f"No conversion for {typ} exists")

def strip_prefix(s: str):
    return s.split('.')[-1]


def filter_type(data: dict, filter_types: list[type] | None = None):
    return {k: v for k, v in data.items() if filter_types is None or type(v) in filter_types}

class BlueForsFridge_Driver(Connectable):
    """Driver for interacting with the BlueFors Control Software application programmatically"""
    _FORBIDDEN_VALVES = {"v15", "v17", "v18"}
    _NO_PROMPT_VALVES = {"v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", "v11", "v12", "v13"}
    _FSE_HEATER_NR = 4

    def __init__(self, host="http://localhost", port=LAN_PORT, tc_host: str | None = None, tc_port: int = TC_PORT):
        self.port = port
        self.url = f"{host}:{self.port}"
        self.session: requests.Session | None = None
        self.tc_url: str | None = f"{tc_host}:{tc_port}" if tc_host is not None else None
        self.tc_session: requests.Session | None = None

    def connect(self, jumpstart=True):
        self.session = requests.Session()
        if jumpstart:
            self._jumpstart_connection()
        if self.tc_url is not None:
            self.tc_session = requests.Session()
    
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
        self.tc_session = None

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
    
    def get_pumps(self) -> dict[str, OnOffError | float | int | None]:
        node_values = self.get_values("pumps")
        pumps = filter_type(node_values, [OnOffError, float, int])
        
        # Attempt to get turbo pump speeds from legacy wrapper
        try:
            legacy_data = self.get_from_root("values/mapper/bflegacy/double")["data"]
            legacy_values = flatten_value_nodes(legacy_data)
            
            # Map tc400 speeds to their turbo counterparts
            if "tc400actualspd" in legacy_values and legacy_values["tc400actualspd"] is not None:
                pumps["turbo1_speed"] = legacy_values["tc400actualspd"]
            if "tc400actualspd_2" in legacy_values and legacy_values["tc400actualspd_2"] is not None:
                pumps["turbo2_speed"] = legacy_values["tc400actualspd_2"]
            if "tc400actualspd_3" in legacy_values and legacy_values["tc400actualspd_3"] is not None:
                pumps["turbo3_speed"] = legacy_values["tc400actualspd_3"]
            if "tc400actualspd_4" in legacy_values and legacy_values["tc400actualspd_4"] is not None:
                pumps["turbo4_speed"] = legacy_values["tc400actualspd_4"]
        except Exception:
            pass # Failsafe in case bflegacy gets removed
            
        return pumps

    def get_heaters(self) -> dict[str, OnOffError]:
        node_values = self.get_values("heaters")
        return filter_type(node_values, [OnOffError])

    def get_pid_settings(self) -> dict[str, Any]:
        """Return PID-related settings for the FSE heater from the TC API."""
        return self._tc_post("heater", {"heater_nr": self._FSE_HEATER_NR})
    
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
        """Configure PID control parameters for the FSE heater via the TC API."""
        payload: dict[str, Any] = {
            "heater_nr": self._FSE_HEATER_NR,
            "pid_mode": 1,
            "control_algorithm": 1,
            "setpoint": setpoint,
            "control_algorithm_settings": {
                "proportional": proportional,
                "integral": integral,
                "derivative": derivative,
            },
            "active": active,
        }
        if max_power is not None:
            payload["max_power"] = max_power
        if resistance is not None:
            payload["resistance"] = resistance

        return self._tc_post("heater/update", payload)

    def enable_fse_temperature_pid_loop(self) -> dict[str, Any]:
        """Enable PID mode on the FSE heater."""
        return self._tc_post("heater/update", {
            "heater_nr": self._FSE_HEATER_NR,
            "pid_mode": 1,
            "active": True,
        })

    def disable_fse_temperature_pid_loop(self, keep_heater_active: bool = False) -> dict[str, Any]:
        """Disable PID mode for the FSE heater."""
        return self._tc_post("heater/update", {
            "heater_nr": self._FSE_HEATER_NR,
            "pid_mode": 0,
            "active": keep_heater_active,
        })

    def _tc_get(self, endpoint: str) -> dict[str, Any]:
        """HTTP GET to the Temperature Controller API."""
        if self.tc_session is None:
            raise RuntimeError("Temperature controller not connected. Provide tc_host and call connect().")
        response = self.tc_session.get(f"{self.tc_url}/{endpoint}")
        response.raise_for_status()
        result = response.json()
        if result.get("status") == "ERROR":
            raise RuntimeError(f"TC API error: {result.get('error', {}).get('message', result)}")
        return result

    def _tc_post(self, endpoint: str, payload: dict[str, Any]) -> dict[str, Any]:
        """HTTP POST to the Temperature Controller API."""
        if self.tc_session is None:
            raise RuntimeError("Temperature controller not connected. Provide tc_host and call connect().")
        response = self.tc_session.post(f"{self.tc_url}/{endpoint}", json=payload)
        response.raise_for_status()
        result = response.json()
        if result.get("status") == "ERROR":
            raise RuntimeError(f"TC API error: {result.get('error', {}).get('message', result)}")
        return result

    def _post_values(self, payload: dict, must_exist: bool = False) -> dict:
        self._validate_values_write_payload(payload)
        if self.session is None:
            raise RuntimeError("Driver is not connected. Call connect() before API calls.")
        url = f"{self.url}/values/?prettyprint=1&fields=name;value;status"
        if must_exist:
            url += "&must_exist=1"
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        out = response.json()
        if "error" in out:
            raise RuntimeError(f"API returned an error: {out['error']}")
        return out

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
