# Class attributes

class Person:
    current_year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_year_of_birth(self):
        return Person.current_year - self.age

person1 = Person('Ricardo', 40)
person2 = Person('Maria', 85)

print(Person.current_year)
print(person1.get_year_of_birth())
print(person2.get_year_of_birth())
