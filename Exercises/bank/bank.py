from accounts import Account, SavingAccount, CheckingAccount
from person import Client

class Bank:
    def __init__(self, name, agencies: 'list[str]' = []):
        self.name = name
        self.agencies: list[str] = agencies
        self.clients: list[Client] = []
        self.accounts: list[Account] = []

    def add_client(self, client: Client):
        self.clients.append(client)

    def add_account(self, account: Account):
        self.accounts.append(account)

    def _check_agency(self, agency: str) -> bool:
        if agency in self.agencies:
            return True

        return False

    def _check_client(self, client: Client) -> bool:
        if client in self.clients:
            return True

        return False

    def _check_account(self, account: Account) -> bool:
        if account in self.accounts:
            return True

        return False

    def _check_if_account_belongs_to_client(self, client: Client, account: Account) -> bool:
        if client.account is account:
            return True

        print('Client not belongs account')
        return False

    def check(self, client: Client, account: Account) -> bool:
        check_agency = self._check_agency(client.account.agency)
        check_client = self._check_client(client)
        check_account = self._check_account(account)
        check_if_account_in_client = self._check_if_account_belongs_to_client(client, account)

        if not check_agency:
            print('Agency not found')
            return False

        if not check_client:
            print('Client not found')
            return False

        if not check_account:
            print('Account not found')
            return False

        if not check_if_account_in_client:
            print('Account does not belongs to client')
            return False

        print('All checks passed')
        return True

    def __repr__(self):
        class_name = type(self).__name__
        attributes = f'({self.agencies!r}, {self.clients!r}, {self.accounts!r})'
        return f'{class_name}{attributes}'

if __name__ == '__main__':
    bank1 = Bank('Inter')
    bank1.agencies.extend(['1', '2', '3', '4'])

    account1 = SavingAccount('2',544,100)
    client1 = Client('Levi', '18')
    client1.create_account(account1)

    account2 = CheckingAccount('3', 654, 1000, 1000)
    client2 = Client('Anne', '16')
    client2.create_account(account2)

    bank1.clients.extend([client1])
    bank1.accounts.extend([account1, account2])

    bank1.check(client1, account1)
    bank1.check(client1, account2)

    print(bank1)
