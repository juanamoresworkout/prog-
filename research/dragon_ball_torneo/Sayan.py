from __future__ import annotations

from Guerrero import * 

class Sayan(Guerrero):
    
    def __init__(self, nombre, energia, deseo, ataque, esquivar, parar, rayo):
        super().__init__(nombre, energia, deseo, ataque, esquivar, parar, rayo)
        self._raza = TipoRaza.Sayan
        self._factor = 2

    def atacar(self, persona: Persona):
        for _ in range(randint(1,3)):
            super().atacar(persona)

    def obtener_esquivar(self)-> float:
        return self._esquivar

    def obtener_parada(self) -> float:
        return self._parar
    