"""
-------------------------------------------------------
Assignment 6, Task 7
-------------------------------------------------------
"""
from functions import hours_required
from functions import paint_cost
from functions import paint_required
from functions import wall_area


print('Enter paint and labour standards:')
area = int(input('Standard wall area (sq ft / gallon): '))
area_per_hour = int(input('Area painted per hour (sq ft / hour): '))
labour_charges = int(input('Labour charges ($ / hour): '))
print()

print('Enter customer information: ')
cost = int(input('Cost of paint (1 gallon): $'))
height = int(input('Height of wall (ft): '))
width = int(input('Width of wall (ft): '))
print()

standard_area = wall_area(width, height)

total_paint = paint_required(area, standard_area)

hours = hours_required(area, area_per_hour)

pc = paint_cost(total_paint, cost)

print('Paint required: {} gallons'.format(total_paint))

print('Hours labour required: {} hours'.format(hours))

print('Paint cost:  ${:>9.2f}'.format(pc))
print('Labour cost: ${:>9.2f}'.format(labour_charges * hours))
print('{:>13s}{:-^10s}'.format(' ', '-'))
print('Total cost:  ${:>9.2f}'.format(pc + (labour_charges * hours)))
