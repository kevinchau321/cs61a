"""
class <name:
	<suite>

class statement creates a new class and bind thats class to <name>
suite creates attributes of the class

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
		if amount > self.baance:
			return 'Insufficient funds'
		self.balance = self.balance - amount
		return self.balance
	def megamillions(self):
		self.balance = self.balance + 1000000
		return self.balance
	def bankrupt(self):
		self.balance = 0
		return self.balance

getattr(account, 'balance')
hasaatr(account, 'balance')

tom_account= Account('tom')

Account.deposit(tom_account, 1001)
tom_account.deposit(1001)