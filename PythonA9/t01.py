"""
-------------------------------------------------------
Assignment 9, Task 1
-------------------------------------------------------
"""
from functions import file_head

file = input('Enter input file name: ')

fh = open('{}'.format(file), 'r+')

n = int(input('Enter n: '))
print()

file_head(fh, n)
fh.close()
