from __future__ import annotations
from coche import Coche, energy 


class Parking : 
    _capacidad : int 
    _coches: list[Coche]

    def __init__(self,capacidad: int):
        if capacidad is not None and isinstance(capacidad, int) : 
            self._capacidad = capacidad 
        self._coches : list[Coche]= []

    def get_listado(self) -> list[str]: 
        informacion = []    
        for coño in self._coches :         
            informacion.append(coño.informacion_coche() )
        return informacion 
    
    def add_coche(self, coche : Coche) : 
        if not isinstance(coche,Coche): 
            raise ValueError("Intentando añadir un vehiculo que no pertenece a la clase Coche")
        if len(self._coches) < self._capacidad : 
            self._coches.append(coche)

    def quitar_coche(self, indice : int )  : 
        if len(self._coches) == 0 :
           return  
        self._coches.pop(indice)
    
    def buscar_posicion_por_matricula (self ,matricula : str ) -> int : 
        matri = matricula.lower()
        for i in range (len(self._coches)) : 
            if self._coches[i]._matricula.lower() == matri : 
                return i 
        return -1   
    
    def buscar_coche_en_posicion(self,posicion: int) -> Coche : 
        for i in range (len(self._coches)): 
            if i == posicion:
                return self._coches[i]
        return "No hay coche en esa posicion"
    
    def contar_coches_combustible(self,energia: energy) -> int : 
        if len(self._coches) == 0 :
            raise ValueError("Lista vacia") 
        contador = 0 
        for i in range(len(self._coches)):
            if self._coches[i]._combustible == energia :
                contador += 1
        return contador 
    
    def coches_año_produccion (self, year: int) -> int : 
        contador = 0 
        if len(year) > 4 or len(year) < 4: 
            raise ValueError("El año debe contener 4 digitos")
        if not isinstance(year,int):
            raise ValueError("Error de tipo, introduce un int valido.")
        for i in range(len(self._coches)): 
            if self._coches[i]._ano_produccion == year : 
                contador += 1 
        return contador 
                

        

Parking_J = Parking(2)
c3 = Coche("1234 ABC","Torrente","Gordo",1970,energy.diesel)
Parking_J.add_coche(c3)
print(Parking_J.get_listado())

print(Parking_J.contar_coches_combustible(energy.diesel))