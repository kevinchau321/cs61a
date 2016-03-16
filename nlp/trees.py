class Tokenizer:
    """An iterator over the tokens of a Treebank."""
    def __init__(self, input):
        self.input = input
        self.line = []

    def __next__(self):
        """Return the next token."""
        while self.line == []:
            s = self.input.readline()
            if s == '':
                raise StopIteration
            self.line = s.replace('(', ' ( ').replace(')', ' ) ').split()
        return self.line.pop(0)

def read_trees(input):
    """Yield trees in a file."""
    tokens = Tokenizer(input)
    while True:
        assert next(tokens) == '('
        assert next(tokens) == '('
        tree = read_tree(tokens)
        yield Tree('ROOT', [START, tree, END])
        assert next(tokens) == ')'

def read_tree(tokens):
    """Read the next well-formed tree, removing empty constituents."""
    tag = next(tokens).split('-')[0].split('=')[0].split('|')[0]
    element = next(tokens)
    if element != '(':
        assert next(tokens) == ')'
        return Leaf(tag, element)
    branches = []
    while element != ')':
        assert element == '('
        branch = read_tree(tokens)
        if branch.tag:
            branches.append(branch)
        element = next(tokens)
    return Tree(tag, branches)

class Leaf:
    """A word tagged with a syntactic category."""
    def __init__(self, tag, word):
        self.tag = tag
        self.word = word

    def __str__(self):
        return '({0} {1})'.format(self.tag, self.word)

    def __repr__(self):
        return '<' + str(self) + '>'

START = Leaf('<S>', '<s>')
END = Leaf('</S>', '</s>')

class Tree:
    """A syntactic constituent."""
    def __init__(self, tag, branches):
        self.tag = tag
        self.branches = branches

    def __str__(self):
        branch_strings = ' '.join(str(b) for b in self.branches)
        return '({0} {1})'.format(self.tag, branch_strings)

    def __repr__(self):
        return '<' + str(self) + '>'
