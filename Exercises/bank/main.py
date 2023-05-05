from accounts import SavingAccount, CheckingAccount, Account
from person import Client
from bank import Bank


saving_account = SavingAccount('1', 878, 1000)
checking_account = CheckingAccount('5', 654, 1000, 1000)

client1 = Client('Levi', '18')
client1.create_account(saving_account)

client2 = Client('Anne', '16')
client2.create_account(checking_account)

inter = Bank('Inter')
inter.add_client(client1)
inter.add_account(saving_account)

saving_account.deposit(100)
saving_account.withdraw(100)
