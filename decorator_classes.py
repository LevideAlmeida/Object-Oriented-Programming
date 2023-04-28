# Decorator classes

# Decorator classes are classes that act as decorators

class Multiply:
    def __init__(self, multiplicator):
        self._multiplicator = multiplicator

    def __call__(self, func):
        def internal(*args, **kwargs):
            result = func(*args, **kwargs)
            result *= self._multiplicator
            return result
        return internal


@Multiply(9)
def sum(x,y):
    return x + y

two_plus_four = sum(2,4)
print(two_plus_four)
