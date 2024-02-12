class BankAccount:
    def __init__(self, account_num, account_holder, balance=0):
        self.account_num = account_num
        self.account_holder = account_holder
        self.balance = balance

class SavingAccount(BankAccount):
    def __init__(self, account_num, account_holder, balance=0, interest_rate=0.02):
        self.interest_rate = interest_rate
        super()._init_(account_num, account_holder, balance)

    def add_interest(self):
        amount = self.balance * self.interest_rate
        self.balance += amount


class CheckingAccount(BankAccount):
    def __init__(self, account_num, account_holder, balance, over_limitdraft = 100):
        super()._init_(account_num, account_holder, balance)
        self.over_limitdraft = over_limitdraft

    def withdraw(self, amount):
        if amount <= self.balance + self.over_limitdraft:
            self.balance -= amount
        else:
            print("Insufficient balance")

while 1:
    print('''
    Welcome to GLA  Bank
          1. Saving Account
          2. Checking account
          3. Current account
          4. Exit
    ''')
choice = int(input("Enter the choice 1/2/3:  "))
if choice == 1:
    ac = SavingAccount(10000001, 'ravi', 10)
    accounts.append(ac)

    while 1:
        print("Menu")
        print('1. Deposite')
        print('2. Withdraw')
        print('5. Display all account')
        if choice == 1:
            

if __name__ == '_main_':
    saving_account1 = SavingAccount(1230099, 'ravi', 100)
    checking_account1 = CheckingAccount(113133, 'Saket', 1200)