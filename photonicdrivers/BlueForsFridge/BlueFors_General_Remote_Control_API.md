# Technical Reference: Remote Access Control API Gen. 1

**Document ID:** BF1000-1234517327-83  
**Version:** 3.0, en-US  
**Date:** October 21, 2024  
**Classification:** CONFIDENTIAL  
© 2024 Bluefors Oy. "Bluefors" and "Cool for Progress" are registered trademarks of Bluefors Oy. All rights reserved and unauthorized use prohibited.

---

## Disclaimer

The information contained in this document is effective as of the publication date. Bluefors Oy reserves the right to make changes to the product and information contained in this document relative to the specifications, features, and design of the product.

Contact us directly (support@bluefors.com) if you have any questions about the specifications or any other content contained in this document.

**Contact information:**  
Bluefors Oy  
Arinatie 10  
00370 Helsinki, Finland  
support@bluefors.com  
+358 9 5617 4800

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Safety](#2-safety)
3. [Control API](#3-control-api)
4. [Program Structure](#4-program-structure)
- [Appendix I: API Reference](#appendix-i-api-reference)

---

## 1 Introduction

### 1.1 Overview of the User Instructions

Bluefors Control Software Gen. 1 is software used to control the Bluefors dilution refrigerator measurement systems. Control Software interfaces with and controls the devices that are part of the Control Unit.

| Document Type | Description |
|---|---|
| **User Manual** | Functional description of the product, component descriptions, and operating, maintenance, and troubleshooting instructions. Can also include installation and commissioning instructions. |
| **Technical Reference** | Necessary background information and technical details about a subject, such as parameter descriptions and use of scripts and API. |

> **NOTE:** These instructions apply to version 2.4.3 and earlier versions of Bluefors Control Software and Control API, Gen. 1.

### 1.2 Related Information

| Information | ID | Location |
|---|---|---|
| Bluefors Control Software Gen. 1 User Manual | BF1000-1234517327-71 | Available on Bluefors website: https://bluefors.com/support/ |

### 1.3 Terms and Abbreviations

| Term / Abbreviation | Definition |
|---|---|
| API | application programming interface |
| CU | Control Unit |
| FSE | Fast Sample Exchange |
| HTTP | Hypertext Transfer Protocol |
| JSON | JavaScript object notation |
| URI | uniform resource identifier |
| URL | uniform resource locator |
| WS | WebSocket |
| WSS | Secure WebSocket |

### 1.4 Symbols and Conventions

A **NOTE** is used to indicate additional important information to the reader.

### 1.5 Customer Service and Support

Bluefors support includes reasonable telephone and email customer service during normal business hours (Finland). Support is provided by experienced technical personnel.

- Support documents and downloadable software: https://bluefors.com/support
- Technical issues or questions: support@bluefors.com or +358 9 5617 4800
- Sales-related issues: sales@bluefors.com or +358 9 5617 4800

### 1.6 Warranty

For warranty information, refer to the Bluefors warranty statement.

---

## 2 Safety

### 2.1 Safety Message Descriptions

| Level | Description |
|---|---|
| **DANGER** | Indicates an imminently hazardous situation which, if not avoided, **will result in death or serious injury**. |
| **WARNING** | Indicates a potentially hazardous situation which, if not avoided, **could result in death or serious injury**. |
| **CAUTION** | Indicates a hazardous situation which, if not avoided, **could result in minor or moderate injury**. |
| **NOTICE** | Indicates a message related to **property damage only**. There is no obvious risk of personal injury. |

### 2.2 Safety Symbol Color Descriptions

| Color | Meaning |
|---|---|
| Yellow | Indicates a warning |
| Red | Indicates a prohibition |
| Blue | Indicates a mandatory action |

### 2.3 Safety Symbols

| Symbol | Meaning |
|---|---|
| Refer to instruction manual/booklet | General mandatory action sign |

---

## 3 Control API

The Control API provides remote access to the software. It supports HTTP and WebSocket based APIs with and without encryption.

All requests and commands in the API use **JSON** (https://www.json.org/) as a format for the content.

> **NOTICE:** Only use Control Software for the intended purpose it has been designed for.

> **NOTICE:** Control Software interfaces directly with the operation of the dilution refrigerator. You are responsible for the correct performance of any operation.

> **NOTICE:** Always read and follow the instructions, safety information, and warnings stated in the instructions. Incorrect action or operation may cause critical malfunction or system breakdown.

### 3.1 Structure and Terminology

#### 3.1.1 Addressing

The resources in the API are referred to by URIs, defined in RFC 3986 (https://datatracker.ietf.org/doc/html/rfc3986).

```
http :// localhost:1234 / values ? filter=value # something
ws   :// localhost:1234 / ws/values
      [scheme] [authority]  [path]   [query]
```

- **Scheme:** Defines the used protocol: `http`, `https`, `ws`, or `wss`.
- **Authority:** Defines the host name and port number as `<hostname>:<port>`.
- **Path:** Defines the location of the resource in the server.
- **Query:** Contains additional data passed to the resource, as key-value pairs separated by commas: `<param1>=<value1>, <param2>=<value2>`.
- **Fragment:** Not used in this API.

#### 3.1.2 Services

The Control API provides features divided into **services** (called **endpoints**) identified by the first part of a URI path.

- **HTTP endpoints** are identified by the first part of the path, e.g., `http://localhost:1234/values/driver/`.
- **WebSocket endpoints** are identified by the first two parts of the path, where the first part is always `ws`, e.g., `http://localhost:1234/ws/values`.

### 3.2 Access Protocols

The API supports HTTP and WebSocket with (HTTPS and Secure WebSocket) and without encryption.

- **HTTP:** Request-based protocol; client must poll for new data.
- **WebSocket:** Establishes a continuous bidirectional connection; server automatically pushes new data when available.

> **NOTE:** Both protocols provide access to the same data. If a simpler HTTP connection is sufficient, there is no need to support WebSocket.

### 3.3 Hypertext Transfer Protocol – HTTP

The HTTP protocol is defined in RFC 2616 (https://datatracker.ietf.org/doc/html/rfc2616). The secured connection (HTTPS) is defined in RFC 2818 (https://datatracker.ietf.org/doc/html/rfc2818).

#### 3.3.1 Quick Start

The simplest way of communicating with the API is to use HTTP or HTTPS.

**Example: Reading the flow sensor via a web browser**

1. Ensure the Bluefors control card device is added and connected.
2. Select the **Configuration** icon.
3. Select the **API** tab.
4. Verify the HTTP/WebSocket port is `49099`. Enable the **Enable API** toggle switch.
5. Enable the **Enable HTTP and WebSocket** toggle switch.
6. Open a web browser and navigate to: `http://localhost:49099/values/mapper/bf/flow`
7. The browser displays a JSON response containing the flow value and additional data.

#### 3.3.2 HTTP Protocol

Communication is **request-response based**. The four commands are:

| Command | Purpose |
|---|---|
| **GET** | Returns the resource or data (e.g., a value in the value tree) |
| **POST** | Updates the data (only supported on writable values) |
| **PUT** | Adds data (currently not used) |
| **DELETE** | Deletes data (currently not used) |

- The **GET** command only has content in the response.
- **POST** and **PUT** allow content in both request and response.
- Query parameters contain additional information such as the API key.
- The response content always contains the data being requested or updated.

### 3.4 WebSocket Protocol

The WebSocket protocol is defined in RFC 6455 (https://tools.ietf.org/html/rfc6455). It establishes a continuous bidirectional stream, allowing subscription to value change events.

#### 3.4.1 Starting the Connection

WebSocket services are accessed through paths starting with `ws` followed by the endpoint name. An access key can be specified as a query parameter `key`.

**Example:**
```
wss://localhost:49099/ws/values/?key=00000000-1111-2222-3333-444444444444
```

If access is denied, an HTTP response with code `503` is returned.

#### 3.4.2 Communication Scheme

Each data packet is a complete JSON object. The server and client can send packets asynchronously at any time.

##### 3.4.2.1 Data Flow

- Client sends a command → server responds with status `RECEIVED`, then `SUCCEEDED` (with data) or `ERROR`.
- All packets related to a specific command are linked by an **ID** (auto-generated or user-supplied).
- The server can also send asynchronous events with status `NOTIFICATION`.

> **NOTE:** Some endpoints may deviate from the standard data flow. Deviations are described in the corresponding endpoint reference sections.

##### 3.4.2.2 Packet Structure

**Commands** (client → server):

| Field | Description |
|---|---|
| `id` | Optional unique string identifier (hex characters, `-`, `_`). Generated if not specified. |
| `command` | Command name (e.g., `set`, `read`, `listen`) |
| `data` | Command-specific JSON payload |

**Success Responses** (server → client):

| Field | Description |
|---|---|
| `id` | Unique string identifier |
| `status` | `RECEIVED` or `SUCCEEDED` |
| `data` | Command-specific JSON payload |

**Error Responses** (server → client):

| Field | Description |
|---|---|
| `id` | Unique string identifier (absent for general errors) |
| `status` | Always `ERROR` |
| `code` | Numeric error type code |
| `description` | Human-readable explanation |
| `details` | Additional command-specific data (e.g., offending payload) |

**Asynchronous Events** (server → client):

| Field | Description |
|---|---|
| `id` | Unique string identifier (absent if not tied to a specific command) |
| `event` | Event type (e.g., value update, disconnect) |
| `status` | Always `NOTIFICATION` |
| `data` | Event-specific JSON payload |

### 3.5 Authentication and Security

- **Port 49099:** Unencrypted, local connections only.
- **Port 49098:** Encrypted (HTTPS/WSS), open for external communication.
- Both connections support access keys for authentication.

#### 3.5.1 Access Keys

The API configuration includes a list of access keys and endpoints. Keys can be configured to grant or deny access per endpoint and per operation type.

- A special key `<unauthenticated>` controls access without a key (unencrypted connections only).
- Secure connections always require a key as a query parameter.
- If a key or permission is removed after a WebSocket connection is established, the connection remains open but all subsequent commands are denied.

#### 3.5.2 Design Considerations

When designing services accessible from the internet:

- Do **not** store keys in client-side applications.
- Use a **proxy server** that holds the actual key and manages communication with both Control Software instances and end users.
- The proxy server must provide its own session management and access control.

---

## 4 Program Structure

### 4.1 High-Level Design

Bluefors Control Software replaces the old Bluefors ValveControl Software. Internally, it is a modular measurement framework organized in four layers:

| Layer | Components |
|---|---|
| **1 – Framework layer** | Module managers, Modules, Value tree, Resource management, Configuration management |
| **2 – Module layer** | Manager types, Specialized modules |
| **3 – Logical layer** | Logical functionality, Set of module instances, Configurations, Resources |
| **4 – User interface layer** | User interface, Defined in resources |

#### 4.1.1 Managers and Modules

Modules handle specific tasks; module managers manage them. The standard managers are:

| Manager | Role |
|---|---|
| `driver` | Manages communication with devices |
| `mapper` | Maps driver data to logical names (e.g., relay channels → valve names V1–V23) |
| `script` | Runs scripted tasks (user-configurable or background monitoring) |
| `general` | General purpose features (e.g., logging, system tray UI) |

#### 4.1.2 Value Tree

The **value tree** is the central structure containing all runtime data: measured values, controls, and device configuration. It follows the same hierarchical structure as modules and managers.

### 4.2 Data Flow

All interaction with measurement and control data is done through the value tree.

#### 4.2.1 Standard Data Flow

Typical flow: user action → mapper module node updated → update request forwarded to device node → device driver performs write operation.

The Bluefors Control Card is a relay control card with up to eight sets of eight outputs (numbered 1.1–8.8), exposed as values `ch11` to `ch88`. Mapper modules translate these to logical valve names (e.g., V1–V23).

#### 4.2.2 Mapped and Driver Values

- **Mapped values** provide a simplified, system-agnostic interface.
- **Driver values** provide direct access to all device features.

> **NOTE:** The device drivers provide direct access to all device features, but be careful not to interfere with the normal functions of the dilution refrigerator.

> **NOTE:** When controlling the system through Control API, remember that the mapped functions remain constant over systems with different configurations while underlying devices can change.

#### 4.2.3 Other Values

Other modules also expose accessible data, for example the script engine provides variables for starting, stopping, pausing, and reading the script status.

### 4.3 Value Tree Content

Each tree node can contain child nodes and one of two content types:

| Type | Description |
|---|---|
| **Value** | A measured or controllable value (e.g., still temperature) |
| **Call** | A callable function (e.g., start script) |

Types are defined as dot-separated strings, e.g., `Value.Number.Float.Unit`.

#### 4.3.1 Value Content

A Value is a communication channel between modules and the value tree. It uses **samples** (value + timestamp + status + exception metadata).

Each value maintains two samples:
- **Latest sample:** The most recent sample (may be invalid).
- **Latest valid sample:** The most recent sample with a valid status.

##### 4.3.1.1 Samples

Each sample contains:

| Field | Description |
|---|---|
| **Value** | The data stored (may be absent on failure) |
| **Timestamp** | Time the value was received (Unix timestamp) |
| **Status** | Status code indicating data validity |
| **Exception** | Java exception information (if operation failed) |

**Value Sample Status Codes:**

| Status Code | Valid | Description |
|---|---|---|
| `SYNCHRONIZED` | Yes | Data is valid and synchronized with the target device. |
| `INVALID` | No | Data is not valid (e.g., read failed or value not read from device). |
| `CHANGED` | Yes | Value changed on module side but not yet updated to device. |
| `DISCONNECTED` | No | Device is disconnected; no data available. |
| `INDEPENDENT` | Yes | Data not bound to any physical device; fully managed by the program. |
| `QUEUED` | Yes | Value is waiting to be updated to the device. |

##### 4.3.1.2 Reading and Writing

- **Write:** Request relayed to the underlying module; value is updated on completion.
- **Read (latest):** Returns the most recent sample, which may be invalid.
- **Read (latest valid):** Returns the most recent valid sample within the maximum age.

##### 4.3.1.3 Use Patterns

Three common value patterns:

**Local values:** Managed entirely within the module. Only use the `INDEPENDENT` status.

**Immediate device values:** Target is an external device (e.g., serial cable). The module actively polls the device and uses `SYNCHRONIZED`, `DISCONNECTED`, and `INVALID` statuses. Supports maximum age for masking brief disconnections.

**Delayed device values:** Settings read and written in batches. When a value is written, it transitions to `CHANGED`, then `QUEUED` when the update sequence starts, and finally back to `SYNCHRONIZED` when confirmed.

##### 4.3.1.4 Value Types

| Type | Description |
|---|---|
| `Value.String` | Textual content; supports read and write. |
| `Value.Number` | Base numeric type; provides compatibility between numeric subtypes. |
| `Value.Number.Integer` | Integer values (e.g., channel indices). |
| `Value.Number.Integer.Enumeration` | Integer with a list of named values (e.g., `0=Off, 1=On, 2=Error`). |
| `Value.Number.Float` | Double-precision floating point (e.g., measured data, calibration values). |
| `Value.Number.Float.Unit` | Float with unit information; supports unit/magnitude conversion (e.g., millikelvin, Fahrenheit). |

#### 4.3.2 Call

The **Call** content type implements function calls from the value tree (e.g., start/stop scripts). Calls can accept parameters and return values. A completion notification (success or error) is sent when the task finishes.

---

## Appendix I: API Reference

### HTTP Endpoints

---

#### `system`

**Description:** Provides general information about the system (name, version). Supports **GET** only.

**URL pattern:**
```
http://address:49099/system/?param1=value1
```

**Parameters:**

| Parameter | Description |
|---|---|
| `key` | API key for authentication |
| `prettyprint` | If `1`, output is indented for readability |

**Response structure:**

```json
{
  "data": {
    "system_name": "string",
    "product_type": "string",
    "sw_name": "string",
    "sw_version": "string",
    "system_version": "string",
    "api_version": "string"
  }
}
```

**Example 1 – Get system information:**

- Request type: `GET`
- URL: `http://localhost:49099/system/?prettyprint=1`

```json
{
  "data": {
    "system_name": "Very Cool Bluefors system",
    "product_type": "kide-ci1",
    "sw_name": "CS1",
    "sw_version": "2.4.3",
    "system_version": "2.4.3",
    "api_version": "api-2.4.3"
  }
}
```

---

#### `values`

**Description:** Provides access to the value tree. Supports **GET** (read) and **POST** (update/call).

**URL pattern:**
```
http://address:49099/values/endpoint/path/?param1=value1
```

**Parameters:**

| Parameter | Description |
|---|---|
| `fields` | Semicolon-separated list of field names to include in response |
| `key` | API key for authentication |
| `prettyprint` | If `1`, output is indented for readability |
| `recursion` | Recursion depth for child nodes; `-1` = unlimited (default). GET only. |
| `style` | Response structure: `flat` (default) or `tree`. GET only. |
| `must_exist` | If `1`, checks existence of all nodes before executing. Default `0`. POST only. |
| `wait_response` | If `1`, waits for commands to complete before returning. Default `1`. POST only. |

**Response structure (style=tree):**

```json
{
  "data": {
    "name": "string",
    "type": "string",
    "children": {},
    "content": {}
  }
}
```

**Response structure (style=flat):**

```json
{
  "data": {
    "<path.to.node>": {
      "name": "string",
      "type": "string",
      "content": {}
    }
  }
}
```

**Content structure for value:**

| Field | Type | Description |
|---|---|---|
| `latest_valid_value` | Object | Latest valid sample (value, outdated, date, status, exception) |
| `latest_value` | Object | Latest acquired sample (same structure) |
| `maximum_age` | Integer | Maximum age in milliseconds |
| `lockable` | Boolean | Whether the value can be locked |
| `read_only` | Boolean | Whether the value cannot be written |
| `owner` | String | Component responsible for updating the value |
| `value` | String | Present only in POST; used to set value |

**Content structure for call:**

| Field | Type | Description |
|---|---|---|
| `parameters` | Array | Parameters the function call expects |
| `description` | String | Short description of the call |
| `call` | Integer | Present only in POST; set to `1` to invoke the call |

**Example 1 – Read flowmeter value:**

- Request type: `GET`
- URL: `http://localhost:49099/values/mapper/bf/flow?prettyprint=1`

```json
{
  "data": {
    "name": "mapper.bf.flow",
    "type": "Value.Number.Float",
    "content": {
      "read_only": true,
      "maximum_age": 5000,
      "lockable": false,
      "locked": true,
      "owner": "driver.vc.flow",
      "latest_valid_value": {
        "value": "1.23",
        "outdated": false,
        "date": 1631106116076,
        "status": "SYNCHRONIZED",
        "exception": ""
      },
      "latest_value": {
        "value": "1.23",
        "outdated": false,
        "date": 1631106116076,
        "status": "SYNCHRONIZED",
        "exception": ""
      }
    }
  }
}
```

**Example 2 – Open V1, close V2:**

- Request type: `POST`
- URL: `http://localhost:49099/values/?prettyprint=1&fields=name;value;status`
- Request body:

```json
{
  "data": {
    "mapper.bf.valves.v1": { "content": { "value": "1" } },
    "mapper.bf.valves.v2": { "content": { "value": "0" } }
  }
}
```

**Example 3 – Run script and access non-existent value (without must_exist):**

- Request type: `POST`
- URL: `http://localhost:49099/values/?prettyprint=1`
- Request body:

```json
{
  "data": {
    "does.not.exist": { "content": { "value": 1 } },
    "script.legacy.run": { "content": { "call": 1 } }
  }
}
```

---

#### `resources`

**Description:** Retrieves static resources used by Control Software (e.g., UI layout files and assets). Supports **GET** only.

**Parameters:**

| Parameter | Description |
|---|---|
| `key` | API key for authentication |

**Example 1 – Get main UI layout:**

- URL: `http://localhost:49099/resources/layout.xml`

```xml
<ui>
  <uimodule order="1" include="frontpanel.xml" />
  <uimodule order="2" include="plots.xml" />
  ...
</ui>
```

---

#### `notifications`

**Description:** Provides access to system notifications. Supports **GET** only.

**URL:** `http://address:49099/notifications/`

**Parameters:**

| Parameter | Description |
|---|---|
| `key` | API key for authentication |
| `prettyprint` | If `1`, output is indented for readability |

**Response structure:**

```json
{
  "data": {
    "notifications": [
      {
        "title": "string",
        "message": "string",
        "type": "debug|info|warning|error",
        "severity": "low|medium|high",
        "seen": true,
        "persistent": true,
        "date": 1656331428335,
        "id": "uuid",
        "source": "string",
        "version": 3,
        "disposed": false
      }
    ]
  }
}
```

---

#### `command`

**Description:** Query and execute predefined scripts by name.

**URL:** `http://address:49099/command/`

**GET** – Retrieve available command names and current script status:

```json
{"data":{"commands":["cooldown","warmup","condense","test"],"status":[0]}}
```

Script execution status codes: `0=stopped, 1=running, 2=paused, 3=error, 4=misc, 5=syntax error`

**POST** – Launch a named script:

```
POST /command/?name=cooldown
```

Response:

```json
{"data":{"Running script":1}}
```

If a script is already running:

```json
{"data":{"Error":"Running the script failed: Script must be stopped before making changes."}}
```

---

### WebSocket Endpoints

---

#### `ws/system` – System Information

Supports only the **read** command.

##### `read`

Returns general system information.

**Response data fields:**

| Field | Description |
|---|---|
| `system_name` | Name given to the system by the user |
| `system_version` | Version in format X.Y.Z (X=major, Y=minor, Z=patch) |
| `api_version` | API version (mirrors system_version) |

**Example 1 – Read system info via secure WebSocket:**

- URL: `wss://localhost:49098/ws/system/?key=0352ebaa-6de5-4f1d-9091-17678d11dfd6`

Sent:
```json
{
  "command": "read",
  "id": "2b64707c-17b0-11ec-827e-14dae904baea"
}
```

Received (RECEIVED):
```json
{
  "id": "2b64707c-17b0-11ec-827e-14dae904baea",
  "status": "RECEIVED",
  "data": { "command": "read", "id": "2b64707c-17b0-11ec-827e-14dae904baea" }
}
```

Received (SUCCEEDED):
```json
{
  "id": "2b64707c-17b0-11ec-827e-14dae904baea",
  "status": "SUCCEEDED",
  "data": {
    "system_name": "",
    "system_version": "1.4",
    "api_version": "1.4"
  }
}
```

---

#### `ws/values` – Values

Provides access to value tree data. Supports reading, writing, and subscribing to changes.

**Commands:**

| Command | Description |
|---|---|
| `read` | Read data from value tree node(s) |
| `set` | Update values or call methods |
| `listen` | Subscribe to changes in value tree nodes |
| `unlisten` | Stop listening to value tree nodes |
| `status` | Return list of values currently being listened to |

---

##### `read`

Returns a single node from the value tree.

**Command data:**

| Field | Type | Description |
|---|---|---|
| `target` | String | Target node path |
| `style` | String | `tree` (default) or `flat` |
| `recursion` | Integer | Recursion depth; `0` = target only, `-1` = infinite |

**Example 1 – Read current flow value:**

Sent:
```json
{
  "command": "read",
  "id": "6352827e-1ac3-11ec-bdf6-14dae904baea",
  "data": { "target": "mapper.bf.flow" }
}
```

Received (SUCCEEDED):
```json
{
  "id": "6352827e-1ac3-11ec-bdf6-14dae904baea",
  "status": "SUCCEEDED",
  "data": {
    "name": "mapper.bf.flow",
    "type": "Value.Number.Float",
    "content": {
      "read_only": true,
      "maximum_age": 5000,
      "lockable": false,
      "locked": true,
      "owner": "driver.vc.flow",
      "latest_valid_value": {
        "value": "1.23",
        "outdated": false,
        "date": 1632218701084,
        "status": "SYNCHRONIZED",
        "exception": ""
      },
      "latest_value": {
        "value": "1.23",
        "outdated": false,
        "date": 1632218701084,
        "status": "SYNCHRONIZED",
        "exception": ""
      }
    }
  }
}
```

**Example 2 – Read script run command info:**

Sent:
```json
{
  "command": "read",
  "id": "acf0e246-1ac7-11ec-bdf6-14dae904baea",
  "data": { "target": "script.legacy.run" }
}
```

Received (SUCCEEDED):
```json
{
  "id": "acf0e246-1ac7-11ec-bdf6-14dae904baea",
  "status": "SUCCEEDED",
  "data": {
    "name": "script.legacy.run",
    "type": "Method",
    "content": {
      "parameters": [],
      "description": "Runs the script"
    }
  }
}
```

---

##### `set`

Updates values or calls methods in the value tree.

**Command data:**

| Field | Type | Description |
|---|---|---|
| `must_exist` | Integer | If `1`, checks node existence before executing. Default `0`. |
| `data` | Object | Flat list of tree nodes to set |

For each node:
- `value` (String): Updated value (for value nodes only)
- `call` (Integer): Set to `1` to invoke a method
- `parameters` (Array): Parameters for the method call

**Example 1 – Close V1, open V2:**

Sent:
```json
{
  "command": "set",
  "id": "4014ffe4-3729-11ec-974d-14dae904baea",
  "data": {
    "must_exist": 1,
    "data": {
      "mapper.bf.valves.v1": { "content": { "value": 0 } },
      "mapper.bf.valves.v2": { "content": { "value": 1 } }
    }
  }
}
```

---

##### `listen`

Starts listening to changes in one or more values. Sends `NOTIFICATION` events when values change.

**Command data:**

| Field | Type | Description |
|---|---|---|
| `target` | String | Target node in the value tree |
| `all` | Boolean | If `true`, notify on all updates including same-value timestamp changes |
| `recursion` | Boolean | If `true`, recursively listen to all child nodes. Default: `false` |

**Notification event:** `changed` – fired each time value or status is updated.

**Example 1 – Listen to flow value changes:**

Sent:
```json
{
  "command": "listen",
  "id": "be4b7d90-3bc8-11ec-84e8-14dae904baea",
  "data": { "target": "mapper.bf.flow" }
}
```

Notification received:
```json
{
  "id": "be4b7d90-3bc8-11ec-84e8-14dae904baea",
  "status": "NOTIFICATION",
  "event": "changed",
  "data": {
    "mapper.bf.flow": {
      "name": "mapper.bf.flow",
      "type": "Value.Number.Float",
      "content": { ... }
    }
  }
}
```

---

##### `unlisten`

Stops listening to changes in one or more values.

**Command data:**

| Field | Type | Description |
|---|---|---|
| `target` | String | Target node. If omitted, matches all nodes for the given ID. |
| `recursion` | Boolean | If `true`, stops listening to the node and all child nodes. |
| `id` | String | Command ID used when setting the listener. If omitted, applies to all listeners matching the target. |

---

##### `status`

Returns a list of all nodes currently being listened to.

**Response fields per node:**

| Field | Type | Description |
|---|---|---|
| `status` | String | `OK` / `UNLINKED` (target does not exist) / `WRONG_TYPE` |
| `all` | Boolean | Refer to `listen` command parameter `all` |
| `id` | String | Unique identifier used when adding this listener |
| `content` | Object | Identical to `read` command tree node contents |

---

#### `ws/notifications` – Notifications

**URL:** `http://address:49099/ws/notifications/`

Allows subscribing to system notifications and their changes.

**Parameters:**

| Parameter | Description |
|---|---|
| `key` | API key for authentication |

**Response data fields:**

| Field | Description |
|---|---|
| `id` | Unique message ID |
| `status` | Always `NOTIFICATION` |
| `title` | Message title |
| `message` | Message text |
| `type` | `debug`, `info`, `warning`, or `error` |
| `severity` | `low`, `medium`, or `high` |
| `seen` | Whether message was already read in UI |
| `persistent` | Whether message is permanent |
| `date` | Timestamp in POSIX format |
| `source` | Message source (e.g., device code) |
| `version` | Message version (incremented with each change) |
| `disposed` | Whether message was deleted |
| `event` | Always `notification` |

**Example:**

```json
{
  "id": "a8f44b2a-7d00-462c-bbca-3e5a84806cd4",
  "status": "NOTIFICATION",
  "data": {
    "title": "Bftc2 is not connected",
    "message": "The program is unable to communicate with th...",
    "type": "error",
    "severity": "high",
    "seen": true,
    "persistent": false,
    "date": 1656332524519,
    "id": "a8f44b2a-7d00-462c-bbca-3e5a84806cd4",
    "source": "bftc2",
    "version": 3,
    "disposed": false
  },
  "event": "notification"
}
```

---

### Error Codes

#### General Errors

| Code | Name | Description |
|---|---|---|
| 1001 | Parameter error | One or more parameters in the request were incorrect or missing. |
| 1002 | Invalid JSON | JSON supplied in API request is not valid JSON. |
| 1003 | Missing JSON | The request does not contain the mandatory JSON content. |
| 1005 | JSON not required | The request contains JSON data, but the endpoint does not use it. |
| 1008 | Path parameter not supported | The specified path is not supported by this endpoint. |
| 10012 | Method not supported | The endpoint does not support the used method. |
| 10013 | Data error | Data supplied in the request is incorrect. |
| 100111 | Unknown error | The program reported an error with unknown error code. |

#### Value Errors

| Code | Name | Description |
|---|---|---|
| 3001 | Value not found | Value tree node not found. |
| 3003 | Read only | Value is read only. |
| 3005 | Value edit error | Failed to update the value. |
| 3006 | Wrong type | The target value tree node content is of an unexpected type. |
| 3007 | Target value has no content | The target value tree node does not have any content. |
| 3008 | Method call exception | Calling method caused an exception. |
| 6001 | Command not found | WebSocket command not found. |

#### Server Errors

| Code | Name | Description |
|---|---|---|
| 2001 | No key supplied | Access key is needed for accessing this resource. |
| 2002 | Content does not exist | Requested content does not exist. |
| 2003 | Access denied | Supplied key has no rights to the content. |
| 2004 | Method type error | HTTP method is not supported. |
| 2005 | Fatal WebSocket error | An unexpected exception occurred in the WS connection. Connection is closed. |