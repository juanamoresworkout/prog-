from __future__ import annotations

from Obstacle import Obstacle
from abc import *
from iRace import iRace 
from Car import Car 
from random import *

class Puddle(Obstacle):
    def __init__(self, name : str, position : float):
        super().__init__(name, position)


    def esta_vivo(self) -> bool:
        pass 

    def simular(self, race: iRace):
        result : list[Car] = race.ordenar_coches()
        for i in range(len(result)):
            coche = result[i].get_position()
            if (coche < self._position and coche > (self._position - 20.0)) or (coche > self._position and coche < (self._position + 20) ) :
                if uniform(0.0,100.0) <= 20.0:
                    result[i].desactivar(randint(1,3))
    
