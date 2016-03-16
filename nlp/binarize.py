#!/usr/bin/env python3

"""Binarize rules."""

import mr
import sys
from ucb import main

def binarize(tag, children):
    """Yield (tag, children) pairs for at most two children at a time."""
    rest_tag = '@' + tag
    while len(children) > 2:
        first, rest = children[0], children[1:]
        yield tag, (first, rest_tag)
        tag, children = rest_tag, rest
    yield tag, children

@main
def run():
    for line in sys.stdin:
        tag, children = mr.parse_key_value_pair(line)
        for rule in binarize(tag, children):
            mr.emit(*rule)
