from ucb import trace

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
	print(n)
	if n >= 10:
		cascade(n // 10)
		print(n)

###Tree Recursion: more than one call to a function
@trace
def fib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fib(n-2)+ fib(n-1)

def count_partitions(n, m)
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif m ==0:
		return 0 
	else:
		with_m = count_parttitions(n-m, m)
		without_m = count_partitions(n, m-1)
		return with_m + without_m

###hog winning
num_possible_rolls= pow(6, n)
###num_way_to_score_k: use Recursion
