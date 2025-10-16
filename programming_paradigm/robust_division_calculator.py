class BankAccount:
    """
    A simple BankAccount class demonstrating encapsulation and basic OOP principles.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes the BankAccount with an optional initial balance.
        """
        self.__account_balance = float(initial_balance)  # private attribute (encapsulation)

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount if sufficient funds exist.
        Returns True if successful, otherwise False.
        """
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
            return False

        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Displays the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
