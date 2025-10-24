from PokerCard import *
import random

class Deck:

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
            self.swap(i,j)

    def show_deck(self) -> list[str]:
        return [carta.return_card() for carta in self._baraja]