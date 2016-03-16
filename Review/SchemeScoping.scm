(define (last s)
		(if (null? (cdr s)) 
			(car s) 
			(last (cdr s))))