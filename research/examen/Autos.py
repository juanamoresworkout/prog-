from __future__ import annotations

from abc import *
from typing import *
from enum import Enum 
from random import *

class TypeObject(Enum):
    Obstacle = 0
    Rock = 1
    Puddle = 2
    Bomb = 3 
    Coche = 4
    Glamour = 5 
    Troglodyte = 6
    WoodCar = 7
    PiereCar = 8  

class IRace(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def AddObject(self,obj:RaceObject, position: float):
        pass 

    @abstractmethod
    def Init(self,distance: float):
        pass 

    @abstractmethod
    def SimulateStep(self):
        pass 

    @abstractmethod
    def VisitDriver(self, visit: Callable[[Driver], None]):
        pass 

    @abstractmethod
    def VisitCars(self,visit: Callable[[Car],None]):
        pass
    
    @abstractmethod
    def VisitObstacles(self, visit: Callable[[Obstacle], None]):
        pass

    @abstractmethod
    def VisitObjects(self, visit: Callable[[RaceObject], None]):
        pass 
    
    @abstractmethod
    def GetObjectCount(self)-> int :
        pass

    @abstractmethod
    def GetObjectAt(self,index: int) -> RaceObject:
        pass 

    @abstractmethod
    def remove_object(self,obj: RaceObject) -> RaceObject|None:
        pass 

class Race(IRace):

    def __init__(self):
        self._participantes: list[RaceObject] = []

    def AddObject(self, obj: RaceObject, position: int):
        pass 
    
    def Init(self, distance):
        pass

    def SimulateStep(self):
        pass 

    def VisitDriver(self, visit: Callable[[Driver], None]):
        for coche in Utils.orden_corredores(self):
            corredor = coche.get_drivers()
            if corredor[0] is not None:
                visit(corredor)
            if corredor[1] is not None:
                visit(corredor)

    def VisitCars(self,visit: Callable[[Car],None]):
        for obj in self._participantes:
            if obj.GetObjectType() == TypeObject.Coche:
                visit(obj)

    def VisitObstacles(self, visit: Callable[[Obstacle], None]):
        for obj in self._participantes:
            if obj.GetObjectType == TypeObject.Obstacle:
                visit(obj)

    def VisitObjects(self, visit: Callable[[RaceObject], None]):
        for obj in self._participantes:
            visit(obj)
    
    def remove_object(self,obj: RaceObject) -> RaceObject|None:
        if obj is None:
            return 
        for i in range(len(self._participantes)):
            if self._participantes[i] == obj:
                self._participantes.pop(i)

    def GetObjectCount(self)-> int :
        return len(self._participantes)

    def GetObjectAt(self,index: int) -> RaceObject:
        for i in range(len(self._participantes)):
            if i == index :
                return self._participantes[i]

class RaceObject:
    def __init__(self,name: str):
        if name is None:
            raise ValueError("Nombre necesario")
        self.___name = name 
        self._position = 0.0 
        self._disable = 0  

    def get_name(self) -> str:
        return self.___name
    
    def get_position(self):
        return self._position
    
    @abstractmethod
    def IsAlive(self)-> bool:
        pass 

    @abstractmethod
    def GetObjectType(self) -> TypeObject:
        pass 

    def Disable(self,turnos: int):
        self._disable += turnos 

    def _can_i_move(self) -> bool:
        if self._disabled_turns > 0:
            self._disabled_turns -= 1
            return False
        return True

    @abstractmethod
    def Simulate(self,race: IRace):
        pass 

class Obstacle(RaceObject):

    def __init__(self, name):
        super().__init__(name)

    @abstractmethod
    def IsAlive(self)-> bool:
        pass 
    
    @abstractmethod
    def GetObstacleType(self) -> TypeObject:
        pass

    def GetObjectType(self) -> TypeObject:
        return TypeObject.Obstacle

    @abstractmethod
    def Simulate(race: IRace):
        pass 

class Rock(Obstacle):
    def __init__(self, name, peso:float):
        super().__init__(name)
        self._peso = peso

    @abstractmethod
    def IsAlive(self)-> bool:
        pass 

    def GetObstacleType(self) -> TypeObject:
        return TypeObject.Rock

    def Simulate(self,race: IRace):
        coches: list[Car] = []
        coches = Utils.orden_corredores(race)
        prob_rock = (10.0 + self._peso)
        for car in coches: 
            if (car._position < self._position and car._position > (self._position - 40)) or (car._position > self._position and car._position < (self._position + 40)):
                if uniform(0.0,100.0) <= prob_rock:
                    car._position -= 25 

class Puddle(Obstacle):

    def __init__(self, name):
        super().__init__(name)
    
    @abstractmethod
    def IsAlive(self)-> bool:
        pass 

    def Simulate(self,race: IRace):
        coches:list[Car] = []
        coches = Utils.orden_corredores(race)
        for coche in coches:
            if coche._position < self._position and coche._position > (self._position - 20):
                if uniform(0.0,100.0) <= 20.0:
                    turnos = randint(1,3)
                    coche._disable += turnos 
        
class Bomb(Obstacle):

    def __init__(self, name: str, turnos: int):
        super().__init__(name)
        self._turnos = turnos 
    
    def IsAlive(self)-> bool:
        return  self._turnos != 0 
    
    def Simulate(self,race: IRace):
        coches: list[Car] = []
        if self.IsAlive():
            self._turnos -= 1 
        else:
            coches =Utils.orden_corredores(race)
            for coche in coches:
                if coche._position < self._position and coche._position > (self._position - 70):
                    nueva_distancia = uniform(-50.0,50.0)
                    coche._position += nueva_distancia 
                    race.remove_object(self)
            
class Car(RaceObject):

    def __init__(self, name: str , finetunning: float, driver: Driver, copilot: Driver):
        super().__init__(name)
        if finetunning < 1.0:
            finetunning = 1.0 
        if finetunning > 3.0:
            finetunning = 3.0 
        
        self._finetunning = finetunning
        self._driver = driver 
        self._copilot = copilot
        self._velocity = 0.0
    
    def get_drivers(self)-> tuple[Driver,Driver]:
        return (self._driver,self._copilot)
    
    @abstractmethod
    def IsAlive(self)-> bool:
        pass 
    
    def GetObjectType(self) -> TypeObject:
        return TypeObject.Coche
    
    @abstractmethod
    def GetCarType(self) -> Car:
        pass

    @abstractmethod
    def Simulate(race: IRace):
        pass

    def get_velocity(self) -> float:
        result = self._velocity * self._finetunning
        if self._copilot is not None:
            result += self._copilot.GetVelocityExtra()
        return result 

class GlamourCar(Car):

    def __init__(self, name, finetunning):
        super().__init__(name, finetunning, Human(), None)
        self._velocity = 15.0
        
    @abstractmethod
    def IsAlive(self)-> bool:
        pass 

    def GetCarType(self) -> TypeObject:
        return TypeObject.Glamour

    def Simulate(self, race: IRace):
        if not self._disable == 0:
            self._disable -= 1 
            return 
        result = self.get_velocity()
        self._position += result 
        
class TroglodyteCar(Car):

    def __init__(self, name, finetunning):
        super().__init__(name, finetunning, Human(), Human())
        self._velocity = 10

    @abstractmethod
    def IsAlive(self)-> bool:
        pass 

    def GetOCarType(self) -> TypeObject:
        return TypeObject.Troglodyte

    def Simulate(self,race: IRace):
        if not self._can_i_move():
            return 
        result = self.get_velocity()
        if uniform(0.0,100.0) <= 30.0:
            if uniform(0.0,100) <= 40.0:
                result += 20
            if uniform(0.0,100.0) <= 20.0:
                self.Disable(1)
        self._position += result

class WoodCar(Car):

    def __init__(self, name, finetunning):
        super().__init__(name, finetunning, Human(), Animal())
        self._velocity = 15 
   
    @abstractmethod
    def IsAlive(self)-> bool:
        pass 
   
    def GetCarType(self) -> TypeObject:
        return TypeObject.WoodCar

    def Simulate(self,race: IRace):
        if uniform(0.0,100.0) <= 60.0:
            self._disable = 0 
        if not self._can_i_move():
            return 
        self._position += self.get_velocity()
            
class PiereCar(Car):

    def __init__(self, name, finetunning, trampas: int):
        super().__init__(name, finetunning, Human(), Animal())       
        if trampa < 10:
            trampa = 10
        if trampa > 20:
            trampa = 20 
        
        self._velocity = 18 
        self.__trampas = trampas

    @abstractmethod
    def IsAlive(self)-> bool:
        pass 

    def GetCarType(self) -> TypeObject:
        return TypeObject.PiereCar
    
    def Simulate(self,race: IRace):
        if race is None:
            raise ValueError("No hay carrera")
        if not self._can_i_move():
            return     
        if self.__trampas > 0:
            if uniform(0.0,100.0) <= 50.0:
                self.__trampas -= 1 
                coches = Utils.orden_corredores(race)
                for i in range(len(coches)):
                    c = coches[i]
                    if c.GetCarType() != TypeObject.PiereCar:
                        continue
                    if uniform(0.0,100.0) <= 30:
                        if i == 0 :
                            self._position += self.get_velocity()
                            break 
                        else:
                            coches[i -1].Disable(1)
                            self._position += self.get_velocity()
                    else:
                        self._copilot = None
                        self._position += self.get_velocity()     
                        break
            else: 
                self._position += self.get_velocity()
        else: 
            self._position += self.get_velocity()
                            
class Driver:
    def __init__(self):
        pass 

    @abstractmethod
    def GetVelocityExtra(self) -> float:
        pass 

class Animal(Driver):

    def __init__(self):
        super().__init__()
    
    def GetVelocityExtra(self) -> float:
        return uniform(-1.0,3.0)
    
class Human(Driver):

    def __init__(self):
        super().__init__()
    
    def GetVelocityExtra(self)-> float:
        return 0.0 
            
class Utils:
        @classmethod
        def orden_corredores(cls,race: IRace):
            coches: list[Car] = []
            race.VisitCars(lambda car : coches.append(car))
            for i in range(len(coches)):
                for j in range(len(coches)-1):
                    if coches[j].get_position() > coches[j + 1].get_position() : 
                        coches[j],coches[j + 1] = coches[j+1],coches[j]
            return coches 
    