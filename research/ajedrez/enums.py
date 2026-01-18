from enum import Enum
# ----------------------------
# Enum de tipo de cada figura:
# ----------------------------
class TipoPieza(Enum):
    REY = 0
    REINA = 1
    TORRE = 2
    ALFIL = 3
    CABALLO = 4
    PEON = 5


# ----------------------------
# Enum de color:
# ----------------------------
class Color(Enum):
    BLANCA = 0
    NEGRA = 1


# ----------------------------
# Enum estado partida:
# ----------------------------
class EstadoPartida(Enum):
    INICIADA = 0
    PAUSADA = 1

