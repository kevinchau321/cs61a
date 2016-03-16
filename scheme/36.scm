;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Sphere and Helix
;;;
;;; Description:
;;;   <Sometimes true beauty
;;;    lies in simplification
;;;    of complex systems.>

(define (sqrt-inner a x)
  (let ((diff (- x (/ a x))))
       (if (and (< diff 0.00001) (> diff -0.00001))
           x
           (sqrt-inner a (/ (+ x (/ a x)) 2)))))
(define (sqrt a) (sqrt-inner a 1))
 
(define (square n) (* n n))

(define (exponent b n)
  (if (= n 0) 1
    (if (even? n)
      (square (exponent b (/ n 2)))
      (* b (exponent b (- n 1))))))

(define (factorial n)
  (if (= n 0) 1 (* n (factorial (- n 1)))))

(define pi 3.14159265359)

(define (sine-approx x n)
  (if (>= n 0)
    (+ (/ (* (exponent -1 n) (exponent x (+ (* 2 n) 1)))
          (factorial (+ (* 2 n) 1)))
       (sine-approx x (- n 1)))
    0))
(define (sine x)
  (let ((d (modulo x (* 2 pi))))
    (cond ((< d (/ pi 2)) (sine-approx d 5))
          ((< d pi) (sine-approx (- pi d) 5))
          (else (* -1 (sine (- d pi)))))))

(define (cosine-approx x n)
  (if (>= n 0)
    (+ (/ (* (exponent -1 n) (exponent x (* 2 n)))
          (factorial (* 2 n)))
       (cosine-approx x (- n 1)))
    0))
(define (cosine x)
  (let ((d (modulo x (* 2 pi))))
    (cond ((< d (/ pi 2)) (cosine-approx d 5))
          ((> d (* pi 1.5)) (cosine-approx (- (* pi 2) d) 5))
          (else (* -1 (cosine (- d pi)))))))

(define (tangent x) (/ (sine x) (cosine x)))

(define (graph-2d-inner xt yt t0 t1 h)
  (if (< t0 t1)
    (begin (setpos (xt t0) (yt t0))
      (graph-2d-inner xt yt (+ t0 h) t1 h)) nil))
(define (graph-2d xt yt t0 t1 h)  
  (penup)
  (setpos (xt t0) (yt t0))
  (pendown)
  (graph-2d-inner xt yt t0 t1 h)
  (penup)
  (ht))

(define (graph-3d xt yt zt eyex eyey eyez focusx focusy focusz scale t0 t1 h) 
  (define (w t)
    (/ (+ (square (- focusx eyex)) (square (- focusy eyey)) (square (- focusz eyez)))
       (+ (* (- focusx eyex) (- (xt t) eyex)) (* (- focusy eyey) (- (yt t) eyey)) (* (- focusz eyez) (- (zt t) eyez)))))
  (define magxwinvec (sqrt (+ (square (- focusy eyey)) 
                         (square (- eyex focusx)))))
  (define magywinvec (sqrt (+ (square (* (- eyex focusx) (- focusz eyez))) 
                         (square (* (- eyey focusy) (- focusz eyez))) 
                         (square (+ (square (- focusy eyey)) (square (- focusx eyex))))))) 
  (define (v t)
    (/ (* (- (+ (* (- (zt t) eyez) (w t)) eyez) focusz) magywinvec)
       (+ (square (- focusy eyey)) (square (- focusx eyex))))) 
  (define (u t)
    (/ (* (- (+ (* (- (xt t) eyex) (w t)) eyex) focusx (/ (* (v t) (- eyex focusx) (- focusz eyez)) magywinvec)) magxwinvec)
       (- focusy eyey)))
  (graph-2d (lambda (t) (* (u t) scale)) (lambda (t) (* (v t) scale)) t0 t1 h))

(define (draw-axes eyex eyey eyez focusx focusy focusz scale len)
  (graph-3d (lambda (t) t) (lambda (t) 0) (lambda (t) 0) eyex eyey eyez focusx focusy focusz scale 0 len (/ len 2))
  (graph-3d (lambda (t) 0) (lambda (t) t) (lambda (t) 0) eyex eyey eyez focusx focusy focusz scale 0 len (/ len 2))
  (graph-3d (lambda (t) 0) (lambda (t) 0) (lambda (t) t) eyex eyey eyez focusx focusy focusz scale 0 len (/ len 2)))

(define (draw)
  (graph-3d (lambda (t) (begin
                          (define foo (/ t pi))
                          (color_rgb (list (- 1 foo) 0 foo))
                          (cosine t)))
            (lambda (t) (* (sine t) (sine (* 36 t)))) 
            (lambda (t) (* (sine t) (cosine (* 36 t)))) 
            3 3 3 2 2 2 512 0 pi 0.002)
  (graph-3d (lambda (t)  (- (* (+ 1.2 (* (cosine (* 64 t)) 0.2)) (cosine t)) 0.5))
            (lambda (t) (+ (* (+ 1.2 (* (cosine (* 64 t)) 0.2)) (sine t)) 0.5))
            (lambda (t) (begin
                          (define foo (/ (+ 1 (sine (* 64 t))) 2))
                          (color_rgb (list 0 (- 1 foo) foo))
                          (+ 2.7 (* t .7) (* .2 (sine (* 64 t))))))
            3 3 3 2 2 2 512 -11 0 0.005)
  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.  All Scheme tokens in this file (including the one below) count
; toward the token limit.
(draw)