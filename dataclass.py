# dataclasses are a sintax sugar for create classes with less code
# dataclasses are used for create classes that only have attributes
# dataclass define methods like __init__, __repr__ and __eq__

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    surname: str

    @property
    def complete_name(self) -> str:
        return f'{self.name} {self.surname}'

    @complete_name.setter
    def complete_name(self, value):
        name, *surname = value.split(' ')
        self.name = name
        self.surname = ' '.join(surname)

if __name__ == '__main__':
    p1 = Person('Levi', 'Almeida')
    p1.complete_name = 'Levi de Almeida Pontes'
    print(p1)
    print(p1.complete_name)
