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

#Step 5: Create a Customer class
#For this next phase, let's set up a Customer class that holds a customer's name and PIN and can contain any number
# and/or combination of Account objects.

class Customer:
    def __init__(self, name, PIN):
        self.name = name
        self.PIN = PIN

        # Create a dictionary of accounts, with lists to hold multiple accounts
        self.accts = {'C': [], 'S': [], 'B': []}

    def __str__(self):
        return self.name

    def open_checking(self, acct_nbr, opening_deposit):
        self.accts['C'].append(Checking(acct_nbr, opening_deposit))

    def open_savings(self, acct_nbr, opening_deposit):
        self.accts['S'].append(Savings(acct_nbr, opening_deposit))

    def open_business(self, acct_nbr, opening_deposit):
        self.accts['B'].append(Business(acct_nbr, opening_deposit))

    # rather than maintain a running total of deposit balances,
    # write a method that computes a total as needed
    def get_total_deposits(self):
        total = 0
        for acct in self.accts['C']:
            print(acct)
            total += acct.balance
        for acct in self.accts['S']:
            print(acct)
            total += acct.balance
        for acct in self.accts['B']:
            print(acct)
            total += acct.balance
        print(f'Combined Deposits: ${total}')

#Step 6: TEST setting up a Customer, adding accounts, and checking balances

bob = Customer('Bob',1)
bob.open_checking(321,555.55)
bob.get_total_deposits()
bob.open_savings(564,444.66)
nancy = Customer('Nancy',2)
nancy.open_business(2018,8900)
nancy.get_total_deposits()
'''
Wait! Why don't Nancy's combined deposits show a decimal?
This is easily fixed in the class definition (mostly copied from above, with a change made to 
the last line of code):
'''


class Customer:
    def __init__(self, name, PIN):
        self.name = name
        self.PIN = PIN
        self.accts = {'C': [], 'S': [], 'B': []}

    def __str__(self):
        return self.name

    def open_checking(self, acct_nbr, opening_deposit):
        self.accts['C'].append(Checking(acct_nbr, opening_deposit))

    def open_savings(self, acct_nbr, opening_deposit):
        self.accts['S'].append(Savings(acct_nbr, opening_deposit))

    def open_business(self, acct_nbr, opening_deposit):
        self.accts['B'].append(Business(acct_nbr, opening_deposit))

    def get_total_deposits(self):
        total = 0
        for acct in self.accts['C']:
            print(acct)
            total += acct.balance
        for acct in self.accts['S']:
            print(acct)
            total += acct.balance
        for acct in self.accts['B']:
            print(acct)
            total += acct.balance
        print(f'Combined Deposits: ${total:.2f}')  # added precision formatting here

#So it's fixed, right?
nancy.get_total_deposits()

'''
Nope! Changes made to the class definition do not affect objects created under different sets of instructions.
To fix Nancy's account, we have to build her record from scratch.
'''
nancy = Customer('Nancy',2)
nancy.open_business(2018,8900)
nancy.get_total_deposits()

'''
Step 7: Let's write some functions for making deposits and withdrawals.
Be sure to include a docstring that explains what's expected by the function!
'''
def make_dep(cust,acct_type,acct_num,dep_amt):
    """
    make_dep(cust, acct_type, acct_num, dep_amt)
    cust      = variable name (Customer record/ID)
    acct_type = string 'C' 'S' or 'B'
    acct_num  = integer
    dep_amt   = integer
    """
    for acct in cust.accts[acct_type]:
        if acct.acct_nbr == acct_num:
            acct.deposit(dep_amt)

make_dep(nancy,'B',2018,67.45)
nancy.get_total_deposits()


class Account:
    def __init__(self, acct_nbr, opening_deposit):
        self.acct_nbr = acct_nbr
        self.balance = opening_deposit

    def __str__(self):
        return f'${self.balance:.2f}'

    def deposit(self, dep_amt):
        self.balance += dep_amt

    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
        else:
            print('Funds Unavailable')  # changed "return" to "print"


class Checking(Account):
    def __init__(self, acct_nbr, opening_deposit):
        super().__init__(acct_nbr, opening_deposit)

    def __str__(self):
        return f'Checking Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'


class Savings(Account):
    def __init__(self, acct_nbr, opening_deposit):
        super().__init__(acct_nbr, opening_deposit)

    def __str__(self):
        return f'Savings Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'


class Business(Account):
    def __init__(self, acct_nbr, opening_deposit):
        super().__init__(acct_nbr, opening_deposit)

    def __str__(self):
        return f'Business Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'