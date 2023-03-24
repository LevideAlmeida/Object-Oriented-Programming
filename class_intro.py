# class => Classes are molds for create new objects
# The classes generate new objects (instances) that
# can have their own attributes and methodes.
# The generate objects by the class can use their inside
# data for perform several actions.
# by convention, we use PascalCase for classes names.

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

person1 = Person('Levi', 'Almeida')
# person1.name = 'Levi'
# person1.surname = 'Almeida'

person2 = Person('Vitória', 'Araújo')
# person2.name = 'Vitória'
# person2.surname = 'Araújo'

print(person1.name)
print(person1.surname)

print(person2.name)
print(person2.surname)
