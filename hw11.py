# Name: Chia-Hao Chiao
# Login: cs61a-xi
# TA: Soumya Basu
# Section: 021

BRACKETS = {('[', ']'): '+',
            ('(', ')'): '-',
            ('<', '>'): '*',
            ('{', '}'): '/'}
LEFT_RIGHT = {left:right for left, right in BRACKETS.keys()}
ALL_BRACKETS = set(b for bs in BRACKETS for b in bs)

# Q1.

def tokenize(line):
    """Convert a string into a list of tokens.

    >>> tokenize('<[2{12.5 6.0}](3 -4 5)>')
    ['<', '[', 2, '{', 12.5, 6.0, '}', ']', '(', 3, -4, 5, ')', '>']

    >>> tokenize('2.3.4')
    Traceback (most recent call last):
        ...
    ValueError: invalid token 2.3.4

    >>> tokenize('?')
    Traceback (most recent call last):
        ...
    ValueError: invalid token ?

    >>> tokenize('hello')
    Traceback (most recent call last):
        ...
    ValueError: invalid token hello

    >>> tokenize('<(GO BEARS)>')
    Traceback (most recent call last):
        ...
    ValueError: invalid token GO
    """
    "*** YOUR CODE HERE ***"
    result = []
    if len(line) == 0:
        return list(line)
    if coerce_to_number(line) != None:
        result.append(line)
        return result
    if line[0] not in ALL_BRACKETS:
        raise ValueError('invalid token {0}'.format(line))
    for i in range(len(line)):
        if line[i] in ALL_BRACKETS:
            result.append(line[i])
        if (line[i-1] in ALL_BRACKETS or line[i-1] == ' ') and (line[i] not in ALL_BRACKETS and line[i] != ' '):
            r = i   
        if i < len(line)-1 and (line[i+1] in ALL_BRACKETS or line[i+1] == ' ') and (line[i] not in ALL_BRACKETS and line[i] != ' '):
            num = line[r:(i+1)]
            if coerce_to_number(num) == None:
                raise ValueError('invalid token {0}'.format(num))
            result.append(coerce_to_number(num))
    return result

def coerce_to_number(token):
    """Coerce a string to a number or return None.

    >>> coerce_to_number('-2.3')
    -2.3
    >>> print(coerce_to_number('('))
    None
    """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return None

# Q2.

def isvalid(tokens):
    """Return whether some prefix of tokens represent a valid Brackulator
    expression. Tokens in that expression are removed from tokens as a side
    effect.

    >>> isvalid(tokenize('([])'))
    True
    >>> isvalid(tokenize('([]')) # Missing right bracket
    False
    >>> isvalid(tokenize('[)]')) # Extra right bracket
    False
    >>> isvalid(tokenize('([)]')) # Improper nesting
    False
    >>> isvalid(tokenize('')) # No expression
    False
    >>> isvalid(tokenize('100'))
    True
    >>> isvalid(tokenize('<(( [{}] [{}] ))>'))
    True
    >>> isvalid(tokenize('<[2{12 6}](3 4 5)>'))
    True
    >>> isvalid(tokenize('()()')) # More than one expression is ok
    True
    >>> isvalid(tokenize('[])')) # Junk after a valid expression is ok
    True
    """
    "*** YOUR CODE HERE ***"
    if len(tokens) == 0:
        return False
    if len(tokens) == 1:
        if coerce_to_number(tokens[0]) != None:
            return True
        return False
    if tokens[0] not in LEFT_RIGHT:
        return False
    first, rest = list(tokens[0]), list(tokens[1:])
    def helper(lst1, lst2):
        if coerce_to_number(lst2[0]) != None:
            lst2.pop(0)
        elif lst2[0] in LEFT_RIGHT:
            lst1.append(lst2[0])
            lst2.pop(0)
        elif lst2[0] in ALL_BRACKETS and lst2[0] not in LEFT_RIGHT:
            if LEFT_RIGHT[lst1[-1]] == lst2[0]:
                if len(lst1) == 1:
                    return True
                lst1 = lst1[:-1]
                lst2 = lst2[1:]
                return isvalid(lst1+lst2)
            return False
        return helper(lst1, lst2)
    return helper(first, rest)

# Q3.

def brack_read(tokens):
    """Return an expression tree for the first well-formed Brackulator
    expression in tokens. Tokens in that expression are removed from tokens as
    a side effect.

    >>> brack_read(tokenize('100'))
    100
    >>> brack_read(tokenize('([])'))
    Pair('-', Pair(Pair('+', nil), nil))
    >>> print(brack_read(tokenize('<[2{12 6}](3 4 5)>')))
    (* (+ 2 (/ 12 6)) (- 3 4 5))
    >>> brack_read(tokenize('(1)(1)')) # More than one expression is ok
    Pair('-', Pair(1, nil))
    >>> brack_read(tokenize('[])')) # Junk after a valid expression is ok
    Pair('+', nil)

    >>> brack_read(tokenize('([]')) # Missing right bracket
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected end of line

    >>> brack_read(tokenize('[)]')) # Extra right bracket
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected )

    >>> brack_read(tokenize('([)]')) # Improper nesting
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected )

    >>> brack_read(tokenize('')) # No expression
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected end of line
    """
    "*** YOUR CODE HERE ***"
    def read_tail(tokens2):
        if len(tokens2) == 0:
            raise SyntaxError("unexpected end of line")
        if tokens2[0] in ALL_BRACKETS and tokens2[0] not in LEFT_RIGHT:
            if tokens2[0] == LEFT_RIGHT[brac]:
                tokens2.remove(tokens2[0])
                return nil
            raise SyntaxError("unexpected {0}".format(tokens2[0]))
        first = brack_read(tokens2)
        rest = read_tail(tokens2)
        return Pair(first, rest)

    if len(tokens) == 0:
        raise SyntaxError("unexpected end of line")
    val = tokens[0]
    if val not in ALL_BRACKETS:
        tokens.remove(tokens[0])
        return coerce_to_number(val)
    elif val in LEFT_RIGHT:
        brac = tokens[0]
        tokens.remove(tokens[0])
        return Pair(BRACKETS[(val, LEFT_RIGHT[val])], read_tail(tokens))
    elif val in ALL_BRACKETS:
        raise SyntaxError("unexpected {0}".format(val))
    raise SyntaxError("unexpected {0}".format(val))



# Q4.

from urllib.request import urlopen

def puzzle_4():
    """Return the soluton to puzzle 4."""
    "*** YOUR CODE HERE ***"
    base = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    num = '12345'
    from urllib.request import urlopen
    while 1 > 0 and num != 16044:
        addr = base + str(num)
        contents = urlopen(addr).read().decode()
        num = [int(s) for s in contents.split() if s.isdigit()][0]
        print(num)
    num = 16044/2
    while 1 > 0 and num != 66831:
        addr = base + str(num)
        contents = urlopen(addr).read().decode()
        num = [int(s) for s in contents.split() if s.isdigit()][0]
        print(num)
    addr = base + '66831'
    contents = urlopen(addr).read().decode()
    return contents
    
    

class Pair(object):
    """A pair has two instance attributes: first and second.  For a Pair to be
    a well-formed list, second is either a well-formed list or nil.  Some
    methods only apply to well-formed lists.

    >>> s = Pair(1, Pair(2, nil))
    >>> s
    Pair(1, Pair(2, nil))
    >>> print(s)
    (1 2)
    >>> len(s)
    2
    >>> s[1]
    2
    >>> print(s.map(lambda x: x+4))
    (5 6)
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return "Pair({0}, {1})".format(repr(self.first), repr(self.second))

    def __str__(self):
        s = "(" + str(self.first)
        second = self.second
        while isinstance(second, Pair):
            s += " " + str(second.first)
            second = second.second
        if second is not nil:
            s += " . " + str(second)
        return s + ")"

    def __len__(self):
        n, second = 1, self.second
        while isinstance(second, Pair):
            n += 1
            second = second.second
        if second is not nil:
            raise TypeError("length attempted on improper list")
        return n

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        y = self
        for _ in range(k):
            if y.second is nil:
                raise IndexError("list index out of bounds")
            elif not isinstance(y.second, Pair):
                raise TypeError("ill-formed list")
            y = y.second
        return y.first

    def map(self, fn):
        """Return a Scheme list after mapping Python function FN to SELF."""
        mapped = fn(self.first)
        if self.second is nil or isinstance(self.second, Pair):
            return Pair(mapped, self.second.map(fn))
        else:
            raise TypeError("ill-formed list")

class nil(object):
    """The empty list"""

    def __repr__(self):
        return "nil"

    def __str__(self):
        return "()"

    def __len__(self):
        return 0

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        raise IndexError("list index out of bounds")

    def map(self, fn):
        return self

nil = nil() # Assignment hides the nil class; there is only one instance


def read_eval_print_loop():
    """Run a read-eval-print loop for the Brackulator language."""
    global Pair, nil
    from scheme_reader import Pair, nil
    from scalc import calc_eval

    while True:
        try:
            src = tokenize(input('> '))
            while len(src) > 0:
              expression = brack_read(src)
              print(calc_eval(expression))
        except (SyntaxError, ValueError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            return


