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
def devolver_media(lista) -> float :
    i = 0 
    sumatory = 0 
    while i < len(lista):
        sumatory = sumatory + lista[i] 
        i += 1
    resultado : float = sumatory/ 2 
    return resultado

def devolver_inversa(lista) : 
    if len(lista) == 0 :
        return []
    i = len(lista) - 1 
    inversa = []
    while i >= 0 :
        inversa.append(lista[i])
        i -=1
    return inversa 

#Devolver index de la posicion del numero que yo le pase de la lista de fibonacci del 
def posicion_fibonacci (number: int ) -> int :
    a = 0 
    b = 1 
    i = 0 
    if number == 0:
        return a
    elif number == 1:
        return b
    while i < number -1 :
        c = a + b 
        a = b 
        b = c 
        i += 1 
    return b 