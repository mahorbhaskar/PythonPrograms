'''Bank Account Manager
Under the Classes section in the list of suggested final capstone projects is a Bank Account Manager program.
The goal is to create a class called Account which will be an abstract class for three other classes called
CheckingAccount, SavingsAccount and BusinessAccount.
Then you should manage credits and debits from these accounts through an ATM style program.'''

'''
Step 1: Establish an abstract Account class with features shared by all accounts.
Note that abstract classes are never instantiated, they simply provide a base class 
with attributes and methods to be inherited by any derived class.
'''


class Account:
    # Define an __init__ constructor method with attributes shared by all accounts:
    def __init__(self, acct_nbr, opening_deposit):
        self.acct_nbr = acct_nbr
        self.balance = opening_deposit

    # Define a __str__ mehthod to return a recognizable string to any print() command
    def __str__(self):
        return f'${self.balance:.2f}'

    # Define a universal method to accept deposits
    def deposit(self, dep_amt):
        self.balance += dep_amt

    # Define a universal method to handle withdrawals
    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
        else:
            return 'Funds Unavailable'

#Step 2: Establish a Checking Account class that inherits from Account, and adds Checking-specific traits.

class Checking(Account):
    def __init__(self,acct_nbr,opening_deposit):
        # Run the base class __init__
        super().__init__(acct_nbr,opening_deposit)

    # Define a __str__ method that returns a string specific to Checking accounts
    def __str__(self):
        return f'Checking Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'

#Step 3: TEST setting up a Checking Account object
x = Checking(54321,654.33)
print(x)
x.withdraw(1000)
x.withdraw(30)
x.balance

#step 4 : setup similar savings and business account classes

class Savings(Account):
    def __init__(self,acct_nbr,opening_deposit):
        # Run the base class __init__
        super().__init__(acct_nbr,opening_deposit)

    # Define a __str__ method that returns a string specific to Savings accounts
    def __str__(self):
        return f'Savings Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'


class Business(Account):
    def __init__(self,acct_nbr,opening_deposit):
        # Run the base class __init__
        super().__init__(acct_nbr,opening_deposit)

    # Define a __str__ method that returns a string specific to Business accounts
    def __str__(self):
        return f'Business Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'
