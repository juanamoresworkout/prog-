from __future__ import annotations
from typing import * 


T = TypeVar("T")


class Queve(Generic[T]): 
    def __init__(self):
        super().__init__()
        self.__list: list[T] = []
    
    def get_element_count(self) -> int :
        if self.__list == [] :
            return 0
        return len(self.__list)
    
    def enqueve(self,element: T):
        self.__list.append(element)

    def top(self):
        if len(self.__list) == 0 :
            return None 
        return self.__list[0]

    def dequeve(self) -> T: 
        aux = self.top()
        self.__list.pop(0)
        return aux 
    
    def visit(self, visitor:Callable[[T], None]):
        if visitor is None : 
            return 
        for element in self.__list:
            visitor(element)
    
    def filter(self, a_filter: Callable[[T], bool]) -> Queve[T]:
        result = Queve[T]()

        for element in self.__list :
            if a_filter(element):
                result.enqueve(element)
        return result 

