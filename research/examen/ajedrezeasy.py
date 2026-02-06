from __future__ import annotations

from abc import *
from typing import * 
from enum import Enum

class Color(Enum):
    BLANCO = 0 
    NEGRO = 1 

class TipoFigura:
    REY = 0 
    PEON = 1 

class Position:
    def __init__(self, x: int, y: int):
        if x < 0 or x > 7 :
            raise ValueError("Error fuera de rango")
        if y < 0 or y > 7 : 
            raise ValueError("Error fuera de rango ")
        
        self._x : int = x
        self._y : int = y 
    
    def set_position_x(self,x: int ):
        if x is None:
            raise ValueError("Esta vacio")
        self._x = x 
    
    def get_position_x(self) -> int :
        return self._x
    
    def set_position_y(self, y : int):
        if y is None:
            raise ValueError("Esta vacio")
        self._y = y 
    
    def get_position_y(self) -> int : 
        return self._y
    
    def get_position_total(self) -> tuple[int,int]:
        return self._x,self._y

class IFigure(ABC):
        
        def __init__(self):
            super().__init__()
        
        @abstractmethod
        def get_color(self) -> Color:
            pass 
        @abstractmethod
        def get_type(self) -> TipoFigura:
            pass 
        @abstractmethod
        def move_to(self, posicion: tuple[int,int]):
            pass
        @abstractmethod
        def get_available_position(self) -> list[tuple[int,int]] :
            pass 
        @abstractmethod
        def has_been_moved(self) -> bool : 
            pass 
    
class Figure(IFigure):
        def __init__(self, posicion: Position, color: Color):
            if color is None or posicion is None:
                raise ValueError("No se a pasado color")

            self._se_movio = False 
            self._color = color 
            self._posicion = posicion 

        def get_color(self) -> Color:
            return self._color

        @abstractmethod
        def get_type(self) -> TipoFigura:
            pass 

        def move_to(self, posicion: tuple[int,int], board: Board):
            if posicion is None:
                raise ValueError("Posicion no valida")
            movimientos = self.get_available_position(board)
            if posicion in movimientos: 
                if board.get_pieza(posicion[0],posicion[1]) is not None:
                    board.remove_pieza(posicion[0],posicion[1])
                    self._posicion.set_position_x(posicion[0])
                    self._posicion.set_position_y(posicion[1])
                    self._se_movio = True 
                
                else:
                    self._posicion.set_position_x(posicion[0])
                    self._posicion.set_position_y(posicion[1])
                    self._se_movio = True
                  
        def get_position(self):
            return self._posicion.get_position_total()
                
        @abstractmethod
        def get_available_position(self,board) -> list[tuple[int,int]] :
            pass 

        def has_been_moved(self) -> bool :
            if self._se_movio is False:
                return False 
            return True 
                    
class Rey(Figure):
        def __init__(self, posicion, color):
            super().__init__(posicion, color)
        
        def get_type(self):
            return TipoFigura.REY
        
        def get_available_position(self, board: Board) -> list[tuple[int,int]]:
            x = self._posicion.get_position_x()
            y = self._posicion.get_position_y()
            result: list[tuple[int,int]] = []
            for i in range(-1,2):
                for j in range(-1,2):
                    dx = x + i 
                    dy = y + j
        
                    if x > 7 or x < 0 or y > 7 or y < 0 : 
                        continue 
                    figura_enemiga: Figure = board.get_pieza(dx,dy)
                    if  figura_enemiga is not None:
                        if figura_enemiga.get_color() != self.get_color():
                            result.append((dx,dy))
                            continue
                    else:
                        result.append((dx,dy))
            return result 
        
class Peon(Figure):
        def __init__(self, posicion, color):
            super().__init__(posicion, color)
        
        def get_type(self):
            return TipoFigura.PEON
        
        def get_available_position(self, board: Board) -> list[tuple[int,int]]:
            x = self._posicion.get_position_x()
            y = self._posicion.get_position_y()
            result: list[tuple[int,int]] = []
            if self._color == Color.BLANCO:
                valor_y = (y + 1)
                doble_paso = (x, y + 2)

            if self._color == Color.NEGRO:
                valor_y = (y - 1)
                doble_paso = (x, y - 2)

            if not self.has_been_moved():
                if board.get_pieza(doble_paso[0],doble_paso[1]) is None:   
                    result.append(doble_paso)        
            for i in range(-1,2):
                dx = x + i 
                dy = valor_y

                if dx > 7 or dx < 0 or dy > 7 or dy < 0 : 
                    continue 
                if i == 0:
                    pieza_rival = board.get_pieza(dx,dy)
                    if pieza_rival is not None :
                        result.append((dx,dy))
                        continue
                if i == -1 or i == 1 :
                    pieza_rival = board.get_pieza(dx,dy)
                    if pieza_rival is not None :
                        if pieza_rival.get_color() !=  self.get_color():
                            result.append((dx,dy))
                            continue
                else:
                    result.append((dx,dy))

            return result 
        
class Board:
        def __init__(self):
            self._figuras: list[Figure] = []
        
        def get_pieza(self, x: int , y : int)-> Figure |None:
            if x < 0 or x > 7 :
                raise ValueError("Numero fuera de rango")
            if y < 0 or y > 7: 
                raise ValueError("Numero fuera de rango")
            for pieza in self._figuras:
                if pieza.get_position() == (x,y):
                    return pieza 
            return None 
        
        def remove_pieza(self,x: int , y : int):
            if x < 0 or x > 7 :
                raise ValueError("Numero fuera de rango")
            if y < 0 or y > 7: 
                raise ValueError("Numero fuera de rango")
            for i in range(len(self._figuras)):
                if self._figuras[i].get_position() == (x,y):
                    self._figuras.pop(i)
                    break 

        def add_reyes(self):
            if not self.hay_tipo_pieza_en(TipoFigura.REY):
                raise ValueError("Reyes dentro")
            rey_blanco = Rey(Position(4,0),Color.BLANCO)
            rey_negro = Rey(Position(7,0),Color.NEGRO)
            self._figuras.append(rey_negro)
            self._figuras.append(rey_blanco)

        def add_peon(self):
            if not self.hay_tipo_pieza_en(TipoFigura.PEON):
                raise ValueError("Peones dentro")
            y_blanca = 0
            y_negra = 7 
            for i in range(0,7):
                peon_blanco = Peon(Position(i,y_blanca),Color.BLANCO)
                peon_negro = Peon(Position(i,y_negra),Color.NEGRO)
                self._figuras.append(peon_blanco)
                self._figuras.append(peon_negro)
            
        def hay_tipo_pieza_en(self, type: TipoFigura) -> bool:
            for fig in self._figuras:
                if isinstance(fig, type):
                    return True 
            return False 