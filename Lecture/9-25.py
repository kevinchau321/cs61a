#Data
"""
Native data types:
	floating point
	integer
	boolean
	complex
Object: represents information
	data + behavior = abstraction
	objects represent things, properties, interactions, processes
	type of object is called a class: classes are first-class values
	Leads to OBJECT ORIENETED PROGRAMMING
	every value in python is an object:
		all objects have attributes
		a lot of data manipulation happens through object methods
"""
from datetime import date
date
today = date(2013, 9, 25)
freedom = date)2013, 12, 20)
str(freedom - today)
today.year
today.day
"""
Data abstraction:
	compound objects combine objects together
	an absract data type lets us manipulate compound objects as units
"""
#Ex: Rational Numbers
def mul_rational(x,y):
	return rational(numer(x)*numer(y), denom(x)*denom(y))
def add_radtional(x,y):
	nx, dx = numer(x), denom(x)
	ny, dy = numer(y), denom(y)
	return rational(nx*dy + ny*dx, dx*dy)
#Tuples
pair = (1,2)
x, y = pair
pair[0] #index notation selection
from operator import getitem
getitem(pair, 1)
#Tuple literal: comma seperated expression
def rational(n, d)