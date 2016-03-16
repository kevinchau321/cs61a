def split(n):
	return n // 10, n % 10

def sum_digits(n):
	"""Return the sum of the digits of positive integer n."""
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return sum_digits(all_but_last) + last

def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n-1)

def fact_iter(n):
	total, k = 1, 1
	while k <= n:
		total, k = total*k, l +1
	return total

def luhn_sum(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
	all_but_last, last = split(n):
	luhn_digit = sum_digits(2*last)
	if n < 10:
		return luhn_digit
	else:
		return luhn_sum(all_but_last) + luhn_digit

def sum_digits_iter(n):
	digit_sum = 0
	while n > 0:
		n, last = split(n)
		digit_sum= digit_sum + last
	return digit_sum

def sum_digits_rec(n, digit_sum):
	if n == 0:
		return digit_sum
	else:
		n, last = split(n)
		return sum_digits_rec(n, digit_sum + last)


