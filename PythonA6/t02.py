"""
-------------------------------------------------------
Assignment 6, Task 2
-------------------------------------------------------
"""
from functions import payment

p = float(input('Amount borrowed: $'))

i = float(input('Interest rate: '))


m = int(input('Length of loan (months): '))

monthly_payment = payment(p, i, m)

print('The monthly payment is ${:,.2f}.'.format(monthly_payment))
