def append_rlist_iter(a,b):
	if a is Rlist.empty:
		return b
	if b is Rlist.empty:
		return a
	lst = []
	for index in range(a.__len__ - 1):
		lst.append(a[index])
	rlist = Rlist(lst.pop)
	for index in range(b.__len__ - 1):
		lst.append(b[index])
	for el in lst:



def append_rlist_iter(a,b):
	result = Rlist.empty
	final_result = result
	if a is not Rlist.empty:
		result = Rlist(a.first)
		a = a.rest
		while a is not Rlist.empty:
			rlist.first = 



class Rlist:
        """A recursive list consisting of a first element and the rest."""
        class EmptyList(object):
            def __len__(self):
                return 0
        empty = EmptyList()
        def __init__(self, first, rest=empty):
            self.first = first
            self.rest = rest
        def __getitem__(self, i):
            if i == 0:
                return self.first
            else:
                return self.rest[i-1]
        def __len__(self):
            return 1 + len(self.rest)