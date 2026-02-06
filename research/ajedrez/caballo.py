from __future__ import annotations

from figura import *

# --------------------------------
# Clase Caballo(Hereda de Figura):
# --------------------------------
class Caballo(Figura):
    def get_tipo_pieza(self) -> TipoPieza:
        return TipoPieza.CABALLO

    def movimiento_posible(self, tablero: "Tablero") -> List[Tuple[int, int]]:
        result: list[Tuple[int,int]] = []

        for posicion in [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]:
                    x = self._x + posicion[0]
                    y = self._y +  posicion[1]
                    
                    if self.fuera_de_rango(x,y): 
                        continue 

                    elif tablero.get_figura_en(x,y) != None:
                        if tablero.get_figura_en(x,y).get_color() == self.get_color():
                            continue
                        else:
                            result.append((x,y))
                            continue 
                    else:
                        result.append((x,y))
        return result 