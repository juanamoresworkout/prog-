from image import * 
from codec import *

class Table2D:
    def __init__(self, width, height):
        self.__w: int = width
        self.__h: int = height
        #Multiplico alto por ancho, para crear las posiciones
        self._table = [0] * (width * height)
    
    def get_width(self) -> int : 
        return self.__w
    
    def get_heigth(self) -> int :
        return self.__h

    def get_index(self, x, y) -> int:
        return y * self.get_width() + x

    def set_cell(self, x, y, value):
        self._table[self.get_index(x, y)] = int(value)

    def get_cell(self, x, y) -> int:
        return self._table[self.get_index(x, y)]

    def posicion_dentro_de_imagen(self, x, y) -> bool:
        return 0 <= x < self.w and 0 <= y < self.h
    
    #Reciclo la funcion que binariza 
    def binarizar(image:Image, num: float): 
        result: Image = Image(image.width,image.height)
        for y in range(image.height):
            for x in range(image.width):
                c = image.get_pixel(x,y)
                media= (c.r + c.g + c.b) / 3.0
                if  media >= num :
                    c.r = 1.0 
                    c.g = 1.0 
                    c.b = 1.0
                else: 
                    c.r = 0
                    c.g = 0 
                    c.b = 0 
                result.set_pixel(x,y,c)
        return result
    
def imagen_binaria_a_tabla2(image: Image) -> Table2D:
    table = Table2D(image.width, image.height)

    for y in range(image.height):
        for x in range(image.width):
            c = image.get_pixel(x, y)
            # Uso cualquier canal porque estan todos a 0 o 1 
            if c.r >= 0.5: 
                table.set_cell(x, y, 1)
 
            else:  
                table.set_cell(x, y, 0)

    return table

img = Image()

img.load_from("pastillas0.tga")

resultado:Table2D = imagen_binaria_a_tabla2(img)

print(resultado._table)




