from accounts import Account

class Person:
    def __init__(self, name: str, age: str):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: str):
        self._age = age

    def __repr__(self):
        class_name = type(self).__name__
        attributes = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attributes}'

class Client(Person):
    def __init__(self, name: str, age: str):
        super().__init__(name, age)
        self.account = None

    def create_account(self, account: Account):
        self.account = account


if __name__ == '__main__':
    client1 = Client('Levi', '18')
    print(client1)
