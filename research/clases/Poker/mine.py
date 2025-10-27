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
deck.shuffle()         
print(deck.count_baraja())

for i in range(deck.count_baraja()):
    c = deck.get_index_card(i)
    print(c.return_card())

# Saco la carta de arriba
carta = deck.pick_top_card()
print("Carta superior:", carta.return_card())

# Saco una carta concreta ejemplo la numero 10
cartafuera = deck.pick_top_card(10)
print("Carta 10:", cartafuera.return_card())

print("Cartas restantes:", deck.count_baraja())

