from PokerCard import Type , Color
class PokerCardConstructor:
    def __init__(self, number: int, type_: int):
        # Validación del número
        if number == None or number <= 0 or number > 13:
            self._number = -1
        else:
            self._number = number
        # Validación del tipo (palo)
        if  type_ == None :
            self._type = Type.Desconocido
        else:
            self._type = type_
            

    def get_number(self) -> int:
        return self._number

    def get_type(self) -> int:
        return self._type

    def is_value(self) -> bool:
        return self.get_number() > 0 and self.get_type() >= 0

    def return_type(self) -> str:
        if self._type == Type.Trebol:
            return "Trebol"
        if self._type == Type.Picas:
            return "Picas"
        if self._type == Type.Diamantes:
            return "Diamantes"
        if self._type == Type.Corazones:
            return "Corazones"
        return "Desconocido"

    def return_card(self) -> str:
        return f"{self.get_number()} de {self.return_type()}"
    



    