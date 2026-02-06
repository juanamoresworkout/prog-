from __future__ import annotations

from abc import *
from typing import * 
from Car import * 
from Driver import Driver
from Humano import Humano
from random import *

class Troglodyte(Car):
    
    def __init__(self, name, fine):
        super().__init__(name, 0.0, fine, 10.0, Humano(), Humano())
    
    def tipo_coche(self) -> TypeObject:
        return TypeObject.Troglodyte

    def simular(self, race: iRace):
        if self.estar_desactivo():
            return 
        result = self.get_velocidad()
        if uniform(0.0,100.0) <= 30.0:
            if uniform(0.0,100.0) <= 40.0:
                result += 20.0
            if uniform(0.0,100.0) <= 20.0:
                self._desactivado += 1 
    
        self._position += result 
    
    def esta_vivo(self) -> bool:
        pass 

    