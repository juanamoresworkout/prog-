from __future__ import annotations 

from abc import *

class Driver(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def get_velocity(self) -> float:
        pass 