"""
-------------------------------------------------------
Assignment 1, Task 1
-------------------------------------------------------
"""

ciphertext = 'DAVIBROWNZCEFGHJKLMPQSTUXY'

from functions import substitute

file1 = input('Input file: ')
file2 = input('Output file: ')

fh_in = open('{}'.format(file1), 'r')
fh_out = open('{}'.format(file2), 'w+')

fh_in.seek(0)

lines = fh_in.readline()

lines = lines.upper()

while lines != '':
    string = lines
    estring = substitute(string, ciphertext)
    fh_out.write(estring)
    lines = fh_in.readline()

    lines = lines.upper()




fh_in.close()
fh_out.close()

print()
print('Done')
