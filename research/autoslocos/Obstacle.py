from __future__ import annotations

from RaceObject import RaceObject 
from abc import *
from typing import *
from RaceObject import TypeObject
from iRace import iRace 


class Obstacle(RaceObject):
    def __init__(self, name : str, position : float):
        super().__init__(name, position)

    @abstractmethod
    def esta_vivo(self) -> bool:
        pass 

    def tipo_objeto(self) -> TypeObject:
        return TypeObject.Obstacle

    @abstractmethod
    def simular(self, race: iRace):
        pass 


    def tipo_coche(self) -> TypeObject:
        pass