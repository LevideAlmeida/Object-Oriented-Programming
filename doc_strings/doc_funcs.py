"""this is a exemple module
this module contains functions and exemples of functions documentation.
sum function is classic.
"""
variable_1 = 1

# def soma(x, y):


def sum(x: int, y: int) -> int:
    """Sum x and y
    this module contains functions and exemples of functions documentation.
    sum function is classic.

    :param x: Number 1
    :type x: int
    :param y: Number 2
    :type y: int
    :return: The sum between x and y
    :rtype: int
    """
    return x + y


def multiply(
    x: int,
    y: int,
    z: int = None
) -> int:
    """Multiply x, y and/or z
    Multiply x and y. If z is sent, multiply x, y and z.
    """
    if z is None:
        return x * y
    return x * y * z


variable_2 = 2
variable_3 = 3
variable_4 = 4
