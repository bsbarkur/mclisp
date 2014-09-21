mclisp
======

This is an on-going implementation of the lisp evaluator as explained in McCarthy's "A MICRO-MANUAL FOR LISP - NOT THE WHOLE TRUTH" paper

[http://www.ee.ryerson.ca/~elf/pub/misc/micromanualLISP.pdf]

TODO:
====
Test cases this passes:

(QUOTE A)
 
(QUOTE (A B C))

(CAR (QUOTE (A B C)))

(CDR (QUOTE (A B C)))

(CONS (QUOTE A) (QUOTE (B C)))

Test cases to implement:

(EQUAL (CAR (QUOTE (A B))) (QUOTE A))

(EQUAL (CAR (CDR (QUOTE (A B)))) (QUOTE A))

(ATOM (QUOTE A))

(COND ((ATOM (QUOTE A)) (QUOTE B)) ((QUOTE T) (QUOTE C)))

((LAMBDA (X Y) (CONS (CAR X) Y)) (QUOTE (A B)) (CDR (QUOTE (C D))))

(LABEL FF (LAMBDA (X Y) (CONS (CAR X) Y)))

(FF (QUOTE (A B)) (CDR (QUOTE (C D))))

(LABEL XX (QUOTE (A B)))

(CAR XX)

Clean up the parsing and evaluator functions so that LABEL and LAMBDA implementation becomes easier


