"""
-------------------------------------------------------
Assignment 5, Task 5
-------------------------------------------------------
"""
num_values = int(input('Number of values: '))
print()
value = int(input('First value: '))
total = value
maximum = value
minimum = value
negative = 0
positive = 0
num_zero = 0
even = 0
odd = 0

if value > 0:
    positive += 1
elif value < 0:
    negative += 1
else:
    num_zero += 1

if value % 2 == 0:
    even += 1
else:
    odd += 1


for i in range(num_values - 1):

    value = int(input('Next value: '))

    if value > maximum:
        maximum = value
    elif value < minimum:
        minimum = value

    if value > 0:
        positive += 1
    elif value < 0:
        negative += 1
    else:
        num_zero += 1

    if value % 2 == 0:
        even += 1
    else:
        odd += 1

    total += value


print()
print('Negative values: {:>5d}'.format(negative))
print('Zero values: {:>9d}'.format(num_zero))
print('Positive values: {:>5d}'.format(positive))
print('Even values: {:>9d}'.format(even))
print('Odd values: {:>10d}'.format(odd))
print('Total: {:>15d}'.format(total))
print('Minimum: {:>13d}'.format(minimum))
print('Maximum: {:>13d}'.format(maximum))
avg = total / num_values
print('Average: {:>16.2f}'.format(avg))
