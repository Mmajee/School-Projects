"""
-------------------------------------------------------
Assignment 8, Task 7
-------------------------------------------------------
"""
from functions import num_to_text

num = int(input('Number? '))

text = num_to_text(num)

print('{} - {}'.format(num, text))
