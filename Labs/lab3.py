def sum(n):
	if n == 0:
		return 0
	return n + sum(n-1)

def ab_plus_c(a,b,c):
	if a == 1:
		return b + c
	return ab_plus_c(a-1, b, c) + b 

def summation(n, term):
	if n == 0:
		return 0
	return summation(n-1, term)+term(n)

def square(x):
	return x*x

k = 0
def hailstone_recursive(n):
	global k
	if n == 1:
		print(1)
		num_steps= k
		k = 0
		return num_steps
	else:
		print(n)
		if n % 2 == 0: #n is even
			k = k + 1
			return hailstone_recursive(n // 2)
		else: 
			k = k + 1
			return hailstone_recursive(3*n+1)

def compose1(f, g):
	def h(x):
		return f(g(x))
	return h

def repeated_recursive(f, n):
	if n <= 2:
		return compose1(f, f)
	return compose1(f, repeated_recursive(f, n-1))

#f		a variable who



def falling(n, k):
	total = 1
	n += 1
	while k > 0:
		k = k -1
		n = n - 1
		total = total * n 
	return total

def make_deriv(f):
	def discrete_deriv(n):
		return f(n+1)-f(n)
	return discrete_deriv

def make_product(f,g):
	def discrete_product_deriv(n):
		return make_deriv(f)(n)*g(n+1)+make_deriv(g)(n)*f(n)
	return discrete_product_deriv

f = lambda


