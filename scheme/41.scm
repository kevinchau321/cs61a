;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Untitled 6
;;;
;;; Description:
;;; 	Hey darling, Merry Christmas!
;;; 	I am your snowman
;;; 	The spring is coming and I am gonna be dead

(define (draw)
  ; *YOUR CODE HERE*

  (begin (color 'blue)
  	(ht)
  	(speed 0)
  	;;;background color
  	(pu)
  	(goto 500 0)
  	(begin_fill)
 	(circle 500)
 	(end_fill)
 	;;;snowman

 	(color 'white)
 	(pu)
  	(goto 60 -60)
  	(pd)
  	(speed 3)
  	(begin_fill)
  	(circle 50)
  	(end_fill)
  	(pu)
  	(goto 90 -180)
  	(pd)
  	(begin_fill)
  	(circle 80)
  	(end_fill)
  	(pu)
  	(goto -10 -45)
  	(color 'black)
  	(pd)
  	(rt 90)
  	(fd 15)
  	(pu)
  	(fd 10)
  	(pd)
  	(fd 15)
  	(pu)
  	(goto 5 -60)
  	(pd)
  	(color 'red)
  	(begin_fill)
  	(fd 10)
  	(rt 113)
  	(fd 13)
  	(rt 134)
  	(fd 13)
  	(end_fill)
  	(pu)
  	(color 'brown)
 	(begin_fill)
 	(goto 10 0)
 	(pd)
 	(seth 105)
 	(fd 77)
 	(seth 270)
 	(fd 149)
 	(seth 75)
 	(fd 77)
 	(end_fill)

  	;;;snow
  	(speed 0)
  	(pu)
  	(goto -200 200)
  	(seth 0)
  	(pd)
  	(color 'white)
  	(repeat 4 (lambda () (begin_fill) (snow 8 2) (end_fill) (pu) (lt 15) (bk 100) (pd)))


  	;;;background color
  	(seth 90)
  	(pu)
  	(color 'yellow)
  	(goto 0 -1200)
  	(begin_fill)

 	(circle 500)
 	(end_fill)
 	;;;tree
 	(pu)
 	(goto -40 -170)
 	(seth 0)
 	(color 'green)
 	(pd)
 	(tree 200)
 	;;;tear
  	(color_rgb (list 0 1 1))
  	(pu)
  	(goto -10 -45)
  	(pd)
  	(seth 180)
  	(speed 1)
  	(repeat 8 (lambda () (fd 20) (pu) (fd 20) (pd)))

  	(exitonclick)))

(define (snow d k)
  (tri (lambda () (leg d k))))

(define (repeat k fn)
  (if (> k 0)
    (begin (fn) (repeat (- k 1) fn))
      nil))
(define (tri fn)
  (repeat 3 (lambda () (fn) (lt 120))))
(define (leg d k)

  (if (= k 0)
   (begin (fd d) (rt 60) (fd d) (lt 120) (fd d) (rt 60) (fd d))
   (begin
   (leg (/ d 2) (- k 1))
   (rt 60)
   (leg (/ d 2) (- k 1))
   (lt 120)
   (leg (/ d 2) (- k 1))
   (rt 60)
   (leg (/ d 2) (- k 1)))))
(define (tree l)
	(if (< l 5)
		nil
		(begin
			(fd (/ l 25)) (lt 80)
			(tree (* l 0.3))
			(rt 82) (fd (/ l 25)) (rt 80)
			(tree (* l 0.3))
			(lt 78)
			(tree (* l 0.9))
			(lt 2) (bk (/ l 25))
			(lt 2) (bk (/ l 25)))))



; Please leave this last line alone.  You may add additional procedures above
; this line.  All Scheme tokens in this file (including the one below) count
; toward the token limit.
(draw)