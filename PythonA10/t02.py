"""
-------------------------------------------------------
Assignment 10, Task 2
-------------------------------------------------------
"""

from functions import flatten


values = [[7.11, 6.07, 1.94], [9.35, 6.76, 5.66],
          [8.07, 7.3, 5.65], [3.84, 3.83, 8.46]]

print('Original: {}'.format(values))

flattened = flatten(values)

print('Flattened: {}'.format(flattened))
