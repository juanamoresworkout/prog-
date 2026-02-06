from Humano import *
from Guerrero import *
from Sayan import *
from random import uniform


class Utils: 

    @classmethod
    def generar_humano(cls, nombre: str)-> Humano:
        energia = uniform(1000.0,2.000)
        deseo = uniform(0.1,0.9)
        ataque = uniform(0.1,0.8)
        esquivar = uniform(0.4,0.6)
        parar = uniform(0.7,0.9)

        return Humano(nombre,energia,deseo,ataque,esquivar,parar)
    
    @classmethod
    def generar_guerrero(cls,nombre: str) -> Guerrero:
        energia = uniform(1000.0,2000.0)
        deseo = uniform(0.1,0.9)
        ataque = uniform(0.1,0.8)
        esquivar = uniform(0.2,0.4)
        parar = uniform(0.4,0.9)
        rayo = uniform(0.3,0.6)

        return Guerrero(nombre,energia,deseo,ataque,esquivar,parar,rayo)

    @classmethod
    def generar_sayan(cls,nombre: str) -> Sayan:
        energia = uniform(1000.0,2000.0)
        deseo = uniform(0.1,0.9)
        ataque = uniform(0.1,0.8)
        esquivar = uniform(0.2,0.4)
        parar = uniform(0.4,0.9)
        rayo = uniform(0.3,0.6)

        return Sayan(nombre,energia,deseo,ataque,esquivar,parar,rayo)
      






