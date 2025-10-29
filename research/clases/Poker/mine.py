from PokerCard import *
from PokerCardConstructor import *
from Deck import * 

carta1 = PokerCard() 
carta1.set_number(15) 
carta1.set_type (Type.Corazones)

carta2 = PokerCardConstructor(2,1)
print(carta2)

from Deck import Deck


deck = Deck()           
deck._init_deck()              
print(deck.count_baraja())



carta = deck.pick_top_card()

carta2 = deck.pick_top_card()

print(deck.string_desk())

clone = deck.clone()

"""
for carta in range (deck.count_baraja()) :
    c = deck.get_index_card(carta) 
    print(c.return_card())
   
"""

print("Cartas restantes:", deck.count_baraja())



