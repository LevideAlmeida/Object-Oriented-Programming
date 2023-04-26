# decorator function and decorator with methods

def my_planet(method):
    def internal(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if 'Earth' in result:
            result = 'You are at home! ' + result
        return result
    return internal

class Planet:
    def __init__(self, name):
        self.name = name

    @my_planet
    def i_am(self):
        return f'I am the planet {self.name}'

earth = Planet('Earth')
mars = Planet("Mars")


print(earth.i_am())
print(mars.i_am())
