# Sacar tabla de multiplicacion por pantalla 
def devolver_tabla(n: int ) -> int : 
    for num in range(1,11) :
        numero = n * num 
        devolver = print(f"{n} x {num} = {numero}" )
    return devolver

def devolver_productorio(n: int) -> int :
    i = 0 
    multiplicacion = 1
    for i in range(1, n + 1 ) :
        multiplicacion *= n 
    return multiplicacion
