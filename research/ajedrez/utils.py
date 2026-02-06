from __future__ import annotations
from figura import *
from enums import *
from peon import * 
from torre import *
from caballo import *
from alfil import * 
from rey import *
from reina import *

class Generar:

    @classmethod
    def generar_peones(cls,lista: list[Figura]):
        if Generar.comprobar_pieza(TipoPieza.PEON,lista):
            y_blancas = 1
            y_negras = 6  

            for i in range (0,8):
                peon_blanco = Peon(Color.BLANCA, i, y_blancas)
                peon_negro = Peon(Color.NEGRA, i, y_negras)
                lista.append(peon_blanco)
                lista.append(peon_negro)
    
    @classmethod
    def generar_torres(cls, lista:list[Figura]):
        if Generar.comprobar_pieza(TipoPieza.TORRE, lista):
            y_blancas = 0 
            y_negras = 7 

            for x in (0, 7):
                torre_blanca = Torre(Color.BLANCA, x, y_blancas)
                torre_negra = Torre(Color.NEGRA, x , y_negras)
                lista.append(torre_blanca)
                lista.append(torre_negra)
    
    @classmethod
    def generar_caballos(cls, lista:list[Figura]):
       if Generar.comprobar_pieza(TipoPieza.CABALLO, lista):
           y_blanca = 0 
           y_negra = 7 
       
           for x in (1,6):
               caballo_blanco = Caballo(Color.BLANCA, x , y_blanca)
               caballo_negra = Caballo(Color.NEGRA, x , y_negra)
               lista.append(caballo_blanco)
               lista.append(caballo_negra)
    
    @classmethod
    def generar_alfil(cls, lista:list[Figura]):
        if Generar.comprobar_pieza(TipoPieza.ALFIL, lista):
            y_blanca = 0 
            y_negra = 7 

            for x in(2,5):
                alfil_blanco = Alfil(Color.BLANCA, x , y_blanca)
                alfil_negro = Alfil(Color.NEGRA, x , y_negra)
                lista.append(alfil_blanco)
                lista.append(alfil_negro)
    
    @classmethod
    def generar_reina(cls, lista:list[Figura]):
        if Generar.comprobar_pieza(TipoPieza.REINA,lista):

            reina_blanca = Reina(Color.BLANCA,3,0)
            reina_negra = Reina(Color.NEGRA,3,7)
            lista.append(reina_blanca)
            lista.append(reina_negra)

    @classmethod
    def generar_rey(cls, lista: list[Figura]):
        if Generar.comprobar_pieza(TipoPieza.REY,lista):

            rey_blanco = Rey(Color.BLANCA,4,0)
            rey_negro = Rey(Color.NEGRA,4,7)
            lista.append(rey_blanco)
            lista.append(rey_negro)
            
    @classmethod
    def comprobar_pieza(cls,tipo: TipoPieza,lista:list[Figura])-> bool:
        for i in range(len(lista)):
            if lista[i].get_tipo_pieza() == tipo:
                return False
        return True 
