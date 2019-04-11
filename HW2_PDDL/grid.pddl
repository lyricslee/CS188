(define (domain grid)

(:predicates (connect ?x ?y) (key-color ?x ?y)
             (lock-color ?x ?y) (at ?x ?y)
             (at-robot ?x) (place ?x)
             (key ?x) (color ?x) (locked ?x)
             (open ?x) (gripper ?x) (free ?x)
             (carry ?x ?y)
)

(:action unlock
    :parameters (?current_position ?key ?color ?x)
    :precondition (and (place ?current_position)
                        (key ?key) (color ?color) (gripper ?x) (carry ?x ?key)
                        (at-robot ?current_position) (locked ?current_position)
                        (key-color ?key ?color) (lock-color ?current_position ?color))
    :effect       (and (open ?current_position) (free ?x)
                       (not (carry ?x ?key)) (not (key ?key)))
)

(:action pickup
    :parameters (?current_position ?key ?x)
    :precondition (and (place ?current_position) (key ?key)
                       (at-robot ?current_position)
                       (at ?key ?current_position)
                       (free ?x) (gripper ?x))
    :effect       (and (carry ?x ?key)
                       (not (at ?key ?current_position)) (not (free ?x)))
)

(:action move
    :parameters (?current_position ?next_position)
    :precondition (and (place ?current_position) (place ?next_position)
                       (at-robot ?current_position)
                       (connect ?current_position ?next_position))
    :effect       (and (at-robot ?next_position)
                       (not (at-robot ?current_position))))

)
