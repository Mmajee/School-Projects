"""
-------------------------------------------------------
Assignment 5, Task 2
-------------------------------------------------------
"""
width = int(input('Width of diamond: '))
char = input('Printing character: ')
print()

if width % 2 != 0:

    for k in range(width - 2, -1, -2):
        print(" " * ((k // 2) + 1), end='')
        print(char * (width - (k + 1)))
else:

    for k in range(width - 1, -1, -2):
        print(" " * ((k // 2) + 1), end='')
        print(char * (width - (k + 1)))


for i in range(-1, width + 1, 2):
    print(" " * ((i // 2) + 1), end='')
    print(char * (width - (i + 1)))
