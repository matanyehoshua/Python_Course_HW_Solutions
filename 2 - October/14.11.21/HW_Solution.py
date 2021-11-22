# HW_Solution 14.11.21
# copied from HW_Solution from 17.11.21

import shelve

class BankAccount:
    def __init__(self, account_id=0, full_name_owner=None, balance=0):
        self.account_id = account_id
        self.full_name_owner = full_name_owner
        self.balance = balance

    def __str__(self):
        return f'Bank Account account_id={self.account_id}, ' \
               f'full_name_owner={self.full_name_owner},' \
               f' balance={self.balance}'

    def __repr__(self):
        return f'BankAccount(account_id={self.account_id}, ' \
               f'full_name_owner={self.full_name_owner},' \
               f' balance={self.balance})'

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.balance == other.balance
        elif type(other) in [int, float]:
            return self.account_id == other
        else:
            # throw Error
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, BankAccount):
            return self.balance > other.balance
        elif type(other) in [int, float]:
            return self.account_id > other
        else:
            # throw Error
            return False

    def __lt__(self, other):
        if isinstance(other, BankAccount):
            return self.balance < other.balance
        elif type(other) in [int, float]:
            return self.account_id < other
        else:
            # throw Error
            return False

    def __add__(self, other):
        self.balance += other
        return self

    def __sub__(self, other):
        self.balance -= other
        return self

    def __mul__(self, other):
        self.balance *= other
        return self

sh = shelve.open('bank_listings.db')
b1 = BankAccount(1, 'user1', 1_000_000)
b2 = BankAccount(2, 'user2', 1_000_000)
b3 = BankAccount(3, 'user3', 2_500_000)
sh[str(b1.account_id)] = b1.__dict__
sh[str(b2.account_id)] = b2.__dict__
sh[str(b3.account_id)] = b3.__dict__
account_id = input('please enter account id: ')
if account_id in sh.keys():
    b = BankAccount()
    b.__dict__ = sh[account_id]
    print(b)
sh.close()
print('same balance', b1 == b2)
if b1 == 1:
    print('b1 account_id is equal to 1')
b1 = b1 + 100
print('b1 + 100', b1)
b1 = b1 * 2
print('b1 * 2', b1)
# not support:
# b1 = b1 + b2