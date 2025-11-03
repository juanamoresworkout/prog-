def operacion (num1,num2,num3) -> int : 
    resultado = num1 * num2 + num3 

    return resultado
operatorio = operacion(4,2,1)
print(operatorio)

def mayor_que (num1,num2,num3) -> int : 
    if num1 > num2 and num1 > num3 : 
        return num1 
    if num2 > num3 :
        return num2
    return num3  
operatorio2 = mayor_que(2,3,4)
print(operatorio2) 

def lista_mayor (lista: list[int]) -> int : 
    num0 = lista [0]
    for i in lista : 
        if i > num0: 
         num0 = i 
    return num0 
def lista_menor (lista: list[int]) -> int : 
    num0 = lista[0]
    for i in lista :
         if i < num0 :
            num0 = i 
    return num0    
            
lista = [1,2,3,6,5]

mi_lista = lista_mayor(lista)
print(mi_lista)

def get_min_max(lista: list[int]) -> list[int]:
    lista_nueva = [] 
    lista_nueva.append(lista_menor(lista))
    lista_nueva.append(lista_mayor(lista))

    return lista_nueva 

mi_lista2 = get_min_max(lista)
print(mi_lista2)

def es_par (numero:int) -> bool :
    return numero % 2 == 0 
def count_pares(lista: list[int]) -> int : 
    num = 0 
    for i in lista : 
        if es_par(i):
            num += 1 
    return num 

print(count_pares(lista))

def sumar_rango_pares(n: int) -> int : 
    num = 0 
    for i in range (0,num) : 
        if es_par (i):
            num = num + i 
    return num

class Triangulo: 
    def __init__(self,altura: float, base: float):
       self._altura = altura 
       self._base = base 
    
    def area(self) -> float: 
        return self._altura * self._base / 2 
    
triangulo = Triangulo(120,20)
print(Triangulo.area(triangulo))


def index_lista (num: int , lista : list[int]) -> int : 
    for i in range (len(lista)) : 
        if lista[i] == num : 
            return i 
    return -1 

def lista_for_n(n: int) -> list[int]:
    lista_vacia = []
    for i in range (0, n + 1):
        lista_vacia.append(i)
    return lista_vacia

lista_multiple = lista_for_n(5)
print(lista_multiple)

def lista_pares(n: int ) -> list[int] : 
    lista_par = []
    for i in range (0,n) : 
        if es_par(i) : 
            lista_par.append(i)
    return lista_par

print(lista_pares(8))

def lista_descendente(n: int) -> list[int] :
    lista_des = []
    while n >= 0 :
        lista_des.append(n)
        n -= 1 
    return lista_des

print(lista_descendente(4))

def numero_primo (n: int) -> bool : 
    num = n - 1 
    while num >= 2 : 
        if n % num == 0 : 
            return False
        num -= 1  
    return True 

print(numero_primo(7))

def primer_primo( n: int , n2: int ) -> int : 
    for i in range(min(n,n2),max(n,n2)): 
       if numero_primo(i): 
           return i 

print(primer_primo(6,10))

def max_div(n:int , n2: int ) -> int : 
    numero = min (n,n2)
    while numero >= 1 : 
        if n % numero == 0 and n2 % numero == 0 : 
            return numero 
        numero -= 1 

def ordenar_lista (lista: list[int]) -> list[int] :
    i = 0 
    while i < len(lista) - 1  : 
        j = 0 
        while j < len(lista) - 1  :
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            j += 1 
        i += 1 
    return lista 
print(ordenar_lista(lista))


def contar_string (nombre: str , lista:list[str]):
    contador = 0 
    for i in lista : 
        if i.lower() in nombre.lower():
            contador += 1 
    return contador 

listan = ["es el pekeño","espekeño","Pekeño","pekeno"]
print(contar_string("pekeño",listan))

def ordenar_lista1 (lista: list[int]) -> list[int]:
    i = 0 

    while i < len(lista) - 1 : 
        j = 0 
        while j < len(lista) - 1 : 
            if lista[j] > lista[j + 1] : 
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            j += 1 
        i += 1 
    return lista 

lista_sucia =  [1567,2,4] 
print(ordenar_lista1(lista_sucia))

def lista_collatz (n: int) -> list[int]: 
    lista = [n]
    while n > 1 : 
        if n % 2 == 0 : 
            n = n // 2 
            lista.append(n)
        else:
            n = 3 * n + 1 
            lista.append(n)
    return lista 

print(lista_collatz(9))

def fibo (numero: int ) -> list[int] : 
    lista = [0,1]
    a = 0 
    b = 1 
    i = 2 

    if numero == 0 :
        return [0] 
    if numero == 1 :
        return [0,1]
    while i < numero : 
        c = a + b 
        a = b 
        b = c 
        lista.append(b)
        i+= 1 
    return lista 
print(fibo(5))
 


