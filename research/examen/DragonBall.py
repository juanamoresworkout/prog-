from __future__ import annotations
from abc import *
from typing import * 
from enum import Enum 
from random import *
from copy import deepcopy

class Raza(Enum):
    Humano =  0 
    Guerrero = 1 
    Sayan = 2 

class Persona(ABC): 
    nombre : str 
    raza: Raza 
    energia: float 
    deseo_esquivar: float 

    def __init__(self,nombre:str,raza: Raza,energia:float,deseo_esquivar: float):
        
        if not isinstance(raza, Raza):
            raise ValueError ("Tipo de raza incorrecto")
        
        if energia < 1000.0: 
            energia = 1000.0 
        if energia > 2000.0:
            energia = 2000.0 

        if deseo_esquivar < 0.1:
            deseo_esquivar = 0.1 
        if deseo_esquivar > 0.9: 
            deseo_esquivar = 0.9

        self._nombre = nombre 
        self._energia = energia 
        self._raza = raza     
        self._deseo_esquivar = deseo_esquivar 

    def get_name(self) -> str: 
        return self._nombre 
    
    @abstractmethod
    def get_raza(self) -> Raza: 
        pass 

    def get_energia(self) -> float: 
        return self._energia
    
    def get_deseo(self) -> float:
        return self._deseo_esquivar
    
    def quitar_energia(self,double: float):
        self._energia -= double 
    
    def esta_muerto(self) -> bool:
        return self._energia <= 0 
    
    @abstractmethod
    def atacar(self, persona: Persona): 
        pass

    @abstractmethod
    def obtener_capacidad_esquiva(self)-> float:
        pass 

    @abstractmethod
    def obtener_capacidad_parada(self)-> float: 
        pass 

    def quiere_esquivar(self) -> bool: 
        return random() <= self._deseo_esquivar
    
class Humano(Persona): 
    def __init__(self, nombre: str,energia:float, deseo_esquivar: float,ataque: float, esquivar: float, parar:float):
        super().__init__(nombre, Raza.Humano ,energia, deseo_esquivar) 
        
        if ataque < 0.1:
            ataque = 0.1 
        if ataque > 0.8:
            ataque = 0.8
        
        if esquivar < 0.4 : 
            esquivar = 0.4
        if esquivar > 0.6:
            esquivar = 0.6
        
        if parar < 0.7:
            parar = 0.7
        if parar > 0.9:
            parar = 0.9  
    
        self.__ataque = ataque 
        self.__esquivar = esquivar 
        self.__parar = parar 

    def get_raza(self) -> Raza: 
        return Raza.Humano 
    
    def get_ataque(self):
        return self.__ataque
     
    def obtener_capacidad_esquiva(self)-> float:
        return self.__esquivar
    
    def obtener_capacidad_parada(self)-> float:
        return self.__parar 
    
    
    def atacar(self,persona:Persona):
        if persona.esta_muerto() or self.esta_muerto():
            return 
        self.quitar_energia(1.0)

        if persona.quiere_esquivar() :
            if persona.obtener_capacidad_esquiva() > self.get_ataque() :   
                    return 
                  
            persona.quitar_energia(5.0)
            return 
        else:
            if persona.obtener_capacidad_parada() > self.get_ataque():
                persona.quitar_energia(0.5)
                return
            persona.quitar_energia(5.0)
            return 
        
class GuerreroDelEspacio(Persona):
    def __init__(self, nombre:str,energia: float, deseo_esquivar:float, ataque: float, ataque_rayo: float, esquivar:float, parar:float):
        super().__init__(nombre,Raza.Guerrero,energia, deseo_esquivar)

        if ataque < 0.1: 
            ataque = 0.1 
        if ataque > 0.8:
            ataque = 0.8
        
        if ataque_rayo < 0.3:
            ataque_rayo = 0.3 
        if ataque_rayo > 0.6:
            ataque_rayo = 0.6    
        
        if esquivar < 0.2: 
            esquivar = 0.2
        if esquivar > 0.4:
            esquivar = 0.4
        
        if parar < 0.4:
            parar = 0.4
        if parar > 0.9:
            parar = 0.9  

        self._factor = 1     
        self.__ataque = ataque 
        self.__ataque_rayo = ataque_rayo
        self.__esquivar = esquivar 
        self.__parar = parar 
                  
    def get_raza(self) -> Raza:
        return Raza.Guerrero
    
    def get_ataque(self) -> float:
        return self.__ataque
    
    def get_ataque_rayo(self) -> float: 
        return self.__ataque_rayo
    
    def obtener_capacidad_esquiva(self) -> float:
        return self.__esquivar
    
    def obtener_capacidad_parada(self)-> float:
        return self.__parar 

    def atacar(self, persona: Persona):
        #Si randint da 1, el Guerrero del espacio hara un ataque de rayo. 
        if persona.esta_muerto() or self.esta_muerto():
            return 
        if randint(0,1) == 1:
            self.atacar_rayo(persona)
        else:
            self.atacar_golpe(persona)
        
    def atacar_rayo(self,persona:Persona):
            if persona.esta_muerto() or self.esta_muerto():
                return 
            
            self.quitar_energia(100.0)

            if persona.quiere_esquivar():
                if persona.obtener_capacidad_esquiva() > self.get_ataque_rayo():
                        return 
  
                persona.quitar_energia(300.0  * self._factor)
                return 
            
            else:
                if persona.obtener_capacidad_parada() > self.get_ataque_rayo():
                    persona.quitar_energia(25.0 * self._factor)
                    return
                
                persona.quitar_energia(300.0 * self._factor)
                return
    
    def atacar_golpe(self,persona:Persona):
            if persona.esta_muerto() or self.esta_muerto():
                return 
            
            self.quitar_energia(5.0)

            if persona.quiere_esquivar():
                if persona.obtener_capacidad_esquiva() > self.get_ataque():
                        return 
                    
                persona.quitar_energia(7.0 * self._factor)
                return 
            else:
                if persona.obtener_capacidad_parada() > self.get_ataque():
                    persona.quitar_energia(2.0 * self._factor)
                    return
                
                persona.quitar_energia(7.0 * self._factor)
                return
            
class Sayan(GuerreroDelEspacio):
    def __init__(self, nombre, energia, deseo_esquivar, ataque, ataque_rayo, esquivar, parar):
        super().__init__(nombre,energia, deseo_esquivar, ataque, ataque_rayo, esquivar, parar)
        self._raza = Raza.Sayan
        self._factor = 2
    def get_raza(self) -> Raza:
        return Raza.Sayan

    def atacar(self, persona: Persona ):
        aleatorio = randint(1,3)
        for _ in range (aleatorio):
            if persona.esta_muerto() or self.esta_muerto():
                break 
            super().atacar(persona)
        
class iTorneo(ABC): 
    def __init__(self):
        super().__init__()

    @abstractmethod
    def iniciar_torneo(self):
        pass
    
    @abstractmethod
    def add_persona(self,persona:Persona):
        pass 

    @abstractmethod
    def iniciar_ronda(self):
        pass 

    @abstractmethod
    def filter_torneo(self,delegate: Callable[[Persona], bool]) -> list[Persona]:
        pass 

    @abstractmethod 
    def devolver_ganador(self):
        pass 

class Torneo(iTorneo):
    def __init__(self):
        self._lista : list[Persona] = []
        
        
    def iniciar_torneo(self):
        if not len(self._lista) == 16:
            raise ValueError("Genera los 16 participantes con la funcion: Utils.Generar_Participantes")
        ganadores:list[Persona] = deepcopy(self._lista)
        for _ in range (4):
            ganadores = self.iniciar_ronda(ganadores)
        if len(ganadores) == 1: 
            self._lista = ganadores 

    
    def add_persona(self, persona:Persona):
        if not isinstance(persona,Persona):
            raise ValueError("No esta dentro de la jerarquia de combatientes")
        if len(self._lista) > 15:
            raise ValueError("Lista llena")
        self._lista.append(persona) 
             
    def iniciar_ronda(self,lista:list[Persona])-> list[Persona]:
        ganadores: list[Persona] = []
        for i in range(0,len(lista),2):
            ganador = Utils.generar_combate(lista[i],lista[i + 1])
            ganadores.append(ganador)
        return ganadores 
    
    def filter_torneo(self, delegate: Callable[[Persona],bool]) -> list[Persona]:
        new_list: list[Persona] = []
        for persona in self._lista:
            if delegate(persona):
                new_list.append(persona)
        return new_list 
    
    def devolver_ganador(self):
        if len(self._lista) == 1:
            return self._lista[0]
        raise ValueError("El torneo no tiene un unico ganador,vuelve a iniciar torneo")
                               
class Utils:
        @classmethod
        def generar_humano(cls,nombre: str) -> Humano: 
            energia = uniform(1000.0,2000.0)
            deseo= uniform(0.1,0.9)
            ataque = uniform(0.1,0.8)
            esquivar= uniform(0.4,0.6)
            parar= uniform(0.7,0.9)

            player = Humano(nombre,energia,deseo,ataque,esquivar,parar)
            return player 

        @classmethod
        def generar_guerrero(cls,nombre:str) -> GuerreroDelEspacio:
            energia = uniform(1000.0,2000.0)
            deseo= uniform(0.1,0.9)
            ataque = uniform(0.1,0.8)
            rayo = uniform(0.3,0.6)
            esquivar= uniform(0.2,0.4)
            parar= uniform(0.4,0.9)

            player = GuerreroDelEspacio(nombre,energia,deseo,ataque,rayo,esquivar,parar)
            return player 
    
        @classmethod
        def generar_sayan(cls,nombre:str) -> Sayan:
            energia = uniform(1000,2000)
            deseo= uniform(0.1,0.9)
            ataque = uniform(0.1,0.8)
            rayo = uniform(0.3,0.6)
            esquivar= uniform(0.2,0.4)
            parar= uniform(0.4,0.9)

            player = Sayan(nombre,energia,deseo,ataque,rayo,esquivar,parar)
            return player    

        @classmethod
        def generar_participantes(cls,torneo:Torneo):
            contador = 1 
            for _ in range(16):     
                nombre = "Player" + str(contador) 
                aleatorio = randint(1,3)
                
                if aleatorio == 1:
                    torneo.add_persona(Utils.generar_humano(nombre))
            
                elif aleatorio == 2: 
                    torneo.add_persona(Utils.generar_guerrero(nombre))
            
                elif aleatorio == 3: 
                    torneo.add_persona(Utils.generar_sayan(nombre))
            
                contador += 1      
        
        @classmethod 
        def generar_combate(cls,c1: Persona, c2:Persona) -> Persona:
            if randint(0,1) == 1 : 
                c2.atacar(c1)
                if c1.esta_muerto():
                    return c2 
                
            while True:
                c1.atacar(c2)
                if c2.esta_muerto(): 
                    return c1 
                c2.atacar(c1)
                if c1.esta_muerto():
                    return c2
                
torneo = Torneo()
Utils.generar_participantes(torneo)
torneo.iniciar_torneo() 
print(torneo.devolver_ganador())



            




        
        



5e



