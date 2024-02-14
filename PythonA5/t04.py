"""
-------------------------------------------------------
Assignment 5, Task 4
-------------------------------------------------------
"""
year = int(input('Number of years of rainfall: '))
print()
print('Enter rainfall in cm.')
print()
months = 0
total = 0
for i in range(1, year + 1):
    print('Year {}'.format(i))
    for k in range(1, 13):
        rain = float(input('{:>2s}Month {}: '.format(' ', k)))
        months += 1
        total += rain

avg = total / months
print()
print('Number of months: {}'.format(months))
print('Total rainfall: {:.1f} cm'.format(total))
print('Average rainfall per month: {:.1f} cm'.format(avg))
