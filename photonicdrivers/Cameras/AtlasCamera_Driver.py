from photonicdrivers.Abstract.Connectable import Connectable
from arena_api.system import system
from arena_api._device import Device
from arena_api.buffer import BufferFactory
from arena_api.enums import PixelFormat
class AtlasCamera_Driver(Connectable):
    def __init__(self, ip: str):
        self.ip = ip


    def is_connected(self):
        return self.camera.is_connected()
    
    def connect(self):
        relevant_infos = [x for x in system.device_infos if x['ip'] == self.ip]
        if len(relevant_infos) != 1:
            raise Exception(f"Expected 1 result with ip {self.ip} but got {len(relevant_infos)}")
        self.info = relevant_infos[0]
        self.camera: Device = system.select_device(system.create_device(self.info))
        self.camera.start_stream()

    def disconnect(self):
        system.destroy_device()
        self.camera = None

    def capture_image(self):
        buf = self.camera.get_buffer()
        BufferFactory.convert(buf, PixelFormat.RGB8)

cam = AtlasCamera_Driver("10.209.69.91")
cam.connect()
print(cam.is_connected())
