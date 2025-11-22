#NickName: Loves 
#Esta clase es privada, pero hice este ejercicio en 20 min, te dije antes de dar el examen que estaba así por eso.
#y que el:  _ para hacerla privada es necesario , pero de lo rapido que iba te dije que no lo ponía pero que si lo sabía.
#Te lo volví a decir en la clase de la correcion, para que lo supíeras, intento ser justo y poner literamente lo que pensaba o tenía.
#me dijiste que te lo dejara aclarado que lo habia escrito asi por ir más rapido.
class Alumno:
    _nombre : str
    _nota: int 
    _id : int 

    def __init__(self,id : int):
        if not isinstance(id,int):
            raise ValueError("Tipo no valido")
        if id is None : 
            raise ValueError("No valido, vacio")
        if id > 0 :
         self._id = id 

        self._nombre = "Añadir"
        self._nota= -1 
    
    def set_nombre(self,nombre: str) : 
       if not isinstance(nombre,str):
          raise ValueError("Tipo no valido.")
       if nombre is None: 
          raise ValueError("No valido, vacío")
       self._nombre = nombre 
    
    def get_nombre(self) -> str : 
       return self._nombre
    
    def set_nota(self,nota: int ) : 
       if not isinstance(nota,int):
          raise ValueError("Tipo no valido.")
       if nota is None : 
          raise ValueError("No valido,vacio.")
       #Aquí no se porque no esta el 1 del diez, pero esta claro que la validacion que quería hacer es esta.
       #Lo dejo claro porque pone 0 pero es que me quedaban 15 min. Fallo de ir tan rapido. Pero era un 10 claro.
       #En actualizar nota, se ve claramente que la validación es esa. 
       if nota >= 0 and nota <= 10 :
          self._nota = nota 
    
    def get_nota(self) -> int : 
       return self._nota
    
    #Si te fijas hay dos veces get_nombre, los nervios y correr me hicieron fallar en la sintaxis, me quedaban
    #15 min, pero cree 3 metodos, que devuelven cada atributo, el ultimo realmente me referia al ID. 
    #Fallando en la sintaxis, aunque en este contexto seria un poco mas dislexia. Discula profesor
    #Este ultimo metodo es este, de ahí que hay 3 uno para cada atributo. 
    def get_id(self) -> int : 
       return self._id 
    
    def to_string (self) -> str:
       return f"Nombre: {self._nombre}, ID: {self._id}, Nota: {self._nota}"
    
    def actualizar_nota(self,nueva_nota:int):
       if nueva_nota is None :
          raise ValueError("No puede ser nada.")
       if not isinstance(nueva_nota,int):
          raise ValueError("Introduce un entero")
       if self._nota == nueva_nota:
          raise ValueError("No puede ser la misma")
       if nueva_nota >= 0 and nueva_nota <= 10:
          self._nota = nueva_nota 
    
    def es_aprobado(self) -> bool: 
       return self._nota >= 5 
    

          
        

    