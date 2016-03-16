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
    if ((k//10)==0) and (k != 7):
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

# Q4.

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    if n % 10 + n // 10 == 10 and n!=100: ##base case, two digits
        return 1
    if n < 100:
        return 0
    def ten_pairs_added(n, k):
        if n == 10 - k:
            return 1
        if n // 10 == 0:
            return 0
        if n%10 + k ==10:
            return ten_pairs_added(n//10, k) + 1
        return ten_pairs_added(n//10, k)
    return ten_pairs(n // 10) + ten_pairs_added(n//10, n % 10)
    


# Q5.

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def count_partitions(n, maxcoin):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif max_exp == 0:
            return 0
        else:
            with_m = count_partitions(n-pow(2, max_exp), pow(2,max_exp)) 
            without_m = count_partitions(n,pow(2, max_exp - 1))
            return with_m + without_m
    def make_coin_set(amount):
        k=0
        coins=[]
        while pow(2, k) < n:
            coins.append(pow(2,k))
        return coins
    def max_coin_exp(n):
        k = 0
        while pow(2, k) < n:
            k = k + 1
        return k - 1
    return count_partitions(amount, pow(2,max_coin_exp(amount))

# Q6.

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return YOUR_EXPRESSION_HERE


