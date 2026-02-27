# https://www.swabianinstruments.com/static/documentation/PulseStreamer/

from instruments.example import Driver
from photonicdrivers.Abstract.Connectable import Connectable

from qm import SimulationConfig, LoopbackInterface
from qm.qua import *
from qm import QuantumMachinesManager

import time 
import numpy as np
    
HIGH = 1
LOW = 0
HIGH = 1
LOW = 0

class OPX_Driver(Connectable):
    def __init__(self, ip_address='10.209.64.242', cluster_name="Cluster_1", qop_port=None):
        self.ip_address = ip_address
        self.cluster_name = cluster_name
        self.qop_port = qop_port
        self.sequence_stack = []

    def connect(self) -> None:
        ### Create a QuantumMachinesManager instance for the OPX and set it as the driver
        self.driver = QuantumMachinesManager(host=self.ip_address, port=self.qop_port, cluster_name=self.cluster_name)
    
    def disconnect(self) -> None:
        self.driver = None
    
    def is_connected(self) -> bool:
        try:
            self.driver.list_open_qms()
            return True
        except Exception:
            return False
    
    def open_quantum_machine(self, config):
        return self.driver.open_qm(config=config)
    
    def is_quantum_machine_open(self):
        if len(self.driver.list_open_qms()) > 0:
            return True
        else:
            return False

    def _get_quantum_machine_id(self):
        open_qms_id = self.driver.list_open_qms()
        if len(open_qms_id) == 0:
            raise Exception("No quantum machine is currently open.")
        elif len(open_qms_id) > 1:
            raise Exception("Multiple quantum machines are currently open. Please specify the machine_id.")
        else:
            return open_qms_id[0]    
    
    def get_quantum_machine(self):
        if self.is_quantum_machine_open():
            machine_id = self._get_quantum_machine_id()
            return self.driver.get_qm(machine_id=machine_id)
        else:
            raise Exception("Quantum machine is not currently open.")
    
    def add_sequence_step(self, pulse=None, element=None, duration=None):
        program_step = {}
        if pulse is not None:
            program_step["pulse"] = pulse
        if element is not None:
            program_step["element"] = element
        if duration is not None:
            program_step["duration"] = duration
        self.sequence_stack.append(program_step)

    def execute_program(self):
        with program() as sequence_program:
            for step in self.sequence_stack:
                if "pulse" in step and "element" in step and "duration" in step:
                    play(pulse=step["pulse"], element=step["element"], duration=step["duration"])
                elif "pulse" in step and "element" in step:
                    play(pulse=step["pulse"], element=step["element"])
                elif "pulse" in step and "duration" in step:
                    play(pulse=step["pulse"], duration=step["duration"])
                elif "element" in step and "duration" in step:
                    play(element=step["element"], duration=step["duration"])
                elif "pulse" in step:
                    play(pulse=step["pulse"])
                elif "element" in step:
                    play(element=step["element"])
                elif "duration" in step:
                    play(duration=step["duration"])

        job = self.get_quantum_machine().execute(sequence_program)
        print(job.get_status())

    def close_all_quantum_machines(self):
        self.driver.close_all_qms()

    def clear_all_job_results(self):
        self.driver.clear_all_job_results()

    def get_controllers(self):
        return self.driver.get_controllers()
    
    def get_devices(self):
        return self.driver.get_devices()
        