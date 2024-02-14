"""
-------------------------------------------------------
Assignment 1, Task 4
-------------------------------------------------------
"""
from functions import is_leap_year

year = int(input('Enter a year: '))

leap_year = is_leap_year(year)

if leap_year == True:
    print('{} is a leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))
