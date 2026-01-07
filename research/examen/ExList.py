from __future__ import annotations
from typing import * 

T = TypeVar('T')

class ExList: 
    array_list: list[T]

    def __init__(self, capacidad):
        if capacidad <= 0 :
            raise ValueError ("El tamaño de la lista no puede ser negativo")
        self.__lista :list[T] = [None for i in range(0,capacidad)]
        self.__count = 0 
        
    def count(self) -> int: 
       return self.__count 
    
    def capacity(self) -> int : 
        return len(self.__lista)
    
    def firs(self) -> T : 
        if self.__count == 0:
            raise ValueError ("Lista vacia")
        return self.__lista[0]
    
    def last(self) -> T : 
        if self.__count == 0 :
            raise ValueError("Lista vacia")
        return self.__lista[self.__count -1]
    
    #Forma de añadir la lista inversa y los none , en una vez 
    def reverse(self) -> list[T]:
        if len(self.__lista) == 0 :
            raise ValueError ("Lista vacia")
        new_list: list[T] = [self.__lista[i] for i in range(self.__count - 1, -1, -1) ] + [None] * [(len(self.__lista)- self.__count)]

    def get_element_add(self,index: int) -> T : 
        if index < 0 or index > (self.__count -1) :
            raise ValueError ("Index fuera de rango")
        return self.__lista[index]

    def set_element_add(self,index: int, element: T) :
        if index < 0 or index > (self.__count -1) :
            raise ValueError ("Index fuera de rango")  
        self.__lista[index] = element 

    def add(self,element: T):
        if self.__count == len(self.__lista):
            raise ValueError ("Lista llena")
        self.__lista[self.__count] = element 
        self.__count += 1 

    def remove_add(self,index:int):
        if index < 0 or index > (self.__count -1) : 
            for i in range(index,self.__count -1 ):
                self.__lista[i] = self.__lista[i + 1]
            self.__lista[self.__count - 1 ] = None 
            self.__count -= 1 
    
    def clear(self):
        if self.__count >= 1 : 
            for i in range (0, self.__count):
                self.__lista[i] = None 

    

        
    