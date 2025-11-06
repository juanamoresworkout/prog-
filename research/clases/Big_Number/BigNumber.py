from __future__ import annotations

class BigNumber: 
    number : str 

    def __init__(self,number : str):
       if BigNumber._validar_number(number): 
           self._number = self.gen_list(number)
    
    def equals(self, other: BigNumber) -> bool : 
        if not isinstance(other,BigNumber):
            return False
        return self._number == other._number
    
    @staticmethod       
    def _validar_number(number :str) -> bool: 
        if number is not None and isinstance(number,str):
            return True 
        return False 
    
    @staticmethod 
    def gen_list (number: str) ->list[int]: 
        lista = []
        if BigNumber._validar_number(number):
            for digito in number: 
                if not digito in ("0","1","2","3","4","5","6","7","8","9"): 
                   return "No se puede"
                lista.append(int(digito))
            return lista 
    def get_number(self) -> list[int]:
        return self._number 
    
numbero = BigNumber("344")

print(numbero.get_number())

