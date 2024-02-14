"""
-------------------------------------------------------
Assignment 1, Task 2
-------------------------------------------------------
"""
from functions import shift

file1 = input('Input file: ')
file2 = input('Output file: ')

fh_in = open('{}'.format(file1), 'r')
fh_out = open('{}'.format(file2), 'w+')
n = int(input('Enter shift: '))
print()

fh_in.seek(0)

lines = fh_in.readline()

lines = lines.upper()

while lines != '':
    string = lines
    estring = shift(string, n)
    fh_out.write(estring)
    lines = fh_in.readline()

    lines = lines.upper()




fh_in.close()
fh_out.close()

print()
print('Done')
