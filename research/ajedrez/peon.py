from __future__ import annotations

from figura import *
from enums import TipoPieza

# -----------------------------
# Clase Peón(Hereda de Figura):
# -----------------------------
class Peon(Figura):
    
    def get_tipo_pieza(self) -> TipoPieza:
        return TipoPieza.PEON

    def _tupla_blancas(self) -> List[tuple[int, int]]:   
            tuplas:list[tuple[int, int]] = [(1,1),(-1,1),(0,1)] 
            if self._contador_movimientos == 0 : 
                tuplas.append((0,2))
            return tuplas 
    
    def _tuplas_negras(self) -> list[tuple[int, int]]:
        tuplas: list[tuple[int, int]] = [(1, -1), (-1, -1), (0, -1)]
        if self._contador_movimientos == 0:
            tuplas.append((0, -2))
        return tuplas

    def movimiento_posible(self, tablero: "Tablero") -> List[Tuple[int, int]]:
        result:  list[Tuple[int,int]] = []
       
        if self.get_color() == Color.BLANCA:
            tuplas = self._tupla_blancas()  
        else: 
            tuplas = self._tuplas_negras()      

        for posicion in tuplas:
            x = self._x + posicion[0]
            y = self._y +  posicion[1]

            if self.fuera_de_rango(x,y): 
                continue 

            otra_figura = tablero.get_figura_en(x,y)

            if posicion == (0, 2):
                if tablero.get_figura_en(self._x, self._y + 1) is not None:
                    continue

            if posicion == (0, -2):
                if tablero.get_figura_en(self._x, self._y - 1) is not None:
                    continue
          
            if otra_figura is not None and (posicion == (0, 1) or posicion == (0, 2) or posicion == (0, -1) or posicion == (0, -2)):
                continue

            if posicion == (1,1) or posicion == (-1,-1) or posicion == (-1,1) or posicion == (1,-1):
                if otra_figura == None:
                    continue 

            if otra_figura != None :
                if otra_figura.get_color() == self.get_color():
                    continue  
                else:
                     result.append((x,y))
            else : 
                result.append((x,y))
        return result 
                               
