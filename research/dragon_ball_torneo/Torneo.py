from __future__ import annotations

from iTorneo import *
from abc import *
from typing import *
from Persona import *
from Utils import *

class Torneo(iTorneo):
    def __init__(self):
        self._lista: list[Persona] = []

    def iniciar_torneo(self):
        self.add_participantes()
        
        for _ in range(4):
            self.ejecutar_ronda()


    def add_participantes(self):
        if len(self._lista) > 0:
            self._lista = []

        cont = 0 
        nombre = "Player" + str(cont)
        for _ in range(0,16):
            participante = randint(1,3)
            if participante == 1:
                humano = Utils.generar_humano(nombre)
                self._lista.append(humano)
                continue
            
            if participante == 2:
                guerrero = Utils.generar_guerrero(nombre)
                self._lista.append(guerrero)
                continue
            
            if participante == 3:
                sayan = Utils.generar_sayan(nombre)
                self._lista.append(sayan)
                continue
            
    def pelear(self,c1: Persona, c2: Persona) -> Persona :
        if randint(0,1) == 1:
            c2.atacar(c1)
            if not c1.esta_vivo():
                return c2
        while True:
            c1.atacar(c2)
            if not c2.esta_vivo():
                return c1
            c2.atacar(c1)
            if not c1.esta_vivo():
                return c2

    def ejecutar_ronda(self):
        if len(self._lista) < 2 : 
            raise ValueError("No se puede ejecutar ronda")
        result: list[Persona] = []
        for i in range(0,len(self._lista),2):
            ganador = self.pelear(self._lista[i],self._lista[i + 1])
            result.append(ganador)
        self._lista = result 

    def filter(self,filter: Callable[[Persona],bool]) -> list[Persona] : 
        pass

    def ganador(self) -> Persona|None:
        if len(self._lista) != 1:
            return None 
        else:
            return self._lista[0]
