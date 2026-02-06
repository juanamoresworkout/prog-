from __future__ import annotations

from Obstacle import Obstacle
from abc import *
from iRace import iRace
from Car import Car 
from random import *

class Bomb(Obstacle):
    def __init__(self, name, position, turnos: int):
        super().__init__(name, position)

        self._turnos = turnos

    def esta_vivo(self) -> bool:
        return self._turnos != 0 

    
    def simular(self, race: iRace):
        if self.esta_vivo():
            self._turnos -= 1
        else:
            lista: list[Car] = race.ordenar_coches()
            for i in range(len(lista)):
                coche = lista[i].get_position()
                if coche < self._position and coche > (self._position - 70):
                    lista[i]._set_position(uniform(-50.0,50.0))
                    index = race.index_of(self)
                    race.remove_objecto(index)

                    

            

