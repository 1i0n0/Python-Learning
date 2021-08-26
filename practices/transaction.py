#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Create some bank accounts and requests various services
class Account:
    __rate = 0.02
    __acct_number = None
    __balance = 0
    __name = None

    # Set up the account by defining its owner, account number,
    # and initial balance
    def __init__(self, owner, account, initial_balance):
        self.__name = owner
        self.__acct_number = account
        self.__balance = initial_balance

    # Deposit the specified amount into the account
    # Return the new balance
    def deposit(self, amount):
        assert amount > 0
        self.__balance = self.__balance + amount
        return self.__balance

    # Withdraw the specified amount from the account and applies the fee
    # Return the new balance
    def withdraw(self, amount, fee):
        assert amount > 0
        assert fee > 0

        if self.__balance > (amount + fee):
            self.__balance = self.__balance - amount - fee
        else:
            print("no enough money!".title())
        return self.__balance

    # Add interest to the account and return the new balance
    def add_interest(self):
        self.__balance += (self.__balance * self.__rate)
        return self.__balance

    # Return the current balance of the account
    def get_balance(self):
        return self.__balance

    # Return a one-line description of the account as a string
    def __str__(self):
        __str = f"{self.__acct_number}\t{self.__name:10}\t${self.__balance:,.2f}"
        return __str


if __name__ == "__main__":
    acc1 = Account("Ted", 72354, 100.00)
    acc2 = Account("Jack", 69713, 200.00)
    acc3 = Account("Edward", 93757, 1000.00)

    acc1.deposit(25.00)

    print(f"Jack balance after deposit: {acc2.deposit(500.00)}")

    print(f"Jack balance after withdrawal: {acc2.withdraw(450.00, 1.50)}")

    acc1.add_interest()
    acc2.add_interest()
    acc3.add_interest()

    print()
    print(acc1)
    print(acc2)
    print(acc3)
