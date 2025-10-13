from GameObject import *
from typing import List

#obj1: GameObject = GameObject()
#obj2: GameObject = obj1

#obj1.id = 10
#obj2.id = 1 
#obj2.id = 0


lista: List[GameObject] = []

obj = GameObject()
obj.id = 1 
obj.name = "Ana"
lista.append(obj) 

o = devolver_nombre(lista,"Ana")
print(o)



