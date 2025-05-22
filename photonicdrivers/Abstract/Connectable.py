
from abc import abstractmethod, ABC
class Connectable(ABC): 

    @abstractmethod
    def connect(self) -> None:
        pass
    
    @abstractmethod
    def disconnect(self) -> None:
        pass
    
    @abstractmethod
    def is_connected(self) -> bool:
        pass