"""
-------------------------------------------------------
Assignment 6, Task 6
-------------------------------------------------------
"""
from functions import time_split

initial_seconds = int(input('Number of seconds: '))
print()

days, hours, minutes, seconds = time_split(initial_seconds)

print('Days: {}, Hours: {}, Minutes: {}, Seconds: {}'.format(
    days, hours, minutes, seconds))
