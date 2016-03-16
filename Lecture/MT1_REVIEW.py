def silly(name):
	def fun():
		print('first')
		return name(y)
	print('second')
	return fun
def bop(y):
	return y // 10 + 1

y = 34
reserve = silly(bop)