'''
class MyString(str):
    def upper(self):
        print("CALL UPPER")
        return super().upper()
        # Super are all classes that are higher in the hierarchy


mystring = MyString('Euzinho')
print(mystring.upper())
'''

class A:
    a_attribute = 'value a'

    def __init__(self, attribute):
        self.attribute = attribute

    def method(self):
        print('A')


class B(A):
    b_attribute = 'value b'

    def __init__(self, attribute):
        super().__init__(attribute)

    def method(self):
        print('B')



class C(B):
    c_attribute = 'value c'

    def __init__(self, *args, **kwargs):
        print("Hello")
        super().__init__(*args, **kwargs)

    def method(self):
        super(B, self).method() # super will call method() looking in classes in B or higher
        print('C')

c = C('Attribute')
print(c.a_attribute)
print(c.b_attribute)
print(c.c_attribute)

b = B('Attribute')

# print(C.mro())
# print(B.mro())
# print(A.mro())
