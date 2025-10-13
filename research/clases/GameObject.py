class GameObject:
    name : str
    id: int 

def devolver_nombre (lista: list,obj:str ) -> GameObject :
    for valor in lista :
        if valor.name == obj:
            return valor 
    return None 
    