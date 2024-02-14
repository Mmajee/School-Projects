"""
-------------------------------------------------------
Assignment 7, Task 3
-------------------------------------------------------
"""
from functions import my_find

s = input('String to search: ')

r = input('String to search for: ')

i = my_find(s, r)

print("'{}' is found at location {} in '{}'".format(r, i, s))
