# Name: Kevin Chau
# Email: kevinchau321@berkeley.edu

# Q1.

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n <= 3:
        return n
    return g(n-1)+2*g(n-2)+3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    k = 1
    a, b , c = 1,2,3
    while k < n:
        a, b, c = b, c, (3*a) + (2*b) +c
        k = k+1
    return a

# Q2.

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
    if k // 10 == 0 and k != 7:
        return False
    return has_seven(k//10)

# Q3.

"1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6"


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -15
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(100)
    2
    """
    if n == 0:
        return 0 
    if (n-1) % 7 == 0 or has_seven(n-1):
        if pingpong(n-1) - pingpong(n-2) == 1:
            return pingpong(n-1) -1
        return pingpong(n-1) + 1
    if pingpong(n-1) - pingpong(n-2) == 1:
        return pingpong(n-1) +1
    return pingpong(n-1) - 1

def pingpong_iter(n):
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
    def switch_direction(switch_index):
        if (switch_index + 1) % 2 ==0:
            return (-1)
        return 1 
    total = 1
    k = 1
    switch_index = 0
    while k < n:
        if k % 7 == 0 or has_seven(k):
            switch_index=switch_index + 1
        total = total + switch_direction(switch_index)
        k = k + 1
    return total
