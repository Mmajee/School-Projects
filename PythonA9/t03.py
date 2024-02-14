"""
-------------------------------------------------------
Assignment 9, Task 3
-------------------------------------------------------
"""
from functions import get_addresses

file = input('Enter address file name: ')

fh = open('{}'.format(file), 'r+')
print()

addresses = get_addresses(fh)

for i in addresses:
    print(i)
fh.close()
