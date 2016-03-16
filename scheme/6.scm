;;; Title: The Golden Rhapsody
;;; 
;;; Description: From across the bay,
;;;              Dreams are born within heart and mind.
;;;              We the Golden Bears.
;;;
;;;
;;;Color call has been added to scheme primitives to allow using white color to cover items.
;;;Also, due to time constraint, asthestic concerns have been prioritized
;;;over code efficiency. 

(define (repeat k fn)
    (if (> k 0)
    (begin (fn) (repeat (- k 1) fn))
    nil))
 
(define (frame)
    (penup) (goto 700 -400) (pendown)
    (repeat 2 (lambda ()
                (fd 800) (lt 90) (fd 1400) (lt 90)))
    (penup))

(define (move_right height)
        (rt 90) (fd height) (lt 90))

(define (move_left height)
        (lt 90) (fd height) (rt 90))

(define (move_in width)
        (fd width) (lt 90) (fd width) (rt 90))

(define (move_out width)
        (rt 90) (fd width) (rt 90) (fd width) (lt 180))
 
(define (rect width height)
    (pendown)
    (repeat 2 (lambda () 
                (fd width) (lt 90)
                (fd height) (lt 90))) (penup))
(define (wrect)
    (pendown) (color "#ffffff")
    (repeat 2 (lambda () 
                (begin_fill) (fd 1400) (lt 90)
                (fd 1400) (lt 90) (color "#ffffff") (end_fill)) (penup)))

(define (rects width height levels)
        (rect width height)
        (move_in 2)
        (if (> levels 1) (rects (- width 4) (- height 4) (- levels 1))))

(define (rect_cross)   
        (seth -90) (rect 8 8) (pendown) (lt 45) (fd 11) (penup) (lt 135) (fd 8)
        (lt 135) (pendown) (fd 11) (penup) (rt 135) (fd 8) (seth -90))         

 
(define (rect_col width height levels)
    (if (> levels 0)
        (begin (rect width height) (move_right height) 
        (rect_col width height (- levels 1)))))    

(define (rect_row width height levels)
    (if (> levels 0)
        (begin (rect width height) (fd width)
        (rect_row width height (- levels 1)))))


(define (rect_stripe width height levels)
    (if (> levels 0)
        (begin (rect width height) (fd (+ 1 width))
        (rect_stripe width height (- levels 1)))))

;brickrow 56 33 3 6 (total length 150)
(define (brickrow1 long mid short width)
    (rect short width) (fd (+ short 1))
    (rect long width) (fd (+ long ))
    (rect mid width) (fd (+ mid))
    (rect long width) (fd (+ long 1))
    (rect short width) (fd short) (rt 90) (rt 90))

(define (brickrow2 l m s w)
    (rect (+ l 1) w) (fd (+ l 1))
    (rect (+ m (* 2 s)) w) (fd (+ m (* 2 s)))
    (rect (+ l 1) w) (fd (+ l 1))
    (lt 90) (fd w) (lt 90))

(define (circles r levels)
    (pendown)
    (circle r)
    (penup)
    (if (> levels 1)
        (repeat 1 (lambda ()
                    (penup) (lt 90) (fd 2) (rt 90) (pendown)                   
                    (circles (- r 2) (- levels 1) (penup))))))

(define (circles_bar r levels count)
    (penup)
    (fd (+ 2 r))
    (repeat count (lambda ()
            (circles r levels) (rt 90) (fd (* 2 (- levels 1))) (lt 90) (fd (* r 2.5)))))                 

(define repeat_num 24)

(define (trapezoid)
        (begin (pendown) (rt 120) (fd 2) (lt 120) (fd 154) (lt 120) 
        (fd 2) (lt 60) (fd 152) (penup)))

(define (trapezoid2)
        (begin (pendown) (rt 120) (fd 4) (lt 120) (fd 166) (lt 120) 
        (fd 4) (lt 60) (fd 161) (penup)))

(define (trapezoid3)
        (pendown) (fd 42) (lt 80) (fd 8) (lt 80) (fd 42) (lt 100) (fd 24)
        (penup) 100)

(define (trapezoid4 s l h i)
        (if (= i 0) (penup)
        (begin (pendown) (fd h) (lt 75) (fd s) (lt 75) (fd h) (lt 105) (fd l) (lt 105)
        (trapezoid4 (- s 8) (- l 8) (- h 4) (- i 1)))))  

(define (coastline l i)
        (if (= i 0) (penup)
        (begin (pendown) (lt 2) (fd l) (rt 3) (fd (/ l 2)) (lt 1) (fd l)
        (coastline (/ l 1.5) (- i 1)))))

(define (house1 s)
        (seth 0) (pendown) (fd s) (lt 90) (fd (/ s 2)) (lt 90) (fd s) (penup) (rt 90) (fd 1) (rt 90)
        (pendown) (fd (+ s 1)) (lt 90) (fd (/ s 2)) (lt 90) (fd (+ s 1)) (penup)
        (rt 90) (fd 2) (rt 90))

(define (house2 s)
        (pendown) (fd s) (lt 90) (fd s) (lt 90) (fd s) (penup) (rt 90) (fd 2) (rt 90)
        (pendown) (fd (+ s 1)) (lt 90) (fd  s) (lt 90) (fd (+ s 1)) (penup)
        (rt 90) (fd 1.5) (rt 90))

(define (houses s i)
        (if (= i 0) (penup)
        (begin (house1 s) (house1 s) (house2 s) (houses (+ s 0.5) (- i 1)))))       

(define (house3 h w)
        (seth 0) (pendown) (fd h) (lt 90) (fd w) (lt 90) (fd h) (seth 0) (penup))

(define (house3s h w l i)
        (repeat i (lambda () (house3 h w) (move_left l)(fd 2))))

(define (transamerica) (pendown) (lt 10) (fd 20) (lt 160) (fd 20) (penup) (rt 170)) 

(define (bridgewire) (seth 75) (pendown) (repeat 5 (lambda () (fd 15) (lt 1)))
                        (seth 105) (repeat 5 (lambda () (fd 17) (lt 1))) (penup))

(define (goldengate) (pendown) (pensize 2) (repeat 7 (lambda () (fd 50) (lt 0.2))) (pensize 1) (penup)
        (bk 20) (bridgewire) (seth 90) (fd 35) (bridgewire) (fd 14) (seth -90) (fd 96)
        (rect_col 2 9.7 3) (fd 189) (move_left 30) (rect_col 2 9.5 3) 
)

(define (mountainup l i)
        (if (= i 0) (penup) (begin (pendown) (lt 25) (fd 10) (rt 10) (fd 3) (rt 13) (fd l)
        (lt 12) (fd (/ l 2)) (rt 16) (fd l) (mountainup (/ l 2) (- i 1)))))

(define (mountaindown l i)
        (if (= i 0) (penup) (begin (pendown) (fd l) (rt 16) (fd (/ l 2)) (lt 12) (fd l)
        (rt 8) (fd 3) (rt 10) (fd 10) (lt 25) (mountaindown (/ l 2) (- i 1)))))

(define (tree1 r)
        (if (< r 5) (begin (fd r) (bk r))
        (begin (pendown)
        (fd (/ r 3)) (lt 30) (tree1 (* (/ r 3) 2))
        (rt 30) (bk (/ r 3)) (fd (/ r 2)) (rt 25) (tree1 (/ r 2)) (lt 25) (bk (/ r 2))
        (fd (* (/ 5 6) r)) (rt 25) (tree1 (/ r 2)) (lt 25) (bk (* r (/ 5 6))) (penup))))

(define (tree2 r)
        (if (< r 5) (begin (fd r) (bk r))
        (begin (pendown)
        (fd (/ r 3)) (lt 20) (tree2 (* (/ r 3) 2))
        (rt 20) (bk (/ r 3)) (fd (/ r 2)) (rt 25) (tree2 (/ r 2)) (lt 25) (bk (/ r 2))
        (fd (* (/ 4 6) r)) (rt 30) (tree1 (/ r 2)) (lt 30) (bk (* r (/ 4 6))) (penup))))

(define (tree3 r)
        (if (< r 5) (begin (fd r) (bk r))
        (begin (pendown) (fd (/ r 6)) (lt 35) (tree3 (/ r 2)) (rt 35) (bk (/ r 6)) 
        (fd (/ r 6)) (rt 15) (tree3 (/ r 2)) (lt 15) (bk (/ r 6)) (penup))))

(define (trees s i)
        (if (> i 0) (begin (pendown) (tree1 s) (penup) (fd 5) (move_right 11) (trees (- s 1) (- i 1)))))


(define (campanile l m s w)
        (seth 270)
        (repeat repeat_num (lambda () 
 ;repeat 28
        (brickrow1 l m s w) (brickrow2 l m s w)
        (rt 90) (fd w) (lt 90)))
        (rt 90) (fd 3) (lt 90) (bk 1)
        (rect 152 8) (circles_bar 4 2 15)        
        (goto 441 (+ -400 (* 12 repeat_num) 10))
        (trapezoid)
        (lt 90) (fd 9) (lt 90) (bk 2)
        (repeat 4 (lambda () (rect 39 6) (fd 39)))
        (bk 154) (rt 90) (fd 18) (lt 90) (rect 27 18) (fd 28)
        (repeat 5 (lambda () (rect 4 18) (fd 5))) 
        (rect 10 18) (fd 11)
        (repeat 5 (lambda () (rect 4 18) (fd 5))) 
        (rect 10 18) (fd 11)
        (repeat 5 (lambda () (rect 4 18) (fd 5))) 
        (rect 27 18) (bk 126) (rt 90) (fd 3) (lt 90)
        (rect 154 3) (fd 2) (move_right 6) (rect_col 27 6 15)
        (move_left 6) (fd 27) (rect_stripe 2 90 9)
        (repeat 2 (lambda () (rect 8 90) (fd 8) (rect_stripe 2 90 9))) 
        (move_left 84) (rect_col 27 6 15) (bk 126)
 ;finish all stripes
        (rect_row 39 6 4) (bk 156) (move_right 14)
        (rect 156 14) (circles_bar 6.9 3 9) (bk 167) (move_right 4)
 ;finish circles bar
        (rect 162 4) (trapezoid2) (move_left 6) (lt 180) (bk 3)
        (rect 166 3) (fd 5) (move_right 8)
        (rect_row 39 8 4) (bk 156) (move_right 4) (brickrow1 50 48 3 4) (fd 153) (lt 180)
        (move_right 19) (rects 26 18 2) (move_out 4) (fd 30)
        (repeat 3 (lambda () (rects 27 18 3) (fd 6) (circles 3 1) (move_out 6) (fd 25)))
        (rects 26 18 2) (move_out 4) (bk 125) (move_right 3) (rect 154 3) 
        (move_right 2) (rect 154 2) (fd 3)
        (rt 80) (trapezoid3) (bk 128) (lt 100) (trapezoid3)
        (fd 1) (rects 101 38 2) (move_out 2) (fd 35) (rects 25 25 3)
        (move_out 3) (fd 58.5) (lt 90) (fd 38) (lt 90) (rect_col 96 4 2) (move_left 3) (fd 4)
        (rt 75) (trapezoid4 13 83 143 2) (fd 144) (lt 75) (bk 8) (move_right 4) (rect 17 4)
        (fd 3) (move_right 6) (rect_col 10 6 2) (fd 4) (move_left 3) (rect_col 2 2 8)
 ;tip 
        (goto 420 -400) (house3 278 110) (goto 415 -400) (house3 275 100)
        (goto 365 -130) (seth -90) (pendown) (circle 50) (penup) (move_left 50) (lt 20) (bk 1) (rect_col 2 2 23)
        (goto 365 -181) (rt 80) (bk 1) (rect_col 2 2 23)         
        (goto 429 128) (seth -90) (rect_col 3 2 10)
        (goto 302 128) (rect_col 3 2 10)

)


(define (draw)
    (seth 0) (speed 100000000) (frame)
    (goto -700 83) (seth 90) (mountaindown 40 8)
    (goto -700 50) (seth 90) (coastline 84 3) (lt 90) (move_left 4) (fd 2)

 ;buildings in SF 
    (houses 1 2) (houses 1.5 3) (move_left 2) (bk 0.5) (houses 3 4) (bk 1) 
    (houses 4 2) (bk 1) (house1 6 1) (bk 0.5) (houses 8 2) (fd 0.5) (move_right 2)
    (house1 14) (move_left 3) (houses 4 2) (houses 3 1) (move_right 2) (house2 9)
    (fd 6) (move_right 90) (house1 10) (house1 9) (house2 9)
    (transamerica) (move_left 16) (fd 5) (house1 13)
    (move_right 200) (bk 1)  (houses 5 3) (move_right 150) (bk 2) (houses 1 3)
    (move_left 100) (bk 8) (houses 1 2) (move_right 705) (fd 5)

;;goldengate bridge
    (lt 89.9) (goldengate) (fd 90) (move_left 60) (seth 90) (coastline 20 3) (bk 111) 
    (mountainup 15 2) (mountaindown 12 1) (bk 70) (move_left 2) (seth 90) (brickrow1 19 2 2 6) 
    (move_left 4) (seth 0) (houses 2 2)

;;buildings across the bridge
    (seth 90) (fd 290) (move_left 27) (rt 1) (coastline 49 2) (bk 200) (lt 3) (seth 80) 
    (mountainup 23 2) (mountainup 6 1)(mountaindown 21 1)
    (goto 440 85) (seth 90) (mountainup 28 2) (seth 88) (mountaindown 47 1) (bk 260)
    (move_right 13) (seth 93) (coastline 50 3)
    (goto 140 60) (seth 0) (houses 2 1) (goto 115 61) (seth -90) (rect_row 9 2 3) 

;;berkeley side
    (goto -700 -55) (seth 94) (coastline 238 2) (fd 151) (coastline 104 1)
    (goto 0 -200) (seth 0) (house3s 25 60 20 4)
    (goto -100 -300) (house3 60 220) (move_right 210) (fd 20) (seth -90) 
    (repeat 3 (lambda () (rect 200 7) (move_right 14)))
    (goto -550 -250) (house1 45) (goto -400 -250)
    (repeat 11 (lambda () (rect_cross) (move_right 8) (fd 0.5)))
    (bk 18) (move_left 20) (repeat 18 (lambda () (rect_cross) (fd 8.5))) 
    (goto -550 -150) (seth 0) (trees 18 6) (goto -470 -180) (trees 20 7)
    (goto -500 -100) (house3s 8 14 10 7) 
    (goto 50 0) (seth -90) (coastline 20 2) (move_right 1) (rect 14 2)
    (goto -400 0) (seth -85) (coastline 10 2) (move_right 1) (seth -88) (rect 9 1)
    (goto -250 -130) (house3s 14 18 13 5) (goto 180 -120) (house3s 9 13 11 6)
    (goto -250 -140) (house3s 10 15 13 5) 
    (goto -220 -110) (house3s 9 13 11 7) 
    (goto 160 -135) (house3s 10 13 11 7) (tree3 30)
    (bk 20) (house3s 15 18 8 2) (move_left 60) (trees 18 5)

;;sky
    (goto 50 300) (seth -90) (coastline 100 4) (goto 200 294) (coastline 100 2)
    (goto -400 270) (coastline 26 2) (goto -420 266) (coastline 19 2)
;;campanile
    (goto 440 -394)
    (campanile 56 30 3 6)

;;trees
    (goto -330 -250) (seth 0) (pendown) (tree2 80) (penup)
    (goto -500 -450) (pendown) (tree2 130) (goto -620 -280) (pendown) (tree2 80) 
    (goto -300 -450) (pendown) (tree2 150) (goto -100 -450) (pendown) (tree2 100)
    (goto 100 -460) (tree1 150) (goto 600 -420) (tree1 150) (goto 730 -460) (tree1 130)
    (goto -550 -150) (seth 0) (trees 18 6) (goto -470 -180) (trees 20 7)
    (goto 0 -300) (tree2 40) (goto 200 -420) (tree1 40)
    (goto 230 -350) (tree1 60) (goto -420 -330) (tree2 80)
    (goto -630 -430) (tree1 85)

;; hide trees outside of frame
    (goto 700 -401) (seth -90) (wrect)
    (goto 701 400) (seth -180) (wrect) 
    


)
(draw)

