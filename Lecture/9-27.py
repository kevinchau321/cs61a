"""
Sequence Abstraction
"""
odds = (41, 43, 47, 49)
"""
>>>len(odds)
4
>>>odds[1]
43
"""
"""
Recursive List Abstract Data Type
"""
def rlist(first, rest):
	return (first, rest)
def first(s):
	return s[0]
def rest(s):
	return s[1]

###########################################
### === +++ ABSTRACTION BARRIER +++ === ###
###########################################
empty_rlist = None
counts = rlist(1, rlist(2, rlist(3, rlist(4, empty_rlist))))
alts = relist(1, rlist(2, rlist(1, rlist(2, empty_rlist))))

both = rlist(counts, rlist(alts, empty_rlist))
"""
>>>first(rest(rest(first(both))))
3
"""
#the way to get to an element is always unique, though the element may not be unique itself

def len_rlist(s):
	length = 0
	while s != empty_rlist:
		s, length = rest(s), length + 1
	return length

def getitem_rlist(s, i):
	while i > 0:
		s, i = rest(s), i - 1
	return first(s)

def len_rec(s):
	if s == empty_rlist:
		return 0
	return len_rec(rest(s)) + 1
def getitem_rec(s, i):
	if i == 0:
		return first(s)
	return getitem_rec(rest(s), i - 1)

def reverse(s):
	"""return s in reverse
	>>>rev = rlist(4, rllist(3, rlist(2, rlist(1, empty_rlist)))
	>>>rev == reverse(count)
	True
	"""
	return reverse_to(s, empty_rlist)
	
def reverse_to(s, result):
	"""return reverse of s followed by result
	"""
	if s == empty_rlist:
		return result
	else:
		return reverse_to(rest(s), rlist(first(s), result))