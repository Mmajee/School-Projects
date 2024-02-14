"""
-------------------------------------------------------
Assignment 3, Task 1
-------------------------------------------------------
"""
from Stack_array import Stack
from functions import stack_reverse
from utilities import array_to_stack

source = Stack()

a = [55, 22, 66, 11, 33, 44]


array_to_stack(source, a)

stack_reverse(source)

print(source)
    
