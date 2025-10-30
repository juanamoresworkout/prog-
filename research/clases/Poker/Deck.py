from PokerCard import *
from PokerCardConstructor import *
import random


class Deck:
    def __init__(self): 
        self._baraja: list[PokerCardConstructor] = []

    def _init_deck(self): 
        self._baraja = []

        for tipos in (Type.Corazones,Type.Diamantes,Type.Picas,Type.Trebol) : 
            for i in range (1,14) :
                carta = PokerCardConstructor(i,tipos)
                self._baraja.append(carta)

    def swap(self, i: int, j : int): 
        if 0 <= i < len(self._baraja) and  0 <= j < len(self._baraja):
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
    def string_desk(self) -> str: 
        for i in self._baraja:
            print(i.return_card())
    
    def get_index_card(self,index : int) -> PokerCardConstructor | None :
        if not isinstance (index, int) :
            return None
        if index < 0 or index >= len(self._baraja):
            return None
        return self._baraja[index]
    
    def pick_top_card(self) -> PokerCardConstructor | None:
        if len(self._baraja) == 0:
            return None
        return self._baraja.pop(0)
    
    def valid_deck(self): 
        if self._baraja is None  or  len(self._baraja) == 0:
            return False 
        for i in self._baraja : 
            if not isinstance(i,PokerCardConstructor):
                return False
            if not i.verifier():
                return False 
        return True 
    def equals(self,card: PokerCardConstructor,card1: PokerCardConstructor) -> bool :
        if not isinstance(card,PokerCardConstructor) or not isinstance(card1,PokerCardConstructor):
            return False 
        if card.get_number() == card1.get_number() and card.get_type() == card1.get_type():
            return True
        return False 

    def contains(self,card : PokerCardConstructor) -> bool :   
        if not isinstance(card,PokerCardConstructor) :
            return False 
        for c in self._baraja:
            if self.equals(c,card):
                return True 
        return False    

    def add_card(self, card: PokerCardConstructor) -> bool:
    
        if not isinstance(card, PokerCardConstructor):
            return False
        if not card.verifier():
            return False

        if self.contains(card):
            return False 
        self._baraja.append(card)
        return True
    def robar_cartas_aleatorias(self,num: int ) :
        for _ in range(num):
          self._baraja.pop(num)
    
    def clone_deck(self) -> 'Deck':
        deck2 = Deck()
        for card in self._baraja:
            deck2.add_card(card.clone_card()) 
        return deck2



    def show_deck(self) -> list[str]:
        return [carta.return_card() for carta in self._baraja]
