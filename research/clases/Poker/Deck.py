from PokerCard import *
import random

class Deck:
    def __init__(self): 
        self._baraja: list[PokerCard] = []

    def _init_deck(self): 
        self._baraja = []

        for tipos in (Type.Corazones,Type.Diamantes,Type.Picas,Type.Trebol) : 
            for i in range (1,14) :
                carta = PokerCard()
                carta.set_number(i)
                carta.set_type(tipos)
                self._baraja.append(carta)

    def swap(self, i: int, j : int): 
        if 0 <= i <= len(self._baraja) and  0 <= j <= len(self._baraja):
            self._baraja[i],self._baraja[j] = self._baraja[j], self._baraja[i]
    
    def shuffle (self):
        for _ in range (100) : 

                i = random.randint(0,len(self._baraja) -1)
                j = random.randint(0,len(self._baraja) -1)
                if i == j:
                    continue 
                else:
                    self.swap(i,j)
    def count_baraja(self) :
        return len(self._baraja)
    
    def get_index_card(self,index : int) -> PokerCard | None :
        if not isinstance (index, int) :
            return None
        if index < 0 or index > len(self._baraja):
            return None
        return self._baraja[index]
    
    def pick_top_card(self, index: int = 0) -> PokerCard | None:
        if not isinstance(index, int):
            return None
        if len(self._baraja) == 0:
            return None
        if index < 0 or index >= len(self._baraja):
            return None
        return self._baraja.pop(index)
    def add_card(self, card: PokerCard) -> bool:
    
        if not isinstance(card, PokerCard):
            return False
        if not card.is_value():
            return False

        # Compruebo si la carta esta en la baraja con un bucle que compara la carta que metes con todas.
        for c in self._baraja:
            if c.get_number() == card.get_number() and c.get_type() == card.get_type():
                return False 

        self._baraja.append(card)
        return True
    
    def show_deck(self) -> list[str]:
        return [carta.return_card() for carta in self._baraja]