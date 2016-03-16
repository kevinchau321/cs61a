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
    
def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    def joint_withdraw(amount,attempt):
        if attempt == new_password:
            return withdraw(amount, old_password)
        return withdraw(amount, attempt)
    return joint_withdraw