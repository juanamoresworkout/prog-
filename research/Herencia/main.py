from abc import abstractmethod
from math import *
class Figure: 
    center: float 
    def __init__(self, x : float = 0.0, y : float = 0.0):
        self.x = x
        self.y = y

    def get_perimeter(self) -> float:
         return 0.0
    
    @abstractmethod
    def get_area(self) -> float :
        pass 

    def __repr__(self):
        return f" x: {self.x}, y:{self.y}"

class Circle(Figure):
    def __init__(self, x = 0.0, y = 0.0, radius: float = 0.0):
        super().__init__(x, y)
        if radius < 0.0:
            radius = 0.0 
        self.__radius = radius 
    
    def get_perimeter(self):
        return 2.0 * pi * self.__radius
    
    def get_area(self):
        return pi * (self.__radius * self.__radius)
    
    def __repr__(self):
        return  f"radius: {self.__radius}" + super().__repr__()

class Rectangle(Figure):
    def __init__(self, x = 0, y = 0, width: float = 0.0 ,height: float = 0.0):
        super().__init__(x, y)
        self._width = width 
        self._heigth = height

    def get_perimeter(self) -> float:
        return self._width * 2.0 + self._heigth * 2.0
    
    def get_area(self):
        return self._width * self._heigth

class Blueprint:
    def __init__(self):
        self._figures :list[Figure]= []

    def get_figures(self) -> list[Figure]:
        return self._figures.copy()
    
    def add_figure(self,figure: Figure):
        if figure is None: 
            return 
        self._figures.append(figure)
    
    def suma_area(self) -> float:
        total_area: float  = 0.0
        for figure in self._figures:
            total_area += figure.get_area()
        return total_area 
    
    def remove_all_rectangle(self):
        for i in range (len(self._figures) -1 ,-1, -1):
            if isinstance(self._figures[i],Rectangle):
                self._figures.pop(i)

    
c : Figure = Circle(1,2,3)
print(c)
print(c.get_area())