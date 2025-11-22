from image import *


img = Image()
img.load_from("celda.tga")  # o .tga, .ppm, .png, .jpg
img.save_to("salida.tga")  
    
def gray_filter(image: Image):
    result:Image = Image(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            c = image.get_pixel(x,y)

            media= (c.r + c.g + c.b) / 3.0
            c.r = media 
            c.g = media
            c.b = media  

            result.set_pixel(x,y,c)
    return result 
def add_factor(image: Image,fr: float, fg: float,fb: float) -> Image :
    result:Image = Image(image.width, image.height)
    #if 0 > fr > 1 or 0 > fg > 1 or 0 > fb > 1 :
        #raise ValueError("Rango factor fuera de 0 y 1 ")
    for y in range(image.height):
        for x in range(image.width):
            c = image.get_pixel(x,y)
            c.r = c.r * fr 
            c.g = c.g * fg 
            c.b = c.b * fb 
            result.set_pixel(x,y,c)
    return result 

def sature(image:Image) : 
    result:Image = Image(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            c = image.get_pixel(x,y)
            if c.r > 1.0 : 
                c.r = 1.0
            if c.r < 0 : 
                c.r = 0 
            
            if c.g > 1.0 : 
                c.g = 1.0
            if c.g < 0 : 
                c.g = 0 
            
            if c.b > 1.0: 
                c.b = 1.0
            if c.b < 0 : 
                c.b = 0 
            result.set_pixel(x,y,c)
    return result

def invert(image:Image) : 
    result:Image = Image(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            c = image.get_pixel(x,y)
            c.r = 1 - c.r 
            c.g = 1 - c.g 
            c.b = 1 - c.b 
            result.set_pixel(x,y,c)
    return result

def incrementar_h_hsl(image:Image, num: float) :   
    result: Image = Image(image.width, image.height)
    for y in range(image.height): 
        for x in range(image.width): 
            c = image.get_pixel(x,y)
            hsl : HSL= c.to_hsl()
            hsl.h += num 
            c = hsl.to_rgb()
            result.set_pixel(x,y,c)
    return result

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


def min_of_neightbours(image:Image, pixel_x: int, pixel_y: int) -> Color: 
    result: Color = Color(1.0,1.0,1.0)
    for y in range(pixel_y - 1 , pixel_y + 2 ):
        for x in range(pixel_x -1, pixel_x + 2 ):  
            c = image.get_pixel(x , y)
            result = min_color(c,result)
    return result 

def max_of_neightbours(image: Image, pixel_x: int, pixel_y: int) -> Color:
    result: Color = Color(0.0, 0.0, 0.0)
    for y in range(pixel_y - 1, pixel_y + 2):
        for x in range(pixel_x - 1, pixel_x + 2):
            c = image.get_pixel(x, y)
            result = max_color(c, result)
    return result

def encoger(image: Image) -> Image:
    result = Image(image.width, image.height)
    for y in range(1, image.height - 1):
        for x in range(1, image.width - 1):
            c = min_of_neightbours(image, x, y)
            result.set_pixel(x, y, c)
    return result


def encoger_por_lineas(image: Image, num: int) -> Image:
    result = image
    for _ in range(num):
        result = encoger(result)
    return result

def agrandar(image: Image) -> Image:
    result = Image(image.width, image.height)
    for y in range(1, image.height - 1):
        for x in range(1, image.width - 1):
            c = max_of_neightbours(image, x, y)
            result.set_pixel(x, y, c)
    return result

def agrandar_por_lineas(image: Image, num: int) -> Image:
    result = image
    for _ in range(num):
        result = agrandar(result)
    return result        
        




#Ejercicio que vale un punto  
# ==========================================================================================     
def convolution_pixel(image:Image,pixel_y:int,pixel_x:int,kermel: tuple[float]) -> Color : 
    result_r = 0.0
    result_g = 0.0
    result_b = 0.0
    k = 0 
    for y in range(pixel_y - 1 , pixel_y + 2 ):
        for x in range(pixel_x -1, pixel_x + 2 ):  
            c = image.get_pixel(x , y)
            pos = kermel[k]
            result_r = result_r + (c.r * pos)
            result_g = result_g + (c.g * pos)
            result_b = result_b + (c.b * pos)
            k += 1
            
    return Color(result_r,result_g,result_b,1.0)

def convolution_img(image:Image,kermel: tuple[float]) -> Image: 
    result = Image(image.width,image.height)
    for y in range(1,image.height - 1 ) :
        for x in range(1,image.width - 1):
            c = convolution_pixel(image, y, x, kermel)
            result.set_pixel(x,y,c)
    return result
# ==========================================================================================  
kermelito = (
    0.11, 0.11, 0.11,
    0.11, 0.11, 0.11,
    0.11, 0.11, 0.11
)
img = Image()
#img2 = Image()
img.load_from("coche.tga")
seco = convolution_img(img,kermelito)
seco.save_to("seco4.tga")
#difuminada = add_factor(img,3.0,3.0,3.0)
#difuminada = difuminar_por_lineas(img,10)
#difuminada.save_to("salida3.tga")
#img2.load_from("matricula.tga")
#res =add_factor(img,3.0,3.0,3.0)
#res2 = sature(res)
#inv = incrementar_h_hsl(img,0.5)
#inv = binarizar(img,0.5)
#inv1= binarizar(img2,0.5)
#inv.save_to("pastillas0.tga")
#inv1.save_to("matricula0.tga")













for y in range(img.height):
    for x in range(img.width):
        c = img.get_pixel(x, y)
        hsl = c.to_hsl()
        hsl.rotate(-0.25)
        c = hsl.to_rgb()
        img.set_pixel(x, y, c)



# guarda en formato texto PPM
