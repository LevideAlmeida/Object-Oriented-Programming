# Methods in class instances

class Car:
    def __init__(self, car_name='No named'):
        self.name = car_name

    def accelerate(self):
        return f'{self.name} is accelerating...'

ford = Car('Ford')
print(ford.name)
print(ford.accelerate())

volkswagen = Car(car_name='Volkswagen')
print(volkswagen.name)
print(volkswagen.accelerate())
