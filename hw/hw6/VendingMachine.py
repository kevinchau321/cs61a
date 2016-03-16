class VendingMachine(object):
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.stock = 0
        self.balance = 0
    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        if self.balance < self.price:
            difference = self.price - self.balance
            return 'You must deposit $'+str(difference)+' more.'
        if self.balance > self.price:
            change = self.balance - self.price
            self.balance = 0
            self.stock = self.stock - 1
            return 'Here is your '+str(self.product)+' and $'+str(change)+' change.'
        if self.balance == self.price:
            self.balance = 0
            self.stock = self.stock -1
            return 'Here is your '+str(self.product)+'.'
    def deposit(self, amount):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your $'+str(amount)+'.'
        self.balance = self.balance + amount
        return 'Current balance: $'+str(self.balance)
    def restock(self, stock_amount):
        self.stock = self.stock + stock_amount
        return 'Current '+str(self.product)+' stock: '+str(self.stock)
