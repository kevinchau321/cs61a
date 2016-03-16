# Name: Kevin Chau
# Email: kevinchau321@berkeley.edu


def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))


# Q1.

def interval(a, b):
    """Construct an interval from a to b."""
    return (a,b)


def lower_bound(x):
    """Return the lower bound of interval x."""
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    return x[1]

# Q2.

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    "*** YOUR CODE HERE ***"
    assert (not(lower_bound(y) <= 0 and upper_bound(y) >= 0)), "interval y contains 0"
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

# Q3.

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    lowest = lower_bound(x) - upper_bound(y)
    highest = upper_bound(x) - lower_bound(y)
    return interval(lowest, highest)


# Q4.

def mul_interval_fast(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y, using as few multiplications as possible.

    >>> str_interval(mul_interval_fast(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    >>> str_interval(mul_interval_fast(interval(-2, -1), interval(4, 8)))
    '-16 to -4'
    >>> str_interval(mul_interval_fast(interval(-1, 3), interval(-4, 8)))
    '-12 to 24'
    >>> str_interval(mul_interval_fast(interval(-1, 2), interval(-8, 4)))
    '-16 to 8'
    """
    if lower_bound(x) > 0 and upper_bound(x) > 0:
        if lower_bound(y) > 0 and upper_bound(y) > 0:
            return interval(lower_bound(x)*lower_bound(y), upper_bound(y)*upper_bound(x))
        if lower_bound(y) < 0 and upper_bound(y) > 0:
            return interval(upper_bound(x)*lower_bound(y), upper_bound(x)*upper_bound(y))
        if lower_bound(y)>0 and lower_bound(y)>0:
            return interval(upper_bound(x)*upper_bound(y),lower_bound(x)*lower_bound(y))
    if lower_bound(x) < 0 and upper_bound(x)<0:
        if lower_bound(y)>0 and upper_bound(y)>0:
            return interval(lower_bound(x)*upper_bound(y),upper_bound(x)*lower_bound(y))
        if lower_bound(y)<0 and upper_bound(y)>0:
            return interval(upper_bound(x)*upperbound(y), upper_bound(x)*lower_bound(y))
        if lower_bound(y)<0 and upperbound(y)<0:
            return interval(lower_bound(x)*upper_bound(y), upper_bound(x)*upper_bound(y))
    if lower_bound(x)<0 and upper_bound(x)>0:
        if lower_bound(y)>0 and upper_bound(y)>0:
            return interval(lower_bound(x)*upper_bound(y), upper_bound(x)*upper_bound(y))
        if lower_bound(y)<0 and upper_bound(y)<0:
            return interval(upper_bound(x)*upper_bound(y), lower_bound(x)*upper_bound(y))
        if lower_bound(y)<0 and upper_bound(y)>0:
            return mul_interval(x,y)

# Q5.

def make_center_width(c, w):
    """Construct an interval from center and width."""
    return interval(c - w, c + w)

def center(x):
    """Return the center of interval x."""
    return (upper_bound(x) + lower_bound(x)) / 2

def width(x):
    """Return the width of interval x."""
    return (upper_bound(x) - lower_bound(x)) / 2


def make_center_percent(c, p):
    """Construct an interval from center and percentage tolerance.

    >>> str_interval(make_center_percent(2, 50))
    '1.0 to 3.0'
    """
    width = (p/100)*c
    return make_center_width(c, width)

def percent(x):
    """Return the percentage tolerance of interval x.

    >>> percent(interval(1, 3))
    50.0
    """
    return ((upper_bound(x)-center(x))/(center(x)))*100 

# Q6.

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))


# These two intervals give different results for parallel resistors:
a = make_center_percent(1,1) #interval (.99,1.01)
b = make_center_percent(1,1) #same interval as a.
print('par1 == par2 is ' + str(par1(a,b)==par2(a,b)))

# Q7.

def multiple_references_explanation():
    return """The mulitple reference problem: The user is correct that
the formula with the least occurances of a resistor interval (R1 or R2)
variable is the one which creates a narrower parallel resistance
interval. The narrower the interval, the more precise of a calculation
we have made since the percent width relative to the center is much
smaller. So the function par2 is more accurate than par1 for
calculating the parallel resistance since it calculates a narrower 
interval, despite having less floating points. For example, take 
intervals a and b which were specified in question 6 
(a=b=make_center_percent(1,1) ). 
par1(a,b) calculates to (0.4851980198019802, 0.5152020202020202) 
and par2(a,b) calculates to (0.495, 0.505). 
Despite par1 having more decimals, par2 is a narrower
interval and therefore is a more precise calculation. 
This will hold for any intervals a and b."""

# Q8.


def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    f_xmin= a*lower_bound(x)*lower_bound(x)+b*lower_bound(x)+c
    f_xmax= a*upper_bound(x)*upper_bound(x)+b*upper_bound(x)+c
    xcrit = (-b/(2*a))
    f_xcrit = a*xcrit*xcrit+b*xcrit+c 
    if xcrit<=upper_bound(x) and xcrit>=lower_bound(x):
        return interval(min(f_xmin, f_xmax, f_xcrit), max(f_xmin, f_xmax, f_xcrit))
    else:
        return interval(min(f_xmin,f_xmax), max(f_xmin, f_xmax))

# Q9.

def non_zero(x):
    """Return whether x contains 0."""
    return lower_bound(x) > 0 or upper_bound(x) < 0

def square_interval(x):
    """Return the interval that contains all squares of values in x, where x
    does not contain 0.
    """
    assert non_zero(x), 'square_interval is incorrect for x containing 0'
    return mul_interval(x, x)

# The first two of these intervals contain 0, but the third does not.
seq = (interval(-1, 2), make_center_width(-1, 2), make_center_percent(-1, 50))

zero = interval(0, 0)

def sum_nonzero_with_for(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using a for statement.

    >>> str_interval(sum_nonzero_with_for(seq))
    '0.25 to 2.25'
    """
    sum_seq = zero
    for interval in seq:
        if non_zero(interval):
            sum_seq=add_interval(sum_seq, square_interval(interval))
    return sum_seq


from functools import reduce
def sum_nonzero_with_map_filter_reduce(seq): 
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using map, filter, and reduce.

    >>> str_interval(sum_nonzero_with_map_filter_reduce(seq))
    '0.25 to 2.25'
    """
    return reduce(add_interval,(map(square_interval,filter(non_zero,seq))))

def sum_nonzero_with_generator_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using reduce and a generator expression.

    >>> str_interval(sum_nonzero_with_generator_reduce(seq))
    '0.25 to 2.25'
    """
    return reduce(add_interval, (square_interval(interval) for interval in seq if non_zero(interval)))