from __future__ import annotations

from abc import *
from typing import * 
from Car import * 
from Driver import Driver
from Humano import Humano
from Animal import Animal
from random import *
from iRace import iRace 

class Piere(Car):
    
    def __init__(self, name, fine,trampa: int):
        super().__init__(name, 0.0, fine, 18.0, Humano(), Animal())
        if trampa < 10:
            trampa = 10 
        if trampa > 20:
            trampa = 20 

        self._trampa = trampa
    
    def tipo_coche(self) -> TypeObject:
        return TypeObject.Piere

    def simular(self, race: iRace):
        if self.estar_desactivo():
            return 
        if self._trampa > 0 :
            if uniform(0.0,100.0) <= 50.0:
                self._trampa -= 1 
                if uniform(0.0,100.0) <= 30.0:       
                    coches = race.ordenar_coches()
                    indice = race.index_of(self)

                    for i in range(len(coches)):
                        if i == indice: 
                            if i == 0:
                                self._position += self.get_velocidad()
                                break
                            else:
                                self._position += self.get_velocidad()
                                coches[i - 1].desactivar(1)
                                break
                else:
                    self._copiloto = None 
                    self._position += self.get_velocidad()
            else:
                self._position += self.get_velocidad()
        else:
            self._position += self.get_velocidad()
        

    def esta_vivo(self) -> bool:
        pass 