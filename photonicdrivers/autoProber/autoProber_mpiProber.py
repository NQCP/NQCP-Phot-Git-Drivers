from autoProber_baseClass import autoProber_baseClass

class autoProber_mpiProber(autoProber_baseClass):
    def connectToLaser(self) -> None:
        print("connecting to the white light laser")

    def connectToPiezos(self) -> None:
        print("connecting to the puck of the autoprober")

    def connectToPowerMeter(self) -> None:
        print("connecting to another power meter")