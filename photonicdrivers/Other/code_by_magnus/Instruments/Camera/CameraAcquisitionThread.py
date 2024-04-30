""" ImageAcquisitionThread

This class derives from threading.Thread and is given a TLCamera instance during initialization. When started, the
thread continuously acquires frames from the camera and converts them to PIL Image objects. These are placed in a
queue.Queue object that can be retrieved using get_output_queue(). The thread doesn't do any arming or triggering,
so users will still need to setup and control the camera from a different thread. Be sure to call stop() when it is
time for the thread to stop.

"""
import queue
import threading

from Instruments.Settings.Console_Controller import Console_Controller
from PIL import Image
from thorlabs_tsi_sdk.tl_camera_enums import SENSOR_TYPE
from thorlabs_tsi_sdk.tl_mono_to_color_processor import MonoToColorProcessorSDK


class NoneThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        pass

    def stop(self):
        pass

    def get_is_alive(self):
        return False


class CameraAcquisitionThread(threading.Thread):

    def __init__(self, camera):
        super(CameraAcquisitionThread, self).__init__()
        self.camera = camera
        self.camera_driver = self.camera.get_driver()
        self.image_queue =  queue.Queue(maxsize=1)
        self.is_alive = False

        # setup color processing if necessary
        self._mono_to_color_sdk = MonoToColorProcessorSDK()
        self._image_width = self.camera_driver.image_width_pixels
        self._image_height = self.camera_driver.image_height_pixels
        self._mono_to_color_processor = self._mono_to_color_sdk.create_mono_to_color_processor(
            SENSOR_TYPE.BAYER,
            self.camera_driver.color_filter_array_phase,
            self.camera_driver.get_color_correction_matrix(),
            self.camera_driver.get_default_white_balance_matrix(),
            self.camera_driver.bit_depth
        )

        self._bit_depth = self.camera_driver.bit_depth
        self.camera_driver.image_poll_timeout_ms = 0  # Do not want to block for long periods of time
        self.stop_event = threading.Event()

    def get_queue(self):
        return self.image_queue

    def stop(self):
        self.stop_event.set()

    def _get_color_image(self, frame):
        width = frame.image_buffer.shape[1]
        height = frame.image_buffer.shape[0]

        if (width != self._image_width) or (height != self._image_height):
            self._image_width = width
            self._image_height = height
            Console_Controller.print_message("Image dimension change detected, image acquisition thread was updated")

        color_image_data = self._mono_to_color_processor.transform_to_24(frame.image_buffer,
                                                                         self._image_width,
                                                                         self._image_height)
        color_image_data = color_image_data.reshape(self._image_height, self._image_width, 3)
        return Image.fromarray(color_image_data, mode='RGB')

    def run(self):
        self.is_alive = True
        while not self.stop_event.is_set():
            self._iteration()
        self._stop()

    def _iteration(self):
        try:
            if not self.camera.get_is_connected():
                raise Exception("Cameras is not connected")

            frame = self.camera_driver.get_pending_frame_or_null()
            if frame is not None:
                pil_image = self._get_color_image(frame)
                self.image_queue.put_nowait(pil_image)
        except queue.Full:
            pass
        except Exception as error:
            self.stop()
    def _stop(self):
        Console_Controller.print_message("Image acquisition has stopped")
        self._mono_to_color_processor.dispose()
        self._mono_to_color_sdk.dispose()
        self.is_alive = False

    def get_is_alive(self):
        return self.is_alive
