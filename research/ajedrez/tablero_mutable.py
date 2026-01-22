from __future__ import annotations

from tablero import Tablero
from figura import Figura 
from utils import * 


# -------------------------------
# Clase Tablero_mutable(Tablero):
# -------------------------------
class TableroMutable(Tablero):
    """
    Hereda de Tablero.
    Permite modificar: mover, setear, sustituir y generar_figuras.
    """
    #Seria necesario, poner si la tubla (x_dest, y_dest) esta dentro de posibles posiciones de esa figura a modo de comprobacion?

    def mover_figura(self, figura_origen: Figura, x_dest: int, y_dest: int) -> None:
        if (x_dest,y_dest) in figura_origen.movimiento_posible(self):
            if self.get_figura_en(x_dest,y_dest) != None:
                self.sustituir_figura(figura_origen,x_dest,y_dest)
                figura_origen.incrementar_movimiento()
         
            else:
                figura_origen.set_x(x_dest)
                figura_origen.set_y(y_dest)
                figura_origen.incrementar_movimiento()

    def set_figura_en(self, figura: Figura, x: int, y: int) -> None:
        if self.get_figura_en(x,y)  == None :
            figura.set_x(x)
            figura.set_y(y)
            self._figuras.append(figura)

    def promocionar(self, figura: Figura):

        if figura.get_tipo_pieza() != TipoPieza.PEON:
            raise ValueError("Promocion solo valida para peones")
        
        x = figura.get_x()
        y = figura.get_y()
        
        if figura.get_color() == Color.BLANCA and figura.get_y() == 7 :
                self.sustituir_figura(Reina(Color.BLANCA,x,y), x, y)
        else:
            if figura.get_color() and figura.get_y() == 0 :
                self.sustituir_figura(Reina(Color.NEGRA,x,y), x, y)


    def sustituir_figura(self, figura: Figura, x: int, y: int) -> None:
        for i in range(len(self._figuras)):
            if self._figuras[i].get_position() == (x, y):
                eliminada : Figura = self._figuras.pop(i)
                figura.set_x(x)
                figura.set_y(y)
                return eliminada
    
    def generar_figuras(self) -> None:
        result: list[Figura] = []

        Generar.generar_peones(result)
        Generar.generar_torres(result)
        Generar.generar_caballos(result)
        Generar.generar_alfil(result)
        Generar.generar_rey(result)
        Generar.generar_reina(result)
        
        if len(result) == 32:
             self._figuras = result 
        
        

    
         
