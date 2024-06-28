from autoProber_ABC import autoProber_ABC

class autoProber_baseClass(autoProber_ABC):
    def __init__(self) -> None:
        print("init")

    def connectToEquipment(self) -> None:
        self.connectToLaser()
        self.connectToPowerMeter()
        self.connectToPiezos()        

    def roughAlignment(self) -> None:
        print("doing rough alignment")

    def fineAlignment(self) -> None:
        print("doing fine alignment")

    