from PokerCard import *
from PokerCardConstructor import *
from Deck import * 

carta1 = PokerCard() 
carta1.set_number(15) 
carta1.set_type (Type.Corazones)

carta2 = PokerCardConstructor(2,1)


from Deck import Deck


deck = Deck()           
deck._init_deck()       
deck.shuffle()          

for carta in deck.show_deck():
    print(carta)

