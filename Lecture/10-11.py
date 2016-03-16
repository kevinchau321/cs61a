"""
Assignment statements with a dot expression on their lef-hand side affect attributes for the object of that dot expression
If the object is an instance, then assignment sets an instance attributes
If the object is a class, then assignment sets a class attribute
"""

class Account:
	interest = .02
	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder
	def deposit(self, amount):
		self.balance = self.balance + amount
		return self.balance
	def deposit2(self, amount):
		return self.withdraw(-amount)
	def withdraw(self, amount):
		if amount > self.balance:
			return 'Insufficient funds'
		self.balance = self.balance - amount
		return self.balance
	def megamillions(self):
		self.balance = self.balance + 1000000
		return self.balance
	def bankrupt(self):
		self.balance = 0
		return self.balance
"""
getattr(account, 'balance')
hasaatr(account, 'balance')
"""

tom_account= Account('tom')

"""
Account.deposit(tom_account, 1001)
tom_account.deposit(1001)
"""
"""
>>>tom_account.interest
.02
>>>Account.interest=.04
>>>tom_account.interest
.04
>>>jim_account.interest = 0.08
>>>jim_account.interest
.08
>>>tom_account.interest
.04
>>>tom_account.interest= .05
>>>tom_account.interest
.05
>>>jim.account.interest
.08
"""

"""
Inheritance:

class <name>(<base class>)
	<suite>
"""
"""
>>> ch.interest
.01
>>>ch.deposit(20)
20
>>>ch.withdraw(5)
14
"""
class CheckingAccount(Account):
	withdraw_fee=1
	interest = .01
	def withdraw(self, amount):
		return Account.withdraw(self, amount + self.withdraw_fee)

ch = CheckingAccount('tom')

class Bank:
	"""A bank has accounts.
	>>>bank = Bank()
	>>>john = bank.open_account('John', 10)
	>>>jack = bank.open_account('Jack', 5, CheckingAccount)
	>>>john.interest
	.02
	>>>jack.interest
	.01
	>>>bank.pay_interest()
	>>>john.balance 
	10.2
	>>>jack.balance
	5.05
	"""
	def __init__(self):
		self.accounts = []
	def open_account(self, holder, amount, kind=Account)
		account = kind(holder)
		account.depot(amount)
		self.accounts.append(account)
		return account
	def pay_interst(self):
		for a in self.accounts:
			a.deposit(a.balance*a.interst)

class SavingsAccount(Account):
	deposit_fee = 2
	def deposit(self, amount):
		return Account.deposit(self, amount - self.deposit_fee)

class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
	def __init__(self, account_holder):
		self.holder = account_holder
		self.balance = 1 ###free dollar when you open account





