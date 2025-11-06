from __future__ import annotations
from enum import Enum 


class energy (Enum) : 
    gasolina = 1 
    diesel = 2 
    hibrido = 3 
    electrico = 4 

class Coche: 
    _matricula : str 
    _marca : str 
    _modelo : str 
    _ano_produccion : int 
    _combustible : energy

    def __init__(self,matricula: str ,marca: str ,modelo: str ,ano_produccion: int ,combustible : energy):
        
        if len(matricula) > 8 : 
            raise ValueError("La matrícula no puede tener más de 8 caracteres.")   
        if Coche.validador_str(matricula) :
            self._matricula = matricula 

        if Coche.validador_str(marca) :  
            self._marca = marca 

        if Coche.validador_str(modelo):
            self._modelo = modelo 
 
        if ano_produccion is  None or not isinstance(ano_produccion,int): 
            raise ValueError("No es una año valido, maximo cuatro caracteres")
        if ano_produccion >= 1930 and ano_produccion < 2026 :
            self._ano_produccion = ano_produccion

        if combustible is not None or isinstance(combustible,energy):
         self._combustible = combustible 
        
    def get_matricula(self) -> str : 
        return self._matricula 
    
    def get_marca(self) -> str: 
        return self._marca 
    
    def get_modelo(self) -> str : 
        return self._modelo
    
    def get_ano_produccion(self) -> int : 
        return self._ano_produccion
    
    def get_combustible(self) -> energy: 
        return self._combustible
 
    #Utilidades 
    def validador_str (texto: str) -> bool : 
        return texto is not None or  isinstance(texto,str)
    
    def informacion_coche(self) -> str : 
        return f"Informacion del coche: Modelo: {self._modelo}, Marca:{self._marca}, Matricula: {self._matricula}, Año de prod: {self._ano_produccion}, Combustible: {self._combustible}"