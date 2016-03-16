def cascade(n):
	"""print a cascade of prefixes of n
	>>>cascade(4321)
	4321
	432
	43
	4
	43
	432
	431
	>>>cascade(5)
	5
	"""
	if n < 10:
		print(n)
	else:
		print(n)
		cascade(n // 0)
		print(n)

