#!/usr/bin/env python3

"""Emit the top k values for each key."""

import sys
from ucb import main
from mr import values_by_key, emit
from collections import Counter

@main
def run(k, normalize=0):
    """Emit the top K values for each key.  If NORMALIZE > 0, divide counts
    by the total for each key and round to NORMALIZE digits."""
    k = int(k)
    for key, value_iterator in values_by_key(sys.stdin):
        counts = Counter(value_iterator)
        format = lambda x: x
        if normalize:
            digits = int(normalize)
            total = sum(counts.values())
            def format(pair):
                return (pair[0], round(pair[1]/total, digits))
        emit(key, tuple(map(format, counts.most_common(k))))
