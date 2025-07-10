from photonicdrivers.Abstract.Connectable import Connectable
from arena_api.system import system
from arena_api._device import Device
from arena_api.buffer import BufferFactory, _Buffer
from arena_api.enums import PixelFormat
import numpy as np

def extract_img_from_buf(buf: _Buffer) -> np.ndarray:
    if buf.has_chunkdata:
        bytes_per_pixel = int(buf.bits_per_pixel / 8)

        image_size_in_bytes = buf.height * buf.width * bytes_per_pixel

        pixels = buf.data[:image_size_in_bytes]
    else:
        pixels = buf.data
    
    return np.asarray(pixels, dtype=np.uint8).reshape((buf.height, buf.width, buf.bits_per_pixel // 8))

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
        stream_nodemap = self.camera.tl_stream_nodemap
        stream_nodemap['StreamAutoNegotiatePacketSize'].value = True
        stream_nodemap['StreamPacketResendEnable'].value = True
        stream_nodemap["StreamBufferHandlingMode"].value = "NewestOnly"
        self.camera.start_stream()

    def disconnect(self):
        system.destroy_device()
        self.camera = None

    def capture_image(self):
        buf: _Buffer = self.camera.get_buffer()
        img_buf = BufferFactory.convert(buf, PixelFormat.Mono8)
        self.camera.requeue_buffer(buf)
        img = extract_img_from_buf(img_buf)
        BufferFactory.destroy(img_buf)
        return img

    def gain(self) -> float:
        return self.camera.nodemap['Gain'].value

    def set_gain(self, gain: float):
        self.camera.nodemap['Gain'].value = gain