"""
-------------------------------------------------------
Assignment 6, Task 5
-------------------------------------------------------
"""
from functions import time_values

seconds = int(input('Number of seconds: '))
print()

days, hours, minutes = time_values(seconds)

print('{} seconds is the same as: '.format(seconds))
print('{:>4d} days'.format(days))
print('{:>5d} hours'.format(hours))
print('{:>7d} minutes'.format(minutes))
