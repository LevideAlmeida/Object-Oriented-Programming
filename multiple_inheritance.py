class A:
    ...

    def I_am(self):
        return 'I am class A'

class B(A):
    ...

    def I_am(self):
        return 'I am class B'

class C(A):
    ...

    def I_am(self):
        return 'I am class C'

class D(C, B):
    ...

    def I_am(self):
        return 'I am class D'


d = D()

print(d.I_am())

mro = D.__mro__
# mro = D.mro()

print(mro)
