from __future__ import annotations

from typing import *


T = TypeVar("T")

class ExTable2DV1(Generic[T]):
    def __init__(self ):
        self._alto = 0
        self._ancho = 0
        self._lista = []

    def get_width(self) -> int:
        return self._ancho

    def get_height(self) -> int:
        return self._alto 

    def reset(self):
        self._alto = 0 
        self._ancho = 0 
        self._lista = []

    def set_size(self, width: int, height: int):
        if width <= 0 :
            self.reset()
            return
        if height <= 0 :
            self.reset()
            return
        
        self._alto = width 
        self._ancho = height
        self._lista = [T for _ in range((width * height))]        

    def get_cell_at(self, x: int, y: int) -> T:
        if x < 0 or  x > self._ancho:
            return
        if y < 0 or  y > self._alto:
            return  
        index = y * self._ancho + x 
        return self._lista[index]

    def set_cell_at(self, x: int, y: int, value: T):
        if x < 0 or  x > self._ancho:
            return
        if y < 0 or  y > self._alto:
            return  
        index = y * self._ancho + x 
        self._lista[index] = value 
    
    #visit normal y visit celda y filter
    def visit(self, callable: Callable[[T],None]):
        for i in range(len(self._lista)):
            callable(self._lista[i])

    def visit_celda(self, callable:Callable[[int,int,T], None]):
        for i in range(self._ancho):
            for j in range(self._alto):
                element = self.get_cell_at(i,j)
                callable(i,j,element)
    
    def filter_celda(self,callable: Callable[[int,int,T], bool]) -> list[T]:
        result:list[T] = []
        for i in range(self._ancho):
            for j in range(self._alto):
                element = self.get_cell_at(i,j)
                if callable(i,j,element) :
                    result.append(element)

tabla2d = ExTable2DV1()
tabla2d.set_size(10,10)
tabla2d.set_size(10,10)

tabla2d.visit_celda(lambda x, y, t : tabla2d.set_cell_at(x,y,f'Tengo {x} y {y}')) 
tabla2d.visit(lambda x : print(x))


