import threading
import time
import random

from photonicdrivers.Abstract.Connectable import Connectable


class Conn:
    def __init__(self, sleep_min_ms=2, sleep_max_ms=5):
        self.sleep_min = sleep_min_ms / 1000.0
        self.sleep_max = sleep_max_ms / 1000.0

    def _io(self):
        time.sleep(random.uniform(self.sleep_min, self.sleep_max))

    def query(self, cmd):
        self._io()
        return f"ok:{cmd}"

    def set(self, option, val):
        self._io()
        return "OK"

    def get(self, option):
        self._io()
        return f"{option}=val"


class Equipment(Connectable):
    def __init__(self, conn):
        self.conn = conn
        self.in_sago = 0

    def status(self):
        if self.in_sago != 0:
            raise AssertionError("status ran during set_and_get_option")
        return self.conn.query("status")

    def set_and_get_option(self, option, val):
        self.in_sago += 1
        try:
            self.set(option, val)
            time.sleep(0.003)
            return self.get(option)
        finally:
            self.in_sago -= 1

    def set(self, option, val):
        return self.conn.set(option, val)

    def get(self, option):
        return self.conn.get(option)


def test_connectable_reentrant_no_deadlock():
    eq = Equipment(Conn())
    t = threading.Thread(target=lambda: eq.set_and_get_option("opt", 1))
    t.start()
    t.join(timeout=1.0)
    assert not t.is_alive(), "set_and_get_option deadlocked (reentrancy broken)"

def test_connectable_mutual_exclusion_deterministic():
    started = threading.Event()
    status_ready = threading.Event()
    allow_exit = threading.Event()
    errors = []

    class DeterministicEquipment(Equipment):
        def set_and_get_option(self, option, val):
            self.in_sago += 1
            started.set()
            try:
                allow_exit.wait(timeout=1.0)
                self.set(option, val)
                time.sleep(0.003)
                return self.get(option)
            finally:
                self.in_sago -= 1

    eq = DeterministicEquipment(Conn(sleep_min_ms=1, sleep_max_ms=1))

    def run_sago():
        try:
            eq.set_and_get_option("opt", 1)
        except Exception as e:
            errors.append(e)

    def run_status():
        try:
            started.wait(timeout=1.0)
            status_ready.set()
            eq.status()
        except Exception as e:
            errors.append(e)

    t1 = threading.Thread(target=run_sago)
    t2 = threading.Thread(target=run_status)

    t1.start()
    t2.start()
    status_ready.wait(timeout=1.0)
    allow_exit.set()
    t1.join(timeout=1.0)
    t2.join(timeout=1.0)

    if errors:
        raise errors[0]


def test_connectable_mutual_exclusion():
    eq = Equipment(Conn())
    stop = threading.Event()
    errors = []

    def run_sago():
        try:
            while not stop.is_set():
                eq.set_and_get_option("opt", 1)
        except Exception as e:
            errors.append(e)
            stop.set()

    def run_status():
        try:
            while not stop.is_set():
                eq.status()
        except Exception as e:
            errors.append(e)
            stop.set()

    threads = [threading.Thread(target=run_sago)]
    threads += [threading.Thread(target=run_status) for _ in range(6)]

    for t in threads:
        t.start()

    time.sleep(2.0)
    stop.set()

    for t in threads:
        t.join()

    if errors:
        raise errors[0]
