"""
-------------------------------------------------------
Assignment 10, Task 1
-------------------------------------------------------
"""
from functions import binary_search

values = [2, 5, 5, 5, 5, 5, 5, 8]
key = 5

print('Search: {} for {}'.format(values, key))

i = binary_search(values, key)

print('Index: {}'.format(i))
