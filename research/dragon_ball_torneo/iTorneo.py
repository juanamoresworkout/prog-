from __future__ import annotations

from abc import *
from typing import *
from Persona import *

class iTorneo(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def iniciar_torneo(self):
        pass 

    @abstractmethod
    def add_participantes(self):
        pass 

    @abstractmethod
    def ejecutar_ronda(self):
        pass 

    @abstractmethod
    def filter(self,filter: Callable[[Persona],bool]) -> list[Persona] : 
        pass

    @abstractmethod
    def ganador(self) -> Persona:
        pass



    

