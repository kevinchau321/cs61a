def has_seven(k):
    """Has a has_seven
    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k % 10 == 7:
        return True
    if ((k//10)==0) and (k != 7):
        return False
    return has_seven(k//10)

# Q3.


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(100)
    2
    """
    def is_seven(n):
        if n % 7 == 0 or has_seven(n):
            return True
        return False
    def isUp(a):
        if a <= 7:
            return True
        if is_seven(a-1):
            return (not isUp(a-1))
        else:
            return isUp(a-1)
    if n <=7:
        return n
    if isUp(n):
        return pingpong(n-1) + 1
    return pingpong(n-1) - 1