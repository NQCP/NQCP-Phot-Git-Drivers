from Code.Instruments.Implementations.Cameras.CameraAcquisitionThread import CameraAcquisitionThread
from Code.Instruments.Implementations.Cameras.examples.windows_setup import configure_path

configure_path()
import tkinter as tk
from PIL import ImageTk
import typing
import queue


class CameraWindow(tk.Canvas):

    def __init__(self, parent):
        self._camera_acquisition_thread = None
        self._image_queue = None
        self._image_width = 0
        self._image_height = 0
        self._frame_time = 50  # ms

        tk.Canvas.__init__(self, parent)
        self.pack()

    def start(self):
        try:
            image = self._image_queue.get_nowait()
            self._image = ImageTk.PhotoImage(master=self, image=image)
            if (self._image.width() != self._image_width) or (self._image.height() != self._image_height):
                # resize the canvas to match the new image size
                self._image_width = self._image.width()
                self._image_height = self._image.height()
                self.config(width=self._image_width, height=self._image_height)
            self.create_image(0, 0, image=self._image, anchor='nw')
        except queue.Empty:
            pass
        self.after(self._frame_time, self.start)

    def set_frame_time(self, frame_time_ms):
        self._frame_time = frame_time_ms

    def set_acquisition_thread(self, camera_acquisition_thread):
        self._camera_acquisition_thread = camera_acquisition_thread
        self._image_queue = self._camera_acquisition_thread.get_queue()



