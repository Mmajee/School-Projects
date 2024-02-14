"""
-------------------------------------------------------
Assignment 3, Task 2
-------------------------------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack

source = Stack()

a = [55, 22, 66, 11, 33, 44]

array_to_stack(source, a)

source.reverse()

print(source)

