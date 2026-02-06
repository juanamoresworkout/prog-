from __future__ import annotations

from RaceObject import RaceObject, TypeObject
from abc import *
from Driver import Driver 
from iRace import iRace 


class Car(RaceObject):
    def __init__(self, name: str, position : float, fine: float, velocity: float, piloto: Driver, copiloto: Driver):
        super().__init__(name, position)
        if fine < 1.0:
            fine = 1.0
        if fine > 3.0:
            fine = 3.0

        self._finetunning = fine
        self._velocity = velocity
        self._driver = piloto
        self._copiloto = copiloto 

    @abstractmethod
    def esta_vivo(self) -> bool:
        pass 

    def tipo_objeto(self) -> TypeObject:
        return TypeObject.Car
    
    @abstractmethod
    def tipo_coche(self) -> TypeObject:
        pass

    @abstractmethod
    def simular(self, race: iRace):
        pass 

    def get_velocidad(self) -> float : 
        result = self._velocity * self._finetunning
        if self._copiloto is not None:
            result += self._copiloto.get_velocity()
        return result 

    def estar_desactivo(self) -> bool:
        if self._desactivado > 0:
            self._desactivado -= 1 
            return True 
        else:
            return False 

    def get_piloto(self) -> Driver:
        return self._driver
    
    def get_copiloto(self) -> Driver:
        return self._copiloto
    

