# Problem 1

def union(s1, s2):
    """Returns the union of two sets.

    >>> r = {0, 6, 6}
    >>> s = {1, 2, 3, 4}
    >>> t = union(s, {1, 6})
    >>> t
    {1, 2, 3, 4, 6}
    >>> union(r, t)
    {0, 1, 2, 3, 4, 6}
    """
    union = set()
    for el in s1:
        union.add(el)
    for el in s2:
        union.add(el)
    return union

# Problem 2

def intersection(s1, s2):
    """Returns the intersection of two sets.

    >>> r = {0, 1, 4, 0}
    >>> s = {1, 2, 3, 4}
    >>> t = intersection(s, {3, 4, 2})
    >>> t
    {2, 3, 4}
    >>> intersection(r, t)
    {4}
    """
    i = set()
    for el in s1:
        if el in s2:
            i.add(el)
    return i     
    

# Problem 3

def extra_elem(a,b):
    """B contains every element in A, and has one additional member, find
    the additional member.

    >>> extra_elem(['dog', 'cat', 'monkey'],  ['dog',  'cat',  'monkey',  'giraffe'])
    'giraffe'
    >>> extra_elem([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6])
    6
    """
    return list(set(b)-set(a))[0]

# Problem 4

def add_up(n, lst):
    """Returns True if any two non identical elements in lst add up to any n.

    >>> add_up(100, [1, 2, 3, 4, 5])
    False
    >>> add_up(7, [1, 2, 3, 4, 2])
    True
    >>> add_up(10, [5, 5])
    False
    """
    for el in lst:
        if n - el in lst and n-el != el:
            return True
    return False

# Problem 5

def find_duplicates(lst):
    """Returns True if lst has any duplicates and False if it does not.

    >>> find_duplicates([1, 2, 3, 4, 5])
    False
    >>> find_duplicates([1, 2, 3, 4, 2])
    True
    """
    return len(set(lst)) != len(lst)

# Problem 6

def find_duplicates_k(k, lst):
    """Returns True if there are any duplicates in lst that are within k
    indices apart.

    >>> find_duplicates_k(3, [1, 2, 3, 4, 1])
    False
    >>> find_duplicates_k(4, [1, 2, 3, 4, 1])
    True
    """
    prev_set = set()
    for i, elem in enumerate(lst):
        if elem in prev_set:
            return True
        prev_set.add(elem)
        if i - k >= 0:
            prev_set.remove(lst[i - k])
    return False
# Problem 7

def pow(n,k):
    """Computes n^k.

    >>> pow(2, 3)
    8
    >>> pow(4, 2)
    16
    """
    if k == 0:
        return 1
    if k == 1:
        return n
    if k % 2 == 0:
        return pow(n, k // 2)**2
    return n*pow(n, k -1)

# Problem 8

def missing_no(lst):
    """lst contains all the numbers from 1 to n for some n except some
    number k. Find k.

    >>> missing_no([1, 0, 4, 5, 7, 9, 2, 6, 3])
    8
    >>> missing_no(list(filter(lambda x: x != 293, list(range(2000)))))
    293
    """
    n = max(lst)
    return list(set(range(1,n)) - set(lst))[0]
