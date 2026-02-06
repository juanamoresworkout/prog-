from __future__ import annotations

from Persona import *
from typing import *
from abc import *


class Guerrero(Persona):
    def __init__(self, nombre :str , energia: float , deseo : float, ataque : float , esquivar: float , parar: float, rayo : float):
        super().__init__(nombre,TipoRaza.Guerrero ,energia, deseo)
        if ataque < 0.1:
            ataque = 0.1 
        if ataque > 0.8:
            ataque = 0.8
        
        if rayo < 0.3:
            rayo = 0.3
        if rayo > 0.6:
            rayo = 0.6 
        
        if esquivar < 0.2:
            esquivar = 0.2
        if esquivar > 0.4:
            esquivar = 0.4

        if parar < 0.4:
            parar = 0.4
        if parar > 0.9:
            parar = 0.9
        
        self._ataque = ataque 
        self._esquivar = esquivar 
        self._parar = parar
        self._factor = 1 

    def atacar(self,persona: Persona):
        
        tipo = randint(0,1)
        if tipo == 0 :
            self.quitar_energia(5)
            if not self.esta_vivo():
                return 
            if persona.quiere_esquivar():
                if persona.obtener_esquivar() > self._ataque:
                    return 
                else:
                    persona.quitar_energia(7.0 * self._factor)
            else:
                if persona.obtener_parada() > self._ataque:
                    persona.quitar_energia(2.0 * self._factor)

                else:
                    persona.quitar_energia(7.0 * self._factor)
        else:
            self.quitar_energia(100)
            if not self.esta_vivo():
                return 
            if persona.quiere_esquivar():
                if persona.obtener_esquivar() > self._ataque:
                    return 
                else:
                    persona.quitar_energia(300.0 * self._factor)
            else:
                if persona.obtener_parada() > self._ataque:
                    persona.quitar_energia(25.0 * self._factor)             
                else:
                    persona.quitar_energia(300.0 * self._factor)

    def obtener_esquivar(self)-> float:
        return self._esquivar

    def obtener_parada(self) -> float:
        return self._parar
    
