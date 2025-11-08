def secuencial_number(num: int , lista: list[int]) -> int : 
    for i in range(len(lista)):
       if lista[i] == num :
           return i 
    return -1 


lista = [1,2,4]

print(secuencial_number(4,lista))

