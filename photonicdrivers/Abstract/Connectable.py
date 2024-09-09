
from abc import abstractmethod, ABC
class Connectable(ABC): 

    @abstractmethod
    def connect():
        pass
    
    @abstractmethod
    def disconnect():
        pass
    
    @abstractmethod
    def is_connected():
        pass