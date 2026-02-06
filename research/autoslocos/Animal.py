from __future__ import annotations

from Driver import Driver
from random import *

class Animal(Driver):
    def __init__(self):
        super().__init__()
    
    
    def get_velocity(self) -> float:
        return uniform(-1.0, 3.0)