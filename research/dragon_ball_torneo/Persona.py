from __future__ import annotations

from typing import *
from abc import *
from random import *
from enum import Enum 

class TipoRaza(Enum):
    Humano = 0 
    Guerrero = 1 
    Sayan = 2 

class Persona(ABC):
    
    def __init__(self, nombre: str, raza:TipoRaza,energia:float,deseo: float):
        if energia < 1000.0:
            energia  = 1000.0 
        if energia > 2000.0:
            energia = 2000.0 
        
        if deseo < 0.1:
            deseo = 0.1
        if deseo > 0.9:
            deseo = 0.9 

        self._raza = raza   
        self._nombre = nombre 
        self._energia = energia 
        self._deseo_esquivar = deseo


    def quitar_energia(self, energia: float):
        self._energia -= energia 
    
    @abstractmethod
    def atacar(self,persona: Persona):
        pass

    @abstractmethod
    def obtener_esquivar(self)-> float:
        pass

    @abstractmethod
    def obtener_parada(self) -> float:
        pass 
    
    def get_raza(self) -> TipoRaza:
        return self._raza

    def quiere_esquivar(self) -> bool:
        return random() <= self._deseo_esquivar 
    
    def esta_vivo(self) -> bool:
        return self._energia > 0 
    

    
