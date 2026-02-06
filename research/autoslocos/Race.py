from __future__ import annotations

from abc import *
from typing import *
from RaceObject import RaceObject,TypeObject
from Obstacle import Obstacle
from Driver import Driver
from Car import Car 
from Bomb import *
from Puddle import * 
from Rock import *
from Piere import *
from Glamour import *
from Troglodyte import *
from Wood import *


class Race(iRace): 
    def __init__(self):
        self._lista: list[RaceObject] = []
    
    def añadir_objeto(self, obj: RaceObject):
        if not isinstance(obj, RaceObject):
            raise ValueError("No esta en la lista")
        self._lista.append(obj)       

    def iniciar(self, distancia: float):      
        self.generar_cuatro_corredores(distancia)
        self.generar_tres_obstaculos(distancia)

        while True: 
          result: list[Car] = self.filter(lambda x: self.finish_race(x,distancia))
          self.simular_ronda()

          if len(result) > 0:
              return 

    def simular_ronda(self):
        for i in range(len(self._lista)):
            self._lista[i].simular(self)
    
    def visitar_corredores(self, visitor: Callable[[Driver], None]):
        result: list[Car] = []
        self.visitar_coches(self,lambda x : result.append(x))
        for i in range(len(result)):
            if result[i].get_piloto() is not None:
                visitor(result[i].get_piloto())
            if result[i].get_copiloto() is not None:
                visitor(result[i].get_copiloto())
            
    def visitar_coches(self,visitor: Callable[[Car], None]):
        for i in range(len(self._lista)):
            if self._lista[i].tipo_objeto() == TypeObject.Car:
                visitor(self._lista[i])


    def visitar_obstaculo(self, visitor: Callable[[Obstacle],None]):
        pass 


    def visitar_objectos(self, visitor: Callable[[RaceObject], None]): 
        pass 
    
    def get_objetos_contador(self) -> int : 
        return len(self._lista) 

    def get_objectos_en(self,index : int) -> RaceObject:
        if index < 0 or index > (len(self._lista) - 1) :
            raise ValueError("Error de rango de indice")
        for i in range(len(self._lista)):
            if i == index :
                return self._lista[i]

    def index_of(self, objeto: RaceObject) -> int:
        for i in range(len(self._lista)):
            if self._lista[i] == objeto:
                return i 
        return None 

    def ordenar_coches(self) -> list[Car]:
        result: list[Car] = []
        self.visitar_coches(lambda x : result.append(x))
        for i in range(len(result)):
            for j in range(len(result)-1):
                if result[j].get_position() > result[j + 1].get_position():
                    result[j],result[ j + 1] = result[j + 1],result[j]
        return result 

    def remove_objecto(self, index : int):
        for i in range(len(self._lista)) :
            if i == index:
                self._lista.pop(i)
                return 
    def generar_tres_obstaculos(self, distancia: float):
        piedra = Rock("Piedra",uniform(10.0,30.0),uniform(10.0,30.0))
        charco = Puddle("Charco",uniform(0,distancia))
        bomba = Bomb("Bomba",uniform(0,distancia),randint(0,10))
        self.añadir_objeto(piedra)
        self.añadir_objeto(charco)
        self.añadir_objeto(bomba)
    
    #Preguntar profesor, porque necesito argumentos
    def generar_cuatro_corredores(self, meta: float):
        glamour = Glamour("Glamour",uniform(1.0,3.0))
        piere = Piere("Piere", uniform(1.0,3.0), randint(10,20))
        troglodyte = Troglodyte("Troglodyte",uniform(1.0,3.0))
        wood = Wood("Wood",uniform(1.0,3.0))
        self.añadir_objeto(glamour)
        self.añadir_objeto(piere)
        self.añadir_objeto(troglodyte)
        self.añadir_objeto(wood)
    

    def finish_race(self, coche: Car, distance: float) -> bool:
        if coche.get_position() > distance:
            return True
        else:
            return False 
        
    def filter(self,filter: Callable[[Car],bool]) -> list[Car]:
        result: list[Car] = []
        for i in range(len(self._lista)):
            if self._lista[i].tipo_objeto() == TypeObject.Car:
                if filter(self._lista[i]):
                    result.append(self._lista[i])
        return result 


nuevo = Race()

nuevo.iniciar(500.0)
ganador = nuevo.filter(lambda x : x.get_position() > 500.0)
print(ganador)




