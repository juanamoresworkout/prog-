def contar_palabras(lista):
    return len(lista)

def devolver_mayor(lista):
    i = 0 
    buscar_mayor = 0
    
    while i < len(lista) : 
        if lista[i] > buscar_mayor :
            buscar_mayor = lista[i]
        i +=1
    return buscar_mayor 
