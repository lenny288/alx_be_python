class BankAccount:
    """
    A simple BankAccount class to demonstrate OOP principles such as encapsulation.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initialize the bank account with an optional starting balance.
        """
        self.__account_balance = float(initial_balance)  # private attribute

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw the specified amount if there are sufficient funds.
        Returns True if successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
