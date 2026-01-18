from __future__ import annotations

from figura import *


# ------------------------------
# Clase Alfil(Hereda de Figura):
# ------------------------------
class Alfil(Figura):
    def get_tipo_pieza(self) -> TipoPieza:
        pass

    def movimiento_posible(self, tablero: "Tablero") -> List[Tuple[int, int]]:
        return self.direccion_posible([(1,1),(1,-1),(-1,1),(-1,-1)],tablero)
