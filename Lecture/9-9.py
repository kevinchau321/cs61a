def fib(n):
	"""compute nth fibonacci number"""
	predecessor, current = 0, 1 #first two fibonacci numbers
	k = 2 # tracks which fibonacci number is called current
	while k < n:
		predecessory, current = current, predecessor + current
		k = k + 1
	return current


def choose(total, selection):
	"""Return the number of ways to choose selection items from total.
	choose(n, k) is defined in math as: n! / (n-k)! / k!
	>>>choose(n,k)
	10
	>>>choose(20,6)
	38760
	"""
	ways = 1
	selected = 0
	while selected < selection
		selected = selected + 1
		ways, total = ways * total//selected, total - 1
	return ways

"""
	domain= set of all inputs
	range = set of all outputs
	behavior= relationship created between i/o
	GIVE EACH FUNCTION EXACTLY ONE JOB
"""

#default parameters
def after_tax(price, sales_tax=.09)
	"""Return the after tax price"""
	>>>after_tax(2, 0.1)
	2.2
	>>>after_tax(5)
	5.45
	"""
	return price * (1 + sales_tax)

#generalizations
from math import pi, sqrt
def area(r, shape_constant):
		assert r > 0, 'A length must be positive'
		return r * r * shape_constant
def area_square(r):
		return area(r,1)
def area_circle(r):
		return area(r, pi)
def area_hexagon(r):
		return area(r, 3*sqrt(3)/2)

#assert statement
"""
>>>assert 2 > 3, 'I said 2 is bigger' #returns string when assert is false
AssertionError: I said 2 is bigger
"""
#Higher Order Functions
def identity(k):
	return k

def cube(k):
	return pow(k, 3)

def sum_naturals(n):
		"""sum the first N natural numbers.
		>>> sum_naturals(5)
		15
		"""
		total, k = 0, 1
		while k<=n:
			total,  k = total +k, k+1
		return total

def sum_cubes(n):
	"""
	>>> sum_cubes(5)
	225
	"""
	total, k = 0, 1
	while k<=n:
		total, k= total+pow(k,3), k+1
	return total

def summation(n, term):
	"""Sum the first N terms of a sequence
	>>> summation(5, cube)
	225
	>>>summation(100000, pi_term)
	3.14
	"""
	total, k = 0, 1
	while k<=n:
		total, k = total + term(k), k+1
	return total
def pi_term(k):
	return 8 / mul(4*k-3, 4*k-1)

#functions as Return Values
def make_adder(n):
	"""return a function that takes an argument K and returns K + N
	>>> add_three = make_adder(3)
	>>>add_three(4)
	7
	>>>add_three(2010)
	2013
	"""
	def adder(k)
		return k + n
	return adder8




