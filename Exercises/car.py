class Car:
    def __init__(self, name):
        self.name = name
        self._engine = None
        self._manufacturer = None

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

class Engine:
    def __init__(self, name):
        self.name = name

class Manufacturer:
    def __init__(self, name):
        self.name = name

fiat = Car('Ford')
mercedes_engine = Engine('BMW 2.0')
ford = Manufacturer('BMW')

fiat.engine = mercedes_engine
fiat.manufacturer = ford

print('Name:', fiat.name)
print('Engine:', fiat.engine.name)
print('Manufacturer:', fiat.manufacturer.name)
print()


fiat = Car('Fiat')
mercedes_engine = Engine('1.0')
ford = Manufacturer('Ford')

fiat.engine = mercedes_engine
fiat.manufacturer = ford

print('Name:', fiat.name)
print('Engine:', fiat.engine.name)
print('Manufacturer:', fiat.manufacturer.name)
