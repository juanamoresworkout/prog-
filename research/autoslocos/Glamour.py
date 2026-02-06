from __future__ import annotations

from abc import *
from typing import * 
from Car import * 
from Driver import Driver
from Humano import Humano
from iRace import iRace 

class Glamour(Car):
    
    def __init__(self, name, fine):
        super().__init__(name, 0.0, fine, 20.0, Humano(), None)
    
    def tipo_coche(self) -> TypeObject:
        return TypeObject.Glamour


    def simular(self, race: iRace):
        if self.estar_desactivo():
            return 
        self._position += self.get_velocidad()  

    def esta_vivo(self) -> bool:
        pass 

    