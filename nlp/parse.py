#!/usr/bin/env python3

"""A natural language parser."""

import sys
from functools import lru_cache
from mr import parse_key_value_pair
from ucb import main, trace
from trees import Tree, Leaf, START, END

open_class_tags = ('NN', 'JJ', 'VB')
unknown_word_tags = {tag: 1/len(open_class_tags) for tag in open_class_tags}
memo = lru_cache(None)
grammar = {}
lexicon = {}

def parse(line):
    """Return the highest scoring parse of the words in a line."""
    tokens = [START.word] + line.split() + [END.word]

    @memo
    def parse_from(start, end, tag):
        """Return the score and parse of tokens[start:end] rooted by tag."""
        best_score, parse = 0, None
        if end-start == 1:
            word = tokens[start]
            tags_for_word = lexicon.get(word, unknown_word_tags)
            best_score = tags_for_word.get(tag, 0)
            parse = Leaf(tag, word)
        for children, rule_score in grammar.get(tag, ()):
            branches_score, branches = parse_children(start, end, children)
            score = rule_score * branches_score
            if score > best_score:
                best_score, parse = score, Tree(tag, branches)
        return best_score, parse

    @memo
    def parse_children(start, end, tags):
        """Return the score and parses of tokens[start:end] rooted by tags."""
        first = tags[0]
        if len(tags) == 1:
            score, parse = parse_from(start, end, first)
            return score, (parse,)
        else:
            rest = tags[1:]
            best_score, parses = 0, ()
            for middle in range(start+1, end+1-len(rest)):
                first_score, branch = parse_from(start, middle, first)
                if first_score > 0:
                    rest_score, branches = parse_children(middle, end, rest)
                    score = first_score * rest_score
                    if score > best_score:
                        best_score, parses = score, (branch,) + branches
            return best_score, parses

    score, parse = parse_from(0, len(tokens), 'ROOT')
    return parse.branches[1]


def load_grammar(grammar_file):
    """Load a value constructed from a MapReduction."""
    for line in open(grammar_file):
        tag, childrens = parse_key_value_pair(line)
        grammar[tag] = childrens

def load_lexicon(lexicon_file):
    """Load a lexicon constructed from a MapReduction."""
    for line in open(lexicon_file):
        word, tags = parse_key_value_pair(line)
        lexicon[word] = {tag: float(score) for tag, score in tags}

########
# Main #
########

@main
def run(grammar_file="grammar.txt", lexicon_file="lexicon.txt"):
    print('Loading...')
    load_grammar(grammar_file)
    load_lexicon(lexicon_file)
    print('Ready.')
    for line in sys.stdin:
        tree = parse(line)
        print('  ', tree)
