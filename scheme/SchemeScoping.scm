(define (last s)
		(if (null? (cdr s)) (car s) (last (cdr s))))


;Python Implementation
;def fib(n):
;	if n == 0:
;		return 0
;	if n == 1:
;		return 1
;	return fib(n-1)+fib(n-2)

;Not Tail Recursive
(define (fib n)
		(cond 
			((equal? n 0) 0)
			((equal? n 1) 1)
			(else (+ (fib (- n 1)) (fib (- n 2)) ))))


def fib(n):
	def fibi(curr, prev, count):
		if count == n:
			return curr
		fibi(curr+prev, curr, count + 1)
	return fibi(1,0,1)

(define (fib n)
	(define (fibi curr prev count)
		(if (= count n)
			curr
			(fibi (+ curr prev)
					curr
					(+ count 1))))
	(fibi 1 0 1))

;Python factorial (using a while loop for constant space)
def fact_while(n):
	total = 1
	while n > 0:
		total = total * n 
		n = n - 1
	return total

def fact(n):
	def fact_optimized(n, total):
		if n == 0:
			return total
		return fact_optimized(n-1, total*n)
	return fact_optimized(n,1)

(define (fact n)
	(define (fact-optimized n total)
			(if (= n 0) total
				(fact-optimized (- n 1) (* total n))))
	(fact-optimized n 1))

