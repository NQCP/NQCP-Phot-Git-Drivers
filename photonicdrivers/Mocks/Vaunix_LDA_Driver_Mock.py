'''
Hardware-free stand-in for the Vaunix LDA variable digital attenuator drivers.

Mirrors the public API of Vaunix_LDA_USB_Driver and Vaunix_LDA_Ethernet_Driver,
including the parts that differ between the two transports, so that consuming code
and the driver's range-checking and quantisation rules can be tested without a
device and without the vendor DLLs.

The transport-specific behaviour is reproduced faithfully, because it is exactly
what callers trip over:

  * connection_type="USB" exposes device status, ramp/profile activity polling,
    multichannel setters and the profile index, and raises
    Vaunix_LDA_Transport_Error for the network getters.
  * connection_type="Ethernet" does the reverse.

Defaults model an LDA-908V: 0-90 dB in 0.1 dB steps, 200-8000 MHz, one channel,
with high-resolution, profile and bidirectional-ramp features present.
'''

from __future__ import annotations

from typing import Optional, Sequence

from photonicdrivers.Abstract.Connectable import Connectable
from photonicdrivers.Variable_Digital_Attenautor.Vaunix_LDA_Constants import (
    HAS_BIDIR_RAMPS,
    HAS_HIRES,
    HAS_MCHANNELS,
    HAS_PROFILES,
    PROFILE_ACTIVE,
    SWP_ACTIVE,
    DEV_CONNECTED,
    DEV_OPENED,
    Vaunix_LDA_Error,
    Vaunix_LDA_Feature_Error,
    Vaunix_LDA_Transport_Error,
    counts_to_db,
    db_to_counts,
    describe_features,
    round_half_up,
)


class Vaunix_LDA_Driver_Mock(Connectable):
    '''
    Simulated Vaunix LDA attenuator.
    '''

    def __init__(
        self,
        connection_type: str = "USB",
        serial_number: int = 29411,
        model_name: str = "LDA-908V",
        ip_address: str = "192.168.100.5",
        min_attenuation_dB: float = 0.0,
        max_attenuation_dB: float = 90.0,
        attenuation_step_dB: float = 0.1,
        min_frequency_MHz: float = 200.0,
        max_frequency_MHz: float = 8000.0,
        number_of_channels: int = 1,
        features: int = HAS_BIDIR_RAMPS | HAS_PROFILES | HAS_HIRES,
        profile_max_length: int = 100,
    ) -> None:
        if connection_type not in ("USB", "Ethernet"):
            raise ValueError(f"connection_type must be 'USB' or 'Ethernet', got {connection_type!r}")

        self.connectionType = connection_type
        self.serial_number = int(serial_number)
        self.ip_address = ip_address if connection_type == "Ethernet" else None
        self.device_id = 1 if connection_type == "USB" else None

        self._model_name = model_name
        self._features = int(features)
        self._num_channels = int(number_of_channels)
        self._profile_max_length = int(profile_max_length)

        self._min_atten_counts = db_to_counts(min_attenuation_dB)
        self._max_atten_counts = db_to_counts(max_attenuation_dB)
        self._step_counts = max(1, db_to_counts(attenuation_step_dB))
        self._min_freq_counts = int(round_half_up(min_frequency_MHz * 10))
        self._max_freq_counts = int(round_half_up(max_frequency_MHz * 10))

        self.connected = False
        self.command_history: list[tuple] = []

        # Simulated device state.
        self._active_channel = 1
        self._attenuation_counts = {channel: self._min_atten_counts
                                    for channel in range(1, self._num_channels + 1)}
        self._frequency_counts = self._min_freq_counts
        self._rf_on = True
        self._ramp_start_counts = self._min_atten_counts
        self._ramp_end_counts = self._max_atten_counts
        self._ramp_step_counts = self._step_counts
        self._ramp_step_two_counts = self._step_counts
        self._ramp_dwell_ms = 1
        self._ramp_dwell_two_ms = 1
        self._ramp_idle_ms = 0
        self._ramp_hold_ms = 0
        self._ramp_up = True
        self._ramp_repeat = False
        self._ramp_bidirectional = False
        self._ramping = False
        self._profile_counts = [self._min_atten_counts] * self._profile_max_length
        self._profile_count = 1
        self._profile_dwell_ms = 1
        self._profile_idle_ms = 0
        self._profile_index = 0
        self._profile_playing = False
        self.saved_settings_count = 0

    # ==================== Connectable ====================

    def connect(self) -> None:
        self.connected = True
        self._active_channel = 1
        self.command_history.append(("connect",))

    def disconnect(self) -> None:
        self.connected = False
        self.command_history.append(("disconnect",))

    def is_connected(self) -> bool:
        return self.connected

    def __enter__(self) -> "Vaunix_LDA_Driver_Mock":
        self.connect()
        return self

    def __exit__(self, exception_type, exception, traceback) -> None:
        self.disconnect()

    # ==================== identity ====================

    def get_model_name(self) -> str:
        self._require_connected("get_model_name")
        return self._model_name

    def get_serial_number(self) -> int:
        self._require_connected("get_serial_number")
        return self.serial_number

    def get_connection_type(self) -> str:
        return self.connectionType

    def get_dll_version(self) -> str:
        self._require_connected("get_dll_version")
        return "2.14" if self.connectionType == "USB" else "1.1"

    def get_features(self) -> int:
        self._require_connected("get_features")
        return self._features

    # ==================== channels ====================

    def get_number_of_channels(self) -> int:
        self._require_connected("get_number_of_channels")
        return self._num_channels

    def get_channel(self) -> int:
        self._require_connected("get_channel")
        return self._active_channel

    def set_channel(self, channel: int) -> None:
        self._require_connected("set_channel")
        self._active_channel = self._validated_channel(channel)
        self.command_history.append(("set_channel", self._active_channel))

    # ==================== attenuation ====================

    def get_attenuation_dB(self, channel: Optional[int] = None) -> float:
        self._require_connected("get_attenuation_dB")
        if channel is not None:
            self._active_channel = self._validated_channel(channel)
        return counts_to_db(self._attenuation_counts[self._active_channel])

    def set_attenuation_dB(self, attenuation_dB: float, channel: Optional[int] = None) -> None:
        self._require_connected("set_attenuation_dB")
        counts = self._quantize_attenuation_counts(attenuation_dB)
        if channel is not None:
            self._active_channel = self._validated_channel(channel)
        self._attenuation_counts[self._active_channel] = counts
        self.command_history.append(("set_attenuation_dB", self._active_channel, counts_to_db(counts)))

    def get_min_attenuation_dB(self) -> float:
        self._require_connected("get_min_attenuation_dB")
        return counts_to_db(self._min_atten_counts)

    def get_max_attenuation_dB(self) -> float:
        self._require_connected("get_max_attenuation_dB")
        return counts_to_db(self._max_atten_counts)

    def get_attenuation_step_dB(self) -> float:
        return counts_to_db(self._step_counts)

    def set_attenuation_multichannel_dB(self, attenuation_dB: float, channels: Sequence[int]) -> None:
        self._require_usb("set_attenuation_multichannel_dB", "fnLDA_SetAttenuationMCHR")
        self._require_feature(HAS_MCHANNELS, "HAS_MCHANNELS", "set_attenuation_multichannel_dB")
        if not channels:
            raise ValueError("channels must contain at least one channel number")
        counts = self._quantize_attenuation_counts(attenuation_dB)
        for channel in channels:
            self._attenuation_counts[self._validated_channel(channel)] = counts
        self.command_history.append(
            ("set_attenuation_multichannel_dB", tuple(channels), counts_to_db(counts))
        )

    # ==================== working frequency ====================

    def get_frequency_MHz(self) -> float:
        self._require_connected("get_frequency_MHz")
        return self._frequency_counts / 10.0

    def set_frequency_MHz(self, frequency_MHz: float) -> None:
        self._require_connected("set_frequency_MHz")
        counts = int(round_half_up(float(frequency_MHz) * 10))
        if not self._min_freq_counts <= counts <= self._max_freq_counts:
            raise ValueError(
                f"frequency_MHz={frequency_MHz} is outside "
                f"[{self._min_freq_counts / 10.0}, {self._max_freq_counts / 10.0}] MHz for "
                f"{self._model_name} serial {self.serial_number}"
            )
        self._frequency_counts = counts
        self.command_history.append(("set_frequency_MHz", counts / 10.0))

    def get_min_frequency_MHz(self) -> float:
        self._require_connected("get_min_frequency_MHz")
        return self._min_freq_counts / 10.0

    def get_max_frequency_MHz(self) -> float:
        self._require_connected("get_max_frequency_MHz")
        return self._max_freq_counts / 10.0

    # ==================== RF path ====================

    def get_rf_on(self) -> bool:
        self._require_connected("get_rf_on")
        return self._rf_on

    def set_rf_on(self, enabled: bool) -> None:
        self._require_connected("set_rf_on")
        self._rf_on = bool(enabled)
        self.command_history.append(("set_rf_on", self._rf_on))

    # ==================== ramp ====================

    def get_ramp_start_dB(self) -> float:
        self._require_connected("get_ramp_start_dB")
        return counts_to_db(self._ramp_start_counts)

    def set_ramp_start_dB(self, attenuation_dB: float) -> None:
        self._require_connected("set_ramp_start_dB")
        self._ramp_start_counts = self._quantize_attenuation_counts(attenuation_dB)
        self.command_history.append(("set_ramp_start_dB", counts_to_db(self._ramp_start_counts)))

    def get_ramp_end_dB(self) -> float:
        self._require_connected("get_ramp_end_dB")
        return counts_to_db(self._ramp_end_counts)

    def set_ramp_end_dB(self, attenuation_dB: float) -> None:
        self._require_connected("set_ramp_end_dB")
        self._ramp_end_counts = self._quantize_attenuation_counts(attenuation_dB)
        self.command_history.append(("set_ramp_end_dB", counts_to_db(self._ramp_end_counts)))

    def get_ramp_step_dB(self) -> float:
        self._require_connected("get_ramp_step_dB")
        return counts_to_db(self._ramp_step_counts)

    def set_ramp_step_dB(self, step_dB: float) -> None:
        self._require_connected("set_ramp_step_dB")
        self._ramp_step_counts = self._quantized_step_counts(step_dB)
        self.command_history.append(("set_ramp_step_dB", counts_to_db(self._ramp_step_counts)))

    def get_ramp_step_two_dB(self) -> float:
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "get_ramp_step_two_dB")
        return counts_to_db(self._ramp_step_two_counts)

    def set_ramp_step_two_dB(self, step_dB: float) -> None:
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "set_ramp_step_two_dB")
        self._ramp_step_two_counts = self._quantized_step_counts(step_dB)
        self.command_history.append(("set_ramp_step_two_dB", counts_to_db(self._ramp_step_two_counts)))

    def get_ramp_dwell_time_ms(self) -> int:
        self._require_connected("get_ramp_dwell_time_ms")
        return self._ramp_dwell_ms

    def set_ramp_dwell_time_ms(self, dwell_time_ms: int) -> None:
        self._require_connected("set_ramp_dwell_time_ms")
        self._ramp_dwell_ms = self._validated_time(dwell_time_ms, minimum_ms=1, name="dwell time")
        self.command_history.append(("set_ramp_dwell_time_ms", self._ramp_dwell_ms))

    def get_ramp_dwell_time_two_ms(self) -> int:
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "get_ramp_dwell_time_two_ms")
        return self._ramp_dwell_two_ms

    def set_ramp_dwell_time_two_ms(self, dwell_time_ms: int) -> None:
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "set_ramp_dwell_time_two_ms")
        self._ramp_dwell_two_ms = self._validated_time(dwell_time_ms, minimum_ms=1, name="dwell time")
        self.command_history.append(("set_ramp_dwell_time_two_ms", self._ramp_dwell_two_ms))

    def get_ramp_idle_time_ms(self) -> int:
        self._require_connected("get_ramp_idle_time_ms")
        return self._ramp_idle_ms

    def set_ramp_idle_time_ms(self, idle_time_ms: int) -> None:
        self._require_connected("set_ramp_idle_time_ms")
        self._ramp_idle_ms = self._validated_time(idle_time_ms, minimum_ms=0, name="idle time")
        self.command_history.append(("set_ramp_idle_time_ms", self._ramp_idle_ms))

    def get_ramp_hold_time_ms(self) -> int:
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "get_ramp_hold_time_ms")
        return self._ramp_hold_ms

    def set_ramp_hold_time_ms(self, hold_time_ms: int) -> None:
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "set_ramp_hold_time_ms")
        self._ramp_hold_ms = self._validated_time(hold_time_ms, minimum_ms=0, name="hold time")
        self.command_history.append(("set_ramp_hold_time_ms", self._ramp_hold_ms))

    def set_ramp_direction(self, up: bool) -> None:
        self._require_connected("set_ramp_direction")
        self._ramp_up = bool(up)
        self.command_history.append(("set_ramp_direction", self._ramp_up))

    def set_ramp_repeat(self, repeat: bool) -> None:
        self._require_connected("set_ramp_repeat")
        self._ramp_repeat = bool(repeat)
        self.command_history.append(("set_ramp_repeat", self._ramp_repeat))

    def set_ramp_bidirectional(self, enabled: bool) -> None:
        self._require_feature(HAS_BIDIR_RAMPS, "HAS_BIDIR_RAMPS", "set_ramp_bidirectional")
        self._ramp_bidirectional = bool(enabled)
        self.command_history.append(("set_ramp_bidirectional", self._ramp_bidirectional))

    def start_ramp(self) -> None:
        self._require_connected("start_ramp")
        self._ramping = True
        self.command_history.append(("start_ramp",))

    def stop_ramp(self) -> None:
        self._require_connected("stop_ramp")
        self._ramping = False
        self.command_history.append(("stop_ramp",))

    def start_ramp_multichannel(self, channels: Sequence[int], repeat: bool = False,
                                deferred: bool = False) -> None:
        self._require_usb("start_ramp_multichannel", "fnLDA_StartRampMC")
        self._require_feature(HAS_MCHANNELS, "HAS_MCHANNELS", "start_ramp_multichannel")
        if not channels:
            raise ValueError("channels must contain at least one channel number")
        for channel in channels:
            self._validated_channel(channel)
        self._ramping = not deferred
        self.command_history.append(("start_ramp_multichannel", tuple(channels), repeat, deferred))

    def is_ramping(self) -> bool:
        self._require_usb("is_ramping", "fnLDA_GetDeviceStatus")
        self._require_connected("is_ramping")
        return self._ramping

    # ==================== profile ====================

    def get_profile_max_length(self) -> int:
        self._require_connected("get_profile_max_length")
        return self._profile_max_length

    def get_profile_count(self) -> int:
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "get_profile_count")
        return self._profile_count

    def set_profile_count(self, count: int) -> None:
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "set_profile_count")
        count = int(count)
        if not 1 <= count <= self._profile_max_length:
            raise ValueError(
                f"profile count={count} is outside [1, {self._profile_max_length}] for "
                f"{self._model_name} serial {self.serial_number}"
            )
        self._profile_count = count
        self.command_history.append(("set_profile_count", count))

    def get_profile_element_dB(self, index: int) -> float:
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "get_profile_element_dB")
        return counts_to_db(self._profile_counts[self._validated_profile_index(index)])

    def set_profile_element_dB(self, index: int, attenuation_dB: float) -> None:
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "set_profile_element_dB")
        validated = self._validated_profile_index(index)
        counts = self._quantize_attenuation_counts(attenuation_dB)
        self._profile_counts[validated] = counts
        self.command_history.append(("set_profile_element_dB", validated, counts_to_db(counts)))

    def set_profile_dB(self, attenuations_dB: Sequence[float]) -> None:
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "set_profile_dB")
        if not attenuations_dB:
            raise ValueError("attenuations_dB must contain at least one point")
        if len(attenuations_dB) > self._profile_max_length:
            raise ValueError(
                f"profile has {len(attenuations_dB)} points but {self._model_name} serial "
                f"{self.serial_number} holds at most {self._profile_max_length}"
            )
        for index, attenuation_dB in enumerate(attenuations_dB):
            self.set_profile_element_dB(index, attenuation_dB)
        self.set_profile_count(len(attenuations_dB))

    def get_profile_dwell_time_ms(self) -> int:
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "get_profile_dwell_time_ms")
        return self._profile_dwell_ms

    def set_profile_dwell_time_ms(self, dwell_time_ms: int) -> None:
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "set_profile_dwell_time_ms")
        self._profile_dwell_ms = self._validated_time(dwell_time_ms, minimum_ms=1, name="dwell time")
        self.command_history.append(("set_profile_dwell_time_ms", self._profile_dwell_ms))

    def get_profile_idle_time_ms(self) -> int:
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "get_profile_idle_time_ms")
        return self._profile_idle_ms

    def set_profile_idle_time_ms(self, idle_time_ms: int) -> None:
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "set_profile_idle_time_ms")
        self._profile_idle_ms = self._validated_time(idle_time_ms, minimum_ms=0, name="idle time")
        self.command_history.append(("set_profile_idle_time_ms", self._profile_idle_ms))

    def get_profile_index(self) -> int:
        self._require_usb("get_profile_index", "an implemented fnLDA_GetProfileIndex")
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "get_profile_index")
        return self._profile_index

    def start_profile(self, repeat: bool = False) -> None:
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "start_profile")
        self._profile_playing = True
        self.command_history.append(("start_profile", bool(repeat)))

    def stop_profile(self) -> None:
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "stop_profile")
        self._profile_playing = False
        self.command_history.append(("stop_profile",))

    def start_profile_multichannel(self, channels: Sequence[int], repeat: bool = False,
                                   delayed: bool = False) -> None:
        self._require_usb("start_profile_multichannel", "fnLDA_StartProfileMC")
        self._require_feature(HAS_MCHANNELS, "HAS_MCHANNELS", "start_profile_multichannel")
        self._require_feature(HAS_PROFILES, "HAS_PROFILES", "start_profile_multichannel")
        if not channels:
            raise ValueError("channels must contain at least one channel number")
        for channel in channels:
            self._validated_channel(channel)
        self._profile_playing = not delayed
        self.command_history.append(("start_profile_multichannel", tuple(channels), repeat, delayed))

    def is_profile_playing(self) -> bool:
        self._require_usb("is_profile_playing", "fnLDA_GetDeviceStatus")
        self._require_connected("is_profile_playing")
        return self._profile_playing

    # ==================== network ====================

    def get_ip_address(self) -> str:
        self._require_ethernet("get_ip_address")
        self._require_connected("get_ip_address")
        return self.ip_address

    def get_netmask(self) -> str:
        self._require_ethernet("get_netmask")
        self._require_connected("get_netmask")
        return "255.255.255.0"

    def get_gateway(self) -> str:
        self._require_ethernet("get_gateway")
        self._require_connected("get_gateway")
        return "192.168.100.1"

    def get_ip_mode(self) -> str:
        self._require_ethernet("get_ip_mode")
        self._require_connected("get_ip_mode")
        return "static"

    def get_software_version(self) -> str:
        self._require_ethernet("get_software_version")
        self._require_connected("get_software_version")
        return "1.7"

    # ==================== persistence and diagnostics ====================

    def save_settings(self) -> None:
        self._require_connected("save_settings")
        self.saved_settings_count += 1
        self.command_history.append(("save_settings",))

    def get_device_status(self) -> int:
        self._require_usb("get_device_status", "fnLDA_GetDeviceStatus")
        self._require_connected("get_device_status")
        status = DEV_CONNECTED | DEV_OPENED
        if self._ramping:
            status |= SWP_ACTIVE
        if self._profile_playing:
            status |= PROFILE_ACTIVE
        return status

    def set_trace_level(self, trace_level: int, io_trace_level: int, verbose: bool) -> None:
        self._require_usb("set_trace_level", "fnLDA_SetTraceLevel")
        self._require_connected("set_trace_level")
        self.command_history.append(("set_trace_level", trace_level, io_trace_level, bool(verbose)))

    # ==================================================================
    #                          PRIVATE METHODS
    # ==================================================================

    def _require_connected(self, method: str) -> None:
        if not self.connected:
            raise Vaunix_LDA_Error(f"{method} requires an open connection -- call connect() first.")

    def _require_feature(self, bit: int, bit_name: str, method: str) -> None:
        self._require_connected(method)
        if not self._features & bit:
            raise Vaunix_LDA_Feature_Error(
                f"{method} requires {bit_name}, but {self._model_name} serial {self.serial_number} "
                f"reports features={describe_features(self._features)}."
            )

    def _require_usb(self, method: str, missing_symbol: str) -> None:
        if self.connectionType != "USB":
            raise Vaunix_LDA_Transport_Error(
                f"{method} is not available over Ethernet: VNX_Eth_Attn64.dll has no "
                f"{missing_symbol}. Use Vaunix_LDA_USB_Driver."
            )

    def _require_ethernet(self, method: str) -> None:
        if self.connectionType != "Ethernet":
            raise Vaunix_LDA_Transport_Error(
                f"{method} is not available over USB: VNX_atten64.dll exports no IP functions. "
                f"Use Vaunix_LDA_Ethernet_Driver."
            )

    def _validated_channel(self, channel: int) -> int:
        channel = int(channel)
        if not 1 <= channel <= self._num_channels:
            raise ValueError(
                f"channel={channel} is outside [1, {self._num_channels}] for {self._model_name} "
                f"serial {self.serial_number}. Channels are 1-indexed."
            )
        return channel

    def _validated_profile_index(self, index: int) -> int:
        index = int(index)
        if not 0 <= index < self._profile_max_length:
            raise ValueError(
                f"profile index={index} is outside [0, {self._profile_max_length - 1}] for "
                f"{self._model_name} serial {self.serial_number}. Indices are 0-based."
            )
        return index

    def _validated_time(self, time_ms: int, minimum_ms: int, name: str) -> int:
        time_ms = int(time_ms)
        if time_ms < minimum_ms:
            raise ValueError(f"{name} requires at least {minimum_ms} ms, got {time_ms}")
        return time_ms

    def _quantized_step_counts(self, step_dB: float) -> int:
        span_counts = self._max_atten_counts - self._min_atten_counts
        counts = self._step_counts * round_half_up(db_to_counts(step_dB) / self._step_counts)
        if counts <= 0 or counts > span_counts:
            raise ValueError(
                f"step={step_dB} dB is outside (0, {counts_to_db(span_counts)}] dB for "
                f"{self._model_name} serial {self.serial_number}"
            )
        return counts

    def _quantize_attenuation_counts(self, attenuation_dB: float) -> int:
        '''
        Same rule as the real drivers: reject out of range, quantise the rest onto
        the hardware step grid.
        '''
        attenuation_dB = float(attenuation_dB)
        minimum_dB = counts_to_db(self._min_atten_counts)
        maximum_dB = counts_to_db(self._max_atten_counts)
        step_dB = counts_to_db(self._step_counts)

        if not minimum_dB - 0.5 * step_dB <= attenuation_dB <= maximum_dB + 0.5 * step_dB:
            raise ValueError(
                f"attenuation_dB={attenuation_dB} is outside [{minimum_dB}, {maximum_dB}] dB for "
                f"{self._model_name} serial {self.serial_number}"
            )

        counts = self._step_counts * round_half_up(attenuation_dB / step_dB)
        return max(self._min_atten_counts, min(self._max_atten_counts, counts))
