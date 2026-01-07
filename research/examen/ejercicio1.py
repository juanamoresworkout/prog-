def encontrar_primo(num: int) ->bool:
    if num <= 1 :
        return False 
    for i in range (2,num) : 
        if num % i == 0 : 
            return False
    return True   

def sumar_primos(numero: int) -> int : 
 
    sumatorio: int = 0  
    for i in range (2, numero):
        if encontrar_primo(i):
            sumatorio += i 
    return sumatorio 


