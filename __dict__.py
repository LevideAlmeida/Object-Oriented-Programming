# __dict__ and vars for instances attributes

class Person:
    current_year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person('Robson', 18)

print(person1.__dict__)
print(person1.name)

del person1.name

print(vars(person1))

data = {'name': 'João', 'age': 35}
person2 = Person(**data)

print(vars(person2))
