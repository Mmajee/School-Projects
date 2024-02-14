"""
-------------------------------------------------------
Assignment 6, Task 3
-------------------------------------------------------
"""

from functions import get_total_change

nickles = int(input('Enter number of nickles: '))

dimes = int(input('Enter number of dimes: '))

quarters = int(input('Enter number of quarters: '))

loonies = int(input('Enter number of loonies: '))

toonies = int(input('Enter number of toonies: '))

tv = get_total_change(nickles, dimes, quarters, loonies, toonies)

print('Total: ${:.2f}'.format(tv))
