def next_square(x):
    """Return the smallest perfect square greater than x.

    >>> next_square(10)
    16
    >>> next_square(39)
    49
    >>> next_square(100)
    121
    >>> result = next_square(2) # Return, don't print
    >>> result
    4
    """
    i = 0
    k = 0
    while k <= x:
        i = i + 1
        k = i * i 
    return k



