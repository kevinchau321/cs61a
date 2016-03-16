# Kevin Chau
# 23816929
# Q1.

from operator import add, sub
def a_plus_abs_b(a, b):
	"""Return a+abs(b), but without calling abs.
	>>> a_plus_abs_b(2, 3)
	5
	>>> a_plus_abs_b(2, -3)
	5
	"""
	if b < 0:
		op = sub
	else:
		op = add
	return op(a, b)
from doctest import run_docstring_examples
run_docstring_examples(a_plus_abs_b, globals(), True)

# Q2.

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest of a, b, c.
    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a*a+b*b+c*c-min(a,b,c)*min(a,b,c)
from doctest import run_docstring_examples
run_docstring_examples(two_of_three, globals(), True)

# Q3.

def if_function(condition, true_result, false_result):
	"""return true_result if condition is a true value, and false_result otherwise."""
	if condition:
		return true_result
	else:
		return false_result
def with_if_statement():
	"""
	>>> with_if_statement()
	1
	"""
	if c():
		return t()
	else:
		return f()
def with_if_function():
	return if_function(c(), t(), f())
def c():
	return 1
def t():
	return 1
def f():
	return 1/0

from doctest import run_docstring_examples
run_docstring_examples(with_if_statement, globals(), True)

# Q4.

def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.
    >>> a = hailstone(10)  # Seven elements are 10, 5, 16, 8, 4, 2, 1
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    from operator import mod
    k=1 #index starts at 1
    print(n)
    while n != 1:
    	if mod(n, 2) == 0: #even number
    		n = n/2
    		k = k + 1 #add 1 to index, increase number of terms in sequence
    		print(n)
    	else: #odd number
    		n = 3*n+1
    		k = k + 1
    		print(n)
    return k #return value of hailstone(n)
from doctest import run_docstring_examples
run_docstring_examples(hailstone, globals(), True)
