"""
APS100_PS_Stub - A robust simulator for the APS100 Power Supply
Simulates the behavior of the Attocube APS100 magnetic power supply without requiring hardware.
"""

import time
import threading
from photonicdrivers.Abstract.Connectable import Connectable


class APS100_PS_Stub(Connectable):
    """
    A robust stub implementation of the APS100 Power Supply.
    
    This stub simulates the behavior of the Attocube APS100 magnetic power supply,
    including ramping with configurable rates, dual-channel support, and thread-safe operations.
    
    Supports both USB and Ethernet connection specifications (though these are simulated).
    """
    
    def __init__(self, com_port: str = None, IP_address: str = None, IP_port: float = None) -> None:
        """
        Initialize the APS100_PS_Stub.
        
        Args:
            com_port: COM port for USB connection (optional)
            IP_address: IP address for Ethernet connection (optional)
            IP_port: Port number for Ethernet connection (optional)
        """
        self.connected = False
        self.mode = "local"
        self.unit = "kG"
        self.channel = 1
        
        # Connection parameters (recorded but not used for stub)
        self.port = com_port
        self.ip_address = IP_address
        self.port_number = IP_port
        
        # Determine connection type for logging
        if com_port is not None:
            self.connectionType = 'USB'
            print(f'Stub connection will simulate USB on port {com_port}')
        elif IP_address is not None and IP_port is not None:
            self.connectionType = 'Ethernet'
            print(f'Stub connection will simulate Ethernet to {IP_address}:{IP_port}')
        else:
            self.connectionType = 'STUB'
            print('Stub connection type: STUB (simulated)')
        
        # Thread safety
        self._lock = threading.RLock()
        self._stop_events = {1: threading.Event(), 2: threading.Event()}
        self._ramp_threads = {1: None, 2: None}
        
        # Simulated device state
        self._sweep_mode = {1: "Standby", 2: "Standby"}
        self._current_kG = {1: 0.0, 2: 0.0}
        self._lower_limit_kG = {1: -10.0, 2: -10.0}
        self._upper_limit_kG = {1: 10.0, 2: 10.0}
        self._ramp_rate_kG_per_s = 2  # Configurable ramp rate

    def connect(self) -> None:
        """Connect to the device (simulated)."""
        self.connected = True
        print("Stub: Connected")

    def disconnect(self) -> None:
        """Disconnect from the device."""
        with self._lock:
            self.connected = False
            for ev in self._stop_events.values():
                ev.set()
        print("Stub: Disconnected")

    def is_connected(self) -> bool:
        """Check if connected."""
        return self.connected

    def get_id(self) -> str:
        """Get device ID."""
        if not self.connected:
            raise RuntimeError("Device not connected")
        return "Stub APS100 Power Supply"

    def get_channel(self) -> str:
        """Get currently selected channel (1 or 2)."""
        return str(self.channel)

    def set_channel(self, channel_number: int) -> str:
        """
        Set the active channel.
        
        Args:
            channel_number: Channel 1 or 2
            
        Raises:
            ValueError: If channel is not 1 or 2
        """
        if channel_number not in (1, 2):
            raise ValueError("APS100 stub only supports channels 1 and 2")
        self.channel = int(channel_number)
        return "OK"

    def set_control_remote(self) -> str:
        """Set device to remote control mode."""
        self.mode = "remote"
        return "OK"

    def set_control_local(self) -> str:
        """Set device to local mode."""
        self.mode = "local"
        return "OK"

    def get_control_mode(self) -> str:
        """Get current control mode."""
        return self.mode

    def get_unit(self) -> str:
        """Get current unit (A or kG)."""
        return self.unit

    def set_unit(self, unit: str) -> str:
        """
        Set the measurement unit.
        
        Args:
            unit: 'A' (amperes) or 'kG' (kilogauss). 'G' and 'T' are converted to 'kG'.
            
        Raises:
            ValueError: If unit is not valid
        """
        if unit in ("A", "kG", "G", "T"):
            # G and T are converted to kG as per actual device
            self.unit = "kG" if unit in ("G", "T") else unit
            return "OK"
        raise ValueError("Unit must be A, kG, G, or T")

    def get_lower_limit(self) -> str:
        """Get the lower field limit for the current channel."""
        return f"{self._lower_limit_kG[self.channel]}{self.unit}"

    def set_lower_limit(self, limit: float, unit: str) -> str:
        """
        Set the lower field limit.
        
        Args:
            limit: Lower limit value
            unit: Unit for the limit (must match current unit)
            
        Returns:
            "OK" on success, warning string if unit mismatch
        """
        if unit != self.unit:
            warning_str = (
                f"Trying to set the lower limit to {limit} {unit}, but the power supply unit is {self.unit}. "
                "Ignoring command."
            )
            print(warning_str)
            return warning_str
        self._lower_limit_kG[self.channel] = float(limit)
        return "OK"

    def get_upper_limit(self) -> tuple[float, str]:
        """Get the upper field limit for the current channel."""
        return self._upper_limit_kG[self.channel], self.unit

    def set_upper_limit(self, limit: float, unit: str) -> str:
        """
        Set the upper field limit.
        
        Args:
            limit: Upper limit value
            unit: Unit for the limit (must match current unit)
            
        Returns:
            "OK" on success, warning string if unit mismatch
        """
        if unit != self.unit:
            warning_str = (
                f"Trying to set the upper limit to {limit} {unit}, but the power supply unit is {self.unit}. "
                "Ignoring command."
            )
            print(warning_str)
            return warning_str
        self._upper_limit_kG[self.channel] = float(limit)
        return "OK"

    def ramp_up(self, wait_while_ramping: bool = True, target_relative_tolerance: float = 0, target_absolute_tolerance: float = 0) -> str:
        """
        Ramp the field up to the upper limit.
        
        Args:
            wait_while_ramping: Whether to block until ramping completes
            target_relative_tolerance: Tolerance for reaching target (as fraction)
            target_absolute_tolerance: Absolute tolerance for reaching target
            
        Returns:
            "OK" on success
        """
        target = self.get_upper_limit()[0]
        return self._ramp("SWEEP UP", wait_while_ramping=wait_while_ramping, target=target,
                          target_relative_tolerance=target_relative_tolerance, target_absolute_tolerance=target_absolute_tolerance)

    def ramp_down(self, wait_while_ramping: bool = True, target_relative_tolerance: float = 0, target_absolute_tolerance: float = 0) -> str:
        """
        Ramp the field down to the lower limit.
        
        Args:
            wait_while_ramping: Whether to block until ramping completes
            target_relative_tolerance: Tolerance for reaching target (as fraction)
            target_absolute_tolerance: Absolute tolerance for reaching target
            
        Returns:
            "OK" on success
        """
        target = self._lower_limit_kG[self.channel]
        return self._ramp("SWEEP DOWN", wait_while_ramping=wait_while_ramping, target=target,
                          target_relative_tolerance=target_relative_tolerance, target_absolute_tolerance=target_absolute_tolerance)

    def ramp_to_zero(self, wait_while_ramping: bool = True) -> str:
        """
        Ramp the field to zero.
        
        Args:
            wait_while_ramping: Whether to block until ramping completes
            
        Returns:
            "OK" on success
        """
        return self._ramp("SWEEP ZERO", wait_while_ramping=wait_while_ramping, target=0.0)

    def get_sweep_mode(self) -> str:
        """
        Get the current sweep mode.
        
        Returns:
            "Standby", "Sweeping up", "Sweeping down", or "Sweeping to zero"
        """
        return self._sweep_mode[self.channel]

    def get_current(self, channel: int = None) -> float:
        """
        Get the current output in Amperes.
        
        Args:
            channel: Optionally specify a channel to read from
            
        Returns:
            Current in Amperes
        """
        if channel is not None:
            self.set_channel(channel)
        if self.unit != "A":
            original_unit = self.unit
            self.set_unit("A")
        return float(self._current_kG[self.channel])

    def get_field(self, channel: int = None) -> float:
        """
        Get the current field in kiloGauss.
        
        Args:
            channel: Optionally specify a channel to read from
            
        Returns:
            Field in kiloGauss
        """
        if channel is not None:
            self.set_channel(channel)
        if self.unit != "kG":
            self.set_unit("kG")
        return float(self._current_kG[self.channel])

    def query_custom_command(self, command: str) -> str:
        """
        Send a custom command and get the response.
        
        Args:
            command: Command string
            
        Returns:
            Response string
        """
        return self._query(command)
    
    def set_ramp_rate(self, rate_kG_per_s: float) -> str:
        """
        Set the ramp rate for field changes.
        
        Args:
            rate_kG_per_s: Ramp rate in kG/second
            
        Returns:
            "OK"
        """
        if rate_kG_per_s <= 0:
            raise ValueError("Ramp rate must be positive")
        self._ramp_rate_kG_per_s = float(rate_kG_per_s)
        return "OK"

    def get_ramp_rate(self) -> float:
        """Get the current ramp rate in kG/second."""
        return self._ramp_rate_kG_per_s

    ################################ PRIVATE METHODS ################################

    def _ramp(self, command: str, wait_while_ramping: bool, target: float, 
              target_relative_tolerance: float = 0, target_absolute_tolerance: float = 0) -> str:
        """
        Internal method to perform a ramp operation.
        
        Args:
            command: Ramp command ("SWEEP UP", "SWEEP DOWN", "SWEEP ZERO")
            wait_while_ramping: Whether to block until complete
            target: Target field value
            target_relative_tolerance: Tolerance for reaching target (as fraction)
            target_absolute_tolerance: Absolute tolerance for reaching target
            
        Returns:
            "OK"
        """
        channel = self.channel

        with self._lock:
            # Stop any existing ramp
            self._stop_events[channel].set()
            self._stop_events[channel] = threading.Event()
            stop_event = self._stop_events[channel]
            self._sweep_mode[channel] = self._command_to_mode(command)

        # Start ramp in background thread
        thread = threading.Thread(
            target=self._ramp_worker,
            args=(channel, float(target), stop_event, target_relative_tolerance, target_absolute_tolerance),
            daemon=True,
        )
        self._ramp_threads[channel] = thread
        thread.start()

        if wait_while_ramping:
            thread.join()

        return "OK"

    def _ramp_worker(self, channel: int, target: float, stop_event: threading.Event, 
                     target_relative_tolerance: float = 0, target_absolute_tolerance: float = 0) -> None:
        """
        Worker thread for performing ramp operations.
        
        Simulates smooth ramping from current value to target at the configured ramp rate.
        Stops when target is reached within the specified tolerances.
        """
        dt = 0.05  # timestep in seconds
        step = self._ramp_rate_kG_per_s * dt

        while not stop_event.is_set():
            with self._lock:
                current = self._current_kG[channel]

            delta = target - current
            
            # Check if we've reached target within tolerances
            relative_error = abs(delta) / abs(target) if target != 0 else abs(delta)
            absolute_error = abs(delta)
            
            if relative_error <= target_relative_tolerance or absolute_error <= target_absolute_tolerance:
                # Close enough to target
                with self._lock:
                    self._current_kG[channel] = target
                    self._sweep_mode[channel] = "Standby"
                break
            
            # Calculate next value
            if abs(delta) <= step:
                next_value = target
            else:
                next_value = current + step if delta > 0 else current - step

            with self._lock:
                self._current_kG[channel] = next_value

            time.sleep(dt)

        # Final update and status
        with self._lock:
            self._current_kG[channel] = target
            self._sweep_mode[channel] = "Standby"

    def _command_to_mode(self, command: str) -> str:
        """Convert ramp command to sweep mode string."""
        mode_map = {
            "SWEEP UP": "Sweeping up",
            "SWEEP DOWN": "Sweeping down",
            "SWEEP ZERO": "Sweeping to zero",
        }
        return mode_map.get(command, "Pause")

    def _query(self, command: str) -> str:
        """
        Process a query command and return the response.
        
        Args:
            command: Query command
            
        Returns:
            Response string
        """
        command_lower = command.upper()
        
        response_map = {
            "SWEEP?": self.get_sweep_mode(),
            "UNITS?": self.unit,
            "CHAN?": str(self.channel),
            "LLIM?": self.get_lower_limit(),
            "ULIM?": f"{self._upper_limit_kG[self.channel]}{self.unit}",
            "IOUT?": f"{self._current_kG[self.channel]}{self.unit}",
            "*IDN?;*ESE 12;*ESE?": self.get_id(),
        }
        
        return response_map.get(command_lower, "OK")


