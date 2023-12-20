class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds on the account")

    def display_account_info(self):
        print(f"Bank Account No: {self.account_number}")
        print(f"Balance: PLN {self.balance:.2f}")

account = BankAccount("12 3456 5555 9090 1111 0000 7722")
account.display_account_info()
account.deposit(25.30)
account.display_account_info()
account.withdraw(31.70)
account.display_account_info()
account.withdraw(14)
account.display_account_info()
