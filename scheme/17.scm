;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: White Trees 
;;;
;;; Description:
;;;   <White trees by mountains
;;;    or some upside down trees too
;;;    I can write haiku.>
;;; 
;;; 
  
(hideturtle)
(speed 100)
(define (rectangle x y h w)
    (penup)
    (goto (+ x (/ h 2)) (+ y (/ w 2)))
    (seth 90)
    (pendown)
    (fd w)
    (seth 180)
    (fd h)
    (seth 270)
    (fd w)
    (seth 360)
    (fd h)
    (penup))

(define (tree x y h w)
    (rectangle x y h w)
    (if (> w 3)
             (begin (tree (+ x (/ w 2)) (+ y (/ h 2)) (/ h 2) (/ w 2))
              (tree (+ x (/ w 4)) (- y (/ h 4)) (/ h 2) (/ w 2)) 
              (tree (- x (/ w 2)) (+ y (/ h 2)) (/ h 2) (/ w 2))
              (tree (- x (/ w 4)) (- y (/ h 4)) (/ h 2) (/ w 2)))
         (penup)))

(define (draw)
  (tree 0 0 250 250)
  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.  All Scheme tokens in this file (including the one below) count
; toward the token limit.
(draw)