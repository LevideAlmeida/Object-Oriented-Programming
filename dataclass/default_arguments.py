# It's possible create default arguments, but only with immutable values

from dataclasses import dataclass, field

@dataclass
class Person:
    name: str = 'missing'
    surname: str = 'Not sent'
    age: int = 0
    
    # use field function to use mutable values with defult arguments
    address: list = field(default_factory=list)

    # field also have other parameter. Explore them if you want.


if __name__ == '__main__':
    p1 = Person('Levi', 'Almeida')
    print(p1)