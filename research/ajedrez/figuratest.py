from __future__ import annotations

from dataclasses import dataclass 
from enums import *

@dataclass 
class FiguraTest: 
    tipo: TipoPieza
    color: Color 
    x: int 
    y: int 
