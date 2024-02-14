"""
-------------------------------------------------------
Assignment 9, Task 7
-------------------------------------------------------
"""
from functions import shift

file1 = input('Input file: ')
file2 = input('Output file: ')

fh_in = open('{}'.format(file1), 'r')
fh_out = open('{}'.format(file2), 'w+')

n = int(input('Enter shift: '))
print()

shift(fh_in, fh_out, n)

fh_in.close()
fh_out.close()
print()
print('Done')
