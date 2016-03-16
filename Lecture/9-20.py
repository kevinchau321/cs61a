def trace1(f):
	def traced(x):
		print('Callling ', f, ' on argument ', x)
		return f(x)
	return traced
	
def gcd(m,n):
	"""return k where k is the largst number that divides m and n without remainder

	k, m, n are all positive integers
	>>>gcd(12,8)
	4
	>>>gcd(16,12)
	4
	"""
	if m % n == 0:
		return n 
	elif m < n:
		return gcd(n-m, m)
	else:
		return gcd(m-n, n)

@trace1
def square(x):
	return x*x

@trace1
def sum_square_up_to(n):
	total, k = 0,1
	while k <= n:
		total, k = total + square(k), k + 1
	return total



