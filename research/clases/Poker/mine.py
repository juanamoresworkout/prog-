from PokerCard import *
from PokerCardConstructor import *
from Deck import * 
from Fecha import *


carta1 = PokerCard() 
carta1.set_number(15) 
carta1.set_type (Type.Corazones)

carta2 = PokerCardConstructor(2,1)
print(carta2)






"""
for carta in range (deck.count_baraja()) :
    c = deck.get_index_card(carta) 
    print(c.return_card())

deck = Deck()           
deck._init_deck()              
print(deck.count_baraja())



carta = deck.pick_top_card()

carta2 = deck.pick_top_card()

print(deck.string_desk())

clone = deck.clone()


print("Cartas restantes:", deck.count_baraja())
   
"""
Fecha1 = Fecha(2000,Meses.Enero,11)

print(Fecha1)




