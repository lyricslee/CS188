
(define (problem gird-one)
   (:domain grid)
   

(:objects node1-1 node1-2 node1-3
          node2-1 node2-2 node2-3
          node3-1 node3-2 node3-3
          key1 key2 key3
          green red yellow
          left right)
          
          
(:init (connect node1-1 node1-2) (connect node1-1 node2-1) (connect node1-2 node1-1)
       (connect node1-2 node1-3) (connect node1-2 node2-2) (connect node1-3 node1-2)
       (connect node1-3 node2-3) (connect node2-1 node1-1) (connect node2-1 node2-2)
       (connect node2-1 node3-1) (connect node2-2 node1-2) (connect node2-2 node2-1)
       (connect node2-2 node2-3) (connect node2-2 node3-2) (connect node2-3 node1-3)
       (connect node2-3 node2-2) (connect node2-3 node3-3) (connect node3-1 node2-1)
       (connect node3-1 node3-2) (connect node3-2 node3-1) (connect node3-2 node2-2)
       (connect node3-2 node3-3) (connect node3-3 node3-2) (connect node3-3 node2-3)
       (place node1-1) (place node1-2) (place node1-3)
       (place node2-1) (place node2-2) (place node2-3)
       (place node3-1) (place node3-2) (place node3-3)
       (key key1) (key key2) (key key3)
       (color green) (color red) (color yellow)
       (key-color key1 green) (key-color key2 red) (key-color key3 yellow)
       (at key1 node3-1) (at key2 node2-2) (at key3 node2-3)
       (lock-color node1-3 green) (lock-color node3-3 red) (lock-color node2-1 yellow)
       (locked node1-3) (locked node2-1) (locked node3-3)
       (open node1-1) (open node1-2) (open node2-2)
       (open node2-3) (open node3-1) (open node3-2)
       (gripper left) (gripper right)
       (free left) (free right)
       (at-robot node1-1)
)


(:goal (and (open node1-3)
            (open node2-1)
            (open node3-3)
            (at-robot node1-1)))
)
