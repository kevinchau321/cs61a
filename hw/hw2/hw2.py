# Name: Kevin Chau 
# Email: kevinchau321@berkeley.edu


def square(x):
    """Return x squared."""
    return x * x

# Q1.

def product(n, term):
    """Return the product of the first n terms in a sequence.

    term -- a function that takes one argument

    >>> product(4, square)
    576
    """
    total, k = 1, 1 #multiplicative identity is 1; so we want our accumulation to start at 1
    while k <=n: 
        total, k = total * term(k), k+1
    return total
    
def factorial(n):
    """Return n factorial for n >= 0 by calling product.

    >>> factorial(4)
    24
    """
    def identity(x): #for factorial, the term() function should not modify index k
        return x
    return product(n, identity)

# Q2.

def accumulate(combiner, start, n, term):
    """Return the result of combining the first n terms in a sequence."""
    total, k = start, 1 #start will be different when accumulating via multiplication versus addition
    while k <=n:
        total, k = combiner(total, term(k)), k+1
    return total


def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate.

    >>> summation_using_accumulate(4, square)
    30
    """
    from operator import add
    return accumulate(add, 0, n, term) #zero is the additive identity; accumulation starts at zero

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    """
    from operator import mul
    return accumulate(mul, 1, n, term)

# Q3.

def double(f):
    """Return a function that applies f twice.

    f -- a function that takes one argument

    >>> double(square)(2)
    16
    """
    def g(x):
        return f(f(x))
    return g



# Q4.

def repeated(f, n):
    """Return the function that computes the nth application of f.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    >>> repeated(square, 4)(5)
    152587890625
    """
    k = 1 #index starts at 1
    g = f #g is our total composition thus far, so it starts as f
    while k < n:
        g = compose1(f, g) #iteratively composes f(f(......))
        k = k+1
    return g
        
def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h