from __future__ import annotations

from abc import *
from typing import *




class iRace(ABC): 
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def añadir_objeto(self, obj: RaceObject, position: float):
        pass 
    
    @abstractmethod
    def iniciar(self, distancia: float):
        pass 

    @abstractmethod
    def simular_ronda(self):
        pass 

    @abstractmethod
    def visitar_corredores(self, visitor: Callable[[Driver,Driver], None]):
        pass 

    @abstractmethod
    def visitar_coches(self,visitor: Callable[[Car], None]):
        pass 

    @abstractmethod
    def visitar_obstaculo(self, visitor: Callable[[Obstacle],None]):
        pass 

    @abstractmethod
    def visitar_objectos(self, visitor: Callable[[RaceObject], None]): 
        pass 
    
    @abstractmethod
    def get_objetos_contador(self) -> int : 
        pass 

    @abstractmethod
    def get_objectos_en(self,index : int) -> RaceObject:
        pass 

    @abstractmethod
    def index_of(self, objeto: RaceObject) -> int:
        pass 

    @abstractmethod
    def ordenar_coches(self) -> list[Car]:
        pass 

    @abstractmethod
    def remove_objecto(self, index : int):
        pass 

    @abstractmethod
    def finish_race(self, distance: float) -> RaceObject:
        pass 

    @abstractmethod
    def filter(self,filter: Callable[[Car],bool]) -> list[Car]:
        pass 
        



