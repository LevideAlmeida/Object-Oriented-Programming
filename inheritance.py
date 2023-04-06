class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def class_name(self):
        print('Person class')
        print(self.name, self.surname, self.__class__.__name__)

class Student(Person):
    def class_name(self):
        print('This is Student class, I AM STUDENT CLASS')
        print(self.name, self.surname, self.__class__.__name__)


class Client(Person):
    ...

vitoria = Student('Vitoria', 'Araújo')
levi = Client('Levi', 'Almeida')

vitoria.class_name()
levi.class_name()
