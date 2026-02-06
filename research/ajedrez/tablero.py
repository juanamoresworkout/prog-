from __future__ import annotations

from figura import Figura
from typing import Optional, List
from copy import deepcopy

# --------------
# Clase Tablero:
# --------------
class Tablero:
    """
    Readonly: solo métodos para leer.
    Contiene lista de Figura (protected).
    """
    
    def __init__(self) -> None:
        self._figuras: List[Figura] = []
    
    def get_numero_piezas(self) -> int:
        return len(self._figuras)

    def get_figura_en(self, x: int, y: int) -> Optional[Figura]:
        if x < 0 or x > 7:
            raise ValueError("Error de casilla")
        
        if y < 0 or y > 7 :
            raise ValueError("Error de de casilla")
        
        for figura in self._figuras:
            if figura.get_position() == (x,y):
                return figura 
        return None 

    def get_piezas(self) -> List[Figura]:
        return deepcopy(self._figuras)
    
    def pieza_ordenadas(self) -> List[Figura]:
        result: list[Figura] = []
        for i in range(0,8):
            for j in range(0,8):
                if self.get_figura_en(i,j) is not None:    
                      result.append(self.get_figura_en(i,j))
        return result

    
   

    
















