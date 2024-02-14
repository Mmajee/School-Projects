"""
-------------------------------------------------------
Assignment 5, Task 1
-------------------------------------------------------
"""
print('Pennyweight to grams Conversion')
start = int(input('Start: '))
limit = int(input('Limit: '))
incr = int(input('Increment: '))
print()
GRAM = 1.5552

print('{}{:>11s}'.format('Pennyweight', 'Grams'))
print('{:-^11s} {:-^10s}'.format('-', '-'))

for i in range(start, limit + 1, incr):
    convert = i * GRAM

    print('{:>11d}{:>11.4f}'.format(i, convert))
