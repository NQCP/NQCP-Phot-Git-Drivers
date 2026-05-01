# Technical Reference: Remote Access Control API Gen. 1

**Document ID:** BF1000-1234517327-83 Version 3.0, en-US  
**Date:** October 21, 2024  
**Classification:** CONFIDENTIAL  
**Copyright:** © 2024 Bluefors Oy. "Bluefors" and "Cool for Progress" are registered trademarks of Bluefors Oy. All rights reserved and unauthorized use prohibited.

---

## Disclaimer

The information contained in this document is effective as of the publication date. Bluefors Oy reserves the right to make changes to the product and information contained in this document relative to the specifications, features, and design of the product.

The information contained in this document covers a wide range of applications and may not specifically apply to your equipment layout or custom setup. Contact us directly (support@bluefors.com) if you have any questions about the specifications or any other content contained in this document.

The information contained in this document is believed to be accurate and reliable as of the time of its publication. However, Bluefors does not accept any responsibility or liability (financial or otherwise) that may result from the use or misuse of the information contained in this document.

Bluefors reserves the right to add, change, modify or delete any or all information contained herein without prior written notice. Revisions to this document may be issued at the time such changes and/or deletions occur.

This document and the information contained in it are confidential information of Bluefors Oy and may not be reproduced, shared, or otherwise disclosed without Bluefors Oy's prior written consent.

### Contact Information

**Bluefors Oy**  
Arinatie 10  
00370 Helsinki  
Finland  
support@bluefors.com  
+358 9 5617 4800

---

## Table of Contents

- [1 Introduction](#1-introduction)
  - [1.1 Overview of the user instructions](#11-overview-of-the-user-instructions)
  - [1.2 Related information](#12-related-information)
  - [1.3 Terms and abbreviations](#13-terms-and-abbreviations)
  - [1.4 Symbols and conventions](#14-symbols-and-conventions)
  - [1.5 Customer service and support](#15-customer-service-and-support)
  - [1.6 Warranty](#16-warranty)
- [2 Safety](#2-safety)
  - [2.1 Safety message descriptions](#21-safety-message-descriptions)
  - [2.2 Safety symbol color descriptions](#22-safety-symbol-color-descriptions)
  - [2.3 Safety symbols](#23-safety-symbols)
- [3 Control API](#3-control-api)
  - [3.1 Structure and terminology](#31-structure-and-terminology)
  - [3.2 Access protocols](#32-access-protocols)
  - [3.3 Hypertext Transfer Protocol – HTTP](#33-hypertext-transfer-protocol--http)
  - [3.4 WebSocket protocol](#34-websocket-protocol)
  - [3.5 Authentication and security](#35-authentication-and-security)
- [4 Program structure](#4-program-structure)
  - [4.1 High-level design](#41-high-level-design)
  - [4.2 Data flow](#42-data-flow)
  - [4.3 Value tree content](#43-value-tree-content)
- [Appendix I: API Reference](#appendix-i-api-reference)
  - [HTTP Endpoints](#http-endpoints)
  - [WebSocket Endpoints](#websocket-endpoints)
  - [Error Codes](#error-codes)

---

## 1 Introduction

### 1.1 Overview of the user instructions

Bluefors Control Software Gen. 1 is software that is used to control the Bluefors dilution refrigerator measurement systems. Control Software interfaces with and controls the devices that are part of the Control Unit.

There are different types of information products available for the product.

- **User Manual** — Functional description of the product, component descriptions, and operating, maintenance, and troubleshooting instructions. Can also include installation and commissioning instructions.
- **Technical Reference** — Necessary background information and technical details about a subject, such as parameter descriptions and use of scripts and API.

For details about the identification and location of the information products, refer to "Related information".

> **NOTE**  
> These instructions apply to version 2.4.3 and earlier versions of Bluefors Control Software and Control API, Gen. 1.

These instructions are essential for the use of Bluefors Control Software. For safe and proper use of the product, read the instructions before use. Keep them for future reference.

### 1.2 Related information

| Information | ID | Location |
|---|---|---|
| Bluefors Control Software Gen. 1 User Manual | BF1000-1234517327-71 | Available on Bluefors website: https://bluefors.com/support/ |

### 1.3 Terms and abbreviations

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

### 1.4 Symbols and conventions

This section presents symbols and writing conventions that are used in the user instructions. Symbols used with safety messages are presented in "Safety symbols".

A note is used to indicate additional important information to the reader.

> **NOTE**  
> Example of a note.

### 1.5 Customer service and support

Bluefors support includes reasonable telephone and email customer service during normal business hours (Finland). Support is provided by experienced technical personnel.

For support documents and downloadable software, refer to Bluefors Support website: https://bluefors.com/support.

For technical issues or questions related to the system operation, contact support@bluefors.com or +358 9 5617 4800.

For sales-related issues or questions, contact sales@bluefors.com or +358 9 5617 4800. For global sales contact information, refer to https://bluefors.com.

> **NOTE**  
> In case of emergency or accidents, call your local emergency services.

### 1.6 Warranty

For warranty information, refer to the Bluefors warranty statement.

---

## 2 Safety

### 2.1 Safety message descriptions

> **⚠ DANGER**  
> *Type of hazard*  
> Danger indicates an imminently hazardous situation which, if not avoided, will result in death or serious injury.

> **⚠ WARNING**  
> *Type of hazard*  
> Warning indicates a potentially hazardous situation which, if not avoided, could result in death or serious injury.

> **⚠ CAUTION**  
> *Type of hazard*  
> Caution indicates a hazardous situation which, if not avoided, could result in minor or moderate injury.

> **NOTICE**  
> Notice indicates a message related to property damage only. There is no obvious risk of personal injury.

### 2.2 Safety symbol color descriptions

| Color | Meaning |
|---|---|
| Yellow | Indicates a warning |
| Red | Indicates a prohibition |
| Blue | Indicates a mandatory action |

### 2.3 Safety symbols

| Symbol | Description |
|---|---|
| 📖 | Refer to instruction manual/booklet |
| ❗ | General mandatory action sign |

---

## 3 Control API

The Control API provides remote access to the software. It supports HTTP and WebSocket based APIs with and without encryption.

All the requests and commands in the API use JSON (https://www.json.org/) as a format for the content.

> **NOTICE**  
> Only use Control Software for the intended purpose it has been designed for.

> **NOTICE**  
> Control Software interfaces directly with the operation of the dilution refrigerator. You are responsible for the correct performance of any operation.

> **NOTICE**  
> Always read and follow the instructions, safety information, and warnings stated in the instructions. Incorrect action or operation may cause critical malfunction or system breakdown.

### 3.1 Structure and terminology

#### 3.1.1 Addressing

The resources in the API are referred by URIs, which are defined in RFC 3986 (https://datatracker.ietf.org/doc/html/rfc3986). These instructions follow the same terminology when referring to URI components.

```
http :// localhost:1234 / values ? filter=value # something
ws   :// localhost:1234 / ws/values

scheme    authority        path     query
```

- **Scheme:** The scheme defines the used protocol. In this case it is either `http`, `https` (secure HTTP), `ws` (WebSocket), or `wss` (secure WebSocket).
- **Authority:** The authority defines the host name and protocol number in form `<hostname>:<port>`.
- **Path:** The path defines the location of the resource in the server.
- **Query:** The query part contains additional data which is passed to the resource found in the path. In this case, this is a list of parameters separated into key-value pairs that are separated by commas, for example, `<param1>=<value1>, <param2>=value2 ..., <paramN>=<valueN>`.
- **Fragment:** The fragment part of a http URI is not used in this API.

#### 3.1.2 Services

The Control API provides a variety of features for different purposes. These features are divided into services by function, for example, general system information or value data access.

The services are called **endpoints** and they are identified by the first part of a URI path.

All HTTP endpoints are identified by the first part of the path, for example, `http://localhost:1234/values/driver/`. The first part of the path that identifies the endpoint is called the **endpoint name**. The rest of the path is called the **endpoint path** and it is used for identifying a resource within the endpoint.

All WebSocket endpoints are identified by the first two parts of the path. The first part is always `ws` followed by the WebSocket endpoint name, for example `http://localhost:1234/ws/values`. As with HTTP, the rest of the path is the endpoint path. However, an endpoint path is rarely used with WebSocket endpoints because the connection is bidirectional and it allows interaction with multiple resources, for example, subscribing to listening changes in multiple values.

### 3.2 Access protocols

The API supports HTTP and WebSocket with (HTTPS and Secure WebSocket) and without encryption. The HTTP-based API is easy to use. However, it is a request-based protocol, and the server cannot notify the client when new data is available, so you must ask for new data, that is, poll the data. The WebSocket protocol establishes a continuous bidirectional connection, allowing you to subscribe for listening changes in the data. Instead of asking for changes, the server automatically sends new data when it is available.

> **NOTE**  
> Both protocols provide access to the same data. If a simpler HTTP connection is sufficient, there is no need to have support for WebSocket.

### 3.3 Hypertext Transfer Protocol – HTTP

Hypertext Transfer Protocol (HTTP) is well-known from delivering web pages, but it is also commonly used in machine-to-machine communication. Part of it can also be experimented with using any web browser, which makes it an easy choice.

The HTTP protocol is defined in the RFC 2616 standard (https://datatracker.ietf.org/doc/html/rfc2616). The secured connection (HTTPS) is defined in RFC 2818 (https://datatracker.ietf.org/doc/html/rfc2818).

#### 3.3.1 Quick start

The simplest way of communicating with the API is to use the HTTP or HTTPS protocol for communication.

This part of the API uses simple client-initiated request-response communication.

As defined in Addressing, HTTP endpoints use a URI path to identify the endpoint and resource in it.

##### 3.3.1.1 Example

One advantage with the HTTP API is that it can be tested with any web browser. For example, the flow sensor can be read in this way.

1. Make sure that you have the Bluefors control card device added and connected to either real or simulated hardware. This works even without one, but it makes more sense to get the actual reading out. Select the **Configuration** icon.
2. Select the **API** tab.
3. Make sure that the HTTP/WebSocket port is **49099**. Turn on the **Enable API** toggle switch.
4. Turn on the **Enable HTTP and WebSocket** toggle switch.

*(See Figure 1: Enabling the API and HTTP/WebSocket)*

5. Open a web browser and navigate to the following URL: `http://localhost:49099/values/mapper/bf/flow`.
6. The browser now shows a JSON response that contains the flow with some additional data.

*(See Figure 2: Accessing flowmeter value in Control API by using a web browser)*

The only limitation is that web browsers normally only allow getting of the pages using the *GET* command. However, the standard also defines the POST, *PUT*, and *DELETE* commands, which are also used by the API. POST is used by the web browser when sending data to server, for example, filling a form in a web page or uploading a file, but it cannot be directly accessed without additional tools or extensions.

#### 3.3.2 HTTP protocol

The protocol description has been simplified to contain only the relevant details that matter when using a library to communicate with the program. For example, the packets can also contain, for example, cookies and headers, and the content can be split into multiple packets, which are ignored by the Control API or are transparent to the user.

The communication is request-response based, which means that you send a request, and the server sends a response. The actual data transferred back is the response content, while the request content is the path in the URL and the query parameters defined in the URL. The protocol uses four different commands: **GET**, **POST**, **PUT**, and **DELETE**. Each of these commands has a specific purpose, and while these are used differently in different APIs, this program follows the standard convention. The command type also defines which data it accepts, for example, the **GET** command only has content in response while **POST** and **PUT** allow content in both request and response.

- **GET**: Returns the resource or data, for example, static resource or value in the value tree
- **POST**: Updates the data (this is only supported on data that can be changed, for example, writeable values)
- **PUT**: Adds data (this is currently not used, but can be used, for example, for adding a device)
- **DELETE**: Deletes data (like PUT, this is currently not used).

With all endpoints, the endpoint path is used for identifying the resource in the endpoint, for example, a specific value, or a branch with multiple values in the value tree.

The query parameters contain additional information, for example, the API key for identification or formatting the data to be returned.

Requests contain content only with POST and PUT commands. The request content for the POST command contains an updated version of the data. The format is the same as what was received with the GET command. PUT works similarly, but it can be used for adding new data, for example device nodes to a device list.

The response content always contains the data being requested or updated. If the data is updated, the response contains the data immediately after the operation has been started, but it is good to note that the data may have not been updated yet.

### 3.4 WebSocket protocol

WebSocket allows bidirectional connection between the client and the server and has been designed to enable bidirectional communication with web applications. The WebSocket protocol is defined in RFC 6455 (https://tools.ietf.org/html/rfc6455).

Control Software also provides WebSocket support. The HTTP API can be used for requesting the data, that is, asking whether new data is available. To overcome this limitation, the API also supports the WebSocket protocol.

While HTTP is request-based, WebSocket establishes a continuous bidirectional stream. When a connection is established, it is possible to send and receive packets asynchronously.

As with HTTP API, it is possible to read and set values, but also subscribe to listening changes in values. If the data is being listened to, the server asynchronously sends updates to the client when the data changes.

The listened values are unique to each connection, so it is possible to establish multiple connections for different purposes. When the connection is disconnected, all connection-specific listeners are cleared.

This section defines the communication scheme shared by all commands. For command-specific details, refer to Appendix I.

#### 3.4.1 Starting the connection

As defined in Services, the WebSocket services are accessed through paths that start with `ws` followed by the endpoint name.

If an access key is needed, it can be specified as a query parameter `key`.

For example, `wss://localhost:49099/ws/values/?key=00000000-1111-2222-3333-444444444444` would refer to Secure WebSocket endpoint "values" with an API key for authentication.

If access is denied, an HTTP response with the code 503 is returned.

#### 3.4.2 Communication scheme

The WebSocket connection is a bidirectional pipe in which the client or server can send data at any time. The communication is divided into packets. Each data packet is a complete JSON object. A packet in this context refers to a complete piece of data, that is, JSON object sent through the connection. WebSocket traffic is also divided into packets, which may or may not follow the same structure, but this protocol level splitting of messages should not be confused to this.

Whenever the server sends data, the client should receive data until it has received a full JSON object. The same applies for packets sent by the client. Whenever the client sends a packet, it should send the data as a full JSON packet, which is complete when the whole package has been sent.

While the server and client can both send packets asynchronously at any time, all the packets follow certain rules to keep the traffic under control.

The messages sent by the client are always control commands and they can be sent at any time. The packets sent by the server are either responses to commands started by the client or asynchronous messages that can be related to earlier commands.

##### 3.4.2.1 Data flow

The normal data flow in the endpoint follows the request-response pattern. Whenever the client sends a command, the server responds. The response is in two parts. For all commands, the server first sends a response with the status `RECEIVED` to notify that it has received the command and started to process it. If the command is processed successfully, the server sends a response with status `SUCCEEDED` containing the data.

Packets sent by the server that are related to a specific command that was sent are connected to it by an ID. When the server sends an initial response to a command, it contains an ID, which is automatically generated, and it remains constant over the whole communication. Depending on the command, the subsequent asynchronous notifications that are sent can contain the ID. The user can also supply an ID that will be used instead of a generated one. The use of an ID enables multiple operations to be in progress at the same time.

In addition, the server can send asynchronous events with the status `NOTIFICATION`. The server can send them at any time, for example, because of unexpected general conditions that must be notified about, or bound to a specific command, for example, starting to listen to changes in a specific value. All events bound to a command use the same ID as the command that they are related to. If no command is involved, the ID does not exist.

> **NOTE**  
> Some endpoints may deviate from the standard data flow. The deviations are described in the corresponding sections of the endpoint reference.

At any part of the command execution process, or in response to a general error condition, an error message can be sent as a response to a command, or asynchronously. The error packets are identified by the `ERROR` status. The command-related errors have the command-specific ID except if parsing the ID from the initial failed packet. If an error message is received, there are no further messages related to the command. For example, if `ERROR` is received instead of `RECEIVED`, the command is stopped, and the server does not send any further `RECEIVED` or `SUCCEEDED` responses in the same command chain with the same ID.

However, it is guaranteed that the server responds with `RECEIVED` and eventually `SUCCEEDED` or `ERROR` in place of either of them.

##### 3.4.2.2 Packet structure

All packets are JSON objects with the same basic structure.

There are four types of packets: commands, success responses, error responses, and asynchronous events.

**Commands**

Each command can contain up to three JSON elements.

- **id**: This is a unique string identifier for binding all elements of a transaction together. This is optional. If not specified, it is generated. It must be composed from hexadecimal numbers, and it can contain the hyphen (`-`) and underscore (`_`) characters, for example, `0123-4567_89ab-cdef`.
- **command**: This is a command name that defines the action to take, for example, `set`, `read`, or `listen`.
- **data**: This is a command-specific payload. Also, this is a JSON object, which has a command-specific structure.

**Success responses**

The server responds to successful commands with one or more response packets, which have the following JSON elements.

- **id**: This is a unique string identifier for binding elements of a transaction together.
- **status**: A status indicates the status and condition of the command execution. The successful responses have either a `RECEIVED` or `SUCCEEDED` status.
- **data**: This is a JSON object containing the actual packet payload, which is specific to a command.

**Error responses**

If there is a failure in some part of the command, an error is returned. Instead of supplying the data, an error code is returned.

- **id**: This is a unique string identifier for binding elements of a transaction together. If the error is a response to a general condition, the ID does not exist.
- **status**: The status indicates the status and condition of the command execution. This is always `ERROR` for error messages.
- **code**: This is a numeric code indicating the error type.
- **description**: This is a human-readable explanation of the error code.
- **details**: The details are in the form of a JSON object containing additional command-specific data, for example the offending payload.

**Asynchronous events**

The server can send asynchronous events at any time.

- **id**: This is a unique string identifier for binding elements of a transaction together. If the notification is a response to a general condition rather than a specific command, the ID does not exist.
- **event**: This is a command-specific type of event describing the purpose, for example, value update or disconnect.
- **status**: The status indicates the type of the message, which, for asynchronous events, is `NOTIFICATION`.
- **data**: This is a JSON object containing the actual packet payload, which is specific to the event-type notification and the command that it is related to.

### 3.5 Authentication and security

The server provides lightweight security mechanisms to provide access control for the server.

The server has different ports for unencrypted and secured connections. By default, port **49099** is used for unencrypted connections and **49098** is used for secure connections.

The unencrypted port is only accessible from the same computer to make it easier to use the API from other programs. However, it is inherently insecure to use it with external services. The encrypted port is open for external communication.

Both connections can use the access keys for authentication.

The program has been designed to be used in an internal network and protected by a firewall, but it supports and fulfills certain security practices to reduce the attack surface. Obey good security practices because there is always a risk of misconfiguration or security breach even in a properly set up environment.

#### 3.5.1 Access keys

The server uses access keys to grant access to the server. The API configuration includes a list of generated access keys and a list of endpoints. The keys can be configured to grant or deny access to each endpoint and operation type separately, for example, by only reading values.

The key list also has a special key called `<unauthenticated>` that can be used for controlling access without a key. Only unencrypted connections allow unauthenticated access.

A secure connection does not allow unauthenticated connections, and it requires a key as a parameter for both HTTP and WebSocket connections.

A WebSocket connection is continuous, and the operations are done after the connection has been established. Like with HTTP, the key is supplied as a query parameter for WebSocket connections. If the key has been defined and there is a permission for the corresponding endpoint, access is granted. The key permissions are also checked when a command is being run. If the key or permission from the key is removed after establishing the connection, the connection remains open, but all subsequent commands are denied.

#### 3.5.2 Design considerations

When designing services that can be accessible from the internet, it is important not to store the keys in an external client-side application because it can be a risk for the whole security scheme.

It is possible to use the API directly, for example, from a single-page web browser application. However, if the browser communicates directly with the API, the key is stored in the application itself and transmitted to the end user's machine, which can be a risk for the security scheme. In such cases, we recommend using a proxy server, which contains the actual key, and which manages the communication with both the Control Software instances and end users. The proxy server must provide its own session management and access control for end users.

---

## 4 Program structure

### 4.1 High-level design

Bluefors Control Software replaces the old Bluefors ValveControl Software. It provides a simple manual interface for controlling the system with scripting support for automatic tasks.

Internally, the program is a modular measurement framework, and the simple user interface logic is designed to hide unnecessary complexity. However, when using the API, it is necessary to understand internal details.

*(See Figure 3: The layered structure of Control Software)*

The layered structure consists of:

1. **Framework layer** — Module managers, Modules, Value tree, Resource management, Configuration management
2. **Module layer** — Manager types, Specialized modules
3. **Logical layer** — Logical functionality, Set of module instances, Configurations, Resources
4. **User interface layer** — User interface, Defined in resources

#### 4.1.1 Managers and modules

The core functionality of the program is constructed from modules which all take care of certain tasks within the program, for example, communicating with Fast Sample Exchange, writing valve logs, or managing the core user interface.

**Module managers** manage the modules. Each manager takes care of one specific type of module, like device communication drivers or system mappings.

There are the following managers in the standard Bluefors system, which have roles in the control process:

- **driver**: Driver modules manage communication with the devices and provide interfaces to operate them.
- **mapper**: Mapper modules are used for "mapping" driver data to logical names, for example, mapping raw control card relay channels to logical valve names from V1 to V23.
- **script**: Script modules provide modules for running scripted tasks within the program. These can be either fully user-configurable scripts, for example, a Bluefors script available through the user interface, or automatic monitoring of tasks running in the background.
- **general**: General modules provide general purpose features, for example, logging modules or a core system tray user interface.

#### 4.1.2 Value tree

The central structure of the program is the **value tree**. It contains all run-time data in the program, such as measured values, controls, and device configuration. Most of the logic in the program interacts with other value tree nodes.

The value tree follows the same hierarchical structure as modules and managers. Each manager has a branch starting from the root of the tree. Each module can have a branch under the corresponding manager. There is a branch only for a module that needs it. For example, logger modules do not have branches because those modules only receive data and do not provide any.

*(See Figure 4: Example value tree)*

The exact structure of the branch is specific to the module. However, certain types of modules can have fixed common characteristics.

### 4.2 Data flow

All interaction with the measurement and control data is done through the value tree. The whole tree is available to the API and user interface logic. Thus, it is possible to interact with any values provided by the modules. However, there are common patterns about how these are generally managed.

#### 4.2.1 Standard data flow

*(See Figure 5: Typical data flow)*

1. **Hardware** — The physical device provides variables that can be read or controlled.
2. **Control card driver** — Each device driver module provides value tree nodes for interacting with the devices from the program. The device drivers provide a low-level interface to the devices.
3. **Value tree** — Central data structure.
4. **Bluefors system mapper** — Maps raw hardware interfaces to logical structures of the system.
5. **User interface** — Presents the logical structure to the user.

The physical device provides variables that can be read or controlled, for example, measurement data or device configuration. Each device driver module provides value tree nodes for interacting with these from the program. The device drivers provide a low-level interface to the devices. The point is to provide at least part, but usually all, of the device functionality to the program.

The data provided by a device may not represent the logical purpose of it in the program. For example, Bluefors Control Card is a relay control card with up to eight sets of eight outputs. These are numbered from 1.1 to 8.8. The driver module provides the channels as values from `ch11` to `ch88` through the value tree. These can be used for changing the corresponding relays.

However, the logical functionality of the Bluefors system is composed of valves and pumps that the relays control, so it would be impractical to directly control the relays that control them. To mitigate this, Control Software also has mapper modules that map the raw hardware interfaces to logical structures of the system, for example from a relay channel to the valve that it controls. The mappings can be simple links or complex modules with intelligence. The value mappings are an example of a simple mapping in which each relay channel directly maps from one relay to one valve.

As an example of a complex mapping, the temperature controller module provides two heaters: the Mixing Chamber Heater and Still Heater. Both are controlled by two variables: enabled and power. The actual underlying hardware can be either Lake Shore 372 (or 370) or Bluefors Temperature Controller. All of these have refined control over heaters that provide different operation modes, range settings, and so on. The Lake Shore devices also have only a sample heater that can be controlled by power, so the actual power for the second heater must be calculated. Mapping this functionality to one power value requires additional logic to work.

#### 4.2.2 Mapped and driver values

The use of mapped values to control the drivers is the most common dataflow in Control Software. However, you can also control the devices directly. The mapped interface has been designed with simplicity and compatibility in consideration of many configurations. It provides only a small subset of the underlying features of the hardware. For example, all supported temperature control devices provide a rich set of features and fine-grained control over them.

You can access these features directly from the driver modules. Be careful when you use them to prevent interference with the control process, for example, if the temperature control device configuration is changed during the cooldown process.

You can define the configuration and values of the devices in the dedicated device views in the user interface.

> **NOTE**  
> The device drivers provide direct access to all device features but be careful not to interfere with the normal functions of the dilution refrigerator.

> **NOTE**  
> When controlling the system through Control API, remember that the mapped functions remain constant over systems with different configurations while underlying devices and the modules used for controlling them can change.

#### 4.2.3 Other values

While most of the data is accessible directly from drivers or through mapper modules, there are also other modules with accessible data. For example, the Bluefors script engine provides variables for updating, starting, stopping, and pausing the script and reading its status.

The module or module type specifies the use of these values.

### 4.3 Value tree content

The value tree is the central data structure that contains all the data and functions required for normal operation.

Each tree node can contain any number of child nodes. Each node can also have a content type. The content type is the actual value or function that the node represents. Two types of nodes are commonly being used:

- **Value**: Represents any measured or controllable value, for example, a still temperature
- **Call**: A function that can be called, for example, to start the script.

The types are hierarchical. Value and Call are the two main value types, but they are often divided into subtypes. Each subtype layer defines more specific control over it.

The type is defined as a dot-separated string of type specifiers. For example, `Value.Number.Float.Unit` defines that the content type is Value with a subtype of a numeric value with a subtype of a floating point value and with unit information.

For example, any content with the Value type can be set and read as a string. If the type is Number, it can also be set and read as an integer or a floating point number. The floating-point subtype defines that the value is a floating point value and it is treated as such. The unit type also contains information about what unit it is, and it provides functions to present and convert it between different units and magnitude systems.

#### 4.3.1 Value content

Value is a communication channel between the modules and the value tree.

The content of the Value type is a variable that can be read or written to. Instead of managing single values, it uses samples. In addition to value, the sample contains the time of the event, status of the operation, and other metadata. For information about the sample structure, refer to "Samples".

The value has two samples: the **latest** and the **latest valid** sample. This is an important feature when dealing with unreliable data sources. For example, there can be short interruptions in the device communication channels. When there is an interruption, the values are updated accordingly. For example, when showing the values in the user interface, or when running scripts, it is sufficient that there is a recent enough valid reading that can be shown.

If the latest valid value becomes too old, the latest one can be used instead to show the actual status. For example, if the serial line has been disconnected long enough so that the latest value is not reliable enough, the device can be disconnected instead of there being an insignificant interference in communication.

You can read both values. When you write or update the value, instead of providing a full sample, you provide only a value itself. The value is sent to the write function in the underlying module that executes an operation with it and creates a new sample as a result and stores it in the value. The operation can be internal buffering, or the device driver can write it directly to the device.

As the only exception, direct one-to-one links in mapping modules show as normal values, but instead of implementing read and write logic, they transparently send the requests to the target node in the value tree.

*(See Figure 6: Reading and writing of values)*

When you read the value, it reads the value (through mapper link) from the sample stored in the driver value node. When you decide to write the value, it invokes a write operation in the value node, which is passed to the hardware driver and eventually to the hardware. When the value is written, the driver reads back the value and writes the new updated value to the value node, which in turn notifies you about the updated value.

Commonly, drivers also update the values when new data becomes available or at a fixed interval.

##### 4.3.1.1 Samples

The data in values is encapsulated in **value samples**, which also contain metadata about the data. Each value keeps track of the latest sample and the latest valid sample.

The samples are events rather than plain representations of the values. Each change in value, whether it was a disruption in communication or value acquisition, has a result in the sample to be created.

Each sample has the following content:

- **Value**: The data stored in the value (it is possible that the data is not there if there has been a failure in the operation)
- **Timestamp**: The time the value was received
- **Status**: The status code which defines whether the data is valid (refer to Table 5).
- **Exception**: If the operation is not successful, there can be a Java exception in the value data available for further analysis.

**Table 5: Value sample status codes**

| Status code | Valid | Description |
|---|---|---|
| SYNCHRONIZED | Yes | Data is valid and synchronized with the target, usually device. |
| INVALID | No | Data is not valid, for example, if read is not successful or the value is not read from the device. |
| CHANGED | Yes | Value is valid and changed on the module side but not updated to the device yet. This is used, for example, with settings that the user can change but only an explicit request updates them. |
| DISCONNECTED | No | The device is disconnected, and no data is available. |
| INDEPENDENT | Yes | Data is not bound to any physical device and the program updates the data completely. |
| QUEUED | Yes | The value is waiting to be updated back to the device. Changed values are transferred to this status when the update sequence is started and before the values are updated. |

##### 4.3.1.2 Reading and writing

When a value is written, the request is relayed to an underlying module that performs the update. When the operation is completed, it is guaranteed that the value is updated. The updated value represents the status after the update. Sometimes, the value is not the one that was written to it because of an error, rounding, or value out of range.

For reading, there are two different functions to do the task. It is possible to request either the **latest value** or **latest valid value**. The latest value is always the most recent sample provided by the module, which can also be invalid, for example, because it is disconnected. The latest valid value returns the latest value, which is valid. The validity check is done from the sample status. The value also has an attribute **maximum age**, which defines how old samples are still valid.

There can be communication errors which can cause values to be unavailable for a short period of time. For the control process, it is usually sufficient that the latest value that can be used, is recent enough, for example, 5 seconds. The use of the latest valid value makes it possible to mask out minor issues, for example, in communication channels. Sometimes the absolute status is needed. For example, when a value is written and updated, it is important to know what the real result of the operation is.

##### 4.3.1.3 Use patterns

There are three ways in which the values are commonly used in the program.

*(See Figure 7: Local value status transitions, Figure 8: Immediate value status transitions, Figure 9: Delayed value status transitions)*

**Local values**

Local values depend on variables within the actual module. They are used for values that are managed directly by the module, so there is no need to think about synchronization status. Thus, the only sample type used is *independent*.

**Immediate device values**

Immediate device values are values with a target that is outside of the program, for example, in a device connected through a serial cable. The actual value is managed by the module, but the target value is in the device. To reach the value, a connection must be established. The connection can also be unreliable. Taking this into account, the values use the synchronized, disconnected, and invalid status values. When writing to the value, the module relays the value to the device and reads the updated value back. It is possible that the device keeps the value updated by polling it with either regular interval or asynchronous notifications. Regardless, the value is actively kept up to date with the device.

- When a sample with a **synchronized** status is received, it corresponds to the value within the device well.
- When a sample with a **disconnected** status is received, the module has lost connection to the target device and no value can be read.
- When a sample with an **invalid** status is received, the value cannot be read for some other reason. It is possible that the connection is established, and the read command is successful, but the response is unsuccessful.

Unlike local values, immediate device values also have a **maximum age**. This is used for masking out brief disconnections and invalid values. When the latest valid value is requested, a latest sample with a synchronized status and a recent enough timestamp is returned even if there are other samples in between.

**Delayed device values**

Delayed device values have many characteristics with immediate values. The way in which the value is updated, is different. While immediate values are written directly to the device and actively updated from the device, the delayed value is only updated from and to the device. This is because the settings are read and written in batches.

Delayed values also have the same statuses as immediate values. However, since delayed values are not updated with a known interval, the maximum age is not used. When writing to the value it cannot be immediately updated to the device. Instead, the temporary value in the module is updated and a new sample with the status **changed** is created. This denotes that the value is no longer synchronized with the device as the user has changed it, but it is still valid. When a write operation is invoked, the value status changes to **queued**, which means that the value waits to be updated to the device. This does not specify how this is done exactly. It is a module-specific functionality.

Once the update is done, a new sample is read, and the value is set back to a synchronized status. If the value is updated from the device when it is in a changed status, it can be updated back to the value read from the device. This is a partially device-specific feature. For example, when connecting again, the module can keep the changed values as is, even if the values are read from the device. When reconnecting, this prevents the user from losing an in-progress configuration. However, the values are reverted if the user explicitly requested the update.

##### 4.3.1.4 Value types

Currently there are string and numeric values. Numeric values also have subtypes for integers and floating point values. Integers also have a subtype for enumeration value, and floating point values have a subtype for values with units.

**Value.String**

The String type is used for textual content. The only supported operations are reading and writing the content.

**Value.Number**

Number is the main type of all numeric values. It is not used by itself. It provides the compatibility and conversion support between different types of numbers.

**Value.Number.Integer**

The Integer subtype represents any integer. Integers are used explicitly when integer numbers are expected, for example when a channel index is scanned.

**Value.Number.Integer.Enumeration**

Enumeration is a subtype of Integer that inherits all the features of Integer, but also adds a list of possible names to the values. These are commonly used with devices which have status values in which each numeric value has a special meaning, for example, 0 = Off, 1 = On, 2 = Error.

**Value.Number.Float**

The Float subtype represents any floating point number. Internally, this is a double precision floating point number. These are commonly used for measured data and calibration values which do not have a unit.

**Value.Number.Float.Unit**

Unit is a subtype of floating point number that represents a value with unit information. The value with a unit can be converted from and to strings with different similar units and magnitude prefixes, for example, you can request or set the value in millikelvin or Fahrenheit. Internally, the values are always stored in its basic type as a running number.

#### 4.3.2 Call

The Call content type is used for implementing function calls, that is, executing tasks, from the value tree, such as starting or stopping the scripts. When a call is invoked, it does the corresponding task. When the task is completed, you receive a notification about it. The response can either be success or an error if there is a failure in the operation.

It is also possible to pass parameters to function calls, and they can return a value.

---

## Appendix I: API Reference

This appendix contains descriptions of the endpoints provided by the Control API and a list of error codes that the API can return.

---

## HTTP Endpoints

### system

**Description**

```
http://address:49099/system/endpoint/path/?param1=value1&param2=value2
```

The system endpoint provides general information about the system, for example, system name and version. System endpoint supports only the GET operation.

**Endpoint path**

```
http://address:49099/system/endpoint/path/?param1=value1&param2=value2
```

Not used.

**Parameters**

- **key**: API key for authentication
- **prettyprint**: If set to `1`, output is indented and split to multiple lines to improve readability.

**Supported operations**

- **GET**: Retrieves the data

**Response structure**

- **data** (Object): JSON object containing the data
  - **system_name** (String): Name of the system
  - **product_type** (String): Type of the product
  - **sw_name** (String): Name of the software
  - **sw_version** (String): Version of the software
  - **system_version** (String): Version of the Core software
  - **api_version** (String): Version string equivalent to system version

**Example 1** — Requests system information in pretty-printed format.

- Request type: `GET`
- Request URL: `http://localhost:49099/system/?prettyprint=1`
- Request content: `<None>`
- Response content returned by the server:

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

### values

**Description**

```
http://address:49099/values/endpoint/path/?param1=value1&param2=value2
```

The values endpoint provides access to the value tree. This endpoint can be used for retrieving any node or branch from the value tree including the node contents.

The endpoint supports the GET operation for reading data and the POST operation for updating the data and calling functions in the value tree.

Data sent in POST is structured in the same way as the GET operation with flat style, but content only specifies the data being updated.

**Endpoint path**

```
http://address:49099/values/endpoint/path/?param1=value1&param2=value2
```

The endpoint path defines the target value tree node or branch to access. If the request has an effect on multiple nodes, the paths in the request are relative to the path defined in the endpoint path.

With the POST command, the path specified in the URL is ignored because the full path must always be specified in the content.

Note also that it is not guaranteed that the nodes listed in the POST operation are executed in the same order. To guarantee ordering, split the operation to multiple requests.

*(See Figure 10: Endpoint path relation to value tree path)*

**Parameters**

- **fields**: A semicolon-separated list of field names to include in the response. This can be used for filtering out unnecessary information. By default, everything is included.
- **key**: API Key used for authentication
- **prettyprint**: If set to `1`, the output is indented and split to multiple lines to improve readability.
- **recursion**: Sets recursion depth. Defines how many levels of child nodes to include in the output. `-1` is unlimited (default), (only GET).
- **style**: Defines the response structure to be `flat` (default) or `tree`. Flat returns all nodes in a single flat list while in the tree representation each node object has its own list of children (only GET).
- **must_exist**: If `1`, existence of all nodes and their contents will be checked before running any commands. Default is `0` (only POST).
- **wait_response**: If `1`, wait for commands to be completed before returning response. If not set, this returns response immediately after starting the operations. The returned value nodes can be updated. Default is `1` (only POST).

**Supported operations**

- **GET**: Retrieves a value tree node or branch
- **POST**: Updates one or more value nodes in value tree or executes methods

**Response structure when style=tree**

- **data** (Object): Response root node
  - **name** (String): Name of the current node
  - **type** (String): Type of the content
  - **children** (Object): JSON object containing the children as named objects
  - **content** (Object): Node content. This is specific to node type

**Response structure when style=flat**

- **data** (Object): Response root node
  - **\<path.to.node1\>** (Object): Tree node 1
    - **name** (String): Name of the node
    - **type** (String): Type of the content
    - **content** (Object): Node content. This is specific to the node type.
  - **\<path.to.node2\>** (Object): Tree node 2
  - ...
  - **\<path.to.nodeN\>** (Object): Tree node N

**Content structure for value**

- **latest_valid_value** (Object): Latest acquired value that had status of being valid and is not too old
  - **value** (String): Value as a string
  - **outdated** (Boolean): Is value more recent than its maximum age
  - **date** (Integer): Timestamp of the sample as Unix timestamp
  - **exception** (String): May contain related Java exception information if the sample is invalid
- **latest_value** (Object): Latest acquired sample. Structure is like the latest valid value
- **maximum_age** (Integer): Maximum age in milliseconds. Used for defining whether the latest valid sample is still valid.
- **lockable** (Boolean): If true, the value can be locked from exclusive access
- **read_only** (Boolean): If set to true the value cannot be written
- **owner** (String): Component that is responsible for updating the value inside Control Software
- **value** (String): Present only in the POST operation. Used for setting value for value nodes.

**Content structure for call**

- **parameters** (Array): List of parameters that the function call expects. With the POST operation this contains the values of parameters.
- **description** (String): Short description about purpose of the call
- **call** (Integer): Present only in the POST operation. Used for calling the function if the content type is a call.

**Example 1** — Requests flowmeter value in pretty printed format.

- Request type: `GET`
- Request URL: `http://localhost:49099/values/mapper/bf/flow?prettyprint=1`
- Request content: `<None>`
- Response content returned by the server:

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

**Example 2** — Opens valves V1 and closes V2. The output is also in pretty printed format and only the name, value, and status fields are outputted to simplify the output.

- Request type: `POST`
- Request URL: `http://localhost:49099/values/?prettyprint=1&fields=name;value;status`
- Request content:

```json
{
  "data": {
    "mapper.bf.valves.v1": {
      "content": {
        "value": "1"
      }
    },
    "mapper.bf.valves.v2": {
      "content": {
        "value": "0"
      }
    }
  }
}
```

- Response content returned by the server:

```json
{
  "data": {
    "mapper.bf.valves.v1": {
      "name": "mapper.bf.valves.v1",
      "content": {
        "latest_valid_value": {
          "value": "1",
          "status": "SYNCHRONIZED"
        },
        "latest_value": {
          "value": "1",
          "status": "SYNCHRONIZED"
        }
      }
    },
    "mapper.bf.valves.v2": {
      "name": "mapper.bf.valves.v2",
      "content": {
        "latest_valid_value": {
          "value": "0",
          "status": "SYNCHRONIZED"
        },
        "latest_value": {
          "value": "0",
          "status": "SYNCHRONIZED"
        }
      }
    }
  }
}
```

**Example 3** — Runs the script and tries to access non-existent value without enforcing the existence, so all operations are executed, but an error response with all data is returned.

- Request type: `POST`
- Request URL: `http://localhost:49099/values/?prettyprint=1`
- Request content:

```json
{
  "data": {
    "does.not.exist": {
      "content": {
        "value": 1
      }
    },
    "script.legacy.run": {
      "content": {
        "call": 1
      }
    }
  }
}
```

- Response content returned by the server:

```json
{
  "error": {
    "code": 10013,
    "name": "Data error",
    "description": "May be caused by incorrect data or request caused an exception...",
    "query": "POST /values/mapper/bf/valves/",
    "query_data": "{\"data\": {\"script.legacy.run\": {\"content\": {\"call\" : 1...",
    "details": {
      "script.legacy.run": {
        "name": "script.legacy.run",
        "type": "Method",
        "content": {
          "parameters": [],
          "description": "Runs the script",
          "return": null
        }
      },
      "does.not.exist": {
        "error": {
          "id": null,
          "status": "ERROR",
          "code": 3001,
          "description": "Value not found"
        }
      }
    }
  }
}
```

---

### resources

**Description**

```
http://address:49099/resources/endpoint/path/?param1=value1&param2=value2
```

This endpoint can be used for retrieving static resources used by Control Software, for example, user interface layout and other assets.

**Endpoint path**

```
http://address:49099/resources/endpoint/path/?param1=value1&param2=value2
```

The endpoint path is the path to the requested resource.

**Parameters**

- **key**: API key used for authentication

**Supported operations**

- **GET**: Retrieves a resource from given path

**Response structure**

- The requested file is returned as is.

**Example 1** — Requests layout.xml, which is the main layout file for the user interface.

- Request type: `GET`
- Request URL: `http://localhost:49099/resources/layout.xml`
- Request content: `<None>`
- Response content returned by the server:

```xml
<ui>
  <uimodule order="1" include="frontpanel.xml" />
  <uimodule order="2" include="plots.xml" />
  <uimodule order="4" include="script_editor.xml"/>
  <uimodule order="5" include="separator.xml"/>
  <uimodule order="6" include="status.xml"/>
  <uimodule order="7" include="bfbridge.xml"/>
  <uimodule order="9" include="lakeshore.xml"/>
  <uimodule order="10" include="el302p.xml"/>
  <uimodule order="11" include="fse.xml"/>
  <uimodule order="12" include="separator.xml"/>
  <uimodule order="15" include="config.xml" />
</ui>
```

---

### notifications

**Description**

```
http://address:49099/notifications/
```

Provides access to system notifications.

**Methods**

- GET

**Parameters**

- **key**: API key for authentication
- **prettyprint**: If set to `1`, the output is indented and split to multiple lines for better readability.

**Response structure**

- **data** (Array): contains an array of actual notifications
  - (Object): notification object of the following structure:
    - **title**: Message title
    - **message**: Message text
    - **type**: Message type (`debug`, `info`, `warning`, `error`)
    - **severity**: Message severity (`low`, `medium`, `high`)
    - **seen**: Was message already read in UI
    - **persistent**: Is message permanent
    - **date**: Message timestamp in POSIX format
    - **id**: Unique message ID
    - **source**: Message source (for example, device code)
    - **version**: Message version. Increased with every message change.
    - **disposed**: Was message disposed (deleted)

**Example** — Requests current notifications

- Request type: `GET`
- Request URL: `http://address:49099/notifications/?prettyprint=1`
- Request content: `<None>`
- Response:

```json
{
  "data": {
    "notifications": [
      {
        "title": "Maxigauge is not present",
        "message": "The maxigauge device is mandatory for correct...",
        "type": "error",
        "severity": "high",
        "seen": true,
        "persistent": true,
        "date": 1656331428335,
        "id": "36f77422-64bf-401a-8ed0-45eee4d235d0",
        "source": "Maxigauge",
        "version": 3,
        "disposed": false
      },
      {
        "title": "Bftc is not connected",
        "message": "The program is unable to communicate with the...",
        "type": "error",
        "severity": "high",
        "seen": true,
        "persistent": false,
        "date": 1656331418200,
        "id": "9df6dac6-21e0-4076-bfb5-0926d2a99995",
        "source": "bftc",
        "version": 4,
        "disposed": false
      }
    ]
  }
}
```

---

### command

**Description**

```
http://address:49099/command/
```

This endpoint is used to query and execute predefined scripts by name.

Control Software contains product type -specific scripts and some of them have command names in addition to the traditional file names which are visible in the script load window.

**Supported operations**

- **GET**: Retrieves predefined command names from the given path.

**Response structure**

The `data` element has a list of available command names, and the `status` element has the current script execution state. It is an enumeration (0=stopped, 1=running, 2=paused, 3=error, 4=misc, 5=syntax error). For more information about the script engine statuses, refer to "Script engine status" in "Bluefors Control Software Gen. 1 User Manual".

```json
{"data":{"commands":["cooldown","warmup","condense","test"],"status":[0]}}
```

You can launch the execution of a given script by name with POST to endpoint `/command/?name`.

The `name` is a name from the previous list of the available command names.

The response from the script launch:

```json
{"data":{"Running script":1}}
```

The number at the end again corresponds to the script execution status.

If you launch a named script to execution while a script is already running, you get this error message:

```json
{"data":{"Error":"Running the script failed: Script must be stopped before making changes."}}
```

This happens regardless of how the script was started, with this `/command/` API or with the traditional Start button in the user interface.

---

## WebSocket Endpoints

### ws/system – System information

System endpoint can be used for querying general information about the software.

System endpoint supports only the `read` command.

#### read

**Description**

Returns general information about the system.

The server first sends a `RECEIVED` notification as an acknowledgement of receiving the message, followed by a `SUCCEEDED` message that contains the payload.

**Command data**

- `<none>`

**Response data**

- **id()**: ID of message that started the operation
- **status()**: Status of operation
- **data()**: Inner JSON object that contains endpoint specific fields
  - **system_name()**: Name given to the system by the user
  - **system_version()**: Version of the main system given in format X.Y.Z
    - X is major version: Changes in features
    - Y is minor version: Features are the same, but there are minor changes that can break something
    - Z is patch number: Bugs were fixed, but it should be fully compatible (except for potential changes because of fixed buggy features)
  - **api_version()**: Similar to system_version, but reflects the part of the system providing API.

**Notifications**

Not used.

**Example 1** — Connecting to a secure port in local host with specified API key and using custom ID for command

- URL: `wss://localhost:49098/ws/system/?key=0352ebaa-6de5-4f1d-9091-17678d11dfd6`
- Communication:

Sent:

```json
{
  "command": "read",
  "id": "2b64707c-17b0-11ec-827e-14dae904baea"
}
```

Received:

```json
{
  "id": "2b64707c-17b0-11ec-827e-14dae904baea",
  "status": "RECEIVED",
  "data": {
    "command": "read",
    "id": "2b64707c-17b0-11ec-827e-14dae904baea"
  }
}
```

Received:

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

### ws/values – Values

The values endpoint provides access to data in the value tree.

The value tree can contain values and function calls as a content. This endpoint provides same features as its HTTP API counterpart: reading and writing values and calling functions. As WebSocket provides a bidirectional channel between the core and the client, this endpoint also supports listening changes in value data.

The endpoint provides following commands:

- **read**: Read data from value tree node(s)
- **set**: Updates values and call methods in the value tree
- **listen**: Listens one or more value tree nodes for changes
- **unlisten**: Stops listening one or more value tree nodes for changes
- **status**: Returns list of values that are currently being listened for changes.

#### read

**Description**

Returns a single node from the value tree. The resulting data structure contains the value tree node and content.

**Command data**

- **target** (String): Target node from the value tree structure which value is read. The target can be a leaf node or branch node, but only the corresponding node without children is returned.
- **style** (String): Optional parameter that defines the output style. If the value is `tree` (default), the nodes are outputted as a tree structure. If the value is `flat` the nodes are returned as a JSON object containing all the values named by the node.
- **recursion** (Integer): Specifies recursion depth when fetching the child nodes. `0` (default) refers only to the node specified by the target. `1` refers to the target node and its immediate children, and so on. `-1` is infinite.

**Response data**

- Identical to the GET operation of HTTP values

**Notifications**

None.

**Example 1** — Retrieve the current flow value

- URL: `wss://localhost:49098/ws/values/?key=0352ebaa-6de5-4f1d-9091-17678d11dfd6`
- Communication:

Sent:

```json
{
  "command": "read",
  "id": "6352827e-1ac3-11ec-bdf6-14dae904baea",
  "data": {
    "target": "mapper.bf.flow"
  }
}
```

Received:

```json
{
  "id": "6352827e-1ac3-11ec-bdf6-14dae904baea",
  "status": "RECEIVED",
  "data": {
    "command": "read",
    "id": "6352827e-1ac3-11ec-bdf6-14dae904baea",
    "data": {
      "target": "mapper.bf.flow"
    }
  }
}
```

Received:

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

**Example 2** — Retrieve information about the script run command

- URL: `wss://localhost:49098/ws/values/?key=0352ebaa-6de5-4f1d-9091-17678d11dfd6`
- Communication:

Sent:

```json
{
  "command": "read",
  "id": "acf0e246-1ac7-11ec-bdf6-14dae904baea",
  "data": {
    "target": "script.legacy.run"
  }
}
```

Received:

```json
{
  "id": "acf0e246-1ac7-11ec-bdf6-14dae904baea",
  "status": "RECEIVED",
  "data": {
    "command": "read",
    "id": "acf0e246-1ac7-11ec-bdf6-14dae904baea",
    "data": {
      "target": "script.legacy.run"
    }
  }
}
```

Received:

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

#### set

**Description**

Set command can be used for updating a value in the value tree. The structure of the data is identical to the POST operation of the HTTP value endpoint.

**Command data**

- **must_exist** (Integer): If set to `1`, checks existence of all nodes before executing any operations. Default is `0`.
- **data** (Object): List of tree nodes to set in flat format
  - **\<path.to.node1\>** (Object): Node 1 data
    - **content** (Object): The node content data
      - **value** (String): Updated value (only for values)
      - **call** (Integer): Must be set `1` to start the call (only for method calls)
      - **parameters** (Array): Array containing the parameter for the call (only for method calls)
  - **\<path.to.node2\>** (Object): Node 2 data
  - ...
  - **\<path.to.nodeN\>** (Object): Node N data

**Response data**

- Identical to the read command with flat style and containing only the specified nodes.

**Notifications**

None.

**Example 1** — Close valve V1 and open valve V2

- URL: `wss://localhost:49098/ws/values/?key=0352ebaa-6de5-4f1d-9091-17678d11dfd6`
- Communication:

Sent:

```json
{
  "command": "set",
  "id": "4014ffe4-3729-11ec-974d-14dae904baea",
  "data": {
    "must_exist": 1,
    "data": {
      "mapper.bf.valves.v1": {
        "content": {
          "value": 0
        }
      },
      "mapper.bf.valves.v2": {
        "content": {
          "value": 1
        }
      }
    }
  }
}
```

Received:

```json
{
  "id": "9ae4bbda-3729-11ec-974d-14dae904baea",
  "status": "RECEIVED",
  "data": {
    "command": "set",
    "id": "9ae4bbda-3729-11ec-974d-14dae904baea",
    "data": {
      "must_exist": 1,
      "data": {
        "mapper.bf.valves.v1": {
          "content": {
            "value": 0
          }
        },
        "mapper.bf.valves.v2": {
          "content": {
            "value": 1
          }
        }
      }
    }
  }
}
```

Received:

```json
{
  "id": "9ae4bbda-3729-11ec-974d-14dae904baea",
  "status": "SUCCEEDED",
  "data": {
    "mapper.bf.valves.v1": {
      "name": "mapper.bf.valves.v1",
      "type": "Value.Number.Integer.Enumeration.onOffE...",
      "content": {
        "read_only": false,
        "maximum_age": 5000,
        "lockable": true,
        "locked": true,
        "owner": "driver.vc.ch.c31",
        "latest_valid_value": {
          "value": "0",
          "outdated": false,
          "date": 1635341237559,
          "status": "SYNCHRONIZED",
          "exception": ""
        },
        "latest_value": {
          "value": "0",
          "outdated": false,
          "date": 1635341237559,
          "status": "SYNCHRONIZED",
          "exception": ""
        }
      }
    },
    "mapper.bf.valves.v2": {
      "name": "mapper.bf.valves.v2",
      "type": "Value.Number.Integer.Enumeration.onOffE...",
      "content": {
        "read_only": false,
        "maximum_age": 5000,
        "lockable": true,
        "locked": true,
        "owner": "driver.vc.ch.c21",
        "latest_valid_value": {
          "value": "1",
          "outdated": false,
          "date": 1635341237760,
          "status": "SYNCHRONIZED",
          "exception": ""
        },
        "latest_value": {
          "value": "1",
          "outdated": false,
          "date": 1635341237760,
          "status": "SYNCHRONIZED",
          "exception": ""
        }
      }
    }
  }
}
```

#### listen

**Description**

Starts listening to changes in one or more values.

**Command data**

- **target** (String): Target node in the value tree
- **all** (Boolean): If `true`, send notification from all updates, for example, same value with updated timestamp, and if `false`, send updates only when the actual value or its status changes.
- **recursion** (Boolean): If `true`, recursively listens all child nodes. Default: `false`

**Response data**

- Response is similar to the status command with only values that were added by this command

**Notifications**

**changed**

Description: Event caused by listening value. Generated each time the value or its status is updated.

Data:
- Similar to status data content with only the value that has been changed

**Example 1** — First start listening all changes in flow, then all valves by only listening actual value changes

- URL: `wss://localhost:49098/ws/values/?key=0352ebaa-6de5-4f1d-9091-17678d11dfd6`
- Communication:

Sent:

```json
{
  "command": "listen",
  "id": "be4b7d90-3bc8-11ec-84e8-14dae904baea",
  "data": {
    "target": "mapper.bf.flow"
  }
}
```

Received:

```json
{
  "id": "be4b7d90-3bc8-11ec-84e8-14dae904baea",
  "status": "RECEIVED",
  "data": {
    "command": "listen",
    "id": "be4b7d90-3bc8-11ec-84e8-14dae904baea",
    "data": {
      "target": "mapper.bf.flow"
    }
  }
}
```

Received:

```json
{
  "id": "be4b7d90-3bc8-11ec-84e8-14dae904baea",
  "status": "SUCCEEDED",
  "data": {
    "mapper.bf.flow": {
      "status": "OK",
      "only_changes": false,
      "id": "be4b7d90-3bc8-11ec-84e8-14dae904baea",
      "content": {
        "read_only": true,
        "maximum_age": 5000,
        "lockable": false,
        "locked": false,
        "owner": "driver.vc.flow",
        "latest_valid_value": {
          "value": "1.23",
          "outdated": false,
          "date": 1635849386887,
          "status": "SYNCHRONIZED",
          "exception": ""
        },
        "latest_value": {
          "value": "1.23",
          "outdated": false,
          "date": 1635849386887,
          "status": "SYNCHRONIZED",
          "exception": ""
        }
      }
    }
  }
}
```

Received (notification):

```json
{
  "id": "be4b7d90-3bc8-11ec-84e8-14dae904baea",
  "status": "NOTIFICATION",
  "event": "changed",
  "data": {
    "mapper.bf.flow": {
      "name": "mapper.bf.flow",
      "type": "Value.Number.Float",
      "content": {
        "read_only": true,
        "maximum_age": 5000,
        "lockable": false,
        "locked": false,
        "owner": "driver.vc.flow",
        "latest_valid_value": {
          "value": "1.23",
          "outdated": false,
          "date": 1635849391886,
          "status": "SYNCHRONIZED",
          "exception": ""
        },
        "latest_value": {
          "value": "1.23",
          "outdated": false,
          "date": 1635849391886,
          "status": "SYNCHRONIZED",
          "exception": ""
        }
      }
    }
  }
}
```

#### unlisten

**Description**

Stops listening to changes in one or more values.

If only target is specified, this applies to all nodes that matches the target. If only ID is specified, this matches to all targets that were associated to given ID.

**Command data**

- **target** (String): Target node from the value tree structure. If not specified, this matches to all nodes matching the command ID.
- **recursion** (Boolean): If `true`, stops listening to the current value and all child nodes in the tree.
- **id** (String): Command ID used for setting the listener. If not specified, this applies to all listeners matching the target.

**Response data**

- Response is similar to the status command with only values that were removed by this command

**Notifications**

None.

#### status

**Description**

Returns list of all nodes that are being listened to.

**Command data**

- **command** (String): Command specifies what operation is intended to start by message.

**Response data**

- **path.to.node** (Object): First node being listened to
  - **status** (String): Reference status: `OK`: Value exists, `UNLINKED`: Target does not exist, `WRONG_TYPE`: The target node content is not a value.
  - **all** (Boolean): Refer to parameter "all" for listen command
  - **id** (String): The unique identifier used for adding this listener.
  - **content** (Object): Identical to the read command tree node contents.
- **path.to.second.listened.node** (Object): Second node being listened to
- ...

**Notifications**

None.

---

### ws/notifications – Notifications

**Description**

```
http://address:49099/ws/notifications/
```

Allows to subscribe to notifications and their changes.

**Parameters**

- **key**: API key for authentication

**Command data**

- The endpoint currently supports no special commands.

**Response data**

- **id**: Unique message ID (same as in 'data')
- **status**: Currently is always `NOTIFICATION`
- **data**:
  - **title**: Message title
  - **message**: Message text
  - **type**: Message type (`debug`, `info`, `warning`, `error`)
  - **severity**: Message severity (`low`, `medium`, `high`)
  - **seen**: Was message already read in UI
  - **persistent**: Is message permanent
  - **date**: Message timestamp in POSIX format
  - **id**: Unique message ID
  - **source**: Message source (for example, device code)
  - **version**: Message version. Increased with every message change
  - **disposed**: Was message disposed (that is deleted)
  - **event**: Currently is always `notification`

**Example** — Message received from 'notifications' websocket:

```json
{
  "id": "a8f44b2a-7d00-462c-bbca-3e5a84806cd4",
  "status": "NOTIFICATION",
  "data": {
    "title": "Bftc2 is not connected",
    "message": "The program is unable to communicate with the...",
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

## Error Codes

### General errors

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

### Value errors

| Code | Name | Description |
|---|---|---|
| 3001 | Value not found | Value tree node not found. |
| 3003 | Read only | Value is read only. |
| 3005 | Value edit error | Failed to update the value. |
| 3006 | Wrong type | The target value tree node content is of an unexpected type. |
| 3007 | Target value has no content | The target value tree node does not have any content. |
| 3008 | Method call exception | Calling method caused an exception. |
| 6001 | Command not found | WebSocket command not found. |

### Server errors

| Code | Name | Description |
|---|---|---|
| 2001 | No key supplied | Access key is needed for accessing this resource. |
| 2002 | Content does not exist | Requested content does not exist. |
| 2003 | Access denied | Supplied key has no rights to the content. |
| 2004 | Method type error | HTTP method is not supported. |
| 2005 | Fatal WebSocket error | An unexpected exception occurred in the WS connection. Connection is closed. |
