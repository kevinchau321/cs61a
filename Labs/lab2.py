def factors(n):
	i = n
	while i >= 1:
		if n % i == 0:
				print(i)
		i -=1

def divide(num, divisor):
	k = 0
	while num > 0:
		num = num - divisor
		k = k+1
	if num < 0:
		k = k - 1
	return k

def cycle(f1, f2, f3):
	"""Returns a function that is itself a higher orer fuction
	>>> def add1(x):
			return x + 1

	>>> def times2(x):
			return x * 2

	>>> def add3(x):
			return x + 3

	>>> my_cycle = cycle(add1, times2, add3)
	>>> identity = my_cycle(0)



