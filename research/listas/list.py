#Para poder declarar List:int bien 
from typing import List

def contar_palabras(lista : List[int]) -> int :
    return len(lista)
#Me pasan una lista de enteros y devuelvo el numero mayor que hay 
def devolver_mayor(lista) -> int:
    i = 1 
    buscar_mayor = lista[0]
    
    while i < len(lista) : 
        if lista[i] > buscar_mayor :
            buscar_mayor = lista[i]
        i +=1
    return buscar_mayor 

#Una funcion que me devuelva la posicion del mayor elemento

def devolver_maxima(lista : List[int]) -> int : 
    if len(lista) == 0 :
        return -9999
    i = 1
    index = 0 
    buscar_mayor = lista[0]
    
    while i < len(lista) : 
        if lista[i] > buscar_mayor : 
            buscar_mayor = lista [i]
            index = i 
        i +=1 
        
    return  index 

#Hacer una funcion que devuelva la media de los elemento de la lista
