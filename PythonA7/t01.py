"""
-------------------------------------------------------
Assignment 7, Task 1
-------------------------------------------------------
"""
from functions import my_isdigit

s = input('Enter a string to test: ')


digits = my_isdigit(s)

if digits:
    print('The string is all digits')
else:
    print('The string contains non_digits')
