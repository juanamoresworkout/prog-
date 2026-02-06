from __future__ import annotations

from abc import *
from typing import *
from enum import Enum 


class TypeObject(Enum):
    Car = 0
    Obstacle = 1 
    Driver = 2 
    Glamour = 3
    Troglodyte = 4 
    Wood = 5 
    Piere = 6 
    Rock = 7 
    Puddle = 8
    Bomb = 9 


class RaceObject(ABC):

    def __init__(self, name : str, position: float):
        self._name = name
        self._position = position
        self._desactivado = 0

    @abstractmethod
    def esta_vivo(self) -> bool:
        pass 

    @abstractmethod
    def tipo_objeto(self) -> TypeObject:
        pass 

    def desactivar(self, turnos: int) :
        self._desactivado += turnos 
    
    def get_position(self) -> float:
        return self._position 
    
    def _set_position(self, posicion: float):
        self._position += posicion 

    
    def simular(self, race: iRace):
        pass

    @abstractmethod
    def tipo_coche(self) -> TypeObject:
        pass