# Temperature Controller API
**Technical Reference**
BF1000-1234517327-58 | Version 2.0, en-US | August 28, 2024

> **CONFIDENTIAL** — © 2024 Bluefors Oy. "Bluefors" and "Cool for Progress" are registered trademarks of Bluefors Oy. All rights reserved and unauthorized use prohibited.

---

## Disclaimer

The information contained in this document is effective as of the publication date. Bluefors Oy reserves the right to make changes to the product and information contained in this document relative to the specifications, features, and design of the product.

Contact us directly at support@bluefors.com if you have any questions about the specifications or any other content contained in this document.

**Contact information:**
Bluefors Oy, Arinatie 10, 00370 Helsinki, Finland
support@bluefors.com | +358 9 5617 4800

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [API Description](#2-api-description)
3. [API Reference](#3-api-reference)
4. [Examples](#4-examples)

---

## 1 Introduction

### 1.1 Overview of the User Instructions

This information applies to Bluefors Temperature Controller.

| Document | Description |
|---|---|
| User Manual | Functional description of the product, component descriptions, and operating, maintenance, and troubleshooting instructions. |
| Technical Reference | Necessary background information and technical details about a subject, such as parameter descriptions and use of scripts and API. |

### 1.2 Related Information

| Information | ID | Location |
|---|---|---|
| Bluefors Temperature Controller User Manual | BF1000-1234517327-60 | https://bluefors.com/support |

### 1.3 Terms and Abbreviations

| Term / Abbreviation | Definition |
|---|---|
| API | application programming interface |
| LAN | local area network |
| URL | unified resource locator |

### 1.4 Symbols and Conventions

> **NOTE** — A note is used to indicate additional important information to the reader.

### 1.5 Customer Service and Support

For support documents and downloadable software: https://bluefors.com/support

For technical issues: support@bluefors.com or +358 9 5617 4800

For sales-related issues: sales@bluefors.com or +358 9 5617 4800

> **NOTE** — In case of emergency or accidents, call your local emergency services.

### 1.6 Warranty

For warranty information, refer to the Bluefors warranty statement.

---

## 2 API Description

### 2.1 General Information

This document describes the application programming interface for Bluefors Temperature Controller. The API is the interface for programs to access and control the device. Any programming language that supports REST API (HTTP GET/POST), WebSocket, or MQTT can be used.

### 2.2 Endpoint Format

The API uses endpoints to access data. General rules:

- **Format:** `element/sub-element/action`
- The `settings` element is default and not written in the endpoints.
- The `read` action is default and not written in the endpoints.
- There are no IDs in endpoints.

**Main elements:**
- `system`
- `statemachine`
- `channels` and `channel`
- `heaters` and `heater`
- `calibration-curves` and `calibration-curve`

**Endpoint construction examples:**

| Goal | Endpoint |
|---|---|
| Reading `/system` settings | `/system/settings/` |
| Subscribing to channel measurements | `/channel/measurements/subscribe` |
| Read every calibration curve with full data | `/calibration-curves/data/read` |

**Operation modes:**

| Mode | Description |
|---|---|
| Request-response | Single request → Single response with latest known data. Example: `/channel/measurement/latest` |
| Subscription | No request needed; subscription done automatically by connecting (WebSocket) or subscribing to topic (MQTT). Unlimited responses. Example: `/channel/measurement/listen` |

> **NOTE** — By default, the WebSocket and MQTT interfaces buffer unread responses to some limit defined by the interface itself, and the next receive attempt could return the last unread response from that buffer.

### 2.3 Protocols

#### 2.3.1 MQTT

- **Port:** 1883
- **Incoming messages topic:** `endpoint/in`
- **Outgoing messages topic:** `endpoint/out`
- **Modes:** request-response, subscription (same outgoing topic used for subscription)

#### 2.3.2 HTTP

- **Port:** 5001
- **Supported URL format:** `http://host:port/endpoint`
- **Unsupported formats:** trailing slash, path IDs (`/{id}`), query parameters (`?id={id}`)
- **Methods:** GET, POST
- **Mode:** request-response only

#### 2.3.3 WebSocket

- **Port:** 5002
- **URL formats:** same as HTTP
- **Modes:** request-response, subscription (subscription done automatically by connecting to the endpoint; requests not supported on subscription endpoints)

### 2.4 Message Payload

All message payloads are sent and received as JSON strings.

**Read all elements:** no payload
**Read one element:** payload with mandatory index fields
**Write one element:** payload with mandatory index fields and optional fields

#### 2.4.1 Common Fields

##### Request Parameters

| Key | Value type | Required | Comment |
|---|---|---|---|
| sender | string | No | Sender name, used to recognize the response |
| hash | string (0–50 chars) | No | Original message hash number, used to recognize the response |

> **NOTE** — Request parameters are not possible in HTTP GET.

**Example:**
```json
{
  "sender": "client-name-or-id",
  "hash": "this-is-just-hash-number-issued-by-client",
  "data1": "...",
  "dataN": "..."
}
```

##### Response Parameters

| Key | Value type | Required | Comment |
|---|---|---|---|
| sender | string | No | Same as in request |
| hash | string | No | Same as in request |
| datetime | datetime string | Yes | UTC format. Example: `"2024-01-31T13:04:43.060313Z"` |
| status | string | Yes | `"OK"` or `"ERROR"` |
| error | error object | No | Always sent if error |

##### Error Object Parameters

| Key | Value type | Required | Comment |
|---|---|---|---|
| code | integer ≥ 0 | Yes | Error code |
| message | string (max 2000 chars) | Yes | Error message |
| details | string (max 2000 chars) | No | Additional information |

**Example:**
```json
{
  "sender": "client-name-or-id",
  "hash": "this-is-just-hash-number-issued-by-client",
  "datetime": "2024-01-31T13:04:43.060313Z",
  "status": "ERROR",
  "error": {
    "code": 123,
    "message": "Wrong parameters provided.",
    "details": "Here are additional information as a string."
  }
}
```

#### 2.4.2 List of Error Codes

| Code | Type | Name | Description |
|---|---|---|---|
| 200 | Error | No data | Internal error: not getting data from the measurement hardware. |
| 241 | Error | Signal too noisy | Indication of high resistance. Examine the sensor connection. |
| 242 | Error | Overflow | Measurement is saturated. Indication of resistance being higher than the current excitation range. |
| 243 | Error | Common mode overflow | Measurements between preamplifier ground (cryostat) and temperature sensor lead are saturated. Indication of noisy grounding. |
| 244 | Error | Zero measured value | Internal error: device does not measure properly or there is a shorted circuit. |
| 245 | Error | Resistance too high | Resistance is above the maximum range. |
| 246 | Error | Resistance too low | Resistance is below the minimum range. |
| 247 | Error | Unreliable data | Measured signal arrives later than expected. |
| 511 | Warning | Temperature below range | Temperature is below the programmed impedance temperature curve. |
| 512 | Warning | Temperature above range | Temperature is above the programmed impedance temperature curve. |
| 514 | Warning | Temperature below calibration range | Temperature is below the calibration range. |
| 515 | Warning | Temperature above calibration range | Temperature is above the calibration range. |
| 518 | Warning | Temperature data unreliable | Calculated temperature is negative. |
| 519 | Warning | No calibration curve | Calibration curve has not been defined. |
| 521 | Warning | Resistance below range | Resistance is below the calibration range. |
| 522 | Warning | Resistance above range | Resistance is above the calibration range. |
| 901 | Notification | Vmax auto-ranging | Current excitation is tuned to set voltage to be the highest possible below the given value, Vmax. |

### 2.5 Tutorial

#### 2.5.1 Example: Access from Browser

Access the device at IP `10.0.0.135` by entering the URL in a browser:

```
http://10.0.0.135:5001/system/network
```

Example response:
```json
{"status": "OK", "state": "UP", "datetime": "2024-01-31T13:01:08.534671Z",
 "netmask": "255.255.0.0", "dns": "", "mac_address": "b8:27:eb:fd:a4:00",
 "ip_configuration": "DHCP", "ip_address": "10.0.0.135", "gateway": ""}
```

```
http://10.0.0.135:5001/channel/measurement/latest
```

Example response:
```json
{"rez": 10002.996333333334, "status": "OK", "angle": 89.59977777777777,
 "temperature": null, "timestamp": 1572353805.343614, "resistance": 10003.483555555556,
 "channel_nr": 6, "datetime": "2024-01-31T12:57:19.791712Z", "reactance": 1433539.4997777776,
 "magnitude": 10003.24, "status_flags": [511], "imz": 69.80922222222222}
```

> **NOTE** — Responses are different depending on the status of the device.

#### 2.5.2 Example: Using a HTTP Interface

```python
import json
import requests

req = requests.get('http://10.0.0.135:5001/channel/measurement/latest', timeout=10)
data = req.json()
print('Response: \n{}'.format(json.dumps(data, indent=2)))
```

Example response:
```json
{
  "rez": 10003.664111111111,
  "status": "OK",
  "angle": 89.6018888888889,
  "temperature": null,
  "timestamp": 1572355882.357602,
  "resistance": 10004.145555555557,
  "channel_nr": 6,
  "datetime": "2024-01-31T13:31:30.926461Z",
  "reactance": 1442043.1812222223,
  "magnitude": 10003.904888888888,
  "status_flags": [511],
  "imz": 69.40755555555556
}
```

#### 2.5.3 Example: Using a WebSocket Interface

Library: [websocket-client](https://pypi.org/project/websocket_client/)

```python
import json
import websocket

ws = websocket.create_connection(
    'ws://10.0.0.135:5002/channel/measurement/listen', timeout=10)
resp = ws.recv()
data = json.loads(resp)
print('Response: \n{}'.format(json.dumps(data, indent=2)))
```

#### 2.5.4 Example: Using a MQTT Interface

Library: [paho-mqtt](https://pypi.org/project/paho-mqtt/)

```python
import json
import paho.mqtt.subscribe as subscribe
from time import sleep

def callback_print(client, userdata, msg):
    data = json.loads(msg.payload)
    print('Message: \n{}'.format(json.dumps(data, indent=2)))

subscribe.callback(callback_print, 'channel/measurement/listen', hostname='10.0.0.135')

while True:
    sleep(1)
```

---

## 3 API Reference

### 3.1 System

**Endpoint: System Information**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/system` | `/system` | — | `/system` | `system/in` / `system/out` |

#### 3.1.1 Read Request
Empty.

#### 3.1.2 Response

| Key | Value type | Required | Comment |
|---|---|---|---|
| api_version | integer | Yes | API version. Allowed: `1` |
| type | string (0–50 chars) | Yes | System type. Allowed: `"Bluefors TC"` |
| serial | string (0–50 chars) | Yes | Device serial number |
| label | string (0–30 chars) | Yes | System label |
| addinfo | string (0–50 chars) | Yes | System additional information |
| software_version | string (0–50 chars) | Yes | Software version |

---

### 3.2 System / Device

**Endpoint: Device Information**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/system/device` | `/system/device` | — | `/system/device` | `system/device/in` / `system/device/out` |

#### 3.2.1 Read Request
Empty.

#### 3.2.2 Response

| Key | Value type | Required | Comment |
|---|---|---|---|
| device_id | string (0–32 chars) | Yes | Device ID |
| device_firmware | string (0–50 chars) | Yes | Device firmware version |

---

### 3.3 System / Network

Only IPv4 is supported.

**Endpoint: Network Settings**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/system/network` | `/system/network` | `/system/network` | `system/network/in` / `system/network/out` | |
| write | `/system/network/update` | — | `/system/network/update` | `/system/network/update` | `system/network/update/in` |
| subscription | `/system/network/listen` | — | — | `/system/network/listen` | `system/network/listen` |

#### 3.3.1 Read Request
Empty.

#### 3.3.2 Write Request

| Key | Value type | Required | Comment |
|---|---|---|---|
| ip_configuration | string | Yes | `"static"` or `"DHCP"` |
| ip_address | string | No | IPv4 address |
| netmask | string | No | IPv4 address |
| gateway | string | No | IPv4 address |
| dns | string | No | IPv4 address |

#### 3.3.3 Response

| Key | Value type | Required | Comment |
|---|---|---|---|
| *(same fields as write request)* | | | |
| state | string | Yes | `"UP"` or `"DOWN"` |
| mac_address | string | Yes | MAC address |

---

### 3.4 System / Reset

Only subscription is supported.

**Endpoint: System Reboot / Shutdown Notification**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| subscription | `/system/reset/listen` | — | — | `/system/reset/listen` | `system/reset/listen` |

#### 3.4.1 Response

| Key | Value type | Required | Comment |
|---|---|---|---|
| message | string | Yes | `"restart"` or `"shutdown"` |

---

### 3.5 System / Resources

Only subscription is supported.

**Endpoint: OS Resources**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| subscription | `/system/resources/listen` | — | — | `/system/resources/listen` | `system/resources/listen` |

#### 3.5.1 Response

| Key | Value type | Required | Comment |
|---|---|---|---|
| uptime | integer | Yes | Uptime in seconds |
| memory_free | integer | Yes | Free memory in KB |
| memory_used | integer | Yes | Used memory in KB |
| cpu_total | float | Yes | CPU usage total (percentage) |
| disk_usage_log | integer | Yes | Log disk usage (percentage) |
| disk_usage_data | integer | Yes | Data disk usage (percentage) |
| rtc_battery | float | Yes | RTC battery voltage |

---

### 3.6 Statemachine

**Endpoint: Measurement State Machine Settings**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/statemachine` | `/statemachine` | — | `/statemachine` | `statemachine/in` / `statemachine/out` |
| write | `/statemachine/update` | — | `/statemachine/update` | `/statemachine/update` | `statemachine/update/in` / `statemachine/update/out` |
| subscription | `/statemachine/listen` | — | — | `/statemachine/listen` | `statemachine/listen` |

#### 3.6.1 Read Request
Empty.

#### 3.6.2 Write Request

| Key | Value type | Required | Comment |
|---|---|---|---|
| wait_time | float: 1...100 | No | Default wait time after changing channel before using values for measurement result (seconds) |
| meas_time | float: 1...100 | No | Measurement time for measurement operation (seconds) |
| control_algorithm | integer: 0...100 | No | Next channel selection algorithm. `1`: round robin |

#### 3.6.3 Response

| Key | Value type | Required | Comment |
|---|---|---|---|
| *(same fields as write request)* | | | |
| state | string | Yes | Textual representation of statemachine status |
| measuring | boolean | Yes | Measurements status: ON or OFF |
| channel_nr | integer: 1...12 | Yes | Current or last used measurement channel |

---

### 3.7 Channels

**Endpoint: Channel Settings (Read Only)**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/channels` | `/channels` | — | `/channels` | `channels/in` / `channels/out` |

#### 3.7.1 Read Request
Empty.

#### 3.7.2 Response
Array of results for each channel. Each element uses the same response format as the single channel endpoint.

---

### 3.8 Channel

**Endpoint: Channel Settings (Read / Write)**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/channel` | — | `/channel` | `/channel` | `channel/in` / `channel/out` |
| write | `/channel/update` | — | `/channel/update` | `/channel/update` | `channel/update/in` / `channel/update/out` |
| subscription | `/channel/listen` | — | — | `/channel/listen` | `channel/listen` |

#### 3.8.1 Read Request

| Key | Value type | Required | Comment |
|---|---|---|---|
| channel_nr | integer: 1...12 | Yes | Channel number |

#### 3.8.2 Write Request

| Key | Value type | Required | Comment |
|---|---|---|---|
| channel_nr | integer | Yes | Channel number |
| active | boolean | No | Active status: ON or OFF |
| name | string | No | Channel name |
| excitation_mode | integer | No | `0`: current excitation, `1`: VMAX, `2`: CMN |
| excitation_current_range | integer | No | Settings number for current excitation mode: `1...22` |
| excitation_cmn_range | integer | No | CMN excitation current: `1` = 50 µA, `2` = 150 µA |
| excitation_vmax_range | integer | No | Max voltage in VMAX mode: `1` = 20 µV, `2` = 200 µV |
| use_non_default_timeconstants | boolean | No | `True`: use channel-specific wait and measurement times; `False`: use default |
| wait_time | float: 1...100 | No | Wait time after switching channel before measurement (seconds). Valid if `use_non_default_timeconstants == True` |
| meas_time | float: 1...100 | No | Measurement time for a single value (seconds). Valid if `use_non_default_timeconstants == True` |
| calib_curve_nr | integer: 1...100 | No | Calibration curve used by this channel |

#### 3.8.3 Response

| Key | Value type | Required | Comment |
|---|---|---|---|
| *(same fields as write request)* | | | |
| coupled_heater_nr | integer: 0...4 | Yes | Coupled heater: `1–4` = heater number, `0` = no heater. To change, see [Channel / Heater](#311-channel--heater) |

---

### 3.9 Channel / Historical-Data

**Endpoint: Channel Historical Data**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/channel/historical-data` | — | `/channel/historical-data` | `/channel/historical-data` | `channel/historical-data/in` / `channel/historical-data/out` |

#### 3.9.1 Read Request

| Key | Value type | Required | Comment |
|---|---|---|---|
| channel_nr | integer: 1...12 | Yes | Channel number |
| start_time | datetime string | Yes | Formats: `YYYY-MM-DD`, `YYYY-MM-DD HH:MM`, `YYYY-MM-DD HH:MM:SS`, `YYYY-MM-DDTHH:MM:SSZ` |
| stop_time | datetime string | Yes | Same formats as `start_time` |
| fields | array of strings | Yes | Available fields: `"temperature"`, `"resistance"`, `"reactance"`, `"rez"`, `"Imz"`, `"magnitude"`, `"angle"`, `"timestamp"`, `"status_flags"`, `"channel_nr"` |

#### 3.9.2 Response

| Key | Value type | Required | Comment |
|---|---|---|---|
| *(same fields as read request)* | | | |
| measurements | object with data arrays | Yes | Requested data; array element names match field names |
| over_limit | boolean | Yes | `True` if requested data exceeds 100,000 records (no data returned) |

**Example:**
```json
{
  "sender": "client-name-or-id",
  "hash": "this-is-just-hash-number-issued-by-client",
  "datetime": "2024-01-31T13:04:43.060313Z",
  "status": "OK",
  "channel_nr": 1,
  "over_limit": false,
  "fields": ["timestamp", "temperature"],
  "measurements": {
    "timestamp": [1542118174.989],
    "temperature": [0.034756]
  }
}
```

---

### 3.10 Channel / Measurement

**Endpoint: Latest Real-Time Measurement Data**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/channel/measurement/latest` | `/channel/measurement/latest` | `/channel/measurement/latest` | — | — |
| subscription | `/channel/measurement/listen` | — | — | `/channel/measurement/listen` | `channel/measurement/listen` |

> **NOTE** — For older measurement data, use the `historical-data` endpoint.

#### 3.10.1 Response

| Key | Value type | Required | Comment |
|---|---|---|---|
| channel_nr | integer: 1...12 | Yes | Channel number |
| resistance | float \| empty | Yes | Resistance (Ohm) |
| reactance | float \| empty | Yes | Reactance (Ohm) |
| temperature | float \| empty | Yes | Temperature (K) |
| rez | float \| empty | Yes | Real part of impedance (Ohm) |
| imz | float \| empty | Yes | Imaginary part of impedance (Ohm) |
| magnitude | float \| empty | Yes | Magnitude of impedance (Ohm) |
| angle | float \| empty | Yes | Angle of impedance (degrees) |
| timestamp | float | Yes | End time of measurement (Unix time) |
| settings_nr | integer: 1...24 | Yes | Measurement settings number |
| status_flags | array of integers | Yes | List of measurement error codes (see error code table) |

---

### 3.11 Channel / Heater

**Endpoint: Relation Between a Channel and a Heater**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| write | `/channel/heater/update` | — | `/channel/heater/update` | `/channel/heater/update` | `channel/heater/update/in` / `channel/heater/update/out` |
| subscription | `/channel/heater/listen` | — | — | `/channel/heater/listen` | `channel/heater/listen` |

#### 3.11.1 Write Request

| Key | Value type | Required | Comment |
|---|---|---|---|
| channel_nr | integer: 1...12 | Yes | Channel number |
| heater_nr | integer: 0...4 | Yes | Heater number |

#### 3.11.2 Response

| Key | Value type | Required | Comment |
|---|---|---|---|
| relations | array of ChannelHeaterRelation objects | Yes | See below |

#### 3.11.3 ChannelHeaterRelation Object

| Key | Value type | Required | Comment |
|---|---|---|---|
| channel_nr | integer | Yes | Channel number |
| heater_nr | integer | Yes | Heater number |

---

### 3.12 Heaters

**Endpoint: Heater Settings (Read All)**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/heaters` | `/heaters` | — | `/heaters` | `heaters/in` / `heaters/out` |

#### 3.12.1 Read Request
Empty.

#### 3.12.2 Response
Array of results for each heater. Each element uses the same response format as the single heater endpoint.

---

### 3.13 Heater

**Endpoint: Heater Settings (Read / Write)**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/heater` | — | `/heater` | `/heater` | `heater/in` / `heater/out` |
| write | `/heater/update` | — | `/heater/update` | `/heater/update` | `heater/update/in` / `heater/update/out` |
| subscription | `/heater/listen` | — | — | `/heater/listen` | `heater/listen` |

#### 3.13.1 Read Request

| Key | Value type | Required | Comment |
|---|---|---|---|
| heater_nr | integer: 1...4 | Yes | Heater number |

#### 3.13.2 Write Request

| Key | Value type | Required | Comment |
|---|---|---|---|
| heater_nr | integer | Yes | Heater number |
| active | boolean | No | Active state: ON or OFF |
| name | string | No | Heater name |
| pid_mode | integer | No | `0`: Manual mode, `1`: PID mode |
| resistance | float: 0...1000 | No | Heater resistance in Ohms |
| power | float: 0.0...1.0 | No | Applied manual power in Watts (max 100 mA) |
| max_power | float: 0.0...1.0 | No | Hard safety limit for power in Watts |
| target_temperature | float: 0...1000.0 | No | Manual mode: target temperature |
| target_temperature_shown | boolean | No | Manual mode: show target temperature in graph |
| control_algorithm | integer | No | `1`: default PID algorithm |
| control_algorithm_settings | ControlAlgorithmSettings object | No | Control algorithm settings |
| setpoint | float: 0...1000.0 | No | Set point for control algorithm |

#### 3.13.3 ControlAlgorithm Settings

| Key | Value type | Required | Comment |
|---|---|---|---|
| proportional | float | No | PID P |
| integral | float | No | PID I |
| derivative | float | No | PID D |

#### 3.13.4 Response

| Key | Value type | Required | Comment |
|---|---|---|---|
| *(same fields as write request)* | | | |
| relay_mode | integer: 0, 1 | Yes | External relay mode: `0` = Shorted, `1` = Open |
| relay_status | integer: 0, 1 | Yes | External relay status: `0` = Shorted, `1` = Open |

---

### 3.14 Heater / Relay

**Endpoint: Heater Relay Settings (Read / Write)**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/heater/relay` | — | `/heater/relay` | `/heater/relay` | `heater/relay/in` / `heater/relay/out` |
| write | `/heater/relay/update` | — | `/heater/relay/update` | `/heater/relay/update` | `heater/relay/update/in` / `heater/relay/update/out` |
| subscription | `/heater/relay/listen` | — | — | `/heater/relay/listen` | `heater/relay/listen` |

#### 3.14.1 Read Request

| Key | Value type | Required | Comment |
|---|---|---|---|
| heater_nr | integer: 1...4 | Yes | Heater number |

#### 3.14.2 Write Request

| Key | Value type | Required | Comment |
|---|---|---|---|
| heater_nr | integer | Yes | Heater number |
| relay_mode | integer: 0, 1 | Yes | External relay mode: `0` = Shorted, `1` = Open |

#### 3.14.3 Response

| Key | Value type | Required | Comment |
|---|---|---|---|
| *(same fields as write request)* | | | |
| relay_status | integer: 0, 1 | Yes | External relay status: `0` = Shorted, `1` = Open |

---

### 3.15 Heater / Historical-Data

**Endpoint: Heater Historical Data**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/heater/historical-data` | — | `/heater/historical-data` | `/heater/historical-data` | `heater/historical-data/in` / `heater/historical-data/out` |

#### 3.15.1 Read Request

| Key | Value type | Required | Comment |
|---|---|---|---|
| heater_nr | integer: 1...4 | Yes | Heater number |
| start_time | datetime string | Yes | Formats: `YYYY-MM-DD`, `YYYY-MM-DD HH:MM`, `YYYY-MM-DD HH:MM:SS`, `YYYY-MM-DDTHH:MM:SSZ` |
| stop_time | datetime string | Yes | Same formats as `start_time` |
| fields | array of strings | Yes | `"power"`, `"current"` |

#### 3.15.2 Response

| Key | Value type | Required | Comment |
|---|---|---|---|
| *(same fields as read request)* | | | |
| measurements | object with data arrays | Yes | Array element names match field names |
| over_limit | boolean | Yes | `True` if requested data is too large |

**Example:**
```json
{
  "sender": "client-name-or-id",
  "hash": "this-is-just-hash-number-issued-by-client",
  "datetime": "2024-01-31T13:04:43.060313Z",
  "status": "OK",
  "heater_nr": 1,
  "over_limit": false,
  "fields": ["timestamp", "power"],
  "measurements": {
    "timestamp": [1542117983.719],
    "power": [1e-06]
  }
}
```

---

### 3.16 Calibration Curves (Multiple)

**Endpoint: Calibration Curves**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/calibration-curves` | `/calibration-curves` | — | `/calibration-curves` | `calibration-curves/in` / `calibration-curves/out` |
| read (full data) | `/calibration-curves/data` | `/calibration-curves/data` | — | `/calibration-curves/data` | `calibration-curves/data/in` / `calibration-curves/data/out` |

#### 3.16.1 Read Request
Empty.

#### 3.16.2 Response (No Full Calibration Curve Data)

Array of results for each calibration curve.

| Key | Value type | Required | Comment |
|---|---|---|---|
| calib_curve_nr | integer: 1...100 | Yes | Calibration curve number |
| type | integer | Yes | `-1`: Slot empty, `1`: R→T curve, `2`: X→T curve (8 Hz), `3`: X→T curve (64 Hz) |
| curve_hash | integer | Yes | Internal unique counter value for calibration curve |

#### 3.16.3 Response (Full Calibration Curve Data)

Array of results. Each element uses the same format as the single calibration curve response (see Table 54).

**Example:**
```json
{
  "sender": "client-name-or-id",
  "hash": "this-is-just-hash-number-issued-by-client",
  "datetime": "2024-01-31T13:04:43.060313Z",
  "status": "OK",
  "data": [
    { "calib_curve_nr": 1, "type": -1, "curve_hash": -1 },
    { "calib_curve_nr": 100, "type": 1, "curve_hash": -1 }
  ]
}
```

---

### 3.17 Calibration Curve (Single)

**Endpoint: Calibration Curve (Single)**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/calibration-curve` | — | `/calibration-curve` | `/calibration-curve` | `calibration-curve/in` / `calibration-curve/out` |
| write | `/calibration-curve/update` | — | `/calibration-curve/update` | `/calibration-curve/update` | `calibration-curve/update/in` / `calibration-curve/update/out` |
| subscription | `/calibration-curve/listen` | — | — | `/calibration-curve/listen` | `calibration-curve/listen` |
| remove | `/calibration-curve/remove` | — | `/calibration-curve/remove` | `/calibration-curve/remove` | `calibration-curve/remove/in` / `calibration-curve/remove/out` |
| file upload | `/calibration-curve/file-upload` | — | `/calibration-curve/file-upload` | `/calibration-curve/file-upload` | `calibration-curve/file-upload/in` / `calibration-curve/file-upload/out` |

#### 3.17.1 Read Request

| Key | Value type | Required | Comment |
|---|---|---|---|
| calib_curve_nr | integer: 1...100 | Yes | Calibration curve number |

#### 3.17.2 Write Request

| Key | Value type | Required | Comment |
|---|---|---|---|
| calib_curve_nr | integer: 1...100 | Yes | Calibration curve number |
| name | string (max 50 chars) | Yes | Name of the curve |
| sensor_model | string (max 50 chars) | Yes | Sensor model |
| points | integer: 2...200 | Yes | Number of points in the curve |
| impedances | array of floats (max 200) | Yes | Resistances or reactances in Ohm |
| temperatures | array of floats (max 200) | Yes | Temperatures in Kelvin (same size as impedances) |
| type | integer | Yes | `1`: R→T curve, `2`: X→T curve (8 Hz), `3`: X→T curve (64 Hz) |

#### 3.17.3 Remove Request

Same format as the read request (requires `calib_curve_nr`).

#### 3.17.4 Upload Request

| Key | Value type | Required | Comment |
|---|---|---|---|
| calib_curve_nr | integer: 1...100 | Yes | Calibration curve number |
| file_contents | string | Yes | Contents of calibration curve file in string format (write request only) |

#### 3.17.5 Response

| Key | Value type | Required | Comment |
|---|---|---|---|
| *(same fields as write request)* | | | |
| curve_hash | integer | Yes | Internal unique counter value for calibration curve |

**Example:**
```json
{
  "sender": "client-name-or-id",
  "hash": "this-is-just-hash-number-issued-by-client",
  "datetime": "2024-01-31T13:04:43.060313Z",
  "status": "OK",
  "calib_curve_nr": 4,
  "name": "NAME",
  "sensor_model": "MODEL",
  "points": 4,
  "impedances": [0.001, 0.002, 0.003, 0.004],
  "temperatures": [1e-06, 2e-06, 3e-06, 4e-06],
  "type": 1,
  "curve_hash": 1
}
```

---

## 4 Examples

Required Python packages:
```
requests>=0.19.1
websocket-client>=0.53.0
```

### 4.1 Read Values with HTTP GET

Continuously reads measurement results using the `/channel/measurement/latest` endpoint.

```python
# -*- coding: utf-8 -*-
"""Example: reading current measurement results using HTTP interface."""

import json
import requests
from time import sleep

DEVICE_IP = 'localhost'
TIMEOUT = 10
LOOP_TIMEOUT = 10

url = 'http://{}:5001/channel/measurement/latest'.format(DEVICE_IP)

while True:
    req = requests.get(url, timeout=TIMEOUT)
    data = req.json()
    print('Response: \n{}'.format(json.dumps(data, indent=2)))
    sleep(LOOP_TIMEOUT)
```

### 4.2 Read Values with WebSocket

Reads the latest measurement results using the `/channel/measurement/listen` endpoint.

```python
# -*- coding: utf-8 -*-
"""Example: reading current measurement results using WebSocket interface."""

import json
import websocket

DEVICE_IP = 'localhost'
TIMEOUT = 10

url = 'ws://{}:5002/channel/measurement/listen'.format(DEVICE_IP)
ws = websocket.create_connection(url, timeout=TIMEOUT)

while True:
    try:
        resp = ws.recv()
    except websocket.WebSocketTimeoutException:
        continue
    data = json.loads(resp)
    print('Response: \n{}'.format(json.dumps(data, indent=2)))
```

### 4.3 Read Settings

Reads settings using the `/system` and `/channel` endpoints.

```python
# -*- coding: utf-8 -*-
"""Example: read different settings using GET and POST methods of HTTP protocol."""

import json
import requests

DEVICE_IP = 'localhost'
TIMEOUT = 10

# Part 1: Read system settings using HTTP GET
url = 'http://{}:5001/system'.format(DEVICE_IP)
req = requests.get(url, timeout=TIMEOUT)
data = req.json()
print('Response: \n{}'.format(json.dumps(data, indent=2)))

# Part 2: Read channel N settings using HTTP POST
url = 'http://{}:5001/channel'.format(DEVICE_IP)
data = {'channel_nr': 2}
req = requests.post(url, json=data, timeout=TIMEOUT)
data = req.json()
print('Response: \n{}'.format(json.dumps(data, indent=2)))
```

### 4.4 Write Settings

Updates channel settings using the `/channel/update` endpoint.

```python
# -*- coding: utf-8 -*-
"""Example: update some of channel settings using HTTP interface."""

import json
import requests

DEVICE_IP = 'localhost'
TIMEOUT = 10

url = 'http://{}:5001/channel/update'.format(DEVICE_IP)
data = {
    'channel_nr': 1,
    'excitation_mode': 0,
    'excitation_current_range': 11,
    'calib_curve_nr': 22
}
req = requests.post(url, json=data, timeout=TIMEOUT)
data = req.json()
print('Response: \n{}'.format(json.dumps(data, indent=2)))
```

### 4.5 Read Historical Data

Loads historical measurement results using the `/channel/historical-data` endpoint.

```python
# -*- coding: utf-8 -*-
"""Example: read channel old measurement data."""

import json
import requests

DEVICE_IP = 'localhost'
TIMEOUT = 100

url = 'http://{}:5001/channel/historical-data'.format(DEVICE_IP)
data = {
    'channel_nr': 8,
    'start_time': '2023-01-31T00:00:00Z',
    'stop_time': '2024-01-31T00:00:00Z',
    'fields': ['temperature', 'resistance', 'reactance']
}
req = requests.post(url, json=data, timeout=TIMEOUT)
data = req.json()
print('Response: \n{}'.format(json.dumps(data, indent=2)))
```

### 4.6 Calibration Curve Loading

Reads and updates a calibration curve using the `/calibration-curve` endpoint.

```python
# -*- coding: utf-8 -*-
"""Example: calibration curve manipulation."""

import json
import requests

DEVICE_IP = 'localhost'
TIMEOUT = 10
CALIB_CURVE_NR = 98

# Read calibration curve N
url = 'http://{}:5001/calibration-curve'.format(DEVICE_IP)
data = {'calib_curve_nr': CALIB_CURVE_NR}
req = requests.post(url, json=data, timeout=TIMEOUT)
data = req.json()
print('Response: \n{}'.format(json.dumps(data, indent=2)))

# Update calibration curve N
url = 'http://{}:5001/calibration-curve/update'.format(DEVICE_IP)
data = {
    'calib_curve_nr': CALIB_CURVE_NR,
    'name': 'NAME',
    'sensor_model': 'MODEL',
    'points': 2,
    'impedances': [1, 2],
    'temperatures': [1, 2],
    'type': 1
}
req = requests.post(url, json=data, timeout=TIMEOUT)
data = req.json()
print('Response: \n{}'.format(json.dumps(data, indent=2)))
```