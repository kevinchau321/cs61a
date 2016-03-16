def if_function(condition, true_result, false_result):
	"""return true_result if condition is a true value, and false_result otherwise."""
	if condition:
		return true_result
	else:
		return false_result
def with_if_statement():
	"""
	>>> with_if_statement()
	1
	"""
	if c():
		return t()
	else:
		return f()
def with_if_function():
	return if_function(c(), t(), f())
def c():
	return 1
def t():
	return 1
def f():
	return 1/0

from doctest import run_docstring_examples
run_docstring_examples(with_if_statement, globals(), True)
	