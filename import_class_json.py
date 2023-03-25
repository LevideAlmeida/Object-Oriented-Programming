import json

from export_class_json import Person, FILE_PATH

with open(FILE_PATH, 'r') as file:
    file_data = json.load(file)

    person1 = Person(**file_data[0])
    person2 = Person(**file_data[1])
    person3 = Person(**file_data[2])

    print(person1.name, person1.age)
    print(person2.name, person2.age)
    print(person3.name, person3.age)
