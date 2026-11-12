import serial
import time
import socket
import threading
import functools

from photonicdrivers.Abstract.Connectable import Connectable


def _locked(method):
    """Runs the method under the driver's lock. A LabServer holds ONE driver object for all its clients
    (notebooks, loggers, GUIs), each in its own thread: the lock keeps one client's command sequence from being
    split by another client's channel switch (2026-11-11 17:22: an X ramp ended on channel 1 = Z)."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        with self._lock:
            return method(self, *args, **kwargs)
    return wrapper


class APS100_PS_Driver(Connectable):
    """
    Attocube APS100 magnet power supply (one or two channels).

    Channel-safe methods (2026-11-12, after the 2026-11-11 X/Z event): select_channel() selects AND checks the
    channel (CHAN?); get_field_on(), get_sweep_mode_on(), start_sweep(), wait_for_sweep() and ramp_channel_to()
    name their channel and select + check it inside one locked call, so no other client of the same driver can
    switch the channel in between. The older methods (set_channel, set_upper_limit, ramp_up, ...) keep their
    behaviour; they now also run under the lock.
    """
    CHANNEL_RETRIES = 2              # extra CHAN attempts before select_channel() raises
    CHANNEL_RETRY_WAIT_S = 0.5
    ZERO_THRESHOLD_KG = 0.005        # |output| below this counts as zero (as the old ramp_to_zero wait)
    ZERO_STANDBY_GRACE_S = 5.0       # at zero but no "Standby" yet: accept after this long
    LIMIT_READBACK_TOLERANCE_KG = 0.0015

    def __init__(self, com_port:str = None, IP_address:str=None, IP_port:float=None,) -> None:
        print("Initialising an APS100 PS Driver. Make sure to set it to REMOTE mode by executing \"set_control_remote\" to control it.")
        print("Also make sure that the PS does not display LOCAL on teh front panel, otherwise it will not accept commands from the computer.")
        print("If it does, press the remote button on the front panel.")
        
        self._lock = threading.RLock()
        self.com_port = com_port
        self.baud_rate = 9600
        self.timeout = 1

        self.termination_char = '\r'

        self.ip_address = IP_address
        self.port_number = IP_port

        if self.com_port is not None:
            print('Connection will be via USB')
            self.connectionType = 'USB'

        elif self.ip_address is not None and self.port_number is not None:
            print('Connection will be via Ethernet')
            self.connectionType = 'Ethernet'

        else:
            print("Either com_port or (IP_address and port) must be provided for APS100_PS_Driver initialization.")

    def connect(self) -> None:
        if self.connectionType == 'USB':
            self.connection = serial.Serial(port=self.com_port, baudrate=self.baud_rate, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE, timeout=self.timeout)

        elif self.connectionType == 'Ethernet':
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.settimeout(5)  # sets the timeout of the receive command.
            self.server_address = (self.ip_address, self.port_number)  # IP address, port
            self.connection.connect(self.server_address)

        else:
            print("Insufficient arguments for connecting the APS100_PS_Driver class")

   
    def disconnect(self) -> None:
        self.connection.close()

    def is_connected(self) -> bool:
        try:
            self.get_id()
            return True
        except Exception:
            return False

    def get_id(self) -> None:
        return self.__query("*IDN?;*ESE 12;*ESE?")

    @_locked
    def get_channel(self) -> str:
        '''
        Returns which output channel is currently controlled (1 or 2)
        '''
        return self.__query("CHAN?")
    
    @_locked
    def set_channel(self, channel_number:int) -> str:
        '''
        Sets which output channel is currently controlled (1 or 2)
        '''
        return self.__write(f"CHAN {channel_number}")
       
    def set_control_remote(self) -> str:
        return self.__write("REMOTE")
    
    def set_control_local(self) -> str:
        return self.__write("LOCAL")
    
    def get_control_mode(self) -> str:
        return "There is no way of asking the PS whether it is in LOCAL or REMOTE mode. Look at the front panel"

    def get_unit(self) -> str:
        return self.__query("UNITS?")
    
    @_locked
    def set_unit(self, unit:str) -> str:
        '''
        Unit options are A or kG.
        Both G and kG will set the unit to kG.
        '''
        # The PS will also accept T and G as an input, but it will set the unit to kG
        if unit == "A" or unit == "kG":
            print(f"Changing unit to {unit}")
            try:
                response = self.__write(f"UNITS {unit}")
                time.sleep(0.5)  # wait for the command to be processed
                print(f"Unit set to {self.get_unit()}")
                return response
            except:
                warning_str = "Set unit failed"
                print(warning_str)
                return warning_str
        else:
            print(f"Trying to set unit to {unit}, but it must be kG or A.")

    @_locked
    def get_lower_limit(self) -> tuple[float, str]:
        ps_unit = self.get_unit()
        raw_response = self.__query("LLIM?")
        if ps_unit == "A":
            limit, unit = raw_response.split("A")
        elif ps_unit == "kG":
            limit, unit = raw_response.split("kG")
        return limit, unit

    @_locked
    def set_lower_limit(self, limit:float, unit:str):
        '''
        unit: should be A or kG
        '''
        ps_unit = self.get_unit()
        if  ps_unit != unit:
            warning_str = f"Trying to set the lower limit to {limit} {unit}, but the power supply unit is {ps_unit}. Ignoring command."
            print(warning_str)
            return warning_str
        return self.__write(f"LLIM {limit}")

    @_locked
    def get_upper_limit(self) -> tuple[float, str]:
        ps_unit = self.get_unit()
        raw_response = self.__query("ULIM?")
        if ps_unit == "A":
            limit, unit = raw_response.split("A")
        elif ps_unit == "kG":
            limit, unit = raw_response.split("kG")
        return limit, unit

    @_locked
    def set_upper_limit(self, limit:float, unit:str):
        '''
        unit: should be A or kG
        '''
        ps_unit = self.get_unit()
        if  ps_unit != unit:
            warning_str = f"Trying to set the upper limit to {limit} {unit}, but the power supply unit is {ps_unit}. Ignoring command."
            print(warning_str)
            return warning_str
        return self.__write(f"ULIM {limit}")
    
    def ramp_up(self, wait_while_ramping:bool=True, target_relative_tolerance:float=0, target_absolute_tolerance:float=0) -> str:
        target = self.get_upper_limit()[0]
        return self.__ramp("SWEEP UP", wait_while_ramping=wait_while_ramping, target=target, target_relative_tolerance=target_relative_tolerance, target_absolute_tolerance=target_absolute_tolerance)
    
    def ramp_down(self, wait_while_ramping:bool=True, target_relative_tolerance:float=0, target_absolute_tolerance:float=0) -> None:
        target = self.get_lower_limit()[0]
        return self.__ramp("SWEEP DOWN", wait_while_ramping=wait_while_ramping, target=target, target_relative_tolerance=target_relative_tolerance, target_absolute_tolerance=target_absolute_tolerance)
    
    def ramp_to_zero(self, wait_while_ramping:bool=True) -> None:
        return self.__ramp("SWEEP ZERO", wait_while_ramping=wait_while_ramping, target=0)
    
    def get_sweep_mode(self) -> str:
        '''
        Returns: "Sweeping up", "Standby", "Pause", "Sweeping to zero", "Sweeping down"
        '''
        return self.__query("SWEEP?")     
    
    @_locked
    def get_current(self, channel:int=None) -> float:
        '''
        Returns the current in A
        '''
        if channel != None:
            self.set_channel(str(channel))        
        
        unit = self.get_unit()

        if unit != "A":
            print("Changing unit to A")
            self.set_unit("A")
            # print(self.get_unit())
        
        response = self.__get_output()
        current = response.rstrip('A')
        return float(current)
    
    # Attocube says the IMAG command should be avoided, as it ignores ramp rate limits.
    # def set_field(self, field_T:float, channel:int=None) -> None:
    #     if channel != None:
    #         self.set_channel(str(channel))
    #     field_kG = field_T*10
    #     return self.__query(f"IMAG {field_kG} G")

    @_locked
    def get_field(self, channel:int=None) -> float:
        '''
        Returns the field in kG. This number is derived from the current used a factor determined at the factory
        '''
        if channel != None:
            print("Changing unit to kG")
            self.set_channel(str(channel))

        unit = self.get_unit()

        if unit != "kG":
            print("Changing unit to kG")
            self.set_unit("kG")
            # print(self.get_unit())   
                 
        response = self.__get_output()
        # print(response)
        # print(self.get_unit())
        field_kG = float(response.rstrip('kG'))
        return field_kG
    
    @_locked
    def query_custom_command(self, command:str) -> str:
        return(self.__query(command))

    ################################ CHANNEL-SAFE METHODS ################################

    @_locked
    def select_channel(self, channel: int) -> None:
        """
        Selects the output channel and checks it with CHAN?; retries CHANNEL_RETRIES times, then raises.
        (2026-11-11: the supply once kept channel 2 after a "CHAN 1" right after a sweep to zero.)
        """
        wanted = str(int(channel))
        reply = None
        for attempt in range(self.CHANNEL_RETRIES + 1):
            self.__write(f"CHAN {wanted}")
            reply = self.__query("CHAN?").strip()
            if reply == wanted:
                return
            time.sleep(self.CHANNEL_RETRY_WAIT_S)
        raise RuntimeError(f"APS100 {self.com_port or self.ip_address}: channel {wanted} not selected - "
                           f"CHAN? answers {reply!r} after {self.CHANNEL_RETRIES + 1} attempts")

    @_locked
    def get_field_on(self, channel: int) -> float:
        """The output of the given channel in kG (selected and checked in the same locked call)."""
        self.select_channel(channel)
        self.__ensure_unit_kG()
        return float(self.__get_output().strip().rstrip("kG"))

    @_locked
    def get_sweep_mode_on(self, channel: int) -> str:
        """The sweep mode of the given channel ("Sweeping up", "Standby", "Pause", ...)."""
        self.select_channel(channel)
        return self.get_sweep_mode().strip()

    @_locked
    def start_sweep(self, channel: int, target_kG: float) -> None:
        """
        Starts the given channel sweeping to target_kG, in one locked call: select + check the channel, kG units,
        the limit (ULIM for a target > 0, LLIM for < 0) set and read back, the channel checked again, then
        SWEEP UP / SWEEP DOWN / SWEEP ZERO. Raises before any SWEEP if a check fails. Returns at once.
        """
        target_kG = float(target_kG)
        self.select_channel(channel)
        self.__ensure_unit_kG()
        if target_kG > 1e-6:
            limit_command, sweep_command = "ULIM", "SWEEP UP"
        elif target_kG < -1e-6:
            limit_command, sweep_command = "LLIM", "SWEEP DOWN"
        else:
            limit_command, sweep_command = None, "SWEEP ZERO"
        if limit_command is not None:
            self.__write(f"{limit_command} {target_kG:.4f}")
            reply = self.__query(f"{limit_command}?").strip()
            try:
                read_back = float(reply.rstrip("kG"))
            except ValueError:
                raise RuntimeError(f"APS100: {limit_command}? answered {reply!r} - no sweep started")
            if abs(read_back - target_kG) > self.LIMIT_READBACK_TOLERANCE_KG:
                raise RuntimeError(f"APS100: {limit_command} reads {read_back} kG on channel {channel}, wanted "
                                   f"{target_kG:.4f} kG - no sweep started")
        reply = self.__query("CHAN?").strip()
        if reply != str(int(channel)):
            raise RuntimeError(f"APS100: channel changed to {reply!r} before {sweep_command} on channel {channel} - "
                               f"no sweep started")
        self.__write(sweep_command)

    @_locked
    def pause_sweep(self, channel: int) -> None:
        """SWEEP PAUSE on the given channel (holds its present output)."""
        self.select_channel(channel)
        self.__write("SWEEP PAUSE")

    def wait_for_sweep(self, channel: int, target_kG: float, relative_tolerance: float = 0,
                       absolute_tolerance: float = 0, timeout_s: float = 1800, poll_s: float = 0.5,
                       watch_channel: int = None, watch_tolerance_kG: float = 0.02) -> float:
        """
        Waits until the channel's output reaches target_kG and returns it [kG]. Not locked as a whole (other
        clients can read between polls); every poll names its channel.

        Done: target 0 -> |output| < ZERO_THRESHOLD_KG and SWEEP? "Standby" (or ZERO_STANDBY_GRACE_S at zero);
        target != 0 -> |output - target| <= absolute_tolerance and <= relative_tolerance * |target| (both, as the old
        ramp wait; 1e-6 kG floor). Raises on timeout, or if the sweep stops ("Standby"/"Pause") away from the target.

        watch_channel: the OTHER channel of a dual supply. If its output moves by more than watch_tolerance_kG
        during the wait, it is paused (SWEEP PAUSE) and this raises - a sweep landed on the wrong channel.
        """
        target_kG = float(target_kG)
        deadline = time.time() + timeout_s
        watch_start = self.get_field_on(watch_channel) if watch_channel is not None else None
        at_zero_since = None
        while True:
            time.sleep(poll_s)
            output = self.get_field_on(channel)
            mode = self.get_sweep_mode_on(channel)
            print(f"APS100 channel {channel}: {mode}, output {output:.4f} kG, target {target_kG:.4f} kG")
            if watch_channel is not None:
                watched = self.get_field_on(watch_channel)
                if abs(watched - watch_start) > watch_tolerance_kG:
                    self.pause_sweep(watch_channel)
                    raise RuntimeError(f"APS100: channel {watch_channel} moved from {watch_start:.4f} to "
                                       f"{watched:.4f} kG while channel {channel} was ramping - paused it")
            if target_kG == 0:
                if abs(output) < self.ZERO_THRESHOLD_KG:
                    if mode == "Standby":
                        return output
                    at_zero_since = at_zero_since or time.time()
                    if time.time() - at_zero_since >= self.ZERO_STANDBY_GRACE_S:
                        return output
                else:
                    at_zero_since = None
            else:
                deviation = abs(output - target_kG)
                if deviation <= max(absolute_tolerance, 1e-6) and \
                        deviation <= max(relative_tolerance * abs(target_kG), 1e-6):
                    return output
                if mode in ("Standby", "Pause"):
                    raise RuntimeError(f"APS100: channel {channel} stopped ({mode}) at {output:.4f} kG, target "
                                       f"{target_kG:.4f} kG")
            if time.time() > deadline:
                raise RuntimeError(f"APS100: channel {channel} did not reach {target_kG:.4f} kG within {timeout_s:g} s "
                                   f"(output {output:.4f} kG, {mode})")

    def ramp_channel_to(self, channel: int, target_kG: float, relative_tolerance: float = 0,
                        absolute_tolerance: float = 0, timeout_s: float = 1800, watch_channel: int = None,
                        watch_tolerance_kG: float = 0.02) -> float:
        """start_sweep() then wait_for_sweep(); returns the output reached [kG]."""
        self.start_sweep(channel, target_kG)
        return self.wait_for_sweep(channel, target_kG, relative_tolerance=relative_tolerance,
                                   absolute_tolerance=absolute_tolerance, timeout_s=timeout_s,
                                   watch_channel=watch_channel, watch_tolerance_kG=watch_tolerance_kG)

    ################################ PRIVATE METHODS ################################

    # Attocube says the IMAG command should be avoided, as it ignores ramp rate limits.
    # def set_current(self, current_A:float, channel:int=None) -> None:
    #     # if channel != None:
    #     #     self.set_channel(str(channel))
    #     return self.__query(f"IMAG {current_A}")
    
    def __ensure_unit_kG(self) -> None:
        if self.__query("UNITS?").strip() != "kG":
            self.__write("UNITS kG")
            time.sleep(0.5)
            unit = self.__query("UNITS?").strip()
            if unit != "kG":
                raise RuntimeError(f"APS100: units are {unit!r}, could not set kG")

    def __get_output(self, channel:int=None) -> str:
        '''
        Returns the output of the power supply in whatever unit it is in.
        '''
        return self.__query("IOUT?")
        # return self.__query("IMAG?")

    def __ramp(self, command:str, wait_while_ramping:bool, target:float, target_relative_tolerance:float=0, target_absolute_tolerance:float=0) -> str:
        with self._lock:
            # the channel this sweep goes to: polled by name below, so another client's channel switch during the
            # wait can no longer make this loop read (and stop on) the other channel
            try:
                ramp_channel = int(self.__query("CHAN?").strip())
            except ValueError:
                ramp_channel = None
            self.__write(command)
        status = "unknown"
        if wait_while_ramping: 
            print("Checking if with the current ramp rates, the PS never really reaches the target field") # Can be removed later if ramp rates are made less cautious
            within_tolerance = False            

            ps_unit = self.get_unit()

            while status != "Standby" and not within_tolerance:
                time.sleep(0.5)
                status = self.get_sweep_mode_on(ramp_channel) if ramp_channel is not None else self.get_sweep_mode().strip()

                # raw_output = self.__get_output()
                # print(f"Raw output from __get_output: {raw_output}")

                
                # output = None
                # unit = None                
                # if ps_unit == "A":
                #     output, unit = raw_output.split("A")
                # elif ps_unit == "kG":
                #     output, unit = raw_output.split("kG")
                # print("unit = {}".format(unit))

                output = self.get_field_on(ramp_channel) if ramp_channel is not None else self.get_field()
                # print(f"Output from get_field: {output} {ps_unit}")

                if target != 0:
                    relative_deviation = abs((float(output) - float(target)) / float(target))        
                    absolute_deviation = abs(float(output) - float(target))    
                    if relative_deviation < target_relative_tolerance and absolute_deviation < target_absolute_tolerance:
                        within_tolerance = True

                    print(f"Status: {status}, Output: {output} {ps_unit}, Tolerance: {target_relative_tolerance}, Deviation: {relative_deviation}")
                else:
                    # Absolute threshold: exit when within 0.005 kG of zero.
                    # This handles both positive and negative starting fields, and acts
                    # as a fallback if the device never returns "Standby".
                    if abs(float(output)) < 0.005:
                        within_tolerance = True
                    print(f"Status: {status}, Output: {output} {ps_unit}, Target is zero (exit when |output| < 0.005 kG).")

                

    def __read(self) -> str:
        '''
        Reads a response from the device.
        '''
        if self.connectionType == 'USB':
            response_raw = self.connection.readline()
            response = response_raw.decode('utf-8').strip()
            # print(f"Raw response: {response_raw}")     
            # print(f"Received response: {response}")

        elif self.connectionType == 'Ethernet':
            response = self.connection.recv(1024)
            # remove the newline characters if present
            if b"\r\n" in response:
                response, dummy = response.split(b'\r\n')

            # convert from byte string to string
            response = response.decode('utf-8').strip()
        else:
            raise Exception("ERROR in APS100_PS_Driver class - connection has not been initialised properly")
        # print(f"Received response: {response}")
        return response
        
    @_locked
    def __write(self, command_str:str) -> None:
        '''
        Writes a command to the device.
        '''
        command = command_str + self.termination_char  
        # print(f"Sending command: {command}")

        if self.connectionType == 'USB':                
            self.connection.reset_input_buffer()  # a late echo / reply left over would shift every later reply
            self.connection.write(command.encode('utf-8'))            
            reflected_command = self.connection.readline() # The power supply first returns the command that was sent to it:

            # print(f"Reflected command: {reflected_command.decode('utf-8').strip()}")

        elif self.connectionType == 'Ethernet':
            self.connection.sendall(command.encode())

        else:
            raise Exception("ERROR in APS100_PS_Driver class - connection has not been initialised properly")\
            
    @_locked
    def __query(self, command:str) -> str:
        '''
        Sends a command to the device and returns the response.
        '''
        self.__write(command)
        response = self.__read()
        
        return response

class APS100_PS_Driver_Stub(Connectable):
    def __init__(self) -> None:
        pass

    def connect(self) -> None:
        pass
   
    def disconnect(self) -> None:
        pass

    def is_connected(self) -> bool:
        return True

    def get_id(self) -> None:
        return "Mock APS100 Power Supply Driver"

    def get_channel(self) -> str:
        '''
        Returns which output channel is currently controlled (1 or 2)
        '''
        return 1
    
    def set_channel(self, channel_number:int) -> str:
        pass
       
    def set_control_remote(self) -> str:
        pass
    
    def set_control_local(self) -> str:
        pass
    
    def get_control_mode(self) -> str:
        return "There is no way of asking the PS whether it is in LOCAL or REMOTE mode. Look at the front panel"

    def get_unit(self) -> str:
        return "T"
    
    def set_unit(self, unit:str) -> str:
        pass

    def get_lower_limit(self) -> str:
        return 0

    def set_lower_limit(self, limit:float, unit:str):
        pass

    def get_upper_limit(self) -> tuple[float, str]:
        return 2

    def set_upper_limit(self, limit:float, unit:str):
        pass
    
    def ramp_up(self, wait_while_ramping:bool=True, target_relative_tolerance:float=0) -> str:
        pass  
      
    def ramp_down(self, wait_while_ramping:bool=True, target_relative_tolerance:float=0) -> None:
        pass
    
    def ramp_to_zero(self, wait_while_ramping:bool=True) -> None:
        pass
    
    def get_sweep_mode(self) -> str:
        '''
        Returns: "Sweeping up", "Standby", "Pause", "Sweeping to zero", "Sweeping down"
        '''
        return "Mock APS100 Power Supply Driver"     
    
    def get_current(self, channel:int=None) -> float:
        '''
        Returns the current in A
        '''
        return 0
    
    # Attocube says the IMAG command should be avoided, as it ignores ramp rate limits.
    # def set_field(self, field_T:float, channel:int=None) -> None:
    #     if channel != None:
    #         self.set_channel(str(channel))
    #     field_kG = field_T*10
    #     return self.__query(f"IMAG {field_kG} G")

    def get_field(self, channel:int=None) -> float:
        '''
        Returns the field in kG. This number is derived from the current used a factor determined at the factory
        '''
        return 0
    

