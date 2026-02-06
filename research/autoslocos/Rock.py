from __future__ import annotations

from Obstacle import Obstacle
from abc import *
from iRace import iRace 
from random import *
from Car import Car


class Rock(Obstacle):
    def __init__(self, name : str, position : float, peso : float):
        super().__init__(name, position)  
        if peso < 10:
            peso = 10 
        if peso > 30:
            peso = 30 
       
        self._peso = peso 


    def simular(self, race: iRace):
        roca = 10.0 + self._peso 
        result : list[Car] = race.ordenar_coches()
        for i in range(len(result)):
            coche = result[i].get_position()
            if (coche < self._position and coche > (self._position - 40.0)) or (coche > self._position and coche < (self._position + 40) ) :
                if uniform(0.0,100.0) <= roca:
                    result[i]._set_position(-25.0)

    def esta_vivo(self) -> bool:
        pass 




