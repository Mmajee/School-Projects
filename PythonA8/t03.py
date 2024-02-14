"""
-------------------------------------------------------
Assignment 8, Task 3
-------------------------------------------------------
"""
from functions import two_element_subset

string = input('String: ')

subsets = two_element_subset(string)

print('Subsets: {}'.format(subsets))
