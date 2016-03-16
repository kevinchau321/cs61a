;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Mandelbrot Rainbow
;;;
;;; Description:
;;;   <A complex fractal
;;;    with self-similarity
;;;    takes hours to run.>

(define (draw)
  ;;; Draw the points
  (for2d left left right top bottom mandelbrotpoint)
  ;;; Hide the turtle
  (ht)
  (exitonclick))

;;; Init
(speed 0)
(define left -341)
(define right 333)
(define top 193)
(define bottom -193)
(define mandel_left -2.5)
(define mandel_right 1)
(define mandel_top 1)
(define mandel_bottom -1)
(define mandel_color_factor 5)

;;; Helper Functions

;;; 2d inclusive for loop
;;; assumes from1 < to1 and from2 > to2
(define (for2d from1init from1 to1 from2 to2 fn)
     (if (<= from1 to1) (begin (fn from1 from2)
                             (for2d from1init (+ from1 1) to1 from2 to2 fn))
                      (if (> from2 to2) (for2d from1init from1init to1 (- from2 1) to2 fn) nil)))

;;; Scale to Range
(define (scale val oldmin oldmax newmin newmax)
        (/ (* val (- newmax newmin)) (- oldmax oldmin)))

(define (mandelbrotpoint xcoord ycoord)
        (let ((x0 (scale xcoord left right mandel_left mandel_right))
              (y0 (scale ycoord bottom top mandel_bottom mandel_top))
              (i_max 1000))
             (begin (define (iterator x y i)
                            (if  (and (> (* 2 2) (+ (* x x) (* y y))) (< i i_max))
                                 (iterator (+ (- (* x x) (* y y)) x0)
                                           (+ (* 2 x y) y0)
                                           (+ i 1))
                                 i))
                    (define i (iterator 0 0 0))
                    (pu)
                    (setposition xcoord ycoord)
                    (pd)
                    (setcolor i)
                    (fd 1)
                    ;;; This lets one see where the turtle is currently more clearly
                    (color 'hotpink))))

(define (setcolor index)
     (define mod (modulo index 7))
     (cond ((= mod 0) (color 'firebrick))
           ((= mod 1) (color 'tomato))
           ((= mod 2) (color 'khaki))
           ((= mod 3) (color 'olivedrab))
           ((= mod 4) (color 'steelblue))
           ((= mod 5) (color 'blueviolet))
           ((= mod 6) (color 'brown))))

; Please leave this last line alone.  You may add additional procedures above
; this line.  All Scheme tokens in this file (including the one below) count
; toward the token limit.
(draw)