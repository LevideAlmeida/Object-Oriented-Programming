# post_init: Executed after __init__ method

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    surname: str

    # def __init__(self, name, surname) -> None:
    #     self.name = name
    #     self.surname = surname

    def __post_init__(self):
        print('Running __post_init__')
        self.complete_name = f'{self.name} {self.surname}'

if __name__ == '__main__':
    p1 = Person('Levi', 'Almeida')
