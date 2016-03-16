def make_withdraw(balance, password):
    """Return a password-protected withdraw function.
    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    p1 = ''
    p2 = ''
    p3 = ''
    incorrect_counter = 0
    def withdraw(amount, attempt):
        nonlocal balance, p1, p2, p3, incorrect_counter
        if incorrect_counter == 3:
            return "Your account is locked. Attempts: ['"+str(p1)+"', '"+str(p2)+"', '"+str(p3)+"']"
        if attempt == password:
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount
            return balance
        if incorrect_counter == 0:
            p1 = attempt
            incorrect_counter += 1
            return 'Incorrect password'
        if incorrect_counter == 1:
            p2 = attempt
            incorrect_counter += 1
            return 'Incorrect password'
        if incorrect_counter == 2:
            p3 = attempt
            incorrect_counter += 1
            return 'Incorrect password'
    return withdraw