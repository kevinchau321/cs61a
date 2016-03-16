#!/usr/bin/env python3

"""A mapper that emits tags keyed by lowercase words."""

import mr
import sys
from trees import read_trees, Tree
from ucb import main

def words(tree):
    """Yield the words in a tree and their syntactic categories."""
    if tree.tag:
        if type(tree) is Tree:
            for b in tree.branches:
                for word in words(b):
                    yield word
        else:
            yield (tree.word, tree.tag)


@main
def run():
    for tree in read_trees(sys.stdin):
        for word, tag in words(tree):
            mr.emit(word.lower(), tag)
