"""
-------------------------------------------------------
Assignment 7, Task 4
-------------------------------------------------------
"""
from functions import common_ending

s1 = input('First string: ')
s2 = input('Second string: ')

common = common_ending(s1, s2)

print('Common ending: {}'.format(common))
