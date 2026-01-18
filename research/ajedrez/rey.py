from __future__ import annotations

from enums import TipoPieza
from figura import *



# ----------------------------
# Clase Rey(Hereda de Figura):
# ----------------------------
class Rey(Figura):
    def get_tipo_pieza(self) -> TipoPieza:
        return TipoPieza.REY

    def movimiento_posible(self, tablero: "Tablero") -> List[Tuple[int, int]]:
            result: list[Tuple] = []
            
            for posicion in [(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)]:
                    x = self._x + posicion[0]
                    y = self._y +  posicion[1]
                    
                    if self.fuera_de_rango(x,y): 
                        continue 

                    if tablero.get_figura_en(x,y) != None:
                        if tablero.get_figura_en(x,y).get_color() == self.get_color():
                            continue 
                        else:
                            result.append((x,y))
                            break
                    else:
                        result.append((x,y))
            return result 