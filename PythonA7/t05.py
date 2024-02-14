"""
-------------------------------------------------------
Assignment 7, Task 5
-------------------------------------------------------
"""
from functions import is_valid_isbn

isbn = input('Enter an ISBN: ')

valid = is_valid_isbn(isbn)


if valid:
    print('Valid ISBN')
else:
    print('INVALID')
