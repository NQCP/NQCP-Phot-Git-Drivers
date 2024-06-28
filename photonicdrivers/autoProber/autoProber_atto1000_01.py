from autoProber_baseClass import autoProber_baseClass

class autoProber_atto1000_01(autoProber_baseClass):
    def connectToLaser(self) -> None:
        print("connecting to the toptica CTL laser")

    def connectToPiezos(self) -> None:
        print("connecting to piezos in the attocube")

    def connectToPowerMeter(self) -> None:
        print("connecting to the chosen power meter")