from enum import Enum
class Meses (Enum): 
    Desconocido = 0 
    Enero = 1 
    Febrero = 2 
    Marzo = 3 
    Abril = 4 
    Mayo = 5 
    Junio = 6 
    Julio = 7 
    Agosto = 8 
    Septiembre = 9 
    Octubre = 10 
    Noviembre = 11 
    Diciembre = 12 

class Fecha : 
    day : int 
    month : Meses
    year : int 

    def __init__(self,year : int, month : Meses, day : int):
        #Restricciones de día 
        if day is not None and isinstance(day, int) and  day >= 1 and day <= 31 :      
            self._day : int = day

        #Restricciones de mes 
        if month is not None and  isinstance(month, Meses) and  month.value >= 1 and month.value <= 12 : 
          self._month : Meses = month  

        #Restricciones de año 
        if year is not None  and  isinstance(year,int ) : 
          self._year : int = year 


    def set_day(self, day: int) : 
        
        if self._month in (Meses.Enero,Meses.Marzo,Meses.Mayo,Meses.Julio,Meses.Agosto,Meses.Octubre,Meses.Diciembre):
            if day < 1 or day > 31 : 
                return 
            self._day = day 

        if self._month in (Meses.Abril,Meses.Junio,Meses.Septiembre,Meses.Noviembre) : 
            if day < 1 or day > 30  :
                return 
            self._day = day 
            
        if self._month == Meses.Febrero :
            if Fecha.is_leap(self._year):
                if day < 1 or day > 29: 
                    return 
                self._day= day  
            else:
                if day < 1 or day > 28:
                    return 
                self._day = day 
    def get_days_in_month (self, year: int , month:int) -> int :
        if self.month in (): 
            return










    def get_day(self) -> int : 
        return self._day

    def set_month(self, month: Meses) : 
        if  not isinstance(month,Meses):
            return 
        if month == Meses.Desconocido : 
            return   
        self._month = month 
    def get_month(self) -> Meses : 
        return self._month 
    
    def set_year(self, year : int ) : 
        if not isinstance(year, int) or year is None: 
            return 
    def get_year(self) -> int : 
        return self._year 
    
    @staticmethod
    def is_leap(year: int ) -> bool : 
       return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
            
   # def get_month(self) -> int dfgbrvsdfgvsdfg: 
        
        
    """
  )
    devolver_los_dias_de_un_mes
    add_days (count: int)
    add_months("")
    add_years("") 
    is_leap(): bool 
    get_week_number(): int 
    get__week_day(): DayOfWeek 
    """