#NickName: Loves
class Rectangulo: 
    _ancho : float 
    _alto: float

    def __init__(self):
        self._ancho = 1
        self._alto = 1 
    
    def set_ancho(self,ancho: float) :
        if not isinstance(ancho,float): 
            raise ValueError ("Valor no valido")
        if ancho is None: 
            raise ValueError ("No es valido nada")
        if ancho > 0 : 
            self._ancho = ancho 
    
    def get_ancho(self) -> float:
        return self._ancho
    
    def set_alto(self, alto: float) : 
        if not isinstance(alto,float): 
            raise ValueError ("Valor no valido")
        if alto is None: 
            raise ValueError ("No es valido nada")
        if alto > 0 :   
            self._alto = alto 

    def get_alto(self) -> float: 
        return self._alto 
    
    def calcular_area(self) -> float :
        area = (self._alto * self._ancho)
        return area 
    
    def calcular_perimetro(self) -> float:
        #Aquí tuve que quitar unas cosas pero realmente lo que se quedaba al final es esto. Lo demas es tipex.
        perimetro = (self._alto * 2) + (self._ancho * 2) 
        return perimetro 


    def es_cuadrado(self) -> bool : 
        return self._alto == self._ancho 

    #No me cabia el float en la hoja pero no devuelve nada, se ve claramente.
    def redimensionar_a(self,new_ancho: float, new_alto: float) :
        if not isinstance(new_ancho,float) or not isinstance(new_alto,float) :
            raise ValueError ("Tip no valido")
        #Se ahora que el tipo ya valida None, puse los dos por forzar el conocimiento de los filtros
        #estan puestos en lineas separadas para que se vieran pero con un or, estaría mejor, 
        # lo mismo para el alto lo añado con un or que se sobre entiende que es así, en la línea de lo mismo.

        if new_ancho is None or new_alto is None : 
            raise ValueError("Escribir un numero real.") 
        if new_ancho > 0 and new_alto > 0: 
            self._ancho = new_ancho
            self._alto = new_alto
        
    def escalar_por(self,num: float):
        if not isinstance (num,float) :
            raise ValueError("Tipo no valido")
        if num is None: 
            raise ValueError("No valido vacio")
        if num > 0 :
            self._ancho = self._ancho * num 
            self._alto = self._alto * num 

    def comparar_area(self, other : "Rectangulo") -> int : 
        if not isinstance(other,Rectangulo):
            raise ValueError("Introduce un rectangulo.")
        if self.calcular_area() == other.calcular_area():
            return 0 
        if self.calcular_area() > other.calcular_area():
            return 1 
        if self.calcular_area() < other.calcular_area():
            return -1 
    
    def obtener_aspecto(self) -> float : 
        return self._ancho / self._alto
    
    def to_string (self) -> str :
        return f"Rectangulo de ancho {self._ancho} y alto {self._alto}"