from __future__ import annotations

from enums import TipoPieza
from figura import *


# ------------------------------
# Clase Reina(Hereda de Figura):
# ------------------------------
class Reina(Figura):
    def get_tipo_pieza(self) -> TipoPieza:
        return TipoPieza.REINA

    def movimiento_posible(self, tablero: "Tablero") -> List[Tuple[int, int]]:
        return self.direccion_posible([(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)],tablero)
    
