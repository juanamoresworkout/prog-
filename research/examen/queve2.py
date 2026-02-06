from __future__ import annotations

from typing import *
from copy import * 

T = TypeVar("T")

class ExQueue:
    def __init__(self):
        self._lista: list[T] = []

    def count(self) -> int:
        return len(self._lista)
    
    def front(self) -> T : 
        if len(self._lista) == 0 :
            raise ValueError("Listuki vacia")
        return self._lista[0]

    def rear(self) -> T :
        if len(self._lista) == 0:
            raise ValueError["Lista vacia"]
        return self._lista[len(self._lista) - 1 ]
    
    def reversed(self) -> list[T]:
        nueva_colita = ExQueue()
        nueva_colita._lista = [self._lista[i] for i in range(len(self._lista)-1,-1,-1)]
        return nueva_colita
    
    def enqueue(self, generico: T):
        pito: list[T] = [self._lista[i] for i in range(len(self._lista))] + [generico]
        self._lista = pito 

    def dequeue(self)-> T:
        nueva:list[T] = [self._lista[i] for i in range(1, len(self._lista))]
        primero = self._lista[0]
        self._lista = nueva 
        return primero 
    
    def contains(self,element:T) -> bool:
        for i in range(len(self._lista)):
            if self._lista[i] == element:
                return True 
        return False

    def index(self,element: T) -> int:
        for i in range(len(self._lista)):
            if self._lista[i] == element:
                return i

    def remove(self, element:T):
        if len(self._lista) == 0:
            raise ValueError("Lista vacia")
        if self.index(element) == 0 :
            self.enqueue(element)
        else:
            jo = self.index(element)
            self._lista = [self._lista[i]for i in range(0,jo)] + [self._lista[i] for i in range((element +1),(len(self._lista)))]

    def clear(self):
        self._lista = []

    def contains(self, delegate: Callable[[T],bool]) ->bool:
        for element in self._lista:
            if delegate(element):
                return True
        return False 
    
    def visit(self, delegate: Callable[[T],None]):
        for element in self._lista:
            delegate(element)

    def filter(self, delegate: Callable[[T],bool]) ->list[T]:
        result: list[T] = []
        for element in self._lista:
            if delegate(element):
                result.append(element)
        return result
    
    def clone(self) ->ExQueue:
        return deepcopy(self)
    
    def array(self) -> list[T]:
        return deepcopy(self._lista)
    
    



    
               
     