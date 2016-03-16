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

