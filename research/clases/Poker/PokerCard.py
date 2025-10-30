from enum import Enum

class Color(Enum):
    RED = 0 
    BLACK = 1
class Type(Enum):
    Trebol = 0
    Picas = 1 
    Diamantes = 2 
    Corazones = 3 
    Desconocido = 5
    


class PokerCard:

    def __init__(self):
        self._number = -1
        self._type = Type.Desconocido 
    
    def set_number(self,number: int) : 
        if number <= 0 : 
            return 
        if number > 13 : 
            return 
        self._number = number 

    def get_number(self) -> int : 
        return  self._number 
    
    def set_type(self, tipo: Type):
        if tipo is None:
            tipo = Type.Desconocido
        self._type = tipo


    def get_type(self) -> Type :
        return self._type

    def is_value(self) -> bool :
      return self.get_number() > 0 and self.get_type() is not Type.Desconocido 
    
    def get_color(self) -> Color | None:
            if self._type in (Type.Trebol, Type.Picas):
                return Color.BLACK
            if self._type in (Type.Diamantes, Type.Corazones):
                return Color.RED
            return None        

    def return_type(self) -> str:
            """Devuelve el nombre del tipo de carta (palo)."""
            if self._type == Type.Trebol:
                return "Trébol"
            if self._type == Type.Picas:
                return "Picas"
            if self._type == Type.Diamantes:
                return "Diamantes"
            if self._type == Type.Corazones:
                return "Corazones"
            return "Desconocido"

    def return_card(self) -> str:
      return  f"{self.get_number()} de {self.return_type()}"
        
    
    
        



      

    


