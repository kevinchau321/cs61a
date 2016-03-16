def fib_recur(n):
	if n <=2:
		return n 
	return fib_recur(n-1)+ fib_recur(n-2)

def fib_iter(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
	return a



		


