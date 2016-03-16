class Bank:
    def __init__(self, name):
        self.name = name
        self.__balance = 0

    def deposit(self, amount):
        assert isinstance(amount, int) or isinstance(amount, float), 'amount should be a number'
        assert amount >= 0, 'amount should be non-negative'
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        assert isinstance(amount, int) or isinstance(amount, float), 'amount should be a number'
        assert amount >= 0, 'amount should be non-negative'
        self.__balance = self.__balance - amount
    @property
    def balance(self):
        return self.__balance
