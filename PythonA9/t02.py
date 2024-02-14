"""
-------------------------------------------------------
Assignment 9, Task 2
-------------------------------------------------------
"""
from functions import number_lines

input_file = input('Enter input file name: ')
output_file = input('Enter output file name: ')

fh_in = open('{}'.format(input_file), 'r+')
fh_out = open('{}'.format(output_file), 'w+')

number_lines(fh_in, fh_out)
fh_in.close()
fh_out.close()
