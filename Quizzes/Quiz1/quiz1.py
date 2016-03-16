# Name: Kevin Chau 
# Email: kevinchau321@berkeley.edu

# Q1.

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

# Q2.

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

# Q3.

def digit_span(x):
    """Return the difference between x's largest and smallest digits.

    >>> digit_span(2013) # 3 - 0 = 3
    3
    >>> digit_span(75) # 7 - 5 = 2
    2
    >>> digit_span(2345678765432) # 8 - 2 = 6
    6
    >>> result = digit_span(6473465) # Return, don't print
    >>> result
    4
    """
    digits=[] #start with an empty list
    n = x
    k = 0
    while k < len(str(x)):
        k = k + 1 #increase the index
        d = n % 10 #extracts the right most digit
        n = n // 10 #extracts the rest of the digits
        digits.append(d) #adds the digit extracted to the list
    return max(digits) - min(digits)
