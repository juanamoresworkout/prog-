from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Tuple, TYPE_CHECKING 

from enums import Color, TipoPieza
if TYPE_CHECKING:
    from tablero import Tablero

# ------------------
# Clase Figura(ABC):
# ------------------
class Figura(ABC):
    """
    La figura tiene un color (enum Color). Protected.
    La figura tiene una X. Protected.
    La figura tiene una Y. Protected.
    La figura tiene un contador_movimientos. Protected.
    """

    def __init__(self, color: Color, x: int, y: int) -> None:
        if not isinstance(color,Color):
            raise ValueError("Tipo de color no valido.")
        
        if x < 0 or x > 7:
            raise ValueError("Fuera de rango")

        if y < 0 or y > 7:
            raise ValueError("Fuera de rango")

        self._color: Color = color
        self._x: int = x
        self._y: int = y
        self._contador_movimientos: int = 0

    @abstractmethod
    def get_tipo_pieza(self) -> TipoPieza:
        pass

    def get_position(self) -> Tuple[int, int]:
        return (self._x,self._y)
    

    def get_color(self) -> Color:
        return self._color
    
    def set_posicion_total(self,x: int, y: int):
        self.set_x(x)
        self.set_y(y)
    
    def get_x(self) -> int:
        return self._x
    
    def get_y(self) -> int : 
        return self._y

    def set_y(self, y:int):
        if y < 0 or y > 7:
            raise ValueError("Rango fuera.")
        self._y = y 
    
    def set_x(self, x:int):
        if x < 0 or x > 7:
            raise ValueError("Rango fuera.")
        self._x = x
    
    def get_movimientos(self) -> int:
        return self._contador_movimientos
    
    def fuera_de_rango(self, x: int, y: int) -> bool:
        if x < 0 or y < 0 :
            return True
        if x > 7 or y > 7:
            return True 
        return False 
    
    def direccion_posible(self,lista: list[Tuple], tablero: Tablero)-> list[Tuple]:
        result: list[Tuple] = []

        for posicion in lista:
            for i in range(1,9):
                x = self._x + i * posicion[0]
                y = self._y + i * posicion[1]
                
                if self.fuera_de_rango(x,y): 
                    break 

                if tablero.get_figura_en(x,y) != None:
                    if tablero.get_figura_en(x,y).get_color() == self.get_color():
                        break 
                    else:
                        result.append((x,y))
                        break
                else:
                    result.append((x,y))
        return result 

    def incrementar_movimiento(self):
        self._contador_movimientos += 1 
    
    def decrementar_movimiento(self):
        self._contador_movimientos -= 1 


    @abstractmethod
    def movimiento_posible(self, tablero: "Tablero") -> List[Tuple[int, int]]:
        """
        Devuelve lista de (x,y) posibles desde la posición recibida.
        """
        pass
