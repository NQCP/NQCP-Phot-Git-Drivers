"""SNSPD_SQ_Driver.get_latest_counts / get_counts_sample_number against a fake counts thread
(the manufacturer's SQCounts: a lock, the list cnts, the counter n). No hardware.

    python -m pytest photonicdrivers/tests/test_snspd_sq_driver_counts.py -q
"""
import threading
import time

import pytest

from photonicdrivers.SNSPDs.SNSPD_SQ_Driver import SNSPD_SQ_Driver


class FakeCounts:
    def __init__(self, rows):
        self.lock = threading.Lock()
        self.cnts = [list(r) for r in rows]
        self.n = len(rows)


def driver_with(rows, connected=True):
    driver = SNSPD_SQ_Driver("10.0.0.1", 12000, 12345)      # builds WebSQControl, no connection
    driver.websq.cnts = FakeCounts(rows)
    driver.websq.connected = connected
    return driver


ROWS = [[100.0 + i, 10.0 * i, 20.0 * i, 30.0 * i, 40.0 * i] for i in range(5)]


def test_returns_the_newest_rows_oldest_first():
    assert driver_with(ROWS).get_latest_counts(2) == ROWS[-2:]


def test_does_not_wait_for_new_samples():
    driver = driver_with(ROWS)
    started = time.perf_counter()
    driver.get_latest_counts(3)                               # getCounts(3) would block here
    assert time.perf_counter() - started < 0.1


def test_fewer_rows_when_fewer_arrived_and_none_when_empty():
    assert driver_with(ROWS).get_latest_counts(50) == ROWS
    assert driver_with([]).get_latest_counts(5) == []
    assert driver_with(ROWS).get_latest_counts(0) == []


def test_returns_copies():
    driver = driver_with(ROWS)
    driver.get_latest_counts(1)[0][1] = -1.0
    assert driver.websq.cnts.cnts[-1][1] == ROWS[-1][1]


def test_waits_for_the_writer_lock_rather_than_reading_mid_update():
    driver = driver_with(ROWS)
    with driver.websq.cnts.lock:                              # the receiver is appending
        reader = threading.Thread(target=driver.get_latest_counts, args=(1,))
        reader.start()
        reader.join(0.05)
        assert reader.is_alive()
    reader.join(1.0)
    assert not reader.is_alive()


def test_sample_number_counts_received_rows():
    driver = driver_with(ROWS)
    assert driver.get_counts_sample_number() == 5
    driver.websq.cnts.n += 1
    assert driver.get_counts_sample_number() == 6


def test_not_connected_is_a_clear_error():
    with pytest.raises(RuntimeError, match="not connected"):
        driver_with(ROWS, connected=False).get_latest_counts()
    with pytest.raises(RuntimeError, match="not connected"):
        driver_with(ROWS, connected=False).get_counts_sample_number()
