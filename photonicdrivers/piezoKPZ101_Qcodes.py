import os
from typing import Any
from qcodes.instrument import Instrument
import qcodes.validators as vals


try:
    import clr  # pyright: ignore[reportMissingTypeStubs,reportMissingImports]
except ImportError as exc:
    raise ImportError(
        "Module clr not found. Please obtain it by running 'pip install pythonnet' in a qcodes environment terminal"
    ) from exc

# get these files by downloading the kinesis software from
# https://www.thorlabs.com/software_pages/viewsoftwarepage.cfm?code=Motion_Control


class PiezoKPZ101(Instrument):
    def __init__(
        self,
        serialno: str,
        path: str = "C:\\Program Files\\Thorlabs\\Kinesis\\",
        **kwargs: Any,
    ) -> None:
        print("Initialising instance of thorlabs piezo class")
        if os.name != "nt":
            raise ImportError("""This driver only works in Windows.""")
        super().__init__(**kwargs)
        self.add_thorlabs_dlls(path)
        self.serial_no = serialno
        print(self.devicemanagercli.BuildDeviceList())
        serialNumbers = self.devicemanagercli.GetDeviceList(
            self.kcube_piezo.DevicePrefix
        )
        print(serialNumbers)
        self.device = self.kcube_piezo.CreateKCubePiezo(self.serial_no)
        self.device.Connect(self.serial_no)

        self.add_parameter(
            "MaxVoltage",
            label="Max Voltage",
            get_cmd=self.device.GetMaxOutputVoltage,
            set_cmd=self.device.SetMaxOutputVoltage,
            unit="V",
            vals=vals.Enum(75, 150),
        )

    def enable(self) -> bool:
        try:
            self.device.EnableDevice()
        except Exception as e:
            print(e)
            print("enable failed")
            return False
        return True

    def getConfig(self) -> Any:
        device_config = self.device.GetPiezoConfiguration(self.serial_no)
        # print(device_config)
        return device_config

    def add_thorlabs_dlls(self, path: str) -> None:
        try:
            clr.AddReference(f"{path}Thorlabs.MotionControl.DeviceManagerCLI.dll")
            clr.AddReference(f"{path}Thorlabs.MotionControl.GenericMotorCLI.dll")
            clr.AddReference(f"{path}ThorLabs.MotionControl.KCube.PiezoCLI.dll")
            from Thorlabs.MotionControl.DeviceManagerCLI import DeviceManagerCLI  # type: ignore[import]
            from Thorlabs.MotionControl.GenericMotorCLI import GenericMotorCLI  # type: ignore[import]
            from Thorlabs.MotionControl.KCube.PiezoCLI import KCubePiezo  # type: ignore[import]

            self.device_manager = DeviceManagerCLI
            self.genericmotorcli = GenericMotorCLI
            self.kcube_piezo = KCubePiezo
        except Exception as e:
            print(e)
            raise ImportError(
                f"""Could not import Thorlabs dlls from {path}. Please check that the dlls are in the specified folder.\n
                Get these files by downloading the kinesis software from:\n
                https://www.thorlabs.com/software_pages/viewsoftwarepage.cfm?code=Motion_Control"""
            ) from e
