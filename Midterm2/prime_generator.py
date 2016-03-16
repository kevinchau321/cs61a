def make_prime_generator():
	prime = 1
	def prime_generator():
		nonlocal prime
		prime += 1
		def is_prime(n):
			for i in range(2,n):
				if n % i == 0:
					return False
			return True
		if prime == 2:
			return 2
		while not is_prime(prime):
			prime += 1
		return prime
	return prime_generator

