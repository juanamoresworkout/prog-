def quitar_duplicados(num: int,lista: list[int]) -> bool: 
    if num in lista:
        return False
    return True 
    
def procesar_enteros(list: list[int]):
    nueva_lista = []
    for numero in list: 
        if numero >= 0 and  not numero % 2 == 0:
            numero *= numero 
        if quitar_duplicados(numero, nueva_lista):
            nueva_lista.append(numero)
    return nueva_lista

lista = [3,3]
lista2 = procesar_enteros(lista)
print(lista2)
    