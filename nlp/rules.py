#!/usr/bin/env python3

"""A mapper that emits rules keyed by their root tag."""

import mr
import sys
from trees import read_trees, Tree
from ucb import main

def rules(tree):
    """Yield the rules of a tree, collapsing unary chains."""
    if tree.tag and type(tree) is Tree:
        branches = tree.branches
        while len(branches) == 1 and type(branches[0]) is Tree:
            branches = branches[0].branches
        if branches:
            yield tree.tag, tuple(b.tag for b in branches)
        for branch in branches:
            for rule in rules(branch):
                yield rule

@main
def run():
    for tree in read_trees(sys.stdin):
        for tag, children in rules(tree):
            mr.emit(tag, children)
