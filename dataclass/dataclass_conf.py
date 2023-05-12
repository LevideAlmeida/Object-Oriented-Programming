# the dataclass decorator also can take arguments
# init=False - Disable automatic init creation

from dataclasses import dataclass, asdict, astuple

# frozen=True - Frozen the class, i.e., prevents the criation/modification of class attributes
# repr=False - Disable repr

@dataclass(frozen=True, repr=False)
class Person:
    name: str
    surname: str
#   def __init__(self, name, surname):
#       self.name = name

# There are others paramether. Explore them

if __name__ == '__main__':
    p1 = Person('Levi', 'Almeida')
    # p1.name = 'aaaaaa' #Frozen
    print(p1)
    print(asdict(p1)) # print instance as dict
    print(astuple(p1)) # print instance as tuple
    