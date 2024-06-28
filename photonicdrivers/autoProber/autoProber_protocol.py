from typing import Protocol

class autoProber_prot(Protocol):
    def roughAlignment(self) -> None:
        pass

    def fineAlignment(self) -> None:
        pass

    def connectToLaser(self) -> None:
        pass

    def connectToPiezos(self) -> None:
        pass

    def connectToPowerMeter(self) -> None:
        pass
