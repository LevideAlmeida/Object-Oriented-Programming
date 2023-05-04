from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency: int, id: int, balance: float) -> None:
        super().__init__()
        self.agency = agency
        self._id = id
        self.balance = balance

    @abstractmethod
    def withdraw(self, money: float) -> None: ...

    def deposit(self, money: float) -> None:
        self.balance += money
        self.info(f'(Deposit: R${money})')

    def info(self, msg: str =''):
        print(f'Your balance have R${self.balance:.2f}  {msg}')
        print('------------------------------------------------\n')


class SavingAccount(Account):
    def __init__(self, agency, id, balance):
        super().__init__(agency, id, balance)

    def withdraw(self, money):
        balance_after_withdraw = self.balance - money
        if balance_after_withdraw > 0:
            self.balance -= money
            self.info(f'(Withdraw: R${money})')
            return

        print('Unable to withdraw desired amount')
        self.info('DENIED WITHDRAW')

    def __repr__(self):
        class_name = type(self).__name__
        attributes = f'({self.agency!r}, {self._id!r}, {self.balance!r})'
        return f'{class_name}{attributes}'

class CheckingAccount(Account):
    def __init__(self, agency: int, id: int, balance: float, limit: float):
        super().__init__(agency, id, balance)
        self.limit = limit

    def withdraw(self, money: float):

        balance_after_withdraw = self.balance - money
        max_limit = -self.limit

        if balance_after_withdraw >= max_limit:
            self.balance -= money
            self.info(f'(Withdraw: R${money})')
            return

        print('Unable to withdraw desired amount')
        print(f'Your limit is {self.limit}')
        self.info('DENIED WITHDRAW')

    def __repr__(self):
        class_name = type(self).__name__
        attributes = f'({self.agency!r}, {self._id!r}, {self.balance!r}, {self.limit!r})'
        return f'{class_name}{attributes}'

if __name__ == '__main__':
    account1 = SavingAccount(2,544,100)
    print(account1)

    # account2 = CheckingAccount(4, 122, 0, 100)
    # account2.withdraw(1000)
    # account2.withdraw(1)
