from abc import ABC, abstractmethod

class autoProber_ABC(ABC):
    @abstractmethod
    def roughAlignment(self) -> None:
        pass

    @abstractmethod
    def fineAlignment(self) -> None:
        pass

    @abstractmethod
    def connectToLaser(self) -> None:
        pass

    @abstractmethod
    def connectToPiezos(self) -> None:
        print("lol")