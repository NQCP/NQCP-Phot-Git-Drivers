import queue
import threading

from Instruments.Settings.Console_Controller import Console_Controller


class CameraAcquisitionThread(threading.Thread):
    def __init__(self, power_meter):
        super(CameraAcquisitionThread, self).__init__()
        self.power_meter = power_meter
        self.power_queue = queue.Queue(maxsize=1)
        self.is_alive = False
        self.stop_event = threading.Event()

    def get_queue(self):
        return self.power_queue

    def stop(self):
        self.stop_event.set()

    def run(self):
        self.is_alive = True
        while not self.stop_event.is_set():
            self._iteration()
        self._stop()

    def _iteration(self):
        try:
            if not self.power_meter.get_is_connected():
                raise Exception("Power meter is not connected")

            power = self.power_meter.get_pending_power()
            self.power_queue.put_nowait(power)
        except queue.Full:
            pass
        except Exception as error:
            self.stop()

    def _stop(self):
        Console_Controller.print_message("Image acquisition has stopped")
        self.is_alive = False

    def get_is_alive(self):
        return self.is_alive
