class Alumno: 
    id: int 
    nombre: str 
    nota : float 
    
    def __init__(self, id: int, nombre:str, nota: float):
        if id > 0 :
            return
        self.__id = id  

        self.__nombre = nombre

        if nota < 0 or nota > 10 :
            return
        self.__nota = nota

    def set_nombre(self, nombre:str) :
        self.__nombre = nombre 
    
    def get_nombre(self):
        return self.__nombre 
    
    def get_id(self):
        return self.__id 
    
    def set_nota(self,nota):
        if nota < 0 or nota > 10 : 
            return  
        self.__nota = nota 
    
    def get_nota(self) ->float:
        return self.__nota 
    
    def to_string(self):
        return f"Alumno: {self.get_nombre()}  con id: {self.get_id()} tiene de nota: {self.get_nota()}"

    def actualizar_nota(self,nueva: int):
        if nueva < 0 or nueva > 10 :
            return 
        self.__nota = nueva 
    
    def es_aprobado(self) ->bool : 
        return self.get_nota() >= 5 
  

class Grupo : 
    grupo = list[Alumno]

    def __init__(self):
        self.__lista:list[Alumno] = []

    def agregar_alumno(self, a:Alumno):
        if a is None :
            return
        for alu in self.__lista:
            if alu.get_nota() == a.get_nota():
                return 
        self.__lista.append(a)

    def eliminar_alumno(self,id: int):
        if id < 0:
            return 
        for alu in self.__lista:
            if alu.get_id() == id :
                self.__lista.pop(alu)

    def buscar_por_id(self,id:int) -> Alumno:
        if id < 0:
            return 
        for alu in self.__lista :
            if alu.get_id() == id :
                return alu 
    
    def obtener_tamano(self) -> int :
        return len(self.__lista)
    
    def obtener_promedio(self) -> float :
        if len(self.__lista) ==  0 :
            return 0 
        cont = 0 
        for alu in self.__lista:
            cont += alu.get_nota()
        return cont / len(self.__lista)
    
    def obtener_mejor(self) -> Alumno:
        if len(self.__lista) == 0 :
            return 
        primero = self.__lista[0]
        for i in range (1,len(self.__lista)):
            if self.__lista[i].get_nota() > primero.get_nota():
                primero = self.__lista[i]
        return primero 
    
    def obtener_peor(self) -> Alumno:
        if len(self.__lista) == 0 :
            return 
        ultimo = self.__lista[0]
        for i in range (1,len(self.__lista)):
            if self.__lista[i].get_nota() < ultimo.get_nota():
                ultimo = self.__lista[i]
        return ultimo 
    
    def filtrar_aprobados(self) -> list[Alumno]:
        lista:list[Alumno] = []
        for alu in self.__lista:
            if alu.get_nota() >= 5 :
                lista.append(alu)
        return lista 

    def filtrar_suspendidos(self) -> list[Alumno]:
        lista:list[Alumno] = []
        for alu in self.__lista:
            if alu.get_nota() < 5 :
                lista.append(alu)
        return lista 

    def actualizar_nota(self,id: int , nueva_nota:int):
        if nueva_nota < 0 or nueva_nota > 10:
            return 
        for alu in self.__lista:
            if alu.get_id() == id :
                alu.set_nota(nueva_nota)

