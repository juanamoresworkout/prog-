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

#FUNCIONES RECURSIVAS INVESTIGAR 
def get_sumatory(n):
    if n <= 0:
        return 0 
    return n + get_sumatory(n-1)
#print(get_sumatory(4))


def sacar_minimo(lista) :
    minimo = lista[0]
    for num in lista:
        if num < minimo :
            minimo = num 
    return minimo 
def sacar_maximo(lista):
    maximo = lista[0]
    for num in lista: 
        if num > maximo:
            maximo = num 
    return maximo 
def sacar_media(lista) -> float:
    resultado = (sacar_minimo(lista) + sacar_maximo(lista))/ 2 
    return resultado 

def sacar_media2(lista) -> float: 
    minimo = sacar_minimo(lista)
    maximo = sacar_maximo(lista)

    resultado = (maximo + minimo)/2
    return resultado 

#Pasamos una lista, donde me de el numero 
def devolver_numeros_mayores(lista: List[int | float], threshold: int | float,
        incluir_mayores: bool,
        incluir_iguales: bool,
        inclur_menores: bool) -> int : 
    
    contador = 0 
    for valor in lista :
        if incluir_mayores and valor > threshold :
            contador += 1 
        if incluir_iguales and valor == threshold :     
            contador += 1 
        if inclur_menores and valor < threshold : 
            contador += 1 
    return contador 


