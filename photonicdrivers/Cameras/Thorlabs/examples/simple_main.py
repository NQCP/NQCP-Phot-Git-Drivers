import tkinter as tk
from photonicdrivers.Cameras.Thorlabs.thorlabs_tsi_sdk.tl_camera import TLCameraSDK
from photonicdrivers.Cameras.Thorlabs.examples.tkinter_camera_live_view import ImageAcquisitionThread, LiveViewCanvas

class CameraController:
    def __init__(self):
        self.sdk = TLCameraSDK()
        self.camera = None

    def discover_and_open_camera(self):
        camera_list = self.sdk.discover_available_cameras()
        if not camera_list:
            raise RuntimeError("No cameras found.")
        self.camera = self.sdk.open_camera(camera_list[0])
        return self.camera

    def close(self):
        if self.camera:
            self.camera.dispose()
        self.sdk.dispose()

class LiveViewWidget:
    def __init__(self, parent, camera):
        self.camera = camera
        self.image_acquisition_thread = ImageAcquisitionThread(self.camera)
        self.canvas = LiveViewCanvas(parent=parent, image_queue=self.image_acquisition_thread.get_output_queue())
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def start(self):
        self.image_acquisition_thread.start()

    def stop(self):
        self.image_acquisition_thread.stop()
        self.image_acquisition_thread.join()

class ExposureControl:
    def __init__(self, parent, camera):
        self.camera = camera
        self.parent = parent
        self.create_exposure_controls()

    def create_exposure_controls(self):
        # Create exposure control widgets
        self.exposure_frame = tk.Frame(self.parent)
        self.exposure_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

        self.slider = tk.Scale(self.exposure_frame, from_=1, to=1000000, orient=tk.HORIZONTAL, label="Exposure Time (us)", command=self.on_slider_change)
        self.slider.pack()

        self.entry = tk.Entry(self.exposure_frame)
        self.entry.pack()
        self.entry.bind("<Return>", self.set_exposure_time)

        # Set initial exposure value
        self.slider.set(self.camera.exposure_time_us if self.camera.exposure_time_us else 10000)
        self.entry.insert(0, str(self.camera.exposure_time_us if self.camera.exposure_time_us else 10000))

    def set_exposure_time(self, event=None):
        try:
            exposure_time = int(self.entry.get())
            self.camera.exposure_time_us = exposure_time
            self.slider.set(exposure_time)
        except ValueError:
            pass  # Handle invalid input if necessary

    def on_slider_change(self, value):
        try:
            exposure_time = int(value)
            self.camera.exposure_time_us = exposure_time
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(exposure_time))
        except ValueError:
            pass  # Handle invalid input if necessary

class GainControl:
    def __init__(self, parent, camera):
        self.camera = camera
        gain_range = self.camera.gain_range
        self.create_gain_controls(parent, gain_range)

    def create_gain_controls(self, parent, gain_range):
        # Create gain control widgets
        self.gain_frame = tk.Frame(parent)
        self.gain_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

        self.slider = tk.Scale(self.gain_frame, from_=gain_range.min, to=gain_range.max, orient=tk.HORIZONTAL, label="Gain (dB)", command=self.on_slider_change)
        self.slider.pack()

        self.entry = tk.Entry(self.gain_frame)
        self.entry.pack()
        self.entry.bind("<Return>", self.set_gain)

        # Set initial gain value
        self.slider.set(self.camera.gain if self.camera.gain else 0)
        self.entry.insert(0, str(self.camera.gain if self.camera.gain else 0))

    def set_gain(self, event=None):
        try:
            gain = int(self.entry.get())
            self.camera.gain = gain
            self.slider.set(gain)
        except ValueError:
            pass  # Handle invalid input if necessary

    def on_slider_change(self, value):
        try:
            gain = int(value)
            self.camera.gain = gain
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(gain))
        except ValueError:
            pass  # Handle invalid input if necessary

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.camera_controller = CameraController()
        self.camera = self.camera_controller.discover_and_open_camera()

        self.root.title(self.camera.name)

        # Create a frame for the live view and controls
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create live view widget
        self.live_view_widget = LiveViewWidget(parent=self.main_frame, camera=self.camera)

        # Create a frame for controls on the right side
        self.controls_frame = tk.Frame(self.main_frame)
        self.controls_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

        # Add exposure and gain controls
        self.exposure_control = ExposureControl(parent=self.controls_frame, camera=self.camera)
        self.gain_control = GainControl(parent=self.controls_frame, camera=self.camera)

        # Start image acquisition
        self.camera.frames_per_trigger_zero_for_unlimited = 0
        self.camera.arm(2)
        self.camera.issue_software_trigger()

    def start(self):
        self.live_view_widget.start()
        self.root.mainloop()

    def stop(self):
        self.live_view_widget.stop()
        self.camera_controller.close()

if __name__ == "__main__":
    root = tk.Tk()

    print("Generating app...")
    app = CameraApp(root)

    print("App starting")
    try:
        app.start()
    except KeyboardInterrupt:
        print("Interrupted by user. Closing...")
    finally:
        print("Waiting for image acquisition thread to finish...")
        app.stop()

    print("App terminated. Goodbye!")
