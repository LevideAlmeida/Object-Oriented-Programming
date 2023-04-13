# @abstractmethod is a decorator that defines abstract methods in abstract classes

from abc import ABC, abstractmethod

class AbstractCar(ABC):
    def __init__(self, name):
        self._name = name

    @property
    @abstractmethod
    def name(self): ...



class Car(AbstractCar):
    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

ford = Car('ford')
print(ford.name)
