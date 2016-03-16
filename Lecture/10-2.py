first_part = 'lambda f:'
second_part = 'lambda x: lambda y: f(x,y)'
first_part+second_part
curry = eval(first_part+ second_part)
#curry(add)(3)(4)

#elookup('SNOWMAN')

"""
byte is 8 bits and can encode any integer 0-255
"""

#### mapping
alternates = -1, 2, -3, 4, -5
tuple(map(abs, alternates))

def fib(k):
	if k == 1:
		return 0
	previous, current = 0, 1
	for _ in range(k-2):
		previous, current = current, previous + current
	return current

def even(n):
	return n % 2 == 0

def sum_even_fibs(n):
	return sum(filter(even, map(fib, range(1, n+1))))
