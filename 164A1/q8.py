"""
-------------------------------------------------------
Assignment 1, Task 8
-------------------------------------------------------
"""
from functions import clean_list

values = [1, 2, 0, 1, 4, 1, 1, 2, 2, 5, 4, 3, 1, 3, 3, 4, 2, 4, 3, 1, 3, 0, 3, 0, 0]

print('Values: {}'.format(values))

clean_list(values)

print('Cleaned: {}'.format(values))
