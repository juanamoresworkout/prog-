# Sacar tabla de multiplicacion por pantalla 

def devolver_tabla(n: int ) -> int : 
    for num in range(1,11) :
        numero = n * num 
        devolver = print(f"{n} x {num} = {numero}" )
    return devolver

def devolver_productorio(n: int) -> int :
    multiplicacion = 1
    if n <= 0:
        return 0 
    for i in range(1, n + 1) :
        multiplicacion *= i 
    return multiplicacion

print(devolver_productorio(5))

