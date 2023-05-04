from abc import ABC, abstractmethod
from accounts import SavingAccount, CheckingAccount, Account
from person import Person, Client


class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []
        self.accounts = []
        self.agencies = ['1', '2', '3', '4']

    def add_client(self, client: Client):
        self.clients.append(client)

    def add_account(self, account: Account):
        self.accounts.append(account)

    def check(self):
        ...

saving_account = SavingAccount(1, 878, 1000)
checking_account = CheckingAccount(5, 654, 1000, 1000)

client1 = Client('Levi', '18')
client1.create_account(saving_account)

client2 = Client('Anne', '16')
client2.create_account(checking_account)

inter = Bank('Inter')
inter.add_client(client1)
inter.add_account(saving_account)

saving_account.deposit(100)
saving_account.withdraw(100)
