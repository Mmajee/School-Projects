"""
-------------------------------------------------------
Assignment 3, Task 5
-------------------------------------------------------
"""
from functions import has_balanced_brackets

BALANCED = 0
MORE_LEFT = 1
MORE_RIGHT = 2
MISMATCHED = 3
string = '{a × 2 - [(c - d) × 4]}]'

balanced = has_balanced_brackets(string)

if balanced == BALANCED:
    print("'{}' has balanced brackets.".format(string))
elif balanced == MORE_LEFT:
    print("'{}' has more left side brackets.".format(string))
elif balanced == MORE_RIGHT:
    print("'{}' has more right side brackets.".format(string))
else:
    print("'{}' has mismatched brackets.".format(string))

