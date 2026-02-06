from __future__ import annotations

from Persona import *
from typing import *
from abc import *


class Humano(Persona):
    def __init__(self, nombre :str , energia: float , deseo : float, ataque : float , esquivar: float , parar: float):
        super().__init__(nombre,TipoRaza.Humano ,energia, deseo)
        if ataque < 0.1:
            ataque = 0.1 
        if ataque > 0.8:
            ataque = 0.8
        
        if esquivar < 0.4:
            esquivar = 0.4
        if esquivar > 0.6:
            esquivar = 0.6

        if parar < 0.7:
            parar = 0.7
        if parar > 0.9:
            parar = 0.9
        
        self._ataque = ataque 
        self._esquivar = esquivar 
        self._parar = parar

    def atacar(self,persona: Persona):
        self.quitar_energia(1)

        if not self.esta_vivo():
            return 
        
        if persona.quiere_esquivar():
            if persona.obtener_esquivar() > self._ataque:
                return 
            else:
                persona.quitar_energia(5.0)
        else:
            if persona.obtener_parada() > self._ataque:
                persona.quitar_energia(0.5)
                
            else:
                persona.quitar_energia(5.0)

    def obtener_esquivar(self)-> float:
        return self._esquivar

    def obtener_parada(self) -> float:
        return self._parar
    
