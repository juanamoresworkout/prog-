
from alumno import Alumno

class Curso: 
    _grupo: list[Alumno]

    def __init__(self) : 
        self._grupo = []

#Escribo esto pero me he dado cuenta que como lo hice rapido lo que realmente queria hacer:

#def agregar_alumno(self, alumno: Alumno):
#    for alu in self._grupo:
#        if alumno.get_id() == alu.get_id():
#            return  
#    self._grupo.append(alumno)
#Porque aqui realmente queria recorrer todos los alumnos y que si no es igual añada, esta mal. Por hacerla corriendo.
#Tacho los true y false porque me lie con si no devolvia nada o true o false y decidi quitar el bool.  
    def agregar_alumno(self,alumno : Alumno) :
        for alu in self._grupo:
            if alumno._id != alu._id:
               return self._grupo.append(alumno)

#Lo que pone en mi hoja de que quito el numero, me refiero al remove que no recordaba como se usaba el pop era de otra forma. 
#De ahi que ponga al lado aun poniendo el pop aqui y en el otro caso lo quito el alumno en esa posicion 
    def eliminar_alumno_por_id(self,id: int) : 
        if len(self._grupo) <= 0 : 
            raise ValueError("Lista no valida, vacia")
        for alu in self._grupo :
            if alu._id == id :
                self._grupo.remove(alu)

    def buscar_por_id(self,id:int) -> Alumno | None :
        if not isinstance(id,int):
            raise ValueError("Tipo no valido")
        if id is None : 
            raise ValueError("No valido, vacio")
        for alu in self._grupo: 
            if alu._id == id :
                return alu 
        #Linea faltante.
        return None 
    
    def obtener_tamano(self) -> int:
        return len(self._grupo)
    
    def obtener_promedio(self) -> float :
        nota_total = 0 
        for alu in self._grupo:
            nota_total += alu._nota 
    #La flecha quiere decir que promedio viene de nota_final, no que va ahí. 
        promedio = float(nota_total/ len(self._grupo))
        return promedio 
 
    def obtener_mejor(self) -> Alumno:
         #El texto de al lado que pongo señalando a esta linea, es que queria almacenar el primer alumno.
         #Para comparar su nota pero no sabia si hacia falta o no la nota, de ahi poner esto aquí o abajo.
         primer = self._grupo[0] 
         for i in range(len(self._grupo)):
            #Puse las dos cosas pero esta es la comprobacion. Fallo a la hora de escribirlo
            #Pero queria referirme a esto 
            if self._grupo[i]._nota > primer._nota:
                 primer = self._grupo[i]
         return primer
     #Se que tendría que haber hecho minimo un que la lista no este vacio pero iba demasiado rapido.    
    def obtener_peor(self) -> Alumno:
        peor = self._grupo[0]  
        for i in range(len(self._grupo)):
            if self._grupo[i]._nota < peor._nota:
                peor = self._grupo[i]
        return peor
    
    def filtrar_aprobados(self)-> list[Alumno]:
        nueva_lista: list[Alumno] = []
        for alu in self._grupo:
            if alu._nota >= 5 :
                nueva_lista.append(alu)
        return nueva_lista 

    def filtrar_suspendidos(self) -> list[Alumno]:
        nueva_lista: list[Alumno] = []
        for alu in self._grupo:
            if alu._nota < 5:
                nueva_lista.append(alu)
        return nueva_lista
    
    def actualizar_nota_id(self,id:int,nueva_nota:int):
        if not isinstance(id,int) or not isinstance(nueva_nota,int):
            raise ValueError("Tipo no valido")
        if id is None or nueva_nota is None : 
            raise ValueError("No valido, vacio")
        if not (nueva_nota >= 0 and nueva_nota <= 10):
            raise ValueError("Fuera de rango")
        for alu in self._grupo :
            if alu._id == id :
                #Lo escribi porque me quedaba un minuto en vez de codigo.
                alu._nota = nueva_nota
    
    def to_string(self) -> list[str]:
        nueva_lista = []
        for alu in self._grupo:
            nueva_lista.append(alu.to_string())
        return nueva_lista 

        