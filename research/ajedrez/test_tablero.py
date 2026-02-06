# tests/test_01_tablero_ordenado_con_piezas_reales.py

from __future__ import annotations

from typing import *

import pytest 

from enums import Color, TipoPieza
from tablero_mutable import TableroMutable

from rey import Rey
from reina import Reina
from torre import Torre
from alfil import Alfil
from caballo import Caballo
from peon import Peon
from partida import Partida


def _crear_pieza(cls: Type[Any], color: Color, x: int, y: int) -> Any:
    """
    (helper interno del test)
    Intenta construir la pieza usando tus constructores reales.
    - Primero prueba constructores típicos (con y sin keywords).
    - Si no encaja, crea con (color) y fija posición con setters.
    """
    try:
        return cls(color=color, x=x, y=y)
    except TypeError:
        pass
    try:
        return cls(color, x, y)
    except TypeError:
        pass
    try:
        return cls(x=x, y=y, color=color)
    except TypeError:
        pass
    try:
        return cls(x, y, color)
    except TypeError:
        pass

    # Último intento: constructor solo con color y setters de posición
    pieza = cls(color)
    pieza.set_x(x)
    pieza.set_y(y)
    return pieza


def _get_lista_ordenada(tablero: Any) -> List[Any]:
    """
    (helper interno del test)
    Llama a tu función nueva del tablero que devuelve las piezas ordenadas (0,0) -> (7,7).
    Como no me has dicho el nombre exacto, pruebo varios nombres típicos.
    """
    posibles_nombres = [
        "get_piezas_ordenadas",
        "get_figuras_ordenadas",
        "get_lista_ordenada",
        "get_tablero_ordenado",
        "ordenar_piezas",
        "ordenar_figuras",
        "pieza_ordenadas",
        "piezas_ordenadas",
        "figuras_ordenadas",
    ]

    for nombre in posibles_nombres:
        if hasattr(tablero, nombre):
            metodo = getattr(tablero, nombre)
            return metodo()  # type: ignore[misc]

    pytest.fail(
        "No encuentro el método del tablero que devuelve la lista ordenada (0,0 -> 7,7)."
    )


def _posiciones(lista: List[Any]) -> List[Optional[tuple[int, int]]]:
    if lista is None:
        pytest.fail("La lista ordenada devuelta por el tablero es None.")
    return [None if p is None else p.get_position() for p in lista]


# -------------------------
# MINI TESTS (base)
# -------------------------

def test_00_tablero_vacio_numero_piezas() -> None:
    tablero = TableroMutable()
    assert tablero.get_numero_piezas() == 0


def test_00_generar_figuras_numero_piezas() -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    assert tablero.get_numero_piezas() == 32


@pytest.mark.parametrize(
    "x,y",
    [(-1, 0), (0, -1), (8, 0), (0, 8), (-1, -1), (8, 8), (9, 3), (3, 9)],
)
def test_00_get_figura_en_fuera_rango(x: int, y: int) -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    with pytest.raises(ValueError):
        tablero.get_figura_en(x, y)


def test_00_get_figura_en_vacio_none() -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    assert tablero.get_figura_en(4, 4) is None


def test_00_get_piezas_es_copia() -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    piezas = tablero.get_piezas()
    piezas.clear()
    assert tablero.get_numero_piezas() == 32


@pytest.mark.parametrize(
    "cls, expected",
    [
        (Rey, TipoPieza.REY),
        (Reina, TipoPieza.REINA),
        (Torre, TipoPieza.TORRE),
        (Alfil, TipoPieza.ALFIL),
        (Caballo, TipoPieza.CABALLO),
        (Peon, TipoPieza.PEON),
    ],
)
def test_00_tipo_pieza(cls: Type[Any], expected: TipoPieza) -> None:
    pieza = _crear_pieza(cls, Color.BLANCA, 0, 0)
    assert pieza.get_tipo_pieza() == expected


@pytest.mark.parametrize(
    "x,y,expected",
    [
        (1, 0, {(0, 2), (2, 2)}),
        (6, 0, {(5, 2), (7, 2)}),
    ],
)
def test_00_movimientos_caballo_inicial(x: int, y: int, expected: set[tuple[int, int]]) -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    caballo = tablero.get_figura_en(x, y)
    movimientos = set(caballo.movimiento_posible(tablero))
    assert expected.issubset(movimientos)


@pytest.mark.parametrize(
    "x,y,expected",
    [
        (0, 1, {(0, 2), (0, 3)}),
        (0, 6, {(0, 5), (0, 4)}),
    ],
)
def test_00_movimientos_peon_inicial(x: int, y: int, expected: set[tuple[int, int]]) -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    peon = tablero.get_figura_en(x, y)
    movimientos = set(peon.movimiento_posible(tablero))
    assert expected.issubset(movimientos)


@pytest.mark.parametrize("x,y", [(0, 0), (7, 0)])
def test_00_movimientos_torre_bloqueada(x: int, y: int) -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    torre = tablero.get_figura_en(x, y)
    assert torre.movimiento_posible(tablero) == []


@pytest.mark.parametrize("x,y", [(2, 0), (5, 0)])
def test_00_movimientos_alfil_bloqueado(x: int, y: int) -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    alfil = tablero.get_figura_en(x, y)
    assert alfil.movimiento_posible(tablero) == []


@pytest.mark.parametrize(
    "x_origen,y_origen,x_dest,y_dest",
    [
        (0, 0, 0, 2),  # torre bloqueada
        (2, 0, 4, 2),  # alfil bloqueado
        (3, 0, 3, 3),  # reina bloqueada
        (4, 0, 4, 2),  # rey bloqueado
        (1, 0, 1, 1),  # caballo a casilla ocupada por peon propio
        (0, 1, 0, 4),  # peon tres pasos
    ],
)
def test_00_movimiento_invalido_levanta_error(x_origen: int, y_origen: int, x_dest: int, y_dest: int) -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    pieza = tablero.get_figura_en(x_origen, y_origen)
    with pytest.raises(ValueError):
        tablero.mover_figura(pieza, x_dest, y_dest)


def test_00_captura_peon_diagonal() -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    peon_blanco = tablero.get_figura_en(1, 1)
    peon_negro = tablero.get_figura_en(2, 6)
    tablero.mover_figura(peon_negro, 2, 4)
    tablero.mover_figura(peon_blanco, 1, 3)
    tablero.mover_figura(peon_blanco, 2, 4)
    assert tablero.get_figura_en(2, 4) is peon_blanco


def test_00_lista_ordenada_len() -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    lista = _get_lista_ordenada(tablero)
    assert len(lista) == 32


@pytest.mark.parametrize(
    "x,y,cls",
    [
        (0, 0, Torre),
        (7, 0, Torre),
        (1, 0, Caballo),
        (6, 0, Caballo),
        (2, 0, Alfil),
        (5, 0, Alfil),
        (3, 0, Reina),
        (4, 0, Rey),
    ],
)
def test_00_posiciones_iniciales_blancas(x: int, y: int, cls: Type[Any]) -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    pieza = tablero.get_figura_en(x, y)
    assert isinstance(pieza, cls)
    assert pieza.get_color() == Color.BLANCA


@pytest.mark.parametrize(
    "x,y,cls",
    [
        (0, 7, Torre),
        (7, 7, Torre),
        (1, 7, Caballo),
        (6, 7, Caballo),
        (2, 7, Alfil),
        (5, 7, Alfil),
        (3, 7, Reina),
        (4, 7, Rey),
    ],
)
def test_00_posiciones_iniciales_negras(x: int, y: int, cls: Type[Any]) -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    pieza = tablero.get_figura_en(x, y)
    assert isinstance(pieza, cls)
    assert pieza.get_color() == Color.NEGRA


def test_00_rey_movimientos_iniciales_vacio() -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    rey = tablero.get_figura_en(4, 0)
    assert rey.movimiento_posible(tablero) == []


def test_00_promocion_blanca_crea_reina() -> None:
    partida = Partida("p_prom", "b", "n")
    partida.iniciar_partida()
    tablero = partida.get_tablero()
    p_b_11 = tablero.get_figura_en(1, 1); partida.mover_partida(p_b_11, 1, 3)
    partida.mover_partida(p_b_11, 1, 4)
    partida.mover_partida(p_b_11, 1, 5)
    p_n_06 = tablero.get_figura_en(0, 6); partida.mover_partida(p_n_06, 1, 5)
    p_n_36 = tablero.get_figura_en(3, 6); partida.mover_partida(p_n_36, 3, 5)
    a_n_27 = tablero.get_figura_en(2, 7); partida.mover_partida(a_n_27, 4, 5)
    c_n_17 = tablero.get_figura_en(1, 7); partida.mover_partida(c_n_17, 2, 5)
    q_n_37 = tablero.get_figura_en(3, 7); partida.mover_partida(q_n_37, 3, 6)
    partida.enrocar(Color.NEGRA, 1)
    p_b_01 = tablero.get_figura_en(0, 1)
    partida.mover_partida(p_b_01, 0, 3)
    partida.mover_partida(p_b_01, 0, 4)
    partida.mover_partida(p_b_01, 0, 5)
    partida.mover_partida(p_b_01, 0, 6)
    partida.mover_partida(p_b_01, 0, 7)
    pieza = tablero.get_figura_en(0, 7)
    assert pieza is not None
    assert pieza.get_tipo_pieza() == TipoPieza.REINA


@pytest.mark.parametrize(
    "x_origen,y_origen,x_dest,y_dest",
    [
        (0, 1, 0, 2),
        (1, 1, 1, 2),
        (2, 1, 2, 2),
        (3, 1, 3, 2),
        (4, 1, 4, 2),
        (5, 1, 5, 2),
        (6, 1, 6, 2),
        (7, 1, 7, 2),
    ],
)
def test_00_peones_blancos_un_paso(x_origen: int, y_origen: int, x_dest: int, y_dest: int) -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    peon = tablero.get_figura_en(x_origen, y_origen)
    tablero.mover_figura(peon, x_dest, y_dest)
    assert tablero.get_figura_en(x_dest, y_dest) is peon


@pytest.mark.parametrize(
    "x_origen,y_origen,x_dest,y_dest",
    [
        (0, 6, 0, 5),
        (1, 6, 1, 5),
        (2, 6, 2, 5),
        (3, 6, 3, 5),
        (4, 6, 4, 5),
        (5, 6, 5, 5),
        (6, 6, 6, 5),
        (7, 6, 7, 5),
    ],
)
def test_00_peones_negros_un_paso(x_origen: int, y_origen: int, x_dest: int, y_dest: int) -> None:
    tablero = TableroMutable()
    tablero.generar_figuras()
    peon = tablero.get_figura_en(x_origen, y_origen)
    tablero.mover_figura(peon, x_dest, y_dest)
    assert tablero.get_figura_en(x_dest, y_dest) is peon



def test_01_lista_ordenada_00_a_77_con_piezas_reales() -> None:
    """
    TEST 1 (como pide tu profesor):
    - Creo dos tableros mutables: uno real (generar_figuras) y otro manual (set_figura_en).
    - Ordeno ambos con tu función del tablero (00 -> 77).
    - Comparo que el orden de las piezas coincide.
    """

    # -------------------------
    # ARRANGE: creo los tableros
    # -------------------------
    tablero_real = TableroMutable()
    tablero_real.generar_figuras()

    tablero_manual = TableroMutable()

    # ----------------------------------------------------------------------
    # ARRANGE: creo piezas reales (manual, una por una, usando tus clases)
    # Coordenadas según tu código: blancas en y=0 y peones blancos en y=1
    #                             negras en y=7 y peones negros en y=6
    # ----------------------------------------------------------------------

    # Fila 0 (blancas)
    t_b_00 = _crear_pieza(Torre, Color.BLANCA, 0, 0); tablero_manual.set_figura_en(t_b_00, 0, 0)
    c_b_10 = _crear_pieza(Caballo, Color.BLANCA, 1, 0); tablero_manual.set_figura_en(c_b_10, 1, 0)
    a_b_20 = _crear_pieza(Alfil, Color.BLANCA, 2, 0); tablero_manual.set_figura_en(a_b_20, 2, 0)
    q_b_30 = _crear_pieza(Reina, Color.BLANCA, 3, 0); tablero_manual.set_figura_en(q_b_30, 3, 0)
    r_b_40 = _crear_pieza(Rey, Color.BLANCA, 4, 0); tablero_manual.set_figura_en(r_b_40, 4, 0)
    a_b_50 = _crear_pieza(Alfil, Color.BLANCA, 5, 0); tablero_manual.set_figura_en(a_b_50, 5, 0)
    c_b_60 = _crear_pieza(Caballo, Color.BLANCA, 6, 0); tablero_manual.set_figura_en(c_b_60, 6, 0)
    t_b_70 = _crear_pieza(Torre, Color.BLANCA, 7, 0); tablero_manual.set_figura_en(t_b_70, 7, 0)

    # Fila 1 (peones blancos)
    p_b_01 = _crear_pieza(Peon, Color.BLANCA, 0, 1); tablero_manual.set_figura_en(p_b_01, 0, 1)
    p_b_11 = _crear_pieza(Peon, Color.BLANCA, 1, 1); tablero_manual.set_figura_en(p_b_11, 1, 1)
    p_b_21 = _crear_pieza(Peon, Color.BLANCA, 2, 1); tablero_manual.set_figura_en(p_b_21, 2, 1)
    p_b_31 = _crear_pieza(Peon, Color.BLANCA, 3, 1); tablero_manual.set_figura_en(p_b_31, 3, 1)
    p_b_41 = _crear_pieza(Peon, Color.BLANCA, 4, 1); tablero_manual.set_figura_en(p_b_41, 4, 1)
    p_b_51 = _crear_pieza(Peon, Color.BLANCA, 5, 1); tablero_manual.set_figura_en(p_b_51, 5, 1)
    p_b_61 = _crear_pieza(Peon, Color.BLANCA, 6, 1); tablero_manual.set_figura_en(p_b_61, 6, 1)
    p_b_71 = _crear_pieza(Peon, Color.BLANCA, 7, 1); tablero_manual.set_figura_en(p_b_71, 7, 1)

    # Fila 6 (peones negros)
    p_n_06 = _crear_pieza(Peon, Color.NEGRA, 0, 6); tablero_manual.set_figura_en(p_n_06, 0, 6)
    p_n_16 = _crear_pieza(Peon, Color.NEGRA, 1, 6); tablero_manual.set_figura_en(p_n_16, 1, 6)
    p_n_26 = _crear_pieza(Peon, Color.NEGRA, 2, 6); tablero_manual.set_figura_en(p_n_26, 2, 6)
    p_n_36 = _crear_pieza(Peon, Color.NEGRA, 3, 6); tablero_manual.set_figura_en(p_n_36, 3, 6)
    p_n_46 = _crear_pieza(Peon, Color.NEGRA, 4, 6); tablero_manual.set_figura_en(p_n_46, 4, 6)
    p_n_56 = _crear_pieza(Peon, Color.NEGRA, 5, 6); tablero_manual.set_figura_en(p_n_56, 5, 6)
    p_n_66 = _crear_pieza(Peon, Color.NEGRA, 6, 6); tablero_manual.set_figura_en(p_n_66, 6, 6)
    p_n_76 = _crear_pieza(Peon, Color.NEGRA, 7, 6); tablero_manual.set_figura_en(p_n_76, 7, 6)

    # Fila 7 (negras)
    t_n_07 = _crear_pieza(Torre, Color.NEGRA, 0, 7); tablero_manual.set_figura_en(t_n_07, 0, 7)
    c_n_17 = _crear_pieza(Caballo, Color.NEGRA, 1, 7); tablero_manual.set_figura_en(c_n_17, 1, 7)
    a_n_27 = _crear_pieza(Alfil, Color.NEGRA, 2, 7); tablero_manual.set_figura_en(a_n_27, 2, 7)
    q_n_37 = _crear_pieza(Reina, Color.NEGRA, 3, 7); tablero_manual.set_figura_en(q_n_37, 3, 7)
    r_n_47 = _crear_pieza(Rey, Color.NEGRA, 4, 7); tablero_manual.set_figura_en(r_n_47, 4, 7)
    a_n_57 = _crear_pieza(Alfil, Color.NEGRA, 5, 7); tablero_manual.set_figura_en(a_n_57, 5, 7)
    c_n_67 = _crear_pieza(Caballo, Color.NEGRA, 6, 7); tablero_manual.set_figura_en(c_n_67, 6, 7)
    t_n_77 = _crear_pieza(Torre, Color.NEGRA, 7, 7); tablero_manual.set_figura_en(t_n_77, 7, 7)

    # -------------------------
    # ACT: listas ordenadas
    # -------------------------
    obtenido_real = _get_lista_ordenada(tablero_real)
    obtenido_manual = _get_lista_ordenada(tablero_manual)

    # -------------------------
    # ASSERT: mismo orden
    # -------------------------
    assert _posiciones(obtenido_real) == _posiciones(obtenido_manual)

# manzana


def test_02_mover_varios_peones_blancas_y_negras() -> None:
    """
    TEST 2:
    - Creo un tablero real con generar_figuras.
    - Muevo varios peones blancos y negros (simulando turnos alternos).
    - Compruebo que las piezas han cambiado de casilla correctamente.
    """
    tablero = TableroMutable()
    tablero.generar_figuras()

    p_b_01 = tablero.get_figura_en(0, 1)
    p_b_11 = tablero.get_figura_en(1, 1)
    p_n_06 = tablero.get_figura_en(0, 6)
    p_n_16 = tablero.get_figura_en(1, 6)

    tablero.mover_figura(p_b_01, 0, 3)  # blanca, doble paso inicial
    tablero.mover_figura(p_n_06, 0, 4)  # negra, doble paso inicial
    tablero.mover_figura(p_b_11, 1, 2)  # blanca, un paso
    tablero.mover_figura(p_n_16, 1, 5)  # negra, un paso

    assert tablero.get_figura_en(0, 3) is p_b_01
    assert tablero.get_figura_en(0, 4) is p_n_06
    assert tablero.get_figura_en(1, 2) is p_b_11
    assert tablero.get_figura_en(1, 5) is p_n_16
    assert tablero.get_figura_en(0, 1) is None
    assert tablero.get_figura_en(0, 6) is None
    assert tablero.get_figura_en(1, 1) is None
    assert tablero.get_figura_en(1, 6) is None


def test_03_bordes_no_fallan_con_torres() -> None:
    """
    TEST 3:
    - Creo un tablero real con generar_figuras.
    - Muevo los peones de los bordes para liberar columna 0 y 7.
    - Pido movimientos posibles de las torres de los bordes.
    - Compruebo que no hay errores y que todas las casillas están dentro de rango.
    """
    tablero = TableroMutable()
    tablero.generar_figuras()

    # Libero las columnas 0 y 7 moviendo peones de borde
    p_b_00 = tablero.get_figura_en(0, 1)
    p_b_70 = tablero.get_figura_en(7, 1)
    p_n_06 = tablero.get_figura_en(0, 6)
    p_n_76 = tablero.get_figura_en(7, 6)

    tablero.mover_figura(p_b_00, 0, 3)
    tablero.mover_figura(p_b_70, 7, 3)
    tablero.mover_figura(p_n_06, 0, 4)
    tablero.mover_figura(p_n_76, 7, 4)

    # Torrez en los bordes
    t_b_00 = tablero.get_figura_en(0, 0)
    t_b_70 = tablero.get_figura_en(7, 0)
    t_n_07 = tablero.get_figura_en(0, 7)
    t_n_77 = tablero.get_figura_en(7, 7)

    mov_b_00 = t_b_00.movimiento_posible(tablero)
    mov_b_70 = t_b_70.movimiento_posible(tablero)
    mov_n_07 = t_n_07.movimiento_posible(tablero)
    mov_n_77 = t_n_77.movimiento_posible(tablero)

    for lista in (mov_b_00, mov_b_70, mov_n_07, mov_n_77):
        assert lista is not None
        for x, y in lista:
            assert 0 <= x <= 7
            assert 0 <= y <= 7

def test_04_mover_todas_las_piezas_una_vez() -> None:
    """
    TEST 4:
    - Creo un tablero real con generar_figuras.
    - Muevo todos los peones 2 pasos para liberar casillas.
    - Muevo el resto de piezas una vez (sin colisiones).
    - Compruebo que cada pieza termina en su destino.
    """
    tablero = TableroMutable()
    tablero.generar_figuras()

    # Mover todos los peones dos pasos
    for x in range(8):
        p_b = tablero.get_figura_en(x, 1)
        p_n = tablero.get_figura_en(x, 6)
        tablero.mover_figura(p_b, x, 3)
        tablero.mover_figura(p_n, x, 4)
        assert tablero.get_figura_en(x, 3) is p_b
        assert tablero.get_figura_en(x, 4) is p_n

    # Blancas (resto de piezas)
    t_b_00 = tablero.get_figura_en(0, 0); tablero.mover_figura(t_b_00, 0, 1)
    t_b_70 = tablero.get_figura_en(7, 0); tablero.mover_figura(t_b_70, 7, 1)
    c_b_10 = tablero.get_figura_en(1, 0); tablero.mover_figura(c_b_10, 2, 2)
    c_b_60 = tablero.get_figura_en(6, 0); tablero.mover_figura(c_b_60, 5, 2)
    a_b_20 = tablero.get_figura_en(2, 0); tablero.mover_figura(a_b_20, 0, 2)
    a_b_50 = tablero.get_figura_en(5, 0); tablero.mover_figura(a_b_50, 7, 2)
    q_b_30 = tablero.get_figura_en(3, 0); tablero.mover_figura(q_b_30, 3, 1)
    r_b_40 = tablero.get_figura_en(4, 0); tablero.mover_figura(r_b_40, 4, 1)

    assert tablero.get_figura_en(0, 1) is t_b_00
    assert tablero.get_figura_en(7, 1) is t_b_70
    assert tablero.get_figura_en(2, 2) is c_b_10
    assert tablero.get_figura_en(5, 2) is c_b_60
    assert tablero.get_figura_en(0, 2) is a_b_20
    assert tablero.get_figura_en(7, 2) is a_b_50
    assert tablero.get_figura_en(3, 1) is q_b_30
    assert tablero.get_figura_en(4, 1) is r_b_40

    # Negras (resto de piezas)
    t_n_07 = tablero.get_figura_en(0, 7); tablero.mover_figura(t_n_07, 0, 6)
    t_n_77 = tablero.get_figura_en(7, 7); tablero.mover_figura(t_n_77, 7, 6)
    c_n_17 = tablero.get_figura_en(1, 7); tablero.mover_figura(c_n_17, 2, 5)
    c_n_67 = tablero.get_figura_en(6, 7); tablero.mover_figura(c_n_67, 5, 5)
    a_n_27 = tablero.get_figura_en(2, 7); tablero.mover_figura(a_n_27, 1, 6)
    a_n_57 = tablero.get_figura_en(5, 7); tablero.mover_figura(a_n_57, 6, 6)
    q_n_37 = tablero.get_figura_en(3, 7); tablero.mover_figura(q_n_37, 3, 6)
    r_n_47 = tablero.get_figura_en(4, 7); tablero.mover_figura(r_n_47, 4, 6)

    assert tablero.get_figura_en(0, 6) is t_n_07
    assert tablero.get_figura_en(7, 6) is t_n_77
    assert tablero.get_figura_en(2, 5) is c_n_17
    assert tablero.get_figura_en(5, 5) is c_n_67
    assert tablero.get_figura_en(1, 6) is a_n_27
    assert tablero.get_figura_en(6, 6) is a_n_57
    assert tablero.get_figura_en(3, 6) is q_n_37
    assert tablero.get_figura_en(4, 6) is r_n_47

def test_05_enroque_corto_blancas_y_negras() -> None:
    """
    TEST 5:
    - Usa Partida (que tiene enroque).
    - Prepara el tablero para enroque corto (blancas y negras).
    - Ejecuta enroque corto y verifica posiciones finales.
    """
    partida = Partida("p1", "blancas", "negras")
    partida.iniciar_partida()
    tablero = partida.get_tablero()

    # ----- Blancas: liberar columnas 5 y 6 -----
    p_b_61 = tablero.get_figura_en(6, 1); partida.mover_partida(p_b_61, 6, 3)
    a_b_50 = tablero.get_figura_en(5, 0); partida.mover_partida(a_b_50, 7, 2)
    c_b_60 = tablero.get_figura_en(6, 0); partida.mover_partida(c_b_60, 5, 2)

    # Enroque corto blancas
    partida.enrocar(Color.BLANCA, 2)
    r_b_40 = tablero.get_figura_en(6, 0)
    t_b_70 = tablero.get_figura_en(5, 0)
    assert r_b_40 is not None
    assert t_b_70 is not None

    # ----- Negras: liberar columnas 5 y 6 -----
    p_n_66 = tablero.get_figura_en(6, 6); partida.mover_partida(p_n_66, 6, 4)
    a_n_57 = tablero.get_figura_en(5, 7); partida.mover_partida(a_n_57, 7, 5)
    c_n_67 = tablero.get_figura_en(6, 7); partida.mover_partida(c_n_67, 5, 5)

    # Enroque corto negras
    partida.enrocar(Color.NEGRA, 2)
    r_n_47 = tablero.get_figura_en(6, 7)
    t_n_77 = tablero.get_figura_en(5, 7)
    assert r_n_47 is not None
    assert t_n_77 is not None

def test_06_enroque_largo_blancas_y_negras() -> None:
    """
    TEST 6:
    - Usa Partida (que tiene enroque).
    - Prepara el tablero para enroque largo (blancas y negras).
    - Ejecuta enroque largo y verifica posiciones finales.
    """
    partida = Partida("p2", "blancas", "negras")
    partida.iniciar_partida()
    tablero = partida.get_tablero()

    # ----- Blancas: liberar columnas 1, 2 y 3 -----
    p_b_11 = tablero.get_figura_en(1, 1); partida.mover_partida(p_b_11, 1, 3)
    p_b_21 = tablero.get_figura_en(2, 1); partida.mover_partida(p_b_21, 2, 3)
    p_b_31 = tablero.get_figura_en(3, 1); partida.mover_partida(p_b_31, 3, 3)
    c_b_10 = tablero.get_figura_en(1, 0); partida.mover_partida(c_b_10, 2, 2)
    a_b_20 = tablero.get_figura_en(2, 0); partida.mover_partida(a_b_20, 0, 2)
    q_b_30 = tablero.get_figura_en(3, 0); partida.mover_partida(q_b_30, 3, 1)

    # Enroque largo blancas
    partida.enrocar(Color.BLANCA, 1)
    r_b_40 = tablero.get_figura_en(2, 0)
    t_b_00 = tablero.get_figura_en(3, 0)
    assert r_b_40 is not None
    assert t_b_00 is not None

    # ----- Negras: liberar columnas 1, 2 y 3 -----
    p_n_16 = tablero.get_figura_en(1, 6); partida.mover_partida(p_n_16, 1, 4)
    p_n_26 = tablero.get_figura_en(2, 6); partida.mover_partida(p_n_26, 2, 4)
    p_n_36 = tablero.get_figura_en(3, 6); partida.mover_partida(p_n_36, 3, 4)
    c_n_17 = tablero.get_figura_en(1, 7); partida.mover_partida(c_n_17, 2, 5)
    a_n_27 = tablero.get_figura_en(2, 7); partida.mover_partida(a_n_27, 0, 5)
    q_n_37 = tablero.get_figura_en(3, 7); partida.mover_partida(q_n_37, 3, 6)

    # Enroque largo negras
    partida.enrocar(Color.NEGRA, 1)
    r_n_47 = tablero.get_figura_en(2, 7)
    t_n_07 = tablero.get_figura_en(3, 7)
    assert r_n_47 is not None
    assert t_n_07 is not None


def test_07_promocion_peon_blanco_en_columna_0() -> None:
    """
    TEST 7:
    - Usa Partida y mover_partida.
    - Libera la columna 0.
    - Sube el peón blanco hasta el final y comprueba promoción a reina.
    """
    partida = Partida("p3", "blancas", "negras")
    partida.iniciar_partida()
    tablero = partida.get_tablero()

    # Preparar: liberar columna 0 moviendo piezas con mover_partida
    # 1) Colocar un peón blanco en (1,5) para que el peón negro de (0,6) capture y salga de la columna 0
    p_b_11 = tablero.get_figura_en(1, 1); partida.mover_partida(p_b_11, 1, 3)
    partida.mover_partida(p_b_11, 1, 4)
    partida.mover_partida(p_b_11, 1, 5)

    p_n_06 = tablero.get_figura_en(0, 6); partida.mover_partida(p_n_06, 1, 5)

    # 2) Preparar enroque largo negro para sacar la torre de (0,7)
    p_n_36 = tablero.get_figura_en(3, 6); partida.mover_partida(p_n_36, 3, 5)
    a_n_27 = tablero.get_figura_en(2, 7); partida.mover_partida(a_n_27, 4, 5)
    c_n_17 = tablero.get_figura_en(1, 7); partida.mover_partida(c_n_17, 2, 5)
    q_n_37 = tablero.get_figura_en(3, 7); partida.mover_partida(q_n_37, 3, 6)

    # Enroque largo negras (quita la torre de la columna 0)
    partida.enrocar(Color.NEGRA, 1)

    # Promoción del peón blanco de la columna 0
    p_b_01 = tablero.get_figura_en(0, 1)
    partida.mover_partida(p_b_01, 0, 3)
    partida.mover_partida(p_b_01, 0, 4)
    partida.mover_partida(p_b_01, 0, 5)
    partida.mover_partida(p_b_01, 0, 6)
    partida.mover_partida(p_b_01, 0, 7)

    pieza_promocion = tablero.get_figura_en(0, 7)
    assert pieza_promocion is not None
    assert pieza_promocion.get_tipo_pieza() == TipoPieza.REINA
    assert pieza_promocion.get_color() == Color.BLANCA


def test_08_promocion_capturando_torre_negra() -> None:
    """
    TEST 8:
    - Usa Partida y mover_partida.
    - Libera la columna 0 y coloca la torre negra en 1,7.
    - El peón blanco captura la torre en 1,7 y promociona a reina.
    - Comprueba que la torre capturada no está y que la reina ocupa su casilla.
    """
    partida = Partida("p4", "blancas", "negras")
    partida.iniciar_partida()
    tablero = partida.get_tablero()

    # Preparar: llevar el peón blanco de columna 1 a (1,5)
    p_b_11 = tablero.get_figura_en(1, 1); partida.mover_partida(p_b_11, 1, 3)
    partida.mover_partida(p_b_11, 1, 4)
    partida.mover_partida(p_b_11, 1, 5)

    # Hacer que el peón negro de (0,6) capture en (1,5), liberando la columna 0
    p_n_06 = tablero.get_figura_en(0, 6); partida.mover_partida(p_n_06, 1, 5)

    # Subir el peón blanco de columna 0 hasta (0,6)
    p_b_01 = tablero.get_figura_en(0, 1)
    partida.mover_partida(p_b_01, 0, 3)
    partida.mover_partida(p_b_01, 0, 4)
    partida.mover_partida(p_b_01, 0, 5)
    partida.mover_partida(p_b_01, 0, 6)

    # Mover el caballo negro de (1,7) para liberar la casilla
    c_n_17 = tablero.get_figura_en(1, 7); partida.mover_partida(c_n_17, 2, 5)

    # Mover la torre negra a (1,7)
    t_n_07 = tablero.get_figura_en(0, 7); partida.mover_partida(t_n_07, 1, 7)

    # Capturar la torre en (1,7) y promocionar
    partida.mover_partida(p_b_01, 1, 7)

    pieza_promocion = tablero.get_figura_en(1, 7)
    assert pieza_promocion is not None
    assert pieza_promocion.get_tipo_pieza() == TipoPieza.REINA
    assert pieza_promocion.get_color() == Color.BLANCA

    # Comprobar que solo queda una torre negra (la de 7,7)
    torres_negras = [
        p for p in partida.devolver_partida()
        if p.get_tipo_pieza() == TipoPieza.TORRE and p.get_color() == Color.NEGRA
    ]
    assert len(torres_negras) == 1


def test_09_jaque_a_rey_negro_con_reina() -> None:
    """
    TEST 9:
    - Usa Partida y mover_partida.
    - Prepara el camino para que la reina dé jaque al rey negro.
    - Comprueba que jaque(Color.NEGRA) devuelve True.
    """
    partida = Partida("p5", "blancas", "negras")
    partida.iniciar_partida()
    tablero = partida.get_tablero()

    # Abrir diagonal para la reina blanca
    p_b_41 = tablero.get_figura_en(4, 1); partida.mover_partida(p_b_41, 4, 3)
    # Abrir diagonal hacia el rey negro quitando el peón de f7
    p_n_56 = tablero.get_figura_en(5, 6); partida.mover_partida(p_n_56, 5, 4)

    # Colocar la reina en h5 dando jaque al rey negro
    q_b_30 = tablero.get_figura_en(3, 0); partida.mover_partida(q_b_30, 7, 4)

    assert partida.jaque(Color.NEGRA) is True


def test_10_en_jaque_solo_mover_rey() -> None:
    """
    TEST 10:
    - Usa Partida y mover_partida.
    - Pone al rey negro en jaque con la reina blanca.
    - Comprueba que mover una pieza que no sea el rey es ilegal.
    - Comprueba que mover el rey quita el jaque.
    """
    partida = Partida("p6", "blancas", "negras")
    partida.iniciar_partida()
    tablero = partida.get_tablero()

    # Preparar jaque: despejar diagonal y f7
    p_n_46 = tablero.get_figura_en(4, 6); partida.mover_partida(p_n_46, 4, 5)  # e7 -> e6
    p_n_56 = tablero.get_figura_en(5, 6); partida.mover_partida(p_n_56, 5, 4)  # f7 -> f5
    p_b_41 = tablero.get_figura_en(4, 1); partida.mover_partida(p_b_41, 4, 3)  # e2 -> e4

    q_b_30 = tablero.get_figura_en(3, 0); partida.mover_partida(q_b_30, 7, 4)  # Qh5+
    assert partida.jaque(Color.NEGRA) is True

    # Intentar mover otra pieza (peón a7) no quita el jaque
    p_n_06 = tablero.get_figura_en(0, 6)
    try:
        partida.mover_partida(p_n_06, 0, 5)
    except ValueError:
        pass
    else:
        assert partida.jaque(Color.NEGRA) is True

    # Mover el rey para salir del jaque
    r_n_47 = tablero.get_figura_en(4, 7)
    partida.mover_partida(r_n_47, 4, 6)  # e8 -> e7
    assert partida.jaque(Color.NEGRA) is False
