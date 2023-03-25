import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class_name = 'Person'
FILE_PATH = 'person.json'


person1 = Person('Levi', 16)
person2 = Person('Vitoria', 25)
person3 = Person('Emily', 15)
person_list = [vars(person1), vars(person2), vars(person3)]

def save_with_json():
    with open(FILE_PATH, 'w') as file:
        json.dump(person_list, file, indent=2)

if __name__ == '__main__':
    save_with_json()
