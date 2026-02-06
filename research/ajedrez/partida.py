from __future__ import annotations
from typing import List 

from enums import Color, EstadoPartida
from tablero_mutable import TableroMutable
from tablero import Tablero
from figura import * 
from copy import deepcopy


# --------------
# Clase Partida:
# --------------
class Partida:
    """
    Maneja tableros.
    Atributos:
      - _id (protected)
      - _estado (protected) EstadoPartida
      - _turno (protected) Color
      - _jugador_blancas (protected)
      - _jugador_negras (protected)
      - _tablero (protected) TableroMutable
      - _movimientos (protected) lista de movimientos (puede ser str o tuplas)
    """

    def __init__(self, id_partida: str, jugador_blancas: str, jugador_negras: str) -> None:
        if len(id_partida) < 0 or len(id_partida) > 32:
            raise ValueError("Longitud del id erroneo.")
          
        self._id: str = id_partida
        self._estado: EstadoPartida = EstadoPartida.PAUSADA
        self._turno: Color = Color.BLANCA
        self._jugador_blancas: str = jugador_blancas
        self._jugador_negras: str = jugador_negras
        self._tablero: TableroMutable = TableroMutable()
        self._movimientos: List[str] = []
        self._contador_tablas = 0

    def get_id(self) -> str:
        return self._id 

    def get_estado(self) -> EstadoPartida:
        return self._estado

    def get_turno(self) -> Color:
        return self._turno

    def get_jugador_blancas(self) -> str:
        return self._jugador_blancas

    def get_jugador_negras(self) -> str:
        return self._jugador_negras

    def iniciar_partida(self) -> None:
        self._tablero.generar_figuras()
        
    def devolver_partida(self) -> list[Figura]:
        return self._tablero.get_piezas()

    def gestion_turnos(self) -> None:
        if self._turno == Color.BLANCA:
            self._turno = Color.NEGRA
        else:
            self._turno = Color.BLANCA  
    
    def buscar_rey(self, color: Color) -> tuple[int, int] | None:
        for pieza in self._tablero.get_piezas():
            if pieza.get_tipo_pieza() == TipoPieza.REY and pieza.get_color() == color:
                return (pieza.get_position())
        return None
    
    def buscar_rey_en_tablero(self, color: Color, tablero: TableroMutable) -> Figura | None:
        for pieza in tablero.get_piezas():
            if pieza.get_tipo_pieza() == TipoPieza.REY and pieza.get_color() == color:
                return pieza
        return None

    def jaque(self, color: Color) -> bool :
        pos_rey: tuple[int,int] = self.buscar_rey(color)
        if pos_rey is None:
            return False
        
        enemigo : Color = Color.NEGRA if color == Color.BLANCA else Color.BLANCA
        for pieza in self._tablero.get_piezas():
            if pieza.get_color() != enemigo:
                continue
            if pos_rey in pieza.movimiento_posible(self._tablero):
                return True

        return False

    def enrocar(self, color: Color, tipo_enrroque: int):
            lista_torres = self.listar_enroque(color)
            if len(lista_torres) == 0:
                return

            rey_x = 4
            rey_y = 0 if color == Color.BLANCA else 7

            torre_elegida = None

            for torre in lista_torres:
                if tipo_enrroque == 1 and torre.get_position()[0] < rey_x:
                    torre_elegida = torre
                elif tipo_enrroque == 2 and torre.get_position()[0] > rey_x:
                    torre_elegida = torre

            rey = self._tablero.get_figura_en(rey_x, rey_y)

            if tipo_enrroque == 1: 
                rey.set_x(2)
                torre_elegida.set_x(3)
                rey.incrementar_movimiento()
                torre_elegida.incrementar_movimiento()
            else: 
                rey.set_x(6)
                torre_elegida.set_x(5)
                rey.incrementar_movimiento()
                torre_elegida.incrementar_movimiento()

    def listar_enroque(self, color: Color) -> list[Figura]:
        rey = None
        posibles: list[Figura] = []
        result = []
        tablero: list[Figura] = self._tablero.get_lista_piezas()
        for pieza in tablero:

            if pieza.get_tipo_pieza() == TipoPieza.REY and pieza.get_color() == color and pieza.get_movimientos() == 0:
                rey = pieza

            if pieza.get_tipo_pieza() == TipoPieza.TORRE and pieza.get_color() == color and pieza.get_movimientos() == 0:
                posibles.append(pieza)

        if len(posibles) == 0 or rey == None:
            return []

        rey_y = rey.get_y()
        for torre in posibles:
            if (3, rey_y) in torre.direccion_posible([(1,0)], self._tablero) or (5, rey_y) in torre.direccion_posible([(-1,0)], self._tablero):
                result.append(torre) 

        return result

    def hay_tablas(self)-> bool:
        lista_blancas: list[Figura] = []
        lista_negras: list[Figura] = []
        
        for pieza in self._tablero.get_piezas():
            if pieza.get_color() == Color.BLANCA:
                lista_blancas.append(pieza)
            else:
                lista_negras.append(pieza)
        
        if len(lista_blancas) == 1 or len(lista_negras) == 1:
            self._contador_tablas += 1 
        
        if self._contador_tablas == 25:
            return True 
        return False 
       
    def cambiar_estado_partida(self) -> None:
        if self._estado == EstadoPartida.PAUSADA :
            self._estado = EstadoPartida.INICIADA
        else:
            self._estado = EstadoPartida.PAUSADA
    
    def get_tablero(self) -> Tablero:
        return self._tablero

    
    def mover_partida(self,figura: Figura, x_dest: int , y_dest: int)-> int :
        color_mueve = figura.get_color()

        if self.jaque(color_mueve):
            if figura.get_tipo_pieza() != TipoPieza.REY:
                raise ValueError("En jaque: solo puedes mover el rey")

        x_ori = figura.get_x()
        y_ori = figura.get_y()

        capturada = self._tablero.get_figura_en(x_dest, y_dest) 

        self._tablero.mover_figura(figura, x_dest, y_dest)
        if figura.get_tipo_pieza() == TipoPieza.PEON:
            self._tablero.promocionar(figura)
        
        if self.jaque(color_mueve):
            if self.puedo_mover_el_rey(color_mueve):

                figura.set_x(x_ori)
                figura.set_y(y_ori)
                figura.decrementar_movimiento()

                if capturada is not None:
                    self._tablero.set_figura_en(capturada,x_dest,y_dest)
                raise ValueError("Movimiento ilegal: te dejas en jaque")
            else:
                return 1
        if self.puedo_mover_el_rey(color_mueve) == False:
            if self.numero_de_piezas_por_color(color_mueve) == 1:
                    return 1        
    
    def devolver_lista_movimiento(self) -> list[str]:
        return self._movimientos

    def numero_de_piezas_por_color(self, color: Color) -> int:
        counter = 0
        pieza: Figura 
        for pieza in self._tablero.get_piezas():
            if pieza.get_color() == color:
                counter += 1
        return counter
   
    def puedo_mover_el_rey(self, color: Color) -> bool:
        tablero_base = deepcopy(self._tablero)
        rey = self.buscar_rey_en_tablero(color, tablero_base)

        if rey is None:
            return False

        for x, y in rey.movimiento_posible(tablero_base):
            tablero_test = deepcopy(tablero_base)
            rey_test = self.buscar_rey_en_tablero(color, tablero_test)

            tablero_test.mover_figura(rey_test, x, y)

            if not self.jaque_del_jaque_mate_y_rey_ahogado(color, tablero_test):
                return True

        return False

    def jaque_del_jaque_mate_y_rey_ahogado(self, color: Color, tablero: TableroMutable) -> bool:
        rey = self.buscar_rey_en_tablero(color, tablero)
        if rey is None:
            return False

        pos_rey = rey.get_position()
        enemigo = Color.NEGRA if color == Color.BLANCA else Color.BLANCA

        for pieza in tablero.get_piezas():
            if pieza.get_color() == enemigo:
                if pos_rey in pieza.movimiento_posible(tablero):
                    return True
        return False
    
        
