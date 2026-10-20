#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script can be used to talk to the SingleQuantum Retina WebSQ.

This project is licensed under the terms of the MIT license.
Copyright (c) 2023 Single Quantum B. V. and Hielke Walinga
"""
import asyncio
import json
import sys
import time
import uuid
from ctypes import Structure, c_double, c_float, c_uint8, c_uint32
from functools import reduce
from math import floor
from typing import Callable
from urllib.parse import urlencode, urlsplit, urlunsplit
from urllib.request import Request, urlopen

import websockets
from websockets.sync.client import connect

# The time (ms) of a cu (channel unit) cycle.
CU_INTTIME = 10
# The size of a singular channel unit message.
CU_MESSAGE_SIZE = 32


class WebSocketMessage(Structure):
    _fields_ = [
        ("mcuId", c_uint8),
        ("cuId", c_uint8),
        ("cuStatus", c_uint8),
        ("monitorV", c_float),
        ("biasI", c_float),
        ("counts", c_uint32),
        ("intSize", c_uint32),
        ("rank", c_uint32),
        ("time", c_double),
    ]

    def asDict(self):
        return {
            "mcuId": self.mcuId,
            "cuId": self.cuId,
            "cuStatus": self.cuStatus,
            "monitorV": self.monitorV,
            "biasI": self.biasI,
            "intTime": self.intSize * CU_INTTIME,
            "counts": self.counts,
            "rank": self.rank,
            "time": self.time,
        }


def __unpack_messages__(buffer: bytes):
    """
    Format websocket message represented in bytes to a list of dictionary data of each channel.
    """
    for offset in range(0, len(buffer), CU_MESSAGE_SIZE):
        yield WebSocketMessage.from_buffer_copy(buffer[offset:(offset + CU_MESSAGE_SIZE)]).asDict()


class ConnectWebsocketClient(websockets.connect):
    """
    Context Manager to create a process WebSocket messages asynchronously. 
    Messages are formatted to a list of channel unit dictionary data.

    Parameters
    ----------
    url : str
        The address of the Retina Driver

    Example
    ----------
    def process_data(payload):
        print(payload)

    def main():
        async with ConnectWebsocketClient('ws://localhost:8080') as ws:
            async for payload in ws:
                process_data(payload)

    if __name__ == '__main__':
        asyncio.get_event_loop().run_until_complete(main())
    """

    def __init__(self, url: str, **kwargs):
        super().__init__(url + "/counts", **kwargs)

    async def __aiter__(self):
        async for buffer in super().__aiter__():
            yield __unpack_messages__(buffer)

    async def __aenter__(self):
        prot = await self
        prot.recv = self._wrap_recv(prot.recv)
        return prot

    def _wrap_recv(self, recv_func):
        async def wrapper():
            return [channel_data for channel_data in __unpack_messages__(await recv_func())]
        return wrapper


def merge(a, b, path=None):
    """Merges dictionary `b` recursively into dictionary `a` keeping all deeply nested data.

    Thus it won't simply overwrite a value at a key if that value is a dictionary again.
    It raises an Exception when `b` contains a value at a place where `a` has a nested data structure.
    Very similar to lodash.merge https://docs-lodash.com/v4/merge/ which is used by the websq as well.

    Parameters
    ----------
    a : dict
        Target dictionary.
    b : dict
        Dictionary to extract new values from.
    path : list
        Keeps track of previous values when going nested during recursion.

    Returns
    -------
    dict
        The `a` dictionary with new values from `b`.
    """
    path = path or []  # Initialize recursion for better error message.

    for key in b:
        if isinstance(a.get(key), dict):
            if not isinstance(b.get(key), dict):
                # Will not merge a value when there is a nested data structure already in place.
                raise Exception('Conflict at ' + '.'.join(path + [str(key)]))

            # Here the dictionaries are recursively merged keeping all the deeply nested data.
            merge(a[key], b[key], path + [str(key)])
            continue

        # b takes precendence
        a[key] = b[key]

    return a


class JsonRpc(object):
    """This class takes the `api_url` and then can be used to send
    standard HTTP requests with `request` or json rpc requests with `jsonrpc`.
    """

    def __init__(self, api_url, jsonrpc_version='2.0'):
        """Initialize a JsonRpc class.

        Parameters
        ----------
        api_url : str
            The URL of the api endpoint.
        jsonrpc_version : str
            The JSON RPC version this endpoint uses.
        """
        self.api_url = api_url
        self.jsonrpc_version = jsonrpc_version

    def request(self, params=None, payload=None):
        """Perform a GET HTTP request, if given a payload a POST.

        Parameters
        ----------
        params : list, optional
            A list of parameters added to the `self.api_url`.
        payload : dict, optional
            If provided sends `payload` as JSON with a POST.

        Returns
        -------
        dict
            Returns the result as a dict converted from the json received.

        Raises
        ------
        AssertionError
            Raises an assertion error when the HTTP response code is not 200.
        """
        headers = {}
        request_data = None
        headers["Accept"] = "application/json"
        target = self.api_url

        if params:
            target += "?" + urlencode(params, doseq=True, safe="/")

        if payload:
            headers["Content-Type"] = "application/json; charset=UTF-8"
            request_data = json.dumps(payload).encode()

        http_request = Request(target, data=request_data, headers=headers)
        http_response = urlopen(http_request, timeout=10)

        content_charset = "utf-8"  # default
        if hasattr(http_response, 'status'):  # Python3 only
            assert http_response.status == 200, "Got HTTP " + str(http_response.status) + " with " \
                + http_response.read().decode(content_charset)
            content_charset = http_response.headers.get_content_charset(
                content_charset)

        body = http_response.read().decode(content_charset)

        return json.loads(body)

    def jsonrpc(self, method, **params):
        """Makes a JSON RPC request to the `self.api_url`.

        Parameters
        ----------
        method : str
            The name of the method you want to call.
        params : list[str], optional
            The list of parameters provided to that function.

        Returns
        -------
        dict with keys as str
            The result of the function as a dictionary.

        Raises
        ------
        AssertionError
            If the request fails are the method does not exists.
        """
        identifier = str(uuid.uuid4())
        payload = {
            'method': method,
            'params': params or [],
            'jsonrpc': self.jsonrpc_version,
            'id': identifier,
        }
        response_data = self.request(payload=payload)
        assert response_data['jsonrpc'], "No jsonrpc response"
        assert response_data['id'] == identifier, "Incorrect identifier in response"

        if 'result' in response_data:
            return response_data['result']
        else:
            raise ValueError(response_data['error']['data']['message'])


class WebSQController(JsonRpc):
    """This class can send requests to the websq via the JSON RPC protocol.
    Set the `domain` of the websq in the initialization.

    A lot of funtionality requires the settings object.
    Function that rely on the settings object can be passed settings as a keyword
    argument to prevent retrieving the settings object multiple times.

    Some functionality accepts the channels parameter.
    This parameter determines from which channels you pull the data.
    The channels parameter is a list of ranks or locations of the channels.
    Ranks can be given as integers, and locations can be given as either
    a tuple or a list formatted as [mcuId, cuId].

    The rankMap specifies the exact location of these detectors.
    If this is not set (or None) all locations are returned.

    """

    def __init__(self, domain=None):
        """Initialize a WebSQController class

        Parameters
        ----------
        domain : str
            The domain the websq controller can be accessed on.
            We set the /api path onto this domain name.
        url : str
            Instead of the domain, you can also specify the api_url directly
            with the correct path to the JSON RPC endpoint.
        cu_inttime : float
            The duration (ms) a cu (channel unit) cycle.
            The default is 10ms for Retina and 50ms for the backport.
        """
        res = urlsplit(domain)

        self.base_url = urlunsplit((res.scheme, res.netloc, '/', '', ''))
        self.ws_url = urlunsplit(('ws', res.netloc, '/counts', '', ''))
        self._settings = None

        api_url = urlunsplit((res.scheme, res.netloc, '/api', '', ''))

        super(WebSQController, self).__init__(api_url)

        # Get settings already on init
        self.getSettings()

    def startRecording(self, channels=[]):
        """Turns on recording mode, the data recorded will be returned by the stopRecording command"""
        if len(channels) == 0:
            channels = self.getAllRanks()
        return self.jsonrpc("startRecording", channels=channels)

    def stopRecording(self):
        """Stops recording mode, will return the data which was collected while recording."""
        return self.jsonrpc("stopRecording")

    def convertToRank(self, rank_or_location):
        """Takes a channel notation in either rank or location ('mcuId.cuId'),
        and converts it to the corresponding rank.
        """
        if isinstance(rank_or_location, list) or isinstance(rank_or_location, tuple):
            return self.getRankByIds(*rank_or_location)
        return self.getRankByIds(*rank_or_location.split('.')) if '.' in str(
            rank_or_location) else int(rank_or_location)

    def convertToLocation(self, rank_or_location):
        """Takes a channel notation in either rank or location ('mcuId.cuId'),
        and converts it to the corresponding location.
        """
        rankMap = self.getRankMap()
        if isinstance(rank_or_location, list) or isinstance(rank_or_location, tuple):
            return [str(rank_or_location[0]), str(rank_or_location[1])]
        return rank_or_location.split('.') if '.' in str(
            rank_or_location) else [str(x) for x in rankMap[str(rank_or_location)]]

    def getChannelInformation(self, name, channels=[]):
        """Gets the channel information for the quantity "name".

        Parameters
        ----------
        channels : list, optional
            A list of channels given as either their rank or their location.
            The location of a channel is given as 'mcuId.cuId'.
            If this is not provided it will select all of them.

        Returns
        -------
        list
            a list containing the values read for the requested quantity

        """
        settings = self.getSettings()
        locations = [self.convertToLocation(c) for c in channels] if channels else self.getAllLocations()

        values = []
        for mcuId, cuId in locations:
            values.append(settings['devices'][str(mcuId)]
                          ['channels'][str(cuId)]["configuration"][name])
        return values

    def setChannelConfiguration(self, name, value, channels=None):
        """ Sets the channel configuration name to value.

        Parameters
        ----------
        channels : list, optional
            A list of channels given as either their rank or their location.
            The location of a channel is given as 'mcuId.cuId'.
            If this is not provided it will select all of them.
        """
        channels = [self.convertToRank(
            c) for c in channels] if channels else self.getAllRanks()
        rankMap = self.getRankMap()

        updates = {}
        for rank, (mcuId, cuId) in rankMap.items():
            if int(rank) not in channels:
                continue
            update = list(reversed(['devices', mcuId, 'channels', cuId, 'configuration', name,
                                    value]))
            cu_update = update[0]
            for indx, key in enumerate(update):
                if indx == 0:
                    continue
                cu_update = {key: cu_update}
            updates = merge(updates, cu_update)
        return self.setSettings(**updates)

    def setTriggerV(self, value, channels=None):
        """ Sets the trigger level for the counters for each channel (all selected channels the same value).
        The trigger voltage is in Volts and must be in the range (-10, 10).


        Parameters
        ----------
        value : float
            The trigger level to set (in V) for all channels. Supported range: (-10, 10)V.
        channels : list, optional
            A list of channels given as either their rank or their location.
            The location of a channel is given as 'mcuId.cuId'.
            If this is not provided it will select all of them.

        Returns
        -------
        updated_settings: dict
            The new and updated settings.
        """
        if abs(value) > 10:
            raise ValueError(
                'The requested value for Trigger is outside the supported range (-10V, 10V).')

        return self.setChannelConfiguration('triggerV', value, channels=channels)

    def setBiasI(self, value, channels=None):
        """ Sets the bias current level for each channel (all selected channels the same value).

        Parameters
        ----------
        value : float
            The bias current to set (in A).
        channels : list, optional
            A list of channels given as either their rank or their location.
            The location of a channel is given as 'mcuId.cuId'.
            If this is not provided it will select all of them.

        Returns
        -------
        updated_settings: dict
            The new and updated settings.
        """
        return self.setChannelConfiguration('biasI', value, channels=channels)

    def setChannelValueMultiple(self, name, values):
        """Sets an array of values for parameter 'name' for all channels.

        Parameters
        ----------
        name: string
            Name of the channelunit configuration parameter which you want to change.
        values : array
            Array of values which you want to assign for all channels.
            This is assumed to be sorted by rank.

        Returns
        -------
        updated_settings: dict
            The new and updated settings.
        """
        rankMap = self.getRankMap()
        if len(values) != len(rankMap.keys()):
            raise ValueError(
                f"The new {name} array needs to be of the same length as the amount of channels in the system.")
        updates = {}
        for rank, (mcuId, cuId) in rankMap.items():
            update = list(reversed(['devices', mcuId, 'channels', cuId, 'configuration', name,
                                    values[int(rank) - 1]]))
            cu_update = update[0]
            for indx, key in enumerate(update):
                if indx == 0:
                    continue
                cu_update = {key: cu_update}
            updates = merge(updates, cu_update)
        return self.setSettings(**updates)

    def setBiasIMultiple(self, values):
        """ Sets the bias current level for each channel given by the array values.

        Parameters
        ----------
        values : array
            Array of floats indicating the bias current to set in each channel (in A).

        Returns
        -------
        updated_settings: dict
            The new and updated settings.
        """
        return self.setChannelValueMultiple('biasI', [v for v in values])

    def setTriggerVMultiple(self, values):
        """ Sets the Trigger level for the counter for each channel given by the array values.
        The Trigger current for each channel is in V and must be in the range (-10,10) V.


        Parameters
        ----------
        values : array
            Array of floats indicating the trigger level in each channel (in V).

        Returns
        -------
        updated_settings: dict
            The new and updated settings.
        """
        return self.setChannelValueMultiple('triggerV', values)

    def getTriggerV(self, channels=None):
        """ Gets the trigger level for each channel.

        Parameters
        ----------
        channels : list, optional
            A list of channels given as either their rank or their location.
            The location of a channel is given as 'mcuId.cuId'.
            If this is not provided it will select all of them.

        Returns
        -------
        list
            a list containing the trigger level for each requested channel

        """
        return self.getChannelInformation('triggerV', channels=channels)

    def getBiasI(self, channels=None):
        """ Gets the bias current for each channel.

        Parameters
        ----------
        channels : list, optional
            A list of channels given as either their rank or their location.
            The location of a channel is given as 'mcuId.cuId'.
            If this is not provided it will select all of them.

        Returns
        -------
        list
            a list containing the bias current for each requested channel

        """
        return self.getChannelInformation('biasI', channels=channels)

    def rebootSystem(self, **params):
        return self.jsonrpc("rebootSystem", **params)

    def getDevices(self):
        response = self.jsonrpc('getDevices')
        return response['devices']

    def getBackend(self):
        response = self.jsonrpc('getBackend')
        return response['backend']

    def getSettings(self) -> dict:
        """Gets the settings once, then caches it as a property.
        `reloadSettings()` can be called to get the most recent settings"""
        if self._settings is None:
            self._settings = self.jsonrpc('getSettings')
        return self._settings

    def reloadSettings(self) -> dict:
        """Clears chached settings requests settings from the api"""
        self._settings = None
        return self.getSettings()

    def setSettings(self, **params):
        self._settings = None
        return self.jsonrpc('setSettings', **params)

    def getIvFile(self, details="", datatype="txt", devicedetails=True):
        """Return a file with the latest iv measurement.

        Parameters
        ----------
        details : str
            Optionally you can pass some extra details/comments in the file.
        datatype : str
            The export datatype, either txt, csv, json.
        devicedetails : bool
            Whether or not to include some extra details of the devices.

        Returns
        -------
        dict
            A dictionary with `ivData` as the root element.
        """
        channels = self.getAllRanks()
        return self.jsonrpc(
            'getIvFile', details=details, datatype=datatype, channels=channels, devicedetails=devicedetails)

    def getLog(self, lines=1000):
        return self.jsonrpc('getLog', lines=lines)

    def getRankMap(self):
        settings = self.getSettings()
        return settings['frontend']['rankMap']

    def getRankByIds(self, mcuId, cuId):
        rankmap = self.getRankMap()
        mcuId = int(mcuId)
        cuId = int(cuId)
        ranks = [k for k, v in rankmap.items() if v == [mcuId, cuId]]
        if len(ranks) != 1:
            raise KeyError(
                f"Could not find rank for channel with Ids: {mcuId}.{cuId}!")
        return int(ranks[0])

    def getAllLocations(self):
        rankmap = self.getRankMap()
        return list(rankmap.values())

    def getAllRanks(self):
        rankmap = self.getRankMap()
        return list(map(lambda x: int(x), rankmap.keys()))

    def getIntTime(self):
        settings = self.getSettings()
        return settings['backend']['intTime']

    def setIntTime(self, intTime):
        """intTime in (ms) should be in steps of 10ms."""
        return self.setSettings(backend={"intTime": intTime})

    def getTemperatureData(self):
        """Returns all the stored temperature data."""
        backend = self.getBackend()
        return backend['temperatures']

    def getTemperatures(self):
        """Returns the latests temperatures measured"""
        temperature_data = self.getTemperatureData()
        return temperature_data[-1]['temp1'], temperature_data[-1]['temp2']

    def startIv(self, biasIStart, biasIStop, biasIStep, intTime, channels=None):
        """Start a IV measurement on the cus of `selectedCus` or if not provided all of them.

        Parameters
        ----------
        biasIStart : float
            The current to start (in uA).
        biasIStop : float
            The current to stop (in uA)
        biasIStep : float
            The step size of the sweep (in uA).
        intTime : float
            The integration time (in ms) of a single step.
        channels : list, optional
            A list of channels given as either their rank or their location.
            The location of a channel is given as 'mcuId.cuId'.
            If this is not provided it will select all of them.

        Returns
        -------
        dict
            The the new updated settings you have send to the server.
        """
        locations = [self.convertToLocation(c) for c in channels] if channels else self.getAllLocations()
        deviceUpdates = [{mcuId: {'channels': {cuId: {'configuration': {
            'biasIStart': biasIStart * 10 ** -6,
            'biasIStop': biasIStop * 10 ** -6,
            'biasIStep': biasIStep * 10 ** -6,
            # The biasSweepT is the amount of cycles a cu (channel unit) runs
            'biasSweepT': intTime / CU_INTTIME,
            'cuStatus': 2,
        }}}}} for (mcuId, cuId) in locations]

        # Reduced specialized merged as mcuId is not unique for each location.
        deviceSettingsUpdated = reduce(merge, deviceUpdates, {})
        return self.setSettings(devices=deviceSettingsUpdated)

    def stopIv(self):
        """Stop the current IV measurement that is running.

        Returns
        -------
        string
            Succes if the IV sweep was stopped succesfully.
        """
        return self.jsonrpc('stopIV')

    def getIvData(self, channels=None):
        """Get the IV curves of the last measurement.

        Parameters
        ----------
        channels : list, optional
            A list of channels given as either their rank or their location.
            The location of a channel is given as 'mcuId.cuId'.
            If this is not provided it will select all of them.

        Returns
        -------
        dict:
            A dictionary that maps the location [mcuId, cuId] to a dictionary object
            that contains the `biasI`, `counts`, and `monitorV`.
        """

        locations = [self.convertToLocation(c) for c in channels] if channels else self.getAllLocations()
        traces = {}
        ivDataAll = self.jsonrpc("getIvData")

        for (mcuId, cuId) in locations:
            ivData = {}
            rank = str(self.getRankByIds(mcuId, cuId))
            populated_indices = [i for i, c in enumerate(
                ivDataAll['counts'][rank]) if c is not None]

            ivData['biasI'] = [ivDataAll['counts']['biasI'][i]
                               for i in populated_indices]
            ivData['counts'] = [ivDataAll['counts'][rank][i]
                                for i in populated_indices]
            ivData['monitorV'] = [ivDataAll['monitorV'][rank][i]
                                  for i in populated_indices]

            traces[(mcuId, cuId)] = ivData

        return traces

    def sweepIv(self, biasIStart, biasIStop, biasIStep, intTime, overhead=1, channels=None):
        """Start a IV sweep and then return the measured data. Blocks the thread with a time.sleep.

        Parameters
        ----------
        biasIStart : float
            The current to start (in uA).
        biasIStop : float
            The current to stop (in uA)
        biasIStep : float
            The step size of the sweep (in uA).
        intTime : float
            The integration time (in ms) which is the duration of each step.
        overhead : float, default=1
            Wait `overhead` seconds longer than necessary because of latency.
        channels : list, optional
            A list of channels given as either their rank or their location.
            The location of a channel is given as 'mcuId.cuId'.
            If this is not provided it will select all of them.

        Returns
        -------
        dict
            A dictionary that maps the location [mcuId, cuId] to a dictionary object
            that contains the `biasI`, `counts`, and `monitorV`.
        """
        self.startIv(biasIStart, biasIStop, biasIStep,
                     intTime, channels=channels)
        steps = ((biasIStop - biasIStart) / biasIStep) + 1
        # Wait the duration of the sweep time plus a little bit more.
        time.sleep((intTime * steps / 1000) + overhead)
        return self.getIvData(channels=channels)

    def getIvIntTime(self):
        settings = self.getSettings()
        return settings['backend']['ivIntTime']

    def getIvTimeStamp(self):
        settings = self.getSettings()
        return settings['backend']['ivTimeStamp']

    def getIvStatus(self):
        return self.jsonrpc('IVStatus')

    def getCounts(self, channels=None, timeout=None, connected_websocket=None):
        """Get the current counts measurement. The amount of counts during the current integration time.

        Parameters
        ----------
        channels : list, optional
            A list of channels given as either their rank or their location.
            The location of a channel is given as 'mcuId.cuId'.
            If this is not provided it will select all of them.
        timeout: float, optional
            An optional timeout can be passed for how long we wait a message.
            This could be changed to ask for counts with very long integration time.

        Returns
        -------
        dict
            A dictionary that maps the location [mcuId, cuId] to a dictionary object
            that contains the `counts`, `time`, and `monitorV`.
            The timestamp in the returned data is since the server started.
            The counts are the counts during an integration time period.
        """
        rankMap = self.getRankMap()
        self._counts_array = [None] * len(rankMap)

        if not connected_websocket:
            websocket = connect(self.ws_url)
        else:
            websocket = connected_websocket

        message = websocket.recv(timeout=timeout)

        ranks = None
        if channels:
            ranks = [self.convertToRank(c) for c in channels]
        try:
            ws_messages = self.decode_websocket_msg(message)

            for msg in ws_messages:
                self._counts_array[msg['rank'] - 1] = msg['counts']

            if ranks:
                return [c for i, c in enumerate(self._counts_array) if i + 1 in ranks]

            return self._counts_array
        except Exception as e:
            print(f"Exception while reading counts: {e}")
            websocket.close()
        finally:
            if not connected_websocket:
                websocket.close()

    def collectCounts(self, runtime=10, interval=0.5, channels=None):
        """Collect counts every `interval` during the `runtime`. Blocks the thread with a time.sleep.

        Parameters
        ----------
        runtime : float
            The amount of time (in seconds) to collect all the counts.
        interval : float
            Attempt to request the counts every time an interval (in seconds) starts.
        channels : list, optional
            A list of channels given as either their rank or their location.
            The location of a channel is given as 'mcuId.cuId'.
            If this is not provided it will select all of them.

        Returns
        -------
        list
            A list with the collected counts of every channel.

        Notes
        -----
        The result contains `floor(runtime / interval)` points.
        The points are only the points when a new interval starts.
        If a request takes longer than one interval, it just starts a new one when
        the next interval starts.
        Prints a warning to stderr (standard error of console) if points are missed.
        You can increase the interval time to prevent skipped points.
        However the data contains a timestamp, so even with missing points your data is still usefull,
        and it is recommended to rely on the timestamps instead of the interval.
        """
        result = []

        websocket = connect(self.ws_url)

        starttime = time.time()
        measured_points = 0
        while time.time() - starttime <= runtime + interval:
            measured_points += 1
            counts = self.getCounts(
                channels=channels, connected_websocket=websocket)
            result.append(counts)

            # Wait until you hit the next interval,
            # might skip an interval if the interval is set too short.
            # For missed points a warning is shown.
            time.sleep(interval - ((time.time() - starttime) % interval))

        expected_points = floor(runtime / interval)
        if measured_points != expected_points:
            sys.stderr.write(
                "WARNING: Failed to retrieve all points."
                + " Instead got %i points, expected %i points." % (measured_points, expected_points)
                + " You might want to increase interval,"
            )

        websocket.close()

        return result[:expected_points]

    def transformToArray(self, data, quantity):
        """Transform your iv data or counts data to a 'a x b' array for `quantity`

        Parameters
        ----------
        data: dict
            Dictionary which is the iv data from getIvData or sweepIv
            or the counts data from getCounts or collectCounts
        quantity: str
            This is the name of quantity:
            biasI, counts, or monitorV for iv data
            counts, time, monitorV for count data

        Returns
        -------
        result: list[list]
            list as 'a x b' data array
            where a is the amount of channels in order of the ranks.
            and b is the amount of data measured.
        """
        locations = list(data.keys())
        locations = sorted(locations, key=lambda loc: self.convertToRank(loc))
        res = [data[locations[0]]['biasI']] + [[] for _ in locations]
        for i, loc in enumerate(locations):
            res[i + 1] = data[loc][quantity]
        return res

    def getIvHistory(self):
        """
        Gets the IV history for all channels and returns a list of lists with the
        bias current in the first list and the monitor voltage for each CU as the next.

        Returns
        -------
        result: list[list]
            the first list is the bias current
            the other lists are the monitor voltages (V) of the channels sorted by rank.
        """
        ivData = self.getIvData()

        if len(ivData) == 0:
            return []
        return self.transformToArray(ivData, 'monitorV')

    def getIcHistory(self):
        """
        Gets the IC history for all channels and returns a list of lists with the
        bias current in the first list and the monitor voltage for each CU as the next.

        Returns
        -------
        result: list[list]
            the first list is the bias current
            the other lists are the counts of the channels sorted by rank.
        """
        ivData = self.getIvData()
        if len(ivData) == 0:
            return []
        return self.transformToArray(ivData, 'counts')

    def setNetworkSettings(self, **params):
        """Sets the networking settings.

        Parameters
        ----------
        dhcp: bool
            Wether or not to enable DHCP.
        address: str
            The static IP address, in case DHCP is off.
        gateway: str
            The gateway IP.
        """
        return self.jsonrpc('setNetworkSettings', **params)

    def setHostName(self, hostname):
        return self.jsonrpc("setHostname", hostname=hostname)

    def decode_websocket_msg(self, msg, attribute=None):
        """Deconstructs a basic websocket message.

        Parameters
        ----------
        msg: bytes
            A byte string of combined channel unit messages.
            Each channel message is 32 bytes.
        attribute: str, optional
           You can pass a specific attribute name.
           If this is given only a list of values for this attribute is returned.

        Returns
        -------
        result: list
            A list of decoded messages.
            If no attribute name is passed it will be a dict with all values.
            Otherwise it will be a list of values for just this attribute.
        """
        data = __unpack_messages__(msg)

        if attribute:
            return [el.get(attribute, None) for el in data]
        return list(data)


class WebsocketClient:
    """
    Easy to use wrapper for ConnectWebsocketClient Context Manager.

    Parameters
    ----------
    url : str
        The address of the Retina Driver
    max_streams : int
        How many times you want to receive messages before ending the listner. -1 will running forever. 

    Example
    ----------
    def process_data(payload):
        print(payload)

    client = WebsocketClient('ws://localhost:8080')
    client.add_callback(process_data)
    client.start()
    """
    callback: Callable = None

    def __init__(self, url: str, max_streams=-1):
        self.uri = url
        self.max_streams = max_streams

    def add_callback(self, callback: Callable):
        self.callback = callback

    async def _run_socket_listener(self):
        n = 0
        async with ConnectWebsocketClient(self.uri) as ws:
            async for payload in ws:
                if self.callback:
                    self.callback(payload)

                if self.max_streams < 0:
                    continue

                if n < self.max_streams:
                    n += 1
                    continue
                return

    def start(self):
        return asyncio.get_event_loop().run_until_complete(self._run_socket_listener())

    def close(self):
        asyncio.get_event_loop().stop()


if __name__ == '__main__':
    import os

    websq_domain = os.environ.get("WEBSQ_DOMAIN", 'http://localhost:8080/')
    sq = WebSQController(websq_domain)
