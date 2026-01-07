from abc import ABC, abstractmethod
from typing import Callable
from __future__ import annotations
from enum import Enum 
import random 

class RaceType(Enum):
    humnano: 0
    guerrero: 2
    super_s: 1
    

class Persona: 
    name : str
    race: RaceType
    energy: float 
    dodge_desire: float 

    def __init__(self, name: str,race: RaceType, energy: float, dodge_desire: float):
        self.__name = name 
        self.__race = race 
        if energy < 1000.0:
            energy = 1000.0
        if energy > 2000.0:
            energy = 2000.0
        self.energy = energy
        self.__dodge_desire = dodge_desire
    
    def get_name(self) -> str:
        return self.__name 
    
    @abstractmethod
    def get_race(self) -> RaceType :
        pass 
    
    @abstractmethod
    def get_race(self) -> RaceType: 
        pass 

    @abstractmethod
    def Quitar_Energia(self,energy: float):
        pass
    
    @abstractmethod
    def atacar(self,other: Persona):
        pass 

    @abstractmethod
    def get_energia(self):
        return self.energia 

    @abstractmethod
    def quitar_energia(self, energy: float):
        pass 

    @abstractmethod  
    def obtener_capacidad_esquivar(self) -> float: 
        pass 
    
    @abstractmethod
    def obtener_capacidad_parada(self) -> float: 
        pass 

    @abstractmethod
    def querer_esquivar(self)->float :
        pass


class GuerroEspacio(Persona):
    pass 

class SuperS(GuerroEspacio):
    pass 

class Humano(Persona):
    hit_attack: float 

    def __init__(self, name: str,  energy: float, dodge_desire:float,hit_attack: float, parry: float,dodge:float):
        super().__init__(name, energy, dodge_desire)
        self.__hit_attack = hit_attack
        self.__dodge = dodge 
        self.__parry = parry
    
    def get_race(self) -> RaceType :
        return RaceType.humnano 
    
    @abstractmethod
    def get_race(self) -> RaceType: 
        pass 

    @abstractmethod
    def Quitar_Energia(self,energy: float):
        pass
    
    @abstractmethod
    def atacar(self,other: Persona):
        pass 

    @abstractmethod
    def get_energia(self):
        return self.energia 

    @abstractmethod
    def quitar_energia(self, energy: float):
        pass 

    @abstractmethod  
    def obtener_capacidad_esquivar(self) -> float: 
        pass 
    
    @abstractmethod
    def obtener_capacidad_parada(self) -> float: 
        pass 

    @abstractmethod
    def querer_esquivar(self)->float :
        return random() < self.dodge_desire 

class ITorneo(ABC): 
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def inicir_torneo(self):
        pass 

    @abstractmethod
    def add_persona(self,persona:Persona): 
        pass 

    @abstractmethod
    def play_round(self):
        pass

    @abstractmethod
    def filter_personas(self, a_filter: Callable[[Persona],bool]) -> list[Persona]:
        pass 
    
    @abstractmethod 
    def get_winner(self)-> Persona:
        pass

class Util:

    @classmethod
    def clamp(value:float, min_value:int , max_value: int):
        return min(max_value (min(value,min_value)))

    @classmethod 
    def generar_humano_ramdon(cls) -> Humano:
        result = Humano()
        return result 

    @classmethod
    def generar_guerrero_ramdon(cls) -> GuerroEspacio:
        result = GuerroEspacio()
        return result 
    
    @classmethod
    def generar_humano_ramdon(cls) -> SuperS:
        result = SuperS()
        return result 
    
    @classmethod
    def make_combat(cls, c1: Persona, c2: Persona) -> Persona:
        if random.randint(0,1) == 1 :
            c2.atacar(c1)
            if c1.get_energia() <= 0:
                return c2 
            
        while True: 
            c1.atacar(c2)
            if c2.get_energia() <= 0:
                return c1
            c2.atacar(c1)
            if c1.get_energia() <= 0:
                return c2 
            
class Torneo(ITorneo): 

    def __init__(self):
        super().__init__()
        self.__personas: list[Persona] = []
    
    
    def inicir_torneo(self):    
        pass 

    
    def add_persona(self,persona:Persona): 
        if persona is None:
            return 
        if persona in self.__personas:
            return 
        self.__personas.append(persona)

   
    def play_round(self):
        if self.get_winner() != None:
            return 
        winners: list[Persona] = []
        while len(self.__personas) > 0 :
            persona1 = self.__personas.pop(0)
            persona2 = self.__personas.pop(0)
            winner = Util.make_combat(persona1,persona2)
            winners.append(winner)

        self.__personas = winners 

        #for i in range (0, len(self.__personas), 2):
         #   persona1= self.__personas[i]
          #  personas2= self._personas[i + 1 ]


   
    def filter_personas(self, a_filter: Callable[[Persona],bool]) -> list[Persona]:
        if a_filter is None:
            return 
        result : list[Persona] = []
        for p in self.__personas:
            if a_filter(p):
                result.append(p)
        return result 
    
    @abstractmethod 
    def get_winner(self)-> Persona:
        pass 