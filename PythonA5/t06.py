"""
-------------------------------------------------------
Assignment 5, Task 6
-------------------------------------------------------
"""
start = int(input('Starting value for table: '))
End = int(input('Ending value for table: '))
print()
print('{:>5s}'.format(' '), end='')

for i in range(start, End + 1):
    print('{:>5d}'.format(i), end='')
print()
print('{:>5s}'.format(' '), end='')
for i in range(start, End + 1):
    print('{:-^5s}'.format('-'),  end='')
print()
for i in range(start, End + 1):
    print(' {:>2d} |'.format(i), end='')
    for k in range(start, End + 1):
        print('{:>5d}'.format(k * i), end='')
    print()
