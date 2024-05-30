class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def __str__(self):
        return f"Account {self.account_number}: Balance ${self.balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount


class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self.balance < (self.overdraft_limit * -1):
            print(f"Overdraft letter sent for Account {self.account_number}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account):
        self.accounts[account.account_number] = account

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]

    def pay_dividend(self, dividend_amount):
        for account in self.accounts.values():
            account.deposit(dividend_amount)

    def update_accounts(self):
        for account in self.accounts.values():
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()

    def show_accounts(self):
        for account in self.accounts.values():
            print(account)


account_1 = Bank()
savings_acc_1 = SavingsAccount(1, 1000, 0.5)
account_1.open_account(savings_acc_1)
            