;;; Title: Untitled 5
;;;
;;; Description:

(speed 0)
(st)
(pd)


(define (base len)
			(rt 90)
			(fd len)
			(rt 180)
			(fd len)
			(fd len)
			(rt 180)
			(fd len)
			(rt 270)
)

(define (recurse len)
			(rt 90)
			(fd len)
			(drawing (/ len 2))
			(rt 180)
			(fd (* len 2))
			(drawing (/ len 2))
			(rt 180)
			(fd len)
			(rt 270)
)


(define (drawing len)

	(if (< len 1)

		(base len)
		(recurse len)

	)

)



(drawing 400)
(exitonclick)