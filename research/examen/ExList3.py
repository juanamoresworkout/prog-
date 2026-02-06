from __future__ import annotations

from typing import *


T = TypeVar("T")

class ExList(Generic[T]):
    def __init__(self):
        self._lista: list[T] = []
        self._count: int = 0 
        
    def count(self) -> int:
        return self._count 
    
    def capacity(self) -> int:
        return len(self._lista)
    
    def first(self) -> T:
        if len(self._lista) == 0:
            raise ValueError("Error de tamaño")
        return self._lista[0]
    
    def last(self) -> T :
        if len(self._lista) == 0:
            raise ValueError("No hay nada")
        return self._lista[self._count - 1]
        
    def reversed(self) -> list[T]:
        if len(self._lista) == 0:
            raise ValueError("No hay nada")
        result: list[T] = [self._lista[i] for i in range(len(self._lista)-1,-1,-1)]
        return result
    
    def get_element(self, index: int) -> T:
        if len(self._lista) == 0:
            raise ValueError("No hay nada")
        if index > (self._count -1) or index <= 0 :
            return self._lista[index]
        
    def set_element_at(self, index: int, element: T) :
        if len(self._lista) == 0:
            raise ValueError("No hay nada")
        if index <= 0 or index > self._count -1:
            raise ValueError("Rango fuera")
        self._lista[index] = element 

    def add(self, element: T):
        if len(self._lista) == self._count:
            self._lista = [self._lista[i] for i in range(len(self._lista))] + [element]
            self._count += 1 
        else: 
            self._lista[self._count] = element
            self._count += 1 

    def remove_at(self, index: int):
        if len(self._lista) == 0:
            raise ValueError("No hay nada")
        if index <= 0 or index > self._count -1:
            raise ValueError("Rango fuera")
        for i in range(index, (self._count - 1)):
            self._lista[i], self._lista[i + 1] = self._lista[i+ 1], self._lista[i]
        self._lista[self._count -1 ] = None 
        self._count -= 1 

    def clear(self):
        for i in range (self._count):
            self._lista[i] = None 
        self._count = 0 
    
    def insert(self,index: int, element: int): 
        if len(self._lista) == 0:
            raise ValueError("No hay nada")
        if index < 0 or index > self._count:
            raise ValueError("Rango fuera")
        if index == 0:
            new_lista:list[T] = [element] + [self._lista[i] for i in range(len(self._lista))]
            self._lista = new_lista
            self._count += 1 

        elif index == self._count:
                if index < len(self._lista):
                    self._lista[index] = element
                if index == self._count:
                    self.add(element)
        else:
            new_lista = [self._lista[i] for i in range(0, index)] + [element] + [self._lista[i] for i in range(index,len(self._lista))]
            self._lista = new_lista
            self._count += 1   

    

    

        
        
    

        

            





    

    




        


            
    

        
