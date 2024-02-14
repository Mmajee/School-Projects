"""
-------------------------------------------------------
Assignment 3, Task 6
-------------------------------------------------------
"""
from functions import postfix

string = '4 5 + 12 * 2 3 * -'
print(string)
print()
answer = postfix(string)

print('= {}'.format(answer))
