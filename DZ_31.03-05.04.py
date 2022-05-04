class People:
    '''Все люди'''
    amount = 0
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age
        People.amount += 1
    def tell(self):
        '''Вывести информацию'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")
    def say(self):
        print('I\'m people')
    @staticmethod
    def howMany():
        '''Выводит численность'''
        print('Количество людей {0:d}'.format(People.amount))

class Student(People):
    '''Только студенты'''
    def __init__(self, name, age, course):
        People.__init__(self, name, age)
        self.course = course
    def tell(self):
        '''Вывести информацию'''
        People.tell(self)
        print('Курс: "{0:d}"'.format(self.course))
    def say(self):
        print('I\'m student')
    

igor = Student('Игорь', 25, 1)

vlad = People("Влад", 20)

ivan = People("Иван", 22)

all = [igor, vlad, ivan]

for member in all:
    member.tell()
    member.say()
People.howMany()

from dataclasses import dataclass
@dataclass
class Size():
    
    size = 100
    
    def __init__(self):
        Size.size = Size.size+100
       
    @classmethod
    def total_size(cls):
        print("Total size: ", cls.size)
# Создаем объекты родительского класса       
my_obj1 = Size()
my_obj2 = Size()
# Создаем дочерний класс
class SecondSize(Size):
    size=0    
    pass
SecondSize.size()