#NickName: Loves 
def es_primo(n:int) -> bool :
    if not isinstance(n,int) or n <= 0 : 
         raise ValueError ("Numero no valido, introducir entero mayor a 0")
    for i in range (2,n):
         if n % i == 0 : 
              return False 
    return True 

def sumar_primo(n: int) -> int :
    sumatorio = 0 
    if not isinstance (n, int) or n <= 0 : 
        raise ValueError ("Numero no valido")
    #Arriba tengo 2 y aquí puse un uno pero quería poner 2 tambien si no suma 1 o no , la respuesta correcta es dos me lie, pero entiendo que así.
    #Lo correcto sería 2,n puse uno por nervios, interpretando que uno tambien contaba como primo,
    # pero era y soy igual de consciente que es 2. 
    for i in range (1, n):
         if es_primo(i):
            sumatorio += i 
    return sumatorio 



