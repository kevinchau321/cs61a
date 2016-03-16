def triangular(x, y, z):
    """Return whether x, y, and z are triangular.

    >>> triangular(3, 4, 5)
    True
    >>> triangular(3, 14, 5) # 14 is greater than 3 + 5
    False
    >>> triangular(7.5, 3.5, 4) # 7.5 is equal to 3.5 + 4
    False
    >>> result = triangular(5, 4, 3) # Return, don't print
    >>> result
    True
    """
    if x < (y + z):
        if y < (x + z):
            if z < (y + x):
                return True
            else:
                return False
        else: 
            return False
    else:
        return False
