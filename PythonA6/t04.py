"""
-------------------------------------------------------
Assignment 6, Task 4
-------------------------------------------------------
"""
from functions import fraction_product

num1 = int(input('Enter numerator of fraction 1: '))
den1 = int(input('Enter denominator of fraction 1: '))

num2 = int(input('Enter numerator of fraction 2: '))
den2 = int(input('Enter denominator of fraction 2: '))
print()

num, den, product = fraction_product(num1, den1, num2, den2)

print('Product = {}/{}'.format(num, den))
print('Decimal = {:.2f}'.format(product))
