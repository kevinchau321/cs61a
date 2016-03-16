#!/usr/bin/env python3

import sys
from ucb import main
from mr import emit

@main
def run():
	for line in sys.stdin:
		for word in line.split():
			if word == "the":
				emit(word, 1)
			elif word == "he":
				emit(word, 1)
			elif word == "she":
				emit(word, 1)
			elif word == "it":
				emit(word, 1)
			elif word == "thee":
				emit(word, 1)
			else:
				emit('other words', 1)


