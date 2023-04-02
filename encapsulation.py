# Encapsulation (access modifiers: public, protected, private)
# Python has no access modifiers
# but is used like convention:
#   (No underscore) = public
#       can be used anywhere
# _ (One underscore) = protect
#       must only be used inside the class
#       or its subclasses.
# __ (Two underscores) = private
#       should only be used inside the class
#       in which it was declared.

class Foo:
    def __init__(self):
        self.public = 'This is public'
        self._protected = 'This is protected'
        self.__private = 'This is private'

    def public_method(self):
        return 'public_method'

    def _protected_method(self):
        return '_protected_method'

    def __private_method(self):
        return "__private_method"

foo = Foo()
print(foo.public)
print(foo.public_method())
print(foo._protected)
print(foo._protected_method())
print(foo._Foo__private)
print(foo._Foo__private_method())

"""
its possible access the private modifier,
but, the python modify the method/attribute
name adding the class name in the beginning
with underscore symbolizing protection
"""
