from queve import * 

cactus = Queve[int]()

cactus.enqueve(66)
cactus.enqueve(6)
cactus.enqueve(6)
cactus.enqueve(4)
cactus.enqueve(4)

#cactus.visit(lambda item: print(item))

filtered = cactus.filter(lambda nombre: nombre > 5 )

filtered.visit(lambda item: print(item))