"""
-------------------------------------------------------
Assignment 4, Task 3
-------------------------------------------------------
"""
from utilities import array_to_pq
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue

a = [0,6,5,2,4,3,1]

key = 3

source = Priority_Queue()
array_to_pq(source, a)
print('Source: ', source) 
target1, target2 = pq_split_key(source, key)
print()
print('Target 1: ', target1)
print('Target 2: ',target2)
