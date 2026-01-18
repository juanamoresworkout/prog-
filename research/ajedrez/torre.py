from __future__ import annotations

from figura import * 

# ------------------------------
# Clase Torre(Hereda de Figura):
# ------------------------------
class Torre(Figura):
    def get_tipo_pieza(self) -> TipoPieza:
        return TipoPieza.TORRE

    def movimiento_posible(self, tablero: "Tablero") -> List[Tuple[int, int]]:
        return self.direccion_posible([(0,1),(0,-1),(1,0),(-1,0)],tablero)