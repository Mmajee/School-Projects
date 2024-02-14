"""
-------------------------------------------------------
Assignment 4, Task 4
-------------------------------------------------------
"""
from utilities import array_to_pq
from Priority_Queue_array import Priority_Queue

a = [0,6,5,2,4,3,1]

key = 3

source = Priority_Queue()
array_to_pq(source, a)
print(source) 
target1, target2 = source.split_key(key)

print(target1)
print(target2)
