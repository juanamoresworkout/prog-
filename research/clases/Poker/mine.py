from PokerCard import *
from PokerCardConstructor import *

carta1 = PokerCard() 
carta1.set_number(15) 
carta1.set_type (Type.Corazones)

carta2 = PokerCardConstructor(2,1)

print(carta1.return_card())
print(carta2.return_card())


