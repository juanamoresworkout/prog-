from __future__ import annotations

from Driver import Driver

class Humano(Driver):
    def __init__(self):
        super().__init__()
    
    
    def get_velocity(self) -> float:
        return 0.0

    