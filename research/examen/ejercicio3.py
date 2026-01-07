from __future__ import annotations
class Rectangulo :
    ancho: float 
    alto: float 

    def __init__(self,ancho, alto):
        if ancho <= 0 :
            return 
        self.__ancho = ancho 

        if alto <= 0 : 
            return 
        self.__alto = alto 
    
    def  get_ancho(self):
        return self.__ancho 
    
    def get__alto(self):
        return self.__alto
    
    def calcular_area(self) -> float:
        return self.__alto * self.__ancho 
    
    def calcular_perimetro(self) -> float:
        resultado = (self.__ancho * 2) + (self.__alto * 2) 
        return resultado
    
    def es_cuadrado(self) -> bool: 
        return self.__ancho == self.__alto
    
    def redimensionar_a(self,a: float, an: float) :
        if a <= 0 or an <= 0 :
            return 
        self.__alto = a 
        self.__ancho = an 
    
    def escalar_por(self,n:float):
        if n <= 0 :
            return 
        self.__alto *= n 
        self.__ancho *= n 

    def comparar_area(self, o: Rectangulo):
        if o is None :
            return 
        if self.calcular_area() < o.calcular_area(): 
            return - 1 
        if self.calcular_area() > o.calcular_area():
            return 1 
        return 0 
    def calcular_aspecto(self): 
        return self.__ancho / self.__alto 
    
    def to_string(self):
        return f"Rectangulo de {self.__alto} x {self.__ancho}"
    