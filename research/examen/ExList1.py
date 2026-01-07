from __future__ import annotations
from typing import *

T = TypeVar('T')

class ExList(Generic[T]): 
    __count: int 
    __lista: list
    
    def __init__(self,capacidad : int):
        if capacidad <= 0 :
            raise ValueError ("Valor negativo, no valido")
        self.__lista: list[T] = [None for _ in range (capacidad)]
        self.__count: int = 0 

    def count(self) -> int :
        return self.__count
    
    def capacity(self) -> int :
        return len(self.__lista)
    
    def first(self) -> T:
        if self.count() <= 0:
            raise ValueError ("No hay objetos")
        return self.__lista[0]
    
    def last(self) -> T:
        if self.count() <= 0:
            raise ValueError ("No hay objetos")
        return self.__lista[self.count() -1]
    
    def reverse(self) -> list[T]:
        if self.count() <= 0 :
            raise ValueError ("No hay objetos en la lista")
        new_list: list[T] = [self.__lista[i] for i in range(self.__count -1,-1,-1)] + [None] * [len(self.__lista) - self.__count]

    def get_element_at(self,index: int ) -> T :
        if index < 0 or index > (self.__count -1) :
            return T
        return self.__lista[index]
        
    def set_element_at(self,index:int,element:T): 
        if index < 0 or index > (self.__count -1):
            raise ValueError("Fuera de rango")
        self.__lista[index] = element

    def add(self,element:T ):
        if len(self.__lista) == self.__count :
            raise ValueError("Lista llena")
        self.__lista[self.__count] = element
        self.__count += 1
    
    def remove_at(self,index: int ):
        if index < 0 or index > len(self.__count -1):
            raise ValueError ("Indice fuera de rango")
        for i in range(index,self.__count - 1):
            self.__lista[i] = self.__lista[i + 1 ]
            self.__lista[self.__count -1 ] = None 
            self.__count -= 1 

    def clear(self):
        for i in range (self.__count):
            self.__lista[i] = None 
        self.__count = 0 
    
    def insert(self,index: int, element: T) : 
        if index < 0 or index > self.__count :
            raise ValueError("Fuera de rango")
        if self.__count == len(self.__lista):
            raise ValueError("Lista llena o crea")
        
        if index < self.__count: 
            for i in range(self.__count, index, -1): 
                self.__lista[i] = self.__lista[i - 1 ] 
            self.__lista[index] = element 
        self.__count += 1 

        if index == self.__count: 
            self.__lista[index] = element 
        self.__count += 1 

    def index_of(self,element: T ) -> int : 
        for i in range(0, self.__count):
            if self.__lista[i] == element:
                return i 
    
    def contains(self, element: T) -> bool: 
        return element in self.__lista 
    
    def index_of_delegate(self, delegate: Callable[[T], bool]) -> int : 
        for i in range(self.__count):
            if delegate(self.__lista[i]):
                return i 
      
    #Comparar con la funcion de arturo, preguntar a profesor
    def contains_delegate(self,landa: Callable[[T],bool]) -> bool : 
        for i in range(self.__count):
             if landa(self.__lista[i]): 
                 return True
        return False 
 
    def visit(self,landa: Callable[[T],bool]):
        for i in range(self.__count): 
            landa(self.__lista[i])
    
    #Explicar, ejemplo tomado de internet(ChatGpt), preguntar si es valido
    def sort_delegate(self, delegate: Callable[[T, T], bool]):
        for i in range(self.__count - 1):
            for j in range(self.__count - 1):
                if delegate(self.__lista[j], self.__lista[j + 1]):
                    self.__lista[j], self.__lista[j + 1] = self.__lista[j + 1], self.__lista[j]


    

#nuevo = ExList(4)
#nuevo.add("Texto")
#nuevo.add(1)
#nuevo.add(3)
#nuevo.add(2)

#indce = nuevo.index_of_delegate(lambda x : x == 2)
#print(indce)