#!/usr/bin/env python3

"""Transform sentences to sound like Yoda."""

import sys
from parse import load_grammar, load_lexicon, parse
from ucb import main
from words import words
from trees import Tree, Leaf

def extract_modal(t):
    """Delete the first clause of a modal verb and return it."""
    if type(t) == Leaf:
        return None
    if len(t.branches) == 2 and t.branches[0].tag == 'MD':
        modal, clause = t.branches
        t.branches = [modal]
        return clause
    for b in t.branches:
        clause = extract_modal(b)
        if clause is not None:
            return clause
    return None

def yoda_transform(t):
    """Place the clause of a modal verb at the front of the sentence."""
    clause = extract_modal(t)
    if clause is not None:
        return Tree(t.tag, (clause, Leaf(',', ',')) + t.branches)
    return t

@main
def run(grammar_file="grammar.txt", lexicon_file="lexicon.txt"):
    print('Loading...')
    load_grammar(grammar_file)
    load_lexicon(lexicon_file)
    print('Ready.')
    for line in sys.stdin:
        tree = parse(line)
        print('  ', tree)
        yoda = yoda_transform(tree)
        if tree != yoda:
            print('   ==>', yoda)
            leaves = [w[0] for w in words(yoda)]
            print('Yoda says, "{0}"'.format(' '.join(leaves)))
