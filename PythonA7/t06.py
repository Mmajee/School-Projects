"""
-------------------------------------------------------
Assignment 7, Task 6
-------------------------------------------------------
"""
from functions import number_convert

number = input('Enter phone number: ')

digits = number_convert(number)

print('Digits: {}'.format(digits))
