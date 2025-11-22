#NickName: Loves 
def es_par(n:int) -> bool : 
    return n % 2 == 0

def procesar_enteros(lista : list[int]) -> list [int] : 
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if j < len(lista) and lista[i] == lista[j]:
                lista.remove(lista[j])
#Lo escrito de remove al lado es por esto. No recordaba lo de remove. 
    for num in lista : 
        if num < 0: 
            lista.remove(num)
        if es_par(num):
            lista.remove(num)
        #Fallo aquí porque solo se guarda en la variable temporal num, quería decir por cada numero de la lista = num**2
        #lista[] = num**2 
        #En un principio queria usar for i in range, para comparar lista[i]  controlar mejor
        #Al hacerte una consulta, malentendi tu consejo y elimine el in range. 
        num = num** 2 
    return lista 

#Yo queria hacer una comprobacion con una lista nueva, donde solo añado si se cumple el if ,
#  pero como pense que de ninguna forma se podia usar in, me lio la logica.

#Si no me hubiera liado una comprobación hubiera sido: 
# for i in lista_original
# if num <= 0 and not is es_par(num) and if not comprobar_lista(num,new_lista)


#Comprobar lista sería una funcion que le paso un num y lista, y devuelve un bool.
# recorre la lista con un for numero in lista y
# si numero == num 
#    return True 
#Fuera del bucle return False
# Esta funcion es de cero, me jugaron una mala pasada los nervios.  
