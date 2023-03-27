# Class method + factories:
# Are methods where "self" will be "cls", in other words,
# the method receive the class as a parameter and not instance.


class Person:
    current_year = 2023 # class attribute

    def __init__(self, name, age):
        self.name = name # instance attribute
        self.age = age

    @classmethod
    def create_person_with_50_years_old(cls, name):
        return cls(name, 50)

    @classmethod
    def create_nameless(cls, age):
        return cls('nameless', age)

person1 = Person('Levi', 16)
person2 = Person.create_person_with_50_years_old('Vitoria')
person3 = Person.create_nameless(30)

print(person1.age)
print(person2.age)
print(person3.name)
