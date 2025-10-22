#Type value 
###########
# Palo (type)

#0.Trebol
#1.Picas
#2.Diamantes
#3.Corazones 


class PokerCard:

    def __init__(self):
        self._number = -1
        self._type = -1 
    
    def set_number(self,number: int) : 
        if number <= 0 : 
            return 
        if number > 13 : 
            return 
        self._number = number 

    def get_number(self) -> int : 
        return  self._number 
    
    def set_type(self,number: int) : 
        if number < 0 : 
            return 
        if number > 3: 
            return 
        self._type = number 
    def get_type(self) -> int :
        return self._type

    def is_value(self) -> bool :
      return self.get_number() > 0 and self.get_type() >= 0

    
    def return_type(self,number: int) -> str :
        if number == 0:
            return "Trebol"
        if number == 1:
            return "Picas"
        if number == 2: 
            return "Diamantes"
        if number == 3:
            return "Corazones"
        return "Desconocido"
    def return_card(self) -> str:
      return  f"{self.get_number()} de {self.return_type(self.get_type())}"
        

    
        



      

    


