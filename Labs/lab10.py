class AnIterator(object):
	def __init__(self):
		self.current = 0
	def __next__(self):
		if self.current > 5:
			raise StopIteration
		self.current += 1
		return self.current
	def __iter__(self):
		return self

class IteratorA(object):
	def __init__(self):
		self.start = 5
	def __next__(self):
		if self.start == 100:
			raise StopIteration
		self.start +=5
		return self.start
	def __iter__(self):
		return self

class IteratorB(object): ###No next implementation, will not iterate, iter will not return object with next method
	def __init__(self):
		self.start = 5
	def __iter__(self):
		return self

class IteratorC(object):
	def __init__(self):
		self.start = 5
	def __next__(self):
		if self.start == 10:
			raise StopIteration
		self.start += 1
		return self.start

class IteratorRestart(object):
	def __init__(self, start, end):
		self.start = start
		self.current = start
		self.end = end
	def __next__(self):
		if self.current > self.end:
			self.current == self.start
			raise StopIteration
		self.current += 1
		return self.current
	def __iter__(self):
		return self

class Str(object):
	def __init__(self, string):
		self.string = string
		self.index = -1
	def __next__(self):
		if self.index == len(self.string) - 1:
			raise StopIteration
		self.index += 1
		return self.string[self.index]
	def __iter__(self):
		return self

def generator_print():
    print("Starting here")  #before the first value is yielded,
    i = 0
    while i < 6:
        print("Before yield")
        yield i
        print("After yield") ##first thing printed after each next call
        i += 1

def countdown(n):
	i = 0
	while i <= n:
		yield n - i
		i += 1

class IterCountdown(object):
	def __init__(self, start):
		self.start = start
		self.index = 0
	def __iter__(self):
		while self.index <= self.start:
			yield self.start - self.index
			self.index += 1

def char_gen(string):
	i = 0
	while i < len(string):
		yield string[i]
		i += 1

def hailstone(n):
	current = n
	while current > 1:
		yield current
		if current % 2 == 0:
			current = current // 2
		else:
			current = (current * 3) + 1
	yield current
	
class Stream:
	class empty:
		def __repr__(self):
			return 'Stream.empty'
	empty = empty()

	def __init__(self, first, compute_rest=lambda: Stream.empty):
		assert callable(compute_rest), 'compute_rest must be callable.'
		self.first = first
		self._compute_rest = compute_rest

	@property
	def rest(self):
		if self._compute_rest is not None:
			self._rest= self._compute_rest()
			self._compute_rest = None
		return self._rest

	def __repr__(self):
		return 'Stream({0}, <...>)'.format(repr(self.first))


def make_integer_stream(first=1):
	def compute_rest():
		return make_integer_stream(first+1)
	return Stream(first, compute_rest)

def make_fib_stream():
	return fib_stream_generator(0,1)
def fib_stream_generator(a,b):
	def compute_rest():
		return fib_stream_generator(b, a+b)
	return Stream(a, compute_rest)


def sub_streams(s1, s2):
	def compute_rest():
		return sub_streams(s1.rest, s2.rest)
	return Stream(s1.first - s2.first, compute_rest)

def converges_to(s, target, max_diff=0.00001, num_values=100):
	count = 0
	deriv = sub_streams(s.rest, s)
	for i in range(num_values):
		if abs(s.first - target) <= max_diff and abs(deriv.first) < max_diff:
			count += 1
		else:
			count = 0
		if count == 10:
			return True
		deriv = deriv.rest
		s = s.rest
	return False

def stream_map(func, stream):
	def compute_rest():
		return stream_map(func, stream.rest)
	if stream.empty:
		return stream
	else:
		return Stream(func(stream.first), compute_rest)



















