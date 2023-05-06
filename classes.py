
import datetime

today=datetime.date.today()
year=today.year
# print(year)

class Student:

    school='AkiraChix'
    def __init__(self,first_name,last_name,age,country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
    def _show_full_name(self):
        return f'{self.first_name} {self.last_name}'
        

    def _year_of_birth(self):
        return year - self.age
    def _show_initials(self):
        return f'{self.first_name[0]}.{self.last_name[0]}'
    

    