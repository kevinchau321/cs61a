def memo(f):
	cache = {}
	def memoized(n):
		if n not in cache:
			cache[n]=f(n)
		return cache[n]
	return memoized

@memo
def fib(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	return fib(n-2) + fib(n-1)