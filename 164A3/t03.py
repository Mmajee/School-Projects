"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
"""
from Stack_array import Stack
from functions import stack_combine
from utilities import array_to_stack

a1 = [5,8,12,8]
a2 = [3,6,1,7,9,14]

source1 = Stack()
source2 = Stack()

array_to_stack(source1, a1)
array_to_stack(source2, a2)

target = stack_combine(source1, source2)
print(target)
