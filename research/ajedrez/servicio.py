from __future__ import annotations

from abc import ABC, abstractmethod
import secrets
from enum import Enum
from typing import Callable, List, Optional, Tuple

from figura import Figura
from partida import Partida
from enums import *

# ----------------------------
# Clase Servicio_partida(ABC):
# ----------------------------
class ServicioPartida(ABC):
    """
    Interfaz.
    Tiene una lista de partidas (protected).
    """
    @abstractmethod
    def __init__(self) -> None:
        pass 

    @abstractmethod
    def crear_partida(self, jugador_blancas: str, jugador_negras: str) -> Partida:
        pass

    @abstractmethod
    def borrar_partida(self, id_partida: str) -> None:
        pass

    @abstractmethod
    def mostrar_partida(self, id_partida: str) -> str:
        """
        Puede devolver un string con todas las piezas vivas / estado.
        """
        pass

    @abstractmethod
    def mover_figura(self, id_partida: str, jugador: str, x_origen: int, y_origen: int, x_dest: int, y_dest: int) -> None:
        pass

    @abstractmethod
    def hacer_enroque(self, id_partida: str, jugador: str, tipo_enroque: str) -> None:
        pass

    @abstractmethod
    def cambiar_estado_partida(self, id_partida: str, nuevo_estado: EstadoPartida) -> None:
        pass

    @abstractmethod
    def filter(self, criterio: Callable[[Partida], bool]) -> List[Partida]:
        """
        Recibe un filtro (lambda) que recibe una Partida y devuelve bool.
        Devuelve la lista de partidas que cumplan el criterio.
        """
        pass

# -----------------------------------------
# Clase Servicio_partida_impl (implementa):
# -----------------------------------------
class ServicioPartidaImpl(ServicioPartida):
    def __init__(self) -> None:
        self.__lista_partida: list[Partida]= []
        
    def borrar_partida(self, id_partida: str) -> None:
        for i in range(len(self.__lista_partida)):
            if self.__lista_partida[i].get_id() == id_partida:
                self.__lista_partida.pop(i)

    def mostrar_partida(self, id_partida: str) -> list[Figura]:
        for partida in self.__lista_partida:
            if partida.get_id() == id_partida:
                return partida.devolver_partida()
            
    def buscar_por_id(self,id: str) -> Partida:
        for partida in self.__lista_partida:
            if partida.get_id() == id:
                return partida 
        raise ValueError("Partida no enccontrada")
            
    def mover_figura(self, id_partida: str, jugador: str, x_origen: int, y_origen: int, x_dest: int, y_dest: int) -> None:
            partida = self.buscar_por_id(id_partida)

            jugador_blancas = partida.get_jugador_blancas()
            jugador_negras = partida.get_jugador_negras()

            if jugador_blancas == jugador :
                color_jugador = Color.BLANCA
            if jugador_negras == jugador:
                color_jugador = Color.NEGRA
          
            if color_jugador != partida.get_turno():
                raise ValueError("Error de turno")
            
            pieza = partida.get_tablero().get_figura_en(x_origen, y_origen)
            if pieza == None:
                 raise ValueError("Error, noy hay pieza en la posicion.")
                       
            if pieza.get_color() != color_jugador:
                raise ValueError("Error de color")
            
            if partida.mover_partida(pieza,x_dest,y_dest) == 1 :
                self.borrar_partida(id_partida)

            partida._movimientos.append(f"El jugador: {jugador} ha movido {pieza} desde {x_origen,y_origen} a {x_dest,y_dest}, movimiento de la pieza numero: {pieza.get_movimientos()}")

            partida.gestion_turnos()

    def hacer_enroque(self, id_partida: int, jugador: str, tipo_enroque: int) -> None:
        partida = self.buscar_por_id(id_partida)
        jugador_blancas = partida.get_jugador_blancas()
        jugador_negras = partida.get_jugador_negras()

        if jugador_blancas == jugador :
            color_jugador = Color.BLANCA
        if jugador_negras == jugador:
            color_jugador = Color.NEGRA

        partida.enrocar(tipo_enroque,color_jugador)
        partida._movimientos.append(f"Se ha efectuado enroque del jugador:{jugador}, del tipo {tipo_enroque}")
        partida.gestion_turnos()

    def cambiar_estado_partida(self, id_partida: int, nuevo_estado: EstadoPartida) -> None:
        for partida in self.__lista_partida:
            if partida.get_id() == id_partida:
                if partida.get_estado() == nuevo_estado:
                    break 
                else: 
                    partida.cambiar_estado_partida()   

    def listar_id(self) ->list[str]:
        result: list[str] = [] 
        for partida in self.__lista_partida:
            result.append(partida.get_id())
        return result 

    def filter(self, criterio: Callable[[Partida], bool]) -> List[Partida]:
        result:list[Partida] = []
        for partida in self.__lista_partida:
            if criterio(partida):
                result.append(partida)
        return result


    def crear_partida(self, jugador_blancas: str, jugador_negras: str) -> Partida:
        id = secrets.token_hex(4)
        blancas = jugador_blancas 
        negras = jugador_negras

        if len(self.__lista_partida) != 0:
            while self.comprobar_token(id):
               id = secrets.token_hex(4) 
            if self.comprobar_max_partidas(blancas,negras):
                raise ValueError("Existen diez partidas en curso")
        
        partida = Partida(id,blancas,negras) 
        partida.iniciar_partida()
        self.__lista_partida.append(partida)

        return partida

    def comprobar_token(self, id: str) -> bool:
        for partida in self.__lista_partida:
            if partida.get_id() == id:
                return True
        return False 

    def comprobar_max_partidas(self,blancas: str, negras: str) -> bool:
        contador = 0  
        for partida in self.__lista_partida:
            jb = partida.get_jugador_blancas()
            jn = partida.get_jugador_negras()
            if (jb == blancas and jn == negras) or (jb == negras and jn == blancas) :
                contador += 1
                if contador == 10 :
                    return True 
        return False 