# decorator function and decorator with classes


# def my_repr(self):
    # class_name = self.__class__.__name__
    # class_dict = self.__dict__
    # class_repr = f'{class_name}({class_dict})'
    # return class_repr

def add_repr(class_):

    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr

    class_.__repr__ = my_repr
    return class_

@add_repr
class Country:
    def __init__(self, name):
        self.name = name

@add_repr
class Planet:
    def __init__(self, name):
        self.name = name


brazil = Country("Brazil")
portugal = Country('Portugal')

earth = Planet('Earth')
mars = Planet("Mars")

print(brazil)
print(portugal)
print(earth)
print(mars)
