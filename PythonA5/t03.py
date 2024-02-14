"""
-------------------------------------------------------
Assignment 5, Task 3
-------------------------------------------------------
"""
n = int(input('Number (>= 1): '))

Sum = 0
inverse = 0

for i in range(1, n + 1):
    inverse = 1 / (i ** 2)
    Sum += inverse
print()
print('Sum of inverse squares for {} = {}'.format(n, Sum))
