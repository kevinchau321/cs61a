def curry2(f):
	def g(x):
		def h(y):
			return f(x,y)
		return h
	return g

#Newton's Method
Given a function f and guess x:
	Repeatedly improve x:
		1. compute f(x)
		2. compute f'(x)
		3. x- f(x)/f'(x)



def square_root(a):
	x=1
	while x * x != a:
		print(x)
		x = (x+a/x)/2
	return x

def square_root_update(x, a):
	return (x+a/x)/2

def cube_root(a):
	x = 1
	while x*x*x != a:
		print(x)
		x= cube_root_update(x, a)
	return x

def cube_root_update(x, a):
	return (2*x +a/(x*x))/3

def approx_eq(x, y , tolerance=1e-15):
	return abs (x-y) < tolerance

def improve(update, close, guess=1):
	while not close(guess):
		guess = update(guess)
	return guess

def square_root(a):
	def update(x):
		return square_root_update(x, a)
	def close(x):
		return approx_eq(x*x, a)
	return improve(update, close)

def cube_root(a):
	return improve(lambda x: cube_root_update(x, a))






def find_zero(f, df):
	def near_zero(x):
		approx_eq(f(x), a)
	return improve(newton_update(f, df), near_zero)

def netwon_update(f, df):
	def update(x):
		return x - f(x)/ df(x)
	return update

def square_root(a):
	def f(x):
		return x*x-a
	def df(x):
		return 2*x
	return find_zero(f,df)

def cube_root(a):
	return find_zero(lamda x: x*x*x-a, lambda x: 3*x*x)


def power(x, n):
	product, k = 1, 0
	while k< x:
		product, k = product * x, k + 1
	return product

def root(n,a):
	def f(x):
		return power(x, n) - a
	def df(x):
		return n*power(x, n-1)
	return find_zero(f, df)


