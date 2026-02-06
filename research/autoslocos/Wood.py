from __future__ import annotations

from abc import *
from typing import * 
from Car import * 
from Driver import Driver
from Humano import Humano
from Animal import Animal
from random import *

class Wood(Car):
    
    def __init__(self, name, fine):
        super().__init__(name, 0.0, fine, 15.0, Humano(), Animal())
    
    def tipo_coche(self) -> TypeObject:
        return TypeObject.Wood

    def simular(self, race: iRace):
        if self._desactivado > 0 :
            if uniform(0.0,100.0) <= 60.0:
                self._desactivado = 0 
                self._position += self.get_velocidad()
            else:
                self._desactivado -= 1 
        else:
            self._position += self.get_velocidad()
 
    def esta_vivo(self) -> bool:
        pass 