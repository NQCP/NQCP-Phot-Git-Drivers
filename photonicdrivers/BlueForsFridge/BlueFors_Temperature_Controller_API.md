# Bluefors Temperature Controller API
**Technical Reference** | Version 2.0, en-US | August 28, 2024  
Document ID: BF1000-1234517327-58

---

## Table of Contents

1. [Introduction](#1-introduction)
   - 1.1 [Overview of the User Instructions](#11-overview-of-the-user-instructions)
   - 1.2 [Related Information](#12-related-information)
   - 1.3 [Terms and Abbreviations](#13-terms-and-abbreviations)
   - 1.4 [Symbols and Conventions](#14-symbols-and-conventions)
   - 1.5 [Customer Service and Support](#15-customer-service-and-support)
   - 1.6 [Warranty](#16-warranty)
2. [API Description](#2-api-description)
   - 2.1 [General Information](#21-general-information)
   - 2.2 [Endpoint Format](#22-endpoint-format)
   - 2.3 [Protocols](#23-protocols)
   - 2.4 [Message Payload](#24-message-payload)
   - 2.5 [Tutorial](#25-tutorial)
3. [API Reference](#3-api-reference)
   - 3.1 [System](#31-system)
   - 3.2 [System / device](#32-system--device)
   - 3.3 [System / network](#33-system--network)
   - 3.4 [System / reset](#34-system--reset)
   - 3.5 [System / resources](#35-system--resources)
   - 3.6 [Statemachine](#36-statemachine)
   - 3.7 [Channels](#37-channels)
   - 3.8 [Channel](#38-channel)
   - 3.9 [Channel / historical-data](#39-channel--historical-data)
   - 3.10 [Channel / measurement](#310-channel--measurement)
   - 3.11 [Channel / heater](#311-channel--heater)
   - 3.12 [Heaters](#312-heaters)
   - 3.13 [Heater](#313-heater)
   - 3.14 [Heater / relay](#314-heater--relay)
   - 3.15 [Heater / historical-data](#315-heater--historical-data)
   - 3.16 [Calibration Curves (multiple)](#316-calibration-curves-multiple)
   - 3.17 [Calibration Curve (single)](#317-calibration-curve-single)
4. [Examples](#4-examples)
   - 4.1 [Read Values with HTTP GET](#41-read-values-with-http-get)
   - 4.2 [Read Values with WebSocket](#42-read-values-with-websocket)
   - 4.3 [Read Settings](#43-read-settings)
   - 4.4 [Write Settings](#44-write-settings)
   - 4.5 [Read Historical Data](#45-read-historical-data)
   - 4.6 [Calibration Curve Loading](#46-calibration-curve-loading)

---

## 1 Introduction

### 1.1 Overview of the User Instructions

This information applies to the Bluefors Temperature Controller. The following types of information products are available:

| Type | Description |
|---|---|
| **User Manual** | Functional description of the product, component descriptions, and operating, maintenance, and troubleshooting instructions. Can also include installation and commissioning instructions. |
| **Technical Reference** | Necessary background information and technical details about a subject, such as parameter descriptions and use of scripts and API. |

> **NOTE:** These instructions are essential for the use of the Bluefors product. For safe and proper use of the product, read the instructions before use. Keep them for future reference.

### 1.2 Related Information

| Information | ID | Location |
|---|---|---|
| Bluefors Temperature Controller User Manual | BF1000-1234517327-60 | Available on Bluefors website: https://bluefors.com/support |

### 1.3 Terms and Abbreviations

| Term / Abbreviation | Definition |
|---|---|
| API | application programming interface |
| LAN | local area network |
| URL | unified resource locator |

### 1.4 Symbols and Conventions

> **NOTE:** A note is used to indicate additional important information to the reader.

### 1.5 Customer Service and Support

Bluefors support includes reasonable telephone and email customer service during normal business hours (Finland). Support is provided by experienced technical personnel.

- **Support documents and downloadable software:** https://bluefors.com/support
- **Technical issues / system operation:** support@bluefors.com or +358 9 5617 4800
- **Sales-related issues:** sales@bluefors.com or +358 9 5617 4800
- **Global sales contact information:** https://bluefors.com

> **NOTE:** In case of emergency or accidents, call your local emergency services.

### 1.6 Warranty

For warranty information, refer to the Bluefors warranty statement.

---

## 2 API Description

### 2.1 General Information

This document describes the application programming interface for the Bluefors Temperature Controller. The API is the interface for programs to access and control the device. Any programming language that supports REST API (HTTP GET/POST), WebSocket, or MQTT can be used.

### 2.2 Endpoint Format

The API uses endpoints to access data. Endpoints are URL patterns (e.g., `network`).

**General rules:**

- Format: `element/sub-element/action`
- The `settings` element is default and not written in the endpoints.
- The `read` action is default and not written in the endpoints.
- There are no IDs in endpoints.
- Main elements:
  - `system`
  - `statemachine`
  - `channels` and `channel`
  - `heaters` and `heater`
  - `calibration-curves` and `calibration-curve`

**Endpoint construction examples:**

| Goal | Endpoint |
|---|---|
| Reading `/system` settings | `/system/settings/` |
| Subscribing to channels' measurements | `/channel/measurements/subscribe` |
| Read every calibration curve with full data | `/calibration-curves/data/read` |

**Operation modes:**

All interfaces use two modes:

- **request-response** — single request, single response containing the latest known data.
- **subscription** — no request; subscription is done by connecting to the endpoint (WebSocket) or subscribing to the topic (MQTT). Unlimited responses, each containing the latest known data at that moment.

> **NOTE:** By default, the WebSocket and MQTT interfaces are buffering unread responses to some limit defined by the interface itself, and the next receive attempt could give the last unread response from that buffer.

### 2.3 Protocols

#### 2.3.1 MQTT

- **Port:** 1883

**Topic formats:**

| Direction | Format |
|---|---|
| Incoming messages | `endpoint/in` |
| Outgoing messages | `endpoint/out` |

**Client modes:** request-response, subscription (no specific subscription endpoint — the same outgoing messages topic is used).

#### 2.3.2 HTTP

- **Port:** 5001

**URL formats:**

| Status | Format |
|---|---|
| Supported | `http://host:port/endpoint` |
| Not supported | `http://host:port/endpoint/` |
| Not supported | `http://host:port/endpoint/{id}` |
| Not supported | `http://host:port/endpoint?id={id}` *(all query parameters will be excluded from processing)* |

**HTTP methods:** `GET`, `POST`

**Client mode:** request-response only.

#### 2.3.3 WebSocket

- **Port:** 5002

**URL formats:** Same as for HTTP client.

**Client modes:** request-response, subscription (subscription done automatically by connecting to the endpoint; requests are not supported on subscription endpoints).

### 2.4 Message Payload

All message payloads are sent and received as JSON strings.

**Payload functionality by content:**

| Payload | Action |
|---|---|
| No payload | Read one/all elements |
| Payload with mandatory index fields | Read one element |
| Payload with mandatory index fields and optional fields | Write one element |

#### 2.4.1 Common Fields

##### Request Parameters

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `sender` | string | No | Sender name. Used by the request sender to recognize the response. |
| `hash` | string (size: 0–50) | No | Original message hash number. Used by the request sender to recognize the response. |

> **NOTE:** Request parameters are not possible in HTTP GET.

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

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `sender` | string | No | Same as in request. |
| `hash` | string | No | Same as in request. |
| `datetime` | datetime string | Yes | Datetime string in UTC format. Example: `"2024-01-31T13:04:43.060313Z"` |
| `status` | string | Yes | Allowed values: `"OK"`, `"ERROR"` |
| `error` | error object | No | Always sent if there is an error. |

##### Error Object Parameters

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `code` | integer >= 0 | Yes | Error code |
| `message` | string (max 2000 chars) | Yes | Error message |
| `details` | string (max 2000 chars) | No | Additional information as a string |

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

##### Error Codes

| Code | Type | Name | Description |
|---|---|---|---|
| 200 | Error | No data | Internal error: not getting data from the measurement hardware. |
| 241 | Error | Signal too noisy | An indication of high resistance. Examine the sensor connection. |
| 242 | Error | Overflow | The measurement is saturated. An indication of the resistance being higher than the current excitation range. |
| 243 | Error | Common mode overflow | The measurements between the preamplifier ground (cryostat) and the temperature sensor lead are saturated. Indication of a noisy grounding. |
| 244 | Error | Zero measured value | Internal error: the device does not measure properly or there is a shorted circuit. |
| 245 | Error | Resistance too high | The resistance is above the maximum range. |
| 246 | Error | Resistance too low | The resistance is below the minimum range. |
| 247 | Error | Unreliable data | The measured signal arrives later than expected. |
| 511 | Warning | Temperature below range | The temperature is below the programmed impedance temperature curve. |
| 512 | Warning | Temperature above range | The temperature is above the programmed impedance temperature curve. |
| 514 | Warning | Temperature below calibration range | The temperature is below the calibration range. |
| 515 | Warning | Temperature above calibration range | The temperature is above the calibration range. |
| 518 | Warning | Temperature data unreliable | The calculated temperature is negative. |
| 519 | Warning | No calibration curve | The calibration curve has not been defined. |
| 521 | Warning | Resistance below range | The resistance is below the calibration range. |
| 522 | Warning | Resistance above range | The resistance is above the calibration range. |
| 901 | Notification | Vmax auto-ranging | The current excitation is tuned to set the voltage to be the highest possible below the given value, Vmax. |

### 2.5 Tutorial

#### 2.5.1 Example: Access from Browser

Navigate to the following URL in a browser (replace IP as appropriate):

```
http://10.0.0.135:5001/system/network
```

Example JSON response:

```json
{
  "status": "OK",
  "state": "UP",
  "datetime": "2024-01-31T13:01:08.534671Z",
  "netmask": "255.255.0.0",
  "dns": "",
  "mac_address": "b8:27:eb:fd:a4:00",
  "ip_configuration": "DHCP",
  "ip_address": "10.0.0.135",
  "gateway": ""
}
```

Latest measurement results via:

```
http://10.0.0.135:5001/channel/measurement/latest
```

Example JSON response:

```json
{
  "rez": 10002.996333333334,
  "status": "OK",
  "angle": 89.59977777777777,
  "temperature": null,
  "timestamp": 1572353805.343614,
  "resistance": 10003.483555555556,
  "channel_nr": 6,
  "datetime": "2024-01-31T12:57:19.791712Z",
  "reactance": 1433539.4997777776,
  "magnitude": 10003.24,
  "status_flags": [511],
  "imz": 69.80922222222222
}
```

> **NOTE:** Responses are different depending on the status of the device.

#### 2.5.2 Example: Using a HTTP Interface

Requires the `requests` library (https://pypi.org/project/requests/).

```python
import json
import requests

req = requests.get('http://10.0.0.135:5001/channel/measurement/latest', timeout=10)
data = req.json()
print('Response: \n{}'.format(json.dumps(data, indent=2)))
```

Example output:

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

Requires the `websocket-client` library (https://pypi.org/project/websocket_client/).

```python
import json
import websocket

ws = websocket.create_connection(
    'ws://10.0.0.135:5002/channel/measurement/listen',
    timeout=10
)
resp = ws.recv()
data = json.loads(resp)
print('Response: \n{}'.format(json.dumps(data, indent=2)))
```

#### 2.5.4 Example: Using a MQTT Interface

Requires the `paho-mqtt` library (https://pypi.org/project/paho-mqtt/).

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

**Endpoint: System information**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/system` | `/system` | — | `/system` | `system/in` / `system/out` |

#### 3.1.1 Read Request

Empty.

#### 3.1.2 Response

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `api_version` | integer | Yes | API version. Allowed values: `1` |
| `type` | string (size: 0–50) | Yes | System type. Allowed values: `"Bluefors TC"` |
| `serial` | string (size: 0–50) | Yes | Device serial number |
| `label` | string (size: 0–30) | Yes | System label |
| `addinfo` | string (size: 0–50) | Yes | System additional information |
| `software_version` | string (size: 0–50) | Yes | Software version |

---

### 3.2 System / device

**Endpoint: Device information**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/system/device` | `/system/device` | — | `/system/device` | `system/device/in` / `system/device/out` |

#### 3.2.1 Read Request

Empty.

#### 3.2.2 Response

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `device_id` | string (size: 0–32) | Yes | Device ID |
| `device_firmware` | string (size: 0–50) | Yes | Device firmware version |

---

### 3.3 System / network

Only IPv4 is supported.

**Endpoint: Network settings**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/system/network` | `/system/network` | `/system/network` | `system/network/in` / `system/network/out` | |
| write | `/system/network/update` | — | `/system/network/update` | `/system/network/update` | `system/network/update/in` |
| subscription | `/system/network/listen` | — | — | `/system/network/listen` | `system/network/listen` |

#### 3.3.1 Read Request

Empty.

#### 3.3.2 Write Request

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `ip_configuration` | string | Yes | Allowed values: `"static"`, `"DHCP"` |
| `ip_address` | string | No | IPv4 address |
| `netmask` | string | No | IPv4 address |
| `gateway` | string | No | IPv4 address |
| `dns` | string | No | IPv4 address |

#### 3.3.3 Response

| Key | Value Type | Required | Comment |
|---|---|---|---|
| *(same fields as in write request)* | | | |
| `state` | string | Yes | Possible values: `"UP"`, `"DOWN"` |
| `mac_address` | string | Yes | MAC address |

---

### 3.4 System / reset

Only subscription is supported.

**Endpoint: System reboot / shutdown notification**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| subscription | `/system/reset/listen` | — | — | `/system/reset/listen` | `system/reset/listen` |

#### 3.4.1 Response

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `message` | string | Yes | Allowed values: `"restart"`, `"shutdown"` |

---

### 3.5 System / resources

Only subscription is supported.

**Endpoint: System resources**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| subscription | `/system/resources/listen` | — | — | `/system/resources/listen` | `system/resources/listen` |

#### 3.5.1 Response

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `uptime` | integer | Yes | Uptime in seconds |
| `memory_free` | integer | Yes | Memory: free in KB |
| `memory_used` | integer | Yes | Memory: used in KB |
| `cpu_total` | float | Yes | CPU usage: total (in percentage) |
| `disk_usage_log` | integer | Yes | Disk usage: log disk (in percentage) |
| `disk_usage_data` | integer | Yes | Disk usage: data disk (in percentage) |
| `rtc_battery` | float | Yes | RTC battery: voltage |

---

### 3.6 Statemachine

**Endpoint: Measurement state machine settings**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/statemachine` | `/statemachine` | — | `/statemachine` | `statemachine/in` / `statemachine/out` |
| write | `/statemachine/update` | — | `/statemachine/update` | `/statemachine/update` | `statemachine/update/in` / `statemachine/update/out` |
| subscription | `/statemachine/listen` | — | — | `/statemachine/listen` | `statemachine/listen` |

#### 3.6.1 Read Request

Empty.

#### 3.6.2 Write Request

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `wait_time` | float: 1...100 | No | Default wait time after changing channel before using values for measurement result. Value in seconds. |
| `meas_time` | float: 1...100 | No | Measurement time for measurement operation. Value in seconds. |
| `control_algorithm` | integer: 0...100 | No | Next channel selection algorithm. `1`: round robin |

#### 3.6.3 Response

| Key | Value Type | Required | Comment |
|---|---|---|---|
| *(same fields as in write request)* | | | |
| `state` | string | Yes | Textual representation of statemachine status |
| `measuring` | boolean | Yes | Measurements status: ON or OFF |
| `channel_nr` | integer: 1...12 | Yes | Current measurement channel or last used channel |

---

### 3.7 Channels

**Endpoint: Channel settings (read only)**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/channels` | `/channels` | — | `/channels` | `channels/in` / `channels/out` |

#### 3.7.1 Read Request

Empty.

#### 3.7.2 Response

An array of results for each channel. Each element uses the same response format as defined in [Section 3.8](#38-channel).

---

### 3.8 Channel

**Endpoint: Channel settings**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/channel` | — | `/channel` | `/channel` | `channel/in` / `channel/out` |
| write | `/channel/update` | — | `/channel/update` | `/channel/update` | `channel/update/in` / `channel/update/out` |
| subscription | `/channel/listen` | — | — | `/channel/listen` | `channel/listen` |

#### 3.8.1 Read Request

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `channel_nr` | integer: 1...12 | Yes | Channel number |

#### 3.8.2 Write Request

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `channel_nr` | integer | Yes | Channel number (the same as in read request) |
| `active` | boolean | No | Active status: ON or OFF |
| `name` | string | No | Channel name |
| `excitation_mode` | integer | No | Excitation modes: `0`: current excitation, `1`: VMAX, `2`: CMN |
| `excitation_current_range` | integer | No | Settings number for current excitation mode: `1`...`22` |
| `excitation_cmn_range` | integer | No | Current used for CMN excitation: `1`: 50 µA, `2`: 150 µA |
| `excitation_vmax_range` | integer | No | Maximum voltage over sample in VMAX mode: `1`: 20 µV, `2`: 200 µV |
| `use_non_default_timeconstants` | boolean | No | `True`: use channel's own wait and measurement times. `False`: use default timer values. |
| `wait_time` | float: 1...100 | No | Wait time after switching channel before measurement, in seconds. Valid if `use_non_default_timeconstants == True`. |
| `meas_time` | float: 1...100 | No | Time used for actual measurement of single value, in seconds. Valid if `use_non_default_timeconstants == True`. |
| `calib_curve_nr` | integer: 1...100 | No | Which calibration curve is used by this channel |

#### 3.8.3 Response

| Key | Value Type | Required | Comment |
|---|---|---|---|
| *(same fields as in write request)* | | | |
| `coupled_heater_nr` | integer: 0...4 | Yes | Which heater is coupled to the channel: `1`–`4`: heater 1–4, `0`: no heater. To change the relation, refer to [Channel / heater](#311-channel--heater). |

---

### 3.9 Channel / historical-data

**Endpoint: Channel historical data**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/channel/historical-data` | — | `/channel/historical-data` | `/channel/historical-data` | `channel/historical-data/in` / `channel/historical-data/out` |

#### 3.9.1 Read Request

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `channel_nr` | integer: 1...12 | Yes | Channel number |
| `start_time` | datetime string | Yes | Formats: `YYYY-MM-DD`, `YYYY-MM-DD HH:MM`, `YYYY-MM-DD HH:MM:SS`, `YYYY-MM-DDTHH:MM:SSZ` |
| `stop_time` | datetime string | Yes | Same formats as `start_time` |
| `fields` | array of strings | Yes | Requested data fields: `"temperature"`, `"resistance"`, `"reactance"`, `"rez"`, `"Imz"`, `"magnitude"`, `"angle"`, `"timestamp"`, `"status_flags"`, `"channel_nr"` |

#### 3.9.2 Response

| Key | Value Type | Required | Comment |
|---|---|---|---|
| *(same fields as in read request)* | | | |
| `measurements` | object with data arrays | Yes | Requested data. Array element names match field names. |
| `over_limit` | boolean | Yes | Flag indicating the amount of requested data is too large. If the limit of 100,000 is exceeded, no data is returned. |

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
    "timestamp": [1542118174.989, "..."],
    "temperature": [0.034756, "..."]
  }
}
```

---

### 3.10 Channel / measurement

**Endpoint: Latest real-time measurement data**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/channel/measurement/latest` | `/channel/measurement/latest` | `/channel/measurement/latest` | — | — |
| subscription | `/channel/measurement/listen` | — | — | `/channel/measurement/listen` | `channel/measurement/listen` |

> **NOTE:** If older measurement data is needed, use the `historical-data` endpoint described in [Section 3.9](#39-channel--historical-data).

#### 3.10.1 Response

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `channel_nr` | integer: 1...12 | Yes | Channel number |
| `resistance` | float \| empty | Yes | Resistance (Ohm) |
| `reactance` | float \| empty | Yes | Reactance (Ohm) |
| `temperature` | float \| empty | Yes | Temperature (K) |
| `rez` | float \| empty | Yes | Real part of impedance (Ohm) |
| `imz` | float \| empty | Yes | Imaginary part of impedance (Ohm) |
| `magnitude` | float \| empty | Yes | Magnitude of impedance (Ohm) |
| `angle` | float \| empty | Yes | Angle of impedance (degrees) |
| `timestamp` | float | Yes | End time of measurement (Unix time) |
| `settings_nr` | integer: 1...24 | Yes | Measurement settings number |
| `status_flags` | array of integers | Yes | List of measurement error codes. Refer to [Error Codes](#error-codes). |

---

### 3.11 Channel / heater

**Endpoint: Relation between a channel and a heater**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| write | `/channel/heater/update` | — | `/channel/heater/update` | `/channel/heater/update` | `channel/heater/update/in` / `channel/heater/update/out` |
| subscription | `/channel/heater/listen` | — | — | `/channel/heater/listen` | `channel/heater/listen` |

#### 3.11.1 Write Request

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `channel_nr` | integer: 1...12 | Yes | Channel number |
| `heater_nr` | integer: 0...4 | Yes | Heater number |

#### 3.11.2 Response

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `relations` | array of ChannelHeaterRelation objects | Yes | Refer to [ChannelHeaterRelation object](#3113-channelheaterrelation-object). |

#### 3.11.3 ChannelHeaterRelation Object

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `channel_nr` | integer | Yes | Channel number |
| `heater_nr` | integer | Yes | Heater number |

---

### 3.12 Heaters

**Endpoint: Heater settings (read)**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/heaters` | `/heaters` | — | `/heaters` | `heaters/in` / `heaters/out` |

#### 3.12.1 Read Request

Empty.

#### 3.12.2 Response

An array of results for each heater. Each element uses the same response format shown in [Section 3.13.4](#3134-response).

---

### 3.13 Heater

**Endpoint: Heater settings**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/heater` | — | `/heater` | `/heater` | `heater/in` / `heater/out` |
| write | `/heater/update` | — | `/heater/update` | `/heater/update` | `heater/update/in` / `heater/update/out` |
| subscription | `/heater/listen` | — | — | `/heater/listen` | `heater/listen` |

#### 3.13.1 Read Request

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `heater_nr` | integer: 1...4 | Yes | Heater number |

#### 3.13.2 Write Request

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `heater_nr` | integer | Yes | Heater number (the same as in read request) |
| `active` | boolean | No | Active state: ON or OFF |
| `name` | string | No | Heater name |
| `pid_mode` | integer | No | Heater mode: `0`: Manual mode, `1`: PID mode |
| `resistance` | float: 0...1000 | No | Heater resistance in Ohms |
| `power` | float: 0.0...1.0 | No | Applied manual power in Watts. Maximum power is 100 mA. |
| `max_power` | float: 0.0...1.0 | No | Hard safety limit for power in Watts |
| `target_temperature` | float: 0...1000.0 | No | Manual mode: target temperature |
| `target_temperature_shown` | boolean | No | Manual mode: show target temperature in the graph |
| `control_algorithm` | integer | No | Control algorithms: `1`: default PID algorithm |
| `control_algorithm_settings` | ControlAlgorithmSettings object | No | Control algorithm settings |
| `setpoint` | float: 0...1000.0 | No | Set point for control algorithm |

#### 3.13.3 ControlAlgorithm Settings

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `proportional` | float | No | PID P |
| `integral` | float | No | PID I |
| `derivative` | float | No | PID D |

#### 3.13.4 Response

| Key | Value Type | Required | Comment |
|---|---|---|---|
| *(same fields as in write request)* | | | |
| `relay_mode` | integer: 0, 1 | Yes | Mode of external relay: `0`: Shorted, `1`: Open |
| `relay_status` | integer: 0, 1 | Yes | Status of external relay: `0`: Shorted, `1`: Open |

---

### 3.14 Heater / relay

**Endpoint: Heater relay settings**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/heater/relay` | — | `/heater/relay` | `/heater/relay` | `heater/relay/in` / `heater/relay/out` |
| write | `/heater/relay/update` | — | `/heater/relay/update` | `/heater/relay/update` | `heater/relay/update/in` / `heater/relay/update/out` |
| subscription | `/heater/relay/listen` | — | — | `/heater/relay/listen` | `heater/relay/listen` |

#### 3.14.1 Read Request

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `heater_nr` | integer: 1...4 | Yes | Heater number |

#### 3.14.2 Write Request

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `heater_nr` | integer | Yes | Heater number (the same as in read request) |
| `relay_mode` | integer: 0, 1 | Yes | Mode of external relay: `0`: Shorted, `1`: Open |

#### 3.14.3 Response

| Key | Value Type | Required | Comment |
|---|---|---|---|
| *(same fields as in write request)* | | | |
| `relay_status` | integer: 0, 1 | Yes | Status of external relay: `0`: Shorted, `1`: Open |

---

### 3.15 Heater / historical-data

**Endpoint: Heater historical data**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/heater/historical-data` | — | `/heater/historical-data` | `/heater/historical-data` | `heater/historical-data/in` / `heater/historical-data/out` |

#### 3.15.1 Read Request

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `heater_nr` | integer: 1...4 | Yes | Heater number |
| `start_time` | datetime string | Yes | Formats: `YYYY-MM-DD`, `YYYY-MM-DD HH:MM`, `YYYY-MM-DD HH:MM:SS`, `YYYY-MM-DDTHH:MM:SSZ` |
| `stop_time` | datetime string | Yes | Same formats as `start_time` |
| `fields` | array of strings | Yes | Requested data fields: `"power"`, `"current"` |

#### 3.15.2 Response

| Key | Value Type | Required | Comment |
|---|---|---|---|
| *(same fields as in read request)* | | | |
| `measurements` | object with data arrays | Yes | Requested data. Array element names match field names. |
| `over_limit` | boolean | Yes | Flag indicating the amount of requested data is too large. |

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
    "timestamp": [1542117983.719, "..."],
    "power": [1e-06, "..."]
  }
}
```

---

### 3.16 Calibration Curves (multiple)

**Endpoint: Calibration curves**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/calibration-curves` | `/calibration-curves` | — | `/calibration-curves` | `calibration-curves/in` / `calibration-curves/out` |
| read (full data) | `/calibration-curves/data` | `/calibration-curves/data` | — | `/calibration-curves/data` | `calibration-curves/data/in` / `calibration-curves/data/out` |

#### 3.16.1 Read Request

Empty.

#### 3.16.2 Response (no full calibration curves data)

An array of results for each calibration curve. Each element has the following format:

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `calib_curve_nr` | integer: 1...100 | Yes | Calibration curve number |
| `type` | integer | Yes | Calibration curve type: `-1`: Slot empty, `1`: R → T curve, `2`: X → T curve (8 Hz), `3`: X → T curve (64 Hz) |
| `curve_hash` | integer | Yes | Internal unique counter value for calibration curve |

#### 3.16.3 Response (full calibration curves data)

An array of results for each calibration curve. Each element uses the same response format as [Section 3.17.5](#3175-response).

**Example:**

```json
{
  "sender": "client-name-or-id",
  "hash": "this-is-just-hash-number-issued-by-client",
  "datetime": "2024-01-31T13:04:43.060313Z",
  "status": "OK",
  "data": [
    { "calib_curve_nr": 1, "type": -1, "curve_hash": -1 },
    "...",
    { "calib_curve_nr": 100, "type": 1, "curve_hash": -1 }
  ]
}
```

---

### 3.17 Calibration Curve (single)

**Endpoint: Calibration curve (single)**

| Request | Endpoint | GET | POST | WebSocket | MQTT |
|---|---|---|---|---|---|
| read | `/calibration-curve` | — | `/calibration-curve` | `/calibration-curve` | `calibration-curve/in` / `calibration-curve/out` |
| write | `/calibration-curve/update` | — | `/calibration-curve/update` | `/calibration-curve/update` | `calibration-curve/update/in` / `calibration-curve/update/out` |
| subscription | `/calibration-curve/listen` | — | — | `/calibration-curve/listen` | `calibration-curve/listen` |
| remove | `/calibration-curve/remove` | — | `/calibration-curve/remove` | `/calibration-curve/remove` | `calibration-curve/remove/in` / `calibration-curve/remove/out` |
| file upload | `/calibration-curve/file-upload` | — | `/calibration-curve/file-upload` | `/calibration-curve/file-upload` | `calibration-curve/file-upload/in` / `calibration-curve/file-upload/out` |

#### 3.17.1 Read Request

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `calib_curve_nr` | integer: 1...100 | Yes | Calibration curve number |

#### 3.17.2 Write Request

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `calib_curve_nr` | integer: 1...100 | Yes | Calibration curve number |
| `name` | string: max 50 chars | Yes | Name of the curve |
| `sensor_model` | string: max 50 chars | Yes | Sensor model |
| `points` | integer: 2...200 | Yes | Number of points in the curve |
| `impedances` | array of floats: max size 200 | Yes | Resistances or reactances in Ohm |
| `temperatures` | array of floats: max size 200 | Yes | Temperatures in Kelvin. Must be the same array size as `impedances`. |
| `type` | integer | Yes | Calibration curve type: `1`: R → T curve, `2`: X → T curve (8 Hz), `3`: X → T curve (64 Hz) |

#### 3.17.3 Remove Request

A remove request uses the same format as the [Read Request](#3171-read-request).

#### 3.17.4 Upload Request

| Key | Value Type | Required | Comment |
|---|---|---|---|
| `calib_curve_nr` | integer: 1...100 | Yes | Calibration curve number |
| `file_contents` | string | Yes | Contents of calibration curve file in string format. Used only in write request message. |

#### 3.17.5 Response

| Key | Value Type | Required | Comment |
|---|---|---|---|
| *(same fields as in write request)* | | | |
| `curve_hash` | integer | Yes | Internal unique counter value for calibration curve |

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

The following examples are written in Python. The examples assume that these packages are installed:

```
requests>=0.19.1
websocket-client>=0.53.0
```

### 4.1 Read Values with HTTP GET

Reads measurement values continuously using the `/channel/measurement/latest` endpoint.

```python
# -*- coding: utf-8 -*-
"""
Example: reading current measurement results using HTTP interface.
"""

import json
import requests
from time import sleep

# Define your device IP here
DEVICE_IP = 'localhost'
# Timeout for get/post operations (in seconds)
TIMEOUT = 10
# Timeout used for loop cycle (in seconds)
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
"""
Example: reading current measurement results using WebSocket interface.
"""

import json
import websocket

# Define your device IP here
DEVICE_IP = 'localhost'
# Timeout for WebSocket operations (in seconds)
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
"""
Example: read different settings using GET and POST methods of HTTP protocol.
"""

import json
import requests

# Define your device IP here
DEVICE_IP = 'localhost'
# Timeout for http operations (in seconds)
TIMEOUT = 10

# --- Part 1: Read system settings using HTTP GET request
url = 'http://{}:5001/system'.format(DEVICE_IP)
req = requests.get(url, timeout=TIMEOUT)
data = req.json()
print('Response: \n{}'.format(json.dumps(data, indent=2)))

# --- Part 2: Read channel N settings using HTTP POST request
url = 'http://{}:5001/channel'.format(DEVICE_IP)
data = {
    'channel_nr': 2
}
req = requests.post(url, json=data, timeout=TIMEOUT)
data = req.json()
print('Response: \n{}'.format(json.dumps(data, indent=2)))
```

### 4.4 Write Settings

Updates channel settings using the `/channel/update` endpoint.

```python
# -*- coding: utf-8 -*-
"""
Example: update some of channel settings using HTTP interface.
"""

import json
import requests

# Define your device IP here
DEVICE_IP = 'localhost'
# Timeout for http operations (in seconds)
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

Loads old measurement results using the `/channel/historical-data` endpoint.

```python
# -*- coding: utf-8 -*-
"""
Example: read channel old measurement data.
"""

import json
import requests

# Define your device IP here
DEVICE_IP = 'localhost'
# Timeout for get/post operations (in seconds)
TIMEOUT = 100

url = 'http://{}:5001/channel/historical-data'.format(DEVICE_IP)
data = {
    'channel_nr': 8,
    'start_time': '2023-01-31T00:00:00Z',
    'stop_time': '2024-01-31T00:00:00Z',
    'fields': [
        'temperature',
        'resistance',
        'reactance'
    ]
}
req = requests.post(url, json=data, timeout=TIMEOUT)
data = req.json()
print('Response: \n{}'.format(json.dumps(data, indent=2)))
```

### 4.6 Calibration Curve Loading

Reads and updates a calibration curve using the `/calibration-curve` and `/calibration-curve/update` endpoints.

```python
# -*- coding: utf-8 -*-
"""
Example: calibration curve manipulation.
"""

import json
import requests

# Define your device IP here
DEVICE_IP = 'localhost'
# Timeout for http operations (in seconds)
TIMEOUT = 10
# Calibration curve number used in example
CALIB_CURVE_NR = 98

# --- Read calibration curve N data
url = 'http://{}:5001/calibration-curve'.format(DEVICE_IP)
data = {
    'calib_curve_nr': CALIB_CURVE_NR
}
req = requests.post(url, json=data, timeout=TIMEOUT)
data = req.json()
print('Response: \n{}'.format(json.dumps(data, indent=2)))

# --- Update calibration curve N data
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

---

*© 2024 Bluefors Oy. "Bluefors" and "Cool for Progress" are registered trademarks of Bluefors Oy. All rights reserved and unauthorized use prohibited.*  
*Contact: support@bluefors.com | +358 9 5617 4800 | https://bluefors.com/support*
