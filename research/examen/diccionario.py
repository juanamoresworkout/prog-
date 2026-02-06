from __future__ import annotations

from typing import *
from enum import Enum 
from copy import *

V = TypeVar('V')
K = TypeVar('K')
T = TypeVar('T')

class MergePolicy(Enum):
    KEEP_OLD = 0 
    REPLACE = 1
    ERROR = 2 


class Diccionario(Generic[K,V]):
    def __init__(self):
        self._keys: list[K] = []
        self._values: list[V] = []

    def validar_tamaño_correcto(self) -> bool:
        return len(self._keys) == len(self._values)

    def get_longitud(self) -> int :
        if not self.validar_tamaño_correcto():
            raise ValueError("Tamaño incorrecto")
        return len(self._keys)

    def visit(self, visitor: Callable[[K,V], None]):
        if not self.validar_tamaño_correcto():
            raise ValueError("Tamaño incorrecto")
        for i in range(len(self._keys)):
            visitor(self._keys[i], self._values[i])

    def keys(self) -> list[K]:
        result: list[K] = []
        self.visit(lambda k, v : result.append(k))
        return result
    
    def values(self) -> list[K]:
        result: list[K] = []
        self.visit(lambda k, v : result.append(v))
        return result
    
    def index_of(self,key: K) -> int: 
        if not self.validar_tamaño_correcto():
            raise ValueError("Error de longitu")
        for i in range(len(self._keys)):
            if self._keys[i] == key:
                return i 
        return -1 
     
    def contains_key(self, key: K) -> bool:
            return self.index_of(key) != -1 
            
    def get(self, key: K) -> V|None :
        if self.index_of(key) != -1:
            return self._values[self.index_of(key)]
        return None 
    
    def set_key_value(self, key: K, value: V) -> bool: 
        index = self.index_of(key)
        if index != -1:  
            self._values[index] = value
            return False
        else:
            self._keys.append(key)
            self._values.append(value)
            return True 
    
    def remove(self, key: K) -> tuple[bool, V|None] : 
        if self.contains_key(key):
            index = self.index_of(key)
            self._keys.pop(index)
            valor = self._values.pop(index)
            return (True,valor)
        
        else:
            return (False,None)
        
    def filter_items(self, predicate: Callable[[K,V],bool]) -> Diccionario[K,V] : 
        if not self.validar_tamaño_correcto():
            raise ValueError("Tamaño incorrecto")
        result: Diccionario[K,V] = Diccionario()
        for i in range(len(self._keys)):
            if predicate(self._keys[i],self._values[i]):
                result.set_key_value(self._keys[i],self._values[i])
    
    def visitor(self, visit: Callable[[T,V],None]):
        for i in range(len(self._keys)):
            visit(self._keys[i],self._values[i]) 

    def map_values(self, transform: Callable[[V],T]) -> Diccionario[K,T]: 
        new_diccionario: Diccionario[K,T] = Diccionario()
        for i in range(len(self._keys)):
            new = transform(self._values[i])
            new_diccionario.set_key_value(self._keys[i],new)
        return new_diccionario
    
    def map_items(self,transform: Callable[[K,V],T]) ->list[T]:
        result: list[T] = []
        for i in range(len(self._keys)):
            tupla = transform(self._keys[i],self._values[i])
            result.append(tupla)
        return result 
    
    def count_if(self,predicate: Callable[[K,V],bool]) -> int : 
        count = 0 
        for i in range(len(self._keys)):
            if predicate(self._keys[i],self._values[i]):
                count += 1 
        return count 

    def sort(self, sort: Callable[[K,K],bool]):
        for i in range(len(self._keys)):
            for j in range(len(self._keys) - 1):
                if sort(self._keys[j],self._keys[j + 1]): 
                    self._keys[j],self._keys[j + 1] = self._keys[j + 1],self._keys[j]
                    self._values[j],self._values[j + 1] = self._values[j + 1],self._values[j]


nuevo = Diccionario()
nuevo.set_key_value("Primera", 2000)
nuevo.set_key_value("Segunda", 75)

multiplicado = nuevo.map_items(lambda x,y: (x + f"{ y}", y * 2) )
print(multiplicado)














        


    





                
    
        



   
        

    

    


