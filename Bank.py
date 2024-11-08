import random

class BankAccount:
    def __init__(self, full_name, account_number=None):
        self.full_name = full_name
        self.account_number = account_number if account_number else self.generate_account_number()
        self.balance = 0.0

    def generate_account_number(self):
        return str(random.randint(10000000, 99999999))

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount:.2f} new balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Charging $10 overdraft fee.")
            self.balance -= 10  # Overdraft fee
        else:
            self.balance -= amount
        print(f"Amount withdrawn: ${amount:.2f} new balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Current balance for {self.full_name}: ${self.balance:.2f}")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083  # Monthly interest
        self.balance += interest
        print(f"Interest added: ${interest:.2f} new balance: ${self.balance:.2f}")

    def print_statement(self):
        print(f"{self.full_name}\nAccount No.: ****{self.account_number[-4:]}\nBalance: ${self.balance:.2f}")

def main():
    # Prompt user for account information
    full_name = input("Enter the full name of the account owner: ")
    account_number = input("Enter the account number (or press Enter for a random one): ")
    
    # Create bank account instance
    bank_account = BankAccount(full_name, account_number if account_number else None)

    # User menu for account operations
    while True:
        print("\nChoose an action:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Get Balance")
        print("4. Add Interest")
        print("5. Print Statement")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            bank_account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            bank_account.withdraw(amount)
        elif choice == '3':
            bank_account.get_balance()
        elif choice == '4':
            bank_account.add_interest()
        elif choice == '5':
            bank_account.print_statement()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
