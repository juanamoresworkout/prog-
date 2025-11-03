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
        max_day = self.get_days_in_month(self._year,self._month) 
        if not isinstance (day, int) : 
            return 
        if 1 > day or day > max_day : 
            return 
        self.day = day
    

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
        self._year = year
    def get_year(self) -> int : 
        return self._year 
    

    def add_year(self, count: int ) : 
        if not isinstance(count,int) : 
            return 
        if count is None :
            return 
        self._year += count 

    def add_month(self, count : int) : 
        new_count_month = self._month.value + count 

        final_count_month = new_count_month  % 12  
        if final_count_month == 0 :
             final_count_month = 1 
        final_year = (new_count_month // 12 + self._year)

        self._year = final_year
        self._month= Meses(final_count_month)
    
    def add_day(self,count : int ) : 
        new_count_day = self._day + count
        while new_count_day > self.get_days_in_month(self._year,self._month) : 
            new_count_day -= self.get_days_in_month(self._year,self._month)
            
            self.add_month(1)
        self._day = new_count_day 

    #Utilidades 
    
    @staticmethod
    def is_leap(year: int ) -> bool : 
       return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
    
    def get_days_in_month (self, year: int , month: Meses) -> int :
            if month in (Meses.Enero,Meses.Marzo,Meses.Mayo,Meses.Julio,Meses.Agosto,Meses.Octubre,Meses.Diciembre): 
                return 31 
            if month in (Meses.Abril,Meses.Junio,Meses.Septiembre,Meses.Noviembre):
                return 30 
            if month == Meses.Febrero :
                if Fecha.is_leap(year) : 
                    return 29 
                return 28 
    def next_month(self) : 
        if not isinstance (self,Fecha): 
            return 
        if self._month == Meses.Diciembre : 
            self._month = Meses.Enero 
            self.add_year(1)
        else: 
            self.month.value += 1 
    def __eq__(self, other) -> bool:
        if not isinstance(other, Fecha):
            return False
        if other is None :
            return False  
        return (
            self._year == other._year and
            self._month == other._month and
            self._day == other._day
        )

    def return_fecha(self) -> str : 
        return f"{self._year} / {self._month.value} / {self._day}"
   # def get_month(self) -> int : 
       
    """
    get_week_number(): int 
    get__week_day(): DayOfWeek 
    """