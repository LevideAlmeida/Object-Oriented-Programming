# __new__ and __init__
# __new__ is the method reponsible for create
# and return the new object. That's why, new receive cls.
# __new__ ❗MUST return the object❗
# __init__ is the method reponsible for initialize
# the instance. That's why, init receive self.
# __init__ ❗ MUST return NONE(None)❗

class A(object):
    def __new__(cls, *args, **kwargs):
        print('before create instance')
        instance = super().__new__(cls)
        print('after create instance')
        return instance

    def __init__(self, x):
        self.x = x
        print('HI! I am init')

    def __repr__(self):
        return 'A()'

a = A(640)
print(a.x)
