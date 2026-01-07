from __future__ import annotations
from typing import *

T = TypeVar('T')


class ExQueue(Generic[T]):
    lista: list[T]

    def __init__(self):
        self.__lista: list[T] = []

    def count(self) -> int: 
        return len(self.__lista)
    
    def front(self) -> T:
        if len(self.__lista) == 0 : 
            raise  ValueError("Lista vacia")
        return self.__lista[0]
    
    def rear(self) -> T:
        if len(self.__lista) == 0 : 
            return 
        return self.__lista[-1]
    
    def reverse(self) -> list[T]:
        new_list: list[T] = [self.__lista[i] for i in range (len(self.__lista) -1 ,-1 ,-1)]
        return new_list
    
    #Enseñar esto al profesor, forma de añadir un elemento  de forma simplificada
    def enqueue(self,element: T):
        new_list: list[T] = [self.__lista[i] for i in range (len(self.__lista))] + [element]
        self.__lista = new_list 
    
    def dequeue(self) -> T: 
        if len(self.__lista) == 0: 
            return 
        new_list:list[T] = [self.__lista[i] for i in range(1,len(self.__lista))]
        self.__lista = new_list 

    def contains(self,element:T) -> bool:
        if len(self.__lista) == 0:
            raise ValueError("Lista vacia")
        for i in range (len(self.__lista)): 
            if self.__lista[i] == element:
                return True 
        return False 
    
    def remove(self,element:T):
        if not self.contains(element):
            raise ValueError("El objeto que deseas eliminar no esta en la lista")
        x = self.__lista.index(element)
        new_list:list[T] = [self.__lista[i] for i in range(0,x)] + [self.__lista[i] for i in range(x +1,len(self.__lista))]
        self.__lista = new_list 

    def clear(self): 
        self.__lista = []
    

    def contains1(self,delegate: Callable[[T], bool]) -> bool: 
        for item in self.__lista:
            if delegate(item):
                return True
        return False 

    def visit(self,delegate:Callable[[T],bool]) -> bool:
        for item in self.__lista:
            delegate(item)

    def filter(self,filtro:Callable[[T],bool]) -> ExQueue[T]:
        new_list = ExQueue()
        for item in self.__lista: 
            if filtro(item):
                new_list.enqueue(item)