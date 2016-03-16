def count_while(s, value):
	"""Return the number of times value appears in the sequence"""
	total, index = 0, 0
	while index < len(s):
		if getitem(s, index) == value:
			total = total + 1
		index = index + 1
	return total

def count(s, value):
	total = 0
	for element in s:
		if element == value:
			total = total + 1
	return total

pairs = ((1,2),(3,3),(5,5), (5,2))

def count_same(pairs):
	total = 0
	for x,y in pairs:
		if x == y:
			total = total + 1
	return total


suits = ['coin', 'string', 'myriad']
