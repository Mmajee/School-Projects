"""
-------------------------------------------------------
Assignment 9, Task 6
-------------------------------------------------------
"""
from functions import substitute

file1 = input('Input file: ')
file2 = input('Output file: ')

fh_in = open('{}'.format(file1), 'r')
fh_out = open('{}'.format(file2), 'w+')

ciphertext = 'DAVIBROWNZCEFGHJKLMPQSTUXY'

substitute(fh_in, fh_out, ciphertext)
fh_in.close()
fh_out.close()

print()
print('Done')
