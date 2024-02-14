"""
-------------------------------------------------------
Assignment 7, Task 2
-------------------------------------------------------
"""

from functions import my_isalpha

s = input('Enter a string to test: ')


alpha = my_isalpha(s)

if alpha:
    print('The string is all letters')
else:
    print('The string contains non_letters')
