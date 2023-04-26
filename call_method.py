# Dunder method __call__
# callable is something that can be executed with parentheses
# In normal classes, __call__ makes a class instance callable


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, name):
        print(name, 'is calling', self.phone)

call1 = CallMe('85987321860')
call1('Levi')

# call2 = CallMe('85986372062')
