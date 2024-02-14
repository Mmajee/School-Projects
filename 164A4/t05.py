"""
-------------------------------------------------------
Assignment 4, Task 5
-------------------------------------------------------
"""
from Queue_circular import Queue


cq = Queue(10)



a = [33, 11, 55, 22, 66, 44]

for value in a:
    cq.insert(value)

for q in cq:
    print(q)
    
value = cq.peek()
print()
print(value)

value = cq.remove()
print()
print(value)
b = cq.is_empty()
print(b)
b = cq.is_full()
print(b)
print(len(cq))
