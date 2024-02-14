"""
-------------------------------------------------------
Assignment 3, Task 7
-------------------------------------------------------
"""

from functions import is_palindrome_stack

string = 'hamburger'
print(string)

palindrome = is_palindrome_stack(string)

if palindrome == True:
    print('{} is a palindrome'.format(string))
else:
    print('{} is not a palindrome'.format(string))
